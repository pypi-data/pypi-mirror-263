# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.device_list import DeviceList
from verizon.models.primary_place_of_use import PrimaryPlaceOfUse


class ProfileRequest(object):

    """Implementation of the 'ProfileRequest' model.

    TODO: type model description here.

    Attributes:
        account_name (str): TODO: type description here.
        devices (List[DeviceList]): TODO: type description here.
        carrier_name (str): TODO: type description here.
        service_plan (str): TODO: type description here.
        mdn_zip_code (str): TODO: type description here.
        primary_place_of_use (List[PrimaryPlaceOfUse]): TODO: type description
            here.
        smsr_oid (str): TODO: type description here.
        carrier_ip_pool_name (str): The name of the pool of IP addresses
            assigned to the profile.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "account_name": 'accountName',
        "devices": 'devices',
        "carrier_name": 'carrierName',
        "service_plan": 'servicePlan',
        "mdn_zip_code": 'mdnZipCode',
        "primary_place_of_use": 'primaryPlaceOfUse',
        "smsr_oid": 'smsrOid',
        "carrier_ip_pool_name": 'carrierIpPoolName'
    }

    _optionals = [
        'carrier_name',
        'service_plan',
        'mdn_zip_code',
        'primary_place_of_use',
        'smsr_oid',
        'carrier_ip_pool_name',
    ]

    def __init__(self,
                 account_name=None,
                 devices=None,
                 carrier_name=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 mdn_zip_code=APIHelper.SKIP,
                 primary_place_of_use=APIHelper.SKIP,
                 smsr_oid=APIHelper.SKIP,
                 carrier_ip_pool_name=APIHelper.SKIP):
        """Constructor for the ProfileRequest class"""

        # Initialize members of the class
        self.account_name = account_name 
        self.devices = devices 
        if carrier_name is not APIHelper.SKIP:
            self.carrier_name = carrier_name 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
        if mdn_zip_code is not APIHelper.SKIP:
            self.mdn_zip_code = mdn_zip_code 
        if primary_place_of_use is not APIHelper.SKIP:
            self.primary_place_of_use = primary_place_of_use 
        if smsr_oid is not APIHelper.SKIP:
            self.smsr_oid = smsr_oid 
        if carrier_ip_pool_name is not APIHelper.SKIP:
            self.carrier_ip_pool_name = carrier_ip_pool_name 

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
        devices = None
        if dictionary.get('devices') is not None:
            devices = [DeviceList.from_dictionary(x) for x in dictionary.get('devices')]
        carrier_name = dictionary.get("carrierName") if dictionary.get("carrierName") else APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        mdn_zip_code = dictionary.get("mdnZipCode") if dictionary.get("mdnZipCode") else APIHelper.SKIP
        primary_place_of_use = None
        if dictionary.get('primaryPlaceOfUse') is not None:
            primary_place_of_use = [PrimaryPlaceOfUse.from_dictionary(x) for x in dictionary.get('primaryPlaceOfUse')]
        else:
            primary_place_of_use = APIHelper.SKIP
        smsr_oid = dictionary.get("smsrOid") if dictionary.get("smsrOid") else APIHelper.SKIP
        carrier_ip_pool_name = dictionary.get("carrierIpPoolName") if dictionary.get("carrierIpPoolName") else APIHelper.SKIP
        # Return an object of this model
        return cls(account_name,
                   devices,
                   carrier_name,
                   service_plan,
                   mdn_zip_code,
                   primary_place_of_use,
                   smsr_oid,
                   carrier_ip_pool_name)
