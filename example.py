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


try:
    print 'Updating user...'
    params = {
        'first_name': 'Yan Yi',
        'last_name': 'Seow',
        'email': 'jelly@xfers.io',
        'date_of_birth': '1986-02-27',
        'address_line_1': 'Blk 608 Jurong East',
        'address_line_2': '#08-41',
        'nationality': 'Singaporean',
        'postal_code': '510608',
        'identity_no': 'S8692038G',
        'id_front_url': 'http://angelsgateadvisory.sg/wp-content/uploads/2015/10/Logo.jpg',
        'id_back_url': 'http://angelsgateadvisory.sg/wp-content/uploads/2015/10/Logo.jpg',
        'selfie_2id_url': 'http://angelsgateadvisory.sg/wp-content/uploads/2015/10/Logo.jpg',
        'proof_of_address_url': 'http://angelsgateadvisory.sg/wp-content/uploads/2015/10/Logo.jpg',
        'meta_data': 'foobar'
    }
    resp = xfuser.update(params)
    print resp['first_name']
    print resp['last_name']
    print resp['available_balance']
    print resp['address_line_1']
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Getting transfer info...'
    resp = xfuser.transfer_info()
    print resp
except error.XfersError as e:
    print str(e)


try:
    print 'Getting activities...'
    activities = xfuser.activities()
    for activity in activities:
        print activity
except error.XfersError as e:
    print str(e)
