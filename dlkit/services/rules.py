# -*- coding: utf-8 -*-
"""Rules Open Service Interface Definitions
rules version 3.0.0

The Rules OSID provides a means to evaluate rules and retrieve results.
A ``Rule`` represents a something that can be executed and can be
organized into ``Engines``. The rule evaluation accepts a ``Condition``
that is used to supply input conditions to the rule engine.

The Rules OSID does not define a means for authoring rules. Definitions
exist for evaluating, examining and organizing rules. A ``Rule`` is
identified by an Id such that a consumer wishing to evaluate a rule must
have knowledge of the ``Rule Id`` along with the expectations of data
(recod ``Type`` ) required in the ``Condition``. The Rule also implies
the structure of the ``Result,`` which can be a simple boolean value or
another structure defined in a Result Record.

Engines can be organized into hierarchies for federation. An engine that
is a parent of another engine makes visible the rules of its children.

Example where the consumer executes a rule with knowledge of the ``Rule
Id`` , ``ConditionRecord``  ``Type,`` and the meaning of the ``Result``.
  RulesSession session = manager.getRulesSession();
  Condition condition = session.getConditionForRule(shouldIWearACoatRuleId);
  if (!condition.hasRecordType(temperatureConditionRecordType) {
      error ("temperature condition record not supported");
  }
  
  TemperatureCondition temp = condition.getConditionRecord(temperatureConditionRecordType);
  temp.setTemperature(28);
  
  if (session.evaluateRule(shouldIWearACoatRuleId, condition) {
      putOnACoat();
  }



"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class RulesProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any engine federation is exposed.
        Federation is exposed when a specific engine may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of engines appears as a
        single engine.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rules(self):
        """Tests if rule evaluation is supported.

        :return: ``true`` if rule evaluation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rule_lookup(self):
        """Tests for the availability of a rule lookup service.

        :return: ``true`` if rule lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rule_query(self):
        """Tests if querying rules is available.

        :return: ``true`` if rule query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rule_search(self):
        """Tests if searching for rules is available.

        :return: ``true`` if rule search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rule_admin(self):
        """Tests if managing rules is available.

        :return: ``true`` if rule admin is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rule_notification(self):
        """Tests if rule notification is available.

        :return: ``true`` if rule notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rule_engine(self):
        """Tests if rule cataloging is available.

        :return: ``true`` if rule cataloging is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rule_engine_assignment(self):
        """Tests if a rule cataloging assignment service is supported.
        A rule cataloging service maps rules to engines.

        :return: ``true`` if rule cataloging is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rule_smart_engine(self):
        """Tests if rule smart engines is available.

        :return: ``true`` if rule smart engines is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_engine_lookup(self):
        """Tests for the availability of an engine lookup service.

        :return: ``true`` if engine lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_engine_query(self):
        """Tests for the availability of an engine query service.

        :return: ``true`` if engine query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_engine_search(self):
        """Tests if searching for engines is available.

        :return: ``true`` if engine search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_engine_admin(self):
        """Tests for the availability of a engine administrative service for creating and deleting engines.

        :return: ``true`` if engine administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_engine_notification(self):
        """Tests for the availability of an engine notification service.

        :return: ``true`` if engine notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_engine_hierarchy(self):
        """Tests for the availability of an engine hierarchy traversal service.

        :return: ``true`` if engine hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_engine_hierarchy_design(self):
        """Tests for the availability of an engine hierarchy design service.

        :return: ``true`` if engine hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_rules_check(self):
        """Tests for the availability of a rules check service.

        :return: ``true`` if a rules check service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_rule_record_types(self):
        """Gets the supported ``Rule`` record types.

        :return: a list containing the supported rule record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    rule_record_types = property(fget=get_rule_record_types)

    def supports_rule_record_type(self, rule_record_type):
        """Tests if the given ``Rule`` record type is supported.

        :param rule_record_type: a ``Type`` indicating a ``Rule`` record type
        :type rule_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_rule_search_record_types(self):
        """Gets the supported rule search record types.

        :return: a list containing the supported rule search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    rule_search_record_types = property(fget=get_rule_search_record_types)

    def supports_rule_search_record_type(self, rule_search_record_type):
        """Tests if the given rule search record type is supported.

        :param rule_search_record_type: a ``Type`` indicating a rule record type
        :type rule_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``rule_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_engine_record_types(self):
        """Gets the supported ``Engine`` record types.

        :return: a list containing the supported engine record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    engine_record_types = property(fget=get_engine_record_types)

    def supports_engine_record_type(self, engine_record_type):
        """Tests if the given ``Engine`` record type is supported.

        :param engine_record_type: a ``Type`` indicating an ``Engine`` record type
        :type engine_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_engine_search_record_types(self):
        """Gets the supported engine search record types.

        :return: a list containing the supported engine search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    engine_search_record_types = property(fget=get_engine_search_record_types)

    def supports_engine_search_record_type(self, engine_search_record_type):
        """Tests if the given engine search record type is supported.

        :param engine_search_record_type: a ``Type`` indicating an engine record type
        :type engine_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class RulesManager(osid_managers.OsidManager, osid_sessions.OsidSession, RulesProfile):

    def get_rules_session(self):
        """Gets the ``OsidSession`` associated with the rule evaluation service.

        :return: a ``RulesSession``
        :rtype: ``osid.rules.RulesSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_rule_lookup_session(self):
        """Gets the ``OsidSession`` associated with the rule lookup service.

        :return: a ``RuleLookupSession``
        :rtype: ``osid.rules.RuleLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_rule_query_session(self):
        """Gets the ``OsidSession`` associated with the rule query service.

        :return: a ``RuleQuerySession``
        :rtype: ``osid.rules.RuleQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_rule_search_session(self):
        """Gets the ``OsidSession`` associated with the rule search service.

        :return: a ``RuleSearchSession``
        :rtype: ``osid.rules.RuleSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_rule_admin_session(self):
        """Gets the ``OsidSession`` associated with the rule administrative service.

        :return: a ``RuleAdminSession``
        :rtype: ``osid.rules.RuleAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_rule_engine_session(self):
        """Gets the ``OsidSession`` to lookup rule/engine mappings.

        :return: a ``RuleEngineSession``
        :rtype: ``osid.rules.RuleEngineSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_engine()`` is ``false``

        """
        raise UNIMPLEMENTED()

    rule_engine_session = property(fget=get_rule_engine_session)

    def get_rule_engine_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning rules to engines.

        :return: a ``RuleEngineAssignmentSession``
        :rtype: ``osid.rules.RuleEngineAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rule_engine_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_engine_lookup_session(self):
        """Gets the ``OsidSession`` associated with the engine lookup service.

        :return: an ``EngineLookupSession``
        :rtype: ``osid.rules.EngineLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    engine_lookup_session = property(fget=get_engine_lookup_session)

    def get_engine_query_session(self):
        """Gets the ``OsidSession`` associated with the engine query service.

        :return: an ``EngineQuerySession``
        :rtype: ``osid.rules.EngineQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    engine_query_session = property(fget=get_engine_query_session)

    def get_engine_search_session(self):
        """Gets the ``OsidSession`` associated with the engine search service.

        :return: an ``EngineSearchSession``
        :rtype: ``osid.rules.EngineSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    engine_search_session = property(fget=get_engine_search_session)

    def get_engine_admin_session(self):
        """Gets the ``OsidSession`` associated with the engine administrative service.

        :return: an ``EngineAdminSession``
        :rtype: ``osid.rules.EngineAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_engine_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the engine hierarchy service.

        :return: an ``EngineHierarchySession``
        :rtype: ``osid.rules.EngineHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    engine_hierarchy_session = property(fget=get_engine_hierarchy_session)

    def get_engine_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the engine hierarchy design service.

        :return: an ``EngineierarchyDesignSession``
        :rtype: ``osid.rules.EngineHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_engine_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    engine_hierarchy_design_session = property(fget=get_engine_hierarchy_design_session)

    def get_rules_check_manager(self):
        """Gets the ``RulesCheckManager``.

        :return: a ``RulesCheckManager``
        :rtype: ``osid.rules.check.RulesCheckManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules_check_manager()`` is ``false``

        """
        raise UNIMPLEMENTED()

    rules_check_manager = property(fget=get_rules_check_manager)


##
# The following methods are from osid.rules.EngineLookupSession

    def can_lookup_engines(self):
        """Tests if this user can perform ``Engine`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_engine_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_engine_view(self):
        """A complete view of the ``Engine`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_engine(self, engine_id):
        """Gets the ``Engine`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Engine`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Engine`` and retained for compatibility.

        :param engine_id: ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: the engine
        :rtype: ``osid.rules.Engine``
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_ids(self, engine_ids):
        """Gets an ``EngineList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the engines
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Engines`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param engine_ids: the list of ``Ids`` to retrieve
        :type engine_ids: ``osid.id.IdList``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``engine_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_genus_type(self, engine_genus_type):
        """Gets an ``EngineList`` corresponding to the given engine genus ``Type`` which does not include engines of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :param engine_genus_type: an engine genus type
        :type engine_genus_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_parent_genus_type(self, engine_genus_type):
        """Gets an ``EngineList`` corresponding to the given engine genus ``Type`` and include any additional engines with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :param engine_genus_type: an engine genus type
        :type engine_genus_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_record_type(self, engine_record_type):
        """Gets an ``EngineList`` containing the given repository record ``Type``.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :param engine_record_type: a engine record type
        :type engine_record_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_provider(self, resource_id):
        """Gets an ``EngineList`` from the given provider.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines(self):
        """Gets all ``Engines``.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :return: a list of ``Engines``
        :rtype: ``osid.rules.EngineList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    engines = property(fget=get_engines)


##
# The following methods are from osid.rules.EngineQuerySession

    def can_search_engines(self):
        """Tests if this user can perform ``Engine`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_engine_query(self):
        """Gets an engine query.

        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``

        """
        raise UNIMPLEMENTED()

    engine_query = property(fget=get_engine_query)

    def get_engines_by_query(self, engine_query):
        """Gets a list of ``Engines`` matching the given search.

        :param engine_query: the engine query
        :type engine_query: ``osid.rules.EngineQuery``
        :return: the returned ``EngineList``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineSearchSession

    def get_engine_search(self):
        """Gets an engine search.

        :return: the engine search
        :rtype: ``osid.rules.EngineSearch``

        """
        raise UNIMPLEMENTED()

    engine_search = property(fget=get_engine_search)

    def get_engine_search_order(self):
        """Gets an engine search order.
        The ``EngineSearchOrder`` is supplied to a ``EngineSearch`` to
        specify the ordering of results.

        :return: the engine search order
        :rtype: ``osid.rules.EngineSearchOrder``

        """
        raise UNIMPLEMENTED()

    engine_search_order = property(fget=get_engine_search_order)

    def get_engines_by_search(self, engine_query, engine_search):
        """Gets the search results matching the given search.

        :param engine_query: the engine query
        :type engine_query: ``osid.rules.EngineQuery``
        :param engine_search: the engine search
        :type engine_search: ``osid.rules.EngineSearch``
        :return: the engine search results
        :rtype: ``osid.rules.EngineSearchResults``
        :raise: ``NullArgument`` -- ``engine_query`` or ``engine_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_query`` or ``engine_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_engine_query_from_inspector(self, engine_query_inspector):
        """Gets an engine query from an inspector.
        The inspector is available from a ``EngineSearchResults``.

        :param engine_query_inspector: an engine query inspector
        :type engine_query_inspector: ``osid.rules.EngineQueryInspector``
        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``
        :raise: ``NullArgument`` -- ``engine_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``engine_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineAdminSession

    def can_create_engines(self):
        """Tests if this user can create ``Engines``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Engine`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_engine_with_record_types(self, engine_record_types):
        """Tests if this user can create a single ``Engine`` using the desired record interface types.
        While ``RulesManager.getEngineRecordTypes()`` can be used to
        examine which record interfaces are supported, this method tests
        which record(s) are required for creating a specific ``Engine``.
        Providing an empty array tests if an ``Engine`` can be created
        with no records.

        :param engine_record_types: array of engine record types
        :type engine_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Engine`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_engine_form_for_create(self, engine_record_types):
        """Gets the engine form for creating new engines.
        A new form should be requested for each create transaction.

        :param engine_record_types: array of engine record types
        :type engine_record_types: ``osid.type.Type[]``
        :return: the engine form
        :rtype: ``osid.rules.EngineForm``
        :raise: ``NullArgument`` -- ``engine_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        raise UNIMPLEMENTED()

    def create_engine(self, engine_form):
        """Creates a new ``Engine``.

        :param engine_form: the form for this ``Engine``
        :type engine_form: ``osid.rules.EngineForm``
        :return: the new ``Engine``
        :rtype: ``osid.rules.Engine``
        :raise: ``IllegalState`` -- ``engine_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``engine_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_form`` did not originate from ``get_engine_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_engines(self):
        """Tests if this user can update ``Engines``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Engine`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_engine_form_for_update(self, engine_id):
        """Gets the engine form for updating an existing engine.
        A new engine form should be requested for each update
        transaction.

        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: the engine form
        :rtype: ``osid.rules.EngineForm``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_engine(self, engine_form):
        """Updates an existing engine.

        :param engine_form: the form containing the elements to be updated
        :type engine_form: ``osid.rules.EngineForm``
        :raise: ``IllegalState`` -- ``engine_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``engine_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_form`` did not originate from ``get_engine_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_engines(self):
        """Tests if this user can delete ``Engines``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Engine`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_engine(self, engine_id):
        """Deletes an ``Engine``.

        :param engine_id: the ``Id`` of the ``Engine`` to remove
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_engine_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Engines``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Engine`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_engine(self, engine_id, alias_id):
        """Adds an ``Id`` to an ``Engine`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Engine`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another engine it is
        reassigned to the given engine ``Id``.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineNotificationSession

    def can_register_for_engine_notifications(self):
        """Tests if this user can register for ``Engine`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_engines(self):
        """Register for notifications of new engines.
        ``EngineReceiver.newEngine()`` is invoked when a new ``Engine``
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_engine_ancestors(self, engine_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified engine.
        ``EngineReceiver.newAncestorEngine()`` is invoked when the
        specified engine node gets a new ancestor.

        :param engine_id: the ``Id`` of the ``Engine`` node to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_engine_descendants(self, engine_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified engine.
        ``EngineReceiver.newDescendantEngine()`` is invoked when the
        specified engine node gets a new descendant.

        :param engine_id: the ``Id`` of the ``Engine`` node to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_engines(self):
        """Registers for notification of updated engines.
        ``EngineReceiver.changedEngine()`` is invoked when an engine is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_engine(self, engine_id):
        """Registers for notification of an updated engine.
        ``EngineReceiver.changedEngine()`` is invoked when the specified
        engine is changed.

        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_engines(self):
        """Registers for notification of deleted engines.
        ``EngineReceiver.deletedEngine()`` is invoked when an engine is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_engine(self, engine_id):
        """Registers for notification of a deleted engine.
        ``EngineReceiver.deletedEngine()`` is invoked when the specified
        engine is deleted.

        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_engine_ancestors(self, engine_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified engine.
        ``EngineReceiver.deletedAncestor()`` is invoked when the
        specified engine node loses an ancestor.

        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_engine_descendants(self, engine_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified engine.
        ``EngineReceiver.deletedDescendant()`` is invoked when the
        specified engine node loses a descendant.

        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineHierarchySession

    def get_engine_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    engine_hierarchy_id = property(fget=get_engine_hierarchy_id)

    def get_engine_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    engine_hierarchy = property(fget=get_engine_hierarchy)

    def can_access_engine_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may wish not to offer
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_engine_ids(self):
        """Gets the root engine ``Ids`` in this hierarchy.

        :return: the root engine ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_engine_ids = property(fget=get_root_engine_ids)

    def get_root_engines(self):
        """Gets the root engines in this engine hierarchy.

        :return: the root engines
        :rtype: ``osid.rules.EngineList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_engines = property(fget=get_root_engines)

    def has_parent_engines(self, engine_id):
        """Tests if the ``Engine`` has any parents.

        :param engine_id: the ``Id`` of a engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the engine has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is a direct parent of an engine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an egine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_engine_ids(self, engine_id):
        """Gets the parent ``Ids`` of the given engine.

        :param engine_id: the ``Id`` of an egine
        :type engine_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the engine
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_engines(self, engine_id):
        """Gets the parent engines of the given ``id``.

        :param engine_id: the ``Id`` of the ``Engine`` to query
        :type engine_id: ``osid.id.Id``
        :return: the parent engines of the ``id``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Engine`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is an ancestor of an engine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_engines(self, engine_id):
        """Tests if an engine has any children.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``engine_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_engine(self, id_, engine_id):
        """Tests if an engine is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_engine_ids(self, engine_id):
        """Gets the child ``Ids`` of the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :return: the children of the engine
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_engines(self, engine_id):
        """Gets the child engines of the given ``id``.

        :param engine_id: the ``Id`` of the ``Engine`` to query
        :type engine_id: ``osid.id.Id``
        :return: the child engines of the ``id``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Engine`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is a descendant of an egine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engine_node_ids(self, engine_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an engine node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engine_nodes(self, engine_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an engine node
        :rtype: ``osid.rules.EngineNode``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineHierarchyDesignSession

    def can_modify_engine_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_engine(self, engine_id):
        """Adds a root engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``engine_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_engine(self, engine_id):
        """Removes a root engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not a root
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_engine(self, engine_id, child_id):
        """Adds a child to an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``engine_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``engine_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_engine(self, engine_id, child_id):
        """Removes a child from an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``engine_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_engines(self, engine_id):
        """Removes all children from an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class RulesProxyManager(osid_managers.OsidProxyManager, RulesProfile):

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_rules_check_proxy_manager(self):
        """Gets the ``RulesCheckProxyManager``.

        :return: a ``RulesCheckProxyManager``
        :rtype: ``osid.rules.check.RulesCheckProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_rules_check_manager()`` is ``false``

        """
        raise UNIMPLEMENTED()

    rules_check_proxy_manager = property(fget=get_rules_check_proxy_manager)


##
# The following methods are from osid.rules.EngineLookupSession

    def can_lookup_engines(self):
        """Tests if this user can perform ``Engine`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_engine_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_engine_view(self):
        """A complete view of the ``Engine`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_engine(self, engine_id):
        """Gets the ``Engine`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Engine`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Engine`` and retained for compatibility.


        :param engine_id: ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: the engine
        :rtype: ``osid.rules.Engine``
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_ids(self, engine_ids):
        """Gets an ``EngineList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the engines
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Engines`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.


        :param engine_ids: the list of ``Ids`` to retrieve
        :type engine_ids: ``osid.id.IdList``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``engine_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_genus_type(self, engine_genus_type):
        """Gets an ``EngineList`` corresponding to the given engine genus ``Type`` which does not include engines of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.


        :param engine_genus_type: an engine genus type
        :type engine_genus_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_parent_genus_type(self, engine_genus_type):
        """Gets an ``EngineList`` corresponding to the given engine genus ``Type`` and include any additional engines with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.


        :param engine_genus_type: an engine genus type
        :type engine_genus_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_record_type(self, engine_record_type):
        """Gets an ``EngineList`` containing the given repository record ``Type``.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.


        :param engine_record_type: a engine record type
        :type engine_record_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_provider(self, resource_id):
        """Gets an ``EngineList`` from the given provider.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines(self):
        """Gets all ``Engines``.
        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.


        :return: a list of ``Engines``
        :rtype: ``osid.rules.EngineList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    engines = property(fget=get_engines)


