import xfers
from xfers import xfconnect
from xfers import error

xfers.set_sg_sandbox()
XFERS_APP_API_KEY = 'AeWpKz5cdPoJFUwF53sBee_WsSoqym_hspiX3bcoB_Y'


try:
    print 'Authorizing connect...'
    params = {
        'phone_no': '+6597288608',
        'signature': 'a4f001729fe3accdbb0d9cfaf3b49b0678a4c91b'
    }
    resp = xfconnect.authorize(params, XFERS_APP_API_KEY)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Getting token...'
    params = {
        'otp': '541231',
        'phone_no': '+6597288608',
        'signature': '132e60cc2b6076824fac1ac4c1bb6b47cc3f9036',
        'return_url': 'https://mywebsite.com/api/v3/account_registration/completed'
    }
    resp = xfconnect.get_token(params, XFERS_APP_API_KEY)
    print resp
except error.XfersError as e:
    print str(e)
