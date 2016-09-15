import xfers
from xfers import xfcharge
from xfers import error

xfers.api_key = 'G-zsfAEScrqdU8GhWTEdjfdnb3XRdU8q1fH-nuWfSzo'
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
    params = {
        'amount': '19.99',
        'currency': 'SGD',
        'order_id': 'A01231z2',
        'description': 'Carousell user - Konsolidate'
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
