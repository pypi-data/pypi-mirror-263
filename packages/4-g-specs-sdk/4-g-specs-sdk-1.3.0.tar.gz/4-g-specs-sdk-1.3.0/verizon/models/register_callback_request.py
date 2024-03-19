# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class RegisterCallbackRequest(object):

    """Implementation of the 'RegisterCallbackRequest' model.

    Request to register a callback.

    Attributes:
        name (str): The name of the callback service that you want to
            subscribe to.
        url (str): The address on your server where you have enabled a
            listening service for callback messages.
        username (str): The user name that the M2M Platform should return in
            the callback messages.
        password (str): The password that the M2M Platform should return in
            the callback messages.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "url": 'url',
        "username": 'username',
        "password": 'password'
    }

    _optionals = [
        'username',
        'password',
    ]

    def __init__(self,
                 name=None,
                 url=None,
                 username=APIHelper.SKIP,
                 password=APIHelper.SKIP):
        """Constructor for the RegisterCallbackRequest class"""

        # Initialize members of the class
        self.name = name 
        self.url = url 
        if username is not APIHelper.SKIP:
            self.username = username 
        if password is not APIHelper.SKIP:
            self.password = password 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        url = dictionary.get("url") if dictionary.get("url") else None
        username = dictionary.get("username") if dictionary.get("username") else APIHelper.SKIP
        password = dictionary.get("password") if dictionary.get("password") else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   url,
                   username,
                   password)
