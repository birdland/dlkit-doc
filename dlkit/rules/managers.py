from ..osid import managers as osid_managers


class RulesProfile(osid_managers.OsidProfile):
    """The rules profile describes the interoperability among rule services."""
    def supports_visible_federation(self):
        """Tests if any engine federation is exposed.

        Federation is exposed when a specific engine may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of engines appears as a
        single engine.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rules(self):
        """Tests if rule evaluation is supported.

        :return: ``true`` if rule evaluation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rule_lookup(self):
        """Tests for the availability of a rule lookup service.

        :return: ``true`` if rule lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rule_query(self):
        """Tests if querying rules is available.

        :return: ``true`` if rule query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rule_search(self):
        """Tests if searching for rules is available.

        :return: ``true`` if rule search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rule_admin(self):
        """Tests if managing rules is available.

        :return: ``true`` if rule admin is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rule_notification(self):
        """Tests if rule notification is available.

        :return: ``true`` if rule notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rule_engine(self):
        """Tests if rule cataloging is available.

        :return: ``true`` if rule cataloging is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rule_engine_assignment(self):
        """Tests if a rule cataloging assignment service is supported.

        A rule cataloging service maps rules to engines.

        :return: ``true`` if rule cataloging is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rule_smart_engine(self):
        """Tests if rule smart engines is available.

        :return: ``true`` if rule smart engines is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_engine_lookup(self):
        """Tests for the availability of an engine lookup service.

        :return: ``true`` if engine lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_engine_query(self):
        """Tests for the availability of an engine query service.

        :return: ``true`` if engine query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_engine_search(self):
        """Tests if searching for engines is available.

        :return: ``true`` if engine search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_engine_admin(self):
        """Tests for the availability of a engine administrative service for creating and deleting engines.

        :return: ``true`` if engine administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_engine_notification(self):
        """Tests for the availability of an engine notification service.

        :return: ``true`` if engine notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_engine_hierarchy(self):
        """Tests for the availability of an engine hierarchy traversal service.

        :return: ``true`` if engine hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_engine_hierarchy_design(self):
        """Tests for the availability of an engine hierarchy design service.

        :return: ``true`` if engine hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_rules_check(self):
        """Tests for the availability of a rules check service.

        :return: ``true`` if a rules check service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_rule_record_types(self):
        """Gets the supported ``Rule`` record types.

        :return: a list containing the supported rule record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    rule_record_types = property(fget=get_rule_record_types)

    def supports_rule_record_type(self, rule_record_type):
        """Tests if the given ``Rule`` record type is supported.

        :param rule_record_type: a ``Type`` indicating a ``Rule`` record type
        :type rule_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``

        """
        return # boolean

    def get_rule_search_record_types(self):
        """Gets the supported rule search record types.

        :return: a list containing the supported rule search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    rule_search_record_types = property(fget=get_rule_search_record_types)

    def supports_rule_search_record_type(self, rule_search_record_type):
        """Tests if the given rule search record type is supported.

        :param rule_search_record_type: a ``Type`` indicating a rule record type
        :type rule_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``rule_search_record_type`` is ``null``

        """
        return # boolean

    def get_engine_record_types(self):
        """Gets the supported ``Engine`` record types.

        :return: a list containing the supported engine record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    engine_record_types = property(fget=get_engine_record_types)

    def supports_engine_record_type(self, engine_record_type):
        """Tests if the given ``Engine`` record type is supported.

        :param engine_record_type: a ``Type`` indicating an ``Engine`` record type
        :type engine_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``

        """
        return # boolean

    def get_engine_search_record_types(self):
        """Gets the supported engine search record types.

        :return: a list containing the supported engine search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    engine_search_record_types = property(fget=get_engine_search_record_types)

    def supports_engine_search_record_type(self, engine_search_record_type):
        """Tests if the given engine search record type is supported.

        :param engine_search_record_type: a ``Type`` indicating an engine record type
        :type engine_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_search_record_type`` is ``null``

        """
        return # boolean


