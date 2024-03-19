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

class Scheduler(object):
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
        'last_updated_by': 'str',
        'created_by': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'archived_at': 'datetime',
        'version': 'float',
        'type': 'str',
        'workflow_id': 'str',
        'schedule': 'str',
        'parameters': 'WorkflowTemplateParameters',
        'organization_id': 'str',
        'job_key': 'str',
        'last_run_at': 'datetime',
        'next_run_at': 'datetime',
        'is_paused': 'object',
        'organization': 'Organization',
        'workflow': 'Workflow'
    }

    attribute_map = {
        'id': 'id',
        'last_updated_by': 'lastUpdatedBy',
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'updated_at': 'updatedAt',
        'archived_at': 'archivedAt',
        'version': 'version',
        'type': 'type',
        'workflow_id': 'workflowId',
        'schedule': 'schedule',
        'parameters': 'parameters',
        'organization_id': 'organizationId',
        'job_key': 'jobKey',
        'last_run_at': 'lastRunAt',
        'next_run_at': 'nextRunAt',
        'is_paused': 'isPaused',
        'organization': 'organization',
        'workflow': 'workflow'
    }

    def __init__(self, id=None, last_updated_by=None, created_by=None, created_at=None, updated_at=None, archived_at=None, version=None, type=None, workflow_id=None, schedule=None, parameters=None, organization_id=None, job_key=None, last_run_at=None, next_run_at=None, is_paused=None, organization=None, workflow=None):  # noqa: E501
        """Scheduler - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._last_updated_by = None
        self._created_by = None
        self._created_at = None
        self._updated_at = None
        self._archived_at = None
        self._version = None
        self._type = None
        self._workflow_id = None
        self._schedule = None
        self._parameters = None
        self._organization_id = None
        self._job_key = None
        self._last_run_at = None
        self._next_run_at = None
        self._is_paused = None
        self._organization = None
        self._workflow = None
        self.discriminator = None
        if id is not None:
            self.id = id
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
        self.type = type
        self.workflow_id = workflow_id
        self.schedule = schedule
        if parameters is not None:
            self.parameters = parameters
        self.organization_id = organization_id
        if job_key is not None:
            self.job_key = job_key
        if last_run_at is not None:
            self.last_run_at = last_run_at
        if next_run_at is not None:
            self.next_run_at = next_run_at
        self.is_paused = is_paused
        if organization is not None:
            self.organization = organization
        if workflow is not None:
            self.workflow = workflow

    @property
    def id(self):
        """Gets the id of this Scheduler.  # noqa: E501


        :return: The id of this Scheduler.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Scheduler.


        :param id: The id of this Scheduler.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_updated_by(self):
        """Gets the last_updated_by of this Scheduler.  # noqa: E501


        :return: The last_updated_by of this Scheduler.  # noqa: E501
        :rtype: str
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, last_updated_by):
        """Sets the last_updated_by of this Scheduler.


        :param last_updated_by: The last_updated_by of this Scheduler.  # noqa: E501
        :type: str
        """

        self._last_updated_by = last_updated_by

    @property
    def created_by(self):
        """Gets the created_by of this Scheduler.  # noqa: E501


        :return: The created_by of this Scheduler.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Scheduler.


        :param created_by: The created_by of this Scheduler.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this Scheduler.  # noqa: E501


        :return: The created_at of this Scheduler.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Scheduler.


        :param created_at: The created_at of this Scheduler.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Scheduler.  # noqa: E501


        :return: The updated_at of this Scheduler.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Scheduler.


        :param updated_at: The updated_at of this Scheduler.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def archived_at(self):
        """Gets the archived_at of this Scheduler.  # noqa: E501


        :return: The archived_at of this Scheduler.  # noqa: E501
        :rtype: datetime
        """
        return self._archived_at

    @archived_at.setter
    def archived_at(self, archived_at):
        """Sets the archived_at of this Scheduler.


        :param archived_at: The archived_at of this Scheduler.  # noqa: E501
        :type: datetime
        """

        self._archived_at = archived_at

    @property
    def version(self):
        """Gets the version of this Scheduler.  # noqa: E501


        :return: The version of this Scheduler.  # noqa: E501
        :rtype: float
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Scheduler.


        :param version: The version of this Scheduler.  # noqa: E501
        :type: float
        """

        self._version = version

    @property
    def type(self):
        """Gets the type of this Scheduler.  # noqa: E501


        :return: The type of this Scheduler.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Scheduler.


        :param type: The type of this Scheduler.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["Cron", "OneTime"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def workflow_id(self):
        """Gets the workflow_id of this Scheduler.  # noqa: E501


        :return: The workflow_id of this Scheduler.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this Scheduler.


        :param workflow_id: The workflow_id of this Scheduler.  # noqa: E501
        :type: str
        """
        if workflow_id is None:
            raise ValueError("Invalid value for `workflow_id`, must not be `None`")  # noqa: E501

        self._workflow_id = workflow_id

    @property
    def schedule(self):
        """Gets the schedule of this Scheduler.  # noqa: E501


        :return: The schedule of this Scheduler.  # noqa: E501
        :rtype: str
        """
        return self._schedule

    @schedule.setter
    def schedule(self, schedule):
        """Sets the schedule of this Scheduler.


        :param schedule: The schedule of this Scheduler.  # noqa: E501
        :type: str
        """
        if schedule is None:
            raise ValueError("Invalid value for `schedule`, must not be `None`")  # noqa: E501

        self._schedule = schedule

    @property
    def parameters(self):
        """Gets the parameters of this Scheduler.  # noqa: E501


        :return: The parameters of this Scheduler.  # noqa: E501
        :rtype: WorkflowTemplateParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Scheduler.


        :param parameters: The parameters of this Scheduler.  # noqa: E501
        :type: WorkflowTemplateParameters
        """

        self._parameters = parameters

    @property
    def organization_id(self):
        """Gets the organization_id of this Scheduler.  # noqa: E501


        :return: The organization_id of this Scheduler.  # noqa: E501
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this Scheduler.


        :param organization_id: The organization_id of this Scheduler.  # noqa: E501
        :type: str
        """
        if organization_id is None:
            raise ValueError("Invalid value for `organization_id`, must not be `None`")  # noqa: E501

        self._organization_id = organization_id

    @property
    def job_key(self):
        """Gets the job_key of this Scheduler.  # noqa: E501


        :return: The job_key of this Scheduler.  # noqa: E501
        :rtype: str
        """
        return self._job_key

    @job_key.setter
    def job_key(self, job_key):
        """Sets the job_key of this Scheduler.


        :param job_key: The job_key of this Scheduler.  # noqa: E501
        :type: str
        """

        self._job_key = job_key

    @property
    def last_run_at(self):
        """Gets the last_run_at of this Scheduler.  # noqa: E501


        :return: The last_run_at of this Scheduler.  # noqa: E501
        :rtype: datetime
        """
        return self._last_run_at

    @last_run_at.setter
    def last_run_at(self, last_run_at):
        """Sets the last_run_at of this Scheduler.


        :param last_run_at: The last_run_at of this Scheduler.  # noqa: E501
        :type: datetime
        """

        self._last_run_at = last_run_at

    @property
    def next_run_at(self):
        """Gets the next_run_at of this Scheduler.  # noqa: E501


        :return: The next_run_at of this Scheduler.  # noqa: E501
        :rtype: datetime
        """
        return self._next_run_at

    @next_run_at.setter
    def next_run_at(self, next_run_at):
        """Sets the next_run_at of this Scheduler.


        :param next_run_at: The next_run_at of this Scheduler.  # noqa: E501
        :type: datetime
        """

        self._next_run_at = next_run_at

    @property
    def is_paused(self):
        """Gets the is_paused of this Scheduler.  # noqa: E501


        :return: The is_paused of this Scheduler.  # noqa: E501
        :rtype: object
        """
        return self._is_paused

    @is_paused.setter
    def is_paused(self, is_paused):
        """Sets the is_paused of this Scheduler.


        :param is_paused: The is_paused of this Scheduler.  # noqa: E501
        :type: object
        """
        if is_paused is None:
            raise ValueError("Invalid value for `is_paused`, must not be `None`")  # noqa: E501

        self._is_paused = is_paused

    @property
    def organization(self):
        """Gets the organization of this Scheduler.  # noqa: E501


        :return: The organization of this Scheduler.  # noqa: E501
        :rtype: Organization
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this Scheduler.


        :param organization: The organization of this Scheduler.  # noqa: E501
        :type: Organization
        """

        self._organization = organization

    @property
    def workflow(self):
        """Gets the workflow of this Scheduler.  # noqa: E501


        :return: The workflow of this Scheduler.  # noqa: E501
        :rtype: Workflow
        """
        return self._workflow

    @workflow.setter
    def workflow(self, workflow):
        """Sets the workflow of this Scheduler.


        :param workflow: The workflow of this Scheduler.  # noqa: E501
        :type: Workflow
        """

        self._workflow = workflow

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
        if issubclass(Scheduler, dict):
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
        if not isinstance(other, Scheduler):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
