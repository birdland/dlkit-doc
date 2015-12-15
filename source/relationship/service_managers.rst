

Service Managers
================


Relationship Manager
--------------------

.. py:class:: RelationshipManager(osid_managers.OsidManager, RelationshipProfile, relationship_managers.RelationshipManager)
    The relationship manager provides access to relationship sessions and provides interoperability
    tests for various aspects of this service.


    The sessions included in this manager are:




      * ``RelationshipLookupSession:`` a session to retrieve and examine
        relationships
      * ``RelationshipQuerySession:`` a session to query relationships
      * ``RelationshipSearchSession:`` a session to search for
        relationships
      * ``RelationshipAdminSession:`` a session to manage relationships
      * ``RelationshipNotificationSession:`` a session to receive
        notifications pertaining to relationship changes
      * ``RelationshipFamilySession:`` a session to look up relationship
        to family mappings
      * ``RelationshipFamilyAssignmentSession:`` a session to manage
        relationship to family catalog mappings
      * ``RelationshipSmartFamilySession:`` a session to manage dynamic
        relationship families




      * ``FamilyLookupSession:`` a session to retrieve families
      * ``FamilyQuerySession:`` a session to query families
      * ``FamilySearchSession:`` a session to search for families
      * ``FamilyAdminSession:`` a session to create and delete families
      * ``FamilyNotificationSession:`` a session to receive
        notifications pertaining to family changes
      * ``FamilyHierarchySession:`` a session to traverse a hierarchy of
        families
      * ``FamilyHierarchyDesignSession:`` a session to manage a family
        hierarchy





    .. py:method:: get_relationship_lookup_session():
        :noindex:


    .. py:attribute:: relationship_lookup_session
        :noindex:


    .. py:method:: get_relationship_lookup_session_for_family(family_id):
        :noindex:


    .. py:method:: get_relationship_query_session():
        :noindex:


    .. py:attribute:: relationship_query_session
        :noindex:


    .. py:method:: get_relationship_query_session_for_family(family_id):
        :noindex:


    .. py:method:: get_relationship_search_session():
        :noindex:


    .. py:attribute:: relationship_search_session
        :noindex:


    .. py:method:: get_relationship_search_session_for_family(family_id):
        :noindex:


    .. py:method:: get_relationship_admin_session():
        :noindex:


    .. py:attribute:: relationship_admin_session
        :noindex:


    .. py:method:: get_relationship_admin_session_for_family(family_id):
        :noindex:


    .. py:method:: get_relationship_notification_session(relationship_receiver):
        :noindex:


    .. py:method:: get_relationship_notification_session_for_family(relationship_receiver, family_id):
        :noindex:


    .. py:method:: get_relationship_family_session():
        :noindex:


    .. py:attribute:: relationship_family_session
        :noindex:


    .. py:method:: get_relationship_family_assignment_session():
        :noindex:


    .. py:attribute:: relationship_family_assignment_session
        :noindex:


    .. py:method:: get_relationship_smart_family_session(family_id):
        :noindex:


    .. py:method:: get_family_lookup_session():
        :noindex:


    .. py:attribute:: family_lookup_session
        :noindex:


    .. py:method:: get_family_query_session():
        :noindex:


    .. py:attribute:: family_query_session
        :noindex:


    .. py:method:: get_family_search_session():
        :noindex:


    .. py:attribute:: family_search_session
        :noindex:


    .. py:method:: get_family_admin_session():
        :noindex:


    .. py:attribute:: family_admin_session
        :noindex:


    .. py:method:: get_family_notification_session(family_receiver):
        :noindex:


    .. py:method:: get_family_hierarchy_session():
        :noindex:


    .. py:attribute:: family_hierarchy_session
        :noindex:


    .. py:method:: get_family_hierarchy_design_session():
        :noindex:


    .. py:attribute:: family_hierarchy_design_session
        :noindex:


    .. py:method:: get_relationship_batch_manager():
        :noindex:


    .. py:attribute:: relationship_batch_manager
        :noindex:


    .. py:method:: get_relationship_rules_manager():
        :noindex:


    .. py:attribute:: relationship_rules_manager
        :noindex:




