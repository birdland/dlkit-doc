

Service Managers
================


Resource Manager
----------------

.. py:class:: ResourceManager(osid_managers.OsidManager, ResourceProfile, resource_managers.ResourceManager)
    The resource manager provides access to resource lookup and creation sessions and provides
    interoperability tests for various aspects of this service.


    The sessions included in this manager are:




      * ``ResourceLookupSession:`` a session to retrieve resources
      * ``ResourceQuerySession:`` a session to query resources
      * ``ResourceSearchSession:`` a session to search for resources
      * ``ResourceAdminSession:`` a session to create and delete
        resources
      * ``ResourceNotificationSession:`` a session to receive
        notifications pertaining to resource changes
      * ``ResourceBinSession:`` a session to look up resource to bin
        mappings
      * ``ResourceBinAssignmentSession:`` a session to manage resource
        to bin mappings
      * ``ResourceSmartBinSession:`` a session to manage smart resource
        bins
      * ``MembershipSession:`` a session to query memberships
      * ``GroupSession:`` a session to retrieve group memberships
      * ``GroupAssignmentSession:`` a session to manage groups
      * ``GroupNotificationSession:`` a session to retrieve
        notifications on changes to group membership
      * ``GroupHierarchySession:`` a session to view a group hierarchy
      * ``RsourceAgentSession:`` a session to retrieve ``Resource`` and
        ``Agent`` mappings
      * ``ResourceAgentAssignmentSession:`` a session to manage
        ``Resource`` and ``Agent`` mappings




      * ``ResourceRelationshipLookupSession:`` a session to retrieve
        resource relationships
      * ``ResourceRelationshipQuerySession:`` a session to query for
        resource relationships
      * ``ResourceRelationshipSearchSession:`` a session to search for
        resource relationships
      * ``ResourceRelationshipAdminSession:`` a session to create and
        delete resource relationships
      * ``ResourceRelationshipNotificationSession:`` a session to
        receive notifications pertaining to resource relationshipchanges
      * ``ResourceRelationshipBinSession:`` a session to look up
        resource relationship to bin mappings
      * ``ResourceRelationshipBinAssignmentSession:`` a session to
        manage resource relationship to bin mappings
      * ``ResourceRelationshipSmartBinSession:`` a session to manage
        smart resource relationship bins




      * ``BinLookupSession: a`` session to retrieve bins
      * ``BinQuerySession:`` a session to query bins
      * ``BinSearchSession:`` a session to search for bins
      * ``BinAdminSession:`` a session to create, update and delete bins
      * ``BinNotificationSession:`` a session to receive notifications
        pertaining to changes in bins
      * ``BinHierarchySession:`` a session to traverse bin hierarchies
      * ``BinHierarchyDesignSession:`` a session to manage bin
        hierarchies





    .. py:method:: get_resource_lookup_session():
        :noindex:


    .. py:attribute:: resource_lookup_session
        :noindex:


    .. py:method:: get_resource_lookup_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_query_session():
        :noindex:


    .. py:attribute:: resource_query_session
        :noindex:


    .. py:method:: get_resource_query_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_search_session():
        :noindex:


    .. py:attribute:: resource_search_session
        :noindex:


    .. py:method:: get_resource_search_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_admin_session():
        :noindex:


    .. py:attribute:: resource_admin_session
        :noindex:


    .. py:method:: get_resource_admin_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_notification_session(resource_receiver):
        :noindex:


    .. py:method:: get_resource_notification_session_for_bin(resource_receiver, bin_id):
        :noindex:


    .. py:method:: get_resource_bin_session():
        :noindex:


    .. py:attribute:: resource_bin_session
        :noindex:


    .. py:method:: get_resource_bin_assignment_session():
        :noindex:


    .. py:attribute:: resource_bin_assignment_session
        :noindex:


    .. py:method:: get_resource_smart_bin_session(bin_id):
        :noindex:


    .. py:method:: get_membership_session():
        :noindex:


    .. py:attribute:: membership_session
        :noindex:


    .. py:method:: get_membership_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_group_session():
        :noindex:


    .. py:attribute:: group_session
        :noindex:


    .. py:method:: get_group_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_group_assignment_session():
        :noindex:


    .. py:attribute:: group_assignment_session
        :noindex:


    .. py:method:: get_group_assignment_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_group_notification_session(group_rceeiver):
        :noindex:


    .. py:method:: get_group_notification_session_for_bin(group_rceeiver, bin_id):
        :noindex:


    .. py:method:: get_group_hierarchy_session():
        :noindex:


    .. py:attribute:: group_hierarchy_session
        :noindex:


    .. py:method:: get_group_hierarchy_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_agent_session():
        :noindex:


    .. py:attribute:: resource_agent_session
        :noindex:


    .. py:method:: get_resource_agent_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_agent_assignment_session():
        :noindex:


    .. py:attribute:: resource_agent_assignment_session
        :noindex:


    .. py:method:: get_resource_agent_assignment_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_lookup_session():
        :noindex:


    .. py:attribute:: resource_relationship_lookup_session
        :noindex:


    .. py:method:: get_resource_relationship_lookup_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_query_session():
        :noindex:


    .. py:attribute:: resource_relationship_query_session
        :noindex:


    .. py:method:: get_resource_relationship_query_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_search_session():
        :noindex:


    .. py:attribute:: resource_relationship_search_session
        :noindex:


    .. py:method:: get_resource_relationship_search_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_admin_session():
        :noindex:


    .. py:attribute:: resource_relationship_admin_session
        :noindex:


    .. py:method:: get_resource_relationship_admin_session_for_bin(bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_notification_session(resource_relationship_receiver):
        :noindex:


    .. py:method:: get_resource_relationship_notification_session_for_bin(resource_relationship_receiver, bin_id):
        :noindex:


    .. py:method:: get_resource_relationship_bin_session():
        :noindex:


    .. py:attribute:: resource_relationship_bin_session
        :noindex:


    .. py:method:: get_resource_relationship_bin_assignment_session():
        :noindex:


    .. py:attribute:: resource_relationship_bin_assignment_session
        :noindex:


    .. py:method:: get_resource_relationship_smart_bin_session(bin_id):
        :noindex:


    .. py:method:: get_bin_lookup_session():
        :noindex:


    .. py:attribute:: bin_lookup_session
        :noindex:


    .. py:method:: get_bin_query_session():
        :noindex:


    .. py:attribute:: bin_query_session
        :noindex:


    .. py:method:: get_bin_search_session():
        :noindex:


    .. py:attribute:: bin_search_session
        :noindex:


    .. py:method:: get_bin_admin_session():
        :noindex:


    .. py:attribute:: bin_admin_session
        :noindex:


    .. py:method:: get_bin_notification_session(bin_receiver):
        :noindex:


    .. py:method:: get_bin_hierarchy_session():
        :noindex:


    .. py:attribute:: bin_hierarchy_session
        :noindex:


    .. py:method:: get_bin_hierarchy_design_session():
        :noindex:


    .. py:attribute:: bin_hierarchy_design_session
        :noindex:


    .. py:method:: get_resource_batch_manager():
        :noindex:


    .. py:attribute:: resource_batch_manager
        :noindex:


    .. py:method:: get_resource_demographic_manager():
        :noindex:


    .. py:attribute:: resource_demographic_manager
        :noindex:




Resource Lookup Methods
-----------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_lookup_resources():
        Tests if this user can perform ``Resource`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_resource_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_resource_view():
        A complete view of the ``Resource`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_bin_view():
        Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bin_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_resource(resource_id):
        Gets the ``Resource`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Resource`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Resource`` and retained for
        compatibility.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to retrieve
        :return: (osid.resource.Resource) - the returned ``Resource``
        :raises:  NotFound - no ``Resource`` found with the given ``Id``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_ids(resource_ids):
        Gets a ``ResourceList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the resources
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Resources`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    resource_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``resource_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_genus_type(resource_genus_type):
        Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` which does not
            include resources of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :arg:    resource_genus_type (osid.type.Type): a resource genus
                type
        :return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        :raises:  NullArgument - ``resource_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_parent_genus_type(resource_genus_type):
        Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` and include any
            additional resources with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :arg:    resource_genus_type (osid.type.Type): a resource genus
                type
        :return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        :raises:  NullArgument - ``resource_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_record_type(resource_record_type):
        Gets a ``ResourceList`` containing the given resource record ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :arg:    resource_record_type (osid.type.Type): a resource record
                type
        :return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        :raises:  NullArgument - ``resource_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources():
        Gets all ``Resources``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :return: (osid.resource.ResourceList) - a list of ``Resources``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: resources




Resource Query Methods
----------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_search_resources():
        Tests if this user can perform ``Resource`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bin_view():
        Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bin_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_resource_query():
        Gets a resource query.

        The returned query will not have an extension query.

        :return: (osid.resource.ResourceQuery) - the resource query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: resource_query


    .. py:method:: get_resources_by_query(resource_query):
        Gets a list of ``Resources`` matching the given resource query.

        :arg:    resource_query (osid.resource.ResourceQuery): the
                resource query
        :return: (osid.resource.ResourceList) - the returned
                ``ResourceList``
        :raises:  NullArgument - ``resource_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``resource_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Resource Search Methods
-----------------------

    .. py:method:: get_resource_search():
        Gets a resource search.

        :return: (osid.resource.ResourceSearch) - the resource search
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: resource_search


    .. py:method:: get_resource_search_order():
        Gets a resource search order.

        The ``ResourceSearchOrder`` is supplied to a ``ResourceSearch``
        to specify the ordering of results.

        :return: (osid.resource.ResourceSearchOrder) - the resource
                search order
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: resource_search_order


    .. py:method:: get_resources_by_search(resource_query, resource_search):
        Gets the search results matching the given search query using the given search.

        :arg:    resource_query (osid.resource.ResourceQuery): the
                resource query
        :arg:    resource_search (osid.resource.ResourceSearch): the
                resource search
        :return: (osid.resource.ResourceSearchResults) - the resource
                search results
        :raises:  NullArgument - ``resource_query`` or ``resource_search``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``resource_query`` or ``resource_search``
                is not of this service
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_query_from_inspector(resource_query_inspector):
        Gets a resource query from an inspector.

        The inspector is available from a ``ResourceSearchResults``.

        :arg:    resource_query_inspector
                (osid.resource.ResourceQueryInspector): a resource query
                inspector
        :return: (osid.resource.ResourceQuery) - the resource query
        :raises:  NullArgument - ``resource_query_inspector`` is ``null``
        :raises:  Unsupported - ``resource_query_inspector`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*






Resource Admin Methods
----------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_create_resources():
        Tests if this user can create ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Resource`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_resource_with_record_types(resource_record_types):
        Tests if this user can create a single ``Resource`` using the desired record types.

        While ``ResourceManager.getResourceRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Resource``.
        Providing an empty array tests if a ``Resource`` can be created
        with no records.

        :arg:    resource_record_types (osid.type.Type[]): array of
                resource record types
        :return: (boolean) - ``true`` if ``Resource`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``resource_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_form_for_create(resource_record_types):
        Gets the resource form for creating new resources.

        A new form should be requested for each create transaction.

        :arg:    resource_record_types (osid.type.Type[]): array of
                resource record types
        :return: (osid.resource.ResourceForm) - the resource form
        :raises:  NullArgument - ``resource_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_resource(resource_form):
        Creates a new ``Resource``.

        :arg:    resource_form (osid.resource.ResourceForm): the form for
                this ``Resource``
        :return: (osid.resource.Resource) - the new ``Resource``
        :raises:  IllegalState - ``resource_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``resource_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``resource_form`` did not originate from
                ``get_resource_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_resources():
        Tests if this user can update ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Resource`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_form_for_update(resource_id):
        Gets the resource form for updating an existing resource.

        A new resource form should be requested for each update
        transaction.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :return: (osid.resource.ResourceForm) - the resource form
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_resource(resource_form):
        Updates an existing resource.

        :arg:    resource_form (osid.resource.ResourceForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``resource_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``resource_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``resource_form`` did not originate from
                ``get_resource_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_resources():
        Tests if this user can delete ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Resource`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_resource(resource_id):
        Deletes a ``Resource``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to remove
        :raises:  NotFound - ``resource_id`` not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_resource_aliases():
        Tests if this user can manage ``Id`` aliases for ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Resource`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_resource(resource_id, alias_id):
        Adds an ``Id`` to a ``Resource`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Resource`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another resource it is
        reassigned to the given resource ``Id``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of a ``Resource``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``resource_id`` not found
        :raises:  NullArgument - ``alias_id`` or ``resource_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Notification Methods
-----------------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_register_for_resource_notifications():
        Tests if this user can register for ``Resource`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: (boolean) - ``false`` if notification methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bin_view():
        Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bin_view():
        Isolates the view for methods in this session.

        An isolated view restricts notifications to this bin only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: register_for_new_resources():
        Register for notifications of new resources.

        ``ResourceReceiver.newResources()`` is invoked when a new
        ``Resource`` is appears in this bin.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_resources():
        Registers for notification of updated resources.

        ``ResourceReceiver.changedResources()`` is invoked when a
        resource in this bin is changed.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_resource(resource_id):
        Registers for notification of an updated resource.

        ``ResourceReceiver.changedResources()`` is invoked when the
        specified resource in this bin is changed.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to monitor
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_resources():
        Registers for notification of deleted resources.

        ``ResourceReceiver.deletedResources()`` is invoked when a
        resource is deleted or removed from this bin.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_resource(resource_id):
        Registers for notification of a deleted resource.

        ``ResourceReceiver.deletedResources()`` is invoked when the
        specified resource is deleted or removed from this bin.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to monitor
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reliable_resource_notifications():
        Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: unreliable_resource_notifications():
        Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: acknowledge_resource_notification(notification_id):
        Acknowledge an resource notification.

        :arg:    notification_id (osid.id.Id): the ``Id`` of the
                notification
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Bin Methods
--------------------

    .. py:method:: use_comparative_bin_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bin_view():
        A complete view of the ``Resource`` and ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: can_lookup_resource_bin_mappings():
        Tests if this user can perform lookups of resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_ids_by_bin(bin_id):
        Gets the list of ``Resource``  ``Ids`` associated with a ``Bin``.

        :arg:    bin_id (osid.id.Id): ``Id`` of a ``Bin``
        :return: (osid.id.IdList) - list of related resource ``Ids``
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_bin(bin_id):
        Gets the list of ``Resources`` associated with a ``Bin``.

        :arg:    bin_id (osid.id.Id): ``Id`` of a ``Bin``
        :return: (osid.resource.ResourceList) - list of related resources
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_ids_by_bins(bin_ids):
        Gets the list of ``Resource Ids`` corresponding to a list of ``Bin`` objects.

        :arg:    bin_ids (osid.id.IdList): list of bin ``Ids``
        :return: (osid.id.IdList) - list of resource ``Ids``
        :raises:  NullArgument - ``bin_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_bins(bin_ids):
        Gets the list of ``Resources`` corresponding to a list of ``Bins``.

        :arg:    bin_ids (osid.id.IdList): list of bin ``Ids``
        :return: (osid.resource.ResourceList) - list of resources
        :raises:  NullArgument - ``bin_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_ids_by_resource(resource_id):
        Gets the list of ``Bin``  ``Ids`` mapped to a ``Resource``.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.id.IdList) - list of bin ``Ids``
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_resource(resource_id):
        Gets the list of ``Bin`` objects mapped to a ``Resource``.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.resource.BinList) - list of bins
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Bin Assignment Methods
-------------------------------

    .. py:method:: can_assign_resources():
        Tests if this user can alter resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_resources_to_bin(bin_id):
        Tests if this user can alter resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied`` . This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bin_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bin_ids(bin_id):
        Gets a list of bins including and under the given bin node in which any resource can be
            assigned.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :return: (osid.id.IdList) - list of assignable bin ``Ids``
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bin_ids_for_resource(bin_id, resource_id):
        Gets a list of bins including and under the given bin node in which a specific resource can
            be assigned.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :return: (osid.id.IdList) - list of assignable bin ``Ids``
        :raises:  NullArgument - ``bin_id`` or ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_resource_to_bin(resource_id, bin_id):
        Adds an existing ``Resource`` to a ``Bin``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :raises:  AlreadyExists - ``resource_id`` is already assigned to
                ``bin_id``
        :raises:  NotFound - ``resource_id`` or ``bin_id`` not found
        :raises:  NullArgument - ``resource_id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_resource_from_bin(resource_id, bin_id):
        Removes a ``Resource`` from a ``Bin``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :raises:  NotFound - ``resource_id`` or ``bin_id`` not found or
                ``resource_id`` not assigned to ``bin_id``
        :raises:  NullArgument - ``resource_id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Agent Methods
----------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_lookup_resource_agent_mappings():
        Tests if this user can perform lookups of resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_agent_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_agent_view():
        A complete view of the ``Agent`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_bin_view():
        Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bin_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_resource_id_by_agent(agent_id):
        Gets the ``Resource``  ``Id`` associated with the given agent.

        :arg:    agent_id (osid.id.Id): ``Id`` of the ``Agent``
        :return: (osid.id.Id) - associated resource
        :raises:  NotFound - ``agent_id`` is not found
        :raises:  NullArgument - ``agent_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_by_agent(agent_id):
        Gets the ``Resource`` associated with the given agent.

        :arg:    agent_id (osid.id.Id): ``Id`` of the ``Agent``
        :return: (osid.resource.Resource) - associated resource
        :raises:  NotFound - ``agent_id`` is not found
        :raises:  NullArgument - ``agent_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_agent_ids_by_resource(resource_id):
        Gets the list of ``Agent``  ``Ids`` mapped to a ``Resource``.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.id.IdList) - list of agent ``Ids``
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_agents_by_resource(resource_id):
        Gets the list of ``Agents`` mapped to a ``Resource``.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.authentication.AgentList) - list of agents
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Agent Assignment Methods
---------------------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_assign_agents():
        Tests if this user can alter resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_agents_to_resource(resource_id):
        Tests if this user can alter resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_agent_to_resource(agent_id, resource_id):
        Adds an existing ``Agent`` to a ``Resource``.

        :arg:    agent_id (osid.id.Id): the ``Id`` of the ``Agent``
        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :raises:  AlreadyExists - ``agent_id`` is already assigned to
                ``resource_id``
        :raises:  NotFound - ``agent_id`` or ``resource_id`` not found
        :raises:  NullArgument - ``agent_id`` or ``resource_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_agent_from_resource(agent_id, resource_id):
        Removes an ``Agent`` from a ``Resource``.

        :arg:    agent_id (osid.id.Id): the ``Id`` of the ``Agent``
        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :raises:  NotFound - ``agent_id`` or ``resource_id`` not found or
                ``agent_id`` not assigned to ``resource_id``
        :raises:  NullArgument - ``agent_id`` or ``resource_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bin Lookup Methods
