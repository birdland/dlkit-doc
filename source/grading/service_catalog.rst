

Service Catalog
===============


Gradebook
---------

.. py:class:: Gradebook(abc_grading_objects.Gradebook, osid_objects.OsidCatalog)
    A gradebook defines a collection of grade entries.

    .. py:method:: get_gradebook_record(gradebook_record_type):
        :noindex:




Grade System Lookup Methods
---------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``GradeSystem``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``GradeSystem Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_lookup_grade_systems():
        Tests if this user can perform ``GradeSystem`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_grade_system_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_grade_system_view():
        A complete view of the ``GradeSystem`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_gradebook_view():
        Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_gradebook_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_grade_system(grade_system_id):
        Gets the ``GradeSystem`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``GradeSystem`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``GradeSystem`` and retained
        for compatibility.

        :arg:    grade_system_id (osid.id.Id): ``Id`` of the
                ``GradeSystem``
        :return: (osid.grading.GradeSystem) - the grade system
        :raises:  NotFound - ``grade_system_id`` not found
        :raises:  NullArgument - ``grade_system_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_grade_system_by_grade(grade_id):
        Gets the ``GradeSystem`` by a ``Grade``  ``Id``.

        :arg:    grade_id (osid.id.Id): ``Id`` of a ``Grade``
        :return: (osid.grading.GradeSystem) - the grade system
        :raises:  NotFound - ``grade_id`` not found
        :raises:  NullArgument - ``grade_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_grade_systems_by_ids(grade_system_ids):
        Gets a ``GradeSystemList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the systems
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``GradeSystems`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :arg:    grade_system_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        :return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystem`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``grade_system_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_systems_by_genus_type(grade_system_genus_type):
        Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` which does
            not include systems of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :arg:    grade_system_genus_type (osid.type.Type): a grade system
                genus type
        :return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystem`` list
        :raises:  NullArgument - ``grade_system_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_systems_by_parent_genus_type(grade_system_genus_type):
        Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` and
            include any additional systems with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :arg:    grade_system_genus_type (osid.type.Type): a grade system
                genus type
        :return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystem`` list
        :raises:  NullArgument - ``grade_system_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_systems_by_record_type(grade_system_record_type):
        Gets a ``GradeSystemList`` containing the given grade record ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :arg:    grade_system_record_type (osid.type.Type): a grade
                system record type
        :return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystem`` list
        :raises:  NullArgument - ``grade_system_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_systems():
        Gets all ``GradeSystems``.

        In plenary mode, the returned list contains all known grade
        systems or an error results. Otherwise, the returned list may
        contain only those grade systems that are accessible through
        this session.

        :return: (osid.grading.GradeSystemList) - a ``GradeSystemList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: grade_systems




