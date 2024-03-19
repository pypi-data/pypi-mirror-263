# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.location import Location


class LocationReport(object):

    """Implementation of the 'LocationReport' model.

    Location information for up to 1,000 devices.

    Attributes:
        dev_location_list (List[Location]): Device location information.
        has_more_data (bool): True if there are more device locations to
            retrieve.
        start_index (str): The zero-based number of the first record to
            return. Set startIndex=0 for the first request. If there are more
            than 1,000 devices to be returned (hasMoreData=true), set
            startIndex=1000 for the second request, 2000 for the third
            request, etc.
        total_count (int): The total number of devices in the original request
            and in the report.
        txid (str): The transaction ID of the report.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "dev_location_list": 'devLocationList',
        "has_more_data": 'hasMoreData',
        "start_index": 'startIndex',
        "total_count": 'totalCount',
        "txid": 'txid'
    }

    _optionals = [
        'dev_location_list',
        'has_more_data',
        'start_index',
        'total_count',
        'txid',
    ]

    def __init__(self,
                 dev_location_list=APIHelper.SKIP,
                 has_more_data=APIHelper.SKIP,
                 start_index=APIHelper.SKIP,
                 total_count=APIHelper.SKIP,
                 txid=APIHelper.SKIP):
        """Constructor for the LocationReport class"""

        # Initialize members of the class
        if dev_location_list is not APIHelper.SKIP:
            self.dev_location_list = dev_location_list 
        if has_more_data is not APIHelper.SKIP:
            self.has_more_data = has_more_data 
        if start_index is not APIHelper.SKIP:
            self.start_index = start_index 
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 
        if txid is not APIHelper.SKIP:
            self.txid = txid 

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
        dev_location_list = None
        if dictionary.get('devLocationList') is not None:
            dev_location_list = [Location.from_dictionary(x) for x in dictionary.get('devLocationList')]
        else:
            dev_location_list = APIHelper.SKIP
        has_more_data = dictionary.get("hasMoreData") if "hasMoreData" in dictionary.keys() else APIHelper.SKIP
        start_index = dictionary.get("startIndex") if dictionary.get("startIndex") else APIHelper.SKIP
        total_count = dictionary.get("totalCount") if dictionary.get("totalCount") else APIHelper.SKIP
        txid = dictionary.get("txid") if dictionary.get("txid") else APIHelper.SKIP
        # Return an object of this model
        return cls(dev_location_list,
                   has_more_data,
                   start_index,
                   total_count,
                   txid)
