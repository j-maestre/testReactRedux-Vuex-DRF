from rest_framework.exceptions import APIException


class TravelDoesNotExist(APIException):
    status_code = 400
    default_detail = 'The requested travel does not exist.'
