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
from verizon.models.intelligence_success_result import IntelligenceSuccessResult
from verizon.models.anomaly_detection_settings import AnomalyDetectionSettings
from verizon.exceptions.intelligence_result_exception import IntelligenceResultException


class AnomalySettingsController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(AnomalySettingsController, self).__init__(config)

    def activate_anomaly_detection(self,
                                   body):
        """Does a POST request to /m2m/v1/intelligence/anomaly/settings.

        Uses the subscribed account ID to activate anomaly detection and set
        threshold values.

        Args:
            body (AnomalyDetectionRequest): Request to activate anomaly
                detection.

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
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/intelligence/anomaly/settings')
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
            .deserialize_into(IntelligenceSuccessResult.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'An error occurred.', IntelligenceResultException)
        ).execute()

    def list_anomaly_detection_settings(self,
                                        account_name):
        """Does a GET request to /m2m/v1/intelligence/{accountName}/anomaly/settings.

        Retrieves the current anomaly detection settings for an account.

        Args:
            account_name (str): The name of the subscribed account.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Retrieve
                the settings for anomaly detection.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/intelligence/{accountName}/anomaly/settings')
            .http_method(HttpMethodEnum.GET)
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
            .deserialize_into(AnomalyDetectionSettings.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'An error occurred.', IntelligenceResultException)
        ).execute()

    def reset_anomaly_detection_parameters(self,
                                           account_name):
        """Does a PUT request to /m2m/v1/intelligence/{accountName}/anomaly/settings/reset.

        Resets the thresholds to zero.

        Args:
            account_name (str): The name of the subscribed account.

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
            RequestBuilder().server(Server.THINGSPACE)
            .path('/m2m/v1/intelligence/{accountName}/anomaly/settings/reset')
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
            .deserialize_into(IntelligenceSuccessResult.from_dictionary)
            .is_api_response(True)
            .local_error('default', 'An error occurred.', IntelligenceResultException)
        ).execute()
