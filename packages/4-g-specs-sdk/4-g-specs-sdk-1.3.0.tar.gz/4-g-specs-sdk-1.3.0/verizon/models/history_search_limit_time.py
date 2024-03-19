# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.api_helper import APIHelper
from verizon.models.numerical_data import NumericalData


class HistorySearchLimitTime(object):

    """Implementation of the 'HistorySearchLimitTime' model.

    The time period for which a request should retrieve data, beginning with
    the limitTime.startOn and proceeding with the limitTime.duration.

    Attributes:
        start_on (datetime): The starting date-time for this request.
        duration (NumericalData): Describes value and unit of time.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "start_on": 'startOn',
        "duration": 'duration'
    }

    _optionals = [
        'start_on',
        'duration',
    ]

    def __init__(self,
                 start_on=APIHelper.SKIP,
                 duration=APIHelper.SKIP):
        """Constructor for the HistorySearchLimitTime class"""

        # Initialize members of the class
        if start_on is not APIHelper.SKIP:
            self.start_on = APIHelper.apply_datetime_converter(start_on, APIHelper.RFC3339DateTime) if start_on else None 
        if duration is not APIHelper.SKIP:
            self.duration = duration 

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
        start_on = APIHelper.RFC3339DateTime.from_value(dictionary.get("startOn")).datetime if dictionary.get("startOn") else APIHelper.SKIP
        duration = NumericalData.from_dictionary(dictionary.get('duration')) if 'duration' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(start_on,
                   duration)
