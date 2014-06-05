from ..osid import search_orders as osid_search_orders


class RuleSearchOrder(osid_search_orders.OsidRuleSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_rule_search_order_record(self, rule_record_type):
        """Gets the rule search order record corresponding to the given rule record ``Type``.

        Multiple retrievals return the same underlying object.

        :param rule_record_type: a rule record type
        :type rule_record_type: ``osid.type.Type``
        :return: the rule search order record
        :rtype: ``osid.rules.records.RuleSearchOrderRecord``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(rule_record_type)`` is ``false``

        """
        return # osid.rules.records.RuleSearchOrderRecord


class EngineSearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_engine_search_order_record(self, engine_record_type):
        """Gets the engine search order record corresponding to the given engine record Type.

        Multiple retrievals return the same underlying object.

        :param engine_record_type: an engine record type
        :type engine_record_type: ``osid.type.Type``
        :return: the engine search order record
        :rtype: ``osid.rules.records.EngineSearchOrderRecord``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(engine_record_type)`` is ``false``

        """
        return # osid.rules.records.EngineSearchOrderRecord


