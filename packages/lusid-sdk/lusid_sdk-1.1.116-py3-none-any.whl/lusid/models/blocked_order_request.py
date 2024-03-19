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


class BlockedOrderRequest(object):
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
        'properties': 'dict(str, PerpetualProperty)',
        'quantity': 'float',
        'order_book_id': 'ResourceId',
        'portfolio_id': 'ResourceId',
        'id': 'ResourceId',
        'state': 'str',
        'date': 'datetime',
        'price': 'CurrencyAndAmount',
        'order_instruction': 'ResourceId',
        'package': 'ResourceId'
    }

    attribute_map = {
        'properties': 'properties',
        'quantity': 'quantity',
        'order_book_id': 'orderBookId',
        'portfolio_id': 'portfolioId',
        'id': 'id',
        'state': 'state',
        'date': 'date',
        'price': 'price',
        'order_instruction': 'orderInstruction',
        'package': 'package'
    }

    required_map = {
        'properties': 'optional',
        'quantity': 'required',
        'order_book_id': 'optional',
        'portfolio_id': 'optional',
        'id': 'required',
        'state': 'optional',
        'date': 'optional',
        'price': 'optional',
        'order_instruction': 'optional',
        'package': 'optional'
    }

    def __init__(self, properties=None, quantity=None, order_book_id=None, portfolio_id=None, id=None, state=None, date=None, price=None, order_instruction=None, package=None, local_vars_configuration=None):  # noqa: E501
        """BlockedOrderRequest - a model defined in OpenAPI"
        
        :param properties:  Client-defined properties associated with this order.
        :type properties: dict[str, lusid.PerpetualProperty]
        :param quantity:  The quantity of given instrument ordered. (required)
        :type quantity: float
        :param order_book_id: 
        :type order_book_id: lusid.ResourceId
        :param portfolio_id: 
        :type portfolio_id: lusid.ResourceId
        :param id:  (required)
        :type id: lusid.ResourceId
        :param state:  The order's state (examples: New, PartiallyFilled, ...)
        :type state: str
        :param date:  The date on which the order was made
        :type date: datetime
        :param price: 
        :type price: lusid.CurrencyAndAmount
        :param order_instruction: 
        :type order_instruction: lusid.ResourceId
        :param package: 
        :type package: lusid.ResourceId

        """  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._properties = None
        self._quantity = None
        self._order_book_id = None
        self._portfolio_id = None
        self._id = None
        self._state = None
        self._date = None
        self._price = None
        self._order_instruction = None
        self._package = None
        self.discriminator = None

        self.properties = properties
        self.quantity = quantity
        if order_book_id is not None:
            self.order_book_id = order_book_id
        if portfolio_id is not None:
            self.portfolio_id = portfolio_id
        self.id = id
        self.state = state
        if date is not None:
            self.date = date
        if price is not None:
            self.price = price
        if order_instruction is not None:
            self.order_instruction = order_instruction
        if package is not None:
            self.package = package

    @property
    def properties(self):
        """Gets the properties of this BlockedOrderRequest.  # noqa: E501

        Client-defined properties associated with this order.  # noqa: E501

        :return: The properties of this BlockedOrderRequest.  # noqa: E501
        :rtype: dict[str, lusid.PerpetualProperty]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BlockedOrderRequest.

        Client-defined properties associated with this order.  # noqa: E501

        :param properties: The properties of this BlockedOrderRequest.  # noqa: E501
        :type properties: dict[str, lusid.PerpetualProperty]
        """

        self._properties = properties

    @property
    def quantity(self):
        """Gets the quantity of this BlockedOrderRequest.  # noqa: E501

        The quantity of given instrument ordered.  # noqa: E501

        :return: The quantity of this BlockedOrderRequest.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this BlockedOrderRequest.

        The quantity of given instrument ordered.  # noqa: E501

        :param quantity: The quantity of this BlockedOrderRequest.  # noqa: E501
        :type quantity: float
        """
        if self.local_vars_configuration.client_side_validation and quantity is None:  # noqa: E501
            raise ValueError("Invalid value for `quantity`, must not be `None`")  # noqa: E501

        self._quantity = quantity

    @property
    def order_book_id(self):
        """Gets the order_book_id of this BlockedOrderRequest.  # noqa: E501


        :return: The order_book_id of this BlockedOrderRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._order_book_id

    @order_book_id.setter
    def order_book_id(self, order_book_id):
        """Sets the order_book_id of this BlockedOrderRequest.


        :param order_book_id: The order_book_id of this BlockedOrderRequest.  # noqa: E501
        :type order_book_id: lusid.ResourceId
        """

        self._order_book_id = order_book_id

    @property
    def portfolio_id(self):
        """Gets the portfolio_id of this BlockedOrderRequest.  # noqa: E501


        :return: The portfolio_id of this BlockedOrderRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._portfolio_id

    @portfolio_id.setter
    def portfolio_id(self, portfolio_id):
        """Sets the portfolio_id of this BlockedOrderRequest.


        :param portfolio_id: The portfolio_id of this BlockedOrderRequest.  # noqa: E501
        :type portfolio_id: lusid.ResourceId
        """

        self._portfolio_id = portfolio_id

    @property
    def id(self):
        """Gets the id of this BlockedOrderRequest.  # noqa: E501


        :return: The id of this BlockedOrderRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BlockedOrderRequest.


        :param id: The id of this BlockedOrderRequest.  # noqa: E501
        :type id: lusid.ResourceId
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def state(self):
        """Gets the state of this BlockedOrderRequest.  # noqa: E501

        The order's state (examples: New, PartiallyFilled, ...)  # noqa: E501

        :return: The state of this BlockedOrderRequest.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BlockedOrderRequest.

        The order's state (examples: New, PartiallyFilled, ...)  # noqa: E501

        :param state: The state of this BlockedOrderRequest.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def date(self):
        """Gets the date of this BlockedOrderRequest.  # noqa: E501

        The date on which the order was made  # noqa: E501

        :return: The date of this BlockedOrderRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this BlockedOrderRequest.

        The date on which the order was made  # noqa: E501

        :param date: The date of this BlockedOrderRequest.  # noqa: E501
        :type date: datetime
        """

        self._date = date

    @property
    def price(self):
        """Gets the price of this BlockedOrderRequest.  # noqa: E501


        :return: The price of this BlockedOrderRequest.  # noqa: E501
        :rtype: lusid.CurrencyAndAmount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this BlockedOrderRequest.


        :param price: The price of this BlockedOrderRequest.  # noqa: E501
        :type price: lusid.CurrencyAndAmount
        """

        self._price = price

    @property
    def order_instruction(self):
        """Gets the order_instruction of this BlockedOrderRequest.  # noqa: E501


        :return: The order_instruction of this BlockedOrderRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._order_instruction

    @order_instruction.setter
    def order_instruction(self, order_instruction):
        """Sets the order_instruction of this BlockedOrderRequest.


        :param order_instruction: The order_instruction of this BlockedOrderRequest.  # noqa: E501
        :type order_instruction: lusid.ResourceId
        """

        self._order_instruction = order_instruction

    @property
    def package(self):
        """Gets the package of this BlockedOrderRequest.  # noqa: E501


        :return: The package of this BlockedOrderRequest.  # noqa: E501
        :rtype: lusid.ResourceId
        """
        return self._package

    @package.setter
    def package(self, package):
        """Sets the package of this BlockedOrderRequest.


        :param package: The package of this BlockedOrderRequest.  # noqa: E501
        :type package: lusid.ResourceId
        """

        self._package = package

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
        if not isinstance(other, BlockedOrderRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, BlockedOrderRequest):
            return True

        return self.to_dict() != other.to_dict()
