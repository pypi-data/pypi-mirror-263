# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_device_list_filter import AccountDeviceListFilter
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId


class AccountDeviceListRequest(object):

    """Implementation of the 'AccountDeviceListRequest' model.

    Request for listing account devices.

    Attributes:
        account_name (str): The billing account for which a list of devices is
            returned. If you don't specify an accountName, the list includes
            all devices to which you have access.
        device_id (DeviceId): An identifier for a single device.
        filter (AccountDeviceListFilter): Filter for a list of devices.
        current_state (str): The name of a device state, to only include
            devices in that state.
        custom_fields (List[CustomFields]): Custom field names and values, if
            you want to only include devices that have matching values.
        earliest (str): Only include devices that were added after this date
            and time.
        group_name (str): Only include devices that are in this device group.
        latest (str): Only include devices that were added before this date
            and time.
        service_plan (str): Only include devices that have this service plan.
        max_number_of_devices (int): TODO: type description here.
        largest_device_id_seen (long|int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "device_id": 'deviceId',
        "filter": 'filter',
        "current_state": 'currentState',
        "custom_fields": 'customFields',
        "earliest": 'earliest',
        "group_name": 'groupName',
        "latest": 'latest',
        "service_plan": 'servicePlan',
        "max_number_of_devices": 'maxNumberOfDevices',
        "largest_device_id_seen": 'largestDeviceIdSeen'
    }

    _optionals = [
        'account_name',
        'device_id',
        'filter',
        'current_state',
        'custom_fields',
        'earliest',
        'group_name',
        'latest',
        'service_plan',
        'max_number_of_devices',
        'largest_device_id_seen',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 device_id=APIHelper.SKIP,
                 filter=APIHelper.SKIP,
                 current_state=APIHelper.SKIP,
                 custom_fields=APIHelper.SKIP,
                 earliest=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 latest=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 max_number_of_devices=APIHelper.SKIP,
                 largest_device_id_seen=APIHelper.SKIP):
        """Constructor for the AccountDeviceListRequest class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if device_id is not APIHelper.SKIP:
            self.device_id = device_id 
        if filter is not APIHelper.SKIP:
            self.filter = filter 
        if current_state is not APIHelper.SKIP:
            self.current_state = current_state 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if earliest is not APIHelper.SKIP:
            self.earliest = earliest 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if latest is not APIHelper.SKIP:
            self.latest = latest 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
        if max_number_of_devices is not APIHelper.SKIP:
            self.max_number_of_devices = max_number_of_devices 
        if largest_device_id_seen is not APIHelper.SKIP:
            self.largest_device_id_seen = largest_device_id_seen 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        device_id = DeviceId.from_dictionary(dictionary.get('deviceId')) if 'deviceId' in dictionary.keys() else APIHelper.SKIP
        filter = AccountDeviceListFilter.from_dictionary(dictionary.get('filter')) if 'filter' in dictionary.keys() else APIHelper.SKIP
        current_state = dictionary.get("currentState") if dictionary.get("currentState") else APIHelper.SKIP
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [CustomFields.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        earliest = dictionary.get("earliest") if dictionary.get("earliest") else APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        latest = dictionary.get("latest") if dictionary.get("latest") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        max_number_of_devices = dictionary.get("maxNumberOfDevices") if dictionary.get("maxNumberOfDevices") else APIHelper.SKIP
        largest_device_id_seen = dictionary.get("largestDeviceIdSeen") if dictionary.get("largestDeviceIdSeen") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   device_id,
                   filter,
                   current_state,
                   custom_fields,
                   earliest,
                   group_name,
                   latest,
                   service_plan,
                   max_number_of_devices,
                   largest_device_id_seen)
