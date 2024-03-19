# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class FirmwareIMEI(object):

    """Implementation of the 'FirmwareIMEI' model.

    A list of IMEIs for devices to be synchronized between ThingSpace and the
    FOTA server.

    Attributes:
        device_list (List[str]): Device IMEI list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "device_list": 'deviceList'
    }

    def __init__(self,
                 device_list=None):
        """Constructor for the FirmwareIMEI class"""

        # Initialize members of the class
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
        device_list = dictionary.get("deviceList") if dictionary.get("deviceList") else None
        # Return an object of this model
        return cls(device_list)
