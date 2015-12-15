

Service Catalog
===============


Objective Bank
--------------

.. py:class:: ObjectiveBank(abc_learning_objects.ObjectiveBank, osid_objects.OsidCatalog)
    an objective bank defines a collection of objectives.

    .. py:method:: get_objective_bank_record(objective_bank_record_type):
        :noindex:




Objective Lookup Methods
------------------------

    .. py:method:: get_objective_bank_id():
        Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_id


    .. py:method:: get_objective_bank():
        Gets the ``ObjectiveBank`` associated with this session.

        :return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank


    .. py:method:: can_lookup_objectives():
        Tests if this user can perform ``Objective`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_view():
        A complete view of the ``Objective`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_objective_bank_view():
        Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_objective_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objective(objective_id):
        Gets the ``Objective`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Objective`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Objective`` and retained
        for compatibility.

        :arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        :return: (osid.learning.Objective) - the objective
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objectives_by_ids(objective_ids):
        Gets an ``ObjectiveList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        objectives specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Objectives`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    objective_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``objective_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objectives_by_genus_type(objective_genus_type):
        Gets an ``ObjectiveList`` corresponding to the given objective genus ``Type`` which does not
            include objectives of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :arg:    objective_genus_type (osid.type.Type): an objective
                genus type
        :return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        :raises:  NullArgument - ``objective_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objectives_by_parent_genus_type(objective_genus_type):
        Gets an ``ObjectiveList`` corresponding to the given objective genus ``Type`` and include
            any additional objective with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session

        :arg:    objective_genus_type (osid.type.Type): an objective
                genus type
        :return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        :raises:  NullArgument - ``objective_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objectives_by_record_type(objective_record_type):
        Gets an ``ObjectiveList`` containing the given objective record ``Type``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :arg:    objective_record_type (osid.type.Type): an objective
                record type
        :return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        :raises:  NullArgument - ``objective_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objectives():
        Gets all ``Objectives``.

        In plenary mode, the returned list contains all known objectives
        or an error results. Otherwise, the returned list may contain
        only those objectives that are accessible through this session.

        :return: (osid.learning.ObjectiveList) - an ``ObjectiveList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objectives




Objective Query Methods
-----------------------

    .. py:method:: get_objective_bank_id():
        Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_id


    .. py:method:: get_objective_bank():
        Gets the ``ObjectiveBank`` associated with this session.

        :return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank


    .. py:method:: can_search_objectives():
        Tests if this user can perform ``Objectives`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_objective_bank_view():
        Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_objective_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_objective_query():
        Gets an objective query.

        :return: (osid.learning.ObjectiveQuery) - the objective query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_query


    .. py:method:: get_objectives_by_query(objective_query):
        Gets a list of ``Objectives`` matching the given objective query.

        :arg:    objective_query (osid.learning.ObjectiveQuery): the
                objective query
        :return: (osid.learning.ObjectiveList) - the returned
                ``ObjectiveList``
        :raises:  NullArgument - ``objective_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``objective_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Objective Admin Methods
-----------------------

    .. py:method:: get_objective_bank_id():
        Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_id


    .. py:method:: get_objective_bank():
        Gets the ``ObjectiveBank`` associated with this session.

        :return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank


    .. py:method:: can_create_objectives():
        Tests if this user can create ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an Objective
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Objective`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_objective_with_record_types(objective_record_types):
        Tests if this user can create a single ``Objective`` using the desired record types.

        While ``LearningManager.getObjectiveRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Objective``.
        Providing an empty array tests if an ``Objective`` can be
        created with no records.

        :arg:    objective_record_types (osid.type.Type[]): array of
                objective record types
        :return: (boolean) - ``true`` if ``Objective`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``objective_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_form_for_create(objective_record_types):
        Gets the objective form for creating new objectives.

        A new form should be requested for each create transaction.

        :arg:    objective_record_types (osid.type.Type[]): array of
                objective record types
        :return: (osid.learning.ObjectiveForm) - the objective form
        :raises:  NullArgument - ``objective_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_objective(objective_form):
        Creates a new ``Objective``.

        :arg:    objective_form (osid.learning.ObjectiveForm): the form
                for this ``Objective``
        :return: (osid.learning.Objective) - the new ``Objective``
        :raises:  IllegalState - ``objective_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``objective_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``objective_form`` did not originate from
                ``get_objective_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_objectives():
        Tests if this user can update ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Objective`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if objective modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_form_for_update(objective_id):
        Gets the objective form for updating an existing objective.

        A new objective form should be requested for each update
        transaction.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :return: (osid.learning.ObjectiveForm) - the objective form
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_objective(objective_form):
        Updates an existing objective.

        :arg:    objective_form (osid.learning.ObjectiveForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``objective_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``objective_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``objective_form`` did not originate from
                ``get_objective_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_objectives():
        Tests if this user can delete ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Objective`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Objective`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_objective(objective_id):
        Deletes the ``Objective`` identified by the given ``Id``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective`` to delete
        :raises:  NotFound - an ``Objective`` was not found identified by
                the given ``Id``
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_objective_aliases():
        Tests if this user can manage ``Id`` aliases for ``Objectives``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Objective`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_objective(objective_id, alias_id):
        Adds an ``Id`` to an ``Objective`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Objective`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another objective, it is
        reassigned to the given objective ``Id``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an
                ``Objective``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Hierarchy Methods
