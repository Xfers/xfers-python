from xfers import api_resource
from xfers import error


RESOURCE_URL = '/charges'


def retrieve(charge_id, connect_key=None):
    if not charge_id:
        raise error.InvalidRequestError("Charge id cannot be empty", 400)
    return api_resource.get(None, '{}/{}'.format(RESOURCE_URL, charge_id), connect_key)


def list_all(params=None, connect_key=None):
    return api_resource.get(params, RESOURCE_URL, connect_key)


def create(params, connect_key=None):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.post(params, RESOURCE_URL, connect_key)


def refund(charge_id, connect_key=None):
    if not charge_id:
        raise error.InvalidRequestError("Charge id cannot be empty", 400)
    return api_resource.post(None, '{}/{}/refunds'.format(RESOURCE_URL, charge_id), connect_key)


def validate(charge_id, params, connect_key=None):
    if not charge_id:
        raise error.InvalidRequestError("Charge id cannot be empty", 400)
    return api_resource.post(params, '{}/{}/validate'.format(RESOURCE_URL, charge_id), connect_key)


def cancel(charge_id, connect_key=None):
    if not charge_id:
        raise error.InvalidRequestError("Charge id cannot be empty", 400)
    return api_resource.post(None, '{}/{}/cancel'.format(RESOURCE_URL, charge_id), connect_key)


def authorize(charge_id, auth_code):
    if not charge_id:
        raise error.InvalidRequestError("Charge id cannot be empty", 400)
    if not auth_code:
        raise error.InvalidRequestError("auth_code cannot be empty", 400)

    params = {'auth_code': auth_code}
    return api_resource.post(params, '{}/{}/authorize'.format(RESOURCE_URL, charge_id), None)