##
# The following methods are from osid.rules.EngineQuerySession

    def can_search_engines(self):
        """Tests if this user can perform ``Engine`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_engine_query(self):
        """Gets an engine query.

        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``

        """
        raise UNIMPLEMENTED()

    engine_query = property(fget=get_engine_query)

    def get_engines_by_query(self, engine_query):
        """Gets a list of ``Engines`` matching the given search.

        :param engine_query: the engine query
        :type engine_query: ``osid.rules.EngineQuery``
        :return: the returned ``EngineList``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineSearchSession

    def get_engine_search(self):
        """Gets an engine search.

        :return: the engine search
        :rtype: ``osid.rules.EngineSearch``

        """
        raise UNIMPLEMENTED()

    engine_search = property(fget=get_engine_search)

    def get_engine_search_order(self):
        """Gets an engine search order.
        The ``EngineSearchOrder`` is supplied to a ``EngineSearch`` to
        specify the ordering of results.


        :return: the engine search order
        :rtype: ``osid.rules.EngineSearchOrder``

        """
        raise UNIMPLEMENTED()

    engine_search_order = property(fget=get_engine_search_order)

    def get_engines_by_search(self, engine_query, engine_search):
        """Gets the search results matching the given search.

        :param engine_query: the engine query
        :type engine_query: ``osid.rules.EngineQuery``
        :param engine_search: the engine search
        :type engine_search: ``osid.rules.EngineSearch``
        :return: the engine search results
        :rtype: ``osid.rules.EngineSearchResults``
        :raise: ``NullArgument`` -- ``engine_query`` or ``engine_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_query`` or ``engine_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_engine_query_from_inspector(self, engine_query_inspector):
        """Gets an engine query from an inspector.
        The inspector is available from a ``EngineSearchResults``.


        :param engine_query_inspector: an engine query inspector
        :type engine_query_inspector: ``osid.rules.EngineQueryInspector``
        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``
        :raise: ``NullArgument`` -- ``engine_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``engine_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineAdminSession

    def can_create_engines(self):
        """Tests if this user can create ``Engines``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Engine`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_engine_with_record_types(self, engine_record_types):
        """Tests if this user can create a single ``Engine`` using the desired record interface types.
        While ``RulesManager.getEngineRecordTypes()`` can be used to
        examine which record interfaces are supported, this method tests
        which record(s) are required for creating a specific ``Engine``.
        Providing an empty array tests if an ``Engine`` can be created
        with no records.


        :param engine_record_types: array of engine record types
        :type engine_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Engine`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_engine_form_for_create(self, engine_record_types):
        """Gets the engine form for creating new engines.
        A new form should be requested for each create transaction.


        :param engine_record_types: array of engine record types
        :type engine_record_types: ``osid.type.Type[]``
        :return: the engine form
        :rtype: ``osid.rules.EngineForm``
        :raise: ``NullArgument`` -- ``engine_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        raise UNIMPLEMENTED()

    def create_engine(self, engine_form):
        """Creates a new ``Engine``.

        :param engine_form: the form for this ``Engine``
        :type engine_form: ``osid.rules.EngineForm``
        :return: the new ``Engine``
        :rtype: ``osid.rules.Engine``
        :raise: ``IllegalState`` -- ``engine_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``engine_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_form`` did not originate from ``get_engine_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_engines(self):
        """Tests if this user can update ``Engines``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Engine`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_engine_form_for_update(self, engine_id):
        """Gets the engine form for updating an existing engine.
        A new engine form should be requested for each update
        transaction.


        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: the engine form
        :rtype: ``osid.rules.EngineForm``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_engine(self, engine_form):
        """Updates an existing engine.

        :param engine_form: the form containing the elements to be updated
        :type engine_form: ``osid.rules.EngineForm``
        :raise: ``IllegalState`` -- ``engine_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``engine_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_form`` did not originate from ``get_engine_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_engines(self):
        """Tests if this user can delete ``Engines``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Engine`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_engine(self, engine_id):
        """Deletes an ``Engine``.

        :param engine_id: the ``Id`` of the ``Engine`` to remove
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_engine_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Engines``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Engine`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_engine(self, engine_id, alias_id):
        """Adds an ``Id`` to an ``Engine`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Engine`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another engine it is
        reassigned to the given engine ``Id``.


        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineNotificationSession

    def can_register_for_engine_notifications(self):
        """Tests if this user can register for ``Engine`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_engines(self):
        """Register for notifications of new engines.
        ``EngineReceiver.newEngine()`` is invoked when a new ``Engine``
        is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_engine_ancestors(self, engine_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified engine.
        ``EngineReceiver.newAncestorEngine()`` is invoked when the
        specified engine node gets a new ancestor.


        :param engine_id: the ``Id`` of the ``Engine`` node to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_engine_descendants(self, engine_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified engine.
        ``EngineReceiver.newDescendantEngine()`` is invoked when the
        specified engine node gets a new descendant.


        :param engine_id: the ``Id`` of the ``Engine`` node to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_engines(self):
        """Registers for notification of updated engines.
        ``EngineReceiver.changedEngine()`` is invoked when an engine is
        changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_engine(self, engine_id):
        """Registers for notification of an updated engine.
        ``EngineReceiver.changedEngine()`` is invoked when the specified
        engine is changed.


        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_engines(self):
        """Registers for notification of deleted engines.
        ``EngineReceiver.deletedEngine()`` is invoked when an engine is
        deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_engine(self, engine_id):
        """Registers for notification of a deleted engine.
        ``EngineReceiver.deletedEngine()`` is invoked when the specified
        engine is deleted.


        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_engine_ancestors(self, engine_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified engine.
        ``EngineReceiver.deletedAncestor()`` is invoked when the
        specified engine node loses an ancestor.


        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_engine_descendants(self, engine_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified engine.
        ``EngineReceiver.deletedDescendant()`` is invoked when the
        specified engine node loses a descendant.


        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineHierarchySession

    def get_engine_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    engine_hierarchy_id = property(fget=get_engine_hierarchy_id)

    def get_engine_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    engine_hierarchy = property(fget=get_engine_hierarchy)

    def can_access_engine_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may wish not to offer
        traversal operations to unauthorized users.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_engine_ids(self):
        """Gets the root engine ``Ids`` in this hierarchy.

        :return: the root engine ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_engine_ids = property(fget=get_root_engine_ids)

    def get_root_engines(self):
        """Gets the root engines in this engine hierarchy.

        :return: the root engines
        :rtype: ``osid.rules.EngineList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_engines = property(fget=get_root_engines)

    def has_parent_engines(self, engine_id):
        """Tests if the ``Engine`` has any parents.

        :param engine_id: the ``Id`` of a engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the engine has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is a direct parent of an engine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an egine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_engine_ids(self, engine_id):
        """Gets the parent ``Ids`` of the given engine.

        :param engine_id: the ``Id`` of an egine
        :type engine_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the engine
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_engines(self, engine_id):
        """Gets the parent engines of the given ``id``.

        :param engine_id: the ``Id`` of the ``Engine`` to query
        :type engine_id: ``osid.id.Id``
        :return: the parent engines of the ``id``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Engine`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is an ancestor of an engine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_engines(self, engine_id):
        """Tests if an engine has any children.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``engine_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_engine(self, id_, engine_id):
        """Tests if an engine is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_engine_ids(self, engine_id):
        """Gets the child ``Ids`` of the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :return: the children of the engine
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_engines(self, engine_id):
        """Gets the child engines of the given ``id``.

        :param engine_id: the ``Id`` of the ``Engine`` to query
        :type engine_id: ``osid.id.Id``
        :return: the child engines of the ``id``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Engine`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is a descendant of an egine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engine_node_ids(self, engine_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an engine node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engine_nodes(self, engine_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an engine node
        :rtype: ``osid.rules.EngineNode``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.EngineHierarchyDesignSession

    def can_modify_engine_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.


        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_engine(self, engine_id):
        """Adds a root engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``engine_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_engine(self, engine_id):
        """Removes a root engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not a root
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_engine(self, engine_id, child_id):
        """Adds a child to an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``engine_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``engine_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_engine(self, engine_id, child_id):
        """Removes a child from an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``engine_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_engines(self, engine_id):
        """Removes all children from an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Engine(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_engine_record(self, engine_record_type):
        """Gets the engine record corresponding to the given ``Engine`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``engine_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(engine_record_type)``
        is ``true`` .

        :param engine_record_type: the type of engine record to retrieve
        :type engine_record_type: ``osid.type.Type``
        :return: the engine record
        :rtype: ``osid.rules.records.EngineRecord``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(engine_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.RulesSession

    def get_engine_id(self):
        """Gets the ``Engine``  ``Id`` associated with this session.

        :return: the ``Engine Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    engine_id = property(fget=get_engine_id)

    def get_engine(self):
        """Gets the ``Engine`` associated with this session.

        :return: the engine
        :rtype: ``osid.rules.Engine``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    engine = property(fget=get_engine)

    def can_evaluate_rules(self):
        """Tests if this user can evaluate rules.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if evaluation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_condition_for_rule(self, rule_id):
        """Gets a condition for the given rule.

        :param rule_id: the ``Id`` of a ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: the returned ``Condition``
        :rtype: ``osid.rules.Condition``
        :raise: ``NotFound`` -- no ``Rule`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def evaluate_rule(self, rule_id, condition):
        """Evaluates a rule based on an input condition.

        :param rule_id: a rule ``Id``
        :type rule_id: ``osid.id.Id``
        :param condition: input conditions
        :type condition: ``osid.rules.Condition``
        :return: result of the evaluation
        :rtype: ``boolean``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``rule_id`` or ``condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``condition`` not of this service

        """
        raise UNIMPLEMENTED()

    def execute_rule(self, rule_id, condition):
        """Executes a rule based on an input condition and returns a result.

        :param rule_id: a rule ``Id``
        :type rule_id: ``osid.id.Id``
        :param condition: input conditions
        :type condition: ``osid.rules.Condition``
        :return: result of the execution
        :rtype: ``osid.rules.Result``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``rule_id`` or ``condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``condition`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.RuleLookupSession

    def can_lookup_rules(self):
        """Tests if this user can perform ``Rule`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_rule_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_rule_view(self):
        """A complete view of the ``Rule`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_engine_view(self):
        """Federates the view for methods in this session.
        A federated view will include rules in engines which are
        children of this engine in the engine hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_engine_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this engine only.



        """
        raise UNIMPLEMENTED()

    def use_active_rule_view(self):
        """Only active rules are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_status_rule_view(self):
        """All active and inactive rules are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_rule(self, rule_id):
        """Gets the ``Rule`` specified by its ``Id``.

        :param rule_id: ``Id`` of the ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: the rule
        :rtype: ``osid.rules.Rule``
        :raise: ``NotFound`` -- ``rule_id`` not found
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_rules_by_ids(self, rule_ids):
        """Gets a ``RuleList`` corresponding to the given ``IdList``.

        :param rule_ids: the list of ``Ids`` to retrieve
        :type rule_ids: ``osid.id.IdList``
        :return: the returned ``Rule`` list
        :rtype: ``osid.rules.RuleList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``rule_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_rules_by_genus_type(self, rule_genus_type):
        """Gets a ``RuleList`` corresponding to the given rule genus ``Type`` which does not include rules of genus types derived from the specified ``Type``.

        :param rule_genus_type: a rule genus type
        :type rule_genus_type: ``osid.type.Type``
        :return: the returned ``Rule`` list
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``rule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_rules_by_parent_genus_type(self, rule_genus_type):
        """Gets a ``RuleList`` corresponding to the given rule genus ``Type`` and include any additional rules with genus types derived from the specified ``Type``.

        :param rule_genus_type: a rule genus type
        :type rule_genus_type: ``osid.type.Type``
        :return: the returned ``Rule`` list
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``rule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_rules_by_record_type(self, rule_record_type):
        """Gets a ``RuleList`` containing the given repository record ``Type``.

        :param rule_record_type: a rule record type
        :type rule_record_type: ``osid.type.Type``
        :return: the returned ``Rule`` list
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_rules(self):
        """Gets all ``Rules``.

        :return: a list of ``Rules``
        :rtype: ``osid.rules.RuleList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    rules = property(fget=get_rules)


##
# The following methods are from osid.rules.RuleQuerySession

    def can_search_rules(self):
        """Tests if this user can perform ``Rule`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_rule_query(self):
        """Gets a rule query.

        :return: the rule query
        :rtype: ``osid.rules.RuleQuery``

        """
        raise UNIMPLEMENTED()

    rule_query = property(fget=get_rule_query)

    def get_rules_by_query(self, rule_query):
        """Gets a list of ``Rules`` matching the given rule query.

        :param rule_query: the rule query
        :type rule_query: ``osid.rules.RuleQuery``
        :return: the returned ``RuleList``
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``rule_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``rule_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.RuleSearchSession

    def get_rule_search(self):
        """Gets a rule search.

        :return: the rule search
        :rtype: ``osid.rules.RuleSearch``

        """
        raise UNIMPLEMENTED()

    rule_search = property(fget=get_rule_search)

    def get_rule_search_order(self):
        """Gets a rule search order.
        The ``RuleSearchOrder`` is supplied to a ``RuleSearch`` to
        specify the ordering of results.

        :return: the rule search order
        :rtype: ``osid.rules.RuleSearchOrder``

        """
        raise UNIMPLEMENTED()

    rule_search_order = property(fget=get_rule_search_order)

    def get_rules_by_search(self, rule_query, rule_search):
        """Gets the search results matching the given search.

        :param rule_query: the rule query
        :type rule_query: ``osid.rules.RuleQuery``
        :param rule_search: the rule search
        :type rule_search: ``osid.rules.RuleSearch``
        :return: the search results
        :rtype: ``osid.rules.RuleSearchResults``
        :raise: ``NullArgument`` -- ``rule_query`` or ``rule_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``rule_query`` or ``rule_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_rule_query_from_inspector(self, rule_query_inspector):
        """Gets a rule query from an inspector.
        The inspector is available from a ``RuleSearchResults``.

        :param rule_query_inspector: a rule query inspector
        :type rule_query_inspector: ``osid.rules.RuleQueryInspector``
        :return: the rule query
        :rtype: ``osid.rules.RuleQuery``
        :raise: ``NullArgument`` -- ``rule_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``rule_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.RuleAdminSession

    def can_create_rules(self):
        """Tests if this user can create ``Rules``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Rule``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Rule`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_rule_with_record_types(self, rule_record_types):
        """Tests if this user can create a single ``Rule`` using the desired record types.
        While ``RulesManager.getRuleRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Rule``.
        Providing an empty array tests if a ``Rule`` can be created with
        no records.

        :param rule_record_types: array of rule record types
        :type rule_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Rule`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``rule_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_rule_form_for_create(self, rule_record_types):
        """Gets the rule form for creating new rules.
        A new form should be requested for each create transaction.

        :param rule_record_types: array of rule record types
        :type rule_record_types: ``osid.type.Type[]``
        :return: the rule form
        :rtype: ``osid.rules.RuleForm``
        :raise: ``NullArgument`` -- ``rule_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        raise UNIMPLEMENTED()

    def create_rule(self, rule_form):
        """Creates a new ``Rule``.

        :param rule_form: the form for this ``Rule``
        :type rule_form: ``osid.rules.RuleForm``
        :return: the new ``Rule``
        :rtype: ``osid.rules.Rule``
        :raise: ``IllegalState`` -- ``rule_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``rule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``rule_form`` did not originate from ``get_rule_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_rules(self):
        """Tests if this user can update ``Rules``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Rule``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if rule modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_rule_form_for_update(self, rule_id):
        """Gets the rule form for updating an existing rule.
        A new rule form should be requested for each update transaction.

        :param rule_id: the ``Id`` of the ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: the rule form
        :rtype: ``osid.rules.RuleForm``
        :raise: ``NotFound`` -- ``rule_id`` is not found
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_rule(self, rule_form):
        """Updates an existing rule.

        :param rule_form: the form containing the elements to be updated
        :type rule_form: ``osid.rules.RuleForm``
        :raise: ``IllegalState`` -- ``rule_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``rule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``rule_form`` did not originate from ``get_rule_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_rules(self):
        """Tests if this user can delete ``Rules``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Rule``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Rule`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_rule(self, rule_id):
        """Deletes the ``Rule`` identified by the given ``Id``.

        :param rule_id: the ``Id`` of the ``Rule`` to delete
        :type rule_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Rule`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_rule_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Rules``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Rule`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_rule(self, rule_id, alias_id):
        """Adds an ``Id`` to a ``Rule`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Rule`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another rule, it is
        reassigned to the given rule ``Id``.

        :param rule_id: the ``Id`` of a ``Rule``
        :type rule_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``rule_id`` not found
        :raise: ``NullArgument`` -- ``rule_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.RuleNotificationSession

    def can_register_for_rule_notifications(self):
        """Tests if this user can register for ``Rule`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_rules(self):
        """Register for notifications of new rules.
        ``RuleReceiver.newRule()`` is invoked when a new ``Rule`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_rules(self):
        """Registers for notification of updated rules.
        ``RuleReceiver.changedRule()`` is invoked when a rule is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_rule(self, rule_id):
        """Registers for notification of an updated rule.
        ``RuleReceiver.changedRule()`` is invoked when the specified
        rule is changed.

        :param rule_id: the ``Id`` of the ``Rule`` to monitor
        :type rule_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_rules(self):
        """Registers for notification of deleted rules.
        ``RuleReceiver.deletedRule()`` is invoked when a rule is removed
        from this engine.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_rule(self, rule_id):
        """Registers for notification of a deleted rule.
        ``RuleReceiver.deletedRule()`` is invoked when the specified
        rule is removed from this engine.

        :param rule_id: the ``Id`` of the ``Rule`` to monitor
        :type rule_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.RuleEngineSession

    def can_lookup_rule_engine_mappings(self):
        """Tests if this user can perform lookups of rule/engine mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_rule_ids_by_engine(self, engine_id):
        """Gets the list of ``Rule Ids`` associated with an ``Engine``.

        :param engine_id: ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: list of related rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_rules_by_engine(self, engine_id):
        """Gets the list of ``Rules`` associated with an ``Engine``.

        :param engine_id: ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: list of related rules
        :rtype: ``osid.rules.RuleList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_rule_ids_by_engines(self, engine_ids):
        """Gets the list of ``Rule Ids`` corresponding to a list of ``Engine`` objects.

        :param engine_ids: list of engine ``Ids``
        :type engine_ids: ``osid.id.IdList``
        :return: list of rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``engine_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_rules_by_engines(self, engine_ids):
        """Gets the list of ``Rules`` corresponding to a list of ``Engine`` objects.

        :param engine_ids: list of engine ``Ids``
        :type engine_ids: ``osid.id.IdList``
        :return: list of rules
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``engine_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engine_ids_by_rule(self, rule_id):
        """Gets the ``Engine``  ``Ids`` mapped to a ``Rule``.

        :param rule_id: ``Id`` of a ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: list of engines
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``rule_id`` is not found
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_engines_by_rule(self, rule_id):
        """Gets the ``Engine`` objects mapped to a ``Rule``.

        :param rule_id: ``Id`` of a ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: list of engines
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- ``rule_id`` is not found
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.RuleEngineAssignmentSession

    def can_assign_rules(self):
        """Tests if this user can alter rule/engine mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_rules_to_engine(self, engine_id):
        """Tests if this user can alter rule/engine mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_engine_ids(self, engine_id):
        """Gets a list of engines including and under the given engine node in which any rule can be assigned.

        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: list of assignable rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_engine_ids_for_rule(self, engine_id, rule_id):
        """Gets a list of engines including and under the given engine node in which a specific rule can be assigned.

        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :param rule_id: the ``Id`` of the ``Engine``
        :type rule_id: ``osid.id.Id``
        :return: list of assignable engine ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``engine_id`` or ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_rule_to_engine(self, rule_id, engine_id):
        """Adds an existing ``Rule`` to an ``Engine``.

        :param rule_id: the ``Id`` of the ``Rule``
        :type rule_id: ``osid.id.Id``
        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``rule_id`` is already assigned to ``engine_id``
        :raise: ``NotFound`` -- ``rule_id`` or ``engine_id`` not found
        :raise: ``NullArgument`` -- ``rule_id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_rule_from_engine(self, rule_id, engine_id):
        """Removes a ``Rule`` from an ``Engine``.

        :param rule_id: the ``Id`` of the ``Rule``
        :type rule_id: ``osid.id.Id``
        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``rule_id`` or ``engine_id`` not found or ``rule_id`` not assigned to ``engine_id``
        :raise: ``NullArgument`` -- ``rule_id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.rules.RuleSmartEngineSession

    def can_manage_smart_engines(self):
        """Tests if this user can manage smart engines.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart engine management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_rule_query(self, rule_query):
        """Applies a rule query to this engine.

        :param rule_query: the rule query
        :type rule_query: ``osid.rules.RuleQuery``
        :raise: ``NullArgument`` -- ``rule_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``rule_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_rule_query(self):
        """Gets a rule query inspector for this engine.

        :return: the rule query inspector
        :rtype: ``osid.rules.RuleQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_rule_sequencing(self, rule_search_order):
        """Applies a rule search order to this engine.

        :param rule_search_order: the rule search order
        :type rule_search_order: ``osid.rules.RuleSearchOrder``
        :raise: ``NullArgument`` -- ``rule_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``rule_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class EngineList(osid_objects.OsidList):

    def get_next_engine(self):
        """Gets the next ``Engine`` in this list.

        :return: the next ``Engine`` in this list. The ``has_next()`` method should be used to test that a next ``Engine`` is available before calling this method.
        :rtype: ``osid.rules.Engine``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_engine = property(fget=get_next_engine)

    def get_next_engines(self, n):
        """Gets the next set of ``Engine`` elements in this list.
        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Engine`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Engine`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.rules.Engine``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Engines(RulesManager):
    pass


