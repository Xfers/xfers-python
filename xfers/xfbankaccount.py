from xfers import api_resource
from xfers import error


RESOURCE_URL = '/user/bank_account'


def list_all(connect_key=None):
    return api_resource.get(None, RESOURCE_URL, connect_key)


def add(params, connect_key=None):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.post(params, RESOURCE_URL, connect_key)


def update(bank_account_id, params, connect_key=None):
    if not bank_account_id or not params:
        raise error.InvalidRequestError("Bank account id and params cannot be empty", 400)
    return api_resource.put(params, '{}/{}'.format(RESOURCE_URL, bank_account_id), connect_key)


def delete(bank_account_id, connect_key=None):
    if not bank_account_id:
        raise error.InvalidRequestError("Bank account id cannot be empty", 400)
    return api_resource.delete('{}/{}'.format(RESOURCE_URL, bank_account_id), connect_key)


def withdraw(bank_account_id, params, connect_key=None):
    if not bank_account_id or not params:
        raise error.InvalidRequestError("Bank account id and params cannot be empty", 400)
    return api_resource.post(params, '{}/{}/withdraw'.format(RESOURCE_URL, bank_account_id), connect_key)


def withdrawal_requests(params=None, connect_key=None):
    return api_resource.get(params, '{}/withdrawal_requests'.format(RESOURCE_URL), connect_key)['withdrawal_requests']
