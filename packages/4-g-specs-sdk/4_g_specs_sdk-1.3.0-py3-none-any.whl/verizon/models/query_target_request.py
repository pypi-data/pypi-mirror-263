# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.account_identifier import AccountIdentifier
from verizon.models.resource_identifier import ResourceIdentifier


class QueryTargetRequest(object):

    """Implementation of the 'QueryTargetRequest' model.

    Search for targets by property values.

    Attributes:
        accountidentifier (AccountIdentifier): The ID of the authenticating
            billing account, in the format
            `{"billingaccountid":"1234567890-12345"}`.
        selection (Dict[str, str]): A comma-separated list of properties and
            comparator values to match against subscriptions in the ThingSpace
            account. See Working with Query Filters for more information. If
            the request does not include `$selection`, the response will
            include all subscriptions to which the requesting user has
            access.
        resourceidentifier (ResourceIdentifier): The ID of the target to
            delete, in the format {"id":
            "dd1682d3-2d80-cefc-f3ee-25154800beff"}.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "accountidentifier": 'accountidentifier',
        "selection": '$selection',
        "resourceidentifier": 'resourceidentifier'
    }

    _optionals = [
        'accountidentifier',
        'selection',
        'resourceidentifier',
    ]

    def __init__(self,
                 accountidentifier=APIHelper.SKIP,
                 selection=APIHelper.SKIP,
                 resourceidentifier=APIHelper.SKIP):
        """Constructor for the QueryTargetRequest class"""

        # Initialize members of the class
        if accountidentifier is not APIHelper.SKIP:
            self.accountidentifier = accountidentifier 
        if selection is not APIHelper.SKIP:
            self.selection = selection 
        if resourceidentifier is not APIHelper.SKIP:
            self.resourceidentifier = resourceidentifier 

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
        accountidentifier = AccountIdentifier.from_dictionary(dictionary.get('accountidentifier')) if 'accountidentifier' in dictionary.keys() else APIHelper.SKIP
        selection = dictionary.get("$selection") if dictionary.get("$selection") else APIHelper.SKIP
        resourceidentifier = ResourceIdentifier.from_dictionary(dictionary.get('resourceidentifier')) if 'resourceidentifier' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(accountidentifier,
                   selection,
                   resourceidentifier)
