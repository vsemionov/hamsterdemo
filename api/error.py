from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError, NotFound


class HamsterException(Exception):
    def __init__(self, status, code):
        self.status = status
        self.code = code


def handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        # 4xx errors are already handled
        if isinstance(exc, ValidationError):
            response.data['code'] = 'invalid_request'
        elif isinstance(exc, NotFound):
            response.data['code'] = 'not_found'
        else:
            response.data['code'] = 'client_error'
    elif isinstance(exc, HamsterException):
        response = Response({'code': exc.code}, status=exc.status)
    else:
        response = Response({'code': 'internal_error'}, status=500)

    return response
