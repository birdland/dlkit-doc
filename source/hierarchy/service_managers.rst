

Service Managers
================


Hierarchy Manager
-----------------

.. py:class:: HierarchyManager(osid_managers.OsidManager, HierarchyProfile, hierarchy_managers.HierarchyManager)
    The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.


    The sessions included in this manager are:




      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies





    .. py:method:: get_hierarchy_traversal_session():
        :noindex:


    .. py:attribute:: hierarchy_traversal_session
        :noindex:


    .. py:method:: get_hierarchy_traversal_session_for_hierarchy(hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchy_design_session():
        :noindex:


    .. py:attribute:: hierarchy_design_session
        :noindex:


    .. py:method:: get_hierarchy_design_session_for_hierarchy(hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchy_sequencing_session():
        :noindex:


    .. py:attribute:: hierarchy_sequencing_session
        :noindex:


    .. py:method:: get_hierarchy_sequencing_session_for_hierarchy(hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchy_structure_notification_session(hierarchy_structure_receiver):
        :noindex:


    .. py:method:: get_hierarchy_structure_notification_session_for_hierarchy(hierarchy_structure_receiver, hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchy_lookup_session():
        :noindex:


    .. py:attribute:: hierarchy_lookup_session
        :noindex:


    .. py:method:: get_hierarchy_query_session():
        :noindex:


    .. py:attribute:: hierarchy_query_session
        :noindex:


    .. py:method:: get_hierarchy_search_session():
        :noindex:


    .. py:attribute:: hierarchy_search_session
        :noindex:


    .. py:method:: get_hierarchy_admin_session():
        :noindex:


    .. py:attribute:: hierarchy_admin_session
        :noindex:


    .. py:method:: get_hierarchy_notification_session(hierarchy_receiver):
        :noindex:




Hierarchy Traversal Methods
---------------------------

    .. py:method:: get_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchy_id


    .. py:method:: get_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchy


    .. py:method:: can_access_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_roots():
        Gets the root nodes of this hierarchy.

        :return: (osid.id.IdList) - the root nodes
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: roots


    .. py:method:: has_parents(id_):
        Tests if this ``Id`` contains any parents.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :return: (boolean) - ``true`` if this ``Id`` contains parents,
                ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent(id_, parent_id):
        Tests if an ``Id`` is a direct parent of another.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    parent_id (osid.id.Id): the ``Id`` of a parent
        :return: (boolean) - ``true`` if this ``parent_id`` is a parent
                of ``id,``  ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` or ``parent_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``parent_id`` not found return
        ``false``.




    .. py:method:: get_parents(id_):
        Gets the parents of the given ``id``.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the parents of the ``id``
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor(id_, ancestor_id):
        Tests if an ``Id`` is an ancestor of another.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_id (osid.id.Id): the ``Id`` of an ancestor
        :return: (boolean) - ``true`` if this ``ancestor_id`` is a parent
                of ``id,``  ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` or ``ancestor_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``ancestor_id`` not found return
        ``false``.




    .. py:method:: has_children(id_):
        Tests if this ``Id`` has any children.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :return: (boolean) - ``true`` if this ``Id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child(id_, child_id):
        Tests if a node is a direct child of another.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    child_id (osid.id.Id): the ``Id`` of a child
        :return: (boolean) - ``true`` if this ``child_id`` is a child of
                the ``Id,``  ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``child_id`` not found return
        ``false``.




    .. py:method:: get_children(id_):
        Gets the children of the given ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the ``id``
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant(id_, descendant_id):
        Tests if a node is a descendant of another.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    descendant_id (osid.id.Id): the ``Id`` of a descendant
        :return: (boolean) - ``true`` if this ``descendant_id`` is a
                child of the ``Id,``  ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` or ``descendant`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If not found return ``false``.




    .. py:method:: get_nodes(id_, ancestor_levels=10, descendant_levels=10, include_siblings=False):
        Gets a portion of the hierarchy for the given ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a node
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Hierarchy Design Methods
------------------------

    .. py:method:: get_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchy_id


    .. py:method:: get_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchy


    .. py:method:: can_modify_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root(id_):
        Adds a root node.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :raises:  AlreadyExists - ``id`` is already in hierarchy
        :raises:  NotFound - ``id`` not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child(id_, child_id):
        Adds a child to a ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``child_id`` is already a child of
                ``id``
        :raises:  NotFound - ``id`` or ``child_id`` not found
        :raises:  NullArgument - ``id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root(id_):
        Removes a root node.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :raises:  NotFound - ``id`` was not found or not in hierarchy
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child(id_, child_id):
        Removes a childfrom an ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :arg:    child_id (osid.id.Id): the ``Id`` of the child to remove
        :raises:  NotFound - ``id`` or ``child_id`` was not found or
                ``child_id`` is not a child of ``id``
        :raises:  NullArgument - ``id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_children(id_):
        Removes all childrenfrom an ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :raises:  NotFound - an node identified by the given ``Id`` was
                not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Hierarchy Lookup Methods
------------------------

    .. py:method:: can_lookup_hierarchies():
        Tests if this user can perform ``Hierarchy`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_hierarchy_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_hierarchy_view():
        A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_hierarchy(hierarchy_id):
        Gets the ``Hierarchy`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Hierarchy`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Hierarchy`` and retained
        for compati

        :arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy`` to retrieve
        :return: (osid.hierarchy.Hierarchy) - the returned ``Hierarchy``
        :raises:  NotFound - no ``Hierarchy`` found with the given ``Id``
        :raises:  NullArgument - ``hierarchy_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_ids(hierarchy_ids):
        Gets a ``Hierarchy`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        hierarchies specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Hierarchy`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :arg:    hierarchy_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``hierarchy_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_genus_type(hierarchy_genus_type):
        Gets a ``HierarchyList`` corresponding to the given genus ``Type`` which does not include
            hierarchies of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :arg:    hierarchy_genus_type (osid.type.Type): a hierarchy genus
                type
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NullArgument - ``hierarchy_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_parent_genus_type(hierarchy_genus_type):
        Gets a ``HierarchyList`` corresponding to the given hierarchy genus ``Type`` and include any
            additional hierarchies with types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :arg:    hierarchy_genus_type (osid.type.Type): a hierarchy genus
                type
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NullArgument - ``hierarchy_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_record_type(hierarchy_record_type):
        Gets a ``HierarchyList`` corresponding to the given hierarchy record ``Type``.

        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :arg:    hierarchy_record_type (osid.type.Type): a hierarchy
                record type
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NullArgument - ``hierarchy_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_provider(resource_id):
        Gets a ``HierarchyList`` for the given provider ````.

        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies():
        Gets all hierarchies.

        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :return: (osid.hierarchy.HierarchyList) - a list of
                ``Hierarchies``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchies




Hierarchy Admin Methods
-----------------------

    .. py:method:: can_create_hierarchies():
        Tests if this user can create ``Hierarchy`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Hierarchy`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_hierarchy_with_record_types(hierarchy_record_types):
        Tests if this user can create a single ``Hierarchy`` using the desired record types.

        While ``HierarchyManager.getHierarchyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Hierarchy``.
        Providing an empty array tests if a ``Hierarchy`` can be created
        with no records.

        :arg:    hierarchy_record_types (osid.type.Type[]): array of
                hierarchy record types
        :return: (boolean) - ``true`` if ``Hierarchy`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``hierarchy_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchy_form_for_create(hierarchy_record_types):
        Gets the hierarchy form for creating new hierarchies.

        A new form should be requested for each create transaction. This
        method is used for creating new hierarchies, where only the
        ``Hierarchy`` ``Type`` is known.

        :arg:    hierarchy_record_types (osid.type.Type[]): array of
                hierarchy record types
        :return: (osid.hierarchy.HierarchyForm) - the hierarchy form
        :raises:  NullArgument - ``hierarchy_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_hierarchy(hierarchy_form):
        Creates a new ``Hierarchy``.

        :arg:    hierarchy_form (osid.hierarchy.HierarchyForm): the form
                for this ``Hierarchy``
        :return: (osid.hierarchy.Hierarchy) - the new ``Hierarchy``
        :raises:  IllegalState - ``hierarchy_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``hierarchy_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``hierarchy_form`` did not originate from
                ``get_hierarchy_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_hierarchies():
        Tests if this user can update ``Hierarchy`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Hierarchy`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchy_form_for_update(hierarchy_id):
        Gets the hierarchy form for updating an existing hierarchy.

        A new hierarchy form should be requested for each update
        transaction.

        :arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy``
        :return: (osid.hierarchy.HierarchyForm) - the hierarchy form
        :raises:  NotFound - ``hierarchy_id`` is not found
        :raises:  NullArgument - ``hierarchy_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_hierarchy(hierarchy_form):
        Updates an existing hierarchy.

        :arg:    hierarchy_form (osid.hierarchy.HierarchyForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``hierarchy_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``hierarchy_id`` or ``hierarchy_form`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``hierarchy_form`` did not originate from
                ``get_hierarchy_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_hierarchies():
        Tests if this user can delete ``Hierarchy`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Hierarchy`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_hierarchy(hierarchy_id):
        Deletes a ``Hierarchy``.

        :arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy`` to remove
        :raises:  NotFound - ``hierarchy_id`` not found
        :raises:  NullArgument - ``hierarchy_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_hierarchy_aliases():
        Tests if this user can manage ``Id`` aliases for ``Hierarchy`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Hierarchy`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_hierarchy(hierarchy_id, alias_id):
        Adds an ``Id`` to a ``Hierarchy`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Hierarchy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.

        :arg:    hierarchy_id (osid.id.Id): the ``Id`` of an
                ``Hierarchy``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``hierarchy_id`` not found
        :raises:  NullArgument - ``hierarchy_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Hierarchy Proxy Manager
-----------------------

.. py:class:: HierarchyProxyManager(osid_managers.OsidProxyManager, HierarchyProfile, hierarchy_managers.HierarchyProxyManager)
    The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.


    Methods in this manager accept a ``Proxy`` to pass information from
    server environments. The sessions included in this manager are:




      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies





    .. py:method:: get_hierarchy_traversal_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_traversal_session_for_hierarchy(hierarchy_id, proxy):
        :noindex:


    .. py:method:: get_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_design_session_for_hierarchy(hierarchy_id, proxy):
        :noindex:


    .. py:method:: get_hierarchy_sequencing_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_sequencing_session_for_hierarchy(hierarchy_id, proxy):
        :noindex:


    .. py:method:: get_hierarchy_structure_notification_session(hierarchy_structure_receiver, proxy):
        :noindex:


    .. py:method:: get_hierarchy_structure_notification_session_for_hierarchy(hierarchy_structure_receiver, hierarchy_id, proxy):
        :noindex:


    .. py:method:: get_hierarchy_lookup_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_query_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_search_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_admin_session(proxy):
        :noindex:


    .. py:method:: get_hierarchy_notification_session(hierarchy_receiver, proxy):
        :noindex:




Hierarchy Traversal Methods
---------------------------

    .. py:method:: get_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchy_id


    .. py:method:: get_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchy


    .. py:method:: can_access_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_roots():
        Gets the root nodes of this hierarchy.

        :return: (osid.id.IdList) - the root nodes
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: roots


    .. py:method:: has_parents(id_):
        Tests if this ``Id`` contains any parents.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :return: (boolean) - ``true`` if this ``Id`` contains parents,
                ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent(id_, parent_id):
        Tests if an ``Id`` is a direct parent of another.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    parent_id (osid.id.Id): the ``Id`` of a parent
        :return: (boolean) - ``true`` if this ``parent_id`` is a parent
                of ``id,``  ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` or ``parent_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``parent_id`` not found return
        ``false``.




    .. py:method:: get_parents(id_):
        Gets the parents of the given ``id``.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the parents of the ``id``
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor(id_, ancestor_id):
        Tests if an ``Id`` is an ancestor of another.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_id (osid.id.Id): the ``Id`` of an ancestor
        :return: (boolean) - ``true`` if this ``ancestor_id`` is a parent
                of ``id,``  ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` or ``ancestor_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``ancestor_id`` not found return
        ``false``.




    .. py:method:: has_children(id_):
        Tests if this ``Id`` has any children.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :return: (boolean) - ``true`` if this ``Id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child(id_, child_id):
        Tests if a node is a direct child of another.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    child_id (osid.id.Id): the ``Id`` of a child
        :return: (boolean) - ``true`` if this ``child_id`` is a child of
                the ``Id,``  ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``child_id`` not found return
        ``false``.




    .. py:method:: get_children(id_):
        Gets the children of the given ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the ``id``
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant(id_, descendant_id):
        Tests if a node is a descendant of another.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    descendant_id (osid.id.Id): the ``Id`` of a descendant
        :return: (boolean) - ``true`` if this ``descendant_id`` is a
                child of the ``Id,``  ``false`` otherwise
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` or ``descendant`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If not found return ``false``.




    .. py:method:: get_nodes(id_, ancestor_levels=10, descendant_levels=10, include_siblings=False):
        Gets a portion of the hierarchy for the given ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a node
        :raises:  NotFound - ``id`` is not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Hierarchy Design Methods
------------------------

    .. py:method:: get_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchy_id


    .. py:method:: get_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchy


    .. py:method:: can_modify_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root(id_):
        Adds a root node.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :raises:  AlreadyExists - ``id`` is already in hierarchy
        :raises:  NotFound - ``id`` not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child(id_, child_id):
        Adds a child to a ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``child_id`` is already a child of
                ``id``
        :raises:  NotFound - ``id`` or ``child_id`` not found
        :raises:  NullArgument - ``id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root(id_):
        Removes a root node.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :raises:  NotFound - ``id`` was not found or not in hierarchy
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child(id_, child_id):
        Removes a childfrom an ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :arg:    child_id (osid.id.Id): the ``Id`` of the child to remove
        :raises:  NotFound - ``id`` or ``child_id`` was not found or
                ``child_id`` is not a child of ``id``
        :raises:  NullArgument - ``id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_children(id_):
        Removes all childrenfrom an ``Id``.

        :arg:    id (osid.id.Id): the ``Id`` of the node
        :raises:  NotFound - an node identified by the given ``Id`` was
                not found
        :raises:  NullArgument - ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Hierarchy Lookup Methods
------------------------

    .. py:method:: can_lookup_hierarchies():
        Tests if this user can perform ``Hierarchy`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_hierarchy_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_hierarchy_view():
        A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_hierarchy(hierarchy_id):
        Gets the ``Hierarchy`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Hierarchy`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Hierarchy`` and retained
        for compati

        :arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy`` to retrieve
        :return: (osid.hierarchy.Hierarchy) - the returned ``Hierarchy``
        :raises:  NotFound - no ``Hierarchy`` found with the given ``Id``
        :raises:  NullArgument - ``hierarchy_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_ids(hierarchy_ids):
        Gets a ``Hierarchy`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        hierarchies specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Hierarchy`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :arg:    hierarchy_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``hierarchy_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_genus_type(hierarchy_genus_type):
        Gets a ``HierarchyList`` corresponding to the given genus ``Type`` which does not include
            hierarchies of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :arg:    hierarchy_genus_type (osid.type.Type): a hierarchy genus
                type
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NullArgument - ``hierarchy_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_parent_genus_type(hierarchy_genus_type):
        Gets a ``HierarchyList`` corresponding to the given hierarchy genus ``Type`` and include any
            additional hierarchies with types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :arg:    hierarchy_genus_type (osid.type.Type): a hierarchy genus
                type
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NullArgument - ``hierarchy_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_record_type(hierarchy_record_type):
        Gets a ``HierarchyList`` corresponding to the given hierarchy record ``Type``.

        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :arg:    hierarchy_record_type (osid.type.Type): a hierarchy
                record type
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NullArgument - ``hierarchy_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies_by_provider(resource_id):
        Gets a ``HierarchyList`` for the given provider ````.

        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchies():
        Gets all hierarchies.

        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        :return: (osid.hierarchy.HierarchyList) - a list of
                ``Hierarchies``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: hierarchies




Hierarchy Admin Methods
-----------------------

    .. py:method:: can_create_hierarchies():
        Tests if this user can create ``Hierarchy`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Hierarchy`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_hierarchy_with_record_types(hierarchy_record_types):
        Tests if this user can create a single ``Hierarchy`` using the desired record types.

        While ``HierarchyManager.getHierarchyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Hierarchy``.
        Providing an empty array tests if a ``Hierarchy`` can be created
        with no records.

        :arg:    hierarchy_record_types (osid.type.Type[]): array of
                hierarchy record types
        :return: (boolean) - ``true`` if ``Hierarchy`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``hierarchy_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchy_form_for_create(hierarchy_record_types):
        Gets the hierarchy form for creating new hierarchies.

        A new form should be requested for each create transaction. This
        method is used for creating new hierarchies, where only the
        ``Hierarchy`` ``Type`` is known.

        :arg:    hierarchy_record_types (osid.type.Type[]): array of
                hierarchy record types
        :return: (osid.hierarchy.HierarchyForm) - the hierarchy form
        :raises:  NullArgument - ``hierarchy_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_hierarchy(hierarchy_form):
        Creates a new ``Hierarchy``.

        :arg:    hierarchy_form (osid.hierarchy.HierarchyForm): the form
                for this ``Hierarchy``
        :return: (osid.hierarchy.Hierarchy) - the new ``Hierarchy``
        :raises:  IllegalState - ``hierarchy_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``hierarchy_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``hierarchy_form`` did not originate from
                ``get_hierarchy_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_hierarchies():
        Tests if this user can update ``Hierarchy`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Hierarchy`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_hierarchy_form_for_update(hierarchy_id):
        Gets the hierarchy form for updating an existing hierarchy.

        A new hierarchy form should be requested for each update
        transaction.

        :arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy``
        :return: (osid.hierarchy.HierarchyForm) - the hierarchy form
        :raises:  NotFound - ``hierarchy_id`` is not found
        :raises:  NullArgument - ``hierarchy_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_hierarchy(hierarchy_form):
        Updates an existing hierarchy.

        :arg:    hierarchy_form (osid.hierarchy.HierarchyForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``hierarchy_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``hierarchy_id`` or ``hierarchy_form`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``hierarchy_form`` did not originate from
                ``get_hierarchy_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_hierarchies():
        Tests if this user can delete ``Hierarchy`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Hierarchy`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_hierarchy(hierarchy_id):
        Deletes a ``Hierarchy``.

        :arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy`` to remove
        :raises:  NotFound - ``hierarchy_id`` not found
        :raises:  NullArgument - ``hierarchy_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_hierarchy_aliases():
        Tests if this user can manage ``Id`` aliases for ``Hierarchy`` objects.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Hierarchy`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_hierarchy(hierarchy_id, alias_id):
        Adds an ``Id`` to a ``Hierarchy`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Hierarchy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.

        :arg:    hierarchy_id (osid.id.Id): the ``Id`` of an
                ``Hierarchy``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``hierarchy_id`` not found
        :raises:  NullArgument - ``hierarchy_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






