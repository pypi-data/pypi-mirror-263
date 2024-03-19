# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.v3_device_status import V3DeviceStatus


class V3CampaignDevice(object):

    """Implementation of the 'V3CampaignDevice' model.

    Campaign history.

    Attributes:
        total_device (int): Total device count.
        has_more_data (bool): Has more report flag.
        last_seen_device_id (str): Device identifier.
        max_page_size (int): Maximum page size.
        device_list (List[V3DeviceStatus]): List of devices with id in IMEI.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "has_more_data": 'hasMoreData',
        "max_page_size": 'maxPageSize',
        "device_list": 'deviceList',
        "total_device": 'totalDevice',
        "last_seen_device_id": 'lastSeenDeviceId'
    }

    _optionals = [
        'total_device',
        'last_seen_device_id',
    ]

    def __init__(self,
                 has_more_data=None,
                 max_page_size=None,
                 device_list=None,
                 total_device=APIHelper.SKIP,
                 last_seen_device_id=APIHelper.SKIP):
        """Constructor for the V3CampaignDevice class"""

        # Initialize members of the class
        if total_device is not APIHelper.SKIP:
            self.total_device = total_device 
        self.has_more_data = has_more_data 
        if last_seen_device_id is not APIHelper.SKIP:
            self.last_seen_device_id = last_seen_device_id 
        self.max_page_size = max_page_size 
        self.device_list = device_list 

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
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else None
        max_page_size = dictionary.get("maxPageSize") if dictionary.get("maxPageSize") else None
        device_list = None
        if dictionary.get('deviceList') is not None:
            device_list = [V3DeviceStatus.from_dictionary(x) for x in dictionary.get('deviceList')]
        total_device = dictionary.get("totalDevice") if dictionary.get("totalDevice") else APIHelper.SKIP
        last_seen_device_id = dictionary.get("lastSeenDeviceId") if dictionary.get("lastSeenDeviceId") else APIHelper.SKIP
        # Return an object of this model
        return cls(has_more_data,
                   max_page_size,
                   device_list,
                   total_device,
                   last_seen_device_id)
