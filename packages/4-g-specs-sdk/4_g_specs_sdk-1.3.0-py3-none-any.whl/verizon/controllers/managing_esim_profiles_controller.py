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
from verizon.models.gio_request_response import GIORequestResponse
from verizon.exceptions.gio_rest_error_response_exception import GIORestErrorResponseException


class ManagingESIMProfilesController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ManagingESIMProfilesController, self).__init__(config)

    def activate_a_device_profile(self,
                                  body):
        """Does a POST request to /m2m/v1/devices/profile/actions/activate.

        Activate a device with either a lead or local profile.

        Args:
            body (GIOProfileRequest): Device Profile Query

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
            .deserialize_into(GIORequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', GIORestErrorResponseException)
        ).execute()

    def enable_a_device_profile(self,
                                body):
        """Does a POST request to /m2m/v1/devices/profile/actions/enable.

        Enable a device lead or local profile.

        Args:
            body (DeviceProfileRequest): Device Profile Query

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
            .path('/m2m/v1/devices/profile/actions/enable')
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
            .deserialize_into(GIORequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', GIORestErrorResponseException)
        ).execute()

    def deactivate_a_device_profile(self,
                                    body):
        """Does a POST request to /m2m/v1/devices/profile/actions/deactivate.

        Deactivate the lead or local profile. **Note:** to reactivate the
        profile, use the **Activate** endpoint above.

        Args:
            body (GIODeactivateDeviceProfileRequest): Device Profile Query

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
            .deserialize_into(GIORequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', GIORestErrorResponseException)
        ).execute()

    def enable_a_device_profile_for_download(self,
                                             body):
        """Does a POST request to /m2m/v1/devices/profile/actions/download_enable.

        Enable the Global IoT Orchestration device profile for download.

        Args:
            body (DeviceProfileRequest): Device Profile Query

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
            .path('/m2m/v1/devices/profile/actions/download_enable')
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
            .deserialize_into(GIORequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', GIORestErrorResponseException)
        ).execute()

    def download_a_device_profile(self,
                                  body):
        """Does a POST request to /m2m/v1/devices/profile/actions/download.

        Download a Global IoT Orchestration device profile.

        Args:
            body (DeviceProfileRequest): Device Profile Query

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
            .path('/m2m/v1/devices/profile/actions/download')
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
            .deserialize_into(GIORequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', GIORestErrorResponseException)
        ).execute()

    def delete_a_device_profile(self,
                                body):
        """Does a POST request to /m2m/v1/devices/profile/actions/delete.

        Delete a device profile for Global IoT Orchestration. **Note:** the
        profile must be deactivated first!

        Args:
            body (DeviceProfileRequest): Device Profile Query

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
            .path('/m2m/v1/devices/profile/actions/delete')
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
            .deserialize_into(GIORequestResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', GIORestErrorResponseException)
        ).execute()
