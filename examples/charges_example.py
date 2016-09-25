import xfers
from xfers import xfcharge
from xfers import error
import json

xfers.api_key = 'dLyFBBNxQx5bQzeyjyUbibapmnD5xEcNB5MoZdx9Kow'
xfers.set_sg_sandbox()

charge_id = ''

try:
    print 'Listing all charges...'
    params = {
        'limit': '5'
    }
    charges = xfcharge.list_all(params)
    for charge in charges:
        print 'Charge: {}'.format(charge)
except error.XfersError as e:
    print str(e)


try:
    print 'Creating charge...'
    items = [{'description': 'Red dress size M', 'price': '9.99', 'quantity': '1', 'name': 'Red dress'}]
    meta_data = {'firstname': 'Tianwei', 'lastname': 'Liu'}
    params = {
        'amount' : '9.99',
        'currency' : 'SGD',
        'notify_url' : 'https://mysite.com/payment_notification',
        'return_url' : 'https://mysite.com/return',
        'cancel_url' : 'https://mysite.com/cancel',
        'order_id' : 'your-order-id',
        'description' : 'unused red dress',
        'shipping' : '2.50',
        'tax' : '0.0',
        'items' : json.dumps(items),
        'meta_data' : json.dumps(meta_data)
    }
    resp = xfcharge.create(params)
    charge_id = resp['id']
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Retrieving charge {}...'.format(charge_id)
    resp = xfcharge.retrieve(charge_id)
    print resp
except error.XfersError as e:
    print str(e)


try:
    params = {
        'order_id': 'A012312',
        'total_amount': '12.49',
        'status': 'paid',
        'currency': 'SGD'
    }
    print 'Validating charge {}...'.format(charge_id)
    resp = xfcharge.validate(charge_id, params)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Cancelling charge {}...'.format(charge_id)
    resp = xfcharge.cancel(charge_id)
    print resp
except error.XfersError as e:
    print str(e)


try:
    charge_id = 'your-charge-id'
    print 'Settling charge {}...'.format(charge_id)
    resp = xfcharge.settle(charge_id, '512312')
    print resp
except error.XfersError as e:
    print str(e)


try:
    charge_id = 'your-charge-id'
    print 'Refunding charge {}...'.format(charge_id)
    resp = xfcharge.refund(charge_id)
    print resp
except error.XfersError as e:
    print str(e)
