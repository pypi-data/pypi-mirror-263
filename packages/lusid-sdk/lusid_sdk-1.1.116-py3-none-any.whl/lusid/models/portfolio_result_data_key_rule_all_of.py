# coding: utf-8

"""
    LUSID API

    FINBOURNE Technology  # noqa: E501

    The version of the OpenAPI document: 1.1.116
    Contact: info@finbourne.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from lusid.configuration import Configuration


class PortfolioResultDataKeyRuleAllOf(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
      required_map (dict): The key is attribute name
                           and the value is whether it is 'required' or 'optional'.
    """
    openapi_types = {
        'supplier': 'str',
        'data_scope': 'str',
        'document_code': 'str',
        'quote_interval': 'str',
        'as_at': 'datetime',
        'portfolio_code': 'str',
        'portfolio_scope': 'str',
        'result_key_rule_type': 'str'
    }

    attribute_map = {
        'supplier': 'supplier',
        'data_scope': 'dataScope',
        'document_code': 'documentCode',
        'quote_interval': 'quoteInterval',
        'as_at': 'asAt',
        'portfolio_code': 'portfolioCode',
        'portfolio_scope': 'portfolioScope',
        'result_key_rule_type': 'resultKeyRuleType'
    }

    required_map = {
        'supplier': 'required',
        'data_scope': 'required',
        'document_code': 'required',
        'quote_interval': 'optional',
        'as_at': 'optional',
        'portfolio_code': 'optional',
        'portfolio_scope': 'optional',
        'result_key_rule_type': 'required'
    }

    def __init__(self, supplier=None, data_scope=None, document_code=None, quote_interval=None, as_at=None, portfolio_code=None, portfolio_scope=None, result_key_rule_type=None, local_vars_configuration=None):  # noqa: E501
        """PortfolioResultDataKeyRuleAllOf - a model defined in OpenAPI"
        
        :param supplier:  the result resource supplier (where the data comes from) (required)
        :type supplier: str
        :param data_scope:  which is the scope in which the data should be found (required)
        :type data_scope: str
        :param document_code:  document code that defines which document is desired (required)
        :type document_code: str
        :param quote_interval:  Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago).
        :type quote_interval: str
        :param as_at:  The AsAt predicate specification.
        :type as_at: datetime
        :param portfolio_code: 
        :type portfolio_code: str
        :param portfolio_scope: 
        :type portfolio_scope: str
        :param result_key_rule_type:  The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule (required)
        :type result_key_rule_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._supplier = None
        self._data_scope = None
        self._document_code = None
        self._quote_interval = None
        self._as_at = None
        self._portfolio_code = None
        self._portfolio_scope = None
        self._result_key_rule_type = None
        self.discriminator = None

        self.supplier = supplier
        self.data_scope = data_scope
        self.document_code = document_code
        self.quote_interval = quote_interval
        self.as_at = as_at
        self.portfolio_code = portfolio_code
        self.portfolio_scope = portfolio_scope
        self.result_key_rule_type = result_key_rule_type

    @property
    def supplier(self):
        """Gets the supplier of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501

        the result resource supplier (where the data comes from)  # noqa: E501

        :return: The supplier of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._supplier

    @supplier.setter
    def supplier(self, supplier):
        """Sets the supplier of this PortfolioResultDataKeyRuleAllOf.

        the result resource supplier (where the data comes from)  # noqa: E501

        :param supplier: The supplier of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :type supplier: str
        """
        if self.local_vars_configuration.client_side_validation and supplier is None:  # noqa: E501
            raise ValueError("Invalid value for `supplier`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                supplier is not None and len(supplier) > 32):
            raise ValueError("Invalid value for `supplier`, length must be less than or equal to `32`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                supplier is not None and len(supplier) < 0):
            raise ValueError("Invalid value for `supplier`, length must be greater than or equal to `0`")  # noqa: E501

        self._supplier = supplier

    @property
    def data_scope(self):
        """Gets the data_scope of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501

        which is the scope in which the data should be found  # noqa: E501

        :return: The data_scope of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._data_scope

    @data_scope.setter
    def data_scope(self, data_scope):
        """Sets the data_scope of this PortfolioResultDataKeyRuleAllOf.

        which is the scope in which the data should be found  # noqa: E501

        :param data_scope: The data_scope of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :type data_scope: str
        """
        if self.local_vars_configuration.client_side_validation and data_scope is None:  # noqa: E501
            raise ValueError("Invalid value for `data_scope`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and len(data_scope) > 256):
            raise ValueError("Invalid value for `data_scope`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and len(data_scope) < 1):
            raise ValueError("Invalid value for `data_scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                data_scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', data_scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `data_scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._data_scope = data_scope

    @property
    def document_code(self):
        """Gets the document_code of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501

        document code that defines which document is desired  # noqa: E501

        :return: The document_code of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._document_code

    @document_code.setter
    def document_code(self, document_code):
        """Sets the document_code of this PortfolioResultDataKeyRuleAllOf.

        document code that defines which document is desired  # noqa: E501

        :param document_code: The document_code of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :type document_code: str
        """
        if self.local_vars_configuration.client_side_validation and document_code is None:  # noqa: E501
            raise ValueError("Invalid value for `document_code`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                document_code is not None and len(document_code) > 256):
            raise ValueError("Invalid value for `document_code`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                document_code is not None and len(document_code) < 1):
            raise ValueError("Invalid value for `document_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._document_code = document_code

    @property
    def quote_interval(self):
        """Gets the quote_interval of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501

        Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago).  # noqa: E501

        :return: The quote_interval of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._quote_interval

    @quote_interval.setter
    def quote_interval(self, quote_interval):
        """Sets the quote_interval of this PortfolioResultDataKeyRuleAllOf.

        Shorthand for the time interval used to select result data. This must be a dot-separated string              specifying a start and end date, for example '5D.0D' to look back 5 days from today (0 days ago).  # noqa: E501

        :param quote_interval: The quote_interval of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :type quote_interval: str
        """
        if (self.local_vars_configuration.client_side_validation and
                quote_interval is not None and len(quote_interval) > 16):
            raise ValueError("Invalid value for `quote_interval`, length must be less than or equal to `16`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                quote_interval is not None and len(quote_interval) < 0):
            raise ValueError("Invalid value for `quote_interval`, length must be greater than or equal to `0`")  # noqa: E501

        self._quote_interval = quote_interval

    @property
    def as_at(self):
        """Gets the as_at of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501

        The AsAt predicate specification.  # noqa: E501

        :return: The as_at of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._as_at

    @as_at.setter
    def as_at(self, as_at):
        """Sets the as_at of this PortfolioResultDataKeyRuleAllOf.

        The AsAt predicate specification.  # noqa: E501

        :param as_at: The as_at of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :type as_at: datetime
        """

        self._as_at = as_at

    @property
    def portfolio_code(self):
        """Gets the portfolio_code of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501


        :return: The portfolio_code of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_code

    @portfolio_code.setter
    def portfolio_code(self, portfolio_code):
        """Sets the portfolio_code of this PortfolioResultDataKeyRuleAllOf.


        :param portfolio_code: The portfolio_code of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :type portfolio_code: str
        """
        if (self.local_vars_configuration.client_side_validation and
                portfolio_code is not None and len(portfolio_code) > 256):
            raise ValueError("Invalid value for `portfolio_code`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                portfolio_code is not None and len(portfolio_code) < 1):
            raise ValueError("Invalid value for `portfolio_code`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                portfolio_code is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', portfolio_code)):  # noqa: E501
            raise ValueError(r"Invalid value for `portfolio_code`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._portfolio_code = portfolio_code

    @property
    def portfolio_scope(self):
        """Gets the portfolio_scope of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501


        :return: The portfolio_scope of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._portfolio_scope

    @portfolio_scope.setter
    def portfolio_scope(self, portfolio_scope):
        """Sets the portfolio_scope of this PortfolioResultDataKeyRuleAllOf.


        :param portfolio_scope: The portfolio_scope of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :type portfolio_scope: str
        """
        if (self.local_vars_configuration.client_side_validation and
                portfolio_scope is not None and len(portfolio_scope) > 256):
            raise ValueError("Invalid value for `portfolio_scope`, length must be less than or equal to `256`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                portfolio_scope is not None and len(portfolio_scope) < 1):
            raise ValueError("Invalid value for `portfolio_scope`, length must be greater than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                portfolio_scope is not None and not re.search(r'^[a-zA-Z0-9\-_]+$', portfolio_scope)):  # noqa: E501
            raise ValueError(r"Invalid value for `portfolio_scope`, must be a follow pattern or equal to `/^[a-zA-Z0-9\-_]+$/`")  # noqa: E501

        self._portfolio_scope = portfolio_scope

    @property
    def result_key_rule_type(self):
        """Gets the result_key_rule_type of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501

        The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule  # noqa: E501

        :return: The result_key_rule_type of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :rtype: str
        """
        return self._result_key_rule_type

    @result_key_rule_type.setter
    def result_key_rule_type(self, result_key_rule_type):
        """Sets the result_key_rule_type of this PortfolioResultDataKeyRuleAllOf.

        The available values are: Invalid, ResultDataKeyRule, PortfolioResultDataKeyRule  # noqa: E501

        :param result_key_rule_type: The result_key_rule_type of this PortfolioResultDataKeyRuleAllOf.  # noqa: E501
        :type result_key_rule_type: str
        """
        if self.local_vars_configuration.client_side_validation and result_key_rule_type is None:  # noqa: E501
            raise ValueError("Invalid value for `result_key_rule_type`, must not be `None`")  # noqa: E501
        allowed_values = ["Invalid", "ResultDataKeyRule", "PortfolioResultDataKeyRule"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and result_key_rule_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `result_key_rule_type` ({0}), must be one of {1}"  # noqa: E501
                .format(result_key_rule_type, allowed_values)
            )

        self._result_key_rule_type = result_key_rule_type

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PortfolioResultDataKeyRuleAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PortfolioResultDataKeyRuleAllOf):
            return True

        return self.to_dict() != other.to_dict()