Family Lookup Methods
---------------------

    .. py:method:: can_lookup_families():
        Tests if this user can perform ``Family`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_family_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_family_view():
        A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_family(family_id):
        Gets the ``Family`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Family`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Family`` and retained for compatibil

        :arg:    family_id (osid.id.Id): ``Id`` of the ``Family``
        :return: (osid.relationship.Family) - the family
        :raises:  NotFound - ``family_id`` not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_families_by_ids(family_ids):
        Gets a ``FamilyList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the families
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible families may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    family_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``family_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families_by_genus_type(family_genus_type):
        Gets a ``FamilyList`` corresponding to the given family genus ``Type`` which does not
            include families of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :arg:    family_genus_type (osid.type.Type): a family genus type
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NullArgument - ``family_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families_by_parent_genus_type(family_genus_type):
        Gets a ``FamilyList`` corresponding to the given family genus ``Type`` and include any
            additional families with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :arg:    family_genus_type (osid.type.Type): a family genus type
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NullArgument - ``family_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families_by_record_type(family_record_type):
        Gets a ``FamilyList`` containing the given family record ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :arg:    family_record_type (osid.type.Type): a family record
                type
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NullArgument - ``family_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families_by_provider(resource_id):
        Gets a ``FamilyList`` from the given provider.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families():
        Gets all families.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :return: (osid.relationship.FamilyList) - a list of families
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: families




Family Admin Methods
--------------------

    .. py:method:: can_create_families():
        Tests if this user can create families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Family`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_family_with_record_types(family_record_types):
        Tests if this user can create a single ``Family`` using the desired record types.

        While ``RelationshipManager.getFamilyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Family``.
        Providing an empty array tests if a ``Family`` can be created
        with no records.

        :arg:    family_record_types (osid.type.Type[]): array of family
                record types
        :return: (boolean) - ``true`` if ``Family`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``family_record_types is null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_family_form_for_create(family_record_types):
        Gets the family form for creating new families.

        A new form should be requested for each create transaction.

        :arg:    family_record_types (osid.type.Type[]): array of family
                record types
        :return: (osid.relationship.FamilyForm) - the family form
        :raises:  NullArgument - ``family_record_types is null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_family(family_form):
        Creates a new ``Family``.

        :arg:    family_form (osid.relationship.FamilyForm): the form for
                this ``Family``.
        :return: (osid.relationship.Family) - the new ``Family``
        :raises:  IllegalState - ``family_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``family_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``family_form`` did not originate from
                ``get_family_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_families():
        Tests if this user can update families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Family`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_family_form_for_update(family_id):
        Gets the family form for updating an existing family.

        A new family form should be requested for each update
        transaction.

        :arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        :return: (osid.relationship.FamilyForm) - the family form
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_family(family_form):
        Updates an existing family.

        :arg:    family_form (osid.relationship.FamilyForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``family_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``family_id`` or ``family_form`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``family_form`` did not originate from
                ``get_family_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_families():
        Tests if this user can delete families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Family`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_family(family_id):
        Deletes a ``Family``.

        :arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                remove
        :raises:  NotFound - ``family_id`` not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_family_aliases():
        Tests if this user can manage ``Id`` aliases for families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Family`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_family(family_id, alias_id):
        Adds an ``Id`` to a ``Family`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Family`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another family, it is
        reassigned to the given family ``Id``.

        :arg:    family_id (osid.id.Id): the ``Id`` of a ``Family``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``family_id`` not found
        :raises:  NullArgument - ``family_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Family Hierarchy Methods
------------------------

    .. py:method:: get_family_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_hierarchy_id


    .. py:method:: get_family_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_hierarchy


    .. py:method:: can_access_family_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_family_view():
        The returns from the family methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_family_view():
        A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_family_ids():
        Gets the root family ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root family ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_family_ids


    .. py:method:: get_root_families():
        Gets the root families in the family hierarchy.

        A node with no parents is an orphan. While all family ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: (osid.relationship.FamilyList) - the root families
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_families


    .. py:method:: has_parent_families(family_id):
        Tests if the ``Family`` has any parents.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if the family has parents,
                ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_family(id_, family_id):
        Tests if an ``Id`` is a direct parent of a family.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``family_id,``  ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``id`` or ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_family_ids(family_id):
        Gets the parent ``Ids`` of the given family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (osid.id.IdList) - the parent ``Ids`` of the family
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_families(family_id):
        Gets the parent families of the given ``id``.

        :arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                query
        :return: (osid.relationship.FamilyList) - the parent families of
                the ``id``
        :raises:  NotFound - a ``Family`` identified by ``Id is`` not
                found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_family(id_, family_id):
        Tests if an ``Id`` is an ancestor of a family.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``family_id,``  ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``id`` or ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_families(family_id):
        Tests if a family has any children.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if the ``family_id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_family(id_, family_id):
        Tests if a family is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``family_id,``  ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``id`` or ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_family_ids(family_id):
        Gets the child ``Ids`` of the given family.

        :arg:    family_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the family
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_families(family_id):
        Gets the child families of the given ``id``.

        :arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                query
        :return: (osid.relationship.FamilyList) - the child families of
                the ``id``
        :raises:  NotFound - a ``Family`` identified by ``Id is`` not
                found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_family(id_, family_id):
        Tests if an ``Id`` is a descendant of a family.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``family_id,``  ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``id`` or ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_family_node_ids(family_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given family.

        :arg:    family_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a family node
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_family_nodes(family_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given family.

        :arg:    family_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.relationship.FamilyNode) - a family node
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Family Hierarchy Design Methods
-------------------------------

    .. py:method:: get_family_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_hierarchy_id


    .. py:method:: get_family_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_hierarchy


    .. py:method:: can_modify_family_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_family(family_id):
        Adds a root family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :raises:  AlreadyExists - ``family_id`` is already in hierarchy
        :raises:  NotFound - ``family_id`` not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_family(family_id):
        Removes a root family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :raises:  NotFound - ``family_id`` not a root
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_family(family_id, child_id):
        Adds a child to a family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``family_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``family_id`` or ``child_id`` not found
        :raises:  NullArgument - ``family_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_family(family_id, child_id):
        Removes a child from a family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``family_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``family_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_families(family_id):
        Removes all children from a family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :raises:  NotFound - ``family_id`` not in hierarchy
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Relationship Proxy Manager
--------------------------

.. py:class:: RelationshipProxyManager(osid_managers.OsidProxyManager, RelationshipProfile, relationship_managers.RelationshipProxyManager)
    The relationship manager provides access to relationship sessions and provides interoperability
    tests for various aspects of this service.


    Methods in this manager support the passing of a Proxy. The sessions
    included in this manager are:




      * ``RelationshipLookupSession:`` a session to retrieve and examine
        relationships
      * ``RelationshipQuerySession:`` a session to query relationships
      * ``RelationshipSearchSession:`` a session to search for
        relationships
      * ``RelationshipAdminSession:`` a session to manage relationships
      * ``RelationshipNotificationSession:`` a session to receive
        notifications pertaining to relationship changes
      * ``RelationshipFamilySession:`` a session to look up relationship
        to family mappings
      * ``RelationshipFamilyAssignmentSession:`` a session to manage
        relationship to family catalog mappings
      * ``RelationshipSmartFamilySession:`` a session to manage dynamic
        relationship families




      * ``FamilyLookupSession:`` a session to retrieve families
      * ``FamilyQuerySession:`` a session to query families
      * ``FamilySearchSession:`` a session to search for families
      * ``FamilyAdminSession:`` a session to create and delete families
      * ``FamilyNotificationSession:`` a session to receive
        notifications pertaining to family changes
      * ``FamilyHierarchySession:`` a session to traverse a hierarchy of
        families
      * ``FamilyHierarchyDesignSession:`` a session to manage a family
        hierarchy





    .. py:method:: get_relationship_lookup_session(proxy):
        :noindex:


    .. py:method:: get_relationship_lookup_session_for_family(family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_query_session(proxy):
        :noindex:


    .. py:method:: get_relationship_query_session_for_family(family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_search_session(proxy):
        :noindex:


    .. py:method:: get_relationship_search_session_for_family(family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_admin_session(proxy):
        :noindex:


    .. py:method:: get_relationship_admin_session_for_family(family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_notification_session(relationship_receiver, proxy):
        :noindex:


    .. py:method:: get_relationship_notification_session_for_family(relationship_receiver, family_id, proxy):
        :noindex:


    .. py:method:: get_relationship_family_session(proxy):
        :noindex:


    .. py:method:: get_relationship_family_assignment_session(proxy):
        :noindex:


    .. py:method:: get_relationship_smart_family_session(family_id, proxy):
        :noindex:


    .. py:method:: get_family_lookup_session(proxy):
        :noindex:


    .. py:method:: get_family_query_session(proxy):
        :noindex:


    .. py:method:: get_family_search_session(proxy):
        :noindex:


    .. py:method:: get_family_admin_session(proxy):
        :noindex:


    .. py:method:: get_family_notification_session(family_receiver, proxy):
        :noindex:


    .. py:method:: get_family_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_family_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_relationship_batch_proxy_manager():
        :noindex:


    .. py:attribute:: relationship_batch_proxy_manager
        :noindex:


    .. py:method:: get_relationship_rules_proxy_manager():
        :noindex:


    .. py:attribute:: relationship_rules_proxy_manager
        :noindex:




Family Lookup Methods
---------------------

    .. py:method:: can_lookup_families():
        Tests if this user can perform ``Family`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_family_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_family_view():
        A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_family(family_id):
        Gets the ``Family`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Family`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Family`` and retained for compatibil

        :arg:    family_id (osid.id.Id): ``Id`` of the ``Family``
        :return: (osid.relationship.Family) - the family
        :raises:  NotFound - ``family_id`` not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_families_by_ids(family_ids):
        Gets a ``FamilyList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the families
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible families may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    family_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``family_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families_by_genus_type(family_genus_type):
        Gets a ``FamilyList`` corresponding to the given family genus ``Type`` which does not
            include families of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :arg:    family_genus_type (osid.type.Type): a family genus type
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NullArgument - ``family_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families_by_parent_genus_type(family_genus_type):
        Gets a ``FamilyList`` corresponding to the given family genus ``Type`` and include any
            additional families with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :arg:    family_genus_type (osid.type.Type): a family genus type
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NullArgument - ``family_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families_by_record_type(family_record_type):
        Gets a ``FamilyList`` containing the given family record ``Type``.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :arg:    family_record_type (osid.type.Type): a family record
                type
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NullArgument - ``family_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families_by_provider(resource_id):
        Gets a ``FamilyList`` from the given provider.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.relationship.FamilyList) - the returned ``Family
                list``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_families():
        Gets all families.

        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :return: (osid.relationship.FamilyList) - a list of families
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: families




