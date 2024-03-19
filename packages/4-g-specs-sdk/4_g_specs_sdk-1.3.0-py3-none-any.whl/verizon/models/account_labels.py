# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_labels import DeviceLabels
from verizon.models.device_list import DeviceList


class AccountLabels(object):

    """Implementation of the 'AccountLabels' model.

    Maximum of 2,000 objects are allowed in the array.

    Attributes:
        devices (List[DeviceList]): TODO: type description here.
        label (List[DeviceLabels]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "devices": 'devices',
        "label": 'label'
    }

    _optionals = [
        'label',
    ]

    def __init__(self,
                 devices=None,
                 label=APIHelper.SKIP):
        """Constructor for the AccountLabels class"""

        # Initialize members of the class
        self.devices = devices 
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
        devices = None
        if dictionary.get('devices') is not None:
            devices = [DeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        label = None
        if dictionary.get('label') is not None:
            label = [DeviceLabels.from_dictionary(x) for x in dictionary.get('label')]
        else:
            label = APIHelper.SKIP
        # Return an object of this model
        return cls(devices,
                   label)
