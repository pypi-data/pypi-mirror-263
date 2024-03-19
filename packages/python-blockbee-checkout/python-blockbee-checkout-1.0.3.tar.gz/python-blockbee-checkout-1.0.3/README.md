[<img src="https://blockbee.io/static/assets/images/blockbee_logo_nospaces.png" width="300"/>](image.png)


# BlockBee's Python Library
Python implementation of BlockBee's payment gateway

##  Deprecated! It has been integrated into [python-blockbee](https://github.com/blockbee-io/python-blockbee).

## Requirements:

```
Python >= 3.0
Requests >= 2.20
```

## Install

```shell script
pip install python-blockbee-checkout
```

[on pypi](https://pypi.python.org/pypi/python-blockbee-checkout)
or
[on GitHub](https://github.com/blockbee-io/python-blockbee-checkout)

## Usage

### Importing in your project file

```python
from BlockBee import BlockBeeCheckoutHelper
```

### Generate a Payment Checkout page

```python
from BlockBee import BlockBeeCheckoutHelper

bb = BlockBeeCheckoutHelper(api_key, params, bb_params)

payment_page = bb.payment_request(redirect_url, value)
```

Where:

* ``api_key`` is the API Key provided by our [Dashboard](https://dash.blockbee.io/).
* ``params`` is any parameter you wish to send to identify the payment, such as `{'order_id': 1234}`.
* ``bb_params`` parameters that will be passed to BlockBee _(check which extra parameters are available here: https://docs.blockbee.io/#operation/create).
* ``redirect_url`` URL in your platform, where the user will be redirected to following the payment. Should be able to process the payment using the `success_token`.
* ``value`` amount in currency set in Payment Settings you want to receive from the user.

### Getting notified when the user completes the Payment
> When receiving payments, you have the option to receive them in either the ``notify_url`` or the ``redirect_url``, but adding the ``redirect_url``  is required (refer to our documentation at https://docs.blockbee.io/#operation/paymentipn).

### Requesting Deposit
```python
from BlockBee import BlockBeeCheckoutHelper

bb = BlockBeeCheckoutHelper(api_key, params, bb_params)

deposit_page = bb.deposit_request(notify_url)
```

* ``api_key`` is the API Key provided by our [Dashboard](https://dash.blockbee.io/).
* ``params`` is any parameter you wish to send to identify the payment, such as `{'order_id': 1234}`.
* ``bb_params`` parameters that will be passed to BlockBee _(check which extra parameters are available here: https://docs.blockbee.io/#operation/deposit).
* ``notify_url`` URL in your platform, where the IPN will be sent notifying that a deposit was done. Parameters are available here: https://docs.blockbee.io/#operation/depositipn.

### Getting notified when the user makes a deposit
> When receiving deposits, you must provide a ``notify_url`` where our system will send an IPN every time a user makes a deposit (refer to our documentation at https://docs.blockbee.io/#operation/depositipn).

## Help

Need help?  
Contact us @ https://blockbee.io/contacts/


### Changelog

#### 1.0.0
* Initial Release

#### 1.0.1
* Minor bugfixes

#### 1.0.2
* Minor bugfixes