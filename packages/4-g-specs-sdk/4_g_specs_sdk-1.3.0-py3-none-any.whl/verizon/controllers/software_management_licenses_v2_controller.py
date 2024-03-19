# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from deprecation import deprecated
from verizon.api_helper import APIHelper
from verizon.configuration import Server
from verizon.http.api_response import ApiResponse
from verizon.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from verizon.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from verizon.models.v2_license_summary import V2LicenseSummary
from verizon.models.v2_licenses_assigned_removed_result import V2LicensesAssignedRemovedResult
from verizon.models.v2_list_of_licenses_to_remove import V2ListOfLicensesToRemove
from verizon.models.v2_list_of_licenses_to_remove_result import V2ListOfLicensesToRemoveResult
from verizon.models.fota_v2_success_result import FotaV2SuccessResult
from verizon.exceptions.fota_v2_result_exception import FotaV2ResultException


class SoftwareManagementLicensesV2Controller(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(SoftwareManagementLicensesV2Controller, self).__init__(config)

    def get_account_license_status(self,
                                   account,
                                   last_seen_device_id=None):
        """Does a GET request to /licenses/{account}.

        The endpoint allows user to list license usage.

        Args:
            account (str): Account identifier.
            last_seen_device_id (str, optional): Last seen device identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Summary
                of license assignment.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/licenses/{account}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('lastSeenDeviceId')
                         .value(last_seen_device_id))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V2LicenseSummary.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    @deprecated()
    def assign_licenses_to_devices(self,
                                   account,
                                   body):
        """Does a POST request to /licenses/{account}/assign.

        This endpoint allows user to assign licenses to a list of devices.

        Args:
            account (str): Account identifier.
            body (V2LicenseIMEI): License assignment.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. License
                assignment result.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/licenses/{account}/assign')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V2LicensesAssignedRemovedResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    @deprecated()
    def remove_licenses_from_devices(self,
                                     account,
                                     body):
        """Does a POST request to /licenses/{account}/remove.

        This endpoint allows user to remove licenses from a list of devices.

        Args:
            account (str): Account identifier.
            body (V2LicenseIMEI): License removal.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. License
                removal result.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/licenses/{account}/remove')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V2LicensesAssignedRemovedResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    @deprecated()
    def list_licenses_to_remove(self,
                                account,
                                start_index=None):
        """Does a GET request to /licenses/{account}/cancel.

        The license cancel endpoint allows user to list registered license
        cancellation candidate devices.

        Args:
            account (str): Account identifier.
            start_index (str, optional): Start index to retrieve.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A list of
                license cancellation candidate devices.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/licenses/{account}/cancel')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('startIndex')
                         .value(start_index))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V2ListOfLicensesToRemove.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    @deprecated()
    def create_list_of_licenses_to_remove(self,
                                          account,
                                          body):
        """Does a POST request to /licenses/{account}/cancel.

        The license cancel endpoint allows user to create a list of license
        cancellation candidate devices.

        Args:
            account (str): Account identifier.
            body (V2ListOfLicensesToRemoveRequest): List of licensess to
                remove.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Return a
                created license cancellation device list.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/licenses/{account}/cancel')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('*/*'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(V2ListOfLicensesToRemoveResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()

    @deprecated()
    def delete_list_of_licenses_to_remove(self,
                                          account):
        """Does a DELETE request to /licenses/{account}/cancel.

        This endpoint allows user to delete a created cancel candidate device
        list.

        Args:
            account (str): Account identifier.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Result of
                deletion of candidate list of devices to remove.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.SOFTWARE_MANAGEMENT_V2)
            .path('/licenses/{account}/cancel')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('account')
                            .value(account)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FotaV2SuccessResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'Unexpected error.', FotaV2ResultException)
        ).execute()
