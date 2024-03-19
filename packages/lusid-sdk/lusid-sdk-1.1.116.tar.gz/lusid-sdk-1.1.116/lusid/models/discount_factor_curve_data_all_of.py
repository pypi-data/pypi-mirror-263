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


class DiscountFactorCurveDataAllOf(object):
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
        'base_date': 'datetime',
        'dates': 'list[datetime]',
        'discount_factors': 'list[float]',
        'lineage': 'str',
        'market_data_options': 'MarketDataOptions',
        'market_data_type': 'str'
    }

    attribute_map = {
        'base_date': 'baseDate',
        'dates': 'dates',
        'discount_factors': 'discountFactors',
        'lineage': 'lineage',
        'market_data_options': 'marketDataOptions',
        'market_data_type': 'marketDataType'
    }

    required_map = {
        'base_date': 'required',
        'dates': 'required',
        'discount_factors': 'required',
        'lineage': 'optional',
        'market_data_options': 'optional',
        'market_data_type': 'required'
    }

    def __init__(self, base_date=None, dates=None, discount_factors=None, lineage=None, market_data_options=None, market_data_type=None, local_vars_configuration=None):  # noqa: E501
        """DiscountFactorCurveDataAllOf - a model defined in OpenAPI"
        
        :param base_date:  BaseDate for the Curve (required)
        :type base_date: datetime
        :param dates:  Dates for which the discount factors apply (required)
        :type dates: list[datetime]
        :param discount_factors:  Discount factors to be applied to cashflow on the specified dates (required)
        :type discount_factors: list[float]
        :param lineage:  Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.
        :type lineage: str
        :param market_data_options: 
        :type market_data_options: lusid.MarketDataOptions
        :param market_data_type:  The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface (required)
        :type market_data_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._base_date = None
        self._dates = None
        self._discount_factors = None
        self._lineage = None
        self._market_data_options = None
        self._market_data_type = None
        self.discriminator = None

        self.base_date = base_date
        self.dates = dates
        self.discount_factors = discount_factors
        self.lineage = lineage
        if market_data_options is not None:
            self.market_data_options = market_data_options
        self.market_data_type = market_data_type

    @property
    def base_date(self):
        """Gets the base_date of this DiscountFactorCurveDataAllOf.  # noqa: E501

        BaseDate for the Curve  # noqa: E501

        :return: The base_date of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :rtype: datetime
        """
        return self._base_date

    @base_date.setter
    def base_date(self, base_date):
        """Sets the base_date of this DiscountFactorCurveDataAllOf.

        BaseDate for the Curve  # noqa: E501

        :param base_date: The base_date of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :type base_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and base_date is None:  # noqa: E501
            raise ValueError("Invalid value for `base_date`, must not be `None`")  # noqa: E501

        self._base_date = base_date

    @property
    def dates(self):
        """Gets the dates of this DiscountFactorCurveDataAllOf.  # noqa: E501

        Dates for which the discount factors apply  # noqa: E501

        :return: The dates of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :rtype: list[datetime]
        """
        return self._dates

    @dates.setter
    def dates(self, dates):
        """Sets the dates of this DiscountFactorCurveDataAllOf.

        Dates for which the discount factors apply  # noqa: E501

        :param dates: The dates of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :type dates: list[datetime]
        """
        if self.local_vars_configuration.client_side_validation and dates is None:  # noqa: E501
            raise ValueError("Invalid value for `dates`, must not be `None`")  # noqa: E501

        self._dates = dates

    @property
    def discount_factors(self):
        """Gets the discount_factors of this DiscountFactorCurveDataAllOf.  # noqa: E501

        Discount factors to be applied to cashflow on the specified dates  # noqa: E501

        :return: The discount_factors of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :rtype: list[float]
        """
        return self._discount_factors

    @discount_factors.setter
    def discount_factors(self, discount_factors):
        """Sets the discount_factors of this DiscountFactorCurveDataAllOf.

        Discount factors to be applied to cashflow on the specified dates  # noqa: E501

        :param discount_factors: The discount_factors of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :type discount_factors: list[float]
        """
        if self.local_vars_configuration.client_side_validation and discount_factors is None:  # noqa: E501
            raise ValueError("Invalid value for `discount_factors`, must not be `None`")  # noqa: E501

        self._discount_factors = discount_factors

    @property
    def lineage(self):
        """Gets the lineage of this DiscountFactorCurveDataAllOf.  # noqa: E501

        Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :return: The lineage of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._lineage

    @lineage.setter
    def lineage(self, lineage):
        """Sets the lineage of this DiscountFactorCurveDataAllOf.

        Description of the complex market data's lineage e.g. 'FundAccountant_GreenQuality'.  # noqa: E501

        :param lineage: The lineage of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :type lineage: str
        """
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) > 1024):
            raise ValueError("Invalid value for `lineage`, length must be less than or equal to `1024`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                lineage is not None and len(lineage) < 0):
            raise ValueError("Invalid value for `lineage`, length must be greater than or equal to `0`")  # noqa: E501

        self._lineage = lineage

    @property
    def market_data_options(self):
        """Gets the market_data_options of this DiscountFactorCurveDataAllOf.  # noqa: E501


        :return: The market_data_options of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :rtype: lusid.MarketDataOptions
        """
        return self._market_data_options

    @market_data_options.setter
    def market_data_options(self, market_data_options):
        """Sets the market_data_options of this DiscountFactorCurveDataAllOf.


        :param market_data_options: The market_data_options of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :type market_data_options: lusid.MarketDataOptions
        """

        self._market_data_options = market_data_options

    @property
    def market_data_type(self):
        """Gets the market_data_type of this DiscountFactorCurveDataAllOf.  # noqa: E501

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface  # noqa: E501

        :return: The market_data_type of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :rtype: str
        """
        return self._market_data_type

    @market_data_type.setter
    def market_data_type(self, market_data_type):
        """Sets the market_data_type of this DiscountFactorCurveDataAllOf.

        The available values are: DiscountFactorCurveData, EquityVolSurfaceData, FxVolSurfaceData, IrVolCubeData, OpaqueMarketData, YieldCurveData, FxForwardCurveData, FxForwardPipsCurveData, FxForwardTenorCurveData, FxForwardTenorPipsCurveData, FxForwardCurveByQuoteReference, CreditSpreadCurveData, EquityCurveByPricesData, ConstantVolatilitySurface  # noqa: E501

        :param market_data_type: The market_data_type of this DiscountFactorCurveDataAllOf.  # noqa: E501
        :type market_data_type: str
        """
        if self.local_vars_configuration.client_side_validation and market_data_type is None:  # noqa: E501
            raise ValueError("Invalid value for `market_data_type`, must not be `None`")  # noqa: E501
        allowed_values = ["DiscountFactorCurveData", "EquityVolSurfaceData", "FxVolSurfaceData", "IrVolCubeData", "OpaqueMarketData", "YieldCurveData", "FxForwardCurveData", "FxForwardPipsCurveData", "FxForwardTenorCurveData", "FxForwardTenorPipsCurveData", "FxForwardCurveByQuoteReference", "CreditSpreadCurveData", "EquityCurveByPricesData", "ConstantVolatilitySurface"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and market_data_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `market_data_type` ({0}), must be one of {1}"  # noqa: E501
                .format(market_data_type, allowed_values)
            )

        self._market_data_type = market_data_type

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
        if not isinstance(other, DiscountFactorCurveDataAllOf):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DiscountFactorCurveDataAllOf):
            return True

        return self.to_dict() != other.to_dict()