Family Admin Methods
--------------------

    .. py:method:: can_create_families():
        Tests if this user can create families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Family`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_family_with_record_types(family_record_types):
        Tests if this user can create a single ``Family`` using the desired record types.

        While ``RelationshipManager.getFamilyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Family``.
        Providing an empty array tests if a ``Family`` can be created
        with no records.

        :arg:    family_record_types (osid.type.Type[]): array of family
                record types
        :return: (boolean) - ``true`` if ``Family`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``family_record_types is null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_family_form_for_create(family_record_types):
        Gets the family form for creating new families.

        A new form should be requested for each create transaction.

        :arg:    family_record_types (osid.type.Type[]): array of family
                record types
        :return: (osid.relationship.FamilyForm) - the family form
        :raises:  NullArgument - ``family_record_types is null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_family(family_form):
        Creates a new ``Family``.

        :arg:    family_form (osid.relationship.FamilyForm): the form for
                this ``Family``.
        :return: (osid.relationship.Family) - the new ``Family``
        :raises:  IllegalState - ``family_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``family_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``family_form`` did not originate from
                ``get_family_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_families():
        Tests if this user can update families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Family`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_family_form_for_update(family_id):
        Gets the family form for updating an existing family.

        A new family form should be requested for each update
        transaction.

        :arg:    family_id (osid.id.Id): the ``Id`` of the ``Family``
        :return: (osid.relationship.FamilyForm) - the family form
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_family(family_form):
        Updates an existing family.

        :arg:    family_form (osid.relationship.FamilyForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``family_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``family_id`` or ``family_form`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``family_form`` did not originate from
                ``get_family_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_families():
        Tests if this user can delete families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Family`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_family(family_id):
        Deletes a ``Family``.

        :arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                remove
        :raises:  NotFound - ``family_id`` not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_family_aliases():
        Tests if this user can manage ``Id`` aliases for families.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Family`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_family(family_id, alias_id):
        Adds an ``Id`` to a ``Family`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Family`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another family, it is
        reassigned to the given family ``Id``.

        :arg:    family_id (osid.id.Id): the ``Id`` of a ``Family``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``family_id`` not found
        :raises:  NullArgument - ``family_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Family Hierarchy Methods
