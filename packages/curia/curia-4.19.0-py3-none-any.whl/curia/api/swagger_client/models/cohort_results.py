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

class CohortResults(object):
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
        'id': 'str',
        'cohort_definition_id': 'str',
        'cohort_definition': 'CohortDefinition',
        'model_population_id': 'str',
        'model_population': 'ModelPopulation',
        'cohort_list_query_id': 'str',
        'cohort_list_query': 'DataQuery',
        'cohort_count_query_id': 'str',
        'cohort_count_query': 'DataQuery',
        'outcome_list_query_id': 'str',
        'outcome_list_query': 'DataQuery',
        'outcome_count_query_id': 'str',
        'outcome_count_query': 'DataQuery',
        'intervention_list_query_id': 'str',
        'intervention_list_query': 'DataQuery',
        'intervention_count_query_id': 'str',
        'intervention_count_query': 'DataQuery',
        'created_at': 'datetime',
        'created_by': 'str',
        'updated_at': 'datetime',
        'archived_at': 'datetime',
        'last_updated_by': 'str',
        'version': 'float'
    }

    attribute_map = {
        'id': 'id',
        'cohort_definition_id': 'cohortDefinitionId',
        'cohort_definition': 'cohortDefinition',
        'model_population_id': 'modelPopulationId',
        'model_population': 'modelPopulation',
        'cohort_list_query_id': 'cohortListQueryId',
        'cohort_list_query': 'cohortListQuery',
        'cohort_count_query_id': 'cohortCountQueryId',
        'cohort_count_query': 'cohortCountQuery',
        'outcome_list_query_id': 'outcomeListQueryId',
        'outcome_list_query': 'outcomeListQuery',
        'outcome_count_query_id': 'outcomeCountQueryId',
        'outcome_count_query': 'outcomeCountQuery',
        'intervention_list_query_id': 'interventionListQueryId',
        'intervention_list_query': 'interventionListQuery',
        'intervention_count_query_id': 'interventionCountQueryId',
        'intervention_count_query': 'interventionCountQuery',
        'created_at': 'createdAt',
        'created_by': 'createdBy',
        'updated_at': 'updatedAt',
        'archived_at': 'archivedAt',
        'last_updated_by': 'lastUpdatedBy',
        'version': 'version'
    }

    def __init__(self, id=None, cohort_definition_id=None, cohort_definition=None, model_population_id=None, model_population=None, cohort_list_query_id=None, cohort_list_query=None, cohort_count_query_id=None, cohort_count_query=None, outcome_list_query_id=None, outcome_list_query=None, outcome_count_query_id=None, outcome_count_query=None, intervention_list_query_id=None, intervention_list_query=None, intervention_count_query_id=None, intervention_count_query=None, created_at=None, created_by=None, updated_at=None, archived_at=None, last_updated_by=None, version=None):  # noqa: E501
        """CohortResults - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._cohort_definition_id = None
        self._cohort_definition = None
        self._model_population_id = None
        self._model_population = None
        self._cohort_list_query_id = None
        self._cohort_list_query = None
        self._cohort_count_query_id = None
        self._cohort_count_query = None
        self._outcome_list_query_id = None
        self._outcome_list_query = None
        self._outcome_count_query_id = None
        self._outcome_count_query = None
        self._intervention_list_query_id = None
        self._intervention_list_query = None
        self._intervention_count_query_id = None
        self._intervention_count_query = None
        self._created_at = None
        self._created_by = None
        self._updated_at = None
        self._archived_at = None
        self._last_updated_by = None
        self._version = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.cohort_definition_id = cohort_definition_id
        if cohort_definition is not None:
            self.cohort_definition = cohort_definition
        self.model_population_id = model_population_id
        if model_population is not None:
            self.model_population = model_population
        if cohort_list_query_id is not None:
            self.cohort_list_query_id = cohort_list_query_id
        if cohort_list_query is not None:
            self.cohort_list_query = cohort_list_query
        if cohort_count_query_id is not None:
            self.cohort_count_query_id = cohort_count_query_id
        if cohort_count_query is not None:
            self.cohort_count_query = cohort_count_query
        if outcome_list_query_id is not None:
            self.outcome_list_query_id = outcome_list_query_id
        if outcome_list_query is not None:
            self.outcome_list_query = outcome_list_query
        if outcome_count_query_id is not None:
            self.outcome_count_query_id = outcome_count_query_id
        if outcome_count_query is not None:
            self.outcome_count_query = outcome_count_query
        if intervention_list_query_id is not None:
            self.intervention_list_query_id = intervention_list_query_id
        if intervention_list_query is not None:
            self.intervention_list_query = intervention_list_query
        if intervention_count_query_id is not None:
            self.intervention_count_query_id = intervention_count_query_id
        if intervention_count_query is not None:
            self.intervention_count_query = intervention_count_query
        if created_at is not None:
            self.created_at = created_at
        if created_by is not None:
            self.created_by = created_by
        if updated_at is not None:
            self.updated_at = updated_at
        if archived_at is not None:
            self.archived_at = archived_at
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this CohortResults.  # noqa: E501


        :return: The id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CohortResults.


        :param id: The id of this CohortResults.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def cohort_definition_id(self):
        """Gets the cohort_definition_id of this CohortResults.  # noqa: E501


        :return: The cohort_definition_id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._cohort_definition_id

    @cohort_definition_id.setter
    def cohort_definition_id(self, cohort_definition_id):
        """Sets the cohort_definition_id of this CohortResults.


        :param cohort_definition_id: The cohort_definition_id of this CohortResults.  # noqa: E501
        :type: str
        """
        if cohort_definition_id is None:
            raise ValueError("Invalid value for `cohort_definition_id`, must not be `None`")  # noqa: E501

        self._cohort_definition_id = cohort_definition_id

    @property
    def cohort_definition(self):
        """Gets the cohort_definition of this CohortResults.  # noqa: E501


        :return: The cohort_definition of this CohortResults.  # noqa: E501
        :rtype: CohortDefinition
        """
        return self._cohort_definition

    @cohort_definition.setter
    def cohort_definition(self, cohort_definition):
        """Sets the cohort_definition of this CohortResults.


        :param cohort_definition: The cohort_definition of this CohortResults.  # noqa: E501
        :type: CohortDefinition
        """

        self._cohort_definition = cohort_definition

    @property
    def model_population_id(self):
        """Gets the model_population_id of this CohortResults.  # noqa: E501


        :return: The model_population_id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._model_population_id

    @model_population_id.setter
    def model_population_id(self, model_population_id):
        """Sets the model_population_id of this CohortResults.


        :param model_population_id: The model_population_id of this CohortResults.  # noqa: E501
        :type: str
        """
        if model_population_id is None:
            raise ValueError("Invalid value for `model_population_id`, must not be `None`")  # noqa: E501

        self._model_population_id = model_population_id

    @property
    def model_population(self):
        """Gets the model_population of this CohortResults.  # noqa: E501


        :return: The model_population of this CohortResults.  # noqa: E501
        :rtype: ModelPopulation
        """
        return self._model_population

    @model_population.setter
    def model_population(self, model_population):
        """Sets the model_population of this CohortResults.


        :param model_population: The model_population of this CohortResults.  # noqa: E501
        :type: ModelPopulation
        """

        self._model_population = model_population

    @property
    def cohort_list_query_id(self):
        """Gets the cohort_list_query_id of this CohortResults.  # noqa: E501


        :return: The cohort_list_query_id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._cohort_list_query_id

    @cohort_list_query_id.setter
    def cohort_list_query_id(self, cohort_list_query_id):
        """Sets the cohort_list_query_id of this CohortResults.


        :param cohort_list_query_id: The cohort_list_query_id of this CohortResults.  # noqa: E501
        :type: str
        """

        self._cohort_list_query_id = cohort_list_query_id

    @property
    def cohort_list_query(self):
        """Gets the cohort_list_query of this CohortResults.  # noqa: E501


        :return: The cohort_list_query of this CohortResults.  # noqa: E501
        :rtype: DataQuery
        """
        return self._cohort_list_query

    @cohort_list_query.setter
    def cohort_list_query(self, cohort_list_query):
        """Sets the cohort_list_query of this CohortResults.


        :param cohort_list_query: The cohort_list_query of this CohortResults.  # noqa: E501
        :type: DataQuery
        """

        self._cohort_list_query = cohort_list_query

    @property
    def cohort_count_query_id(self):
        """Gets the cohort_count_query_id of this CohortResults.  # noqa: E501


        :return: The cohort_count_query_id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._cohort_count_query_id

    @cohort_count_query_id.setter
    def cohort_count_query_id(self, cohort_count_query_id):
        """Sets the cohort_count_query_id of this CohortResults.


        :param cohort_count_query_id: The cohort_count_query_id of this CohortResults.  # noqa: E501
        :type: str
        """

        self._cohort_count_query_id = cohort_count_query_id

    @property
    def cohort_count_query(self):
        """Gets the cohort_count_query of this CohortResults.  # noqa: E501


        :return: The cohort_count_query of this CohortResults.  # noqa: E501
        :rtype: DataQuery
        """
        return self._cohort_count_query

    @cohort_count_query.setter
    def cohort_count_query(self, cohort_count_query):
        """Sets the cohort_count_query of this CohortResults.


        :param cohort_count_query: The cohort_count_query of this CohortResults.  # noqa: E501
        :type: DataQuery
        """

        self._cohort_count_query = cohort_count_query

    @property
    def outcome_list_query_id(self):
        """Gets the outcome_list_query_id of this CohortResults.  # noqa: E501


        :return: The outcome_list_query_id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._outcome_list_query_id

    @outcome_list_query_id.setter
    def outcome_list_query_id(self, outcome_list_query_id):
        """Sets the outcome_list_query_id of this CohortResults.


        :param outcome_list_query_id: The outcome_list_query_id of this CohortResults.  # noqa: E501
        :type: str
        """

        self._outcome_list_query_id = outcome_list_query_id

    @property
    def outcome_list_query(self):
        """Gets the outcome_list_query of this CohortResults.  # noqa: E501


        :return: The outcome_list_query of this CohortResults.  # noqa: E501
        :rtype: DataQuery
        """
        return self._outcome_list_query

    @outcome_list_query.setter
    def outcome_list_query(self, outcome_list_query):
        """Sets the outcome_list_query of this CohortResults.


        :param outcome_list_query: The outcome_list_query of this CohortResults.  # noqa: E501
        :type: DataQuery
        """

        self._outcome_list_query = outcome_list_query

    @property
    def outcome_count_query_id(self):
        """Gets the outcome_count_query_id of this CohortResults.  # noqa: E501


        :return: The outcome_count_query_id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._outcome_count_query_id

    @outcome_count_query_id.setter
    def outcome_count_query_id(self, outcome_count_query_id):
        """Sets the outcome_count_query_id of this CohortResults.


        :param outcome_count_query_id: The outcome_count_query_id of this CohortResults.  # noqa: E501
        :type: str
        """

        self._outcome_count_query_id = outcome_count_query_id

    @property
    def outcome_count_query(self):
        """Gets the outcome_count_query of this CohortResults.  # noqa: E501


        :return: The outcome_count_query of this CohortResults.  # noqa: E501
        :rtype: DataQuery
        """
        return self._outcome_count_query

    @outcome_count_query.setter
    def outcome_count_query(self, outcome_count_query):
        """Sets the outcome_count_query of this CohortResults.


        :param outcome_count_query: The outcome_count_query of this CohortResults.  # noqa: E501
        :type: DataQuery
        """

        self._outcome_count_query = outcome_count_query

    @property
    def intervention_list_query_id(self):
        """Gets the intervention_list_query_id of this CohortResults.  # noqa: E501


        :return: The intervention_list_query_id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._intervention_list_query_id

    @intervention_list_query_id.setter
    def intervention_list_query_id(self, intervention_list_query_id):
        """Sets the intervention_list_query_id of this CohortResults.


        :param intervention_list_query_id: The intervention_list_query_id of this CohortResults.  # noqa: E501
        :type: str
        """

        self._intervention_list_query_id = intervention_list_query_id

    @property
    def intervention_list_query(self):
        """Gets the intervention_list_query of this CohortResults.  # noqa: E501


        :return: The intervention_list_query of this CohortResults.  # noqa: E501
        :rtype: DataQuery
        """
        return self._intervention_list_query

    @intervention_list_query.setter
    def intervention_list_query(self, intervention_list_query):
        """Sets the intervention_list_query of this CohortResults.


        :param intervention_list_query: The intervention_list_query of this CohortResults.  # noqa: E501
        :type: DataQuery
        """

        self._intervention_list_query = intervention_list_query

    @property
    def intervention_count_query_id(self):
        """Gets the intervention_count_query_id of this CohortResults.  # noqa: E501


        :return: The intervention_count_query_id of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._intervention_count_query_id

    @intervention_count_query_id.setter
    def intervention_count_query_id(self, intervention_count_query_id):
        """Sets the intervention_count_query_id of this CohortResults.


        :param intervention_count_query_id: The intervention_count_query_id of this CohortResults.  # noqa: E501
        :type: str
        """

        self._intervention_count_query_id = intervention_count_query_id

    @property
    def intervention_count_query(self):
        """Gets the intervention_count_query of this CohortResults.  # noqa: E501


        :return: The intervention_count_query of this CohortResults.  # noqa: E501
        :rtype: DataQuery
        """
        return self._intervention_count_query

    @intervention_count_query.setter
    def intervention_count_query(self, intervention_count_query):
        """Sets the intervention_count_query of this CohortResults.


        :param intervention_count_query: The intervention_count_query of this CohortResults.  # noqa: E501
        :type: DataQuery
        """

        self._intervention_count_query = intervention_count_query

    @property
    def created_at(self):
        """Gets the created_at of this CohortResults.  # noqa: E501


        :return: The created_at of this CohortResults.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CohortResults.


        :param created_at: The created_at of this CohortResults.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this CohortResults.  # noqa: E501


        :return: The created_by of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CohortResults.


        :param created_by: The created_by of this CohortResults.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def updated_at(self):
        """Gets the updated_at of this CohortResults.  # noqa: E501


        :return: The updated_at of this CohortResults.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CohortResults.


        :param updated_at: The updated_at of this CohortResults.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def archived_at(self):
        """Gets the archived_at of this CohortResults.  # noqa: E501


        :return: The archived_at of this CohortResults.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this CohortResults.


        :param archived_at: The archived_at of this CohortResults.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this CohortResults.  # noqa: E501


        :return: The last_updated_by of this CohortResults.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this CohortResults.


        :param last_updated_by: The last_updated_by of this CohortResults.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def version(self):
        """Gets the version of this CohortResults.  # noqa: E501


        :return: The version of this CohortResults.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CohortResults.


        :param version: The version of this CohortResults.  # noqa: E501
        :type: float
        """

        self._version = version

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
        if issubclass(CohortResults, dict):
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
        if not isinstance(other, CohortResults):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
