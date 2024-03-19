# Python bitget API Library

[bitget](https://www.bitget.com/en/referral/register?from=referral&clacCode=6EKP94LE) is a cryptocurrency derivatives exchange.

This is a wrapper around the Bitget API as described on Bitget, including all features the API provides using clear and readable objects, both for the REST  as the websocket API.

# Get Started and Documentation

* [Register an account with Bitget.](https://partner.bitget.com/bg/e55g05831674816745836)
* [Generate an API Key and assign relevant permissions.](https://www.bitget.com/en/support/articles/360038968251-API%20Creation%20Guide)
* [Bitget API docs](https://bitgetlimited.github.io/apidoc/en/mix/#welcome)
  * [Example Bitget rest API](https://github.com/cuongitl/python-bitget/blob/master/examples/example_rest_api.py)
  * [Example Bitget websocket API](https://github.com/cuongitl/python-bitget/blob/master/examples/example_websocket_api.py)

# Install

Exécute pip commande: 

```
pip install PybitgetApi
```

# Usage

> Change your API KEY and your SECRET KEY.

### Restful Api Sample Code

```python
from PybitgetApi import Client

api_key = "your-api-key"
api_secret = "your-secret-key"
api_passphrase = "your-api-passphrase"

client = Client(api_key, api_secret, passphrase=api_passphrase)
result = client.mix_get_accounts(productType='UMCBL')
print(result)
```