------------------------

    .. py:method:: get_family_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_hierarchy_id


    .. py:method:: get_family_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_hierarchy


    .. py:method:: can_access_family_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_family_view():
        The returns from the family methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_family_view():
        A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_family_ids():
        Gets the root family ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root family ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_family_ids


    .. py:method:: get_root_families():
        Gets the root families in the family hierarchy.

        A node with no parents is an orphan. While all family ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: (osid.relationship.FamilyList) - the root families
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_families


    .. py:method:: has_parent_families(family_id):
        Tests if the ``Family`` has any parents.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if the family has parents,
                ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_family(id_, family_id):
        Tests if an ``Id`` is a direct parent of a family.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``family_id,``  ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``id`` or ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_family_ids(family_id):
        Gets the parent ``Ids`` of the given family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (osid.id.IdList) - the parent ``Ids`` of the family
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_families(family_id):
        Gets the parent families of the given ``id``.

        :arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                query
        :return: (osid.relationship.FamilyList) - the parent families of
                the ``id``
        :raises:  NotFound - a ``Family`` identified by ``Id is`` not
                found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_family(id_, family_id):
        Tests if an ``Id`` is an ancestor of a family.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``family_id,``  ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``id`` or ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_families(family_id):
        Tests if a family has any children.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if the ``family_id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_family(id_, family_id):
        Tests if a family is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``family_id,``  ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``id`` or ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_family_ids(family_id):
        Gets the child ``Ids`` of the given family.

        :arg:    family_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the family
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_families(family_id):
        Gets the child families of the given ``id``.

        :arg:    family_id (osid.id.Id): the ``Id`` of the ``Family`` to
                query
        :return: (osid.relationship.FamilyList) - the child families of
                the ``id``
        :raises:  NotFound - a ``Family`` identified by ``Id is`` not
                found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_family(id_, family_id):
        Tests if an ``Id`` is a descendant of a family.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``family_id,``  ``false`` otherwise
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``id`` or ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_family_node_ids(family_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given family.

        :arg:    family_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a family node
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_family_nodes(family_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given family.

        :arg:    family_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.relationship.FamilyNode) - a family node
        :raises:  NotFound - ``family_id`` is not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Family Hierarchy Design Methods
-------------------------------

    .. py:method:: get_family_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_hierarchy_id


    .. py:method:: get_family_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_hierarchy


    .. py:method:: can_modify_family_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_family(family_id):
        Adds a root family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :raises:  AlreadyExists - ``family_id`` is already in hierarchy
        :raises:  NotFound - ``family_id`` not found
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_family(family_id):
        Removes a root family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :raises:  NotFound - ``family_id`` not a root
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_family(family_id, child_id):
        Adds a child to a family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``family_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``family_id`` or ``child_id`` not found
        :raises:  NullArgument - ``family_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_family(family_id, child_id):
        Removes a child from a family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``family_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``family_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_families(family_id):
        Removes all children from a family.

        :arg:    family_id (osid.id.Id): the ``Id`` of a family
        :raises:  NotFound - ``family_id`` not in hierarchy
        :raises:  NullArgument - ``family_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






