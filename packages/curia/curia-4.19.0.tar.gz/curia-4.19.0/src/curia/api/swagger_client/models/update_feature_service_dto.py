# coding: utf-8

"""
    Curia Platform API

    These are the docs for the curia platform API. To test, generate an authorization token first.  # noqa: E501

    OpenAPI spec version: 3.13.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateFeatureServiceDto(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'description': 'str',
        'synced_at': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'synced_at': 'syncedAt'
    }

    def __init__(self, name=None, description=None, synced_at=None):  # noqa: E501
        """UpdateFeatureServiceDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._synced_at = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if synced_at is not None:
            self.synced_at = synced_at

    @property
    def name(self):
        """Gets the name of this UpdateFeatureServiceDto.  # noqa: E501


        :return: The name of this UpdateFeatureServiceDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateFeatureServiceDto.


        :param name: The name of this UpdateFeatureServiceDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateFeatureServiceDto.  # noqa: E501


        :return: The description of this UpdateFeatureServiceDto.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateFeatureServiceDto.


        :param description: The description of this UpdateFeatureServiceDto.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def synced_at(self):
        """Gets the synced_at of this UpdateFeatureServiceDto.  # noqa: E501


        :return: The synced_at of this UpdateFeatureServiceDto.  # noqa: E501
        :rtype: datetime
        """
        return self._synced_at

    @synced_at.setter
    def synced_at(self, synced_at):
        """Sets the synced_at of this UpdateFeatureServiceDto.


        :param synced_at: The synced_at of this UpdateFeatureServiceDto.  # noqa: E501
        :type: datetime
        """

        self._synced_at = synced_at

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateFeatureServiceDto, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateFeatureServiceDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