Grade System Query Methods
--------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_search_grade_systems():
        Tests if this user can perform ``GradeSystem`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_gradebook_view():
        Federates the view for methods in this session.

        A federated view will include grades in gradebooks which are
        children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_gradebook_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_grade_system_query():
        Gets a grade system query.

        :return: (osid.grading.GradeSystemQuery) - a grade system query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: grade_system_query


    .. py:method:: get_grade_systems_by_query(grade_system_query):
        Gets a list of ``GradeSystem`` objects matching the given grade system query.

        :arg:    grade_system_query (osid.grading.GradeSystemQuery): the
                grade system query
        :return: (osid.grading.GradeSystemList) - the returned
                ``GradeSystemList``
        :raises:  NullArgument - ``grade_system_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_system_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Grade System Admin Methods
--------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_create_grade_systems():
        Tests if this user can create ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``GradeSystem`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_grade_system_with_record_types(grade_system_record_types):
        Tests if this user can create a single ``GradeSystem`` using the desired record types.

        While ``GradingManager.getGradeSystemRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeSystem``.
        Providing an empty array tests if a ``GradeSystem`` can be
        created with no records.

        :arg:    grade_system_record_types (osid.type.Type[]): array of
                grade system types
        :return: (boolean) - ``true`` if ``GradeSystem`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``grade_system_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_system_form_for_create(grade_system_record_types):
        Gets the grade system form for creating new grade systems.

        A new form should be requested for each create transaction.

        :arg:    grade_system_record_types (osid.type.Type[]): array of
                grade system types
        :return: (osid.grading.GradeSystemForm) - the grade system form
        :raises:  NullArgument - ``grade_system_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_grade_system(grade_system_form):
        Creates a new ``GradeSystem``.

        :arg:    grade_system_form (osid.grading.GradeSystemForm): the
                form for this ``GradeSystem``
        :return: (osid.grading.GradeSystem) - the new ``GradeSystem``
        :raises:  IllegalState - ``grade_system_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``grade_system_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_system_form`` did not originate
                from ``get_grade_system_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_grade_systems():
        Tests if this user can update ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``GradeSystem`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_system_form_for_update(grade_system_id):
        Gets the grade system form for updating an existing grade system.

        A new grade system form should be requested for each update
        transaction.

        :arg:    grade_system_id (osid.id.Id): the ``Id`` of the
                ``GradeSystem``
        :return: (osid.grading.GradeSystemForm) - the grade system form
        :raises:  NotFound - ``grade_system_id`` is not found
        :raises:  NullArgument - ``grade_system_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_grade_system(grade_system_form):
        Updates an existing grade system.

        :arg:    grade_system_form (osid.grading.GradeSystemForm): the
                form containing the elements to be updated
        :raises:  IllegalState - ``grade_system_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``grade_system_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_system_form`` did not originate
                from ``get_grade_system_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_grade_systems():
        Tests if this user can delete grade systems.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``GradeSystem`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_grade_system(grade_system_id):
        Deletes a ``GradeSystem``.

        :arg:    grade_system_id (osid.id.Id): the ``Id`` of the
                ``GradeSystem`` to remove
        :raises:  NotFound - ``grade_system_id`` not found
        :raises:  NullArgument - ``grade_system_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_grade_system_aliases():
        Tests if this user can manage ``Id`` aliases for ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``GradeSystem`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_grade_system(grade_system_id, alias_id):
        Adds an ``Id`` to a ``GradeSystem`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradeSystem`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade system, it is
        reassigned to the given grade system ``Id``.

        :arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``grade_system_id`` not found
        :raises:  NullArgument - ``grade_system_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_grades(grade_system_id):
        Tests if this user can create ``Grade`` s for a ``GradeSystem``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        :return: (boolean) - ``false`` if ``Grade`` creation is not
                authorized, ``true`` otherwise
        :raises:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_grade_with_record_types(grade_system_id, grade_record_types):
        Tests if this user can create a single ``Grade`` using the desired record types.

        While ``GradingManager.getGradeRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Grade``.
        Providing an empty array tests if a ``Grade`` can be created
        with no records.

        :arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        :arg:    grade_record_types (osid.type.Type[]): array of grade
                recod types
        :return: (boolean) - ``true`` if ``Grade`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        :raises:  NullArgument - ``grade_system_id`` or
                ``grade_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_form_for_create(grade_system_id, grade_record_types):
        Gets the grade form for creating new grades.

        A new form should be requested for each create transaction.

        :arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        :arg:    grade_record_types (osid.type.Type[]): array of grade
                recod types
        :return: (osid.grading.GradeForm) - the grade form
        :raises:  NotFound - ``grade_system_id`` is not found
        :raises:  NullArgument - ``grade_system_id`` or
                ``grade_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_grade(grade_form):
        Creates a new ``Grade``.

        :arg:    grade_form (osid.grading.GradeForm): the form for this
                ``Grade``
        :return: (osid.grading.Grade) - the new ``Grade``
        :raises:  IllegalState - ``grade_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``grade_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_form`` did not originate from
                ``get_grade_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_grades(grade_system_id):
        Tests if this user can update ``Grades``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Grade``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        :return: (boolean) - ``false`` if ``Grade`` modification is not
                authorized, ``true`` otherwise
        :raises:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_form_for_update(grade_id):
        Gets the grade form for updating an existing grade.

        A new grade form should be requested for each update
        transaction.

        :arg:    grade_id (osid.id.Id): the ``Id`` of the ``Grade``
        :return: (osid.grading.GradeForm) - the grade form
        :raises:  NotFound - ``grade_id`` is not found
        :raises:  NullArgument - ``grade_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_grade(grade_form):
        Updates an existing grade.

        :arg:    grade_form (osid.grading.GradeForm): the form containing
                the elements to be updated
        :raises:  IllegalState - ``grade_form`` already used in an update
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``grade_id`` or ``grade_form`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_form`` did not originate from
                ``get_grade_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_grades(grade_system_id):
        Tests if this user can delete grades.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Grade``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :arg:    grade_system_id (osid.id.Id): the ``Id`` of a
                ``GradeSystem``
        :return: (boolean) - ``false`` if ``Grade`` deletion is not
                authorized, ``true`` otherwise
        :raises:  NullArgument - ``grade_system_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_grade(grade_id):
        Deletes a ``Grade``.

        :arg:    grade_id (osid.id.Id): the ``Id`` of the ``Grade`` to
                remove
        :raises:  NotFound - ``grade_id`` not found
        :raises:  NullArgument - ``grade_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_grade_aliases():
        Tests if this user can manage ``Id`` aliases for ``Grades``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Grade`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_grade(grade_id, alias_id):
        Adds an ``Id`` to a ``Grade`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Grade`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade, it is
        reassigned to the given grade ``Id``.

        :arg:    grade_id (osid.id.Id): the ``Id`` of a ``Grade``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``grade_id`` not found
        :raises:  NullArgument - ``grade_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Grade Entry Lookup Methods
--------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_lookup_grade_entries():
        Tests if this user can perform ``GradeEntry`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_grade_entry_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_grade_entry_view():
        A complete view of the ``GradeEntry`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_gradebook_view():
        Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_gradebook_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_effective_grade_entry_view():
        Only grade entries whose effective dates are current are returned by methods in this
            session.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_any_effective_grade_entry_view():
        All grade entries of any effective dates are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_grade_entry(grade_entry_id):
        Gets the ``GradeEntry`` specified by its ``Id``.

        :arg:    grade_entry_id (osid.id.Id): ``Id`` of the
                ``GradeEntry``
        :return: (osid.grading.GradeEntry) - the grade entry
        :raises:  NotFound - ``grade_entry_id`` not found
        :raises:  NullArgument - ``grade_entry_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_grade_entries_by_ids(grade_entry_ids):
        Gets a ``GradeEntryList`` corresponding to the given ``IdList``.

        :arg:    grade_entry_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``grade_entry_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_by_genus_type(grade_entry_genus_type):
        Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` which does
            not include grade entries of genus types derived from the specified ``Type``.

        :arg:    grade_entry_genus_type (osid.type.Type): a grade entry
                genus type
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  NullArgument - ``grade_entry_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_by_parent_genus_type(grade_entry_genus_type):
        Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` and include
            any additional grade entry with genus types derived from the specified ``Type``.

        :arg:    grade_entry_genus_type (osid.type.Type): a grade entry
                genus type
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  NullArgument - ``grade_entry_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_by_record_type(grade_entry_record_type):
        Gets a ``GradeEntryList`` containing the given grade entry record ``Type``.

        :arg:    grade_entry_record_type (osid.type.Type): a grade entry
                record type
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  NullArgument - ``grade_entry_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_on_date(from_, to):
        Gets a ``GradeEntryList`` effective during the entire given date range inclusive but not
            confined to the date range.

        :arg:    from (osid.calendaring.DateTime): start of date range
        :arg:    to (osid.calendaring.DateTime): end of date range
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``from or to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_for_gradebook_column(gradebook_column_id):
        Gets a ``GradeEntryList`` for the gradebook column.

        :arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  NullArgument - ``gradebook_column_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_for_gradebook_column_on_date(gradebook_column_id, from_, to):
        Gets a ``GradeEntryList`` for the given gradebook column and effective during the entire
            given date range inclusive but not confined to the date range.

        :arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        :arg:    from (osid.calendaring.DateTime): start of date range
        :arg:    to (osid.calendaring.DateTime): end of date range
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``gradebook_column_id, from, or to`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_for_resource(resource_id):
        Gets a ``GradeEntryList`` for the given key key resource.

        :arg:    resource_id (osid.id.Id): a key resource ``Id``
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_for_resource_on_date(resource_id, from_, to):
        Gets a ``GradeEntryList`` for the given key resource and effective during the entire given
            date range inclusive but not confined to the date range.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :arg:    from (osid.calendaring.DateTime): start of date range
        :arg:    to (osid.calendaring.DateTime): end of date range
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``resource_id, from, or to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_for_gradebook_column_and_resource(gradebook_column_id, resource_id):
        Gets a ``GradeEntryList`` for the gradebook column and key resource.

        :arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        :arg:    resource_id (osid.id.Id): a key resource ``Id``
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  NullArgument - ``gradebook_column_id`` or
                ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_for_gradebook_column_and_resource_on_date(gradebook_column_id, resource_id, from_, to):
        Gets a ``GradeEntryList`` for the given gradebook column, resource, and effective during the
            entire given date range inclusive but not confined to the date range.

        :arg:    gradebook_column_id (osid.id.Id): a gradebook column
                ``Id``
        :arg:    resource_id (osid.id.Id): a key resource ``Id``
        :arg:    from (osid.calendaring.DateTime): start of date range
        :arg:    to (osid.calendaring.DateTime): end of date range
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``gradebook_column_id, resource, from, or
                to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries_by_grader(resource_id):
        Gets a ``GradeEntryList`` for the given grader.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntry`` list
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entries():
        Gets all grade entries.

        :return: (osid.grading.GradeEntryList) - a ``GradeEntryList``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: grade_entries




