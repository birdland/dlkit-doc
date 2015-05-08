from ..osid import managers as osid_managers


class LearningProfile(osid_managers.OsidProfile):
    """The ``LearningProfile`` describes the interoperability among learning services."""
    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_lookup(self):
        """Tests if an objective lookup service is supported.

        An objective lookup service defines methods to access
        objectives.

        :return: true if objective lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_query(self):
        """Tests if an objective query service is supported.

        :return: ``true`` if objective query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_search(self):
        """Tests if an objective search service is supported.

        :return: ``true`` if objective search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_admin(self):
        """Tests if an objective administrative service is supported.

        :return: ``true`` if objective admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_notification(self):
        """Tests if objective notification is supported.

        Messages may be sent when objectives are created, modified, or
        deleted.

        :return: ``true`` if objective notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_hierarchy(self):
        """Tests if an objective hierarchy traversal is supported.

        :return: ``true`` if an objective hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_hierarchy_design(self):
        """Tests if an objective hierarchy design is supported.

        :return: ``true`` if an objective hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_sequencing(self):
        """Tests if an objective sequencing design is supported.

        :return: ``true`` if objective sequencing is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_objective_bank(self):
        """Tests if an objective to objective bank lookup session is available.

        :return: ``true`` if objective objective bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_objective_bank_assignment(self):
        """Tests if an objective to objective bank assignment session is available.

        :return: ``true`` if objective objective bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_smart_objective_bank(self):
        """Tests if an objective smart objective bank cataloging service is supported.

        :return: ``true`` if objective smart objective banks are supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_requisite(self):
        """Tests if an objective requisite service is supported.

        :return: ``true`` if objective requisite service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_requisite_assignment(self):
        """Tests if an objective requisite assignment service is supported.

        :return: ``true`` if objective requisite assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_activity_lookup(self):
        """Tests if an activity lookup service is supported.

        :return: ``true`` if activity lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_activity_query(self):
        """Tests if an activity query service is supported.

        :return: ``true`` if activity query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_activity_search(self):
        """Tests if an activity search service is supported.

        :return: ``true`` if activity search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_activity_admin(self):
        """Tests if an activity administrative service is supported.

        :return: ``true`` if activity admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_activity_notification(self):
        """Tests if activity notification is supported.

        Messages may be sent when activities are created, modified, or
        deleted.

        :return: ``true`` if activity notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_activity_objective_bank(self):
        """Tests if an activity to objective bank lookup session is available.

        :return: ``true`` if activity objective bank lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_activity_objective_bank_assignment(self):
        """Tests if an activity to objective bank assignment session is available.

        :return: ``true`` if activity objective bank assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_activity_smart_objective_bank(self):
        """Tests if an activity smart objective bank cataloging service is supported.

        :return: ``true`` if activity smart objective banks are supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_proficiency_lookup(self):
        """Tests if looking up proficiencies is supported.

        :return: ``true`` if proficiency lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_proficiency_query(self):
        """Tests if querying proficiencies is supported.

        :return: ``true`` if proficiency query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_proficiency_search(self):
        """Tests if searching proficiencies is supported.

        :return: ``true`` if proficiency search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_proficiency_admin(self):
        """Tests if proficiencyadministrative service is supported.

        :return: ``true`` if proficiency administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_proficiency_notification(self):
        """Tests if a proficiencynotification service is supported.

        :return: ``true`` if proficiency notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_proficiency_objective_bank(self):
        """Tests if a proficiency objective bank mapping lookup service is supported.

        :return: ``true`` if a proficiency objective bank lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_proficiency_objective_bank_assignment(self):
        """Tests if a proficiency objective bank mapping service is supported.

        :return: ``true`` if proficiency to objective bank mapping service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_proficiency_smart_objective_bank(self):
        """Tests if a proficiency smart objective bank cataloging service is supported.

        :return: ``true`` if proficiency smart objective banks are supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_my_learning_path(self):
        """Tests if a learning path service is supported for the authenticated agent.

        :return: ``true`` if learning path is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_learning_path(self):
        """Tests if a learning path service is supported.

        :return: ``true`` if learning path is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_bank_lookup(self):
        """Tests if an objective bank lookup service is supported.

        :return: ``true`` if objective bank lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_bank_query(self):
        """Tests if an objective bank query service is supported.

        :return: ``true`` if objective bank query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_bank_search(self):
        """Tests if an objective bank search service is supported.

        :return: ``true`` if objective bank search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_bank_admin(self):
        """Tests if an objective bank administrative service is supported.

        :return: ``true`` if objective bank admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_bank_notification(self):
        """Tests if objective bank notification is supported.

        Messages may be sent when objective banks are created, modified,
        or deleted.

        :return: ``true`` if objective bank notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_bank_hierarchy(self):
        """Tests if an objective bank hierarchy traversal is supported.

        :return: ``true`` if an objective bank hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_objective_bank_hierarchy_design(self):
        """Tests if objective bank hierarchy design is supported.

        :return: ``true`` if an objective bank hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_learning_batch(self):
        """Tests if a learning batch service is supported.

        :return: ``true`` if a learning batch service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_objective_record_types(self):
        """Gets the supported ``Objective`` record types.

        :return: a list containing the supported ``Objective`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    objective_record_types = property(fget=get_objective_record_types)

    def supports_objective_record_type(self, objective_record_type):
        """Tests if the given ``Objective`` record type is supported.

        :param objective_record_type: a ``Type`` indicating an ``Objective`` record type
        :type objective_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_record_type`` is ``null``

        """
        return # boolean

    def get_objective_search_record_types(self):
        """Gets the supported ``Objective`` search record types.

        :return: a list containing the supported ``Objective`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    objective_search_record_types = property(fget=get_objective_search_record_types)

    def supports_objective_search_record_type(self, objective_search_record_type):
        """Tests if the given ``Objective`` search record type is supported.

        :param objective_search_record_type: a ``Type`` indicating an ``Objective`` search record type
        :type objective_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_search_record_type`` is ``null``

        """
        return # boolean

    def get_activity_record_types(self):
        """Gets the supported ``Activity`` record types.

        :return: a list containing the supported ``Activity`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    activity_record_types = property(fget=get_activity_record_types)

    def supports_activity_record_type(self, activity_record_type):
        """Tests if the given ``Activity`` record type is supported.

        :param activity_record_type: a ``Type`` indicating a ``Activity`` record type
        :type activity_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``activity_record_type`` is ``null``

        """
        return # boolean

    def get_activity_search_record_types(self):
        """Gets the supported ``Activity`` search record types.

        :return: a list containing the supported ``Activity`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    activity_search_record_types = property(fget=get_activity_search_record_types)

    def supports_activity_search_record_type(self, activity_search_record_type):
        """Tests if the given ``Activity`` search record type is supported.

        :param activity_search_record_type: a ``Type`` indicating a ``Activity`` search record type
        :type activity_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``activity_search_record_type`` is ``null``

        """
        return # boolean

    def get_proficiency_record_types(self):
        """Gets the supported ``Proficiency`` record types.

        :return: a list containing the supported ``Proficiency`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    proficiency_record_types = property(fget=get_proficiency_record_types)

    def supports_proficiency_record_type(self, proficiency_record_type):
        """Tests if the given ``Proficiency`` record type is supported.

        :param proficiency_record_type: a ``Type`` indicating a ``Proficiency`` record type
        :type proficiency_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proficiency_record_type`` is ``null``

        """
        return # boolean

    def get_proficiency_search_record_types(self):
        """Gets the supported ``Proficiency`` search types.

        :return: a list containing the supported ``Proficiency`` search types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    proficiency_search_record_types = property(fget=get_proficiency_search_record_types)

    def supports_proficiency_search_record_type(self, proficiency_search_record_type):
        """Tests if the given ``Proficiency`` search type is supported.

        :param proficiency_search_record_type: a ``Type`` indicating a ``Proficiency`` search type
        :type proficiency_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proficiency_search_record_type`` is ``null``

        """
        return # boolean

    def get_objective_bank_record_types(self):
        """Gets the supported ``ObjectiveBank`` record types.

        :return: a list containing the supported ``ObjectiveBank`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    objective_bank_record_types = property(fget=get_objective_bank_record_types)

    def supports_objective_bank_record_type(self, objective_bank_record_type):
        """Tests if the given ``ObjectiveBank`` record type is supported.

        :param objective_bank_record_type: a ``Type`` indicating an ``ObjectiveBank`` type
        :type objective_bank_record_type: ``osid.type.Type``
        :return: ``true`` if the given objective bank record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_record_type`` is ``null``

        """
        return # boolean

    def get_objective_bank_search_record_types(self):
        """Gets the supported objective bank search record types.

        :return: a list containing the supported ``ObjectiveBank`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    objective_bank_search_record_types = property(fget=get_objective_bank_search_record_types)

    def supports_objective_bank_search_record_type(self, objective_bank_search_record_type):
        """Tests if the given objective bank search record type is supported.

        :param objective_bank_search_record_type: a ``Type`` indicating an ``ObjectiveBank`` search record type
        :type objective_bank_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``objective_bank_search_record_type`` is ``null``

        """
        return # boolean


