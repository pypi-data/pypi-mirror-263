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

class UpdateModelPopulationDto(object):
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
        'query_count_status': 'str',
        'query_count_error': 'str',
        'query_list_status': 'str',
        'query_list_error': 'str',
        'query_all_status': 'str',
        'query_all_error': 'str',
        'query_count_started_at': 'datetime',
        'query_count_ended_at': 'datetime',
        'query_list_started_at': 'datetime',
        'query_list_ended_at': 'datetime',
        'query_all_started_at': 'datetime',
        'query_all_ended_at': 'datetime',
        'population_id': 'str',
        'data_query_id': 'str',
        'outcome_distribution_histogram_query_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'query_count_status': 'queryCountStatus',
        'query_count_error': 'queryCountError',
        'query_list_status': 'queryListStatus',
        'query_list_error': 'queryListError',
        'query_all_status': 'queryAllStatus',
        'query_all_error': 'queryAllError',
        'query_count_started_at': 'queryCountStartedAt',
        'query_count_ended_at': 'queryCountEndedAt',
        'query_list_started_at': 'queryListStartedAt',
        'query_list_ended_at': 'queryListEndedAt',
        'query_all_started_at': 'queryAllStartedAt',
        'query_all_ended_at': 'queryAllEndedAt',
        'population_id': 'populationId',
        'data_query_id': 'dataQueryId',
        'outcome_distribution_histogram_query_id': 'outcomeDistributionHistogramQueryId'
    }

    def __init__(self, name=None, query_count_status=None, query_count_error=None, query_list_status=None, query_list_error=None, query_all_status=None, query_all_error=None, query_count_started_at=None, query_count_ended_at=None, query_list_started_at=None, query_list_ended_at=None, query_all_started_at=None, query_all_ended_at=None, population_id=None, data_query_id=None, outcome_distribution_histogram_query_id=None):  # noqa: E501
        """UpdateModelPopulationDto - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._query_count_status = None
        self._query_count_error = None
        self._query_list_status = None
        self._query_list_error = None
        self._query_all_status = None
        self._query_all_error = None
        self._query_count_started_at = None
        self._query_count_ended_at = None
        self._query_list_started_at = None
        self._query_list_ended_at = None
        self._query_all_started_at = None
        self._query_all_ended_at = None
        self._population_id = None
        self._data_query_id = None
        self._outcome_distribution_histogram_query_id = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if query_count_status is not None:
            self.query_count_status = query_count_status
        if query_count_error is not None:
            self.query_count_error = query_count_error
        if query_list_status is not None:
            self.query_list_status = query_list_status
        if query_list_error is not None:
            self.query_list_error = query_list_error
        if query_all_status is not None:
            self.query_all_status = query_all_status
        if query_all_error is not None:
            self.query_all_error = query_all_error
        if query_count_started_at is not None:
            self.query_count_started_at = query_count_started_at
        if query_count_ended_at is not None:
            self.query_count_ended_at = query_count_ended_at
        if query_list_started_at is not None:
            self.query_list_started_at = query_list_started_at
        if query_list_ended_at is not None:
            self.query_list_ended_at = query_list_ended_at
        if query_all_started_at is not None:
            self.query_all_started_at = query_all_started_at
        if query_all_ended_at is not None:
            self.query_all_ended_at = query_all_ended_at
        if population_id is not None:
            self.population_id = population_id
        if data_query_id is not None:
            self.data_query_id = data_query_id
        if outcome_distribution_histogram_query_id is not None:
            self.outcome_distribution_histogram_query_id = outcome_distribution_histogram_query_id

    @property
    def name(self):
        """Gets the name of this UpdateModelPopulationDto.  # noqa: E501


        :return: The name of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateModelPopulationDto.


        :param name: The name of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def query_count_status(self):
        """Gets the query_count_status of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_count_status of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._query_count_status

    @query_count_status.setter
    def query_count_status(self, query_count_status):
        """Sets the query_count_status of this UpdateModelPopulationDto.


        :param query_count_status: The query_count_status of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._query_count_status = query_count_status

    @property
    def query_count_error(self):
        """Gets the query_count_error of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_count_error of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._query_count_error

    @query_count_error.setter
    def query_count_error(self, query_count_error):
        """Sets the query_count_error of this UpdateModelPopulationDto.


        :param query_count_error: The query_count_error of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._query_count_error = query_count_error

    @property
    def query_list_status(self):
        """Gets the query_list_status of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_list_status of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._query_list_status

    @query_list_status.setter
    def query_list_status(self, query_list_status):
        """Sets the query_list_status of this UpdateModelPopulationDto.


        :param query_list_status: The query_list_status of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._query_list_status = query_list_status

    @property
    def query_list_error(self):
        """Gets the query_list_error of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_list_error of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._query_list_error

    @query_list_error.setter
    def query_list_error(self, query_list_error):
        """Sets the query_list_error of this UpdateModelPopulationDto.


        :param query_list_error: The query_list_error of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._query_list_error = query_list_error

    @property
    def query_all_status(self):
        """Gets the query_all_status of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_all_status of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._query_all_status

    @query_all_status.setter
    def query_all_status(self, query_all_status):
        """Sets the query_all_status of this UpdateModelPopulationDto.


        :param query_all_status: The query_all_status of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._query_all_status = query_all_status

    @property
    def query_all_error(self):
        """Gets the query_all_error of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_all_error of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._query_all_error

    @query_all_error.setter
    def query_all_error(self, query_all_error):
        """Sets the query_all_error of this UpdateModelPopulationDto.


        :param query_all_error: The query_all_error of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._query_all_error = query_all_error

    @property
    def query_count_started_at(self):
        """Gets the query_count_started_at of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_count_started_at of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: datetime
        """
        return self._query_count_started_at

    @query_count_started_at.setter
    def query_count_started_at(self, query_count_started_at):
        """Sets the query_count_started_at of this UpdateModelPopulationDto.


        :param query_count_started_at: The query_count_started_at of this UpdateModelPopulationDto.  # noqa: E501
        :type: datetime
        """

        self._query_count_started_at = query_count_started_at

    @property
    def query_count_ended_at(self):
        """Gets the query_count_ended_at of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_count_ended_at of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: datetime
        """
        return self._query_count_ended_at

    @query_count_ended_at.setter
    def query_count_ended_at(self, query_count_ended_at):
        """Sets the query_count_ended_at of this UpdateModelPopulationDto.


        :param query_count_ended_at: The query_count_ended_at of this UpdateModelPopulationDto.  # noqa: E501
        :type: datetime
        """

        self._query_count_ended_at = query_count_ended_at

    @property
    def query_list_started_at(self):
        """Gets the query_list_started_at of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_list_started_at of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: datetime
        """
        return self._query_list_started_at

    @query_list_started_at.setter
    def query_list_started_at(self, query_list_started_at):
        """Sets the query_list_started_at of this UpdateModelPopulationDto.


        :param query_list_started_at: The query_list_started_at of this UpdateModelPopulationDto.  # noqa: E501
        :type: datetime
        """

        self._query_list_started_at = query_list_started_at

    @property
    def query_list_ended_at(self):
        """Gets the query_list_ended_at of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_list_ended_at of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: datetime
        """
        return self._query_list_ended_at

    @query_list_ended_at.setter
    def query_list_ended_at(self, query_list_ended_at):
        """Sets the query_list_ended_at of this UpdateModelPopulationDto.


        :param query_list_ended_at: The query_list_ended_at of this UpdateModelPopulationDto.  # noqa: E501
        :type: datetime
        """

        self._query_list_ended_at = query_list_ended_at

    @property
    def query_all_started_at(self):
        """Gets the query_all_started_at of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_all_started_at of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: datetime
        """
        return self._query_all_started_at

    @query_all_started_at.setter
    def query_all_started_at(self, query_all_started_at):
        """Sets the query_all_started_at of this UpdateModelPopulationDto.


        :param query_all_started_at: The query_all_started_at of this UpdateModelPopulationDto.  # noqa: E501
        :type: datetime
        """

        self._query_all_started_at = query_all_started_at

    @property
    def query_all_ended_at(self):
        """Gets the query_all_ended_at of this UpdateModelPopulationDto.  # noqa: E501


        :return: The query_all_ended_at of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: datetime
        """
        return self._query_all_ended_at

    @query_all_ended_at.setter
    def query_all_ended_at(self, query_all_ended_at):
        """Sets the query_all_ended_at of this UpdateModelPopulationDto.


        :param query_all_ended_at: The query_all_ended_at of this UpdateModelPopulationDto.  # noqa: E501
        :type: datetime
        """

        self._query_all_ended_at = query_all_ended_at

    @property
    def population_id(self):
        """Gets the population_id of this UpdateModelPopulationDto.  # noqa: E501


        :return: The population_id of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._population_id

    @population_id.setter
    def population_id(self, population_id):
        """Sets the population_id of this UpdateModelPopulationDto.


        :param population_id: The population_id of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._population_id = population_id

    @property
    def data_query_id(self):
        """Gets the data_query_id of this UpdateModelPopulationDto.  # noqa: E501


        :return: The data_query_id of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._data_query_id

    @data_query_id.setter
    def data_query_id(self, data_query_id):
        """Sets the data_query_id of this UpdateModelPopulationDto.


        :param data_query_id: The data_query_id of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._data_query_id = data_query_id

    @property
    def outcome_distribution_histogram_query_id(self):
        """Gets the outcome_distribution_histogram_query_id of this UpdateModelPopulationDto.  # noqa: E501


        :return: The outcome_distribution_histogram_query_id of this UpdateModelPopulationDto.  # noqa: E501
        :rtype: str
        """
        return self._outcome_distribution_histogram_query_id

    @outcome_distribution_histogram_query_id.setter
    def outcome_distribution_histogram_query_id(self, outcome_distribution_histogram_query_id):
        """Sets the outcome_distribution_histogram_query_id of this UpdateModelPopulationDto.


        :param outcome_distribution_histogram_query_id: The outcome_distribution_histogram_query_id of this UpdateModelPopulationDto.  # noqa: E501
        :type: str
        """

        self._outcome_distribution_histogram_query_id = outcome_distribution_histogram_query_id

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
        if issubclass(UpdateModelPopulationDto, dict):
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
        if not isinstance(other, UpdateModelPopulationDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
