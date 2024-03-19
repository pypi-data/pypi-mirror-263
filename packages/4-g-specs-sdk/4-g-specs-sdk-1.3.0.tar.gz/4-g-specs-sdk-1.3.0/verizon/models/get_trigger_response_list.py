# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.get_trigger_response import GetTriggerResponse


class GetTriggerResponseList(object):

    """Implementation of the 'GetTriggerResponseList' model.

    TODO: type model description here.

    Attributes:
        triggers (List[GetTriggerResponse]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "triggers": 'triggers'
    }

    _optionals = [
        'triggers',
    ]

    def __init__(self,
                 triggers=APIHelper.SKIP):
        """Constructor for the GetTriggerResponseList class"""

        # Initialize members of the class
        if triggers is not APIHelper.SKIP:
            self.triggers = triggers 

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
        triggers = None
        if dictionary.get('triggers') is not None:
            triggers = [GetTriggerResponse.from_dictionary(x) for x in dictionary.get('triggers')]
        else:
            triggers = APIHelper.SKIP
        # Return an object of this model
        return cls(triggers)
