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

class ModelJobJoinedModelJobOutputResponseDto(object):
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
        'name': 'object',
        'data': 'object',
        'model_job_id': 'str',
        'dataset_id': 'str',
        'last_updated_by': 'str',
        'created_by': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'archived_at': 'datetime',
        'version': 'float'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'data': 'data',
        'model_job_id': 'modelJobId',
        'dataset_id': 'datasetId',
        'last_updated_by': 'lastUpdatedBy',
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'archived_at': 'archivedAt',
        'version': 'version'
    }

    def __init__(self, id=None, name=None, data=None, model_job_id=None, dataset_id=None, last_updated_by=None, created_by=None, created_at=None, updated_at=None, archived_at=None, version=None):  # noqa: E501
        """ModelJobJoinedModelJobOutputResponseDto - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._data = None
        self._model_job_id = None
        self._dataset_id = None
        self._last_updated_by = None
        self._created_by = None
        self._created_at = None
        self._updated_at = None
        self._archived_at = None
        self._version = None
        self.discriminator = None
        if id is not None:
            self.id = id
        self.name = name
        self.data = data
        self.model_job_id = model_job_id
        if dataset_id is not None:
            self.dataset_id = dataset_id
        if last_updated_by is not None:
            self.last_updated_by = last_updated_by
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if archived_at is not None:
            self.archived_at = archived_at
        if version is not None:
            self.version = version

    @property
    def id(self):
        """Gets the id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ModelJobJoinedModelJobOutputResponseDto.


        :param id: The id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The name of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: object
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ModelJobJoinedModelJobOutputResponseDto.


        :param name: The name of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: object
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def data(self):
        """Gets the data of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The data of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ModelJobJoinedModelJobOutputResponseDto.


        :param data: The data of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def model_job_id(self):
        """Gets the model_job_id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The model_job_id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._model_job_id

    @model_job_id.setter
    def model_job_id(self, model_job_id):
        """Sets the model_job_id of this ModelJobJoinedModelJobOutputResponseDto.


        :param model_job_id: The model_job_id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: str
        """
        if model_job_id is None:
            raise ValueError("Invalid value for `model_job_id`, must not be `None`")  # noqa: E501

        self._model_job_id = model_job_id

    @property
    def dataset_id(self):
        """Gets the dataset_id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The dataset_id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._dataset_id

    @dataset_id.setter
    def dataset_id(self, dataset_id):
        """Sets the dataset_id of this ModelJobJoinedModelJobOutputResponseDto.


        :param dataset_id: The dataset_id of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: str
        """

        self._dataset_id = dataset_id

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The last_updated_by of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this ModelJobJoinedModelJobOutputResponseDto.


        :param last_updated_by: The last_updated_by of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def created_by(self):
        """Gets the created_by of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The created_by of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ModelJobJoinedModelJobOutputResponseDto.


        :param created_by: The created_by of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The created_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ModelJobJoinedModelJobOutputResponseDto.


        :param created_at: The created_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The updated_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ModelJobJoinedModelJobOutputResponseDto.


        :param updated_at: The updated_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def archived_at(self):
        """Gets the archived_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The archived_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this ModelJobJoinedModelJobOutputResponseDto.


        :param archived_at: The archived_at of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

    @property
    def version(self):
        """Gets the version of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501


        :return: The version of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ModelJobJoinedModelJobOutputResponseDto.


        :param version: The version of this ModelJobJoinedModelJobOutputResponseDto.  # noqa: E501
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
        if issubclass(ModelJobJoinedModelJobOutputResponseDto, dict):
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
        if not isinstance(other, ModelJobJoinedModelJobOutputResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
