"""DNS Authenticator for myLoc."""
import logging
import os
import httpx
from certbot import errors
from certbot.plugins import dns_common
from certbot.plugins.dns_common import CredentialsConfiguration
from typing import Any
from typing import Callable
from typing import Dict
from typing import List
from typing import Optional
from certbot_dns_myloc.version import __version__

logger = logging.getLogger(__name__)

ACME_TTL: int = 60
MYLOC_API_FRONTEND_URLS: str = ' - https://zkm.myloc.de/s/api/token\n' + \
                          ' - https://zkm.webtropia.com/s/api/token\n' + \
                          ' - https://zkm.servdiscount.com/s/api/token\n'
MYLOC_API_URLS: Dict[str, str] = {
    'myloc': 'https://zkm.myloc.de/api',
    'webtropia': 'https://zkm.webtropia.com/api',
    'servdiscount': 'https://zkm.servdiscount.com/api',
}


class Authenticator(dns_common.DNSAuthenticator):
    """DNS Authenticator for myLoc

    This Authenticator uses the myLoc API to fulfill a dns-01 challenge.
    """

    description = 'Obtain certificates using a DNS TXT record (if you are using myLoc for DNS).'

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.credentials: Optional[CredentialsConfiguration] = None

    @classmethod
    def add_parser_arguments(cls, add: Callable[..., None],
                             default_propagation_seconds: int = 10) -> None:
        super().add_parser_arguments(add, default_propagation_seconds)
        add('credentials', help='myLoc credentials INI file.')

    def more_info(self) -> str:
        return 'This plugin configures a DNS TXT record to respond to a dns-01 challenge using ' + \
            'the myLoc API.'

    def _validate_credentials(self, credentials: CredentialsConfiguration) -> None:
        brand = credentials.conf('brand')

        if brand not in MYLOC_API_URLS.keys():
            raise errors.PluginError('{}: brand can only be one of the following brands: {}'
                                     .format(credentials.confobj.filename, ', '.join(MYLOC_API_URLS.keys())))

    def _setup_credentials(self) -> None:
        self.credentials = self._configure_credentials(
            'credentials',
            'myLoc credentials INI file',
            {
                'api_token': 'myLoc API Token from one of the following ZKMs:\n{}'.format(MYLOC_API_FRONTEND_URLS),
                'brand': 'myLoc brand ({})'.format(', '.join(MYLOC_API_URLS.keys()))
            },
            self._validate_credentials
        )
        self._get_myloc_client().validate_token()

    def _perform(self, domain: str, validation_name: str, validation: str) -> None:
        self._get_myloc_client().add_txt_record(domain, validation_name, validation, ACME_TTL)

    def _cleanup(self, domain: str, validation_name: str, validation: str) -> None:
        self._get_myloc_client().del_txt_record(domain, validation_name, validation)

    def _get_myloc_client(self) -> "_MyLocClient":
        if not self.credentials:
            raise errors.Error("Plugin has not been prepared.")

        return _MyLocClient(self.credentials.conf('api_token'), self.credentials.conf('brand'))


class _MyLocClient:
    """
    Encapsulates all communication with the myLoc API.
    """

    def __init__(self, api_token: str, brand: str) -> None:
        self.api = httpx.Client(
            base_url=MYLOC_API_URLS[brand],
            headers={
                'Authorization': 'Bearer {}'.format(api_token),
                'User-Agent': 'Certbot-myLoc-Authenticator {}'.format(__version__),
                'Accept': 'application/json',
            }
        )

    def validate_token(self):
        response = self.api.request('GET', '/token/validate')
        logger.debug('myLoc API: /token/validate response: %s', response.text)

        if response.status_code == 200:
            response_json = response.json()
            scopes: List[str] = response_json['content']['scope']

            if 'API_DNS_WRITE' not in scopes \
                    and 'API_CUSTOMER_FULL_ACCESS' not in scopes:
                raise errors.PluginError('myLoc Authenticator: the provided api_token doesn\'t have the API_DNS_WRITE '
                                         'or API_CUSTOMER_FULL_ACCESS scope.')
        else:
            raise errors.PluginError('myloc Authenticator: Validation request returned non 200 response. Returned status {}: '
                                     .format(response.status_code, response.text))

    def add_txt_record(self, domain: str, record_name: str, record_content: str, record_ttl: int) -> None:
        record = {
            'type': 'TXT',
            'name': record_name,
            'content': record_content,
            'ttl': record_ttl
        }

        logger.debug('myLoc API: Attempting to add record to zone %s: %s', domain, record)
        response = self.api.request('PUT', '/dns/zone/{}'.format(domain), data=record)

        if response.status_code == 204:
            logger.debug('myLoc API: Successfully added TXT record to zone %s.', domain)
        else:
            logger.warning('myLoc API: Failed to add TXT record to zone %s. status %s: %s', domain, response.status_code, response.text)
            raise errors.PluginError('myLoc API: Failed to add TXT record to zone {}.'.format(domain))

    def del_txt_record(self, domain: str, record_name: str, record_content: str) -> None:
        record = {
            'type': 'TXT',
            'name': record_name,
            'content': record_content
        }

        logger.debug('myLoc API: Attempting to delete record from zone %s: %s', domain, record)
        response = self.api.request('DELETE', '/dns/zone/{}'.format(domain), data=record)

        if response.status_code == 204:
            logger.debug('myLoc API: Successfully deleted TXT record from zone %s.', domain)
        else:
            logger.warning('myLoc API: Failed to delete TXT record to zone %s. status %s: %s', domain, response.status_code, response.text)
