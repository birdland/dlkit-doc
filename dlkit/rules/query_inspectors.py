from ..osid import query_inspectors as osid_query_inspectors


class RuleQueryInspector(osid_query_inspectors.OsidObjectQueryInspector):
    """This is the query inspector for examining rule queries."""
    def get_engine_id_terms(self):
        """Gets the engine ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    engine_id_terms = property(fget=get_engine_id_terms)

    def get_engine_terms(self):
        """Gets the engine query terms.

        :return: the query terms
        :rtype: ``osid.rules.EngineQueryInspector``

        """
        return # osid.rules.EngineQueryInspector

    engine_terms = property(fget=get_engine_terms)

    def get_rule_query_inspector_record(self, rule_record_type):
        """Gets the rule query inspector record corresponding to the given ``Rule`` record ``Type``.

        :param rule_record_type: a rule record type
        :type rule_record_type: ``osid.type.Type``
        :return: the rule query inspector record
        :rtype: ``osid.rules.records.RuleQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(rule_record_type)`` is ``false``

        """
        return # osid.rules.records.RuleQueryInspectorRecord


class EngineQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining engine queries."""
    def get_rule_id_terms(self):
        """Gets the rule ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    rule_id_terms = property(fget=get_rule_id_terms)

    def get_rule_terms(self):
        """Gets the rule query terms.

        :return: the query terms
        :rtype: ``osid.rules.RuleQueryInspector``

        """
        return # osid.rules.RuleQueryInspector

    rule_terms = property(fget=get_rule_terms)

    def get_ancestor_engine_id_terms(self):
        """Gets the ancestor engine ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_engine_id_terms = property(fget=get_ancestor_engine_id_terms)

    def get_ancestor_engine_terms(self):
        """Gets the ancestor engine query terms.

        :return: the query terms
        :rtype: ``osid.rules.EngineQueryInspector``

        """
        return # osid.rules.EngineQueryInspector

    ancestor_engine_terms = property(fget=get_ancestor_engine_terms)

    def get_descendant_engine_id_terms(self):
        """Gets the descendant engine ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_engine_id_terms = property(fget=get_descendant_engine_id_terms)

    def get_descendant_engine_terms(self):
        """Gets the descendant engine query terms.

        :return: the query terms
        :rtype: ``osid.rules.EngineQueryInspector``

        """
        return # osid.rules.EngineQueryInspector

    descendant_engine_terms = property(fget=get_descendant_engine_terms)

    def get_engine_query_inspector_record(self, engine_record_type):
        """Gets the engine query inspector record corresponding to the given ``Engine`` record ``Type``.

        :param engine_record_type: an engine record type
        :type engine_record_type: ``osid.type.Type``
        :return: the engine query inspector record
        :rtype: ``osid.rules.records.EngineQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(engine_record_type)`` is ``false``

        """
        return # osid.rules.records.EngineQueryInspectorRecord


