# certbot-dns-myloc

---

## Table of Contents
- [Installation](#installation)
- [Named Arguments](#arguments)
- [Credentials](#credentials)
- [Retrieving an API Token](#get-api-token)
- [Examples](#examples)
- [Legal Disclaimer](#legal-disclaimer)
- [Contributing](#contributing)
- [License](#license)

---

[myLoc](https://myloc.de) DNS authenticator plugin for
[Certbot](https://certbot.eff.org/).

This plugin automates the process of completing a dns-01 challenge by
creating, and subsequently removing, TXT records using the [myLoc
API](https://apidoc.myloc.de/).

<a name="installation"></a>
## Installation

    pip install certbot-dns-myloc

<a name="arguments"></a>
## Named Arguments

To start using DNS authentication for myLoc, pass the following
arguments on certbot\'s command line:

| Option                              | Description                                                                                             |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------|
| `--authenticator dns-myloc`         | Select the authenticator plugin (Required)                                                              |
| `--dns-myloc-credentials`           | myLoc Remote User credentials INI file (Required)                                                       |
| `--dns-myloc-propagation-seconds`   | Waiting time for DNS to propagate before asking the ACME server to verify the DNS record. (Default: 10) |

<a name="credentials"></a>
## Credentials

An example `myloc.ini` file:

``` ini
dns_myloc_api_token = <api token>
dns_myloc_brand = <myloc|webtropia|servdiscount>
```

The path to this file can be provided interactively or using the
`--dns-myloc-credentials` command-line argument. Certbot records the
path to this file for use during renewal, but does not store the file\'s
contents, so if you at some point change the directory of the file make 
sure your renewal configs are changed too.

Please make sure that this file can only be accessed by your user.

<a name="get-api-token"></a>
## Retrieving an API Token

Go into the appropriate ZKM API management of your myLoc brand:

-   [myLoc API management](https://zkm.myloc.de/s/api/)
-   [webtropia API management](https://zkm.webtropia.com/s/api/)
-   [servdiscount API management](https://zkm.servdiscount.com/s/api/)

Click "Create" in the dashboard and set a wanted expiry date of the
token and only give it *API_DNS_READ* and *API_DNS_WRITE* so the
token can only manage your DNS zones.

If you cant access the API management and get send to the normal
customer overview please create a support ticket to request API access.

<a name="examples"></a>
## Examples

These examples assume you have a `~/.secrets/certbot/myloc.ini` file with your [credentials](#credentials) set.

    certbot certonly --authenticator dns-myloc --dns-myloc-credentials ~/.secrets/certbot/myloc.ini -d example.com

<a name="legal-disclaimer"></a>
## Legal Disclaimer

The use of this Certbot plugin is at your own risk. The authors and
maintainers of this plugin are not responsible for any damages, losses,
or issues that may arise from its use. By using this plugin, you
acknowledge and agree to this disclaimer.

<a name="contributing"></a>
## Contributing

If you would like to contribute to this Certbot plugin, feel free to
fork the repository, make your changes, and submit a pull request.

<a name="license"></a>
## License

This Certbot plugin is open-source software, and its use is governed by
the terms of its respective license. Please refer to the
[LICENSE](LICENSE) file in the repository for licensing information.
The legal disclaimer has been added under the Legal Disclaimer
section to make it clear
