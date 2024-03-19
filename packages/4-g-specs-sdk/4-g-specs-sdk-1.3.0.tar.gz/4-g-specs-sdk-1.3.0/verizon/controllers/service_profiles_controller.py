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
from verizon.models.create_service_profile_result import CreateServiceProfileResult
from verizon.models.list_service_profiles_result import ListServiceProfilesResult
from verizon.models.resources_service_profile_with_id import ResourcesServiceProfileWithId
from verizon.models.update_service_profile_result import UpdateServiceProfileResult
from verizon.models.delete_service_profile_result import DeleteServiceProfileResult
from verizon.exceptions.edge_discovery_result_exception import EdgeDiscoveryResultException


class ServiceProfilesController(BaseController):

    """A Controller to access Endpoints in the verizon API."""
    def __init__(self, config):
        super(ServiceProfilesController, self).__init__(config)

    def create_service_profile(self,
                               body):
        """Does a POST request to /serviceprofiles.

        Creates a service profile that describes the resource requirements of
        a service.

        Args:
            body (ResourcesServiceProfile): The request body passes all of the
                needed parameters to create a service profile. Parameters will
                be edited here rather than the **Parameters** section above.
                The `maxLatencyMs` and `clientType` parameters are both
                required in the request body. **Note:** The `maxLatencyMs`
                value must be submitted in multiples of 5. Additionally, "GPU"
                is future functionality and the values are not captured.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Service
                profile ID.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceprofiles')
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
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(CreateServiceProfileResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def list_service_profiles(self):
        """Does a GET request to /serviceprofiles.

        List all service profiles registered under your API key.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. A comma
                delimited list of all the service profiles registered under
                your API key.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceprofiles')
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListServiceProfilesResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def get_service_profile(self,
                            service_profile_id):
        """Does a GET request to /serviceprofiles/{serviceProfileId}.

        Returns a specified service profile.

        Args:
            service_profile_id (str): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Requested
                service profile.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceprofiles/{serviceProfileId}')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('serviceProfileId')
                            .value(service_profile_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ResourcesServiceProfileWithId.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def update_service_profile(self,
                               service_profile_id,
                               body):
        """Does a PUT request to /serviceprofiles/{serviceProfileId}.

        Update the definition of a Service Profile.

        Args:
            service_profile_id (str): TODO: type description here.
            body (ResourcesServiceProfile): The request body passes the rest
                of the needed parameters to create a service profile. The
                `maxLatencyMs` and `clientType` parameters are both required
                in the request body. **Note:** The `maxLatencyMs` value must
                be submitted in multiples of 5. Additionally, "GPU" is future
                functionality and the values are not captured. Default values
                to use are shown.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Update a
                service profile.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceprofiles/{serviceProfileId}')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('serviceProfileId')
                            .value(service_profile_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
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
            .deserialize_into(UpdateServiceProfileResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()

    def delete_service_profile(self,
                               service_profile_id):
        """Does a DELETE request to /serviceprofiles/{serviceProfileId}.

        Delete Service Profile based on unique service profile ID.

        Args:
            service_profile_id (str): TODO: type description here.

        Returns:
            ApiResponse: An object with the response value as well as other
                useful information such as status codes and headers. Delete a
                service profile.

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.EDGE_DISCOVERY)
            .path('/serviceprofiles/{serviceProfileId}')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('serviceProfileId')
                            .value(service_profile_id)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('oAuth2'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(DeleteServiceProfileResult.from_dictionary)
            .is_api_response(True)
            .local_error('400', 'HTTP 400 Bad Request.', EdgeDiscoveryResultException)
            .local_error('401', 'HTTP 401 Unauthorized.', EdgeDiscoveryResultException)
            .local_error('default', 'HTTP 500 Internal Server Error.', EdgeDiscoveryResultException)
        ).execute()
