from ..osid import searches as osid_searches


class ParameterSearch(osid_searches.OsidSearch):
    """``ParameterSearch`` specifies the interface for specifying parameter search options."""
    def search_among_parameters(self, parameter_ids):
        """Executes this search among a given list of parameters.

        :param parameter_ids: list of parameters
        :type parameter_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``parameter_ids`` is ``null``

        """
        pass

    def order_parameter_results(self, parameter_search_order):
        """Specify an ordering to the search results.

        :param parameter_search_order: parameter search order
        :type parameter_search_order: ``osid.configuration.ParameterSearchOrder``
        :raise: ``NullArgument`` -- ``parameter_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``parameter_search_order`` is not of this service

        """
        pass

    def get_parameter_search_record(self, parameter_search_record_type):
        """Gets the parameter search record corresponding to the given parameter search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param parameter_search_record_type: a parameter search record type
        :type parameter_search_record_type: ``osid.type.Type``
        :return: the parameter search record
        :rtype: ``osid.configuration.records.ParameterSearchRecord``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_search_record_type)`` is ``false``

        """
        return # osid.configuration.records.ParameterSearchRecord


class ParameterSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_parameters(self):
        """Gets the parameter list resulting from a search.

        :return: the parameter list
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.configuration.ParameterList

    parameters = property(fget=get_parameters)

    def get_parameter_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the parameter query inspector
        :rtype: ``osid.configuration.ParameterQueryInspector``

        """
        return # osid.configuration.ParameterQueryInspector

    parameter_query_inspector = property(fget=get_parameter_query_inspector)

    def get_parameter_search_results_record(self, parameter_search_record_type):
        """Gets the parameter search results record corresponding to the given parameter search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param parameter_search_record_type: a parameter search record type
        :type parameter_search_record_type: ``osid.type.Type``
        :return: the parameter search results record
        :rtype: ``osid.configuration.records.ParameterSearchResultsRecord``
        :raise: ``NullArgument`` -- ``parameter_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(parameter_search_record_type)`` is ``false``

        """
        return # osid.configuration.records.ParameterSearchResultsRecord


class ValueSearch(osid_searches.OsidSearch):
    """The interface for governing value searches."""
    def search_among_values(self, value_ids):
        """Executes this search among a given list of values.

        :param value_ids: list of values
        :type value_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``value_ids`` is ``null``

        """
        pass

    def order_value_results(self, value_search_order):
        """Specify an ordering to the search results.

        :param value_search_order: value search order
        :type value_search_order: ``osid.configuration.ValueSearchOrder``
        :raise: ``NullArgument`` -- ``value_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``value_search_order`` is not of this service

        """
        pass

    def get_value_search_record(self, value_search_record_type):
        """Gets the value search record corresponding to the given value search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param value_search_record_type: a value search record type
        :type value_search_record_type: ``osid.type.Type``
        :return: the value search record
        :rtype: ``osid.configuration.records.ValueSearchRecord``
        :raise: ``NullArgument`` -- ``value_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_search_record_type)`` is ``false``

        """
        return # osid.configuration.records.ValueSearchRecord


class ValueSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_values(self):
        """Gets the vakue list resulting from a search.

        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.configuration.ValueList

    values = property(fget=get_values)

    def get_value_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the value query inspector
        :rtype: ``osid.configuration.ValueQueryInspector``

        """
        return # osid.configuration.ValueQueryInspector

    value_query_inspector = property(fget=get_value_query_inspector)

    def get_value_search_results_record(self, value_search_record_type):
        """Gets the value search results record corresponding to the given value search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param value_search_record_type: a value search record type
        :type value_search_record_type: ``osid.type.Type``
        :return: the value search results record
        :rtype: ``osid.configuration.records.ValueSearchResultsRecord``
        :raise: ``NullArgument`` -- ``value_search_record_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_search_record_type) is false``

        """
        return # osid.configuration.records.ValueSearchResultsRecord


class ConfigurationSearch(osid_searches.OsidSearch):
    """The search interface to query a configuration."""
    def search_among_configurations(self, configuration_ids):
        """Execute this search among the given list of configurations.

        :param configuration_ids: list of configurations
        :type configuration_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``

        """
        pass

    def order_configuration_results(self, configuration_search_order):
        """Specify an ordering to the search results.

        :param configuration_search_order: configuration search order
        :type configuration_search_order: ``osid.configuration.ConfigurationSearchOrder``
        :raise: ``NullArgument`` -- ``configuration_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``configuration_search_order`` is not of this service

        """
        pass

    def get_configuration_search_record(self, configuration_search_record_type):
        """Gets the configuration search record corresponding to the given configuration search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param configuration_search_record_type: a configuration search record type
        :type configuration_search_record_type: ``osid.type.Type``
        :return: the configuration search record
        :rtype: ``osid.configuration.records.ConfigurationSearchRecord``
        :raise: ``NullArgument`` -- ``configuration_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_search_record_type)`` is ``false``

        """
        return # osid.configuration.records.ConfigurationSearchRecord


class ConfigurationSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_configurations(self):
        """Gets the configuration list resulting from a search.

        :return: the configuration list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.configuration.ConfigurationList

    configurations = property(fget=get_configurations)

    def get_configuration_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the configuration query inspector
        :rtype: ``osid.configuration.ConfigurationQueryInspector``

        """
        return # osid.configuration.ConfigurationQueryInspector

    configuration_query_inspector = property(fget=get_configuration_query_inspector)

    def get_configuration_search_results_record(self, configuration_search_record_type):
        """Gets the configuration search results record corresponding to the given configuration search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param configuration_search_record_type: a configuration search record type
        :type configuration_search_record_type: ``osid.type.Type``
        :return: the configuration search results
        :rtype: ``osid.configuration.records.ConfigurationSearchResultsRecord``
        :raise: ``NullArgument`` -- ``configuration_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_search_record_type) is false``

        """
        return # osid.configuration.records.ConfigurationSearchResultsRecord


