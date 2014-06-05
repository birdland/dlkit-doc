from ..osid import queries as osid_queries


class RuleQuery(osid_queries.OsidRuleQuery):
    """This is the query for searching rules.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_engine_id(self, engine_id, match):
        """Sets the engine ``Id`` for this query to match rules assigned to engines.

        :param engine_id: an engine ``Id``
        :type engine_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``

        """
        pass

    def clear_engine_id_terms(self):
        """Clears the engine ``Id`` query terms."""
        pass

    engine_id_terms = property(fdel=clear_engine_id_terms)

    def supports_engine_query(self):
        """Tests if an ``EngineQuery`` is available.

        :return: ``true`` if an engine query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_engine_query(self):
        """Gets the query for an engine query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``
        :raise: ``Unimplemented`` -- ``supports_engine_query()`` is ``false``

        """
        return # osid.rules.EngineQuery

    engine_query = property(fget=get_engine_query)

    def clear_engine_terms(self):
        """Clears the engine query terms."""
        pass

    engine_terms = property(fdel=clear_engine_terms)

    def get_rule_query_record(self, rule_record_type):
        """Gets the rule query record corresponding to the given ``Rule`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param rule_record_type: a rule record type
        :type rule_record_type: ``osid.type.Type``
        :return: the rule query record
        :rtype: ``osid.rules.records.RuleQueryRecord``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(rule_record_type)`` is ``false``

        """
        return # osid.rules.records.RuleQueryRecord


class EngineQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching for engines.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_rule_id(self, rule_id, match):
        """Sets the rule ``Id`` for this query to match rules assigned to engines.

        :param rule_id: a rule ``Id``
        :type rule_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``

        """
        pass

    def clear_rule_id_terms(self):
        """Clears the rule ``Id`` query terms."""
        pass

    rule_id_terms = property(fdel=clear_rule_id_terms)

    def supports_rule_query(self):
        """Tests if a rule query is available.

        :return: ``true`` if a rule query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_rule_query(self):
        """Gets the query for a rule.

        :return: the rule query
        :rtype: ``osid.rules.RuleQuery``
        :raise: ``Unimplemented`` -- ``supports_rule_query()`` is ``false``

        """
        return # osid.rules.RuleQuery

    rule_query = property(fget=get_rule_query)

    def match_any_rule(self, match):
        """Matches engines with any riule.

        :param match: ``true`` to match engines with any rule,, ``false`` to match engines with no rules
        :type match: ``boolean``

        """
        pass

    def clear_rule_terms(self):
        """Clears the rule query terms."""
        pass

    rule_terms = property(fdel=clear_rule_terms)

    def match_ancestor_engine_id(self, engine_id, match):
        """Sets the engine ``Id`` for this query to match engines that have the specified engine as an ancestor.

        :param engine_id: an engine ``Id``
        :type engine_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``

        """
        pass

    def clear_ancestor_engine_id_terms(self):
        """Clears the ancestor engine ``Id`` query terms."""
        pass

    ancestor_engine_id_terms = property(fdel=clear_ancestor_engine_id_terms)

    def supports_ancestor_engine_query(self):
        """Tests if an ``EngineQuery`` is available.

        :return: ``true`` if an engine query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_engine_query(self):
        """Gets the query for an engine.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_engine_query()`` is ``false``

        """
        return # osid.rules.EngineQuery

    ancestor_engine_query = property(fget=get_ancestor_engine_query)

    def match_any_ancestor_engine(self, match):
        """Matches engines with any ancestor.

        :param match: ``true`` to match engine with any ancestor, ``false`` to match root engines
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_engine_terms(self):
        """Clears the ancestor engine query terms."""
        pass

    ancestor_engine_terms = property(fdel=clear_ancestor_engine_terms)

    def match_descendant_engine_id(self, engine_id, match):
        """Sets the engine ``Id`` for this query to match engines that have the specified engine as a descendant.

        :param engine_id: an engine ``Id``
        :type engine_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``

        """
        pass

    def clear_descendant_engine_id_terms(self):
        """Clears the descendant engine ``Id`` query terms."""
        pass

    descendant_engine_id_terms = property(fdel=clear_descendant_engine_id_terms)

    def supports_descendant_engine_query(self):
        """Tests if an ``EngineQuery`` is available.

        :return: ``true`` if an engine query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_engine_query(self):
        """Gets the query for an engine.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_engine_query()`` is ``false``

        """
        return # osid.rules.EngineQuery

    descendant_engine_query = property(fget=get_descendant_engine_query)

    def match_any_descendant_engine(self, match):
        """Matches engines with any descendant.

        :param match: ``true`` to match engine with any descendant, ``false`` to match leaf engines
        :type match: ``boolean``

        """
        pass

    def clear_descendant_engine_terms(self):
        """Clears the descendant engine query terms."""
        pass

    descendant_engine_terms = property(fdel=clear_descendant_engine_terms)

    def get_engine_query_record(self, engine_record_type):
        """Gets the engine query record corresponding to the given ``Engine`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param engine_record_type: an engine record type
        :type engine_record_type: ``osid.type.Type``
        :return: the engine query record
        :rtype: ``osid.rules.records.EngineQueryRecord``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(engine_record_type)`` is ``false``

        """
        return # osid.rules.records.EngineQueryRecord


