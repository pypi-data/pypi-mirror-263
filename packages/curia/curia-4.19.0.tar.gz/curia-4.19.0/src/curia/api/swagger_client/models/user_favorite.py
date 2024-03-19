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

class UserFavorite(object):
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
        'user_id': 'str',
        'favorite_model_id': 'str',
        'favorite_project_id': 'str',
        'model': 'Model',
        'project': 'Project',
        'last_updated_by': 'str',
        'created_by': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'archived_at': 'datetime',
        'version': 'float'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'userId',
        'favorite_model_id': 'favoriteModelId',
        'favorite_project_id': 'favoriteProjectId',
        'model': 'model',
        'project': 'project',
        'last_updated_by': 'lastUpdatedBy',
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'archived_at': 'archivedAt',
        'version': 'version'
    }

    def __init__(self, id=None, user_id=None, favorite_model_id=None, favorite_project_id=None, model=None, project=None, last_updated_by=None, created_by=None, created_at=None, updated_at=None, archived_at=None, version=None):  # noqa: E501
        """UserFavorite - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._user_id = None
        self._favorite_model_id = None
        self._favorite_project_id = None
        self._model = None
        self._project = None
        self._last_updated_by = None
        self._created_by = None
        self._created_at = None
        self._updated_at = None
        self._archived_at = None
        self._version = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if favorite_model_id is not None:
            self.favorite_model_id = favorite_model_id
        if favorite_project_id is not None:
            self.favorite_project_id = favorite_project_id
        if model is not None:
            self.model = model
        if project is not None:
            self.project = project
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
        """Gets the id of this UserFavorite.  # noqa: E501


        :return: The id of this UserFavorite.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserFavorite.


        :param id: The id of this UserFavorite.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def user_id(self):
        """Gets the user_id of this UserFavorite.  # noqa: E501


        :return: The user_id of this UserFavorite.  # noqa: E501
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this UserFavorite.


        :param user_id: The user_id of this UserFavorite.  # noqa: E501
        :type: str
        """

        self._user_id = user_id

    @property
    def favorite_model_id(self):
        """Gets the favorite_model_id of this UserFavorite.  # noqa: E501


        :return: The favorite_model_id of this UserFavorite.  # noqa: E501
        :rtype: str
        """
        return self._favorite_model_id

    @favorite_model_id.setter
    def favorite_model_id(self, favorite_model_id):
        """Sets the favorite_model_id of this UserFavorite.


        :param favorite_model_id: The favorite_model_id of this UserFavorite.  # noqa: E501
        :type: str
        """

        self._favorite_model_id = favorite_model_id

    @property
    def favorite_project_id(self):
        """Gets the favorite_project_id of this UserFavorite.  # noqa: E501


        :return: The favorite_project_id of this UserFavorite.  # noqa: E501
        :rtype: str
        """
        return self._favorite_project_id

    @favorite_project_id.setter
    def favorite_project_id(self, favorite_project_id):
        """Sets the favorite_project_id of this UserFavorite.


        :param favorite_project_id: The favorite_project_id of this UserFavorite.  # noqa: E501
        :type: str
        """

        self._favorite_project_id = favorite_project_id

    @property
    def model(self):
        """Gets the model of this UserFavorite.  # noqa: E501


        :return: The model of this UserFavorite.  # noqa: E501
        :rtype: Model
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this UserFavorite.


        :param model: The model of this UserFavorite.  # noqa: E501
        :type: Model
        """

        self._model = model

    @property
    def project(self):
        """Gets the project of this UserFavorite.  # noqa: E501


        :return: The project of this UserFavorite.  # noqa: E501
        :rtype: Project
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this UserFavorite.


        :param project: The project of this UserFavorite.  # noqa: E501
        :type: Project
        """

        self._project = project

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this UserFavorite.  # noqa: E501


        :return: The last_updated_by of this UserFavorite.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this UserFavorite.


        :param last_updated_by: The last_updated_by of this UserFavorite.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def created_by(self):
        """Gets the created_by of this UserFavorite.  # noqa: E501


        :return: The created_by of this UserFavorite.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this UserFavorite.


        :param created_by: The created_by of this UserFavorite.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this UserFavorite.  # noqa: E501


        :return: The created_at of this UserFavorite.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this UserFavorite.


        :param created_at: The created_at of this UserFavorite.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this UserFavorite.  # noqa: E501


        :return: The updated_at of this UserFavorite.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this UserFavorite.


        :param updated_at: The updated_at of this UserFavorite.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def archived_at(self):
        """Gets the archived_at of this UserFavorite.  # noqa: E501


        :return: The archived_at of this UserFavorite.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this UserFavorite.


        :param archived_at: The archived_at of this UserFavorite.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

    @property
    def version(self):
        """Gets the version of this UserFavorite.  # noqa: E501


        :return: The version of this UserFavorite.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UserFavorite.


        :param version: The version of this UserFavorite.  # noqa: E501
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
        if issubclass(UserFavorite, dict):
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
        if not isinstance(other, UserFavorite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