------------------

    .. py:method:: can_lookup_bins():
        Tests if this user can perform ``Bin`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bin_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bin_view():
        A complete view of the ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_bin(bin_id):
        Gets the ``Bin`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bin`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bin`` and retained for compatibility.

        :arg:    bin_id (osid.id.Id): ``Id`` of the ``Bin``
        :return: (osid.resource.Bin) - the bin
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_bins_by_ids(bin_ids):
        Gets a ``BinList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the bins
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bins`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    bin_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``bin_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_genus_type(bin_genus_type):
        Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins
            of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :arg:    bin_genus_type (osid.type.Type): a bin genus type
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NullArgument - ``bin_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_parent_genus_type(bin_genus_type):
        Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional
            bins with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :arg:    bin_genus_type (osid.type.Type): a bin genus type
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NullArgument - ``bin_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_record_type(bin_record_type):
        Gets a ``BinList`` containing the given bin record ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :arg:    bin_record_type (osid.type.Type): a bin record type
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NullArgument - ``bin_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_provider(resource_id):
        Gets a ``BinList`` from the given provider.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins():
        Gets all ``Bins``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :return: (osid.resource.BinList) - a list of ``Bins``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bins




Bin Query Methods
-----------------

    .. py:method:: can_search_bins():
        Tests if this user can perform ``Bin`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_query():
        Gets a bin query.

        The returned query will not have an extension query.

        :return: (osid.resource.BinQuery) - the bin query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_query


    .. py:method:: get_bins_by_query(bin_query):
        Gets a list of ``Bins`` matching the given bin query.

        :arg:    bin_query (osid.resource.BinQuery): the bin query
        :return: (osid.resource.BinList) - the returned ``BinList``
        :raises:  NullArgument - ``bin_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - a ``bin_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Bin Admin Methods
-----------------

    .. py:method:: can_create_bins():
        Tests if this user can create ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bin`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_bin_with_record_types(bin_record_types):
        Tests if this user can create a single ``Bin`` using the desired record types.

        While ``ResourceManager.getBinRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bin``.
        Providing an empty array tests if a ``Bin`` can be created with
        no records.

        :arg:    bin_record_types (osid.type.Type[]): array of bin record
                types
        :return: (boolean) - ``true`` if ``Bin`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``bin_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_form_for_create(bin_record_types):
        Gets the bin form for creating new bins.

        :arg:    bin_record_types (osid.type.Type[]): array of bin record
                types
        :return: (osid.resource.BinForm) - the bin form
        :raises:  NullArgument - ``bin_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_bin(bin_form):
        Creates a new ``Bin``.

        :arg:    bin_form (osid.resource.BinForm): the form for this
                ``Bin``
        :return: (osid.resource.Bin) - the new ``Bin``
        :raises:  IllegalState - ``bin_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``bin_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``bin_form`` did not originate from
                ``get_bin_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_bins():
        Tests if this user can update ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bin`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_form_for_update(bin_id):
        Gets the bin form for updating an existing bin.

        A new bin form should be requested for each update transaction.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :return: (osid.resource.BinForm) - the bin form
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_bin(bin_form):
        Updates an existing bin.

        :arg:    bin_form (osid.resource.BinForm): the form containing
                the elements to be updated
        :raises:  IllegalState - ``bin_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``bin_id`` or ``bin_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``bin_form`` did not originate from
                ``get_bin_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_bins():
        Tests if this user can delete ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bin`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_bin(bin_id):
        Deletes a ``Bin``.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin`` to remove
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_bin_aliases():
        Tests if this user can manage ``Id`` aliases for ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Bin`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_bin(bin_id, alias_id):
        Adds an ``Id`` to a ``Bin`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Bin`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another bin, it is reassigned to the
        given bin ``Id``.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a ``Bin``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bin Hierarchy Methods
---------------------

    .. py:method:: get_bin_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_hierarchy_id


    .. py:method:: get_bin_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_hierarchy


    .. py:method:: can_access_bin_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bin_view():
        The returns from the bin methods may omit or translate elements based on this session, such
            as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bin_view():
        A complete view of the ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_bin_ids():
        Gets the root bin ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root bin ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_bin_ids


    .. py:method:: get_root_bins():
        Gets the root bins in the bin hierarchy.

        A node with no parents is an orphan. While all bin ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: (osid.resource.BinList) - the root bins
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_bins


    .. py:method:: has_parent_bins(bin_id):
        Tests if the ``Bin`` has any parents.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if the bin has parents, ``false``
                otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_bin(id_, bin_id):
        Tests if an ``Id`` is a direct parent of a bin.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``bin_id,``  ``false`` otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_bin_ids(bin_id):
        Gets the parent ``Ids`` of the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (osid.id.IdList) - the parent ``Ids`` of the bin
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_bins(bin_id):
        Gets the parents of the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :return: (osid.resource.BinList) - the parents of the bin
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_bin(id_, bin_id):
        Tests if an ``Id`` is an ancestor of a bin.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``bin_id,``  ``false`` otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_bins(bin_id):
        Tests if a bin has any children.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if the ``bin_id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_bin(id_, bin_id):
        Tests if a bin is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``bin_id,``  ``false`` otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_bin_ids(bin_id):
        Gets the child ``Ids`` of the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the bin
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_bins(bin_id):
        Gets the children of the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :return: (osid.resource.BinList) - the children of the bin
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_bin(id_, bin_id):
        Tests if an ``Id`` is a descendant of a bin.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``bin_id,``  ``false`` otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_bin_node_ids(bin_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a bin node
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_nodes(bin_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.resource.BinNode) - a bin node
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bin Hierarchy Design Methods
----------------------------

    .. py:method:: get_bin_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_hierarchy_id


    .. py:method:: get_bin_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_hierarchy


    .. py:method:: can_modify_bin_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_bin(bin_id):
        Adds a root bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :raises:  AlreadyExists - ``bin_id`` is already in hierarchy
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_bin(bin_id):
        Removes a root bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :raises:  NotFound - ``bin_id`` not a root
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_bin(bin_id, child_id):
        Adds a child to a bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``bin_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``bin_id`` or ``child_id`` not found
        :raises:  NullArgument - ``bin_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_bin(bin_id, child_id):
        Removes a child from a bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``bin_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``bin_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_bins(bin_id):
        Removes all children from a bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :raises:  NotFound - ``bin_id`` not in hierarchy
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Proxy Manager
----------------------

.. py:class:: ResourceProxyManager(osid_managers.OsidProxyManager, ResourceProfile, resource_managers.ResourceProxyManager)
    The resource manager provides access to resource lookup and creation session and provides
    interoperability tests for various aspects of this service.


    Methods in this manager accept a ``Proxy``. The sessions included in
    this manager are:




      * ``ResourceLookupSession:`` a session to retrieve resources
      * ``ResourceQuerySession:`` a session to query resources
      * ``ResourceSearchSession:`` a session to search for resources
      * ``ResourceAdminSession:`` a session to create and delete
        resources
      * ``ResourceNotificationSession:`` a session to receive
        notifications pertaining to resource changes
      * ``ResourceBinSession:`` a session to look up resource to bin
        mappings
      * ``ResourceBinAssignmentSession:`` a session to manage resource
        to bin mappings
      * ``ResourceSmartBinSession:`` a session to manage smart resource
        bins
      * ``MembershipSession:`` a session to query memberships
      * ``GroupSession:`` a session to retrieve group memberships
      * ``GroupAssignmentSession:`` a session to manage groups
      * ``GroupNotificationSession:`` a session to retrieve
        notifications on changes to group membership
      * ``GroupHierarchySession:`` a session to view a group hierarchy
      * ``RsourceAgentSession:`` a session to retrieve ``Resource`` and
        ``Agent`` mappings
      * ``ResourceAgentAssignmentSession:`` a session to manage
        ``Resource`` and ``Agent`` mappings




      * ``ResourceRelationshipLookupSession:`` a session to retrieve
        resource relationships
      * ``ResourceRelationshipQuerySession:`` a session to query for
        resource relationships
      * ``ResourceRelationshipSearchSession:`` a session to search for
        resource relationships
      * ``ResourceRelationshipAdminSession:`` a session to create and
        delete resource relationships
      * ``ResourceRelationshipNotificationSession:`` a session to
        receive notifications pertaining to resource relationshipchanges
      * ``ResourceRelationshipBinSession:`` a session to look up
        resource relationship to bin mappings
      * ``ResourceRelationshipBinAssignmentSession:`` a session to
        manage resource relationship to bin mappings
      * ``ResourceRelationshipSmartBinSession:`` a session to manage
        smart resource relationship bins




      * ``BinLookupSession: a`` session to retrieve bins
      * ``BinQuerySession:`` a session to query bins
      * ``BinSearchSession:`` a session to search for bins
      * ``BinAdminSession:`` a session to create, update and delete bins
      * ``BinNotificationSession:`` a session to receive notifications
        pertaining to changes in bins
      * ``BinHierarchySession:`` a session to traverse bin hierarchies
      * ``BinHierarchyDesignSession:`` a session to manage bin
        hierarchies





    .. py:method:: get_resource_lookup_session(proxy):
        :noindex:


    .. py:method:: get_resource_lookup_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_query_session(proxy):
        :noindex:


    .. py:method:: get_resource_query_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_search_session(proxy):
        :noindex:


    .. py:method:: get_resource_search_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_admin_session(proxy):
        :noindex:


    .. py:method:: get_resource_admin_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_notification_session(resource_receiver, proxy):
        :noindex:


    .. py:method:: get_resource_notification_session_for_bin(resource_receiver, bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_bin_session(proxy):
        :noindex:


    .. py:method:: get_resource_bin_assignment_session(proxy):
        :noindex:


    .. py:method:: get_resource_smart_bin_session(bin_id, proxy):
        :noindex:


    .. py:method:: get_membership_session(proxy):
        :noindex:


    .. py:method:: get_membership_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_group_session(proxy):
        :noindex:


    .. py:method:: get_group_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_group_assignment_session(proxy):
        :noindex:


    .. py:method:: get_group_assignment_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_group_notification_session(group_rceeiver, proxy):
        :noindex:


    .. py:method:: get_group_notification_session_for_bin(group_rceeiver, bin_id, proxy):
        :noindex:


    .. py:method:: get_group_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_group_hierarchy_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_agent_session(proxy):
        :noindex:


    .. py:method:: get_resource_agent_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_agent_assignment_session(proxy):
        :noindex:


    .. py:method:: get_resource_agent_assignment_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_lookup_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_lookup_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_query_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_query_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_search_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_search_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_admin_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_admin_session_for_bin(bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_notification_session(resource_relationship_receiver, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_notification_session_for_bin(resource_relationship_receiver, bin_id, proxy):
        :noindex:


    .. py:method:: get_resource_relationship_bin_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_bin_assignment_session(proxy):
        :noindex:


    .. py:method:: get_resource_relationship_smart_bin_session(bin_id, proxy):
        :noindex:


    .. py:method:: get_bin_lookup_session(proxy):
        :noindex:


    .. py:method:: get_bin_query_session(proxy):
        :noindex:


    .. py:method:: get_bin_search_session(proxy):
        :noindex:


    .. py:method:: get_bin_admin_session(proxy):
        :noindex:


    .. py:method:: get_bin_notification_session(bin_receiver, proxy):
        :noindex:


    .. py:method:: get_bin_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_bin_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_resource_batch_proxy_manager():
        :noindex:


    .. py:attribute:: resource_batch_proxy_manager
        :noindex:


    .. py:method:: get_resource_demographic_proxy_manager():
        :noindex:


    .. py:attribute:: resource_demographic_proxy_manager
        :noindex:




Resource Lookup Methods
-----------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_lookup_resources():
        Tests if this user can perform ``Resource`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_resource_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_resource_view():
        A complete view of the ``Resource`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_bin_view():
        Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bin_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_resource(resource_id):
        Gets the ``Resource`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Resource`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Resource`` and retained for
        compatibility.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to retrieve
        :return: (osid.resource.Resource) - the returned ``Resource``
        :raises:  NotFound - no ``Resource`` found with the given ``Id``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_ids(resource_ids):
        Gets a ``ResourceList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the resources
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Resources`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    resource_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``resource_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_genus_type(resource_genus_type):
        Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` which does not
            include resources of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :arg:    resource_genus_type (osid.type.Type): a resource genus
                type
        :return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        :raises:  NullArgument - ``resource_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_parent_genus_type(resource_genus_type):
        Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` and include any
            additional resources with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :arg:    resource_genus_type (osid.type.Type): a resource genus
                type
        :return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        :raises:  NullArgument - ``resource_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_record_type(resource_record_type):
        Gets a ``ResourceList`` containing the given resource record ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :arg:    resource_record_type (osid.type.Type): a resource record
                type
        :return: (osid.resource.ResourceList) - the returned ``Resource``
                list
        :raises:  NullArgument - ``resource_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources():
        Gets all ``Resources``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :return: (osid.resource.ResourceList) - a list of ``Resources``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: resources




Resource Query Methods
----------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_search_resources():
        Tests if this user can perform ``Resource`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bin_view():
        Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bin_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_resource_query():
        Gets a resource query.

        The returned query will not have an extension query.

        :return: (osid.resource.ResourceQuery) - the resource query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: resource_query


    .. py:method:: get_resources_by_query(resource_query):
        Gets a list of ``Resources`` matching the given resource query.

        :arg:    resource_query (osid.resource.ResourceQuery): the
                resource query
        :return: (osid.resource.ResourceList) - the returned
                ``ResourceList``
        :raises:  NullArgument - ``resource_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``resource_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Resource Search Methods
-----------------------

    .. py:method:: get_resource_search():
        Gets a resource search.

        :return: (osid.resource.ResourceSearch) - the resource search
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: resource_search


    .. py:method:: get_resource_search_order():
        Gets a resource search order.

        The ``ResourceSearchOrder`` is supplied to a ``ResourceSearch``
        to specify the ordering of results.

        :return: (osid.resource.ResourceSearchOrder) - the resource
                search order
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: resource_search_order


    .. py:method:: get_resources_by_search(resource_query, resource_search):
        Gets the search results matching the given search query using the given search.

        :arg:    resource_query (osid.resource.ResourceQuery): the
                resource query
        :arg:    resource_search (osid.resource.ResourceSearch): the
                resource search
        :return: (osid.resource.ResourceSearchResults) - the resource
                search results
        :raises:  NullArgument - ``resource_query`` or ``resource_search``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``resource_query`` or ``resource_search``
                is not of this service
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_query_from_inspector(resource_query_inspector):
        Gets a resource query from an inspector.

        The inspector is available from a ``ResourceSearchResults``.

        :arg:    resource_query_inspector
                (osid.resource.ResourceQueryInspector): a resource query
                inspector
        :return: (osid.resource.ResourceQuery) - the resource query
        :raises:  NullArgument - ``resource_query_inspector`` is ``null``
        :raises:  Unsupported - ``resource_query_inspector`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*






Resource Admin Methods
----------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_create_resources():
        Tests if this user can create ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Resource`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_resource_with_record_types(resource_record_types):
        Tests if this user can create a single ``Resource`` using the desired record types.

        While ``ResourceManager.getResourceRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Resource``.
        Providing an empty array tests if a ``Resource`` can be created
        with no records.

        :arg:    resource_record_types (osid.type.Type[]): array of
                resource record types
        :return: (boolean) - ``true`` if ``Resource`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``resource_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_form_for_create(resource_record_types):
        Gets the resource form for creating new resources.

        A new form should be requested for each create transaction.

        :arg:    resource_record_types (osid.type.Type[]): array of
                resource record types
        :return: (osid.resource.ResourceForm) - the resource form
        :raises:  NullArgument - ``resource_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_resource(resource_form):
        Creates a new ``Resource``.

        :arg:    resource_form (osid.resource.ResourceForm): the form for
                this ``Resource``
        :return: (osid.resource.Resource) - the new ``Resource``
        :raises:  IllegalState - ``resource_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``resource_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``resource_form`` did not originate from
                ``get_resource_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_resources():
        Tests if this user can update ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Resource`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_form_for_update(resource_id):
        Gets the resource form for updating an existing resource.

        A new resource form should be requested for each update
        transaction.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :return: (osid.resource.ResourceForm) - the resource form
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_resource(resource_form):
        Updates an existing resource.

        :arg:    resource_form (osid.resource.ResourceForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``resource_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``resource_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``resource_form`` did not originate from
                ``get_resource_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_resources():
        Tests if this user can delete ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Resource`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_resource(resource_id):
        Deletes a ``Resource``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to remove
        :raises:  NotFound - ``resource_id`` not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_resource_aliases():
        Tests if this user can manage ``Id`` aliases for ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Resource`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_resource(resource_id, alias_id):
        Adds an ``Id`` to a ``Resource`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Resource`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another resource it is
        reassigned to the given resource ``Id``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of a ``Resource``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``resource_id`` not found
        :raises:  NullArgument - ``alias_id`` or ``resource_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Notification Methods
-----------------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_register_for_resource_notifications():
        Tests if this user can register for ``Resource`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: (boolean) - ``false`` if notification methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_bin_view():
        Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bin_view():
        Isolates the view for methods in this session.

        An isolated view restricts notifications to this bin only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: register_for_new_resources():
        Register for notifications of new resources.

        ``ResourceReceiver.newResources()`` is invoked when a new
        ``Resource`` is appears in this bin.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_resources():
        Registers for notification of updated resources.

        ``ResourceReceiver.changedResources()`` is invoked when a
        resource in this bin is changed.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_resource(resource_id):
        Registers for notification of an updated resource.

        ``ResourceReceiver.changedResources()`` is invoked when the
        specified resource in this bin is changed.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to monitor
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_resources():
        Registers for notification of deleted resources.

        ``ResourceReceiver.deletedResources()`` is invoked when a
        resource is deleted or removed from this bin.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_resource(resource_id):
        Registers for notification of a deleted resource.

        ``ResourceReceiver.deletedResources()`` is invoked when the
        specified resource is deleted or removed from this bin.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
                to monitor
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reliable_resource_notifications():
        Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: unreliable_resource_notifications():
        Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: acknowledge_resource_notification(notification_id):
        Acknowledge an resource notification.

        :arg:    notification_id (osid.id.Id): the ``Id`` of the
                notification
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Bin Methods
--------------------

    .. py:method:: use_comparative_bin_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bin_view():
        A complete view of the ``Resource`` and ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: can_lookup_resource_bin_mappings():
        Tests if this user can perform lookups of resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_ids_by_bin(bin_id):
        Gets the list of ``Resource``  ``Ids`` associated with a ``Bin``.

        :arg:    bin_id (osid.id.Id): ``Id`` of a ``Bin``
        :return: (osid.id.IdList) - list of related resource ``Ids``
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_bin(bin_id):
        Gets the list of ``Resources`` associated with a ``Bin``.

        :arg:    bin_id (osid.id.Id): ``Id`` of a ``Bin``
        :return: (osid.resource.ResourceList) - list of related resources
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_ids_by_bins(bin_ids):
        Gets the list of ``Resource Ids`` corresponding to a list of ``Bin`` objects.

        :arg:    bin_ids (osid.id.IdList): list of bin ``Ids``
        :return: (osid.id.IdList) - list of resource ``Ids``
        :raises:  NullArgument - ``bin_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resources_by_bins(bin_ids):
        Gets the list of ``Resources`` corresponding to a list of ``Bins``.

        :arg:    bin_ids (osid.id.IdList): list of bin ``Ids``
        :return: (osid.resource.ResourceList) - list of resources
        :raises:  NullArgument - ``bin_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_ids_by_resource(resource_id):
        Gets the list of ``Bin``  ``Ids`` mapped to a ``Resource``.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.id.IdList) - list of bin ``Ids``
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_resource(resource_id):
        Gets the list of ``Bin`` objects mapped to a ``Resource``.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.resource.BinList) - list of bins
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Bin Assignment Methods
-------------------------------

    .. py:method:: can_assign_resources():
        Tests if this user can alter resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_resources_to_bin(bin_id):
        Tests if this user can alter resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied`` . This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``bin_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bin_ids(bin_id):
        Gets a list of bins including and under the given bin node in which any resource can be
            assigned.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :return: (osid.id.IdList) - list of assignable bin ``Ids``
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_bin_ids_for_resource(bin_id, resource_id):
        Gets a list of bins including and under the given bin node in which a specific resource can
            be assigned.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :return: (osid.id.IdList) - list of assignable bin ``Ids``
        :raises:  NullArgument - ``bin_id`` or ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_resource_to_bin(resource_id, bin_id):
        Adds an existing ``Resource`` to a ``Bin``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :raises:  AlreadyExists - ``resource_id`` is already assigned to
                ``bin_id``
        :raises:  NotFound - ``resource_id`` or ``bin_id`` not found
        :raises:  NullArgument - ``resource_id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_resource_from_bin(resource_id, bin_id):
        Removes a ``Resource`` from a ``Bin``.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :raises:  NotFound - ``resource_id`` or ``bin_id`` not found or
                ``resource_id`` not assigned to ``bin_id``
        :raises:  NullArgument - ``resource_id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Agent Methods
----------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_lookup_resource_agent_mappings():
        Tests if this user can perform lookups of resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_agent_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_agent_view():
        A complete view of the ``Agent`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_bin_view():
        Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_bin_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_resource_id_by_agent(agent_id):
        Gets the ``Resource``  ``Id`` associated with the given agent.

        :arg:    agent_id (osid.id.Id): ``Id`` of the ``Agent``
        :return: (osid.id.Id) - associated resource
        :raises:  NotFound - ``agent_id`` is not found
        :raises:  NullArgument - ``agent_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_resource_by_agent(agent_id):
        Gets the ``Resource`` associated with the given agent.

        :arg:    agent_id (osid.id.Id): ``Id`` of the ``Agent``
        :return: (osid.resource.Resource) - associated resource
        :raises:  NotFound - ``agent_id`` is not found
        :raises:  NullArgument - ``agent_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_agent_ids_by_resource(resource_id):
        Gets the list of ``Agent``  ``Ids`` mapped to a ``Resource``.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.id.IdList) - list of agent ``Ids``
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_agents_by_resource(resource_id):
        Gets the list of ``Agents`` mapped to a ``Resource``.

        :arg:    resource_id (osid.id.Id): ``Id`` of a ``Resource``
        :return: (osid.authentication.AgentList) - list of agents
        :raises:  NotFound - ``resource_id`` is not found
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Resource Agent Assignment Methods
---------------------------------

    .. py:method:: get_bin_id():
        Gets the ``Bin``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Bin Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_id


    .. py:method:: get_bin():
        Gets the ``Bin`` associated with this session.

        :return: (osid.resource.Bin) - the ``Bin`` associated with this
                session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin


    .. py:method:: can_assign_agents():
        Tests if this user can alter resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_agents_to_resource(resource_id):
        Tests if this user can alter resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_agent_to_resource(agent_id, resource_id):
        Adds an existing ``Agent`` to a ``Resource``.

        :arg:    agent_id (osid.id.Id): the ``Id`` of the ``Agent``
        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :raises:  AlreadyExists - ``agent_id`` is already assigned to
                ``resource_id``
        :raises:  NotFound - ``agent_id`` or ``resource_id`` not found
        :raises:  NullArgument - ``agent_id`` or ``resource_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_agent_from_resource(agent_id, resource_id):
        Removes an ``Agent`` from a ``Resource``.

        :arg:    agent_id (osid.id.Id): the ``Id`` of the ``Agent``
        :arg:    resource_id (osid.id.Id): the ``Id`` of the ``Resource``
        :raises:  NotFound - ``agent_id`` or ``resource_id`` not found or
                ``agent_id`` not assigned to ``resource_id``
        :raises:  NullArgument - ``agent_id`` or ``resource_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bin Lookup Methods
------------------

    .. py:method:: can_lookup_bins():
        Tests if this user can perform ``Bin`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bin_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bin_view():
        A complete view of the ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_bin(bin_id):
        Gets the ``Bin`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bin`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bin`` and retained for compatibility.

        :arg:    bin_id (osid.id.Id): ``Id`` of the ``Bin``
        :return: (osid.resource.Bin) - the bin
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_bins_by_ids(bin_ids):
        Gets a ``BinList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the bins
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bins`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    bin_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``bin_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_genus_type(bin_genus_type):
        Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins
            of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :arg:    bin_genus_type (osid.type.Type): a bin genus type
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NullArgument - ``bin_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_parent_genus_type(bin_genus_type):
        Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional
            bins with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :arg:    bin_genus_type (osid.type.Type): a bin genus type
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NullArgument - ``bin_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_record_type(bin_record_type):
        Gets a ``BinList`` containing the given bin record ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :arg:    bin_record_type (osid.type.Type): a bin record type
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NullArgument - ``bin_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins_by_provider(resource_id):
        Gets a ``BinList`` from the given provider.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.resource.BinList) - the returned ``Bin list``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bins():
        Gets all ``Bins``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :return: (osid.resource.BinList) - a list of ``Bins``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bins




Bin Query Methods
-----------------

    .. py:method:: can_search_bins():
        Tests if this user can perform ``Bin`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_query():
        Gets a bin query.

        The returned query will not have an extension query.

        :return: (osid.resource.BinQuery) - the bin query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_query


    .. py:method:: get_bins_by_query(bin_query):
        Gets a list of ``Bins`` matching the given bin query.

        :arg:    bin_query (osid.resource.BinQuery): the bin query
        :return: (osid.resource.BinList) - the returned ``BinList``
        :raises:  NullArgument - ``bin_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - a ``bin_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Bin Admin Methods
-----------------

    .. py:method:: can_create_bins():
        Tests if this user can create ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bin`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_bin_with_record_types(bin_record_types):
        Tests if this user can create a single ``Bin`` using the desired record types.

        While ``ResourceManager.getBinRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bin``.
        Providing an empty array tests if a ``Bin`` can be created with
        no records.

        :arg:    bin_record_types (osid.type.Type[]): array of bin record
                types
        :return: (boolean) - ``true`` if ``Bin`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``bin_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_form_for_create(bin_record_types):
        Gets the bin form for creating new bins.

        :arg:    bin_record_types (osid.type.Type[]): array of bin record
                types
        :return: (osid.resource.BinForm) - the bin form
        :raises:  NullArgument - ``bin_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form with requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_bin(bin_form):
        Creates a new ``Bin``.

        :arg:    bin_form (osid.resource.BinForm): the form for this
                ``Bin``
        :return: (osid.resource.Bin) - the new ``Bin``
        :raises:  IllegalState - ``bin_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``bin_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``bin_form`` did not originate from
                ``get_bin_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_bins():
        Tests if this user can update ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bin`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_form_for_update(bin_id):
        Gets the bin form for updating an existing bin.

        A new bin form should be requested for each update transaction.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin``
        :return: (osid.resource.BinForm) - the bin form
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_bin(bin_form):
        Updates an existing bin.

        :arg:    bin_form (osid.resource.BinForm): the form containing
                the elements to be updated
        :raises:  IllegalState - ``bin_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``bin_id`` or ``bin_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``bin_form`` did not originate from
                ``get_bin_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_bins():
        Tests if this user can delete ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Bin`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_bin(bin_id):
        Deletes a ``Bin``.

        :arg:    bin_id (osid.id.Id): the ``Id`` of the ``Bin`` to remove
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_bin_aliases():
        Tests if this user can manage ``Id`` aliases for ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Bin`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_bin(bin_id, alias_id):
        Adds an ``Id`` to a ``Bin`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Bin`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another bin, it is reassigned to the
        given bin ``Id``.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a ``Bin``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bin Hierarchy Methods
---------------------

    .. py:method:: get_bin_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_hierarchy_id


    .. py:method:: get_bin_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_hierarchy


    .. py:method:: can_access_bin_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_bin_view():
        The returns from the bin methods may omit or translate elements based on this session, such
            as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_bin_view():
        A complete view of the ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_bin_ids():
        Gets the root bin ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root bin ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_bin_ids


    .. py:method:: get_root_bins():
        Gets the root bins in the bin hierarchy.

        A node with no parents is an orphan. While all bin ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: (osid.resource.BinList) - the root bins
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_bins


    .. py:method:: has_parent_bins(bin_id):
        Tests if the ``Bin`` has any parents.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if the bin has parents, ``false``
                otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_bin(id_, bin_id):
        Tests if an ``Id`` is a direct parent of a bin.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``bin_id,``  ``false`` otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_bin_ids(bin_id):
        Gets the parent ``Ids`` of the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (osid.id.IdList) - the parent ``Ids`` of the bin
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_bins(bin_id):
        Gets the parents of the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :return: (osid.resource.BinList) - the parents of the bin
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_bin(id_, bin_id):
        Tests if an ``Id`` is an ancestor of a bin.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``bin_id,``  ``false`` otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_bins(bin_id):
        Tests if a bin has any children.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if the ``bin_id`` has children,
                ``false`` otherwise
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_bin(id_, bin_id):
        Tests if a bin is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``bin_id,``  ``false`` otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_bin_ids(bin_id):
        Gets the child ``Ids`` of the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the bin
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_bins(bin_id):
        Gets the children of the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :return: (osid.resource.BinList) - the children of the bin
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_bin(id_, bin_id):
        Tests if an ``Id`` is a descendant of a bin.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``bin_id,``  ``false`` otherwise
        :raises:  NotFound - ``bin_id`` is not found
        :raises:  NullArgument - ``id`` or ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_bin_node_ids(bin_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - a bin node
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_bin_nodes(bin_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.resource.BinNode) - a bin node
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Bin Hierarchy Design Methods
----------------------------

    .. py:method:: get_bin_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_hierarchy_id


    .. py:method:: get_bin_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: bin_hierarchy


    .. py:method:: can_modify_bin_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_bin(bin_id):
        Adds a root bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :raises:  AlreadyExists - ``bin_id`` is already in hierarchy
        :raises:  NotFound - ``bin_id`` not found
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_bin(bin_id):
        Removes a root bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :raises:  NotFound - ``bin_id`` not a root
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_bin(bin_id, child_id):
        Adds a child to a bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``bin_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``bin_id`` or ``child_id`` not found
        :raises:  NullArgument - ``bin_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_bin(bin_id, child_id):
        Removes a child from a bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``bin_id`` not a parent of ``child_id``
        :raises:  NullArgument - ``bin_id`` or ``child_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_bins(bin_id):
        Removes all children from a bin.

        :arg:    bin_id (osid.id.Id): the ``Id`` of a bin
        :raises:  NotFound - ``bin_id`` not in hierarchy
        :raises:  NullArgument - ``bin_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






