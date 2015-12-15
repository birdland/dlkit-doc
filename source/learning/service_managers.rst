

Service Managers
================


Learning Manager
----------------

.. py:class:: LearningManager(osid_managers.OsidManager, LearningProfile, learning_managers.LearningManager)
    The learning manager provides access to learning sessions and provides interoperability tests
        for
    various aspects of this service.


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





    .. py:method:: get_objective_lookup_session():
        :noindex:


    .. py:attribute:: objective_lookup_session
        :noindex:


    .. py:method:: get_objective_lookup_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_query_session():
        :noindex:


    .. py:attribute:: objective_query_session
        :noindex:


    .. py:method:: get_objective_query_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_search_session():
        :noindex:


    .. py:attribute:: objective_search_session
        :noindex:


    .. py:method:: get_objective_search_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_admin_session():
        :noindex:


    .. py:attribute:: objective_admin_session
        :noindex:


    .. py:method:: get_objective_admin_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_notification_session(objective_receiver):
        :noindex:


    .. py:method:: get_objective_notification_session_for_objective_bank(objective_receiver, objective_bank_id):
        :noindex:


    .. py:method:: get_objective_hierarchy_session():
        :noindex:


    .. py:attribute:: objective_hierarchy_session
        :noindex:


    .. py:method:: get_objective_hierarchy_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_hierarchy_design_session():
        :noindex:


    .. py:attribute:: objective_hierarchy_design_session
        :noindex:


    .. py:method:: get_objective_hierarchy_design_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_sequencing_session():
        :noindex:


    .. py:attribute:: objective_sequencing_session
        :noindex:


    .. py:method:: get_objective_sequencing_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_objective_bank_session():
        :noindex:


    .. py:attribute:: objective_objective_bank_session
        :noindex:


    .. py:method:: get_objective_objective_bank_assignment_session():
        :noindex:


    .. py:attribute:: objective_objective_bank_assignment_session
        :noindex:


    .. py:method:: get_objective_smart_objective_bank_session(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_requisite_session():
        :noindex:


    .. py:attribute:: objective_requisite_session
        :noindex:


    .. py:method:: get_objective_requisite_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_requisite_assignment_session():
        :noindex:


    .. py:attribute:: objective_requisite_assignment_session
        :noindex:


    .. py:method:: get_objective_requisite_assignment_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_lookup_session():
        :noindex:


    .. py:attribute:: activity_lookup_session
        :noindex:


    .. py:method:: get_activity_lookup_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_query_session():
        :noindex:


    .. py:attribute:: activity_query_session
        :noindex:


    .. py:method:: get_activity_query_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_search_session():
        :noindex:


    .. py:attribute:: activity_search_session
        :noindex:


    .. py:method:: get_activity_search_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_admin_session():
        :noindex:


    .. py:attribute:: activity_admin_session
        :noindex:


    .. py:method:: get_activity_admin_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_notification_session(activity_receiver):
        :noindex:


    .. py:method:: get_activity_notification_session_for_objective_bank(activity_receiver, objective_bank_id):
        :noindex:


    .. py:method:: get_activity_objective_bank_session():
        :noindex:


    .. py:attribute:: activity_objective_bank_session
        :noindex:


    .. py:method:: get_activity_objective_bank_assignment_session():
        :noindex:


    .. py:attribute:: activity_objective_bank_assignment_session
        :noindex:


    .. py:method:: get_activity_smart_objective_bank_session(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_lookup_session():
        :noindex:


    .. py:attribute:: proficiency_lookup_session
        :noindex:


    .. py:method:: get_proficiency_lookup_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_query_session():
        :noindex:


    .. py:attribute:: proficiency_query_session
        :noindex:


    .. py:method:: get_proficiency_query_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_search_session():
        :noindex:


    .. py:attribute:: proficiency_search_session
        :noindex:


    .. py:method:: get_proficiency_search_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_admin_session():
        :noindex:


    .. py:attribute:: proficiency_admin_session
        :noindex:


    .. py:method:: get_proficiency_admin_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_notification_session(proficiency_receiver):
        :noindex:


    .. py:method:: get_proficiency_notification_session_for_objective_bank(proficiency_receiver, objective_bank_id):
        :noindex:


    .. py:method:: get_proficiency_objective_bank_session():
        :noindex:


    .. py:attribute:: proficiency_objective_bank_session
        :noindex:


    .. py:method:: get_proficiency_objective_bank_assignment_session():
        :noindex:


    .. py:attribute:: proficiency_objective_bank_assignment_session
        :noindex:


    .. py:method:: get_proficiency_smart_objective_bank_session(objective_bank_id):
        :noindex:


    .. py:method:: get_my_learning_path_session():
        :noindex:


    .. py:attribute:: my_learning_path_session
        :noindex:


    .. py:method:: get_my_learning_path_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_learning_path_session():
        :noindex:


    .. py:attribute:: learning_path_session
        :noindex:


    .. py:method:: get_learning_path_session_for_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_bank_lookup_session():
        :noindex:


    .. py:attribute:: objective_bank_lookup_session
        :noindex:


    .. py:method:: get_objective_bank_query_session():
        :noindex:


    .. py:attribute:: objective_bank_query_session
        :noindex:


    .. py:method:: get_objective_bank_search_session():
        :noindex:


    .. py:attribute:: objective_bank_search_session
        :noindex:


    .. py:method:: get_objective_bank_admin_session():
        :noindex:


    .. py:attribute:: objective_bank_admin_session
        :noindex:


    .. py:method:: get_objective_bank_notification_session(objective_bank_receiver):
        :noindex:


    .. py:method:: get_objective_bank_hierarchy_session():
        :noindex:


    .. py:attribute:: objective_bank_hierarchy_session
        :noindex:


    .. py:method:: get_objective_bank_hierarchy_design_session():
        :noindex:


    .. py:attribute:: objective_bank_hierarchy_design_session
        :noindex:


    .. py:method:: get_learning_batch_manager():
        :noindex:


    .. py:attribute:: learning_batch_manager
        :noindex:




Objective Objective Bank Methods
--------------------------------

    .. py:method:: can_lookup_objective_objective_bank_mappings():
        Tests if this user can perform lookups of objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_bank_view():
        A complete view of the ``Objective`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objective_ids_by_objective_bank(objective_bank_id):
        Gets the list of ``Objective``  ``Ids`` associated with an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.id.IdList) - list of related objectives
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objectives_by_objective_bank(objective_bank_id):
        Gets the list of ``Objectives`` associated with an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.learning.ObjectiveList) - list of related
                objective ``Ids``
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_ids_by_objective_banks(objective_bank_ids):
        Gets the list of ``Objective Ids`` corresponding to a list of ``ObjectiveBanks``.

        :arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        :return: (osid.id.IdList) - list of objective ``Ids``
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objectives_by_objective_banks(objective_bank_ids):
        Gets the list of ``Objectives`` corresponding to a list of ``ObjectiveBanks``.

        :arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        :return: (osid.learning.ObjectiveList) - list of objectives
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_ids_by_objective(objective_id):
        Gets the list of ``ObjectiveBank``  ``Ids`` mapped to an ``Objective``.

        :arg:    objective_id (osid.id.Id): ``Id`` of an ``Objective``
        :return: (osid.id.IdList) - list of objective bank ``Ids``
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_objective(objective_id):
        Gets the list of ``ObjectiveBanks`` mapped to an ``Objective``.

        :arg:    objective_id (osid.id.Id): ``Id`` of an ``Objective``
        :return: (osid.learning.ObjectiveBankList) - list of objective
                banks
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Objective Bank Assignment Methods
-------------------------------------------

    .. py:method:: can_assign_objectives():
        Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_objectives_to_objective_bank(objective_bank_id):
        Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_objective_bank_ids(objective_bank_id):
        Gets a list of objective banks including and under the given objective bank node in which
            any objective can be assigned.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_objective_bank_ids_for_objective(objective_bank_id, objective_id):
        Gets a list of objective banks including and under the given objective bank node in which a
            specific objective can be assigned.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        :raises:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_objective_to_objective_bank(objective_id, objective_bank_id):
        Adds an existing ``Objective`` to an ``ObjectiveBank``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :raises:  AlreadyExists - ``objective_id`` already mapped to
                ``objective_bank_id``
        :raises:  NotFound - ``objective_id`` or ``objective_bank_id`` not
                found
        :raises:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_objective_from_objective_bank(objective_id, objective_bank_id):
        Removes an ``Objective`` from an ``ObjectiveBank``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :raises:  NotFound - ``objective_id`` or ``objective_bank_id`` not
                found or ``objective_id`` not mapped to
                ``objective_bank_id``
        :raises:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_proficiency_to_objective_bank(objective_id, from_objective_bank_id, to_objective_bank_id):
        Moves an ``Objective`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :arg:    from_objective_bank_id (osid.id.Id): the ``Id`` of the
                current ``ObjectiveBank``
        :arg:    to_objective_bank_id (osid.id.Id): the ``Id`` of the
                destination ``ObjectiveBank``
        :raises:  NotFound - ``objective_id, from_objective_bank_id,`` or
                ``to_objective_bank_id`` not found or ``objective_id``
                not mapped to ``from_objective_bank_id``
        :raises:  NullArgument - ``objective_id, from_objective_bank_id,``
                or ``to_objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Activity Objective Bank Methods
-------------------------------

    .. py:method:: can_lookup_activity_objective_bank_mappings():
        Tests if this user can perform lookups of activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_bank_view():
        A complete view of the ``Activity`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_activity_ids_by_objective_bank(objective_bank_id):
        Gets the list of ``Activity``  ``Ids`` associated with an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.id.IdList) - list of related activity ``Ids``
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activities_by_objective_bank(objective_bank_id):
        Gets the list of ``Activities`` associated with an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.learning.ActivityList) - list of related
                activities
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activity_ids_by_objective_banks(objective_bank_ids):
        Gets the list of ``Activity Ids`` corresponding to a list of ``ObjectiveBanks``.

        :arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        :return: (osid.id.IdList) - list of activity ``Ids``
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activities_by_objective_banks(objective_bank_ids):
        Gets the list of ``Activities`` corresponding to a list of ``ObjectiveBanks``.

        :arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        :return: (osid.learning.ActivityList) - list of activities
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_ids_by_activity(activity_id):
        Gets the list of ``ObjectiveBank Ids`` mapped to a ``Activity``.

        :arg:    activity_id (osid.id.Id): ``Id`` of a ``Activity``
        :return: (osid.id.IdList) - list of objective bank ``Ids``
        :raises:  NotFound - ``activity_id`` is not found
        :raises:  NullArgument - ``activity_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_activity(activity_id):
        Gets the list of ``ObjectiveBanks`` mapped to a ``Activity``.

        :arg:    activity_id (osid.id.Id): ``Id`` of a ``Activity``
        :return: (osid.learning.ObjectiveBankList) - list of objective
                bank ``Ids``
        :raises:  NotFound - ``activity_id`` is not found
        :raises:  NullArgument - ``activity_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Activity Objective Bank Assignment Methods
------------------------------------------

    .. py:method:: can_assign_activities():
        Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_activities_to_objective_bank(objective_bank_id):
        Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_objective_bank_ids(objective_bank_id):
        Gets a list of objective banks including and under the given objective bank node in which
            any activity can be assigned.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_objective_bank_ids_for_activity(objective_bank_id, activity_id):
        Gets a list of objective banks including and under the given objective bank node in which a
            specific activity can be assigned.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        :raises:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_activity_to_objective_bank(activity_id, objective_bank_id):
        Adds an existing ``Activity`` to a ``ObjectiveBank``.

        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :raises:  AlreadyExists - ``activity_id`` already mapped to
                ``objective_bank_id``
        :raises:  NotFound - ``activity_id`` or ``objective_bank_id`` not
                found
        :raises:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_activity_from_objective_bank(activity_id, objective_bank_id):
        Removes a ``Activity`` from a ``ObjectiveBank``.

        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :raises:  NotFound - ``activity_id`` or ``objective_bank_id`` not
                found or ``activity_id`` not mapped to
                ``objective_bank_id``
        :raises:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_activity_to_objective_bank(activity_id, from_objective_bank_id, to_objective_bank_id):
        Moves an ``Activity`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :arg:    from_objective_bank_id (osid.id.Id): the ``Id`` of the
                current ``ObjectiveBank``
        :arg:    to_objective_bank_id (osid.id.Id): the ``Id`` of the
                destination ``ObjectiveBank``
        :raises:  NotFound - ``activity_id, from_objective_bank_id,`` or
                ``to_objective_bank_id`` not found or ``activity_id``
                not mapped to ``from_objective_bank_id``
        :raises:  NullArgument - ``activity_id, from_objective_bank_id,``
                or ``to_objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Bank Lookup Methods
-----------------------------

    .. py:method:: can_lookup_objective_banks():
        Tests if this user can perform ``ObjectiveBank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_bank_view():
        A complete view of the ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objective_bank(objective_bank_id):
        Gets the ``ObjectiveBank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``ObjectiveBank`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``ObjectiveBank`` and
        retained for compatility.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.learning.ObjectiveBank) - the objective bank
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objective_banks_by_ids(objective_bank_ids):
        Gets a ``ObjectiveBankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the objective
        banks specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``ObjectiveBank`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :arg:    objective_bank_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_genus_type(objective_bank_genus_type):
        Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` which
            does not include objective banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :arg:    objective_bank_genus_type (osid.type.Type): an objective
                bank genus type
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NullArgument - ``objective_bank_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_parent_genus_type(objective_bank_genus_type):
        Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` and
            include any additional objective banks with genus types derived from the specified
            ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :arg:    objective_bank_genus_type (osid.type.Type): an objective
                bank genus type
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NullArgument - ``objective_bank_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_record_type(objective_bank_record_type):
        Gets a ``ObjectiveBankList`` containing the given objective bank record ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :arg:    objective_bank_record_type (osid.type.Type): an
                objective bank record type
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NullArgument - ``objective_bank_record_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_provider(resource_id):
        Gets a ``ObjectiveBankList`` for the given provider.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks():
        Gets all ``ObjectiveBanks``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :return: (osid.learning.ObjectiveBankList) - a
                ``ObjectiveBankList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_banks




Objective Bank Admin Methods
----------------------------

    .. py:method:: can_create_objective_banks():
        Tests if this user can create ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``ObjectiveBank`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_objective_bank_with_record_types(objective_bank_record_types):
        Tests if this user can create a single ``ObjectiveBank`` using the desired record types.

        While ``LearningManager.getObjectiveBankRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``ObjectiveBank``. Providing an empty array tests if an
        ``ObjectiveBank`` can be created with no records.

        :arg:    objective_bank_record_types (osid.type.Type[]): array of
                objective bank record types
        :return: (boolean) - ``true`` if ``ObjectiveBank`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``objective_bank_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_form_for_create(objective_bank_record_types):
        Gets the objective bank form for creating new objective banks.

        A new form should be requested for each create transaction.

        :arg:    objective_bank_record_types (osid.type.Type[]): array of
                objective bank record types
        :return: (osid.learning.ObjectiveBankForm) - the objective bank
                form
        :raises:  NullArgument - ``objective_bank_record_types`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types.
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_objective_bank(objective_bank_form):
        Creates a new ``ObjectiveBank``.

        :arg:    objective_bank_form (osid.learning.ObjectiveBankForm):
                the form for this ``ObjectiveBank``
        :return: (osid.learning.ObjectiveBank) - the new
                ``ObjectiveBank``
        :raises:  IllegalState - ``objective_bank_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``objective_bank_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``objective_bank_form`` did not originate
                from ``get_objective_bank_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_objective_banks():
        Tests if this user can update ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``ObjectiveBank`` modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_form_for_update(objective_bank_id):
        Gets the objective bank form for updating an existing objective bank.

        A new objective bank form should be requested for each update
        transaction.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.learning.ObjectiveBankForm) - the objective bank
                form
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_objective_bank(objective_bank_form):
        Updates an existing objective bank.

        :arg:    objective_bank_form (osid.learning.ObjectiveBankForm):
                the form containing the elements to be updated
        :raises:  IllegalState - ``objective_bank_form`` already used in
                an update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``objective_bank_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``objective_bank_form did not originate
                from get_objective_bank_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_objective_banks():
        Tests if this user can delete objective banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``ObjectiveBank`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_objective_bank(objective_bank_id):
        Deletes an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank`` to remove
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_objective_bank_aliases():
        Tests if this user can manage ``Id`` aliases for ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``ObjectiveBank`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_objective_bank(objective_bank_id, alias_id):
        Adds an ``Id`` to an ``ObjectiveBank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``ObjectiveBank`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective bank, it
        is reassigned to the given objective bank ``Id``.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                ``ObjectiveBank``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Bank Hierarchy Methods
--------------------------------

    .. py:method:: get_objective_bank_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_hierarchy_id


    .. py:method:: get_objective_bank_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_hierarchy


    .. py:method:: can_access_objective_bank_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_bank_view():
        The returns from the objective bank methods may omit or translate elements based on this
            session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_bank_view():
        A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_objective_bank_ids():
        Gets the root objective bank ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root objective bank ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_objective_bank_ids


    .. py:method:: get_root_objective_banks():
        Gets the root objective banks in this objective bank hierarchy.

        :return: (osid.learning.ObjectiveBankList) - the root objective
                banks
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_objective_banks


    .. py:method:: has_parent_objective_banks(objective_bank_id):
        Tests if the ``ObjectiveBank`` has any parents.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if the objective bank has parents,
                ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_objective_bank(id_, objective_bank_id):
        Tests if an ``Id`` is a direct parent of an objective bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``objective_bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_objective_bank_ids(objective_bank_id):
        Gets the parent ``Ids`` of the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (osid.id.IdList) - the parent ``Ids`` of the objective
                bank
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_objective_banks(objective_bank_id):
        Gets the parents of the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (osid.learning.ObjectiveBankList) - the parents of the
                objective bank
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_objective_bank(id_, objective_bank_id):
        Tests if an ``Id`` is an ancestor of an objective bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``objective_bank_id,`` ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_objective_banks(objective_bank_id):
        Tests if an objective bank has any children.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if the ``objective_bank_id`` has
                children, ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_objective_bank(id_, objective_bank_id):
        Tests if an objective bank is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``objective_bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_objective_bank_ids(objective_bank_id):
        Gets the child ``Ids`` of the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the objective bank
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_objective_banks(objective_bank_id):
        Gets the children of the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        :return: (osid.learning.ObjectiveBankList) - the children of the
                objective bank
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_objective_bank(id_, objective_bank_id):
        Tests if an ``Id`` is a descendant of an objective bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``objective_bank_id,`` ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_objective_bank_node_ids(objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a catalog node
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_nodes(objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.learning.ObjectiveBankNode) - an objective bank
                node
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Bank Hierarchy Design Methods
---------------------------------------

    .. py:method:: get_objective_bank_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_hierarchy_id


    .. py:method:: get_objective_bank_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_hierarchy


    .. py:method:: can_modify_objective_bank_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_objective_bank(objective_bank_id):
        Adds a root objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :raises:  AlreadyExists - ``objective_bank_id`` is already in
                hierarchy
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_objective_bank(objective_bank_id):
        Removes a root objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :raises:  NotFound - ``objective_bank_id`` is not a root
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_objective_bank(objective_bank_id, child_id):
        Adds a child to an objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``objective_bank_id`` is already a
                parent of ``child_id``
        :raises:  NotFound - ``objective_bank_id`` or ``child_id`` not
                found
        :raises:  NullArgument - ``objective_bank_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_objective_bank(objective_bank_id, child_id):
        Removes a child from an objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :arg:    child_id (osid.id.Id): the ``Id`` of the child
        :raises:  NotFound - ``objective_bank_id`` not a parent of
                ``child_id``
        :raises:  NullArgument - ``objective_bank_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_objective_banks(objective_bank_id):
        Removes all children from an objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :raises:  NotFound - ``objective_bank_id`` not in hierarchy
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Learning Proxy Manager
----------------------

.. py:class:: LearningProxyManager(osid_managers.OsidProxyManager, LearningProfile, learning_managers.LearningProxyManager)
    The learning manager provides access to learning sessions and provides interoperability tests
        for
    various aspects of this service.


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





    .. py:method:: get_objective_lookup_session(proxy):
        :noindex:


    .. py:method:: get_objective_lookup_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_query_session(proxy):
        :noindex:


    .. py:method:: get_objective_query_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_search_session(proxy):
        :noindex:


    .. py:method:: get_objective_search_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_admin_session(proxy):
        :noindex:


    .. py:method:: get_objective_admin_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_notification_session(objective_receiver, proxy):
        :noindex:


    .. py:method:: get_objective_notification_session_for_objective_bank(objective_receiver, objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_objective_hierarchy_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_objective_hierarchy_design_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_sequencing_session(proxy):
        :noindex:


    .. py:method:: get_objective_sequencing_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_objective_bank_session(proxy):
        :noindex:


    .. py:method:: get_objective_objective_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_objective_smart_objective_bank_session(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_requisite_session(proxy):
        :noindex:


    .. py:method:: get_objective_requisite_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_requisite_assignment_session(proxy):
        :noindex:


    .. py:method:: get_objective_requisite_assignment_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_lookup_session(proxy):
        :noindex:


    .. py:method:: get_activity_lookup_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_query_session(proxy):
        :noindex:


    .. py:method:: get_activity_query_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_search_session(proxy):
        :noindex:


    .. py:method:: get_activity_search_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_admin_session(proxy):
        :noindex:


    .. py:method:: get_activity_admin_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_notification_session(activity_receiver, proxy):
        :noindex:


    .. py:method:: get_activity_notification_session_for_objective_bank(activity_receiver, objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_activity_objective_bank_session(proxy):
        :noindex:


    .. py:method:: get_activity_objective_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_activity_smart_objective_bank_session(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_lookup_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_lookup_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_query_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_query_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_search_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_search_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_admin_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_admin_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_notification_session(proficiency_receiver, proxy):
        :noindex:


    .. py:method:: get_proficiency_notification_session_for_objective_bank(proficiency_receiver, objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_proficiency_objective_bank_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_objective_bank_assignment_session(proxy):
        :noindex:


    .. py:method:: get_proficiency_smart_objective_bank_session(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_my_learning_path_session(proxy):
        :noindex:


    .. py:method:: get_my_learning_path_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_learning_path_session(proxy):
        :noindex:


    .. py:method:: get_learning_path_session_for_objective_bank(objective_bank_id, proxy):
        :noindex:


    .. py:method:: get_objective_bank_lookup_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_query_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_search_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_admin_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_notification_session(objective_bank_receiver, proxy):
        :noindex:


    .. py:method:: get_objective_bank_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_objective_bank_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_learning_batch_proxy_manager():
        :noindex:


    .. py:attribute:: learning_batch_proxy_manager
        :noindex:




Objective Objective Bank Methods
--------------------------------

    .. py:method:: can_lookup_objective_objective_bank_mappings():
        Tests if this user can perform lookups of objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_bank_view():
        A complete view of the ``Objective`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objective_ids_by_objective_bank(objective_bank_id):
        Gets the list of ``Objective``  ``Ids`` associated with an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.id.IdList) - list of related objectives
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objectives_by_objective_bank(objective_bank_id):
        Gets the list of ``Objectives`` associated with an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.learning.ObjectiveList) - list of related
                objective ``Ids``
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_ids_by_objective_banks(objective_bank_ids):
        Gets the list of ``Objective Ids`` corresponding to a list of ``ObjectiveBanks``.

        :arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        :return: (osid.id.IdList) - list of objective ``Ids``
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objectives_by_objective_banks(objective_bank_ids):
        Gets the list of ``Objectives`` corresponding to a list of ``ObjectiveBanks``.

        :arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        :return: (osid.learning.ObjectiveList) - list of objectives
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_ids_by_objective(objective_id):
        Gets the list of ``ObjectiveBank``  ``Ids`` mapped to an ``Objective``.

        :arg:    objective_id (osid.id.Id): ``Id`` of an ``Objective``
        :return: (osid.id.IdList) - list of objective bank ``Ids``
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_objective(objective_id):
        Gets the list of ``ObjectiveBanks`` mapped to an ``Objective``.

        :arg:    objective_id (osid.id.Id): ``Id`` of an ``Objective``
        :return: (osid.learning.ObjectiveBankList) - list of objective
                banks
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Objective Bank Assignment Methods
-------------------------------------------

    .. py:method:: can_assign_objectives():
        Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_objectives_to_objective_bank(objective_bank_id):
        Tests if this user can alter objective/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_objective_bank_ids(objective_bank_id):
        Gets a list of objective banks including and under the given objective bank node in which
            any objective can be assigned.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_objective_bank_ids_for_objective(objective_bank_id, objective_id):
        Gets a list of objective banks including and under the given objective bank node in which a
            specific objective can be assigned.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        :raises:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_objective_to_objective_bank(objective_id, objective_bank_id):
        Adds an existing ``Objective`` to an ``ObjectiveBank``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :raises:  AlreadyExists - ``objective_id`` already mapped to
                ``objective_bank_id``
        :raises:  NotFound - ``objective_id`` or ``objective_bank_id`` not
                found
        :raises:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_objective_from_objective_bank(objective_id, objective_bank_id):
        Removes an ``Objective`` from an ``ObjectiveBank``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :raises:  NotFound - ``objective_id`` or ``objective_bank_id`` not
                found or ``objective_id`` not mapped to
                ``objective_bank_id``
        :raises:  NullArgument - ``objective_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_proficiency_to_objective_bank(objective_id, from_objective_bank_id, to_objective_bank_id):
        Moves an ``Objective`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :arg:    from_objective_bank_id (osid.id.Id): the ``Id`` of the
                current ``ObjectiveBank``
        :arg:    to_objective_bank_id (osid.id.Id): the ``Id`` of the
                destination ``ObjectiveBank``
        :raises:  NotFound - ``objective_id, from_objective_bank_id,`` or
                ``to_objective_bank_id`` not found or ``objective_id``
                not mapped to ``from_objective_bank_id``
        :raises:  NullArgument - ``objective_id, from_objective_bank_id,``
                or ``to_objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Activity Objective Bank Methods
-------------------------------

    .. py:method:: can_lookup_activity_objective_bank_mappings():
        Tests if this user can perform lookups of activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_bank_view():
        A complete view of the ``Activity`` and ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_activity_ids_by_objective_bank(objective_bank_id):
        Gets the list of ``Activity``  ``Ids`` associated with an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.id.IdList) - list of related activity ``Ids``
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activities_by_objective_bank(objective_bank_id):
        Gets the list of ``Activities`` associated with an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.learning.ActivityList) - list of related
                activities
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activity_ids_by_objective_banks(objective_bank_ids):
        Gets the list of ``Activity Ids`` corresponding to a list of ``ObjectiveBanks``.

        :arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        :return: (osid.id.IdList) - list of activity ``Ids``
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activities_by_objective_banks(objective_bank_ids):
        Gets the list of ``Activities`` corresponding to a list of ``ObjectiveBanks``.

        :arg:    objective_bank_ids (osid.id.IdList): list of objective
                bank ``Ids``
        :return: (osid.learning.ActivityList) - list of activities
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_ids_by_activity(activity_id):
        Gets the list of ``ObjectiveBank Ids`` mapped to a ``Activity``.

        :arg:    activity_id (osid.id.Id): ``Id`` of a ``Activity``
        :return: (osid.id.IdList) - list of objective bank ``Ids``
        :raises:  NotFound - ``activity_id`` is not found
        :raises:  NullArgument - ``activity_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_activity(activity_id):
        Gets the list of ``ObjectiveBanks`` mapped to a ``Activity``.

        :arg:    activity_id (osid.id.Id): ``Id`` of a ``Activity``
        :return: (osid.learning.ObjectiveBankList) - list of objective
                bank ``Ids``
        :raises:  NotFound - ``activity_id`` is not found
        :raises:  NullArgument - ``activity_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Activity Objective Bank Assignment Methods
------------------------------------------

    .. py:method:: can_assign_activities():
        Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_activities_to_objective_bank(objective_bank_id):
        Tests if this user can alter activity/objective bank mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_objective_bank_ids(objective_bank_id):
        Gets a list of objective banks including and under the given objective bank node in which
            any activity can be assigned.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_objective_bank_ids_for_activity(objective_bank_id, activity_id):
        Gets a list of objective banks including and under the given objective bank node in which a
            specific activity can be assigned.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :return: (osid.id.IdList) - list of assignable objective bank
                ``Ids``
        :raises:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_activity_to_objective_bank(activity_id, objective_bank_id):
        Adds an existing ``Activity`` to a ``ObjectiveBank``.

        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :raises:  AlreadyExists - ``activity_id`` already mapped to
                ``objective_bank_id``
        :raises:  NotFound - ``activity_id`` or ``objective_bank_id`` not
                found
        :raises:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_activity_from_objective_bank(activity_id, objective_bank_id):
        Removes a ``Activity`` from a ``ObjectiveBank``.

        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :raises:  NotFound - ``activity_id`` or ``objective_bank_id`` not
                found or ``activity_id`` not mapped to
                ``objective_bank_id``
        :raises:  NullArgument - ``activity_id`` or ``objective_bank_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reassign_activity_to_objective_bank(activity_id, from_objective_bank_id, to_objective_bank_id):
        Moves an ``Activity`` from one ``ObjectiveBank`` to another.

        Mappings to other ``ObjectiveBanks`` are unaffected.

        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :arg:    from_objective_bank_id (osid.id.Id): the ``Id`` of the
                current ``ObjectiveBank``
        :arg:    to_objective_bank_id (osid.id.Id): the ``Id`` of the
                destination ``ObjectiveBank``
        :raises:  NotFound - ``activity_id, from_objective_bank_id,`` or
                ``to_objective_bank_id`` not found or ``activity_id``
                not mapped to ``from_objective_bank_id``
        :raises:  NullArgument - ``activity_id, from_objective_bank_id,``
                or ``to_objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Bank Lookup Methods
-----------------------------

    .. py:method:: can_lookup_objective_banks():
        Tests if this user can perform ``ObjectiveBank`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_bank_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_bank_view():
        A complete view of the ``ObjectiveBank`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objective_bank(objective_bank_id):
        Gets the ``ObjectiveBank`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``ObjectiveBank`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``ObjectiveBank`` and
        retained for compatility.

        :arg:    objective_bank_id (osid.id.Id): ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.learning.ObjectiveBank) - the objective bank
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objective_banks_by_ids(objective_bank_ids):
        Gets a ``ObjectiveBankList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the objective
        banks specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``ObjectiveBank`` objects may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :arg:    objective_bank_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``objective_bank_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_genus_type(objective_bank_genus_type):
        Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` which
            does not include objective banks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :arg:    objective_bank_genus_type (osid.type.Type): an objective
                bank genus type
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NullArgument - ``objective_bank_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_parent_genus_type(objective_bank_genus_type):
        Gets a ``ObjectiveBankList`` corresponding to the given objective bank genus ``Type`` and
            include any additional objective banks with genus types derived from the specified
            ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :arg:    objective_bank_genus_type (osid.type.Type): an objective
                bank genus type
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NullArgument - ``objective_bank_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_record_type(objective_bank_record_type):
        Gets a ``ObjectiveBankList`` containing the given objective bank record ``Type``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :arg:    objective_bank_record_type (osid.type.Type): an
                objective bank record type
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NullArgument - ``objective_bank_record_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks_by_provider(resource_id):
        Gets a ``ObjectiveBankList`` for the given provider.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.learning.ObjectiveBankList) - the returned
                ``ObjectiveBank`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_banks():
        Gets all ``ObjectiveBanks``.

        In plenary mode, the returned list contains all known objective
        banks or an error results. Otherwise, the returned list may
        contain only those objective banks that are accessible through
        this session.

        :return: (osid.learning.ObjectiveBankList) - a
                ``ObjectiveBankList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_banks




Objective Bank Admin Methods
----------------------------

    .. py:method:: can_create_objective_banks():
        Tests if this user can create ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``ObjectiveBank`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_objective_bank_with_record_types(objective_bank_record_types):
        Tests if this user can create a single ``ObjectiveBank`` using the desired record types.

        While ``LearningManager.getObjectiveBankRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``ObjectiveBank``. Providing an empty array tests if an
        ``ObjectiveBank`` can be created with no records.

        :arg:    objective_bank_record_types (osid.type.Type[]): array of
                objective bank record types
        :return: (boolean) - ``true`` if ``ObjectiveBank`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``objective_bank_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_form_for_create(objective_bank_record_types):
        Gets the objective bank form for creating new objective banks.

        A new form should be requested for each create transaction.

        :arg:    objective_bank_record_types (osid.type.Type[]): array of
                objective bank record types
        :return: (osid.learning.ObjectiveBankForm) - the objective bank
                form
        :raises:  NullArgument - ``objective_bank_record_types`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types.
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_objective_bank(objective_bank_form):
        Creates a new ``ObjectiveBank``.

        :arg:    objective_bank_form (osid.learning.ObjectiveBankForm):
                the form for this ``ObjectiveBank``
        :return: (osid.learning.ObjectiveBank) - the new
                ``ObjectiveBank``
        :raises:  IllegalState - ``objective_bank_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``objective_bank_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``objective_bank_form`` did not originate
                from ``get_objective_bank_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_objective_banks():
        Tests if this user can update ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``ObjectiveBank`` modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_form_for_update(objective_bank_id):
        Gets the objective bank form for updating an existing objective bank.

        A new objective bank form should be requested for each update
        transaction.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank``
        :return: (osid.learning.ObjectiveBankForm) - the objective bank
                form
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_objective_bank(objective_bank_form):
        Updates an existing objective bank.

        :arg:    objective_bank_form (osid.learning.ObjectiveBankForm):
                the form containing the elements to be updated
        :raises:  IllegalState - ``objective_bank_form`` already used in
                an update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``objective_bank_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``objective_bank_form did not originate
                from get_objective_bank_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_objective_banks():
        Tests if this user can delete objective banks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``ObjectiveBank`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``ObjectiveBank`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_objective_bank(objective_bank_id):
        Deletes an ``ObjectiveBank``.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of the
                ``ObjectiveBank`` to remove
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_objective_bank_aliases():
        Tests if this user can manage ``Id`` aliases for ``ObjectiveBanks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``ObjectiveBank`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_objective_bank(objective_bank_id, alias_id):
        Adds an ``Id`` to an ``ObjectiveBank`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``ObjectiveBank`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective bank, it
        is reassigned to the given objective bank ``Id``.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                ``ObjectiveBank``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Bank Hierarchy Methods
--------------------------------

    .. py:method:: get_objective_bank_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_hierarchy_id


    .. py:method:: get_objective_bank_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_hierarchy


    .. py:method:: can_access_objective_bank_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_bank_view():
        The returns from the objective bank methods may omit or translate elements based on this
            session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_bank_view():
        A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_objective_bank_ids():
        Gets the root objective bank ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root objective bank ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_objective_bank_ids


    .. py:method:: get_root_objective_banks():
        Gets the root objective banks in this objective bank hierarchy.

        :return: (osid.learning.ObjectiveBankList) - the root objective
                banks
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_objective_banks


    .. py:method:: has_parent_objective_banks(objective_bank_id):
        Tests if the ``ObjectiveBank`` has any parents.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if the objective bank has parents,
                ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_objective_bank(id_, objective_bank_id):
        Tests if an ``Id`` is a direct parent of an objective bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``objective_bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_objective_bank_ids(objective_bank_id):
        Gets the parent ``Ids`` of the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (osid.id.IdList) - the parent ``Ids`` of the objective
                bank
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_objective_banks(objective_bank_id):
        Gets the parents of the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (osid.learning.ObjectiveBankList) - the parents of the
                objective bank
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_objective_bank(id_, objective_bank_id):
        Tests if an ``Id`` is an ancestor of an objective bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``objective_bank_id,`` ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_objective_banks(objective_bank_id):
        Tests if an objective bank has any children.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if the ``objective_bank_id`` has
                children, ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_objective_bank(id_, objective_bank_id):
        Tests if an objective bank is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``objective_bank_id,``  ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_objective_bank_ids(objective_bank_id):
        Gets the child ``Ids`` of the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the objective bank
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_objective_banks(objective_bank_id):
        Gets the children of the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        :return: (osid.learning.ObjectiveBankList) - the children of the
                objective bank
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_objective_bank(id_, objective_bank_id):
        Tests if an ``Id`` is a descendant of an objective bank.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``objective_bank_id,`` ``false`` otherwise
        :raises:  NotFound - ``objective_bank_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_bank_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_objective_bank_node_ids(objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a catalog node
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_bank_nodes(objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.learning.ObjectiveBankNode) - an objective bank
                node
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Bank Hierarchy Design Methods
---------------------------------------

    .. py:method:: get_objective_bank_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_hierarchy_id


    .. py:method:: get_objective_bank_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_hierarchy


    .. py:method:: can_modify_objective_bank_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_objective_bank(objective_bank_id):
        Adds a root objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :raises:  AlreadyExists - ``objective_bank_id`` is already in
                hierarchy
        :raises:  NotFound - ``objective_bank_id`` not found
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_objective_bank(objective_bank_id):
        Removes a root objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :raises:  NotFound - ``objective_bank_id`` is not a root
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_objective_bank(objective_bank_id, child_id):
        Adds a child to an objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``objective_bank_id`` is already a
                parent of ``child_id``
        :raises:  NotFound - ``objective_bank_id`` or ``child_id`` not
                found
        :raises:  NullArgument - ``objective_bank_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_objective_bank(objective_bank_id, child_id):
        Removes a child from an objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :arg:    child_id (osid.id.Id): the ``Id`` of the child
        :raises:  NotFound - ``objective_bank_id`` not a parent of
                ``child_id``
        :raises:  NullArgument - ``objective_bank_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_objective_banks(objective_bank_id):
        Removes all children from an objective bank.

        :arg:    objective_bank_id (osid.id.Id): the ``Id`` of an
                objective bank
        :raises:  NotFound - ``objective_bank_id`` not in hierarchy
        :raises:  NullArgument - ``objective_bank_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






