from xfers import api_resource
from xfers import error


RESOURCE_URL = '/user'


def retrieve(connect_key=None):
    return api_resource.get(RESOURCE_URL, connect_key)


def update(params=None, connect_key=None):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.put(params, RESOURCE_URL, connect_key)


def transfer_info(connect_key=None):
    return api_resource.get(RESOURCE_URL + '/transfer_info', connect_key)


def activities(connect_key=None):
    return api_resource.get(RESOURCE_URL + '/activities', connect_key)['activities']
