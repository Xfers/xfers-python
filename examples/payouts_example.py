import xfers
from xfers import xfpayout
from xfers import error

xfers.api_key = 'G-zsfAEScrqdU8GhWTEdjfdnb3XRdU8q1fH-nuWfSzo'
xfers.set_sg_sandbox()

payout_id = ''

try:
    print 'Creating payout...'
    params = {
        'amount': '0.84',
        'invoice_id': 'SPA-MEMBERSHIP',
        'recipient': 'demo@xfers.io'
    }
    resp = xfpayout.create(params)
    payout_id = resp['id']
    print payout_id
    print resp['recipient']
    print resp['invoice_id']
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Retrieving payout {}...'.format(payout_id)
    resp = xfpayout.retrieve(payout_id)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Listing all payouts...'
    params = {
        'recipient': '+6597288608'
    }
    payouts = xfpayout.list_all(params)
    for payout in payouts:
        print 'Payout: {}'.format(payout)
except error.XfersError as e:
    print str(e)
