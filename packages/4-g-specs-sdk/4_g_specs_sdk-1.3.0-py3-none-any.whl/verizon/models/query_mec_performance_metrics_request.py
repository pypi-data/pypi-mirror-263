# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class QueryMECPerformanceMetricsRequest(object):

    """Implementation of the 'QueryMECPerformanceMetricsRequest' model.

    MEC performance metrics request.

    Attributes:
        imei (str): The 15-digit International Mobile Equipment Identifier.
        msisdn (str): The 12-digit Mobile Station International Subscriber
            Directory Number.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "imei": 'IMEI',
        "msisdn": 'MSISDN'
    }

    def __init__(self,
                 imei=None,
                 msisdn=None):
        """Constructor for the QueryMECPerformanceMetricsRequest class"""

        # Initialize members of the class
        self.imei = imei 
        self.msisdn = msisdn 

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
        imei = dictionary.get("IMEI") if dictionary.get("IMEI") else None
        msisdn = dictionary.get("MSISDN") if dictionary.get("MSISDN") else None
        # Return an object of this model
        return cls(imei,
                   msisdn)
