from rest_framework.views import exception_handler
from rest_framework.response import Response


def handler(exc, context):
    # 4xx errors are handled by default
    response = exception_handler(exc, context)
    if response is None:
        response = Response({}, status=500)

    response.data['code'] = '1001'

    return response