Grade Entry Query Methods
-------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_search_grade_entries():
        Tests if this user can perform ``GradeEntry`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_gradebook_view():
        Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_gradebook_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_grade_entry_query():
        Gets a grade entry query.

        :return: (osid.grading.GradeEntryQuery) - the grade entry query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: grade_entry_query


    .. py:method:: get_grade_entries_by_query(grade_entry_query):
        Gets a list of entries matching the given grade entry query.

        :arg:    grade_entry_query (osid.grading.GradeEntryQuery): the
                grade entry query
        :return: (osid.grading.GradeEntryList) - the returned
                ``GradeEntryList``
        :raises:  NullArgument - ``grade_entry_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_entry_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Grade Entry Admin Methods
-------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_create_grade_entries():
        Tests if this user can create grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``GradeEntry`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_grade_entry_with_record_types(grade_entry_record_types):
        Tests if this user can create a single ``GradeEntry`` using the desired record types.

        While ``GradingManager.getGradeEntryRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeEntry``.
        Providing an empty array tests if a ``GradeEntry`` can be
        created with no records.

        :arg:    grade_entry_record_types (osid.type.Type[]): array of
                grade entry record types
        :return: (boolean) - ``true`` if ``GradeEntry`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``grade_entry_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entry_form_for_create(gradebook_column_id, resource_id, grade_entry_record_types):
        Gets the grade entry form for creating new grade entries.

        A new form should be requested for each create transaction.

        :arg:    gradebook_column_id (osid.id.Id): the gradebook column
        :arg:    resource_id (osid.id.Id): the key resource
        :arg:    grade_entry_record_types (osid.type.Type[]): array of
                grade entry record types
        :return: (osid.grading.GradeEntryForm) - the grade entry form
        :raises:  NotFound - ``gradebook_column_id or resource_id`` not
                found
        :raises:  NullArgument - ``gradebook_column_id, resource_id,`` or
                ``grade_entry_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_grade_entry(grade_entry_form):
        Creates a new ``GradeEntry``.

        :arg:    grade_entry_form (osid.grading.GradeEntryForm): the form
                for this ``GradeEntry``
        :return: (osid.grading.GradeEntry) - the new ``GradeEntry``
        :raises:  IllegalState - ``grade_entry_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``grade_entry_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_entry_form`` did not originate
                from ``get_grade_entry_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_overridecalculated_grade_entries():
        Tests if this user can override grade entries calculated from another.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``GradeEntry`` override is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entry_form_for_override(grade_entry_id, grade_entry_record_types):
        Gets the grade entry form for overriding calculated grade entries.

        A new form should be requested for each create transaction.

        :arg:    grade_entry_id (osid.id.Id): the ``Id`` of the grade
                entry to be overridden
        :arg:    grade_entry_record_types (osid.type.Type[]): array of
                grade entry record types
        :return: (osid.grading.GradeEntryForm) - the grade entry form
        :raises:  AlreadyExists - ``grade_entry_id`` is already overridden
        :raises:  NotFound - ``grade_entry_id`` not found or
                ``grade_entry_id`` is not a calculated entry
        :raises:  NullArgument - ``grade_entry_id`` or
                ``grade_entry_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: override_calculated_grade_entry(grade_entry_form):
        Creates a new overriding ``GradeEntry``.

        :arg:    grade_entry_form (osid.grading.GradeEntryForm): the form
                for this ``GradeEntry``
        :return: (osid.grading.GradeEntry) - the new ``GradeEntry``
        :raises:  IllegalState - ``grade_entry_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``grade_entry_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_entry_form`` did not originate
                from ``get_grade_entry_form_for_override()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_grade_entries():
        Tests if this user can update grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if grade entry modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_grade_entry_form_for_update(grade_entry_id):
        Gets the grade entry form for updating an existing entry.

        A new grade entry form should be requested for each update
        transaction.

        :arg:    grade_entry_id (osid.id.Id): the ``Id`` of the
                ``GradeEntry``
        :return: (osid.grading.GradeEntryForm) - the grade entry form
        :raises:  NotFound - ``grade_entry_id`` is not found
        :raises:  NullArgument - ``grade_entry_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_grade_entry(grade_entry_form):
        Updates an existing grade entry.

        :arg:    grade_entry_form (osid.grading.GradeEntryForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``grade_entry_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``grade_entry_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``grade_entry_form`` did not originate
                from ``get_grade_entry_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_grade_entries():
        Tests if this user can delete grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``GradeEntry`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_grade_entry(grade_entry_id):
        Deletes the ``GradeEntry`` identified by the given ``Id``.

        :arg:    grade_entry_id (osid.id.Id): the ``Id`` of the
                ``GradeEntry`` to delete
        :raises:  NotFound - a ``GradeEntry`` was not found identified by
                the given ``Id``
        :raises:  NullArgument - ``grade_entry_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_grade_entry_aliases():
        Tests if this user can manage ``Id`` aliases for ``GradeEntries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``GradeEntry`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_grade_entry(grade_entry_id, alias_id):
        Adds an ``Id`` to a ``GradeEntry`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradeEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade entry, it is
        reassigned to the given grade entry ``Id``.

        :arg:    grade_entry_id (osid.id.Id): the ``Id`` of a
                ``GradeEntry``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``grade_entry_id`` not found
        :raises:  NullArgument - ``grade_entry_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Gradebook Column Lookup Methods
