# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class CallbackSummary(object):

    """Implementation of the 'CallbackSummary' model.

    Registered callback information.

    Attributes:
        url (str): Callback URL for an subscribed service.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "url": 'url'
    }

    _optionals = [
        'url',
    ]

    def __init__(self,
                 url=APIHelper.SKIP):
        """Constructor for the CallbackSummary class"""

        # Initialize members of the class
        if url is not APIHelper.SKIP:
            self.url = url 

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
        url = dictionary.get("url") if dictionary.get("url") else APIHelper.SKIP
        # Return an object of this model
        return cls(url)
