class XfersError(Exception):

    def __init__(self, message=None, http_status=None):
        self.message = message
        self.http_status = http_status

    def __str__(self):
        return "{} ---- Body: {}\t Code: {}".format(type(self).__name__, self.message, self.http_status)


class InvalidRequestError(XfersError):
    pass


class AuthenticationError(XfersError):
    pass


class InternalServerError(XfersError):
    pass