class RulesManager(osid_managers.OsidManager, RulesProfile):
    """The rules manager provides access to rules sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``RulesSession:`` a session for evaluating and executing rules
      * ``RuleLookupSession:`` a session to lookup rules
      * ``RuleSearchSession:`` a session to query rules
      * ``RuleSearchSession:`` a session to search rules
      * ``RuleAdminSession:`` a session to manage rules
      * ``RuleNotificationSession:`` a session to subscribe to
        notifications of new rules
      * ``RuleEngineSession`` a session to retrieve rule engine mappings
      * ``RuleEngineAssignmentSession`` a session to manage rule engine
        mappings
      * ``RuleSmartEngineSession`` a session to manage dynamic engines
      * ``EngineLookupSession:`` a session to retrieve engine objects
      * ``EngineSearchSession:`` a session to query engines
      * ``EngineSearchSession:`` a session to search for engines
      * ``EngineAdminSession:`` a session to create, update and delete
        engines
      * ``EngineNotificationSession:`` a session to receive
        notifications for changes in engines
      * ``EngineHierarchyTraversalSession:`` a session to traverse
        hierarchies of engines
      * ``EngineHierarchyDesignSession:`` a session to manage
        hierarchies of engines

    
    The rules manager also provides a profile for determing the
    supported search types supported by this service.

    """
    def get_rules_session(self):
        """Gets the ``OsidSession`` associated with the rule evaluation service.

        :return: a ``RulesSession``
        :rtype: ``osid.rules.RulesSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules()`` is ``false``

        """
        return # osid.rules.RulesSession

    rules_session = property(fget=get_rules_session)

    def get_rules_session_for_engine(self, engine_id):
        """Gets the ``OsidSession`` associated with the rule evaluation service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: a ``RulesSession``
        :rtype: ``osid.rules.RulesSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RulesSession

    def get_rule_lookup_session(self):
        """Gets the ``OsidSession`` associated with the rule lookup service.

        :return: a ``RuleLookupSession``
        :rtype: ``osid.rules.RuleLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_lookup()`` is ``false``

        """
        return # osid.rules.RuleLookupSession

    rule_lookup_session = property(fget=get_rule_lookup_session)

    def get_rule_lookup_session_for_engine(self, engine_id):
        """Gets the ``OsidSession`` associated with the rule lookup service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: a ``RuleLookupSession``
        :rtype: ``osid.rules.RuleLookupSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleLookupSession

    def get_rule_query_session(self):
        """Gets the ``OsidSession`` associated with the rule query service.

        :return: a ``RuleQuerySession``
        :rtype: ``osid.rules.RuleQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_query()`` is ``false``

        """
        return # osid.rules.RuleQuerySession

    rule_query_session = property(fget=get_rule_query_session)

    def get_rule_query_session_for_engine(self, engine_id):
        """Gets the ``OsidSession`` associated with the rule query service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: a ``RuleQuerySession``
        :rtype: ``osid.rules.RuleQuerySession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleQuerySession

    def get_rule_search_session(self):
        """Gets the ``OsidSession`` associated with the rule search service.

        :return: a ``RuleSearchSession``
        :rtype: ``osid.rules.RuleSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_search()`` is ``false``

        """
        return # osid.rules.RuleSearchSession

    rule_search_session = property(fget=get_rule_search_session)

    def get_rule_search_session_for_engine(self, engine_id):
        """Gets the ``OsidSession`` associated with the rule search service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: a ``RuleSearchSession``
        :rtype: ``osid.rules.RuleSearchSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleSearchSession

    def get_rule_admin_session(self):
        """Gets the ``OsidSession`` associated with the rule administrative service.

        :return: a ``RuleAdminSession``
        :rtype: ``osid.rules.RuleAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_admin()`` is ``false``

        """
        return # osid.rules.RuleAdminSession

    rule_admin_session = property(fget=get_rule_admin_session)

    def get_rule_admin_session_for_engine(self, engine_id):
        """Gets the ``OsidSession`` associated with the rule administrative service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: a ``RuleAdminSession``
        :rtype: ``osid.rules.RuleAdminSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleAdminSession

    def get_rule_notification_session(self, rule_receiver):
        """Gets the ``OsidSession`` associated with the rule notification service.

        :param rule_receiver: the receiver
        :type rule_receiver: ``osid.rules.RuleReceiver``
        :return: a ``RuleNotificationSession``
        :rtype: ``osid.rules.RuleNotificationSession``
        :raise: ``NullArgument`` -- ``rule_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_notification()`` is ``false``

        """
        return # osid.rules.RuleNotificationSession

    def get_rule_notification_session_for_engine(self, rule_receiver, engine_id):
        """Gets the ``OsidSession`` associated with the rule notification service for the given engine.

        :param rule_receiver: the receiver
        :type rule_receiver: ``osid.rules.RuleReceiver``
        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: a ``RuleNotificationSession``
        :rtype: ``osid.rules.RuleNotificationSession``
        :raise: ``NotFound`` -- no ``Rule`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``rule_receiver`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleNotificationSession

    def get_rule_engine_session(self):
        """Gets the ``OsidSession`` to lookup rule/engine mappings.

        :return: a ``RuleEngineSession``
        :rtype: ``osid.rules.RuleEngineSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_engine()`` is ``false``

        """
        return # osid.rules.RuleEngineSession

    rule_engine_session = property(fget=get_rule_engine_session)

    def get_rule_engine_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning rules to engines.

        :return: a ``RuleEngineAssignmentSession``
        :rtype: ``osid.rules.RuleEngineAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_engine_assignment()`` is ``false``

        """
        return # osid.rules.RuleEngineAssignmentSession

    rule_engine_assignment_session = property(fget=get_rule_engine_assignment_session)

    def get_rule_smart_engine_session(self, engine_id):
        """Gets the ``OsidSession`` associated with the rule smart engine service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: a ``RuleSmartEngineSession``
        :rtype: ``osid.rules.RuleSmartEngineSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_smart_engine()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleSmartEngineSession

    def get_engine_lookup_session(self):
        """Gets the ``OsidSession`` associated with the engine lookup service.

        :return: an ``EngineLookupSession``
        :rtype: ``osid.rules.EngineLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_lookup()`` is ``false``

        """
        return # osid.rules.EngineLookupSession

    engine_lookup_session = property(fget=get_engine_lookup_session)

    def get_engine_query_session(self):
        """Gets the ``OsidSession`` associated with the engine query service.

        :return: an ``EngineQuerySession``
        :rtype: ``osid.rules.EngineQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_query()`` is ``false``

        """
        return # osid.rules.EngineQuerySession

    engine_query_session = property(fget=get_engine_query_session)

    def get_engine_search_session(self):
        """Gets the ``OsidSession`` associated with the engine search service.

        :return: an ``EngineSearchSession``
        :rtype: ``osid.rules.EngineSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_search()`` is ``false``

        """
        return # osid.rules.EngineSearchSession

    engine_search_session = property(fget=get_engine_search_session)

    def get_engine_admin_session(self):
        """Gets the ``OsidSession`` associated with the engine administrative service.

        :return: an ``EngineAdminSession``
        :rtype: ``osid.rules.EngineAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_admin()`` is ``false``

        """
        return # osid.rules.EngineAdminSession

    engine_admin_session = property(fget=get_engine_admin_session)

    def get_engine_notification_session(self, engine_receiver):
        """Gets the ``OsidSession`` associated with the engine notification service.

        :param engine_receiver: the receiver
        :type engine_receiver: ``osid.rules.EngineReceiver``
        :return: an ``EngineNotificationSession``
        :rtype: ``osid.rules.EngineNotificationSession``
        :raise: ``NullArgument`` -- ``engine_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_notification()`` is ``false``

        """
        return # osid.rules.EngineNotificationSession

    def get_engine_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the engine hierarchy service.

        :return: an ``EngineHierarchySession``
        :rtype: ``osid.rules.EngineHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_hierarchy()`` is ``false``

        """
        return # osid.rules.EngineHierarchySession

    engine_hierarchy_session = property(fget=get_engine_hierarchy_session)

    def get_engine_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the engine hierarchy design service.

        :return: an ``EngineierarchyDesignSession``
        :rtype: ``osid.rules.EngineHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_hierarchy_design()`` is ``false``

        """
        return # osid.rules.EngineHierarchyDesignSession

    engine_hierarchy_design_session = property(fget=get_engine_hierarchy_design_session)

    def get_rules_check_manager(self):
        """Gets the ``RulesCheckManager``.

        :return: a ``RulesCheckManager``
        :rtype: ``osid.rules.check.RulesCheckManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules_check_manager()`` is ``false``

        """
        return # osid.rules.check.RulesCheckManager

    rules_check_manager = property(fget=get_rules_check_manager)


