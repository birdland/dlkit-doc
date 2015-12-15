

Service Managers
================


Grading Manager
---------------

.. py:class:: GradingManager(osid_managers.OsidManager, GradingProfile, grading_managers.GradingManager)
    The grading manager provides access to grading sessions and provides interoperability tests for
    various aspects of this service.


    The sessions included in this manager are:




      * ``GradeSystemLookupSession:`` a session to look up grades and
        grade systems
      * ``GradeSystemQuerySession:`` a session to query grade systems
        ``None``
      * ``GradeSystemSearchSession:`` a session to search grade systems
      * ``GradeSystemAdminSession:`` a session to manage grade systems
      * ``GradeSystemNotificationSession`` a session for subscribing to
        new or deleted grades or grade systems
      * ``GradeSystemGradebookSession:`` a session for retrieving grade
        system to gradebook mappings
      * ``GradeSystemGradebookAssignmentSession:`` a session for
        managing grade system to gradebook mappings
      * ``GradeSystemSmartGradebookSession:`` a session for managing
        smart gradebooks of grade systems




      * ``GradeEntryLookupSession:`` a session to look up grade entries
      * ``GradeEntryQuerySession:`` a session to query grade entries
        ``None``
      * ``GradeEntrySearchSession:`` a session to search grade entries
      * ``GradeEntryAdminSession:`` a session to create, modify and
        delete grade entries ``None``
      * ``GradeEntryNotificationSession: a`` session to receive messages
        pertaining to grade entry ```` changes




      * ``GradebookColumnLookupSession:`` a session to look up gradebook
        columns
      * ``GradebookColumnQuerySession:`` a session to query gradebook
        columns ``None``
      * ``GradebookColumnSearchSession:`` a session to search gradebook
        columns
      * ``GradebookColumnAdminSession:`` a session to manage gradebook
        columns
      * ``GradebookColumnNotificationSession`` a session for subscribing
        to new or deleted gradebook columns
      * ``GradebookColumnGradebookSession:`` a session for retrieving
        gradebook column to gradebook mappings
      * ``GradebookColumnGradebookAssignmentSession:`` a session for
        managing gradebook column to gradebook mappings
      * ``GradebookColumnSmartGradebookSession:`` a session for managing
        smart gradebooks of gradebook columns




      * ``GradebookLookupSession:`` a session to lookup gradebooks
      * ``GradebookQuerySession:`` a session to query gradebooks
      * ``GradebookSearchSession`` : a session to search gradebooks
      * ``GradebookAdminSession`` : a session to create, modify and
        delete gradebooks
      * ``GradebookNotificationSession`` : a session to receive messages
        pertaining to gradebook changes
      * ``GradebookHierarchySession:`` a session to traverse the
        gradebook hierarchy
      * ``GradebookHierarchyDesignSession:`` a session to manage the
        gradebook hierarchy





    .. py:method:: get_grade_system_lookup_session():
        :noindex:


    .. py:attribute:: grade_system_lookup_session
        :noindex:


    .. py:method:: get_grade_system_lookup_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_query_session():
        :noindex:


    .. py:attribute:: grade_system_query_session
        :noindex:


    .. py:method:: get_grade_system_query_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_search_session():
        :noindex:


    .. py:attribute:: grade_system_search_session
        :noindex:


    .. py:method:: get_grade_system_search_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_admin_session():
        :noindex:


    .. py:attribute:: grade_system_admin_session
        :noindex:


    .. py:method:: get_grade_system_admin_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_notification_session(grade_system_receiver):
        :noindex:


    .. py:method:: get_grade_system_notification_session_for_gradebook(grade_system_receiver, gradebook_id):
        :noindex:


    .. py:method:: get_grade_system_gradebook_session():
        :noindex:


    .. py:attribute:: grade_system_gradebook_session
        :noindex:


    .. py:method:: get_grade_system_gradebook_assignment_session():
        :noindex:


    .. py:attribute:: grade_system_gradebook_assignment_session
        :noindex:


    .. py:method:: get_grade_system_smart_gradebook_session(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_lookup_session():
        :noindex:


    .. py:attribute:: grade_entry_lookup_session
        :noindex:


    .. py:method:: get_grade_entry_lookup_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_query_session():
        :noindex:


    .. py:attribute:: grade_entry_query_session
        :noindex:


    .. py:method:: get_grade_entry_query_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_search_session():
        :noindex:


    .. py:attribute:: grade_entry_search_session
        :noindex:


    .. py:method:: get_grade_entry_search_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_admin_session():
        :noindex:


    .. py:attribute:: grade_entry_admin_session
        :noindex:


    .. py:method:: get_grade_entry_admin_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_grade_entry_notification_session(receiver):
        :noindex:


    .. py:method:: get_grade_entry_notification_session_for_gradebook(receiver, gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_lookup_session():
        :noindex:


    .. py:attribute:: gradebook_column_lookup_session
        :noindex:


    .. py:method:: get_gradebook_column_lookup_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_query_session():
        :noindex:


    .. py:attribute:: gradebook_column_query_session
        :noindex:


    .. py:method:: get_gradebook_column_query_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_search_session():
        :noindex:


    .. py:attribute:: gradebook_column_search_session
        :noindex:


    .. py:method:: get_gradebook_column_search_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_admin_session():
        :noindex:


    .. py:attribute:: gradebook_column_admin_session
        :noindex:


    .. py:method:: get_gradebook_column_admin_session_for_gradebook(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_notification_session(gradebook_column_receiver):
        :noindex:


    .. py:method:: get_gradebook_column_notification_session_for_gradebook(gradebook_column_receiver, gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_column_gradebook_session():
        :noindex:


    .. py:attribute:: gradebook_column_gradebook_session
        :noindex:


    .. py:method:: get_gradebook_column_gradebook_assignment_session():
        :noindex:


    .. py:attribute:: gradebook_column_gradebook_assignment_session
        :noindex:


    .. py:method:: get_gradebook_column_smart_gradebook_session(gradebook_id):
        :noindex:


    .. py:method:: get_gradebook_lookup_session():
        :noindex:


    .. py:attribute:: gradebook_lookup_session
        :noindex:


    .. py:method:: get_gradebook_query_session():
        :noindex:


    .. py:attribute:: gradebook_query_session
        :noindex:


    .. py:method:: get_gradebook_search_session():
        :noindex:


    .. py:attribute:: gradebook_search_session
        :noindex:


    .. py:method:: get_gradebook_admin_session():
        :noindex:


    .. py:attribute:: gradebook_admin_session
        :noindex:


    .. py:method:: get_gradebook_notification_session(gradebook_receiver):
        :noindex:


    .. py:method:: get_gradebook_hierarchy_session():
        :noindex:


    .. py:attribute:: gradebook_hierarchy_session
        :noindex:


    .. py:method:: get_gradebook_hierarchy_design_session():
        :noindex:


    .. py:attribute:: gradebook_hierarchy_design_session
        :noindex:


    .. py:method:: get_grading_batch_manager():
        :noindex:


    .. py:attribute:: grading_batch_manager
        :noindex:


    .. py:method:: get_grading_calculation_manager():
        :noindex:


    .. py:attribute:: grading_calculation_manager
        :noindex:


    .. py:method:: get_grading_transform_manager():
        :noindex:


    .. py:attribute:: grading_transform_manager
        :noindex:




Gradebook Lookup Methods
------------------------

    .. py:method:: can_lookup_gradebooks():
        Tests if this user can perform ``Gradebook`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_gradebook_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_gradebook_view():
        A complete view of the ``Gradebook`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_gradebook(gradebook_id):
        Gets the ``Gradebook`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Gradebook`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Gradebook`` and retained
        for compatility.

        :arg:    gradebook_id (osid.id.Id): ``Id`` of the ``Gradebook``
        :return: (osid.grading.Gradebook) - the gradebook
        :raises:  NotFound - ``gradebook_id`` not found
        :raises:  NullArgument - ``gradebook_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_gradebooks_by_ids(gradebook_ids):
        Gets a ``GradebookList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        gradebooks specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Gradebook`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :arg:    gradebook_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``gradebook_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks_by_genus_type(gradebook_genus_type):
        Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not
            include gradebooks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :arg:    gradebook_genus_type (osid.type.Type): a gradebook genus
                type
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NullArgument - ``gradebook_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks_by_parent_genus_type(gradebook_genus_type):
        Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any
            additional gradebooks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :arg:    gradebook_genus_type (osid.type.Type): a gradebook genus
                type
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NullArgument - ``gradebook_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks_by_record_type(gradebook_record_type):
        Gets a ``GradebookList`` containing the given gradebook record ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :arg:    gradebook_record_type (osid.type.Type): a gradebook
                record type
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NullArgument - ``gradebook_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks_by_provider(resource_id):
        Gets a ``GradebookList`` for the given provider ````.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks():
        Gets all ``Gradebooks``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :return: (osid.grading.GradebookList) - a ``GradebookList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebooks




Gradebook Admin Methods
-----------------------

    .. py:method:: can_create_gradebooks():
        Tests if this user can create ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Gradebook`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_gradebook_with_record_types(gradebook_record_types):
        Tests if this user can create a single ``Gradebook`` using the desired record types.

        While ``GradingManager.getGradebookRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Gradebook``.
        Providing an empty array tests if a ``Gradebook`` can be created
        with no records.

        :arg:    gradebook_record_types (osid.type.Type[]): array of
                gradebook record types
        :return: (boolean) - ``true`` if ``Gradebook`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``gradebook_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_form_for_create(gradebook_record_types):
        Gets the gradebook form for creating new gradebooks.

        A new form should be requested for each create transaction.

        :arg:    gradebook_record_types (osid.type.Type[]): array of
                gradebook record types
        :return: (osid.grading.GradebookForm) - the gradebook form
        :raises:  NullArgument - ``gradebook_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_gradebook(gradebook_form):
        Creates a new ``Gradebook``.

        :arg:    gradebook_form (osid.grading.GradebookForm): the form
                for this ``Gradebook``
        :return: (osid.grading.Gradebook) - the new ``Gradebook``
        :raises:  IllegalState - ``gradebook_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``gradebook_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``gradebook_form`` did not originate from
                ``get_gradebook_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_gradebooks():
        Tests if this user can update ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Gradebook`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_form_for_update(gradebook_id):
        Gets the gradebook form for updating an existing gradebook.

        A new gradebook form should be requested for each update
        transaction.

        :arg:    gradebook_id (osid.id.Id): the ``Id`` of the
                ``Gradebook``
        :return: (osid.grading.GradebookForm) - the gradebook form
        :raises:  NotFound - ``gradebook_id`` is not found
        :raises:  NullArgument - ``gradebook_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_gradebook(gradebook_form):
        Updates an existing gradebook.

        :arg:    gradebook_form (osid.grading.GradebookForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``gradebook_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``gradebook_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``gradebook_form did not originate from
                get_gradebook_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_gradebooks():
        Tests if this user can delete gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Gradebook`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_gradebook(gradebook_id):
        Deletes a ``Gradebook``.

        :arg:    gradebook_id (osid.id.Id): the ``Id`` of the
                ``Gradebook`` to remove
        :raises:  NotFound - ``gradebook_id`` not found
        :raises:  NullArgument - ``gradebook_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_gradebook_aliases():
        Tests if this user can manage ``Id`` aliases for ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Gradebook`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_gradebook(gradebook_id, alias_id):
        Adds an ``Id`` to a ``Gradebook`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Gradebook`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another gradebook, it is
        reassigned to the given gradebook ``Id``.

        :arg:    gradebook_id (osid.id.Id): the ``Id`` of a ``Gradebook``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``gradebook_id`` not found
        :raises:  NullArgument - ``gradebook_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Grading Proxy Manager
---------------------

.. py:class:: GradingProxyManager(osid_managers.OsidProxyManager, GradingProfile, grading_managers.GradingProxyManager)
    The grading manager provides access to grading sessions and provides interoperability tests for
    various aspects of this service.


    Methods in this manager accept a ``Proxy`` for passing information
    from server environments.The sessions included in this manager are:




      * ``GradeSystemLookupSession:`` a session to look up grades and
        grade systems
      * ``GradeSystemQuerySession:`` a session to query grade systems
        ``None``
      * ``GradeSystemSearchSession:`` a session to search grade systems
      * ``GradeSystemAdminSession:`` a session to manage grade systems
      * ``GradeSystemNotificationSession`` a session for subscribing to
        new or deleted grades or grade systems
      * ``GradeSystemGradebookSession:`` a session for retrieving grade
        system to gradebook mappings
      * ``GradeSystemGradebookAssignmentSession:`` a session for
        managing grade system to gradebook mappings
      * ``GradeSystemSmartGradebookSession:`` a session for managing
        smart gradebooks of grade systems




      * ``GradeEntryLookupSession:`` a session to look up grade entries
      * ``GradeEntryQuerySession:`` a session to query grade entries
        ``None``
      * ``GradeEntrySearchSession:`` a session to search grade entries
      * ``GradeEntryAdminSession:`` a session to create, modify and
        delete grade entries ``None``
      * ``GradeEntryNotificationSession: a`` session to receive messages
        pertaining to grade entry ```` changes




      * ``GradebookColumnLookupSession:`` a session to look up gradebook
        columns
      * ``GradebookColumnQuerySession:`` a session to query gradebook
        columns ``None``
      * ``GradebookColumnSearchSession:`` a session to search gradebook
        columns
      * ``GradebookColumnAdminSession:`` a session to manage gradebook
        columns
      * ``GradebookColumnDerivationSession:`` a session to manage
        derived gradebook columns
      * ``GradebookColumnNotificationSession`` a session for subscribing
        to new or deleted gradebook columns
      * ``GradebookColumnGradebookSession:`` a session for retrieving
        gradebook column to gradebook mappings
      * ``GradebookColumnGradebookAssignmentSession:`` a session for
        managing gradebook column to gradebook mappings
      * ``GradebookColumnSmartGradebookSession:`` a session for managing
        smart gradebooks of gradebook columns




      * ``GradebookLookupSession:`` a session to lookup gradebooks
      * ``GradebookQuerySession:`` a session to query gradebooks
      * ``GradebookSearchSession`` : a session to search gradebooks
      * ``GradebookAdminSession`` : a session to create, modify and
        delete gradebooks
      * ``GradebookNotificationSession`` : a session to receive messages
        pertaining to gradebook changes
      * ``GradebookHierarchySession:`` a session to traverse the
        gradebook hierarchy
      * ``GradebookHierarchyDesignSession:`` a session to manage the
        gradebook hierarchy





    .. py:method:: get_grade_system_lookup_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_lookup_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_query_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_query_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_search_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_search_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_admin_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_admin_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_notification_session(grade_system_receiver, proxy):
        :noindex:


    .. py:method:: get_grade_system_notification_session_for_gradebook(grade_system_receiver, gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_system_gradebook_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_gradebook_assignment_session(proxy):
        :noindex:


    .. py:method:: get_grade_system_smart_gradebook_session(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_lookup_session(proxy):
        :noindex:


    .. py:method:: get_grade_entry_lookup_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_query_session(proxy):
        :noindex:


    .. py:method:: get_grade_entry_query_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_search_session(proxy):
        :noindex:


    .. py:method:: get_grade_entry_search_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_admin_session(proxy):
        :noindex:


    .. py:method:: get_grade_entry_admin_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_grade_entry_notification_session(grade_entry_receiver, proxy):
        :noindex:


    .. py:method:: get_grade_entry_notification_session_for_gradebook(grade_entry_receiver, gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_lookup_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_lookup_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_query_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_query_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_search_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_search_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_admin_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_admin_session_for_gradebook(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_notification_session(gradebook_column_receiver, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_notification_session_for_gradebook(gradebook_column_receiver, gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_column_gradebook_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_gradebook_assignment_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_column_smart_gradebook_session(gradebook_id, proxy):
        :noindex:


    .. py:method:: get_gradebook_lookup_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_query_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_search_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_admin_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_notification_session(gradebook_receiver, proxy):
        :noindex:


    .. py:method:: get_gradebook_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_gradebook_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_grading_batch_proxy_manager():
        :noindex:


    .. py:attribute:: grading_batch_proxy_manager
        :noindex:


    .. py:method:: get_grading_calculation_proxy_manager():
        :noindex:


    .. py:attribute:: grading_calculation_proxy_manager
        :noindex:


    .. py:method:: get_grading_transform_proxy_manager():
        :noindex:


    .. py:attribute:: grading_transform_proxy_manager
        :noindex:




Gradebook Lookup Methods
------------------------

    .. py:method:: can_lookup_gradebooks():
        Tests if this user can perform ``Gradebook`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_gradebook_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_gradebook_view():
        A complete view of the ``Gradebook`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_gradebook(gradebook_id):
        Gets the ``Gradebook`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Gradebook`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Gradebook`` and retained
        for compatility.

        :arg:    gradebook_id (osid.id.Id): ``Id`` of the ``Gradebook``
        :return: (osid.grading.Gradebook) - the gradebook
        :raises:  NotFound - ``gradebook_id`` not found
        :raises:  NullArgument - ``gradebook_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_gradebooks_by_ids(gradebook_ids):
        Gets a ``GradebookList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        gradebooks specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Gradebook`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :arg:    gradebook_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``gradebook_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks_by_genus_type(gradebook_genus_type):
        Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not
            include gradebooks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :arg:    gradebook_genus_type (osid.type.Type): a gradebook genus
                type
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NullArgument - ``gradebook_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks_by_parent_genus_type(gradebook_genus_type):
        Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any
            additional gradebooks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :arg:    gradebook_genus_type (osid.type.Type): a gradebook genus
                type
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NullArgument - ``gradebook_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks_by_record_type(gradebook_record_type):
        Gets a ``GradebookList`` containing the given gradebook record ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :arg:    gradebook_record_type (osid.type.Type): a gradebook
                record type
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NullArgument - ``gradebook_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks_by_provider(resource_id):
        Gets a ``GradebookList`` for the given provider ````.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.grading.GradebookList) - the returned
                ``Gradebook`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebooks():
        Gets all ``Gradebooks``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :return: (osid.grading.GradebookList) - a ``GradebookList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebooks




Gradebook Admin Methods
-----------------------

    .. py:method:: can_create_gradebooks():
        Tests if this user can create ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Gradebook`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_gradebook_with_record_types(gradebook_record_types):
        Tests if this user can create a single ``Gradebook`` using the desired record types.

        While ``GradingManager.getGradebookRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Gradebook``.
        Providing an empty array tests if a ``Gradebook`` can be created
        with no records.

        :arg:    gradebook_record_types (osid.type.Type[]): array of
                gradebook record types
        :return: (boolean) - ``true`` if ``Gradebook`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``gradebook_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_form_for_create(gradebook_record_types):
        Gets the gradebook form for creating new gradebooks.

        A new form should be requested for each create transaction.

        :arg:    gradebook_record_types (osid.type.Type[]): array of
                gradebook record types
        :return: (osid.grading.GradebookForm) - the gradebook form
        :raises:  NullArgument - ``gradebook_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_gradebook(gradebook_form):
        Creates a new ``Gradebook``.

        :arg:    gradebook_form (osid.grading.GradebookForm): the form
                for this ``Gradebook``
        :return: (osid.grading.Gradebook) - the new ``Gradebook``
        :raises:  IllegalState - ``gradebook_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``gradebook_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``gradebook_form`` did not originate from
                ``get_gradebook_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_gradebooks():
        Tests if this user can update ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Gradebook`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_form_for_update(gradebook_id):
        Gets the gradebook form for updating an existing gradebook.

        A new gradebook form should be requested for each update
        transaction.

        :arg:    gradebook_id (osid.id.Id): the ``Id`` of the
                ``Gradebook``
        :return: (osid.grading.GradebookForm) - the gradebook form
        :raises:  NotFound - ``gradebook_id`` is not found
        :raises:  NullArgument - ``gradebook_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_gradebook(gradebook_form):
        Updates an existing gradebook.

        :arg:    gradebook_form (osid.grading.GradebookForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``gradebook_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``gradebook_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``gradebook_form did not originate from
                get_gradebook_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_gradebooks():
        Tests if this user can delete gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Gradebook`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_gradebook(gradebook_id):
        Deletes a ``Gradebook``.

        :arg:    gradebook_id (osid.id.Id): the ``Id`` of the
                ``Gradebook`` to remove
        :raises:  NotFound - ``gradebook_id`` not found
        :raises:  NullArgument - ``gradebook_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_gradebook_aliases():
        Tests if this user can manage ``Id`` aliases for ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Gradebook`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_gradebook(gradebook_id, alias_id):
        Adds an ``Id`` to a ``Gradebook`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Gradebook`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another gradebook, it is
        reassigned to the given gradebook ``Id``.

        :arg:    gradebook_id (osid.id.Id): the ``Id`` of a ``Gradebook``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``gradebook_id`` not found
        :raises:  NullArgument - ``gradebook_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






