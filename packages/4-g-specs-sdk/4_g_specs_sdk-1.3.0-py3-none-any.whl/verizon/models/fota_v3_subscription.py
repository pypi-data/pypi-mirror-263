# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper


class FotaV3Subscription(object):

    """Implementation of the 'FotaV3Subscription' model.

    Information for licenses applied to devices.

    Attributes:
        account_name (str): Account identifier in "##########-#####".
        purchase_type (str): Subscription models used by the account.
        license_count (int): Number of monthly licenses in an MRC
            subscription.
        license_used_count (int): Number of licenses currently assigned to
            devices.
        update_time (str): The date and time of when the subscription was last
            updated.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "purchase_type": 'purchaseType',
        "license_count": 'licenseCount',
        "license_used_count": 'licenseUsedCount',
        "update_time": 'updateTime'
    }

    _optionals = [
        'account_name',
        'purchase_type',
        'license_count',
        'license_used_count',
        'update_time',
    ]

    def __init__(self,
                 account_name=APIHelper.SKIP,
                 purchase_type=APIHelper.SKIP,
                 license_count=APIHelper.SKIP,
                 license_used_count=APIHelper.SKIP,
                 update_time=APIHelper.SKIP):
        """Constructor for the FotaV3Subscription class"""

        # Initialize members of the class
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if purchase_type is not APIHelper.SKIP:
            self.purchase_type = purchase_type 
        if license_count is not APIHelper.SKIP:
            self.license_count = license_count 
        if license_used_count is not APIHelper.SKIP:
            self.license_used_count = license_used_count 
        if update_time is not APIHelper.SKIP:
            self.update_time = update_time 

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
        purchase_type = dictionary.get("purchaseType") if dictionary.get("purchaseType") else APIHelper.SKIP
        license_count = dictionary.get("licenseCount") if dictionary.get("licenseCount") else APIHelper.SKIP
        license_used_count = dictionary.get("licenseUsedCount") if dictionary.get("licenseUsedCount") else APIHelper.SKIP
        update_time = dictionary.get("updateTime") if dictionary.get("updateTime") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   purchase_type,
                   license_count,
                   license_used_count,
                   update_time)
