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
from verizon.models.esim_request_response import ESIMRequestResponse
from verizon.exceptions.esim_rest_error_response_exception import ESIMRestErrorResponseException


class SIMActionsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(SIMActionsController, self).__init__(config)

    def setactivate_using_post(self,
                               body):
        """Does a POST request to /m2m/v1/devices/profile/actions/activate.

        Uses the profile to activate the SIM.

        Args:
            body (ESIMProfileRequest): Device Profile Query

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/activate')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('thingspace_oauth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ESIMRequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', ESIMRestErrorResponseException)
            .local_error('401', 'Unauthorized', ESIMRestErrorResponseException)
            .local_error('403', 'Forbidden', ESIMRestErrorResponseException)
            .local_error('404', 'Not Found / Does not exist', ESIMRestErrorResponseException)
            .local_error('406', 'Format / Request Unacceptable', ESIMRestErrorResponseException)
            .local_error('429', 'Too many requests', ESIMRestErrorResponseException)
            .local_error('default', 'Error response', ESIMRestErrorResponseException)
        ).execute()

    def setdeactivate_using_post(self,
                                 body):
        """Does a POST request to /m2m/v1/devices/profile/actions/deactivate.

        Uses the profile to deactivate the SIM.

        Args:
            body (ProfileRequest2): Device Profile Query

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                ID

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/devices/profile/actions/deactivate')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('thingspace_oauth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ESIMRequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Bad request', ESIMRestErrorResponseException)
            .local_error('401', 'Unauthorized', ESIMRestErrorResponseException)
            .local_error('403', 'Forbidden', ESIMRestErrorResponseException)
            .local_error('404', 'Not Found / Does not exist', ESIMRestErrorResponseException)
            .local_error('406', 'Format / Request Unacceptable', ESIMRestErrorResponseException)
            .local_error('429', 'Too many requests', ESIMRestErrorResponseException)
            .local_error('default', 'Error response', ESIMRestErrorResponseException)
        ).execute()
