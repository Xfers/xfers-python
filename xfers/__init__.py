# Xfers Python bindings
# API docs at http://docs.xfers.io/

# Configuration variables

api_key = None
api_base = ''

SG_SANDBOX_BASE = 'https://sandbox.xfers.io/api/v3'
SG_PRODUCTION_BASE = 'https://www.xfers.io/api/v3'
ID_SANDBOX_BASE = 'https://sandbox-id.xfers.com/api/v3'
ID_PRODUCTION_BASE = 'https://id.xfers.com/api/v3'


def set_sg_sandbox():
    global api_base
    api_base = SG_SANDBOX_BASE


def set_sg_production():
    global api_base
    api_base = SG_PRODUCTION_BASE


def set_id_sandbox():
    global api_base
    api_base = ID_SANDBOX_BASE


def set_id_production():
    global api_base
    api_base = ID_PRODUCTION_BASE
