from xfers import api_resource
from xfers import error


RESOURCE_URL = '/payouts'


def retrieve(payout_id, connect_key=None):
    if not payout_id:
        raise error.InvalidRequestError("Payout id cannot be empty", 400)
    return api_resource.get(None, '{}/{}'.format(RESOURCE_URL, payout_id), connect_key)


def list_all(params=None, connect_key=None):
    return api_resource.get(params, RESOURCE_URL, connect_key)


def create(params, connect_key=None):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.post(params, RESOURCE_URL, connect_key)
