from xfers import api_resource
from xfers import error


RESOURCE_URL = '/intents'


def list_all(connect_key=None):
    return api_resource.get(None, RESOURCE_URL, connect_key)


def create(params, connect_key=None):
    if not params:
        raise error.InvalidRequestError("Params cannot be empty", 400)
    return api_resource.post(params, RESOURCE_URL, connect_key)


def cancel(intent_id, connect_key=None):
    if not intent_id:
        raise error.InvalidRequestError("Intent id cannot be empty", 400)
    return api_resource.post(None, '{}/{}/cancel'.format(RESOURCE_URL, intent_id), connect_key)