class LearningManager(osid_managers.OsidManager, LearningProfile):
    """The learning manager provides access to learning sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``ObjectiveLookupSession:`` a session to look up objectives
      * ``ObjectiveLookupSession:`` a session to query objectives
        ``None``
      * ``ObjectiveSearchSession:`` a session to search objectives
      * ``ObjectiveAdminSession:`` a session to create, modify and
        delete objectives ``None``
      * ``ObjectiveNotificationSession: a`` session to receive messages
        pertaining to objective ```` changes
      * ``ObjectiveHierarchySession:`` a session to traverse objective
        hierarchies
      * ``ObjectiveHierarchyDesignSession:`` a session to design
        objective hierarchies
      * ``ObjectiveSequencingSession:`` a session to sequence objectives
      * ``ObjectiveObjectiveBankSession:`` a session for retriieving
        objective and objective bank mappings
      * ``ObjectiveObjectiveBankAssignmentSession:`` a session for
        managing objective and objective bank mappings
      * ``ObjectiveSmartObjectiveBankSession:`` a session for managing
        dynamic objective banks
      * ``ObjectiveRequisiteSession:`` a session to examine objective
        requisites
      * ``ObjectiveRequisiteAssignmentSession:`` a session to manage
        objective requisites

      * ``ActivityLookupSession:`` a session to look up activities
      * ``ActivityQuerySession:`` a session to query activities ``None``
      * ``ActivitySearchSession:`` a session to search activities
      * ``ActivityAdminSession:`` a session to create, modify and delete
        activities ``None``
      * ``ActivityNotificationSession: a`` session to receive messages
        pertaining to activity ```` changes
      * ``ActivityObjectiveBankSession:`` a session for retriieving
        activity and objective bank mappings
      * ``ActivityObjectiveBankAssignmentSession:`` a session for
        managing activity and objective bank mappings
      * ``ActivitySmartObjectiveBankSession:`` a session for managing
        dynamic objective banks of activities

      * ``ProficiencyLookupSession:`` a session to retrieve
        proficiencies
      * ``ProficiencyQuerySession:`` a session to query proficiencies
      * ``ProficiencySearchSession:`` a session to search for
        proficiencies
      * ``ProficiencyAdminSession:`` a session to create, update, and
        delete proficiencies
      * ``ProficiencyNotificationSession:`` a session to receive
        notifications pertaining to proficiency changes
      * ``ProficiencyObjectiveBankSession:`` a session to look up
        proficiency to objective bank mappings
      * ``ProficiencyObjectiveBankAssignmentSession:`` a session to
        manage proficiency to objective bank mappings
      * ``ProficiencySmartObjectiveBankSession:`` a session to manage
        smart objective banks of proficiencies
      * ``MyLearningPathSession:`` a session to examine learning paths
        of objectives
      * ``LearningPathSession:`` a session to examine learning paths of
        objectives

      * ``ObjectiveBankLookupSession:`` a session to lookup objective
        banks
      * ``ObjectiveBankQuerySession:`` a session to query objective
        banks
      * ``ObjectiveBankSearchSession`` : a session to search objective
        banks
      * ``ObjectiveBankAdminSession`` : a session to create, modify and
        delete objective banks
      * ``ObjectiveBankNotificationSession`` : a session to receive
        messages pertaining to objective bank changes
      * ``ObjectiveBankHierarchySession:`` a session to traverse the
        objective bank hierarchy
      * ``ObjectiveBankHierarchyDesignSession:`` a session to manage the
        objective bank hierarchy


    """
    def get_objective_lookup_session(self):
        """Gets the ``OsidSession`` associated with the objective lookup service.

        :return: an ``ObjectiveLookupSession``
        :rtype: ``osid.learning.ObjectiveLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_lookup()`` is ``false``

        """
        return # osid.learning.ObjectiveLookupSession

    objective_lookup_session = property(fget=get_objective_lookup_session)

    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_lookup_session``
        :rtype: ``osid.learning.ObjectiveLookupSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveLookupSession

    def get_objective_query_session(self):
        """Gets the ``OsidSession`` associated with the objective query service.

        :return: an ``ObjectiveQuerySession``
        :rtype: ``osid.learning.ObjectiveQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` is ``false``

        """
        return # osid.learning.ObjectiveQuerySession

    objective_query_session = property(fget=get_objective_query_session)

    def get_objective_query_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_query_session``
        :rtype: ``osid.learning.ObjectiveQuerySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveQuerySession

    def get_objective_search_session(self):
        """Gets the ``OsidSession`` associated with the objective search service.

        :return: an ``ObjectiveSearchSession``
        :rtype: ``osid.learning.ObjectiveSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_search()`` is ``false``

        """
        return # osid.learning.ObjectiveSearchSession

    objective_search_session = property(fget=get_objective_search_session)

    def get_objective_search_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_search_session``
        :rtype: ``osid.learning.ObjectiveSearchSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveSearchSession

    def get_objective_admin_session(self):
        """Gets the ``OsidSession`` associated with the objective administration service.

        :return: an ``ObjectiveAdminSession``
        :rtype: ``osid.learning.ObjectiveAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_admin()`` is ``false``

        """
        return # osid.learning.ObjectiveAdminSession

    objective_admin_session = property(fget=get_objective_admin_session)

    def get_objective_admin_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective admin service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_admin_session``
        :rtype: ``osid.learning.ObjectiveAdminSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveAdminSession

    def get_objective_notification_session(self, objective_receiver):
        """Gets the notification session for notifications pertaining to objective changes.

        :param objective_receiver: the objective receiver
        :type objective_receiver: ``osid.learning.ObjectiveReceiver``
        :return: an ``ObjectiveNotificationSession``
        :rtype: ``osid.learning.ObjectiveNotificationSession``
        :raise: ``NullArgument`` -- ``objective_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_notification()`` is ``false``

        """
        return # osid.learning.ObjectiveNotificationSession

    def get_objective_notification_session_for_objective_bank(self, objective_receiver, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective notification service for the given objective bank.

        :param objective_receiver: the objective receiver
        :type objective_receiver: ``osid.learning.ObjectiveReceiver``
        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _objective_notification_session``
        :rtype: ``osid.learning.ObjectiveNotificationSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_receiver`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveNotificationSession

    def get_objective_hierarchy_session(self):
        """Gets the session for traversing objective hierarchies.

        :return: an ``ObjectiveHierarchySession``
        :rtype: ``osid.learning.ObjectiveHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy()`` is ``false``

        """
        return # osid.learning.ObjectiveHierarchySession

    objective_hierarchy_session = property(fget=get_objective_hierarchy_session)

    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective hierarchy traversal service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveHierarchySession``
        :rtype: ``osid.learning.ObjectiveHierarchySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveHierarchySession

    def get_objective_hierarchy_design_session(self):
        """Gets the session for designing objective hierarchies.

        :return: an ``ObjectiveHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy_design()`` is ``false``

        """
        return # osid.learning.ObjectiveHierarchyDesignSession

    objective_hierarchy_design_session = property(fget=get_objective_hierarchy_design_session)

    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective hierarchy design service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveHierarchyDesignSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveHierarchyDesignSession

    def get_objective_sequencing_session(self):
        """Gets the session for sequencing objectives.

        :return: an ``ObjectiveSequencingSession``
        :rtype: ``osid.learning.ObjectiveSequencingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_sequencing()`` is ``false``

        """
        return # osid.learning.ObjectiveSequencingSession

    objective_sequencing_session = property(fget=get_objective_sequencing_session)

    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveSequencingSession``
        :rtype: ``osid.learning.ObjectiveSequencingSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_sequencing()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveSequencingSession

    def get_objective_objective_bank_session(self):
        """Gets the session for retrieving objective to objective bank mappings.

        :return: an ``ObjectiveObjectiveBankSession``
        :rtype: ``osid.learning.ObjectiveObjectiveBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_objective_bank()`` is ``false``

        """
        return # osid.learning.ObjectiveObjectiveBankSession

    objective_objective_bank_session = property(fget=get_objective_objective_bank_session)

    def get_objective_objective_bank_assignment_session(self):
        """Gets the session for assigning objective to objective bank mappings.

        :return: an ``ObjectiveObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ObjectiveObjectiveBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_objective_bank_assignment()`` is ``false``

        """
        return # osid.learning.ObjectiveObjectiveBankAssignmentSession

    objective_objective_bank_assignment_session = property(fget=get_objective_objective_bank_assignment_session)

    def get_objective_smart_objective_bank_session(self, objective_bank_id):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveSmartObjectiveBankSession``
        :rtype: ``osid.learning.ObjectiveSmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_smart_objective_bank()`` is ``false``

        """
        return # osid.learning.ObjectiveSmartObjectiveBankSession

    def get_objective_requisite_session(self):
        """Gets the session for examining objective requisites.

        :return: an ``ObjectiveRequisiteSession``
        :rtype: ``osid.learning.ObjectiveRequisiteSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_requisite()`` is ``false``

        """
        return # osid.learning.ObjectiveRequisiteSession

    objective_requisite_session = property(fget=get_objective_requisite_session)

    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveRequisiteSession``
        :rtype: ``osid.learning.ObjectiveRequisiteSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_requisite()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveRequisiteSession

    def get_objective_requisite_assignment_session(self):
        """Gets the session for managing objective requisites.

        :return: an ``ObjectiveRequisiteAssignmentSession``
        :rtype: ``osid.learning.ObjectiveRequisiteAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_requisite_assignment()`` is ``false``

        """
        return # osid.learning.ObjectiveRequisiteAssignmentSession

    objective_requisite_assignment_session = property(fget=get_objective_requisite_assignment_session)

    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ObjectiveRequisiteAssignmentSession``
        :rtype: ``osid.learning.ObjectiveRequisiteAssignmentSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_requisite_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveRequisiteAssignmentSession

    def get_activity_lookup_session(self):
        """Gets the ``OsidSession`` associated with the activity lookup service.

        :return: an ``ActivityLookupSession``
        :rtype: ``osid.learning.ActivityLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_lookup()`` is ``false``

        """
        return # osid.learning.ActivityLookupSession

    activity_lookup_session = property(fget=get_activity_lookup_session)

    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivityLookupSession``
        :rtype: ``osid.learning.ActivityLookupSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivityLookupSession

    def get_activity_query_session(self):
        """Gets the ``OsidSession`` associated with the activity query service.

        :return: a ``ActivityQuerySession``
        :rtype: ``osid.learning.ActivityQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` is ``false``

        """
        return # osid.learning.ActivityQuerySession

    activity_query_session = property(fget=get_activity_query_session)

    def get_activity_query_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivityQuerySession``
        :rtype: ``osid.learning.ActivityQuerySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivityQuerySession

    def get_activity_search_session(self):
        """Gets the ``OsidSession`` associated with the activity search service.

        :return: a ``ActivitySearchSession``
        :rtype: ``osid.learning.ActivitySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_search()`` is ``false``

        """
        return # osid.learning.ActivitySearchSession

    activity_search_session = property(fget=get_activity_search_session)

    def get_activity_search_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivitySearchSession``
        :rtype: ``osid.learning.ActivitySearchSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivitySearchSession

    def get_activity_admin_session(self):
        """Gets the ``OsidSession`` associated with the activity administration service.

        :return: a ``ActivityAdminSession``
        :rtype: ``osid.learning.ActivityAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_admin()`` is ``false``

        """
        return # osid.learning.ActivityAdminSession

    activity_admin_session = property(fget=get_activity_admin_session)

    def get_activity_admin_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity admin service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivityAdminSession``
        :rtype: ``osid.learning.ActivityAdminSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivityAdminSession

    def get_activity_notification_session(self, activity_receiver):
        """Gets the notification session for notifications pertaining to activity changes.

        :param activity_receiver: the activity receiver
        :type activity_receiver: ``osid.learning.ActivityReceiver``
        :return: an ``ActivityNotificationSession``
        :rtype: ``osid.learning.ActivityNotificationSession``
        :raise: ``NullArgument`` -- ``activity_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_notification()`` is ``false``

        """
        return # osid.learning.ActivityNotificationSession

    def get_activity_notification_session_for_objective_bank(self, activity_receiver, objective_bank_id):
        """Gets the ``OsidSession`` associated with the activity notification service for the given objective bank.

        :param activity_receiver: the activity receiver
        :type activity_receiver: ``osid.learning.ActivityReceiver``
        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: ``an _activity_notification_session``
        :rtype: ``osid.learning.ActivityNotificationSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``activity_receiver`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivityNotificationSession

    def get_activity_objective_bank_session(self):
        """Gets the session for retrieving activity to objective bank mappings.

        :return: an ``ActivityObjectiveBankSession``
        :rtype: ``osid.learning.ActivityObjectiveBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_objective_bank()`` is ``false``

        """
        return # osid.learning.ActivityObjectiveBankSession

    activity_objective_bank_session = property(fget=get_activity_objective_bank_session)

    def get_activity_objective_bank_assignment_session(self):
        """Gets the session for assigning activity to objective bank mappings.

        :return: an ``ActivityObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ActivityObjectiveBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_objective_bank_assignment()`` is ``false``

        """
        return # osid.learning.ActivityObjectiveBankAssignmentSession

    activity_objective_bank_assignment_session = property(fget=get_activity_objective_bank_assignment_session)

    def get_activity_smart_objective_bank_session(self, objective_bank_id):
        """Gets the ``OsidSession`` to manage dynamic objective banks of activities.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: an ``ActivitySmartObjectiveBankSession``
        :rtype: ``osid.learning.ActivitySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_smart_objective_bank()`` is ``false``

        """
        return # osid.learning.ActivitySmartObjectiveBankSession

    def get_proficiency_lookup_session(self):
        """Gets the ``OsidSession`` associated with the proficiency lookup service.

        :return: a ``ProficiencyLookupSession``
        :rtype: ``osid.learning.ProficiencyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_lookup()`` is ``false``

        """
        return # osid.learning.ProficiencyLookupSession

    proficiency_lookup_session = property(fget=get_proficiency_lookup_session)

    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the obective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencyLookupSession``
        :rtype: ``osid.learning.ProficiencyLookupSession``
        :raise: ``NotFound`` -- no ``ObjectiveBank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencyLookupSession

    def get_proficiency_query_session(self):
        """Gets the ``OsidSession`` associated with the proficiency query service.

        :return: a ``ProficiencyQuerySession``
        :rtype: ``osid.learning.ProficiencyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_query()`` is ``false``

        """
        return # osid.learning.ProficiencyQuerySession

    proficiency_query_session = property(fget=get_proficiency_query_session)

    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the obective bank
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencyQuerySession``
        :rtype: ``osid.learning.ProficiencyQuerySession``
        :raise: ``NotFound`` -- no ``ObjectiveBank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencyQuerySession

    def get_proficiency_search_session(self):
        """Gets the ``OsidSession`` associated with the proficiency search service.

        :return: a ``ProficiencySearchSession``
        :rtype: ``osid.learning.ProficiencySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_search()`` is ``false``

        """
        return # osid.learning.ProficiencySearchSession

    proficiency_search_session = property(fget=get_proficiency_search_session)

    def get_proficiency_search_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencySearchSession``
        :rtype: ``osid.learning.ProficiencySearchSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencySearchSession

    def get_proficiency_admin_session(self):
        """Gets the ``OsidSession`` associated with the proficiency administration service.

        :return: a ``ProficiencyAdminSession``
        :rtype: ``osid.learning.ProficiencyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_admin()`` is ``false``

        """
        return # osid.learning.ProficiencyAdminSession

    proficiency_admin_session = property(fget=get_proficiency_admin_session)

    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency administration service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencyAdminSession``
        :rtype: ``osid.learning.ProficiencyAdminSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencyAdminSession

    def get_proficiency_notification_session(self, proficiency_receiver):
        """Gets the ``OsidSession`` associated with the proficiency notification service.

        :param proficiency_receiver: the notification callback
        :type proficiency_receiver: ``osid.learning.ProficiencyReceiver``
        :return: a ``ProficiencyNotificationSession``
        :rtype: ``osid.learning.ProficiencyNotificationSession``
        :raise: ``NullArgument`` -- ``proficiency_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_notification()`` is ``false``

        """
        return # osid.learning.ProficiencyNotificationSession

    def get_proficiency_notification_session_for_objective_bank(self, proficiency_receiver, objective_bank_id):
        """Gets the ``OsidSession`` associated with the proficiency notification service for the given objective bank.

        :param proficiency_receiver: the notification callback
        :type proficiency_receiver: ``osid.learning.ProficiencyReceiver``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencyNotificationSession``
        :rtype: ``osid.learning.ProficiencyNotificationSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``proficiency_receiver`` or ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencyNotificationSession

    def get_proficiency_objective_bank_session(self):
        """Gets the ``OsidSession`` to lookup proficiency/objective bank mappings.

        :return: a ``ProficiencyObjectiveBankSession``
        :rtype: ``osid.learning.ProficiencyObjectiveBankSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_objective_bank()`` is ``false``

        """
        return # osid.learning.ProficiencyObjectiveBankSession

    proficiency_objective_bank_session = property(fget=get_proficiency_objective_bank_session)

    def get_proficiency_objective_bank_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning proficiencys to objective banks.

        :return: a ``ProficiencyObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ProficiencyObjectiveBankAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_objective_bank_assignment()`` is ``false``

        """
        return # osid.learning.ProficiencyObjectiveBankAssignmentSession

    proficiency_objective_bank_assignment_session = property(fget=get_proficiency_objective_bank_assignment_session)

    def get_proficiency_smart_objective_bank_session(self, objective_bank_id):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``ProficiencySmartObjectiveBankSession``
        :rtype: ``osid.learning.ProficiencySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_smart_objective_bank()`` is ``false``

        """
        return # osid.learning.ProficiencySmartObjectiveBankSession

    def get_my_learning_path_session(self):
        """Gets the ``OsidSession`` associated with the my learning path service.

        :return: a ``MyLearningPathSession``
        :rtype: ``osid.learning.MyLearningPathSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_learning_path()`` is ``false``

        """
        return # osid.learning.MyLearningPathSession

    my_learning_path_session = property(fget=get_my_learning_path_session)

    def get_my_learning_path_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the my learning path service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``MyLearningPathSession``
        :rtype: ``osid.learning.MyLearningPathSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_learning_path()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.MyLearningPathSession

    def get_learning_path_session(self):
        """Gets the ``OsidSession`` associated with the learning path service.

        :return: a ``LearningPathSession``
        :rtype: ``osid.learning.LearningPathSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_learning_path()`` is ``false``

        """
        return # osid.learning.LearningPathSession

    learning_path_session = property(fget=get_learning_path_session)

    def get_learning_path_session_for_objective_bank(self, objective_bank_id):
        """Gets the ``OsidSession`` associated with the learning path service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :return: a ``LearningPathSession``
        :rtype: ``osid.learning.LearningPathSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supporty_learning_path()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.LearningPathSession

    def get_objective_bank_lookup_session(self):
        """Gets the OsidSession associated with the objective bank lookup service.

        :return: an ``ObjectiveBankLookupSession``
        :rtype: ``osid.learning.ObjectiveBankLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_lookup() is false``

        """
        return # osid.learning.ObjectiveBankLookupSession

    objective_bank_lookup_session = property(fget=get_objective_bank_lookup_session)

    def get_objective_bank_query_session(self):
        """Gets the OsidSession associated with the objective bank query service.

        :return: an ``ObjectiveBankQuerySession``
        :rtype: ``osid.learning.ObjectiveBankQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_query() is false``

        """
        return # osid.learning.ObjectiveBankQuerySession

    objective_bank_query_session = property(fget=get_objective_bank_query_session)

    def get_objective_bank_search_session(self):
        """Gets the OsidSession associated with the objective bank search service.

        :return: an ``ObjectiveBankSearchSession``
        :rtype: ``osid.learning.ObjectiveBankSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_search() is false``

        """
        return # osid.learning.ObjectiveBankSearchSession

    objective_bank_search_session = property(fget=get_objective_bank_search_session)

    def get_objective_bank_admin_session(self):
        """Gets the OsidSession associated with the objective bank administration service.

        :return: an ``ObjectiveBankAdminSession``
        :rtype: ``osid.learning.ObjectiveBankAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_admin() is false``

        """
        return # osid.learning.ObjectiveBankAdminSession

    objective_bank_admin_session = property(fget=get_objective_bank_admin_session)

    def get_objective_bank_notification_session(self, objective_bank_receiver):
        """Gets the notification session for notifications pertaining to objective bank service changes.

        :param objective_bank_receiver: the objective bank receiver
        :type objective_bank_receiver: ``osid.learning.ObjectiveBankReceiver``
        :return: an ``ObjectiveBankNotificationSession``
        :rtype: ``osid.learning.ObjectiveBankNotificationSession``
        :raise: ``NullArgument`` -- ``objective_bank_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_notification() is false``

        """
        return # osid.learning.ObjectiveBankNotificationSession

    def get_objective_bank_hierarchy_session(self):
        """Gets the session traversing objective bank hierarchies.

        :return: an ``ObjectiveBankHierarchySession``
        :rtype: ``osid.learning.ObjectiveBankHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_hierarchy() is false``

        """
        return # osid.learning.ObjectiveBankHierarchySession

    objective_bank_hierarchy_session = property(fget=get_objective_bank_hierarchy_session)

    def get_objective_bank_hierarchy_design_session(self):
        """Gets the session designing objective bank hierarchies.

        :return: an ``ObjectiveBankHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveBankHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_hierarchy_design() is false``

        """
        return # osid.learning.ObjectiveBankHierarchyDesignSession

    objective_bank_hierarchy_design_session = property(fget=get_objective_bank_hierarchy_design_session)

    def get_learning_batch_manager(self):
        """Gets a ``LearningBatchManager``.

        :return: a ``LearningBatchManager``
        :rtype: ``osid.learning.batch.LearningBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_learning_batch() is false``

        """
        return # osid.learning.batch.LearningBatchManager

    learning_batch_manager = property(fget=get_learning_batch_manager)


class LearningProxyManager(osid_managers.OsidProxyManager, LearningProfile):
    """The learning manager provides access to learning sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:

      * ``ObjectiveLookupSession:`` a session to look up objectives
      * ``ObjectiveLookupSession:`` a session to query objectives
        ``None``
      * ``ObjectiveSearchSession:`` a session to search objectives
      * ``ObjectiveAdminSession:`` a session to create, modify and
        delete objectives ``None``
      * ``ObjectiveNotificationSession: a`` session to receive messages
        pertaining to objective ```` changes
      * ``ObjectiveHierarchySession:`` a session to traverse objective
        hierarchies
      * ``ObjectiveHierarchyDesignSession:`` a session to design
        objective hierarchies
      * ``ObjectiveSequencingSession:`` a session to sequence objectives
      * ``ObjectiveObjectiveBankSession:`` a session for retriieving
        objective and objective bank mappings
      * ``ObjectiveObjectiveBankAssignmentSession:`` a session for
        managing objective and objective bank mappings
      * ``ObjectiveSmartObjectiveBankSession:`` a session for managing
        dynamic objective banks
      * ``ObjectiveRequisiteSession:`` a session to examine objective
        requisites
      * ``ObjectiveRequisiteAssignmentSession:`` a session to manage
        objective requisites

      * ``ActivityLookupSession:`` a session to look up activities
      * ``ActivityQuerySession:`` a session to query activities ``None``
      * ``ActivitySearchSession:`` a session to search activities
      * ``ActivityAdminSession:`` a session to create, modify and delete
        activities ``None``
      * ``ActivityNotificationSession: a`` session to receive messages
        pertaining to activity ```` changes
      * ``ActivityObjectiveBankSession:`` a session for retriieving
        activity and objective bank mappings
      * ``ActivityObjectiveBankAssignmentSession:`` a session for
        managing activity and objective bank mappings
      * ``ActivitySmartObjectiveBankSession:`` a session for managing
        dynamic objective banks of activities

      * ``ProficiencyLookupSession:`` a session to retrieve
        proficiencies
      * ``ProficiencyQuerySession:`` a session to query proficiencies
      * ``ProficiencySearchSession:`` a session to search for
        proficiencies
      * ``ProficiencyAdminSession:`` a session to create, update, and
        delete proficiencies
      * ``ProficiencyNotificationSession:`` a session to receive
        notifications pertaining to proficiency changes
      * ``ProficiencyObjectiveBankSession:`` a session to look up
        proficiency to objective bank mappings
      * ``ProficiencyObjectiveBankAssignmentSession:`` a session to
        manage proficiency to objective bank mappings
      * ``ProficiencySmartObjectiveBankSession:`` a session to manage
        smart objective banks of proficiencies
      * ``MyLearningPathSession:`` a session to examine learning paths
        of objectives
      * ``LearningPathSession:`` a session to examine learning paths of
        objectives

      * ``ObjectiveBankLookupSession:`` a session to lookup objective
        banks
      * ``ObjectiveBankQuerySession:`` a session to query objective
        banks
      * ``ObjectiveBankSearchSession`` : a session to search objective
        banks
      * ``ObjectiveBankAdminSession`` : a session to create, modify and
        delete objective banks
      * ``ObjectiveBankNotificationSession`` : a session to receive
        messages pertaining to objective bank changes
      * ``ObjectiveBankHierarchySession:`` a session to traverse the
        objective bank hierarchy
      * ``ObjectiveBankHierarchyDesignSession:`` a session to manage the
        objective bank hierarchy


    """
    def get_objective_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the objective lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveLookupSession``
        :rtype: ``osid.learning.ObjectiveLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_lookup()`` is ``false``

        """
        return # osid.learning.ObjectiveLookupSession

    def get_objective_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_lookup_session``
        :rtype: ``osid.learning.ObjectiveLookupSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveLookupSession

    def get_objective_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the objective query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveQuerySession``
        :rtype: ``osid.learning.ObjectiveQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` is ``false``

        """
        return # osid.learning.ObjectiveQuerySession

    def get_objective_query_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_query_session``
        :rtype: ``osid.learning.ObjectiveQuerySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveQuerySession

    def get_objective_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the objective search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveSearchSession``
        :rtype: ``osid.learning.ObjectiveSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_search()`` is ``false``

        """
        return # osid.learning.ObjectiveSearchSession

    def get_objective_search_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_search_session``
        :rtype: ``osid.learning.ObjectiveSearchSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveSearchSession

    def get_objective_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the objective administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveAdminSession``
        :rtype: ``osid.learning.ObjectiveAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_admin()`` is ``false``

        """
        return # osid.learning.ObjectiveAdminSession

    def get_objective_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective admin service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_admin_session``
        :rtype: ``osid.learning.ObjectiveAdminSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveAdminSession

    def get_objective_notification_session(self, objective_receiver, proxy):
        """Gets the notification session for notifications pertaining to objective changes.

        :param objective_receiver: the objective receiver
        :type objective_receiver: ``osid.learning.ObjectiveReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveNotificationSession``
        :rtype: ``osid.learning.ObjectiveNotificationSession``
        :raise: ``NullArgument`` -- ``objective_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_notification()`` is ``false``

        """
        return # osid.learning.ObjectiveNotificationSession

    def get_objective_notification_session_for_objective_bank(self, objective_receiver, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective notification service for the given objective bank.

        :param objective_receiver: the objective receiver
        :type objective_receiver: ``osid.learning.ObjectiveReceiver``
        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _objective_notification_session``
        :rtype: ``osid.learning.ObjectiveNotificationSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_receiver, objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveNotificationSession

    def get_objective_hierarchy_session(self, proxy):
        """Gets the session for traversing objective hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveHierarchySession``
        :rtype: ``osid.learning.ObjectiveHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy()`` is ``false``

        """
        return # osid.learning.ObjectiveHierarchySession

    def get_objective_hierarchy_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective hierarchy traversal service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveHierarchySession``
        :rtype: ``osid.learning.ObjectiveHierarchySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveHierarchySession

    def get_objective_hierarchy_design_session(self, proxy):
        """Gets the session for designing objective hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy_design()`` is ``false``

        """
        return # osid.learning.ObjectiveHierarchyDesignSession

    def get_objective_hierarchy_design_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective hierarchy design service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveHierarchyDesignSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveHierarchyDesignSession

    def get_objective_sequencing_session(self, proxy):
        """Gets the session for sequencing objectives.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveSequencingSession``
        :rtype: ``osid.learning.ObjectiveSequencingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_sequencing()`` is ``false``

        """
        return # osid.learning.ObjectiveSequencingSession

    def get_objective_sequencing_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveSequencingSession``
        :rtype: ``osid.learning.ObjectiveSequencingSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_sequencing()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveSequencingSession

    def get_objective_objective_bank_session(self, proxy):
        """Gets the session for retrieving objective to objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveObjectiveBankSession``
        :rtype: ``osid.learning.ObjectiveObjectiveBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_objective_bank()`` is ``false``

        """
        return # osid.learning.ObjectiveObjectiveBankSession

    def get_objective_objective_bank_assignment_session(self, proxy):
        """Gets the session for assigning objective to objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ObjectiveObjectiveBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_objective_bank_assignment()`` is ``false``

        """
        return # osid.learning.ObjectiveObjectiveBankAssignmentSession

    def get_objective_smart_objective_bank_session(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` to manage dynamic objective banks of objectives.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveSmartObjectiveBankSession``
        :rtype: ``osid.learning.ActivitySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_smart_objective_bank()`` is ``false``

        """
        return # osid.learning.ActivitySmartObjectiveBankSession

    def get_objective_requisite_session(self, proxy):
        """Gets the session for examining objective requisites.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveRequisiteSession``
        :rtype: ``osid.learning.ObjectiveRequisiteSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_requisite()`` is ``false``

        """
        return # osid.learning.ObjectiveRequisiteSession

    def get_objective_requisite_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveRequisiteSession``
        :rtype: ``osid.learning.ObjectiveRequisiteSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_requisite()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveRequisiteSession

    def get_objective_requisite_assignment_session(self, proxy):
        """Gets the session for managing objective requisites.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveRequisiteAssignmentSession``
        :rtype: ``osid.learning.ObjectiveRequisiteAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_requisite_assignment()`` is ``false``

        """
        return # osid.learning.ObjectiveRequisiteAssignmentSession

    def get_objective_requisite_assignment_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the objective sequencing service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveRequisiteAssignmentSession``
        :rtype: ``osid.learning.ObjectiveRequisiteAssignmentSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_objective_requisite_assignment()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ObjectiveRequisiteAssignmentSession

    def get_activity_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the activity lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityLookupSession``
        :rtype: ``osid.learning.ActivityLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_lookup()`` is ``false``

        """
        return # osid.learning.ActivityLookupSession

    def get_activity_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityLookupSession``
        :rtype: ``osid.learning.ActivityLookupSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivityLookupSession

    def get_activity_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the activity query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityQuerySession``
        :rtype: ``osid.learning.ActivityQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` is ``false``

        """
        return # osid.learning.ActivityQuerySession

    def get_activity_query_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityQuerySession``
        :rtype: ``osid.learning.ActivityQuerySession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivityQuerySession

    def get_activity_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the activity search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivitySearchSession``
        :rtype: ``osid.learning.ActivitySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_search()`` is ``false``

        """
        return # osid.learning.ActivitySearchSession

    def get_activity_search_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivitySearchSession``
        :rtype: ``osid.learning.ActivitySearchSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivitySearchSession

    def get_activity_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the activity administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityAdminSession``
        :rtype: ``osid.learning.ActivityAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_admin()`` is ``false``

        """
        return # osid.learning.ActivityAdminSession

    def get_activity_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity admin service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ActivityAdminSession``
        :rtype: ``osid.learning.ActivityAdminSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivityAdminSession

    def get_activity_notification_session(self, activity_receiver, proxy):
        """Gets the notification session for notifications pertaining to activity changes.

        :param activity_receiver: the activity receiver
        :type activity_receiver: ``osid.learning.ActivityReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityNotificationSession``
        :rtype: ``osid.learning.ActivityNotificationSession``
        :raise: ``NullArgument`` -- ``activity_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_notification()`` is ``false``

        """
        return # osid.learning.ActivityNotificationSession

    def get_activity_notification_session_for_objective_bank(self, activity_receiver, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the activity notification service for the given objective bank.

        :param activity_receiver: the activity receiver
        :type activity_receiver: ``osid.learning.ActivityReceiver``
        :param objective_bank_id: the ``Id`` of the objective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _activity_notification_session``
        :rtype: ``osid.learning.ActivityNotificationSession``
        :raise: ``NotFound`` -- ``objective_bank_id`` not found
        :raise: ``NullArgument`` -- ``activity_receiver, objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_activity_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ActivityNotificationSession

    def get_activity_objective_bank_session(self, proxy):
        """Gets the session for retrieving activity to objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityObjectiveBankSession``
        :rtype: ``osid.learning.ActivityObjectiveBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_objective_bank()`` is ``false``

        """
        return # osid.learning.ActivityObjectiveBankSession

    def get_activity_objective_bank_assignment_session(self, proxy):
        """Gets the session for assigning activity to objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivityObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ActivityObjectiveBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_objective_bank_assignment()`` is ``false``

        """
        return # osid.learning.ActivityObjectiveBankAssignmentSession

    def get_activity_smart_objective_bank_session(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` to manage dynamic objective banks of activities.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ActivitySmartObjectiveBankSession``
        :rtype: ``osid.learning.ActivitySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_activity_smart_objective_bank()`` is ``false``

        """
        return # osid.learning.ActivitySmartObjectiveBankSession

    def get_proficiency_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the proficiency lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyLookupSession``
        :rtype: ``osid.learning.ProficiencyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_lookup()`` is ``false``

        """
        return # osid.learning.ProficiencyLookupSession

    def get_proficiency_lookup_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency lookup service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the obective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyLookupSession``
        :rtype: ``osid.learning.ProficiencyLookupSession``
        :raise: ``NotFound`` -- no ``ObjectiveBank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencyLookupSession

    def get_proficiency_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the proficiency query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyQuerySession``
        :rtype: ``osid.learning.ProficiencyQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_query()`` is ``false``

        """
        return # osid.learning.ProficiencyQuerySession

    def get_proficiency_query_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency query service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the obective bank
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyQuerySession``
        :rtype: ``osid.learning.ProficiencyQuerySession``
        :raise: ``NotFound`` -- no ``ObjectiveBank`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencyQuerySession

    def get_proficiency_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the proficiency search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencySearchSession``
        :rtype: ``osid.learning.ProficiencySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_search()`` is ``false``

        """
        return # osid.learning.ProficiencySearchSession

    def get_proficiency_search_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency search service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencySearchSession``
        :rtype: ``osid.learning.ProficiencySearchSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencySearchSession

    def get_proficiency_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the proficiency administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyAdminSession``
        :rtype: ``osid.learning.ProficiencyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_admin()`` is ``false``

        """
        return # osid.learning.ProficiencyAdminSession

    def get_proficiency_admin_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency administration service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyAdminSession``
        :rtype: ``osid.learning.ProficiencyAdminSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencyAdminSession

    def get_proficiency_notification_session(self, proficiency_receiver, proxy):
        """Gets the ``OsidSession`` associated with the proficiency notification service.

        :param proficiency_receiver: the notification callback
        :type proficiency_receiver: ``osid.learning.ProficiencyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyNotificationSession``
        :rtype: ``osid.learning.ProficiencyNotificationSession``
        :raise: ``NullArgument`` -- ``proficiency_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_notification()`` is ``false``

        """
        return # osid.learning.ProficiencyNotificationSession

    def get_proficiency_notification_session_for_objective_bank(self, proficiency_receiver, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the proficiency notification service for the given objective bank.

        :param proficiency_receiver: the notification callback
        :type proficiency_receiver: ``osid.learning.ProficiencyReceiver``
        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyNotificationSession``
        :rtype: ``osid.learning.ProficiencyNotificationSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``proficiency_receiver, objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.ProficiencyNotificationSession

    def get_proficiency_objective_bank_session(self, proxy):
        """Gets the ``OsidSession`` to lookup proficiency/objective bank mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyObjectiveBankSession``
        :rtype: ``osid.learning.ProficiencyObjectiveBankSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_objective_bank()`` is ``false``

        """
        return # osid.learning.ProficiencyObjectiveBankSession

    def get_proficiency_objective_bank_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning proficiencies to objective banks.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencyObjectiveBankAssignmentSession``
        :rtype: ``osid.learning.ProficiencyObjectiveBankAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_objective_bank_assignment()`` is ``false``

        """
        return # osid.learning.ProficiencyObjectiveBankAssignmentSession

    def get_proficiency_smart_objective_bank_session(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` to manage dynamic objective banks of proficiencies.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProficiencySmartObjectiveBankSession``
        :rtype: ``osid.learning.ProficiencySmartObjectiveBankSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proficiency_smart_objective_bank()`` is ``false``

        """
        return # osid.learning.ProficiencySmartObjectiveBankSession

    def get_my_learning_path_session(self, proxy):
        """Gets the ``OsidSession`` associated with the my learning path service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyLearningPathSession``
        :rtype: ``osid.learning.MyLearningPathSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_learning_path()`` is ``false``

        """
        return # osid.learning.MyLearningPathSession

    def get_my_learning_path_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the my learning path service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyLearningPathSession``
        :rtype: ``osid.learning.MyLearningPathSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_learning_path()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.MyLearningPathSession

    def get_learning_path_session(self, proxy):
        """Gets the ``OsidSession`` associated with the learning path service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LearningPathSession``
        :rtype: ``osid.learning.LearningPathSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_learning_path()`` is ``false``

        """
        return # osid.learning.LearningPathSession

    def get_learning_path_session_for_objective_bank(self, objective_bank_id, proxy):
        """Gets the ``OsidSession`` associated with the learning path service for the given objective bank.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LearningPathSession``
        :rtype: ``osid.learning.LearningPathSession``
        :raise: ``NotFound`` -- no objective bank found by the given ``Id``
        :raise: ``NullArgument`` -- ``objective_bank_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supporty_learning_path()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.learning.LearningPathSession

    def get_objective_bank_lookup_session(self, proxy):
        """Gets the OsidSession associated with the objective bank lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankLookupSession``
        :rtype: ``osid.learning.ObjectiveBankLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_lookup() is false``

        """
        return # osid.learning.ObjectiveBankLookupSession

    def get_objective_bank_query_session(self, proxy):
        """Gets the OsidSession associated with the objective bank query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankQuerySession``
        :rtype: ``osid.learning.ObjectiveBankQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_query() is false``

        """
        return # osid.learning.ObjectiveBankQuerySession

    def get_objective_bank_search_session(self, proxy):
        """Gets the OsidSession associated with the objective bank search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankSearchSession``
        :rtype: ``osid.learning.ObjectiveBankSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_search() is false``

        """
        return # osid.learning.ObjectiveBankSearchSession

    def get_objective_bank_admin_session(self, proxy):
        """Gets the OsidSession associated with the objective bank administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankAdminSession``
        :rtype: ``osid.learning.ObjectiveBankAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_admin() is false``

        """
        return # osid.learning.ObjectiveBankAdminSession

    def get_objective_bank_notification_session(self, objective_bank_receiver, proxy):
        """Gets the notification session for notifications pertaining to objective bank service changes.

        :param objective_bank_receiver: the objective bank receiver
        :type objective_bank_receiver: ``osid.learning.ObjectiveBankReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankNotificationSession``
        :rtype: ``osid.learning.ObjectiveBankNotificationSession``
        :raise: ``NullArgument`` -- ``objective_bank_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_notification() is false``

        """
        return # osid.learning.ObjectiveBankNotificationSession

    def get_objective_bank_hierarchy_session(self, proxy):
        """Gets the session traversing objective bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankHierarchySession``
        :rtype: ``osid.learning.ObjectiveBankHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_hierarchy() is false``

        """
        return # osid.learning.ObjectiveBankHierarchySession

    def get_objective_bank_hierarchy_design_session(self, proxy):
        """Gets the session designing objective bank hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``ObjectiveBankHierarchyDesignSession``
        :rtype: ``osid.learning.ObjectiveBankHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_objective_bank_hierarchy_design() is false``

        """
        return # osid.learning.ObjectiveBankHierarchyDesignSession

    def get_learning_batch_proxy_manager(self):
        """Gets a ``LearningBatchProxyManager``.

        :return: a ``LearningBatchProxyManager``
        :rtype: ``osid.learning.batch.LearningBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_learning_batch() is false``

        """
        return # osid.learning.batch.LearningBatchProxyManager

    learning_batch_proxy_manager = property(fget=get_learning_batch_proxy_manager)


