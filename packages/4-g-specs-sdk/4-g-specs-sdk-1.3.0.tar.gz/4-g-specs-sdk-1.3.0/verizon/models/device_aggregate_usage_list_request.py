# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_id import DeviceId
from verizon.models.label import Label


class DeviceAggregateUsageListRequest(object):

    """Implementation of the 'DeviceAggregateUsageListRequest' model.

    Request to list device aggregate usage.

    Attributes:
        start_time (str): The beginning of the reporting period. The startTime
            cannot be more than 6 months before the current date.
        end_time (str): The end of the reporting period. The endTime date must
            be within on month of the startTime date.
        device_ids (List[DeviceId]): One or more devices for which you want
            aggregate data, specified by device ID.
        account_name (str): The name of a billing account.
        group_name (str): The name of a device group, if you want to only
            include devices in that group.
        label (List[Label]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_time": 'startTime',
        "end_time": 'endTime',
        "device_ids": 'deviceIds',
        "account_name": 'accountName',
        "group_name": 'groupName',
        "label": 'label'
    }

    _optionals = [
        'device_ids',
        'account_name',
        'group_name',
        'label',
    ]

    def __init__(self,
                 start_time=None,
                 end_time=None,
                 device_ids=APIHelper.SKIP,
                 account_name=APIHelper.SKIP,
                 group_name=APIHelper.SKIP,
                 label=APIHelper.SKIP):
        """Constructor for the DeviceAggregateUsageListRequest class"""

        # Initialize members of the class
        self.start_time = start_time 
        self.end_time = end_time 
        if device_ids is not APIHelper.SKIP:
            self.device_ids = device_ids 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if group_name is not APIHelper.SKIP:
            self.group_name = group_name 
        if label is not APIHelper.SKIP:
            self.label = label 

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
        start_time = dictionary.get("startTime") if dictionary.get("startTime") else None
        end_time = dictionary.get("endTime") if dictionary.get("endTime") else None
        device_ids = None
        if dictionary.get('deviceIds') is not None:
            device_ids = [DeviceId.from_dictionary(x) for x in dictionary.get('deviceIds')]
        else:
            device_ids = APIHelper.SKIP
        account_name = dictionary.get("accountName") if dictionary.get("accountName") else APIHelper.SKIP
        group_name = dictionary.get("groupName") if dictionary.get("groupName") else APIHelper.SKIP
        label = None
        if dictionary.get('label') is not None:
            label = [Label.from_dictionary(x) for x in dictionary.get('label')]
        else:
            label = APIHelper.SKIP
        # Return an object of this model
        return cls(start_time,
                   end_time,
                   device_ids,
                   account_name,
                   group_name,
                   label)
