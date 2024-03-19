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

class ModelJobJoinedDataQueryResponseDto(object):
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
        'name': 'str',
        'statement': 'str',
        'execution_id': 'str',
        'results': 'list[object]',
        'status': 'str',
        'dataset_id': 'str',
        'organization_id': 'str',
        'last_updated_by': 'str',
        'created_by': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'version': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'statement': 'statement',
        'execution_id': 'executionId',
        'results': 'results',
        'status': 'status',
        'dataset_id': 'datasetId',
        'organization_id': 'organizationId',
        'last_updated_by': 'lastUpdatedBy',
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, statement=None, execution_id=None, results=None, status=None, dataset_id=None, organization_id=None, last_updated_by=None, created_by=None, created_at=None, updated_at=None, version=None):  # noqa: E501
        """ModelJobJoinedDataQueryResponseDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._statement = None
        self._execution_id = None
        self._results = None
        self._status = None
        self._dataset_id = None
        self._organization_id = None
        self._last_updated_by = None
        self._created_by = None
        self._created_at = None
        self._updated_at = None
        self._version = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        self.statement = statement
        if execution_id is not None:
            self.execution_id = execution_id
        if results is not None:
            self.results = results
        if status is not None:
            self.status = status
        if dataset_id is not None:
            self.dataset_id = dataset_id
        self.organization_id = organization_id
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelJobJoinedDataQueryResponseDto.


        :param id: The id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The name of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelJobJoinedDataQueryResponseDto.


        :param name: The name of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def statement(self):
        """Gets the statement of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The statement of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._statement

    @statement.setter
    def statement(self, statement):
        """Sets the statement of this ModelJobJoinedDataQueryResponseDto.


        :param statement: The statement of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """
        if statement is None:
            raise ValueError("Invalid value for `statement`, must not be `None`")  # noqa: E501

        self._statement = statement

    @property
    def execution_id(self):
        """Gets the execution_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The execution_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        """Sets the execution_id of this ModelJobJoinedDataQueryResponseDto.


        :param execution_id: The execution_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """

        self._execution_id = execution_id

    @property
    def results(self):
        """Gets the results of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The results of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: list[object]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ModelJobJoinedDataQueryResponseDto.


        :param results: The results of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: list[object]
        """

        self._results = results

    @property
    def status(self):
        """Gets the status of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The status of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ModelJobJoinedDataQueryResponseDto.


        :param status: The status of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def dataset_id(self):
        """Gets the dataset_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The dataset_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this ModelJobJoinedDataQueryResponseDto.


        :param dataset_id: The dataset_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def organization_id(self):
        """Gets the organization_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The organization_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ModelJobJoinedDataQueryResponseDto.


        :param organization_id: The organization_id of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The last_updated_by of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this ModelJobJoinedDataQueryResponseDto.


        :param last_updated_by: The last_updated_by of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def created_by(self):
        """Gets the created_by of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The created_by of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ModelJobJoinedDataQueryResponseDto.


        :param created_by: The created_by of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The created_at of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelJobJoinedDataQueryResponseDto.


        :param created_at: The created_at of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The updated_at of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelJobJoinedDataQueryResponseDto.


        :param updated_at: The updated_at of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def version(self):
        """Gets the version of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501


        :return: The version of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelJobJoinedDataQueryResponseDto.


        :param version: The version of this ModelJobJoinedDataQueryResponseDto.  # noqa: E501
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
        if issubclass(ModelJobJoinedDataQueryResponseDto, dict):
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
        if not isinstance(other, ModelJobJoinedDataQueryResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
