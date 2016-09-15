# Xfers Python bindings

You can sign up for a Xfers account at https://xfers.com.

## Installation

You don't need this source code unless you want to modify the
package. If you just want to use the Xfers Python bindings, you
should run:

    pip install --upgrade xfers

or

    easy_install --upgrade xfers

See http://www.pip-installer.org/en/latest/index.html for instructions
on installing pip. If you are on a system with easy_install but not
pip, you can use easy_install instead. If you're not using virtualenv,
you may have to prefix those commands with `sudo`. You can learn more
about virtualenv at http://www.virtualenv.org/

To install from source, run:

    python setup.py install

## Getting Started

Simple usage looks like:

```python
import xfers
from xfers import xfuser
from xfers import error

xfers.api_key = 'G-zsfAEScrqdU8GhWTEdjfdnb3XRdU8q1fH-nuWfSzo'
xfers.set_sg_sandbox()


try:
    print 'Retrieving user...'
    resp = xfuser.retrieve()
    print resp['first_name']
    print resp['last_name']
    print resp['available_balance']
    print resp['address_line_1']
    bank_accounts = resp['bank_accounts']
    for account in bank_accounts:
        print 'Bank account: {}'.format(account)
    print resp
except error.XfersError as e:
    print str(e)
```

## Documentation

Please see http://docs.xfers.io/ for up-to-date documentation.