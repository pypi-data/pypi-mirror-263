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
from verizon.models.sms_messages_response import SmsMessagesResponse
from verizon.models.success_response import SuccessResponse
from verizon.exceptions.gio_rest_error_response_exception import GIORestErrorResponseException


class DeviceSMSMessagingController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(DeviceSMSMessagingController, self).__init__(config)

    def send_an_sms_message(self,
                            body):
        """Does a POST request to /m2m/v1/sms.

        Sends an SMS message to one device. Messages are queued on the M2M MC
        Platform and sent as soon as possible, but they may be delayed due to
        traffic and routing considerations.

        Args:
            body (GIOSMSSendRequest): SMS message to an indiividual device.

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
            .path('/m2m/v1/sms')
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

    def get_sms_messages(self,
                         account_name,
                         next=None):
        """Does a GET request to /m2m/v1/sms/{accountName}/history.

        Retrieves queued SMS messages sent by all M2M MC devices associated
        with an account.

        Args:
            account_name (str): Numeric account name
            next (str, optional): Continue the previous query from the pageUrl
                in Location Header

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers.
                Successful response

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/sms/{accountName}/history')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('accountName')
                            .value(account_name)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('next')
                         .value(next))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('thingspace_oauth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SmsMessagesResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', GIORestErrorResponseException)
        ).execute()

    def start_sms_message_delivery(self,
                                   account_name):
        """Does a PUT request to /m2m/v1/sms/{accountName}/startCallbacks.

        Starts delivery of SMS messages for the specified account.

        Args:
            account_name (str): Numeric account name

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Request
                Success Message

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/sms/{accountName}/startCallbacks')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('accountName')
                            .value(account_name)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('thingspace_oauth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SuccessResponse.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'Error response', GIORestErrorResponseException)
        ).execute()

    def list_sms_message_history(self,
                                 body):
        """Does a POST request to /m2m/v1/devices/sms/history/actions/list.

        Returns a list of sms history for a given device during a specified
        time frame.

        Args:
            body (SMSEventHistoryRequest): Device Query

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
            .path('/m2m/v1/devices/sms/history/actions/list')
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
