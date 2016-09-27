import xfers
from xfers import xfintent
from xfers import error

xfers.api_key = 'G-zsfAEScrqdU8GhWTEdjfdnb3XRdU8q1fH-nuWfSzo'
xfers.set_sg_sandbox()

intent_id = ''

try:
    print 'Creating intent...'
    params = {
        'amount': '1.49',
        'currency': 'SGD',
        'bank': 'DBS',
        'request_id': 'YOUR-CUSTOM-REQUEST-ID',
        'notify_url': 'https://mysite.com/topup_notification'
    }
    resp = xfintent.create(params)
    intent_id = resp['id']
    print intent_id
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Current intent...'
    intent = xfintent.retrieve()
    print 'Intent: {}'.format(intent)
except error.XfersError as e:
    print str(e)


try:
    print 'Cancelling intent {}...'.format(intent_id)
    resp = xfintent.cancel(intent_id)
    print resp
except error.XfersError as e:
    print str(e)
