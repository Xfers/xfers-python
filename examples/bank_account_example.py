import xfers
from xfers import xfbankaccount
from xfers import error

xfers.api_key = 'G-zsfAEScrqdU8GhWTEdjfdnb3XRdU8q1fH-nuWfSzo'
xfers.set_sg_sandbox()

try:
    print 'Adding bank account...'
    params = {
        'account_no': '12988012511',
        'bank': 'OCBC'
    }
    bank_accounts = xfbankaccount.add(params)
    for bank_account in bank_accounts:
        print 'Bank account: {}'.format(bank_account)
except error.XfersError as e:
    print str(e)

try:
    print 'Adding bank account...'
    params = {
        'account_no': '03931234321',
        'bank': 'DBS'
    }
    bank_accounts = xfbankaccount.add(params)
    for bank_account in bank_accounts:
        print 'Bank account: {}'.format(bank_account)
except error.XfersError as e:
    print str(e)

try:
    print 'Listing all bank_accounts...'
    bank_accounts = xfbankaccount.list_all()
    for bank_account in bank_accounts:
        print 'Bank account: {}'.format(bank_account)
except error.XfersError as e:
    print str(e)


try:
    print 'Deleting bank account {}...'.format('17')
    resp = xfbankaccount.delete('17')
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Updating bank account {}...'.format('18')
    params = {
        'account_no': '209367866',
        'bank': 'POSB'
    }
    resp = xfbankaccount.update('18', params)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Withdrawing from bank account {}...'.format('18')
    params = {
        'amount': '20',
        'express': 'false'
    }
    resp = xfbankaccount.withdraw('18', params)
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Listing withdrawal requests...'
    params = {
        'filter': 'pending'
    }
    withdrawal_requests = xfbankaccount.withdrawal_requests(params)
    for request in withdrawal_requests:
        print 'Withdrawal request: {}'.format(request)
except error.XfersError as e:
    print str(e)
