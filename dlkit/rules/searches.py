from ..osid import searches as osid_searches


class RuleSearch(osid_searches.OsidSearch):
    """The search interface for governing rule searches."""
    def search_among_rules(self, rule_ids):
        """Execute this search among the given list of rules.

        :param rule_ids: list of rules
        :type rule_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``rule_ids`` is ``null``

        """
        pass

    def order_rule_results(self, rule_search_order):
        """Specify an ordering to the search results.

        :param rule_search_order: rule search order
        :type rule_search_order: ``osid.rules.RuleSearchOrder``
        :raise: ``NullArgument`` -- ``rule_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``rule_search_order`` is not of this service

        """
        pass

    def get_rule_search_record(self, rule_search_record_type):
        """Gets the rule search record corresponding to the given rule search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param rule_search_record_type: a rule search record type
        :type rule_search_record_type: ``osid.type.Type``
        :return: the rule search record
        :rtype: ``osid.rules.records.RuleSearchRecord``
        :raise: ``NullArgument`` -- ``rule_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(rule_search_record_type)`` is ``false``

        """
        return # osid.rules.records.RuleSearchRecord


class RuleSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_rules(self):
        """Gets the rule list resulting from a search.

        :return: the rule list
        :rtype: ``osid.rules.RuleList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.rules.RuleList

    rules = property(fget=get_rules)

    def get_rule_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the rule query inspector
        :rtype: ``osid.rules.RuleQueryInspector``

        """
        return # osid.rules.RuleQueryInspector

    rule_query_inspector = property(fget=get_rule_query_inspector)

    def get_rule_search_results_record(self, rule_search_record_type):
        """Gets the rule search results record corresponding to the given rule search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param rule_search_record_type: a rule search record type
        :type rule_search_record_type: ``osid.type.Type``
        :return: the rule search results record
        :rtype: ``osid.rules.records.RuleSearchResultsRecord``
        :raise: ``NullArgument`` -- ``rule_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(rule_search_record_type)`` is ``false``

        """
        return # osid.rules.records.RuleSearchResultsRecord


class EngineSearch(osid_searches.OsidSearch):
    """The search interface for governing engine searches."""
    def search_among_engines(self, engine_ids):
        """Execute this search among the given list of engines.

        :param engine_ids: list of engines
        :type engine_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``engine_ids`` is ``null``

        """
        pass

    def order_engine_results(self, engine_search_order):
        """Specify an ordering to the search results.

        :param engine_search_order: engine search order
        :type engine_search_order: ``osid.rules.EngineSearchOrder``
        :raise: ``NullArgument`` -- ``engine_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``engine_search_order`` is not of this service

        """
        pass

    def get_engine_search_record(self, engine_search_record_type):
        """Gets the engine search record corresponding to the given engine search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param engine_search_record_type: an engine search record type
        :type engine_search_record_type: ``osid.type.Type``
        :return: the engine search record
        :rtype: ``osid.rules.records.EngineSearchRecord``
        :raise: ``NullArgument`` -- ``engine_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(engine_search_record_type)`` is ``false``

        """
        return # osid.rules.records.EngineSearchRecord


class EngineSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_engines(self):
        """Gets the engine list resulting from a search.

        :return: the engine list
        :rtype: ``osid.rules.EngineList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.rules.EngineList

    engines = property(fget=get_engines)

    def get_engine_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the engine query inspector
        :rtype: ``osid.rules.EngineQueryInspector``

        """
        return # osid.rules.EngineQueryInspector

    engine_query_inspector = property(fget=get_engine_query_inspector)

    def get_engine_search_results_record(self, engine_search_record_type):
        """Gets the engine search results record corresponding to the given engine search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param engine_search_record_type: an engine search record type
        :type engine_search_record_type: ``osid.type.Type``
        :return: the engine search results record
        :rtype: ``osid.rules.records.EngineSearchResultsRecord``
        :raise: ``NullArgument`` -- ``EngineSearchRecordType`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(engine_search_record_type)`` is ``false``

        """
        return # osid.rules.records.EngineSearchResultsRecord


