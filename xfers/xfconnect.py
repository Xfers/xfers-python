from xfers import api_resource
from xfers import error


RESOURCE_URL = '/authorize'


def authorize(params, connect_key=None):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.post(params, '{}/signup_login'.format(RESOURCE_URL), connect_key)


def get_token(params, connect_key=None):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.get(params, '{}/get_token'.format(RESOURCE_URL), connect_key)
