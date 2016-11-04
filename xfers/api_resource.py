import requests
import xfers
import json
from error import (XfersError, InvalidRequestError, AuthenticationError, InternalServerError)


def create_auth_headers(connect_key):
    if connect_key:
        return {'X-XFERS-APP-API-KEY': connect_key}
    else:
        return {'X-XFERS-USER-API-KEY': xfers.api_key}


def handle_api_error(msg, status_code):
    if status_code == 400:
        raise InvalidRequestError(msg, status_code)
    elif status_code == 401:
        raise AuthenticationError(msg, status_code)
    elif status_code == 500:
        raise InternalServerError(msg, status_code)
    else:
        raise XfersError(msg, status_code)


def get(params, resource_url, connect_key):
    url = xfers.api_base + resource_url
    r = requests.get(url, headers=create_auth_headers(connect_key), params=params)
    if r.status_code != 200:
        handle_api_error(r.text, r.status_code)
    return json.loads(r.text)


def post(params, resource_url, connect_key):
    url = xfers.api_base + resource_url
    r = requests.post(url, headers=create_auth_headers(connect_key), data=params)
    if r.status_code != 200:
        handle_api_error(r.text, r.status_code)
    return json.loads(r.text)


def put(params, resource_url, connect_key):
    url = xfers.api_base + resource_url
    r = requests.put(url, headers=create_auth_headers(connect_key), data=params)
    if r.status_code != 200:
        handle_api_error(r.text, r.status_code)
    return json.loads(r.text)


def delete(resource_url, connect_key, params=None):
    url = xfers.api_base + resource_url
    r = requests.delete(url, headers=create_auth_headers(connect_key), data=params)
    if r.status_code != 200:
        handle_api_error(r.text, r.status_code)
    return json.loads(r.text)

