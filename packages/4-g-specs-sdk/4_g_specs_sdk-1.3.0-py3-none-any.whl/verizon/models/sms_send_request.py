# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.custom_fields import CustomFields
from verizon.models.device_id import DeviceId


class SMSSendRequest(object):

    """Implementation of the 'SMSSendRequest' model.

    Request to send SMS.

    Attributes:
        account_name (str): The name of a billing account.
        sms_message (str): The contents of the SMS message. The SMS message is
            limited to 160 characters in 7-bit format, or 140 characters in
            8-bit format.
        custom_fields (List[CustomFields]): The names and values of custom
            fields, if you want to only include devices that have matching
            custom fields.
        data_encoding (str): The SMS message encoding, which can be 7-bit
            (default), 8-bit-ASCII, 8-bit-UTF-8, 8-bit-DATA.
        device_ids (List[DeviceId]): The devices that you want to send the
            message to, specified by device identifier.
        group_name (str): The name of a device group, if you want to send the
            SMS message to all devices in the device group.
        service_plan (str): The name of a service plan, if you want to only
            include devices that have that service plan.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "sms_message": 'smsMessage',
        "custom_fields": 'customFields',
        "data_encoding": 'dataEncoding',
        "device_ids": 'deviceIds',
        "group_name": 'groupName',
        "service_plan": 'servicePlan'
    }

    _optionals = [
        'custom_fields',
        'data_encoding',
        'device_ids',
        'group_name',
        'service_plan',
    ]

    def __init__(self,
                 account_name=None,
                 sms_message=None,
                 custom_fields=APIHelper.SKIP,
                 data_encoding=APIHelper.SKIP,
                 device_ids=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP):
        """Constructor for the SMSSendRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.sms_message = sms_message 
        if custom_fields is not APIHelper.SKIP:
            self.custom_fields = custom_fields 
        if data_encoding is not APIHelper.SKIP:
            self.data_encoding = data_encoding 
        if device_ids is not APIHelper.SKIP:
            self.device_ids = device_ids 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 

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
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else None
        sms_message = dictionary.get("smsMessage") if dictionary.get("smsMessage") else None
        custom_fields = None
        if dictionary.get('customFields') is not None:
            custom_fields = [CustomFields.from_dictionary(x) for x in dictionary.get('customFields')]
        else:
            custom_fields = APIHelper.SKIP
        data_encoding = dictionary.get("dataEncoding") if dictionary.get("dataEncoding") else APIHelper.SKIP
        device_ids = None
        if dictionary.get('deviceIds') is not None:
            device_ids = [DeviceId.from_dictionary(x) for x in dictionary.get('deviceIds')]
        else:
            device_ids = APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   sms_message,
                   custom_fields,
                   data_encoding,
                   device_ids,
                   group_name,
                   service_plan)
