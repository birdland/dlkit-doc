from ..osid import search_orders as osid_search_orders


class ParameterSearchOrder(osid_search_orders.OsidRuleSearchOrder):
    """This interface specifies options for ordering search results."""
    def order_by_value_syntax(self, style):
        """Specifies a preference for ordering the results by the value syntax and object type.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_values_shuffled(self, style):
        """Specifies a preference for ordering the results by the shuffle flag.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def get_parameter_search_order_record(self, parameter_record_type):
        """Gets the parameter search order record corresponding to the given parameter record ``Type``.

        Multiple retrievals return the same underlying object.

        :param parameter_record_type: a parameter record type
        :type parameter_record_type: ``osid.type.Type``
        :return: the parameter search order record
        :rtype: ``osid.configuration.records.ParameterSearchOrderRecord``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_record_type)`` is ``false``

        """
        return # osid.configuration.records.ParameterSearchOrderRecord


class ValueSearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidOperableSearchOrder, osid_search_orders.OsidSubjugateableSearchOrder):
    """This interface specifies options for ordering search results."""
    def order_by_priority(self, style):
        """Specifies a preference for ordering the results by the value priority.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_value(self, style):
        """Specifies a preference for ordering the results by the value.

        :param style: a search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_parameter_search_order(self):
        """Tests if a ``ParameterSearchOrder`` is available.

        :return: ``true`` if a parameter search order interface is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_parameter_search_order(self):
        """Gets the parameter search order.

        :return: the parameter search order
        :rtype: ``osid.configuration.ParameterSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_parameter_search_order()`` is ``false``

        """
        return # osid.configuration.ParameterSearchOrder

    parameter_search_order = property(fget=get_parameter_search_order)

    def get_value_search_order_record(self, value_record_type):
        """Gets the value search order record corresponding to the given value record ``Type``.

        Multiple retrievals return the same underlying object.

        :param value_record_type: a value record type
        :type value_record_type: ``osid.type.Type``
        :return: the value search order record
        :rtype: ``osid.configuration.records.ValueSearchOrderRecord``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_record_type)`` is ``false``

        """
        return # osid.configuration.records.ValueSearchOrderRecord


class ConfigurationSearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_configuration_search_order_record(self, configuration_record_type):
        """Gets the configuration search order record corresponding to the given configuration record ``Type``.

        Multiple retrievals return the same underlying object.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: the configuration search order record
        :rtype: ``osid.configuration.records.ConfigurationSearchOrderRecord``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_record_type)`` is ``false``

        """
        return # osid.configuration.records.ConfigurationSearchOrderRecord