-------------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_lookup_gradebook_columns():
        Tests if this user can perform ``GradebookColumn`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_gradebook_column_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_gradebook_column_view():
        A complete view of the ``GradebookColumn`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_gradebook_view():
        Federates the view for methods in this session.

        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_gradebook_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_gradebook_column(gradebook_column_id):
        Gets the ``GradebookColumn`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``GradebookColumn`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``GradebookColumn`` and
        retained for compatibility.

        :arg:    gradebook_column_id (osid.id.Id): ``Id`` of the
                ``GradebookColumn``
        :return: (osid.grading.GradebookColumn) - the gradebook column
        :raises:  NotFound - ``gradebook_column_id`` not found
        :raises:  NullArgument - ``gradebook_column_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_gradebook_columns_by_ids(gradebook_column_ids):
        Gets a ``GradebookColumnList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the gradebook
        columns specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if a ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible gradeboook columns may be omitted from the list.

        :arg:    gradebook_column_ids (osid.id.IdList): the list of
                ``Ids`` to retrieve
        :return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumn`` list
        :raises:  NotFound - an ``Id was`` not found
        :raises:  NullArgument - ``grade_book_column_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_columns_by_genus_type(gradebook_column_genus_type):
        Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type``
            which does not include gradebook columns of genus types derived from the specified
            ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :arg:    gradebook_column_genus_type (osid.type.Type): a
                gradebook column genus type
        :return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumn`` list
        :raises:  NullArgument - ``gradebook_column_genus_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_columns_by_parent_genus_type(gradebook_column_genus_type):
        Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type``
            and include any additional columns with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :arg:    gradebook_column_genus_type (osid.type.Type): a
                gradebook column genus type
        :return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumn`` list
        :raises:  NullArgument - ``gradebook_column_genus_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_columns_by_record_type(gradebook_column_record_type):
        Gets a ``GradebookColumnList`` containing the given gradebook column record ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :arg:    gradebook_column_record_type (osid.type.Type): a
                gradebook column record type
        :return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumn`` list
        :raises:  NullArgument - ``gradebook_column_record_type`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_columns():
        Gets all gradebook columns.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :return: (osid.grading.GradebookColumnList) - a
                ``GradebookColumn``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_columns


    .. py:method:: supports_summary():
        Tests if a summary entry is available.

        :return: (boolean) - ``true`` if a summary entry is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_column_summary(gradebook_column_id):
        Gets the ``GradebookColumnSummary`` for summary results.

        :arg:    gradebook_column_id (osid.id.Id): ``Id`` of the
                ``GradebookColumn``
        :return: (osid.grading.GradebookColumnSummary) - the gradebook
                column summary
        :raises:  NotFound - ``gradebook_column_id`` is not found
        :raises:  NullArgument - ``gradebook_column_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unimplemented - ``has_summary()`` is ``false``
        *compliance: mandatory -- This method is must be implemented.*






Gradebook Column Query Methods
------------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_search_gradebook_columns():
        Tests if this user can perform ``GradebookColumn`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_gradebook_view():
        Federates the view for methods in this session.

        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_gradebook_view():
        Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_gradebook_column_query():
        Gets a gradebook column query.

        :return: (osid.grading.GradebookColumnQuery) - the gradebook
                column
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_column_query


    .. py:method:: get_gradebook_columns_by_query(gradebook_column_query):
        Gets a list of gradebook columns matching the given query.

        :arg:    gradebook_column_query
                (osid.grading.GradebookColumnQuery): the gradebook
                column query
        :return: (osid.grading.GradebookColumnList) - the returned
                ``GradebookColumnList``
        :raises:  NullArgument - ``gradebook_column_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``gradebook_column_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Gradebook Column Admin Methods
