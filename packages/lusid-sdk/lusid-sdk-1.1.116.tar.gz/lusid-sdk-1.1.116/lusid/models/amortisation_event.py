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


class AmortisationEvent(object):
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
        'amount_reduced': 'float',
        'dom_ccy': 'str',
        'pay_receive': 'str',
        'payment_date': 'datetime',
        'instrument_event_type': 'str'
    }

    attribute_map = {
        'amount_reduced': 'amountReduced',
        'dom_ccy': 'domCcy',
        'pay_receive': 'payReceive',
        'payment_date': 'paymentDate',
        'instrument_event_type': 'instrumentEventType'
    }

    required_map = {
        'amount_reduced': 'required',
        'dom_ccy': 'required',
        'pay_receive': 'required',
        'payment_date': 'required',
        'instrument_event_type': 'required'
    }

    def __init__(self, amount_reduced=None, dom_ccy=None, pay_receive=None, payment_date=None, instrument_event_type=None, local_vars_configuration=None):  # noqa: E501
        """AmortisationEvent - a model defined in OpenAPI"
        
        :param amount_reduced:  The amount reduced in this amortisation event.  That is, the difference between the previous notional amount and the current notional amount as set in this event. (required)
        :type amount_reduced: float
        :param dom_ccy:  Domestic currency of the originating instrument (required)
        :type dom_ccy: str
        :param pay_receive:  Is this event in relation to the Pay or Receive leg (required)
        :type pay_receive: str
        :param payment_date:  The date the principal payment is to be made. (required)
        :type payment_date: datetime
        :param instrument_event_type:  The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent (required)
        :type instrument_event_type: str

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._amount_reduced = None
        self._dom_ccy = None
        self._pay_receive = None
        self._payment_date = None
        self._instrument_event_type = None
        self.discriminator = None

        self.amount_reduced = amount_reduced
        self.dom_ccy = dom_ccy
        self.pay_receive = pay_receive
        self.payment_date = payment_date
        self.instrument_event_type = instrument_event_type

    @property
    def amount_reduced(self):
        """Gets the amount_reduced of this AmortisationEvent.  # noqa: E501

        The amount reduced in this amortisation event.  That is, the difference between the previous notional amount and the current notional amount as set in this event.  # noqa: E501

        :return: The amount_reduced of this AmortisationEvent.  # noqa: E501
        :rtype: float
        """
        return self._amount_reduced

    @amount_reduced.setter
    def amount_reduced(self, amount_reduced):
        """Sets the amount_reduced of this AmortisationEvent.

        The amount reduced in this amortisation event.  That is, the difference between the previous notional amount and the current notional amount as set in this event.  # noqa: E501

        :param amount_reduced: The amount_reduced of this AmortisationEvent.  # noqa: E501
        :type amount_reduced: float
        """
        if self.local_vars_configuration.client_side_validation and amount_reduced is None:  # noqa: E501
            raise ValueError("Invalid value for `amount_reduced`, must not be `None`")  # noqa: E501

        self._amount_reduced = amount_reduced

    @property
    def dom_ccy(self):
        """Gets the dom_ccy of this AmortisationEvent.  # noqa: E501

        Domestic currency of the originating instrument  # noqa: E501

        :return: The dom_ccy of this AmortisationEvent.  # noqa: E501
        :rtype: str
        """
        return self._dom_ccy

    @dom_ccy.setter
    def dom_ccy(self, dom_ccy):
        """Sets the dom_ccy of this AmortisationEvent.

        Domestic currency of the originating instrument  # noqa: E501

        :param dom_ccy: The dom_ccy of this AmortisationEvent.  # noqa: E501
        :type dom_ccy: str
        """
        if self.local_vars_configuration.client_side_validation and dom_ccy is None:  # noqa: E501
            raise ValueError("Invalid value for `dom_ccy`, must not be `None`")  # noqa: E501

        self._dom_ccy = dom_ccy

    @property
    def pay_receive(self):
        """Gets the pay_receive of this AmortisationEvent.  # noqa: E501

        Is this event in relation to the Pay or Receive leg  # noqa: E501

        :return: The pay_receive of this AmortisationEvent.  # noqa: E501
        :rtype: str
        """
        return self._pay_receive

    @pay_receive.setter
    def pay_receive(self, pay_receive):
        """Sets the pay_receive of this AmortisationEvent.

        Is this event in relation to the Pay or Receive leg  # noqa: E501

        :param pay_receive: The pay_receive of this AmortisationEvent.  # noqa: E501
        :type pay_receive: str
        """
        if self.local_vars_configuration.client_side_validation and pay_receive is None:  # noqa: E501
            raise ValueError("Invalid value for `pay_receive`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                pay_receive is not None and len(pay_receive) < 1):
            raise ValueError("Invalid value for `pay_receive`, length must be greater than or equal to `1`")  # noqa: E501

        self._pay_receive = pay_receive

    @property
    def payment_date(self):
        """Gets the payment_date of this AmortisationEvent.  # noqa: E501

        The date the principal payment is to be made.  # noqa: E501

        :return: The payment_date of this AmortisationEvent.  # noqa: E501
        :rtype: datetime
        """
        return self._payment_date

    @payment_date.setter
    def payment_date(self, payment_date):
        """Sets the payment_date of this AmortisationEvent.

        The date the principal payment is to be made.  # noqa: E501

        :param payment_date: The payment_date of this AmortisationEvent.  # noqa: E501
        :type payment_date: datetime
        """
        if self.local_vars_configuration.client_side_validation and payment_date is None:  # noqa: E501
            raise ValueError("Invalid value for `payment_date`, must not be `None`")  # noqa: E501

        self._payment_date = payment_date

    @property
    def instrument_event_type(self):
        """Gets the instrument_event_type of this AmortisationEvent.  # noqa: E501

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent  # noqa: E501

        :return: The instrument_event_type of this AmortisationEvent.  # noqa: E501
        :rtype: str
        """
        return self._instrument_event_type

    @instrument_event_type.setter
    def instrument_event_type(self, instrument_event_type):
        """Sets the instrument_event_type of this AmortisationEvent.

        The Type of Event. The available values are: TransitionEvent, InformationalEvent, OpenEvent, CloseEvent, StockSplitEvent, BondDefaultEvent, CashDividendEvent, AmortisationEvent, CashFlowEvent, ExerciseEvent, ResetEvent, TriggerEvent, RawVendorEvent, InformationalErrorEvent, BondCouponEvent, DividendReinvestmentEvent, AccumulationEvent, BondPrincipalEvent, DividendOptionEvent, MaturityEvent, FxForwardSettlementEvent  # noqa: E501

        :param instrument_event_type: The instrument_event_type of this AmortisationEvent.  # noqa: E501
        :type instrument_event_type: str
        """
        if self.local_vars_configuration.client_side_validation and instrument_event_type is None:  # noqa: E501
            raise ValueError("Invalid value for `instrument_event_type`, must not be `None`")  # noqa: E501
        allowed_values = ["TransitionEvent", "InformationalEvent", "OpenEvent", "CloseEvent", "StockSplitEvent", "BondDefaultEvent", "CashDividendEvent", "AmortisationEvent", "CashFlowEvent", "ExerciseEvent", "ResetEvent", "TriggerEvent", "RawVendorEvent", "InformationalErrorEvent", "BondCouponEvent", "DividendReinvestmentEvent", "AccumulationEvent", "BondPrincipalEvent", "DividendOptionEvent", "MaturityEvent", "FxForwardSettlementEvent"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and instrument_event_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `instrument_event_type` ({0}), must be one of {1}"  # noqa: E501
                .format(instrument_event_type, allowed_values)
            )

        self._instrument_event_type = instrument_event_type

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
        if not isinstance(other, AmortisationEvent):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AmortisationEvent):
            return True

        return self.to_dict() != other.to_dict()