---------------------------

    .. py:method:: get_objective_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_hierarchy_id


    .. py:method:: get_objective_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_hierarchy


    .. py:method:: can_access_objective_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_view():
        The returns from the objective methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_view():
        A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_objective_ids():
        Gets the root objective ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root objective ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_objective_ids


    .. py:method:: get_root_objectives():
        Gets the root objective in this objective hierarchy.

        :return: (osid.learning.ObjectiveList) - the root objective
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_objectives


    .. py:method:: has_parent_objectives(objective_id):
        Tests if the ``Objective`` has any parents.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :return: (boolean) - ``true`` if the objective has parents,
                ``false`` otherwise
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_objective(id_, objective_id):
        Tests if an ``Id`` is a direct parent of an objective.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``objective_id,``  ``false`` otherwise
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_objective_ids(objective_id):
        Gets the parent ``Ids`` of the given objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :return: (osid.id.IdList) - the parent ``Ids`` of the objective
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_objectives(objective_id):
        Gets the parents of the given objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :return: (osid.learning.ObjectiveList) - the parents of the
                objective
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_objective(id_, objective_id):
        Tests if an ``Id`` is an ancestor of an objective.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``objective_id,``  ``false`` otherwise
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_objectives(objective_id):
        Tests if an objective has any children.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :return: (boolean) - ``true`` if the ``objective_id`` has
                children, ``false`` otherwise
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_objective(id_, objective_id):
        Tests if an objective is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``objective_id,``  ``false`` otherwise
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_objective_ids(objective_id):
        Gets the child ``Ids`` of the given objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the objective
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_objectives(objective_id):
        Gets the children of the given objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` to query
        :return: (osid.learning.ObjectiveList) - the children of the
                objective
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_objective(id_, objective_id):
        Tests if an ``Id`` is a descendant of an objective.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``objective_id,`` ``false`` otherwise
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``id`` or ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_objective_node_ids(objective_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` to query
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
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_objective_nodes(objective_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.learning.ObjectiveNode) - an objective node
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Hierarchy Design Methods
----------------------------------

    .. py:method:: get_objective_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_hierarchy_id


    .. py:method:: get_objective_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_hierarchy


    .. py:method:: can_modify_objective_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_objective(objective_id):
        Adds a root objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :raises:  AlreadyExists - ``objective_id`` is already in hierarchy
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_objective(objective_id):
        Removes a root objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_objective(objective_id, child_id):
        Adds a child to an objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``objective_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``objective_id`` or ``child_id`` not found
        :raises:  NullArgument - ``objective_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_objective(objective_id, child_id):
        Removes a child from an objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``objective_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``objective_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_objectives(objective_id):
        Removes all children from an objective.

        :arg:    objective_id (osid.id.Id): the ``Id`` of an objective
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Sequencing Methods
----------------------------

    .. py:method:: get_objective_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_hierarchy_id


    .. py:method:: get_objective_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_hierarchy


    .. py:method:: can_sequence_objectives():
        Tests if this user can sequence objectives.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if sequencing objectives is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: move_objective_ahead(parent_objective_id, reference_objective_id, objective_id):
        Moves an objective ahead of a refrence objective under the given parent.

        :arg:    parent_objective_id (osid.id.Id): the ``Id`` of the
                parent objective
        :arg:    reference_objective_id (osid.id.Id): the ``Id`` of the
                objective
        :arg:    objective_id (osid.id.Id): the ``Id`` of the objective
                to move ahead of ``reference_objective_id``
        :raises:  NotFound - ``parent_objective_id,
                reference_objective_id,`` or ``objective_id`` not found,
                or ``reference_objective_id`` or ``objective_id`` is not
                a child of ``parent_objective_id``
        :raises:  NullArgument - ``parent_objective_id,
                reference_objective_id,`` or ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: move_objective_behind(parent_objective_id, reference_objective_id, objective_id):
        Moves an objective behind a refrence objective under the given parent.

        :arg:    parent_objective_id (osid.id.Id): the ``Id`` of the
                parent objective
        :arg:    reference_objective_id (osid.id.Id): the ``Id`` of the
                objective
        :arg:    objective_id (osid.id.Id): the ``Id`` of the objective
                to move behind ``reference_objective_id``
        :raises:  NotFound - ``parent_objective_id,
                reference_objective_id,`` or ``objective_id`` not found,
                or ``reference_objective_id`` or ``objective_id`` is not
                a child of ``parent_objective_id``
        :raises:  NullArgument - ``parent_objective_id,
                reference_objective_id,`` or ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: sequence_objectives(parent_objective_id, objective_ids):
        Sequences a set of objectives under a parent.

        :arg:    parent_objective_id (osid.id.Id): the ``Id`` of the
                parent objective
        :arg:    objective_ids (osid.id.Id[]): the ``Id`` of the
                objectives
        :raises:  NotFound - ``parent_id`` or an ``objective_id`` not
                found, or an ``objective_id`` is not a child of
                ``parent_objective_id``
        :raises:  NullArgument - ``paren_objectivet_id`` or
                ``objective_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Requisite Methods