class RulesProxyManager(osid_managers.OsidProxyManager, RulesProfile):
    """The rules manager provides access to rules sessions and provides interoperability tests for various aspects of this service.

    These methods accept a ``Proxy``. The sessions included in this
    manager are:

      * ``RulesSession:`` a session for evaluating and executing rules
      * ``RuleLookupSession:`` a session to lookup rules
      * ``RuleSearchSession:`` a session to query rules
      * ``RuleSearchSession:`` a session to search rules
      * ``RuleAdminSession:`` a session to manage rules
      * ``RuleNotificationSession:`` a session to subscribe to
        notifications of new rules
      * ``RuleEngineSession`` a session to retrieve rule engine mappings
      * ``RuleEngineAssignmentSession`` a session to manage rule engine
        mappings
      * ``RuleSmartEngineSession`` a session to manage dynamic engines
      * ``EngineLookupSession:`` a session to retrieve engine objects
      * ``EngineSearchSession:`` a session to query engines
      * ``EngineSearchSession:`` a session to search for engines
      * ``EngineAdminSession:`` a session to create, update and delete
        engines
      * ``EngineNotificationSession:`` a session to receive
        notifications for changes in engines
      * ``EngineHierarchyTraversalSession:`` a session to traverse
        hierarchies of engines
      * ``EngineHierarchyDesignSession:`` a session to manage
        hierarchies of engines

    
    The rules manager also provides a profile for determing the
    supported search types supported by this service.

    """
    def get_rules_session(self, proxy):
        """Gets the ``OsidSession`` associated with the rule evaluation service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RulesSession``
        :rtype: ``osid.rules.RulesSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules()`` is ``false``

        """
        return # osid.rules.RulesSession

    def get_rules_session_for_engine(self, engine_id, proxy):
        """Gets the ``OsidSession`` associated with the rule evaluation service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RulesSession``
        :rtype: ``osid.rules.RulesSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RulesSession

    def get_rule_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the rule lookup service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleLookupSession``
        :rtype: ``osid.rules.RuleLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_lookup()`` is ``false``

        """
        return # osid.rules.RuleLookupSession

    def get_rule_lookup_session_for_engine(self, engine_id, proxy):
        """Gets the ``OsidSession`` associated with the rule lookup service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleLookupSession``
        :rtype: ``osid.rules.RuleLookupSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleLookupSession

    def get_rule_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the rule query service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleQuerySession``
        :rtype: ``osid.rules.RuleQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_query()`` is ``false``

        """
        return # osid.rules.RuleQuerySession

    def get_rule_query_session_for_engine(self, engine_id, proxy):
        """Gets the ``OsidSession`` associated with the rule query service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleQuerySession``
        :rtype: ``osid.rules.RuleQuerySession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engine_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleQuerySession

    def get_rule_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the rule search service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleSearchSession``
        :rtype: ``osid.rules.RuleSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_search()`` is ``false``

        """
        return # osid.rules.RuleSearchSession

    def get_rule_search_session_for_engine(self, engine_id, proxy):
        """Gets the ``OsidSession`` associated with the rule search service for the given engine.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleSearchSession``
        :rtype: ``osid.rules.RuleSearchSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engind_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleSearchSession

    def get_rule_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the rule administration service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleAdminSession``
        :rtype: ``osid.rules.RuleAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_admin()`` is ``false``

        """
        return # osid.rules.RuleAdminSession

    def get_rule_admin_session_for_engine(self, engine_id, proxy):
        """Gets the ``OsidSession`` associated with the rule administration service for the given engine.

        :param engine_id: the ``Id`` of the ``Rule``
        :type engine_id: ``osid.id.Id``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleAdminSession``
        :rtype: ``osid.rules.RuleAdminSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engind_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleAdminSession

    def get_rule_notification_session(self, rule_receiver, proxy):
        """Gets the ``OsidSession`` associated with the rule notification service.

        :param rule_receiver: the receiver
        :type rule_receiver: ``osid.rules.RuleReceiver``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleNotificationSession``
        :rtype: ``osid.rules.RuleNotificationSession``
        :raise: ``NullArgument`` -- ``rule_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_notification()`` is ``false``

        """
        return # osid.rules.RuleNotificationSession

    def get_rule_notification_session_for_engine(self, rule_receiver, engine_id, proxy):
        """Gets the ``OsidSession`` associated with the rule notification service for the given engine.

        :param rule_receiver: the receiver
        :type rule_receiver: ``osid.rules.RuleReceiver``
        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleNotificationSession``
        :rtype: ``osid.rules.RuleNotificationSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``rule_receiver, engine_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleNotificationSession

    def get_rule_engine_session(self, proxy):
        """Gets the ``OsidSession`` to lookup rule/engine mappings.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleEngineSession``
        :rtype: ``osid.rules.RuleEngineSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_engine()`` is ``false``

        """
        return # osid.rules.RuleEngineSession

    def get_rule_engine_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning rules to engines.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleEngineAssignmentSession``
        :rtype: ``osid.rules.RuleEngineAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_engine_assignment()`` is ``false``

        """
        return # osid.rules.RuleEngineAssignmentSession

    def get_rule_smart_engine_session(self, engine_id, proxy):
        """Gets the ``OsidSession`` associated with the rule smart engine service for the given engine.

        :param engine_id: the ``Id`` of the ``Rule``
        :type engine_id: ``osid.id.Id``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RuleSmartEngineSession``
        :rtype: ``osid.rules.RuleSmartEngineSession``
        :raise: ``NotFound`` -- no ``Engine`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``engind_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_smart_engine()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.rules.RuleSmartEngineSession

    def get_engine_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the engine lookup service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EngineLookupSession``
        :rtype: ``osid.rules.EngineLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_lookup()`` is ``false``

        """
        return # osid.rules.EngineLookupSession

    def get_engine_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the engine query service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EngineQuerySession``
        :rtype: ``osid.rules.EngineQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_query()`` is ``false``

        """
        return # osid.rules.EngineQuerySession

    def get_engine_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the engine search service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EngineSearchSession``
        :rtype: ``osid.rules.EngineSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_search()`` is ``false``

        """
        return # osid.rules.EngineSearchSession

    def get_engine_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the engine administrative service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EngineAdminSession``
        :rtype: ``osid.rules.EngineAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_admin()`` is ``false``

        """
        return # osid.rules.EngineAdminSession

    def get_engine_notification_session(self, engine_receiver, proxy):
        """Gets the ``OsidSession`` associated with the engine notification service.

        :param engine_receiver: the receiver
        :type engine_receiver: ``osid.rules.EngineReceiver``
        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EngineNotificationSession``
        :rtype: ``osid.rules.EngineNotificationSession``
        :raise: ``NullArgument`` -- ``engine_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_notification()`` is ``false``

        """
        return # osid.rules.EngineNotificationSession

    def get_engine_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the engine hierarchy service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EngineHierarchySession``
        :rtype: ``osid.rules.EngineHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_hierarchy()`` is ``false``

        """
        return # osid.rules.EngineHierarchySession

    def get_engine_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the engine hierarchy design service.

        :param proxy: the proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EngineHierarchyDesignSession``
        :rtype: ``osid.rules.EngineHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_hierarchy_design()`` is ``false``

        """
        return # osid.rules.EngineHierarchyDesignSession

    def get_rules_check_proxy_manager(self):
        """Gets the ``RulesCheckProxyManager``.

        :return: a ``RulesCheckProxyManager``
        :rtype: ``osid.rules.check.RulesCheckProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules_check_manager()`` is ``false``

        """
        return # osid.rules.check.RulesCheckProxyManager

    rules_check_proxy_manager = property(fget=get_rules_check_proxy_manager)


