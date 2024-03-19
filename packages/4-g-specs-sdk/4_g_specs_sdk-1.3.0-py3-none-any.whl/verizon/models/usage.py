# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.custom_fields import CustomFields


class Usage(object):

    """Implementation of the 'Usage' model.

    The daily network data usage of a single device during a specified time
    period.

    Attributes:
        bytes_used (long|int): The number of bytes that the device sent or
            received on the report date.
        extended_attributes (List[CustomFields]): The number of
            mobile-originated and mobile-terminated SMS messages on the report
            date.
        service_plan (str): The list of service plans associated with the
            device/account.
        sms_used (int): The number of SMS messages that were sent or received
            on the report date.
        source (str): The source of the information for the reported usage.
        timestamp (str): The date of the recorded usage.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "bytes_used": 'bytesUsed',
        "extended_attributes": 'extendedAttributes',
        "service_plan": 'servicePlan',
        "sms_used": 'smsUsed',
        "source": 'source',
        "timestamp": 'timestamp'
    }

    _optionals = [
        'bytes_used',
        'extended_attributes',
        'service_plan',
        'sms_used',
        'source',
        'timestamp',
    ]

    def __init__(self,
                 bytes_used=APIHelper.SKIP,
                 extended_attributes=APIHelper.SKIP,
                 service_plan=APIHelper.SKIP,
                 sms_used=APIHelper.SKIP,
                 source=APIHelper.SKIP,
                 timestamp=APIHelper.SKIP):
        """Constructor for the Usage class"""

        # Initialize members of the class
        if bytes_used is not APIHelper.SKIP:
            self.bytes_used = bytes_used 
        if extended_attributes is not APIHelper.SKIP:
            self.extended_attributes = extended_attributes 
        if service_plan is not APIHelper.SKIP:
            self.service_plan = service_plan 
        if sms_used is not APIHelper.SKIP:
            self.sms_used = sms_used 
        if source is not APIHelper.SKIP:
            self.source = source 
        if timestamp is not APIHelper.SKIP:
            self.timestamp = timestamp 

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
        bytes_used = dictionary.get("bytesUsed") if dictionary.get("bytesUsed") else APIHelper.SKIP
        extended_attributes = None
        if dictionary.get('extendedAttributes') is not None:
            extended_attributes = [CustomFields.from_dictionary(x) for x in dictionary.get('extendedAttributes')]
        else:
            extended_attributes = APIHelper.SKIP
        service_plan = dictionary.get("servicePlan") if dictionary.get("servicePlan") else APIHelper.SKIP
        sms_used = dictionary.get("smsUsed") if dictionary.get("smsUsed") else APIHelper.SKIP
        source = dictionary.get("source") if dictionary.get("source") else APIHelper.SKIP
        timestamp = dictionary.get("timestamp") if dictionary.get("timestamp") else APIHelper.SKIP
        # Return an object of this model
        return cls(bytes_used,
                   extended_attributes,
                   service_plan,
                   sms_used,
                   source,
                   timestamp)
