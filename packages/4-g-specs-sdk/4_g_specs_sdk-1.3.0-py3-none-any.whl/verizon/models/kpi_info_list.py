# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.kpi_info import KPIInfo


class KPIInfoList(object):

    """Implementation of the 'KPIInfoList' model.

    TODO: type model description here.

    Attributes:
        kpi_info_list (List[KPIInfo]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "kpi_info_list": 'KpiInfoList'
    }

    _optionals = [
        'kpi_info_list',
    ]

    def __init__(self,
                 kpi_info_list=APIHelper.SKIP):
        """Constructor for the KPIInfoList class"""

        # Initialize members of the class
        if kpi_info_list is not APIHelper.SKIP:
            self.kpi_info_list = kpi_info_list 

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
        kpi_info_list = None
        if dictionary.get('KpiInfoList') is not None:
            kpi_info_list = [KPIInfo.from_dictionary(x) for x in dictionary.get('KpiInfoList')]
        else:
            kpi_info_list = APIHelper.SKIP
        # Return an object of this model
        return cls(kpi_info_list)