------------------------------

    .. py:method:: get_gradebook_id():
        Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Gradebook Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook_id


    .. py:method:: get_gradebook():
        Gets the ``Gradebook`` associated with this session.

        :return: (osid.grading.Gradebook) - the ``Gradebook`` associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: gradebook


    .. py:method:: can_create_gradebook_columns():
        Tests if this user can create gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a gradebook
        column will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``GradebookColumn`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_gradebook_column_with_record_types(gradebook_column_record_types):
        Tests if this user can create a single ``GradebookColumn`` using the desired record types.

        While ``GradingManager.getGradebookColumnRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``GradebookColumn``. Providing an empty array tests if a
        ``GradebookColumn`` can be created with no records.

        :arg:    gradebook_column_record_types (osid.type.Type[]): array
                of gradebook column record types
        :return: (boolean) - ``true`` if ``GradebookColumn`` creation
                using the specified record ``Types`` is supported,
                ``false`` otherwise
        :raises:  NullArgument - ``gradebook_column_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_column_form_for_create(gradebook_column_record_types):
        Gets the gradebook column form for creating new gradebook columns.

        A new form should be requested for each create transaction.

        :arg:    gradebook_column_record_types (osid.type.Type[]): array
                of gradebook column record types
        :return: (osid.grading.GradebookColumnForm) - the gradebook
                column form
        :raises:  NullArgument - ``gradebook_column_record_types`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_gradebook_column(gradebook_column_form):
        Creates a new ``GradebookColumn``.

        :arg:    gradebook_column_form
                (osid.grading.GradebookColumnForm): the form for this
                ``GradebookColumn``
        :return: (osid.grading.GradebookColumn) - the new
                ``GradebookColumn``
        :raises:  IllegalState - ``gradebook_column_form`` already used in
                a create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``gradebook_column_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``gradebook_column_form`` did not
                originate from
                ``get_gradebook_column_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_gradebook_columns():
        Tests if this user can update gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: (boolean) - ``false`` if gradebook column modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_gradebook_column_form_for_update(gradebook_column_id):
        Gets the gradebook column form for updating an existing gradebook column.

        A new gradebook column form should be requested for each update
        transaction.

        :arg:    gradebook_column_id (osid.id.Id): the ``Id`` of the
                ``GradebookColumn``
        :return: (osid.grading.GradebookColumnForm) - the gradebook
                column form
        :raises:  NotFound - ``gradebook_column_id`` is not found
        :raises:  NullArgument - ``gradebook_column_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_gradebook_column(gradebook_column_form):
        Updates an existing gradebook column.

        :arg:    gradebook_column_form
                (osid.grading.GradebookColumnForm): the form containing
                the elements to be updated
        :raises:  IllegalState - ``gradebook_column_form`` already used in
                an update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``gradebook_column_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``gradebook_column_form`` did not
                originate from
                ``get_gradebook_column_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: sequence_gradebook_columns(gradebook_column_ids):
        Resequences the gradebook columns.

        :arg:    gradebook_column_ids (osid.id.IdList): the ``Ids`` of
                the ``GradebookColumns``
        :raises:  NullArgument - ``gradebook_column_id_list`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: move_gradebook_column(front_gradebook_column_id, back_gradebook_column_id):
        Moves a gradebook column in front of another.

        :arg:    front_gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        :arg:    back_gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        :raises:  NotFound - ``front_gradebook_column_id or
                back_gradebook_column_id`` is not found
        :raises:  NullArgument - ``front_gradebook_column_id or
                back_gradebook_column_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: copy_gradebook_column_entries(source_gradebook_column_id, target_gradebook_column_id):
        Copies gradebook column entries from one column to another.

        If the target grade column grade system differs from the source,
        the grades in the entries are transformed to the new grade
        system.

        :arg:    source_gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        :arg:    target_gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        :raises:  NotFound - ``source_gradebook_column_id
                ortarget_gradebook_column_id`` is not found
        :raises:  NullArgument - ``source_gradebook_column_id
                target_gradebook_column_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_gradebook_columns():
        Tests if this user can delete gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``GradebookColumn`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_gradebook_column(gradebook_column_id):
        Deletes the ``GradebookColumn`` identified by the given ``Id``.

        :arg:    gradebook_column_id (osid.id.Id): the ``Id`` of the
                ``GradebookColumn`` to delete
        :raises:  NotFound - a ``GradebookColumn`` was not found
                identified by the given ``Id``
        :raises:  NullArgument - ``gradebook_column_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_gradebook_column_aliases():
        Tests if this user can manage ``Id`` aliases for ``GradebookColumns``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``GradebookColumn`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_gradebook_column(gradebook_column_id, alias_id):
        Adds an ``Id`` to a ``GradebookColumn`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradebookColumn`` is determined by
        the provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another gradebook column,
        it is reassigned to the given gradebook column ``Id``.

        :arg:    gradebook_column_id (osid.id.Id): the ``Id`` of a
                ``GradebookColumn``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``gradebook_column_id`` not found
        :raises:  NullArgument - ``gradebook_column_id`` or ``alias_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