---------------------------

    .. py:method:: get_objective_bank_id():
        Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_id


    .. py:method:: get_objective_bank():
        Gets the ``ObjectiveBank`` associated with this session.

        :return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank


    .. py:method:: can_lookup_objective_prerequisites():
        Tests if this user can perform ``Objective`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_objective_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_objective_view():
        A complete view of the ``Objective`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_objective_bank_view():
        Federates the view for methods in this session.

        A federated view will include objectives in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_objective_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_requisite_objectives(objective_id):
        Gets a list of ``Objectives`` that are the immediate requisites for the given ``Objective``.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an ``Objective`` is not found
        or inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        :return: (osid.learning.ObjectiveList) - the returned requisite
                ``Objectives``
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_all_requisite_objectives(objective_id):
        Gets a list of ``Objectives`` that are the requisites for the given ``Objective`` including
            the requistes of the requisites, and so on.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an ``Objective`` is not found
        or inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        :return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_dependent_objectives(objective_id):
        Gets a list of ``Objectives`` that require the given ``Objective``.

        In plenary mode, the returned list contains all of the immediate
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        :return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_objective_required(objective_id, required_objective_id):
        Tests if an objective is required before proceeding with an objective.

        One objective may indirectly depend on another objective by way
        of one or more other objectives.

        :arg:    objective_id (osid.id.Id): ``Id`` of the dependent
                ``Objective``
        :arg:    required_objective_id (osid.id.Id): ``Id`` of the
                required ``Objective``
        :return: (boolean) - ``true`` if ``objective_id`` depends on
                ``required_objective_id,`` ``false`` otherwise
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_equivalent_objectives(objective_id):
        Gets a list of ``Objectives`` that are equivalent to the given ``Objective`` for the purpose
            of requisites.

        An equivalent objective can satisfy the given objective. In
        plenary mode, the returned list contains all of the equivalent
        requisites, or an error results if an Objective is not found or
        inaccessible. Otherwise, inaccessible ``Objectives`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        :return: (osid.learning.ObjectiveList) - the returned
                ``Objective`` list
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Objective Requisite Assignment Methods
--------------------------------------

    .. py:method:: get_objective_bank_id():
        Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_id


    .. py:method:: get_objective_bank():
        Gets the ``ObjectiveBank`` associated with this session.

        :return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank


    .. py:method:: can_assign_requisites():
        Tests if this user can manage objective requisites.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_objective_requisite(objective_id, requisite_objective_id):
        Creates a requirement dependency between two ``Objectives``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the dependent
                ``Objective``
        :arg:    requisite_objective_id (osid.id.Id): the ``Id`` of the
                required ``Objective``
        :raises:  AlreadyExists - ``objective_id`` already mapped to
                ``requisite_objective_id``
        :raises:  NotFound - ``objective_id`` or
                ``requisite_objective_id`` not found
        :raises:  NullArgument - ``objective_id`` or
                ``requisite_objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_objective_requisite(objective_id, requisite_objective_id):
        Removes an ``Objective`` requisite from an ``Objective``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :arg:    requisite_objective_id (osid.id.Id): the ``Id`` of the
                required ``Objective``
        :raises:  NotFound - ``objective_id`` or
                ``requisite_objective_id`` not found or ``objective_id``
                not mapped to ``requisite_objective_id``
        :raises:  NullArgument - ``objective_id`` or
                ``requisite_objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_equivalent_objective(objective_id, equivalent_objective_id):
        Makes an objective equivalent to another objective for the purposes of satisfying a
            requisite.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the principal
                ``Objective``
        :arg:    equivalent_objective_id (osid.id.Id): the ``Id`` of the
                equivalent ``Objective``
        :raises:  AlreadyExists - ``objective_id`` already mapped to
                ``equiavelnt_objective_id``
        :raises:  NotFound - ``objective_id`` or
                ``equivalent_objective_id`` not found
        :raises:  NullArgument - ``objective_id`` or
                ``equivalent_objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_equivalent_objective(objective_id, equivalent_objective_id):
        Removes an ``Objective`` requisite from an ``Objective``.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the principal
                ``Objective``
        :arg:    equivalent_objective_id (osid.id.Id): the ``Id`` of the
                equivalent ``Objective``
        :raises:  NotFound - ``objective_id`` or
                ``equivalent_objective_id`` not found or
                ``objective_id`` is already equivalent to
                ``equivalent_objective_id``
        :raises:  NullArgument - ``objective_id`` or
                ``equivalent_objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Activity Lookup Methods
-----------------------

    .. py:method:: get_objective_bank_id():
        Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_id


    .. py:method:: get_objective_bank():
        Gets the ``ObjectiveBank`` associated with this session.

        :return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank


    .. py:method:: can_lookup_activities():
        Tests if this user can perform ``Activity`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_activity_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_activity_view():
        A complete view of the ``Activity`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_objective_bank_view():
        Federates the view for methods in this session.

        A federated view will include activities in objective banks
        which are children of this objective bank in the objective bank
        hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_objective_bank_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this objective bank only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_activity(activity_id):
        Gets the ``Activity`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Activity`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Activity`` and retained for
        compatibility.

        :arg:    activity_id (osid.id.Id): ``Id`` of the ``Activity``
        :return: (osid.learning.Activity) - the activity
        :raises:  NotFound - ``activity_id`` not found
        :raises:  NullArgument - ``activity_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_activities_by_ids(activity_ids):
        Gets an ``ActivityList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        activities specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Activities`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    activity_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.learning.ActivityList) - the returned ``Activity``
                list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``activity_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activities_by_genus_type(activity_genus_type):
        Gets an ``ActivityList`` corresponding to the given activity genus ``Type`` which does not
            include activities of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :arg:    activity_genus_type (osid.type.Type): an activity genus
                type
        :return: (osid.learning.ActivityList) - the returned ``Activity``
                list
        :raises:  NullArgument - ``activity_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activities_by_parent_genus_type(activity_genus_type):
        Gets an ``ActivityList`` corresponding to the given activity genus ``Type`` and include any
            additional activity with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :arg:    activity_genus_type (osid.type.Type): an activity genus
                type
        :return: (osid.learning.ActivityList) - the returned ``Activity``
                list
        :raises:  NullArgument - ``activity_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activities_by_record_type(activity_record_type):
        Gets a ``ActivityList`` containing the given activity record ``Type``.

        In plenary mode, the returned list contains all known activities
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :arg:    activity_record_type (osid.type.Type): an activity
                record type
        :return: (osid.learning.ActivityList) - the returned ``Activity``
                list
        :raises:  NullArgument - ``activity_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activities_for_objective(objective_id):
        Gets the activities for the given objective.

        In plenary mode, the returned list contains all of the
        activities mapped to the objective ``Id`` or an error results if
        an Id in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :arg:    objective_id (osid.id.Id): ``Id`` of the ``Objective``
        :return: (osid.learning.ActivityList) - list of enrollments
        :raises:  NotFound - ``objective_id`` not found
        :raises:  NullArgument - ``objective_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_activities_for_objectives(objective_ids):
        Gets the activities for the given objectives.

        In plenary mode, the returned list contains all of the
        activities specified in the objective ``Id`` list, in the order
        of the list, including duplicates, or an error results if a
        course offering ``Id`` in the supplied list is not found or
        inaccessible. Otherwise, inaccessible ``Activities`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :arg:    objective_ids (osid.id.IdList): list of objective
                ``Ids``
        :return: (osid.learning.ActivityList) - list of activities
        :raises:  NotFound - an ``objective_id`` not found
        :raises:  NullArgument - ``objective_id_list`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_activities_by_asset(asset_id):
        Gets the activities for the given asset.

        In plenary mode, the returned list contains all of the
        activities mapped to the asset ``Id`` or an error results if an
        ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :arg:    asset_id (osid.id.Id): ``Id`` of an ``Asset``
        :return: (osid.learning.ActivityList) - list of activities
        :raises:  NotFound - ``asset_id`` not found
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_activities_by_assets(asset_ids):
        Gets the activities for the given asset.

        In plenary mode, the returned list contains all of the
        activities mapped to the asset ``Id`` or an error results if an
        ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Activities`` may be omitted from the
        list and may present the elements in any order including
        returning a unique set.

        :arg:    asset_ids (osid.id.IdList): ``Ids`` of ``Assets``
        :return: (osid.learning.ActivityList) - list of activities
        :raises:  NotFound - an ``asset_id`` not found
        :raises:  NullArgument - ``asset_id_list`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_activities():
        Gets all ``Activities``.

        In plenary mode, the returned list contains all known activites
        or an error results. Otherwise, the returned list may contain
        only those activities that are accessible through this session.

        :return: (osid.learning.ActivityList) - a ``ActivityList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: activities




Activity Admin Methods
----------------------

    .. py:method:: get_objective_bank_id():
        Gets the ``ObjectiveBank``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``ObjectiveBank Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank_id


    .. py:method:: get_objective_bank():
        Gets the ``ObjectiveBank`` associated with this session.

        :return: (osid.learning.ObjectiveBank) - the ``ObjectiveBank``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: objective_bank


    .. py:method:: can_create_activities():
        Tests if this user can create ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Activity`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_activity_with_record_types(activity_record_types):
        Tests if this user can create a single ``Activity`` using the desired record types.

        While ``LearningManager.getActivityRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Activity``.
        Providing an empty array tests if an ``Activity`` can be created
        with no records.

        :arg:    activity_record_types (osid.type.Type[]): array of
                activity record types
        :return: (boolean) - ``true`` if ``Activity`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``activity_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activity_form_for_create(objective_id, activity_record_types):
        Gets the activity form for creating new activities.

        A new form should be requested for each create transaction.

        :arg:    objective_id (osid.id.Id): the ``Id`` of the
                ``Objective``
        :arg:    activity_record_types (osid.type.Type[]): array of
                activity record types
        :return: (osid.learning.ActivityForm) - the activity form
        :raises:  NotFound - ``objective_id`` is not found
        :raises:  NullArgument - ``objective_id`` or
                ``activity_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_activity(activity_form):
        Creates a new ``Activity``.

        :arg:    activity_form (osid.learning.ActivityForm): the form for
                this ``Activity``
        :return: (osid.learning.Activity) - the new ``Activity``
        :raises:  IllegalState - ``activity_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``activity_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``activity_form`` did not originate from
                ``get_activity_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_activities():
        Tests if this user can update ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if activity modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_activity_form_for_update(activity_id):
        Gets the activity form for updating an existing activity.

        A new activity form should be requested for each update
        transaction.

        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
        :return: (osid.learning.ActivityForm) - the activity form
        :raises:  NotFound - ``activity_id`` is not found
        :raises:  NullArgument - ``activity_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_activity(activity_form):
        Updates an existing activity,.

        :arg:    activity_form (osid.learning.ActivityForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``activity_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``activity_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``activity_form`` did not originate from
                ``get_activity_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_activities():
        Tests if this user can delete ``Activities``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Activity`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Activity`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_activity(activity_id):
        Deletes the ``Activity`` identified by the given ``Id``.

        :arg:    activity_id (osid.id.Id): the ``Id`` of the ``Activity``
                to delete
        :raises:  NotFound - an ``Activity`` was not found identified by
                the given ``Id``
        :raises:  NullArgument - ``activity_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_activity_aliases():
        Tests if this user can manage ``Id`` aliases for activities.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Activity`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_activity(activity_id, alias_id):
        Adds an ``Id`` to an ``Activity`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Activity`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another activity, it is
        reassigned to the given activity ``Id``.

        :arg:    activity_id (osid.id.Id): the ``Id`` of an ``Activity``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``activity_id`` not found
        :raises:  NullArgument - ``activity_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






