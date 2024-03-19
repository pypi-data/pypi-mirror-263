# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.http.api_response import ApiResponse
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from verizon.models.security_success_result import SecuritySuccessResult
from verizon.exceptions.security_result_exception import SecurityResultException


class SIMSecureForIoTLicensesController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(SIMSecureForIoTLicensesController, self).__init__(config)

    def assign_license_to_devices(self,
                                  body,
                                  x_request_id=None):
        """Does a POST request to /v1/devices/license/actions/assign.

        Assigns SIM-Secure for IoT licenses to SIMs.

        Args:
            body (AssignLicenseRequest): Request to assign license to
                devices.
            x_request_id (str, optional): Transaction Id.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success
                response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.M2M)
            .path('/v1/devices/license/actions/assign')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('X-Request-ID')
                          .value(x_request_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SecuritySuccessResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request.', SecurityResultException)
            .local_error('401', 'Unauthorized request.', SecurityResultException)
            .local_error('403', 'Request Forbidden.', SecurityResultException)
            .local_error('404', 'Not Found / Does not exist.', SecurityResultException)
            .local_error('406', 'Format / Request Unacceptable.', SecurityResultException)
            .local_error('429', 'Too many requests.', SecurityResultException)
            .local_error('default', 'Error response.', SecurityResultException)
        ).execute()

    def unassign_license_to_devices(self,
                                    x_request_id):
        """Does a DELETE request to /v1/devices/license/actions/assign.

        Unassigns SIM-Secure for IoT Flexible and Flexible Bundle license from
        SIMs.

        Args:
            x_request_id (str): Transaction Id.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Success
                response.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.M2M)
            .path('/v1/devices/license/actions/assign')
            .http_method(HttpMethodEnum.DELETE)
            .header_param(Parameter()
                          .key('X-Request-ID')
                          .value(x_request_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SecuritySuccessResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request.', SecurityResultException)
            .local_error('401', 'Unauthorized request.', SecurityResultException)
            .local_error('403', 'Request forbidden.', SecurityResultException)
            .local_error('404', 'Not Found / Does not exist.', SecurityResultException)
            .local_error('406', 'Format / Request Unacceptable.', SecurityResultException)
            .local_error('429', 'Too many requests.', SecurityResultException)
            .local_error('default', 'Error response.', SecurityResultException)
        ).execute()
