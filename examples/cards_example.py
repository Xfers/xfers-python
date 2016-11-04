import xfers
from xfers import xfcard
from xfers import error

xfers.api_key = 'WuTp3zM7UEpmUkeAyGPxRHmnXAx-hXJ7jzdqmxY6S1o'
xfers.set_sg_sandbox()

# Get the following user_api_token from http://docs.xfers.io/#xfers-connect
# you should have one user_api_token for every user you wish to add a credit card to.
user_api_token = 'osEdbc8uzxY5vaXA-oe-7E86sVWCYTCVPuHQyFQ-uPQ'


try:
    print 'Listing all cards...'
    cards = xfcard.list_all(user_api_token)
    for card in cards:
        print 'Card: {}'.format(card)
except error.XfersError as e:
    print str(e)


try:
    print 'Adding card...'
    params = {
        'user_api_token': user_api_token,
        'credit_card_token': 'tok_19C22fB8MXWbQJDjSx4Ek9Wk',  # gotten from http://docs.xfers.io/#xfers-tokenize
        'first6': '424242',
        'last4': '4242'
    }
    resp = xfcard.add(params)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Deleting card'
    card_id = 'card_19BhF9I7jGeCrIKD1ICQ6snN'
    resp = xfcard.delete(card_id, user_api_token)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Setting default card'
    card_id = 'card_196kDPI7jGeCrIKDlgVDBvER'
    resp = xfcard.set_default(card_id, user_api_token)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Charge guest card'
    charge_id = 'f0fbdd1c16b44deba3f15cc11a29fefc'  # you must create a charge first
    params = {
        'txn_id': charge_id,
        'credit_card_token': 'tok_19C5hlB8MXWbQJDjT6HAsM3A',  # gotten from http://docs.xfers.io/#xfers-tokenize
        'first6': '424242',
        'last4': '4242'
    }
    resp = xfcard.charge_guest(params)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Charge existing card'
    # You must add a credit card with xfcard.add before this
    charge_id = '59290c99da0044b398445c24a63d5cf7'  # you must create a charge first with user_api_token of your user
    resp = xfcard.charge_existing(charge_id)
    print resp
except error.XfersError as e:
    print str(e)
