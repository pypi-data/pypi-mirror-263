from rest_framework.exceptions import APIException


class InvalidDateParams(APIException):
    status_code = 422
    default_code = 'invalid_date'
    default_detail = 'Invalid date params.'


class ReportUpdating(APIException):
    status_code = 204


class DontHaveReportData(APIException):
    status_code = 406
    default_detail = 'Dont have reports for this integration'


class InvalidFieldsParam(APIException):
    status_code = 422
    default_code = 'invalid_fields'
    default_detail = 'Invalid fields param, fields must be a list'


class NotDataEverException(APIException):
    status_code = 400
    default_code = 'no data'
    default_detail = 'no data ever'


class NotDataException(APIException):
    status_code = 205
    default_code = 'no data'
    default_detail = 'no data for this params'
