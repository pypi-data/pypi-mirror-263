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

class ModelJoinedModelOutputDetailsResponseDto(object):
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
        'model_id': 'str',
        'latest_train_job_updated_at': 'datetime',
        'model_job_output_id': 'str',
        'model_job_id': 'str',
        'att_value': 'str',
        'att_direction': 'str',
        'att_se': 'str',
        'ate_value': 'str',
        'ate_direction': 'str',
        'ate_se': 'str',
        'top_impact_quartile_ate_value': 'str',
        'top_impact_quartile_ate_direction': 'str',
        'top_impact_quartile_se': 'str',
        'treated_records': 'float',
        'total_records': 'float',
        'n_features': 'float',
        'average_outcome_all': 'str',
        'average_outcome_treated': 'str',
        'average_outcome_untreated': 'str',
        'spearman_stability': 'str',
        'target_method': 'str',
        'r2': 'str',
        'auc': 'str',
        'n_records': 'float',
        'risk_average_outcome': 'str'
    }

    attribute_map = {
        'model_id': 'modelId',
        'latest_train_job_updated_at': 'latestTrainJobUpdatedAt',
        'model_job_output_id': 'modelJobOutputId',
        'model_job_id': 'modelJobId',
        'att_value': 'attValue',
        'att_direction': 'attDirection',
        'att_se': 'attSe',
        'ate_value': 'ateValue',
        'ate_direction': 'ateDirection',
        'ate_se': 'ateSe',
        'top_impact_quartile_ate_value': 'topImpactQuartileAteValue',
        'top_impact_quartile_ate_direction': 'topImpactQuartileAteDirection',
        'top_impact_quartile_se': 'topImpactQuartileSe',
        'treated_records': 'treatedRecords',
        'total_records': 'totalRecords',
        'n_features': 'nFeatures',
        'average_outcome_all': 'averageOutcomeAll',
        'average_outcome_treated': 'averageOutcomeTreated',
        'average_outcome_untreated': 'averageOutcomeUntreated',
        'spearman_stability': 'spearmanStability',
        'target_method': 'targetMethod',
        'r2': 'r2',
        'auc': 'auc',
        'n_records': 'n_records',
        'risk_average_outcome': 'riskAverageOutcome'
    }

    def __init__(self, model_id=None, latest_train_job_updated_at=None, model_job_output_id=None, model_job_id=None, att_value=None, att_direction=None, att_se=None, ate_value=None, ate_direction=None, ate_se=None, top_impact_quartile_ate_value=None, top_impact_quartile_ate_direction=None, top_impact_quartile_se=None, treated_records=None, total_records=None, n_features=None, average_outcome_all=None, average_outcome_treated=None, average_outcome_untreated=None, spearman_stability=None, target_method=None, r2=None, auc=None, n_records=None, risk_average_outcome=None):  # noqa: E501
        """ModelJoinedModelOutputDetailsResponseDto - a model defined in Swagger"""  # noqa: E501
        self._model_id = None
        self._latest_train_job_updated_at = None
        self._model_job_output_id = None
        self._model_job_id = None
        self._att_value = None
        self._att_direction = None
        self._att_se = None
        self._ate_value = None
        self._ate_direction = None
        self._ate_se = None
        self._top_impact_quartile_ate_value = None
        self._top_impact_quartile_ate_direction = None
        self._top_impact_quartile_se = None
        self._treated_records = None
        self._total_records = None
        self._n_features = None
        self._average_outcome_all = None
        self._average_outcome_treated = None
        self._average_outcome_untreated = None
        self._spearman_stability = None
        self._target_method = None
        self._r2 = None
        self._auc = None
        self._n_records = None
        self._risk_average_outcome = None
        self.discriminator = None
        self.model_id = model_id
        self.latest_train_job_updated_at = latest_train_job_updated_at
        self.model_job_output_id = model_job_output_id
        self.model_job_id = model_job_id
        self.att_value = att_value
        self.att_direction = att_direction
        self.att_se = att_se
        self.ate_value = ate_value
        self.ate_direction = ate_direction
        self.ate_se = ate_se
        self.top_impact_quartile_ate_value = top_impact_quartile_ate_value
        self.top_impact_quartile_ate_direction = top_impact_quartile_ate_direction
        self.top_impact_quartile_se = top_impact_quartile_se
        self.treated_records = treated_records
        self.total_records = total_records
        self.n_features = n_features
        self.average_outcome_all = average_outcome_all
        self.average_outcome_treated = average_outcome_treated
        self.average_outcome_untreated = average_outcome_untreated
        self.spearman_stability = spearman_stability
        self.target_method = target_method
        self.r2 = r2
        self.auc = auc
        self.n_records = n_records
        self.risk_average_outcome = risk_average_outcome

    @property
    def model_id(self):
        """Gets the model_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The model_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        """Sets the model_id of this ModelJoinedModelOutputDetailsResponseDto.


        :param model_id: The model_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if model_id is None:
            raise ValueError("Invalid value for `model_id`, must not be `None`")  # noqa: E501

        self._model_id = model_id

    @property
    def latest_train_job_updated_at(self):
        """Gets the latest_train_job_updated_at of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The latest_train_job_updated_at of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: datetime
        """
        return self._latest_train_job_updated_at

    @latest_train_job_updated_at.setter
    def latest_train_job_updated_at(self, latest_train_job_updated_at):
        """Sets the latest_train_job_updated_at of this ModelJoinedModelOutputDetailsResponseDto.


        :param latest_train_job_updated_at: The latest_train_job_updated_at of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: datetime
        """
        if latest_train_job_updated_at is None:
            raise ValueError("Invalid value for `latest_train_job_updated_at`, must not be `None`")  # noqa: E501

        self._latest_train_job_updated_at = latest_train_job_updated_at

    @property
    def model_job_output_id(self):
        """Gets the model_job_output_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The model_job_output_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._model_job_output_id

    @model_job_output_id.setter
    def model_job_output_id(self, model_job_output_id):
        """Sets the model_job_output_id of this ModelJoinedModelOutputDetailsResponseDto.


        :param model_job_output_id: The model_job_output_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if model_job_output_id is None:
            raise ValueError("Invalid value for `model_job_output_id`, must not be `None`")  # noqa: E501

        self._model_job_output_id = model_job_output_id

    @property
    def model_job_id(self):
        """Gets the model_job_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The model_job_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._model_job_id

    @model_job_id.setter
    def model_job_id(self, model_job_id):
        """Sets the model_job_id of this ModelJoinedModelOutputDetailsResponseDto.


        :param model_job_id: The model_job_id of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if model_job_id is None:
            raise ValueError("Invalid value for `model_job_id`, must not be `None`")  # noqa: E501

        self._model_job_id = model_job_id

    @property
    def att_value(self):
        """Gets the att_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The att_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._att_value

    @att_value.setter
    def att_value(self, att_value):
        """Sets the att_value of this ModelJoinedModelOutputDetailsResponseDto.


        :param att_value: The att_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if att_value is None:
            raise ValueError("Invalid value for `att_value`, must not be `None`")  # noqa: E501

        self._att_value = att_value

    @property
    def att_direction(self):
        """Gets the att_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The att_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._att_direction

    @att_direction.setter
    def att_direction(self, att_direction):
        """Sets the att_direction of this ModelJoinedModelOutputDetailsResponseDto.


        :param att_direction: The att_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if att_direction is None:
            raise ValueError("Invalid value for `att_direction`, must not be `None`")  # noqa: E501

        self._att_direction = att_direction

    @property
    def att_se(self):
        """Gets the att_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The att_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._att_se

    @att_se.setter
    def att_se(self, att_se):
        """Sets the att_se of this ModelJoinedModelOutputDetailsResponseDto.


        :param att_se: The att_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if att_se is None:
            raise ValueError("Invalid value for `att_se`, must not be `None`")  # noqa: E501

        self._att_se = att_se

    @property
    def ate_value(self):
        """Gets the ate_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The ate_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._ate_value

    @ate_value.setter
    def ate_value(self, ate_value):
        """Sets the ate_value of this ModelJoinedModelOutputDetailsResponseDto.


        :param ate_value: The ate_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if ate_value is None:
            raise ValueError("Invalid value for `ate_value`, must not be `None`")  # noqa: E501

        self._ate_value = ate_value

    @property
    def ate_direction(self):
        """Gets the ate_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The ate_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._ate_direction

    @ate_direction.setter
    def ate_direction(self, ate_direction):
        """Sets the ate_direction of this ModelJoinedModelOutputDetailsResponseDto.


        :param ate_direction: The ate_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if ate_direction is None:
            raise ValueError("Invalid value for `ate_direction`, must not be `None`")  # noqa: E501

        self._ate_direction = ate_direction

    @property
    def ate_se(self):
        """Gets the ate_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The ate_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._ate_se

    @ate_se.setter
    def ate_se(self, ate_se):
        """Sets the ate_se of this ModelJoinedModelOutputDetailsResponseDto.


        :param ate_se: The ate_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if ate_se is None:
            raise ValueError("Invalid value for `ate_se`, must not be `None`")  # noqa: E501

        self._ate_se = ate_se

    @property
    def top_impact_quartile_ate_value(self):
        """Gets the top_impact_quartile_ate_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The top_impact_quartile_ate_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._top_impact_quartile_ate_value

    @top_impact_quartile_ate_value.setter
    def top_impact_quartile_ate_value(self, top_impact_quartile_ate_value):
        """Sets the top_impact_quartile_ate_value of this ModelJoinedModelOutputDetailsResponseDto.


        :param top_impact_quartile_ate_value: The top_impact_quartile_ate_value of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if top_impact_quartile_ate_value is None:
            raise ValueError("Invalid value for `top_impact_quartile_ate_value`, must not be `None`")  # noqa: E501

        self._top_impact_quartile_ate_value = top_impact_quartile_ate_value

    @property
    def top_impact_quartile_ate_direction(self):
        """Gets the top_impact_quartile_ate_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The top_impact_quartile_ate_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._top_impact_quartile_ate_direction

    @top_impact_quartile_ate_direction.setter
    def top_impact_quartile_ate_direction(self, top_impact_quartile_ate_direction):
        """Sets the top_impact_quartile_ate_direction of this ModelJoinedModelOutputDetailsResponseDto.


        :param top_impact_quartile_ate_direction: The top_impact_quartile_ate_direction of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if top_impact_quartile_ate_direction is None:
            raise ValueError("Invalid value for `top_impact_quartile_ate_direction`, must not be `None`")  # noqa: E501

        self._top_impact_quartile_ate_direction = top_impact_quartile_ate_direction

    @property
    def top_impact_quartile_se(self):
        """Gets the top_impact_quartile_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The top_impact_quartile_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._top_impact_quartile_se

    @top_impact_quartile_se.setter
    def top_impact_quartile_se(self, top_impact_quartile_se):
        """Sets the top_impact_quartile_se of this ModelJoinedModelOutputDetailsResponseDto.


        :param top_impact_quartile_se: The top_impact_quartile_se of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if top_impact_quartile_se is None:
            raise ValueError("Invalid value for `top_impact_quartile_se`, must not be `None`")  # noqa: E501

        self._top_impact_quartile_se = top_impact_quartile_se

    @property
    def treated_records(self):
        """Gets the treated_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The treated_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._treated_records

    @treated_records.setter
    def treated_records(self, treated_records):
        """Sets the treated_records of this ModelJoinedModelOutputDetailsResponseDto.


        :param treated_records: The treated_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: float
        """
        if treated_records is None:
            raise ValueError("Invalid value for `treated_records`, must not be `None`")  # noqa: E501

        self._treated_records = treated_records

    @property
    def total_records(self):
        """Gets the total_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The total_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._total_records

    @total_records.setter
    def total_records(self, total_records):
        """Sets the total_records of this ModelJoinedModelOutputDetailsResponseDto.


        :param total_records: The total_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: float
        """
        if total_records is None:
            raise ValueError("Invalid value for `total_records`, must not be `None`")  # noqa: E501

        self._total_records = total_records

    @property
    def n_features(self):
        """Gets the n_features of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The n_features of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._n_features

    @n_features.setter
    def n_features(self, n_features):
        """Sets the n_features of this ModelJoinedModelOutputDetailsResponseDto.


        :param n_features: The n_features of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: float
        """
        if n_features is None:
            raise ValueError("Invalid value for `n_features`, must not be `None`")  # noqa: E501

        self._n_features = n_features

    @property
    def average_outcome_all(self):
        """Gets the average_outcome_all of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The average_outcome_all of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._average_outcome_all

    @average_outcome_all.setter
    def average_outcome_all(self, average_outcome_all):
        """Sets the average_outcome_all of this ModelJoinedModelOutputDetailsResponseDto.


        :param average_outcome_all: The average_outcome_all of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if average_outcome_all is None:
            raise ValueError("Invalid value for `average_outcome_all`, must not be `None`")  # noqa: E501

        self._average_outcome_all = average_outcome_all

    @property
    def average_outcome_treated(self):
        """Gets the average_outcome_treated of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The average_outcome_treated of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._average_outcome_treated

    @average_outcome_treated.setter
    def average_outcome_treated(self, average_outcome_treated):
        """Sets the average_outcome_treated of this ModelJoinedModelOutputDetailsResponseDto.


        :param average_outcome_treated: The average_outcome_treated of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if average_outcome_treated is None:
            raise ValueError("Invalid value for `average_outcome_treated`, must not be `None`")  # noqa: E501

        self._average_outcome_treated = average_outcome_treated

    @property
    def average_outcome_untreated(self):
        """Gets the average_outcome_untreated of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The average_outcome_untreated of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._average_outcome_untreated

    @average_outcome_untreated.setter
    def average_outcome_untreated(self, average_outcome_untreated):
        """Sets the average_outcome_untreated of this ModelJoinedModelOutputDetailsResponseDto.


        :param average_outcome_untreated: The average_outcome_untreated of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if average_outcome_untreated is None:
            raise ValueError("Invalid value for `average_outcome_untreated`, must not be `None`")  # noqa: E501

        self._average_outcome_untreated = average_outcome_untreated

    @property
    def spearman_stability(self):
        """Gets the spearman_stability of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The spearman_stability of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._spearman_stability

    @spearman_stability.setter
    def spearman_stability(self, spearman_stability):
        """Sets the spearman_stability of this ModelJoinedModelOutputDetailsResponseDto.


        :param spearman_stability: The spearman_stability of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if spearman_stability is None:
            raise ValueError("Invalid value for `spearman_stability`, must not be `None`")  # noqa: E501

        self._spearman_stability = spearman_stability

    @property
    def target_method(self):
        """Gets the target_method of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The target_method of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._target_method

    @target_method.setter
    def target_method(self, target_method):
        """Sets the target_method of this ModelJoinedModelOutputDetailsResponseDto.


        :param target_method: The target_method of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if target_method is None:
            raise ValueError("Invalid value for `target_method`, must not be `None`")  # noqa: E501

        self._target_method = target_method

    @property
    def r2(self):
        """Gets the r2 of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The r2 of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._r2

    @r2.setter
    def r2(self, r2):
        """Sets the r2 of this ModelJoinedModelOutputDetailsResponseDto.


        :param r2: The r2 of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if r2 is None:
            raise ValueError("Invalid value for `r2`, must not be `None`")  # noqa: E501

        self._r2 = r2

    @property
    def auc(self):
        """Gets the auc of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The auc of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._auc

    @auc.setter
    def auc(self, auc):
        """Sets the auc of this ModelJoinedModelOutputDetailsResponseDto.


        :param auc: The auc of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if auc is None:
            raise ValueError("Invalid value for `auc`, must not be `None`")  # noqa: E501

        self._auc = auc

    @property
    def n_records(self):
        """Gets the n_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The n_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._n_records

    @n_records.setter
    def n_records(self, n_records):
        """Sets the n_records of this ModelJoinedModelOutputDetailsResponseDto.


        :param n_records: The n_records of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: float
        """
        if n_records is None:
            raise ValueError("Invalid value for `n_records`, must not be `None`")  # noqa: E501

        self._n_records = n_records

    @property
    def risk_average_outcome(self):
        """Gets the risk_average_outcome of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501


        :return: The risk_average_outcome of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._risk_average_outcome

    @risk_average_outcome.setter
    def risk_average_outcome(self, risk_average_outcome):
        """Sets the risk_average_outcome of this ModelJoinedModelOutputDetailsResponseDto.


        :param risk_average_outcome: The risk_average_outcome of this ModelJoinedModelOutputDetailsResponseDto.  # noqa: E501
        :type: str
        """
        if risk_average_outcome is None:
            raise ValueError("Invalid value for `risk_average_outcome`, must not be `None`")  # noqa: E501

        self._risk_average_outcome = risk_average_outcome

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
        if issubclass(ModelJoinedModelOutputDetailsResponseDto, dict):
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
        if not isinstance(other, ModelJoinedModelOutputDetailsResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
