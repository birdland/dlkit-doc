

Sessions
========


Objective Lookup Session
------------------------

.. py:class:: ObjectiveLookupSession(abc_learning_sessions.ObjectiveLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Objective`` s.

    .. py:method:: get_objective_bank_id():
        :noindex:


    .. py:attribute:: objective_bank_id
        :noindex:


    .. py:method:: get_objective_bank():
        :noindex:


    .. py:attribute:: objective_bank
        :noindex:


    .. py:method:: can_lookup_objectives():
        :noindex:


    .. py:method:: use_comparative_objective_view():
        :noindex:


    .. py:method:: use_plenary_objective_view():
        :noindex:


    .. py:method:: use_federated_objective_bank_view():
        :noindex:


    .. py:method:: use_isolated_objective_bank_view():
        :noindex:


    .. py:method:: get_objective(objective_id):
        :noindex:


    .. py:method:: get_objectives_by_ids(objective_ids):
        :noindex:


    .. py:method:: get_objectives_by_genus_type(objective_genus_type):
        :noindex:


    .. py:method:: get_objectives_by_parent_genus_type(objective_genus_type):
        :noindex:


    .. py:method:: get_objectives_by_record_type(objective_record_type):
        :noindex:


    .. py:method:: get_objectives():
        :noindex:


    .. py:attribute:: objectives
        :noindex:


Objective Query Session
-----------------------

.. py:class:: ObjectiveQuerySession(abc_learning_sessions.ObjectiveQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching ``Objective`` objects.


    The search query is constructed using the ``ObjectiveQuery``. The
    objective record ``Type`` also specifies the record for the
    objective query.




    This session defines views that offer differing behaviors for
    searching.




      * federated objective bank view: searches include objectives in
        objective banks of which this objective bank is a ancestor in
        the objective bank hierarchy
      * isolated objective bank view: searches are restricted to
        objectives in this objective bank








    Objectives may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``ObjectiveQuery``.





    .. py:method:: get_objective_bank_id():
        :noindex:


    .. py:attribute:: objective_bank_id
        :noindex:


    .. py:method:: get_objective_bank():
        :noindex:


    .. py:attribute:: objective_bank
        :noindex:


    .. py:method:: can_search_objectives():
        :noindex:


    .. py:method:: use_federated_objective_bank_view():
        :noindex:


    .. py:method:: use_isolated_objective_bank_view():
        :noindex:


    .. py:method:: get_objective_query():
        :noindex:


    .. py:attribute:: objective_query
        :noindex:


    .. py:method:: get_objectives_by_query(objective_query):
        :noindex:


Objective Admin Session
-----------------------

.. py:class:: ObjectiveAdminSession(abc_learning_sessions.ObjectiveAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Objectives``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create an
    ``Objective,`` a ``ObjectiveForm`` is requested using
    ``get_objective_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``ObjectiveForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``ObjectiveForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ObjectiveForm``
    corresponds to an attempted transaction.




    For updates, ``ObjectiveForms`` are requested to the ``Objective``
    ``Id`` that is to be updated using ``getObjectiveFormForUpdate()``.
    Similarly, the ``ObjectiveForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``ObjectiveForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``Objectives``. To unmap an
    ``Objective`` from the current ``ObjectiveBank,`` the
    ``ObjectiveObjectiveBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``Objective`` itself thus
    removing it from all known ``ObjectiveBank`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_objective_bank_id():
        :noindex:


    .. py:attribute:: objective_bank_id
        :noindex:


    .. py:method:: get_objective_bank():
        :noindex:


    .. py:attribute:: objective_bank
        :noindex:


    .. py:method:: can_create_objectives():
        :noindex:


    .. py:method:: can_create_objective_with_record_types(objective_record_types):
        :noindex:


    .. py:method:: get_objective_form_for_create(objective_record_types):
        :noindex:


    .. py:method:: create_objective(objective_form):
        :noindex:


    .. py:method:: can_update_objectives():
        :noindex:


    .. py:method:: get_objective_form_for_update(objective_id):
        :noindex:


    .. py:method:: update_objective(objective_form):
        :noindex:


    .. py:method:: can_delete_objectives():
        :noindex:


    .. py:method:: delete_objective(objective_id):
        :noindex:


    .. py:method:: can_manage_objective_aliases():
        :noindex:


    .. py:method:: alias_objective(objective_id, alias_id):
        :noindex:


Objective Hierarchy Session
---------------------------

.. py:class:: ObjectiveHierarchySession(abc_learning_sessions.ObjectiveHierarchySession, osid_sessions.OsidSession)
    This session defines methods for traversing a hierarchy of ``Objective`` objects.


    Each node in the hierarchy is a unique ``Objective that contains its
    child objectives``. The hierarchy may be traversed recursively to
    establish the tree structure through ``get_parent_objectives()`` and
    ``getChildObjectives()``. To relate these ``Ids`` to another OSID,
    ``get_objective_nodes()`` can be used for retrievals that can be
    used for bulk lookups in other OSIDs. Any ``Objective`` available in
    the Learning OSID is known to this hierarchy but does not appear in
    the hierarchy traversal until added as a root node or a child of
    another node.




    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_objectives()`` or ``get_child_objectives()``
    in lieu of a ``PermissionDenied`` error that may disrupt the
    traversal through authorized pathways.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: objective elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition





    .. py:method:: get_objective_hierarchy_id():
        :noindex:


    .. py:attribute:: objective_hierarchy_id
        :noindex:


    .. py:method:: get_objective_hierarchy():
        :noindex:


    .. py:attribute:: objective_hierarchy
        :noindex:


    .. py:method:: can_access_objective_hierarchy():
        :noindex:


    .. py:method:: use_comparative_objective_view():
        :noindex:


    .. py:method:: use_plenary_objective_view():
        :noindex:


    .. py:method:: get_root_objective_ids():
        :noindex:


    .. py:attribute:: root_objective_ids
        :noindex:


    .. py:method:: get_root_objectives():
        :noindex:


    .. py:attribute:: root_objectives
        :noindex:


    .. py:method:: has_parent_objectives(objective_id):
        :noindex:


    .. py:method:: is_parent_of_objective(id_, objective_id):
        :noindex:


    .. py:method:: get_parent_objective_ids(objective_id):
        :noindex:


    .. py:method:: get_parent_objectives(objective_id):
        :noindex:


    .. py:method:: is_ancestor_of_objective(id_, objective_id):
        :noindex:


    .. py:method:: has_child_objectives(objective_id):
        :noindex:


    .. py:method:: is_child_of_objective(id_, objective_id):
        :noindex:


    .. py:method:: get_child_objective_ids(objective_id):
        :noindex:


    .. py:method:: get_child_objectives(objective_id):
        :noindex:


    .. py:method:: is_descendant_of_objective(id_, objective_id):
        :noindex:


    .. py:method:: get_objective_node_ids(objective_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


    .. py:method:: get_objective_nodes(objective_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


Objective Hierarchy Design Session
----------------------------------

.. py:class:: ObjectiveHierarchyDesignSession(abc_learning_sessions.ObjectiveHierarchyDesignSession, osid_sessions.OsidSession)
    This session defines methods for managing a hierarchy of ``Objective`` objects.


    Each node in the hierarchy is a unique ``Objective``.





    .. py:method:: get_objective_hierarchy_id():
        :noindex:


    .. py:attribute:: objective_hierarchy_id
        :noindex:


    .. py:method:: get_objective_hierarchy():
        :noindex:


    .. py:attribute:: objective_hierarchy
        :noindex:


    .. py:method:: can_modify_objective_hierarchy():
        :noindex:


    .. py:method:: add_root_objective(objective_id):
        :noindex:


    .. py:method:: remove_root_objective(objective_id):
        :noindex:


    .. py:method:: add_child_objective(objective_id, child_id):
        :noindex:


    .. py:method:: remove_child_objective(objective_id, child_id):
        :noindex:


    .. py:method:: remove_child_objectives(objective_id):
        :noindex:


Objective Sequencing Session
----------------------------

.. py:class:: ObjectiveSequencingSession(abc_learning_sessions.ObjectiveSequencingSession, osid_sessions.OsidSession)
    This session provides methods to sequence the objectives in the objective hierarchy.

    .. py:method:: get_objective_hierarchy_id():
        :noindex:


    .. py:attribute:: objective_hierarchy_id
        :noindex:


    .. py:method:: get_objective_hierarchy():
        :noindex:


    .. py:attribute:: objective_hierarchy
        :noindex:


    .. py:method:: can_sequence_objectives():
        :noindex:


    .. py:method:: move_objective_ahead(parent_objective_id, reference_objective_id, objective_id):
        :noindex:


    .. py:method:: move_objective_behind(parent_objective_id, reference_objective_id, objective_id):
        :noindex:


    .. py:method:: sequence_objectives(parent_objective_id, objective_ids):
        :noindex:


Objective Objective Bank Session
--------------------------------

.. py:class:: ObjectiveObjectiveBankSession(abc_learning_sessions.ObjectiveObjectiveBankSession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``Objective`` to ``ObjectiveBank`` mappings.


    An ``Objective`` may appear in multiple ``ObjectiveBanks``. Each
    ``ObjectiveBank`` may have its own authorizations governing who is
    allowed to look at it.




    This lookup session defines two views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: can_lookup_objective_objective_bank_mappings():
        :noindex:


    .. py:method:: use_comparative_objective_bank_view():
        :noindex:


    .. py:method:: use_plenary_objective_bank_view():
        :noindex:


    .. py:method:: get_objective_ids_by_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objectives_by_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_ids_by_objective_banks(objective_bank_ids):
        :noindex:


    .. py:method:: get_objectives_by_objective_banks(objective_bank_ids):
        :noindex:


    .. py:method:: get_objective_bank_ids_by_objective(objective_id):
        :noindex:


    .. py:method:: get_objective_banks_by_objective(objective_id):
        :noindex:


Objective Objective Bank Assignment Session
-------------------------------------------

.. py:class:: ObjectiveObjectiveBankAssignmentSession(abc_learning_sessions.ObjectiveObjectiveBankAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``Objectives`` to ``ObjectiveBanks``.


    An ``Objective`` may map to multiple ``ObjectiveBanks`` and removing
    the last reference to an ``Objective`` is the equivalent of deleting
    it. Each ``ObjectiveBank`` may have its own authorizations governing
    who is allowed to operate on it.




    Moving or adding a reference of an ``Objective`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).





    .. py:method:: can_assign_objectives():
        :noindex:


    .. py:method:: can_assign_objectives_to_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_assignable_objective_bank_ids(objective_bank_id):
        :noindex:


    .. py:method:: get_assignable_objective_bank_ids_for_objective(objective_bank_id, objective_id):
        :noindex:


    .. py:method:: assign_objective_to_objective_bank(objective_id, objective_bank_id):
        :noindex:


    .. py:method:: unassign_objective_from_objective_bank(objective_id, objective_bank_id):
        :noindex:


    .. py:method:: reassign_proficiency_to_objective_bank(objective_id, from_objective_bank_id, to_objective_bank_id):
        :noindex:


Objective Requisite Session
---------------------------

.. py:class:: ObjectiveRequisiteSession(abc_learning_sessions.ObjectiveRequisiteSession, osid_sessions.OsidSession)
    This session provides methods for retrieving objective requisites.


    A requisite is a set of ``Objectives`` that should be achieved
    before another ``Objective`` is attempted.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * isolated objective bank view: All objective methods in this
        session operate, retrieve and pertain to objectives defined
        explicitly in the current objective bank. Using an isolated view
        is useful for managing objectives with the
        ``ObjectiveAdminSession.``
      * federated objective bank view: All objective methods in this
        session operate, retrieve and pertain to all objectives defined
        in this objective bank and any other objective banks implicitly
        available in this objective bank through objective bank
        inheritence.








    Objectives may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Objective``.





    .. py:method:: get_objective_bank_id():
        :noindex:


    .. py:attribute:: objective_bank_id
        :noindex:


    .. py:method:: get_objective_bank():
        :noindex:


    .. py:attribute:: objective_bank
        :noindex:


    .. py:method:: can_lookup_objective_prerequisites():
        :noindex:


    .. py:method:: use_comparative_objective_view():
        :noindex:


    .. py:method:: use_plenary_objective_view():
        :noindex:


    .. py:method:: use_federated_objective_bank_view():
        :noindex:


    .. py:method:: use_isolated_objective_bank_view():
        :noindex:


    .. py:method:: get_requisite_objectives(objective_id):
        :noindex:


    .. py:method:: get_all_requisite_objectives(objective_id):
        :noindex:


    .. py:method:: get_dependent_objectives(objective_id):
        :noindex:


    .. py:method:: is_objective_required(objective_id, required_objective_id):
        :noindex:


    .. py:method:: get_equivalent_objectives(objective_id):
        :noindex:


Objective Requisite Assignment Session
--------------------------------------

.. py:class:: ObjectiveRequisiteAssignmentSession(abc_learning_sessions.ObjectiveRequisiteAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to manage requisites.


    Each ``ObjectiveBank`` may have its own authorizations governing who
    is allowed to operate on it.




    Moving or adding a reference of an ``Objective`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).





    .. py:method:: get_objective_bank_id():
        :noindex:


    .. py:attribute:: objective_bank_id
        :noindex:


    .. py:method:: get_objective_bank():
        :noindex:


    .. py:attribute:: objective_bank
        :noindex:


    .. py:method:: can_assign_requisites():
        :noindex:


    .. py:method:: assign_objective_requisite(objective_id, requisite_objective_id):
        :noindex:


    .. py:method:: unassign_objective_requisite(objective_id, requisite_objective_id):
        :noindex:


    .. py:method:: assign_equivalent_objective(objective_id, equivalent_objective_id):
        :noindex:


    .. py:method:: unassign_equivalent_objective(objective_id, equivalent_objective_id):
        :noindex:


Activity Lookup Session
-----------------------

.. py:class:: ActivityLookupSession(abc_learning_sessions.ActivityLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Activity`` objects.


    The ``Activity`` represents something to perform in order to achieve
    a learning objective.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * isolated objective bank view: All activity methods in this
        session operate, retrieve and pertain to activities defined
        explicitly in the current objective bank. Using an isolated view
        is useful for managing activities with the
        ``ActivityAdminSession.``
      * federated objective bank view: All activity methods in this
        session operate, retrieve and pertain to all activities defined
        in this objective bank and any other objective banks implicitly
        available in this objective bank through objective bank
        inheritence.








    Activities may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Activity``.





    .. py:method:: get_objective_bank_id():
        :noindex:


    .. py:attribute:: objective_bank_id
        :noindex:


    .. py:method:: get_objective_bank():
        :noindex:


    .. py:attribute:: objective_bank
        :noindex:


    .. py:method:: can_lookup_activities():
        :noindex:


    .. py:method:: use_comparative_activity_view():
        :noindex:


    .. py:method:: use_plenary_activity_view():
        :noindex:


    .. py:method:: use_federated_objective_bank_view():
        :noindex:


    .. py:method:: use_isolated_objective_bank_view():
        :noindex:


    .. py:method:: get_activity(activity_id):
        :noindex:


    .. py:method:: get_activities_by_ids(activity_ids):
        :noindex:


    .. py:method:: get_activities_by_genus_type(activity_genus_type):
        :noindex:


    .. py:method:: get_activities_by_parent_genus_type(activity_genus_type):
        :noindex:


    .. py:method:: get_activities_by_record_type(activity_record_type):
        :noindex:


    .. py:method:: get_activities_for_objective(objective_id):
        :noindex:


    .. py:method:: get_activities_for_objectives(objective_ids):
        :noindex:


    .. py:method:: get_activities_by_asset(asset_id):
        :noindex:


    .. py:method:: get_activities_by_assets(asset_ids):
        :noindex:


    .. py:method:: get_activities():
        :noindex:


    .. py:attribute:: activities
        :noindex:


Activity Admin Session
----------------------

.. py:class:: ActivityAdminSession(abc_learning_sessions.ActivityAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Activities``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create an
    ``Activity,`` an ``ActivityForm`` is requested using
    ``get_activity_form_for_create()`` specifying the desired objective
    and record ``Types`` or none if no record ``Types`` are needed. The
    returned ``ActivityForm`` will indicate that it is to be used with a
    create operation and can be used to examine metdata or validate data
    prior to creation. Once the ``ActivityForm`` is submiited to a
    create operation, it cannot be reused with another create operation
    unless the first operation was unsuccessful. Each ``ActivityForm``
    corresponds to an attempted transaction.




    For updates, ``ActivityForms`` are requested to the ``Activity``
    ``Id`` that is to be updated using ``getActivityFormForUpdate()``.
    Similarly, the ``ActivityForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``ActivityForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``Activities``. To unmap an
    ``Activity`` from the current ``ObjectiveBank,`` the
    ``ActivityObjectiveBankAssignmentSession`` should be used. These
    delete operations attempt to remove the ``Activity`` itself thus
    removing it from all known ``ObjectiveBank`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_objective_bank_id():
        :noindex:


    .. py:attribute:: objective_bank_id
        :noindex:


    .. py:method:: get_objective_bank():
        :noindex:


    .. py:attribute:: objective_bank
        :noindex:


    .. py:method:: can_create_activities():
        :noindex:


    .. py:method:: can_create_activity_with_record_types(activity_record_types):
        :noindex:


    .. py:method:: get_activity_form_for_create(objective_id, activity_record_types):
        :noindex:


    .. py:method:: create_activity(activity_form):
        :noindex:


    .. py:method:: can_update_activities():
        :noindex:


    .. py:method:: get_activity_form_for_update(activity_id):
        :noindex:


    .. py:method:: update_activity(activity_form):
        :noindex:


    .. py:method:: can_delete_activities():
        :noindex:


    .. py:method:: delete_activity(activity_id):
        :noindex:


    .. py:method:: can_manage_activity_aliases():
        :noindex:


    .. py:method:: alias_activity(activity_id, alias_id):
        :noindex:


Activity Objective Bank Session
-------------------------------

.. py:class:: ActivityObjectiveBankSession(abc_learning_sessions.ActivityObjectiveBankSession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``Activity`` to ``ObjectiveBank`` mappings.


    An ``Activity`` may appear in multiple ``ObjectiveBanks``. Each
    ``ObjectiveBank`` may have its own authorizations governing who is
    allowed to look at it.




    This lookup session defines two views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: can_lookup_activity_objective_bank_mappings():
        :noindex:


    .. py:method:: use_comparative_objective_bank_view():
        :noindex:


    .. py:method:: use_plenary_objective_bank_view():
        :noindex:


    .. py:method:: get_activity_ids_by_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activities_by_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_activity_ids_by_objective_banks(objective_bank_ids):
        :noindex:


    .. py:method:: get_activities_by_objective_banks(objective_bank_ids):
        :noindex:


    .. py:method:: get_objective_bank_ids_by_activity(activity_id):
        :noindex:


    .. py:method:: get_objective_banks_by_activity(activity_id):
        :noindex:


Activity Objective Bank Assignment Session
------------------------------------------

.. py:class:: ActivityObjectiveBankAssignmentSession(abc_learning_sessions.ActivityObjectiveBankAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``Activities`` to ``ObjectiveBanks``.


    An ``Activity`` may map to multiple ``ObjectiveBanks`` and removing
    the last reference to a ``Activity`` is the equivalent of deleting
    it. Each ``ObjectiveBank`` may have its own authorizations governing
    who is allowed to operate on it.




    Moving or adding a reference of an ``Activity`` to another
    ``ObjectiveBank`` is not a copy operation (eg: does not change its
    ``Id`` ).





    .. py:method:: can_assign_activities():
        :noindex:


    .. py:method:: can_assign_activities_to_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_assignable_objective_bank_ids(objective_bank_id):
        :noindex:


    .. py:method:: get_assignable_objective_bank_ids_for_activity(objective_bank_id, activity_id):
        :noindex:


    .. py:method:: assign_activity_to_objective_bank(activity_id, objective_bank_id):
        :noindex:


    .. py:method:: unassign_activity_from_objective_bank(activity_id, objective_bank_id):
        :noindex:


    .. py:method:: reassign_activity_to_objective_bank(activity_id, from_objective_bank_id, to_objective_bank_id):
        :noindex:


Objective Bank Lookup Session
-----------------------------

.. py:class:: ObjectiveBankLookupSession(abc_learning_sessions.ObjectiveBankLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``ObjectiveBank`` objects.


    The ``ObjectiveBank`` represents a collection of ``Objectives
    Activities`` , and ``Proficiencies``.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition








    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``ObjectiveBanks`` it can access, without breaking
    execution. However, an administrative application may require all
    ``ObjectiveBank`` elements to be available.




    ``ObjectiveBanks`` may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``ObjectiveBank``.





    .. py:method:: can_lookup_objective_banks():
        :noindex:


    .. py:method:: use_comparative_objective_bank_view():
        :noindex:


    .. py:method:: use_plenary_objective_bank_view():
        :noindex:


    .. py:method:: get_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: get_objective_banks_by_ids(objective_bank_ids):
        :noindex:


    .. py:method:: get_objective_banks_by_genus_type(objective_bank_genus_type):
        :noindex:


    .. py:method:: get_objective_banks_by_parent_genus_type(objective_bank_genus_type):
        :noindex:


    .. py:method:: get_objective_banks_by_record_type(objective_bank_record_type):
        :noindex:


    .. py:method:: get_objective_banks_by_provider(resource_id):
        :noindex:


    .. py:method:: get_objective_banks():
        :noindex:


    .. py:attribute:: objective_banks
        :noindex:


Objective Bank Admin Session
----------------------------

.. py:class:: ObjectiveBankAdminSession(abc_learning_sessions.ObjectiveBankAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``ObjectiveBanks``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create an
    ``ObjectiveBank,`` an ``ObjectiveBankForm`` is requested using
    ``get_objective_bank_form_for_create()`` specifying the desired
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``ObjectiveBankForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``ObjectiveBankForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``ObjectiveBankForm`` corresponds to an attempted transaction.




    For updates, ``ObjectiveBankForms`` are requested to the
    ``ObjectiveBank``  ``Id`` that is to be updated using
    ``getObjectiveBankFormForUpdate()``. Similarly, the
    ``ObjectiveBankForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``ObjectiveBankForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``ObjectiveBanks``. It is safer to
    remove all mappings to the ``ObjectiveBank`` catalogs before
    deletion.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: can_create_objective_banks():
        :noindex:


    .. py:method:: can_create_objective_bank_with_record_types(objective_bank_record_types):
        :noindex:


    .. py:method:: get_objective_bank_form_for_create(objective_bank_record_types):
        :noindex:


    .. py:method:: create_objective_bank(objective_bank_form):
        :noindex:


    .. py:method:: can_update_objective_banks():
        :noindex:


    .. py:method:: get_objective_bank_form_for_update(objective_bank_id):
        :noindex:


    .. py:method:: update_objective_bank(objective_bank_form):
        :noindex:


    .. py:method:: can_delete_objective_banks():
        :noindex:


    .. py:method:: delete_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: can_manage_objective_bank_aliases():
        :noindex:


    .. py:method:: alias_objective_bank(objective_bank_id, alias_id):
        :noindex:


Objective Bank Hierarchy Session
--------------------------------

.. py:class:: ObjectiveBankHierarchySession(abc_learning_sessions.ObjectiveBankHierarchySession, osid_sessions.OsidSession)
    This session defines methods for traversing a hierarchy of ``ObjectiveBank`` objects.


    Each node in the hierarchy is a unique ``ObjectiveBank``. The
    hierarchy may be traversed recursively to establish the tree
    structure through ``get_parent_objective_banks()`` and
    ``getChildObjectiveBanks()``. To relate these ``Ids`` to another
    OSID, ``get_objective_bank_nodes()`` can be used for retrievals that
    can be used for bulk lookups in other OSIDs. Any ``ObjectiveBank``
    available in the ObjectiveBanking OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.




    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_objective_banks()`` or
    ``get_child_objective_banks()`` in lieu of a ``PermissionDenied``
    error that may disrupt the traversal through authorized pathways.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: objective bank elements may be silently
        omitted or re-ordered
      * plenary view: provides a complete set or is an error condition





    .. py:method:: get_objective_bank_hierarchy_id():
        :noindex:


    .. py:attribute:: objective_bank_hierarchy_id
        :noindex:


    .. py:method:: get_objective_bank_hierarchy():
        :noindex:


    .. py:attribute:: objective_bank_hierarchy
        :noindex:


    .. py:method:: can_access_objective_bank_hierarchy():
        :noindex:


    .. py:method:: use_comparative_objective_bank_view():
        :noindex:


    .. py:method:: use_plenary_objective_bank_view():
        :noindex:


    .. py:method:: get_root_objective_bank_ids():
        :noindex:


    .. py:attribute:: root_objective_bank_ids
        :noindex:


    .. py:method:: get_root_objective_banks():
        :noindex:


    .. py:attribute:: root_objective_banks
        :noindex:


    .. py:method:: has_parent_objective_banks(objective_bank_id):
        :noindex:


    .. py:method:: is_parent_of_objective_bank(id_, objective_bank_id):
        :noindex:


    .. py:method:: get_parent_objective_bank_ids(objective_bank_id):
        :noindex:


    .. py:method:: get_parent_objective_banks(objective_bank_id):
        :noindex:


    .. py:method:: is_ancestor_of_objective_bank(id_, objective_bank_id):
        :noindex:


    .. py:method:: has_child_objective_banks(objective_bank_id):
        :noindex:


    .. py:method:: is_child_of_objective_bank(id_, objective_bank_id):
        :noindex:


    .. py:method:: get_child_objective_bank_ids(objective_bank_id):
        :noindex:


    .. py:method:: get_child_objective_banks(objective_bank_id):
        :noindex:


    .. py:method:: is_descendant_of_objective_bank(id_, objective_bank_id):
        :noindex:


    .. py:method:: get_objective_bank_node_ids(objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


    .. py:method:: get_objective_bank_nodes(objective_bank_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


Objective Bank Hierarchy Design Session
---------------------------------------

.. py:class:: ObjectiveBankHierarchyDesignSession(abc_learning_sessions.ObjectiveBankHierarchyDesignSession, osid_sessions.OsidSession)
    This session defines methods for managing a hierarchy of ``ObjectiveBank`` objects.


    Each node in the hierarchy is a unique ``ObjectiveBank``.





    .. py:method:: get_objective_bank_hierarchy_id():
        :noindex:


    .. py:attribute:: objective_bank_hierarchy_id
        :noindex:


    .. py:method:: get_objective_bank_hierarchy():
        :noindex:


    .. py:attribute:: objective_bank_hierarchy
        :noindex:


    .. py:method:: can_modify_objective_bank_hierarchy():
        :noindex:


    .. py:method:: add_root_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: remove_root_objective_bank(objective_bank_id):
        :noindex:


    .. py:method:: add_child_objective_bank(objective_bank_id, child_id):
        :noindex:


    .. py:method:: remove_child_objective_bank(objective_bank_id, child_id):
        :noindex:


    .. py:method:: remove_child_objective_banks(objective_bank_id):
        :noindex:


