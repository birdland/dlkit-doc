

Service Catalog
===============


Bin
---

.. py:class:: Bin(abc_resource_objects.Bin, osid_objects.OsidCatalog)
    An inventory defines a collection of resources.

    .. py:method:: get_bin_record(bin_record_type):
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






