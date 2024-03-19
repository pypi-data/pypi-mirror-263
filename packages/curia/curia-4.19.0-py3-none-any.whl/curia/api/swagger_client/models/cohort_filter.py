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

class CohortFilter(object):
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
        'dataset_id': 'str',
        'enabled': 'bool',
        'order': 'float',
        'period_definition': 'str',
        'period_preposition': 'str',
        'start_date': 'datetime',
        'end_date': 'datetime',
        'cohort_filter_conditions': 'list[CohortFilterCondition]',
        'type': 'str'
    }

    attribute_map = {
        'dataset_id': 'datasetId',
        'enabled': 'enabled',
        'order': 'order',
        'period_definition': 'periodDefinition',
        'period_preposition': 'periodPreposition',
        'start_date': 'startDate',
        'end_date': 'endDate',
        'cohort_filter_conditions': 'cohortFilterConditions',
        'type': 'type'
    }

    def __init__(self, dataset_id=None, enabled=None, order=None, period_definition=None, period_preposition=None, start_date=None, end_date=None, cohort_filter_conditions=None, type=None):  # noqa: E501
        """CohortFilter - a model defined in Swagger"""  # noqa: E501
        self._dataset_id = None
        self._enabled = None
        self._order = None
        self._period_definition = None
        self._period_preposition = None
        self._start_date = None
        self._end_date = None
        self._cohort_filter_conditions = None
        self._type = None
        self.discriminator = None
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if enabled is not None:
            self.enabled = enabled
        self.order = order
        if period_definition is not None:
            self.period_definition = period_definition
        if period_preposition is not None:
            self.period_preposition = period_preposition
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if cohort_filter_conditions is not None:
            self.cohort_filter_conditions = cohort_filter_conditions
        self.type = type

    @property
    def dataset_id(self):
        """Gets the dataset_id of this CohortFilter.  # noqa: E501


        :return: The dataset_id of this CohortFilter.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this CohortFilter.


        :param dataset_id: The dataset_id of this CohortFilter.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def enabled(self):
        """Gets the enabled of this CohortFilter.  # noqa: E501


        :return: The enabled of this CohortFilter.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this CohortFilter.


        :param enabled: The enabled of this CohortFilter.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def order(self):
        """Gets the order of this CohortFilter.  # noqa: E501


        :return: The order of this CohortFilter.  # noqa: E501
        :rtype: float
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this CohortFilter.


        :param order: The order of this CohortFilter.  # noqa: E501
        :type: float
        """
        if order is None:
            raise ValueError("Invalid value for `order`, must not be `None`")  # noqa: E501

        self._order = order

    @property
    def period_definition(self):
        """Gets the period_definition of this CohortFilter.  # noqa: E501


        :return: The period_definition of this CohortFilter.  # noqa: E501
        :rtype: str
        """
        return self._period_definition

    @period_definition.setter
    def period_definition(self, period_definition):
        """Sets the period_definition of this CohortFilter.


        :param period_definition: The period_definition of this CohortFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["evidence", "data_delay", "intervention", "pre_outcome_delay", "outcome", "diagnosis_gaps_validation", "diagnosis_gaps_follow_up", "data delay", "pre-outcome delay"]  # noqa: E501
        if period_definition not in allowed_values:
            raise ValueError(
                "Invalid value for `period_definition` ({0}), must be one of {1}"  # noqa: E501
                .format(period_definition, allowed_values)
            )

        self._period_definition = period_definition

    @property
    def period_preposition(self):
        """Gets the period_preposition of this CohortFilter.  # noqa: E501


        :return: The period_preposition of this CohortFilter.  # noqa: E501
        :rtype: str
        """
        return self._period_preposition

    @period_preposition.setter
    def period_preposition(self, period_preposition):
        """Sets the period_preposition of this CohortFilter.


        :param period_preposition: The period_preposition of this CohortFilter.  # noqa: E501
        :type: str
        """
        allowed_values = ["before", "during", "after", "outside"]  # noqa: E501
        if period_preposition not in allowed_values:
            raise ValueError(
                "Invalid value for `period_preposition` ({0}), must be one of {1}"  # noqa: E501
                .format(period_preposition, allowed_values)
            )

        self._period_preposition = period_preposition

    @property
    def start_date(self):
        """Gets the start_date of this CohortFilter.  # noqa: E501


        :return: The start_date of this CohortFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this CohortFilter.


        :param start_date: The start_date of this CohortFilter.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this CohortFilter.  # noqa: E501


        :return: The end_date of this CohortFilter.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this CohortFilter.


        :param end_date: The end_date of this CohortFilter.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def cohort_filter_conditions(self):
        """Gets the cohort_filter_conditions of this CohortFilter.  # noqa: E501


        :return: The cohort_filter_conditions of this CohortFilter.  # noqa: E501
        :rtype: list[CohortFilterCondition]
        """
        return self._cohort_filter_conditions

    @cohort_filter_conditions.setter
    def cohort_filter_conditions(self, cohort_filter_conditions):
        """Sets the cohort_filter_conditions of this CohortFilter.


        :param cohort_filter_conditions: The cohort_filter_conditions of this CohortFilter.  # noqa: E501
        :type: list[CohortFilterCondition]
        """

        self._cohort_filter_conditions = cohort_filter_conditions

    @property
    def type(self):
        """Gets the type of this CohortFilter.  # noqa: E501


        :return: The type of this CohortFilter.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CohortFilter.


        :param type: The type of this CohortFilter.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["cohort", "outcome", "intervention"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(CohortFilter, dict):
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
        if not isinstance(other, CohortFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
