# -*- coding: utf-8 -*-

"""
verizon

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from verizon.models.coordinates import Coordinates


class Locationscoord(object):

    """Implementation of the 'Locationscoord' model.

    Location coordinates.

    Attributes:
        coordinates_list (List[Coordinates]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "coordinates_list": 'coordinatesList'
    }

    def __init__(self,
                 coordinates_list=None):
        """Constructor for the Locationscoord class"""

        # Initialize members of the class
        self.coordinates_list = coordinates_list 

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
        coordinates_list = None
        if dictionary.get('coordinatesList') is not None:
            coordinates_list = [Coordinates.from_dictionary(x) for x in dictionary.get('coordinatesList')]
        # Return an object of this model
        return cls(coordinates_list)
