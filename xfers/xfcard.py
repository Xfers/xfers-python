from xfers import api_resource
from xfers import error


RESOURCE_URL = '/cards'


def list_all(user_api_token):
    params = {'user_api_token': user_api_token}
    return api_resource.get(params, RESOURCE_URL, None)


def add(params):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.post(params, RESOURCE_URL, None)


def delete(card_id, user_api_token):
    if not card_id:
        raise error.InvalidRequestError("Card id cannot be empty", 400)
    if not user_api_token:
        raise error.InvalidRequestError("user_api_token cannot be empty", 400)
    params = {'user_api_token': user_api_token}
    return api_resource.delete('{}/{}'.format(RESOURCE_URL, card_id), None, params)


def set_default(card_id, user_api_token):
    if not card_id:
        raise error.InvalidRequestError("Card id cannot be empty", 400)
    if not user_api_token:
        raise error.InvalidRequestError("user_api_token cannot be empty", 400)
    params = {'user_api_token': user_api_token}
    return api_resource.post(params, '{}/{}/set_default'.format(RESOURCE_URL, card_id), None)


def charge_guest(params):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.post(params, '/credit_card_charges/charge_card_guest', None)


def charge_existing(card_id):
    if not card_id:
        raise error.InvalidRequestError("Card id cannot be empty", 400)
    params = {'txn_id': card_id}
    return api_resource.post(params, '/credit_card_charges/charge_card', None)
