from ..osid import sessions as osid_sessions


class GradeSystemLookupSession(osid_sessions.OsidSession):
    """The session defines methods for retrieving ``Grades`` and ``GradeSystems``.

    A Grade represents a qualified ranking defined in some grade system.

    Two views are defined in this session:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * federated gradebook view: lookups include grade systems from
        this gradebook and other gradebooks which are children of this
        gradebook in the gradebook hierarchy
      * isolated gradebook view: lookups include only those grade
        systems defined in this gradebook

    
    Grades and grade systems may have an additional records indicated by
    their respective record types. The record may not be accessed
    through a cast of the object.

    """
    def get_gradebook_id(self):
        """Gets the ``GradeSystem``  ``Id`` associated with this session.

        :return: the ``GradeSystem Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_lookup_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_grade_system_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_grade_system_view(self):
        """A complete view of the ``GradeSystem`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.



        """
        pass

    def get_grade_system(self, grade_system_id):
        """Gets the ``GradeSystem`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``GradeSystem`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``GradeSystem`` and retained
        for compatibility.

        :param grade_system_id: ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``NotFound`` -- ``grade_system_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystem

    def get_grade_system_by_grade(self, grade_id):
        """Gets the ``GradeSystem`` by a ``Grade``  ``Id``.

        :param grade_id: ``Id`` of a ``Grade``
        :type grade_id: ``osid.id.Id``
        :return: the grade system
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``NotFound`` -- ``grade_id`` not found
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystem

    def get_grade_systems_by_ids(self, grade_system_ids):
        """Gets a ``GradeSystemList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the systems
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``GradeSystems`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param grade_system_ids: the list of ``Ids`` to retrieve
        :type grade_system_ids: ``osid.id.IdList``
        :return: the returned ``GradeSystem`` list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``grade_system_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystemList

    def get_grade_systems_by_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` which does not include systems of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :param grade_system_genus_type: a grade system genus type
        :type grade_system_genus_type: ``osid.type.Type``
        :return: the returned ``GradeSystem`` list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``grade_system_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystemList

    def get_grade_systems_by_parent_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` and include any additional systems with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :param grade_system_genus_type: a grade system genus type
        :type grade_system_genus_type: ``osid.type.Type``
        :return: the returned ``GradeSystem`` list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``grade_system_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystemList

    def get_grade_systems_by_record_type(self, grade_system_record_type):
        """Gets a ``GradeSystemList`` containing the given grade record ``Type``.

        In plenary mode, the returned list contains all known systems or
        an error results. Otherwise, the returned list may contain only
        those systems that are accessible through this session.

        :param grade_system_record_type: a grade system record type
        :type grade_system_record_type: ``osid.type.Type``
        :return: the returned ``GradeSystem`` list
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``grade_system_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystemList

    def get_grade_systems(self):
        """Gets all ``GradeSystems``.

        In plenary mode, the returned list contains all known grade
        systems or an error results. Otherwise, the returned list may
        contain only those grade systems that are accessible through
        this session.

        :return: a ``GradeSystemList``
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystemList

    grade_systems = property(fget=get_grade_systems)


class GradeSystemQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``GradeSystems``.

    The search query is constructed using the ``GradeSystemQuery``.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated gradebook view: searches include grade systems in
        gradebooks of which this gradebook is a ancestor in the
        gradebook hierarchy
      * isolated gradebook view: searches are restricted to grade
        systems in this gradebook

    
    Grade systems may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradeSystemQuery``.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_search_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grades in gradebooks which are
        children of this gradebook in the gradebook hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.



        """
        pass

    def get_grade_system_query(self):
        """Gets a grade system query.

        :return: a grade system query
        :rtype: ``osid.grading.GradeSystemQuery``

        """
        return # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)

    def get_grade_systems_by_query(self, grade_system_query):
        """Gets a list of ``GradeSystem`` objects matching the given grade system query.

        :param grade_system_query: the grade system query
        :type grade_system_query: ``osid.grading.GradeSystemQuery``
        :return: the returned ``GradeSystemList``
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``grade_system_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_system_query`` is not of this service

        """
        return # osid.grading.GradeSystemList


class GradeSystemSearchSession(GradeSystemQuerySession):
    """This session provides methods for searching among ``GradeSystems``.

    The search query is constructed using the ``GradeSystemQuery``.

    ``get_grade_systems_by_query()`` is the basic search method and
    returns a list of ``GradeSystems``. A more advanced search may be
    performed with ``getGradeSystemsBySearch()``. It accepts a
    ``GradeSystemSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_grade_systems_by_search()`` returns a
    ``GradeSystemSearchResults`` that can be used to access the
    resulting ``GradeSystemList`` or be used to perform a search within
    the result set through ``GradeSystemSearch``.
    
    This session defines views that offer differing behaviors for
    searching.
    
      * federated gradebook view: searches include grade systems in
        gradebooks of which this gradebook is a ancestor in the
        gradebook hierarchy
      * isolated gradebook view: searches are restricted to grade
        systems in this gradebook

    
    Grade systems may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradeSystemQuery``.

    """
    def get_grade_system_search(self):
        """Gets a grade system search.

        :return: a grade system search
        :rtype: ``osid.grading.GradeSystemSearch``

        """
        return # osid.grading.GradeSystemSearch

    grade_system_search = property(fget=get_grade_system_search)

    def get_grade_system_search_order(self):
        """Gets a grade system search order.

        The ``GradeSystemSearchOrder`` is supplied to a
        ``GradeSystemSearch`` to specify the ordering of results.

        :return: the grade system search order
        :rtype: ``osid.grading.GradeSystemSearchOrder``

        """
        return # osid.grading.GradeSystemSearchOrder

    grade_system_search_order = property(fget=get_grade_system_search_order)

    def get_grade_systems_by_search(self, grade_system_query, grade_system_search):
        """Gets the search results matching the given search query using the given search.

        :param grade_system_query: the grade system query
        :type grade_system_query: ``osid.grading.GradeSystemQuery``
        :param grade_system_search: the grade system search
        :type grade_system_search: ``osid.grading.GradeSystemSearch``
        :return: the grade system search results
        :rtype: ``osid.grading.GradeSystemSearchResults``
        :raise: ``NullArgument`` -- ``grade_system_query`` or ``grade_system_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_system_query`` or ``grade_system_search`` is not of this service

        """
        return # osid.grading.GradeSystemSearchResults

    def get_grade_system_query_from_inspector(self, grade_system_query_inspector):
        """Gets a grade system query from an inspector.

        The inspector is available from an ``GradeSystemSearchResults``.

        :param grade_system_query_inspector: a grade system query inspector
        :type grade_system_query_inspector: ``osid.grading.GradeSystemQueryInspector``
        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``NullArgument`` -- ``grade_system_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``grade_system_query_inspector`` is not of this service

        """
        return # osid.grading.GradeSystemQuery


class GradeSystemAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``GradeSystems``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``GradeSystem,`` a ``GradeSystemForm`` is requested using
    ``get_grade_system_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradeSystemForm`` will indicate that it is to be used with a
    create operation and can be used to examine metdata or validate data
    prior to creation. Once the ``GradeSystemForm`` is submiited to a
    create operation, it cannot be reused with another create operation
    unless the first operation was unsuccessful. Each
    ``GradeSystemForm`` corresponds to an attempted transaction.
    
    For updates, ``GradeSystemForms`` are requested to the
    ``GradeSystem``  ``Id`` that is to be updated using
    ``getGradeSystemFormForUpdate()``. Similarly, the
    ``GradeSystemForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``GradeSystemForm`` can only be used once for a successful update
    and cannot be reused.
    
    The delete operations delete ``GradeSystems`` To unmap a
    ``GradeSystem`` from the current ``Gradebook,`` the
    ``GradeSystemGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradeSystem`` itself thus
    removing it from all known ``Gradebook`` catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_create_grade_systems(self):
        """Tests if this user can create ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_grade_system_with_record_types(self, grade_system_record_types):
        """Tests if this user can create a single ``GradeSystem`` using the desired record types.

        While ``GradingManager.getGradeSystemRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeSystem``.
        Providing an empty array tests if a ``GradeSystem`` can be
        created with no records.

        :param grade_system_record_types: array of grade system types
        :type grade_system_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``GradeSystem`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_record_types`` is ``null``

        """
        return # boolean

    def get_grade_system_form_for_create(self, grade_system_record_types):
        """Gets the grade system form for creating new grade systems.

        A new form should be requested for each create transaction.

        :param grade_system_record_types: array of grade system types
        :type grade_system_record_types: ``osid.type.Type[]``
        :return: the grade system form
        :rtype: ``osid.grading.GradeSystemForm``
        :raise: ``NullArgument`` -- ``grade_system_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.grading.GradeSystemForm

    def create_grade_system(self, grade_system_form):
        """Creates a new ``GradeSystem``.

        :param grade_system_form: the form for this ``GradeSystem``
        :type grade_system_form: ``osid.grading.GradeSystemForm``
        :return: the new ``GradeSystem``
        :rtype: ``osid.grading.GradeSystem``
        :raise: ``IllegalState`` -- ``grade_system_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``grade_system_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_system_form`` did not originate from ``get_grade_system_form_for_create()``

        """
        return # osid.grading.GradeSystem

    def can_update_grade_systems(self):
        """Tests if this user can update ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_system_form_for_update(self, grade_system_id):
        """Gets the grade system form for updating an existing grade system.

        A new grade system form should be requested for each update
        transaction.

        :param grade_system_id: the ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: the grade system form
        :rtype: ``osid.grading.GradeSystemForm``
        :raise: ``NotFound`` -- ``grade_system_id`` is not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystemForm

    def update_grade_system(self, grade_system_form):
        """Updates an existing grade system.

        :param grade_system_form: the form containing the elements to be updated
        :type grade_system_form: ``osid.grading.GradeSystemForm``
        :raise: ``IllegalState`` -- ``grade_system_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``grade_system_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_system_form`` did not originate from ``get_grade_system_form_for_update()``

        """
        pass

    def can_delete_grade_systems(self):
        """Tests if this user can delete grade systems.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``GradeSystem`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_grade_system(self, grade_system_id):
        """Deletes a ``GradeSystem``.

        :param grade_system_id: the ``Id`` of the ``GradeSystem`` to remove
        :type grade_system_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``grade_system_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_grade_system_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradeSystems``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradeSystem`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_grade_system(self, grade_system_id, alias_id):
        """Adds an ``Id`` to a ``GradeSystem`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradeSystem`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade system, it is
        reassigned to the given grade system ``Id``.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``grade_system_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_create_grades(self, grade_system_id):
        """Tests if this user can create ``Grade`` s for a ``GradeSystem``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: ``false`` if ``Grade`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        """
        return # boolean

    def can_create_grade_with_record_types(self, grade_system_id, grade_record_types):
        """Tests if this user can create a single ``Grade`` using the desired record types.

        While ``GradingManager.getGradeRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Grade``.
        Providing an empty array tests if a ``Grade`` can be created
        with no records.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param grade_record_types: array of grade recod types
        :type grade_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Grade`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``grade_record_types`` is ``null``

        """
        return # boolean

    def get_grade_form_for_create(self, grade_system_id, grade_record_types):
        """Gets the grade form for creating new grades.

        A new form should be requested for each create transaction.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param grade_record_types: array of grade recod types
        :type grade_record_types: ``osid.type.Type[]``
        :return: the grade form
        :rtype: ``osid.grading.GradeForm``
        :raise: ``NotFound`` -- ``grade_system_id`` is not found
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``grade_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.grading.GradeForm

    def create_grade(self, grade_form):
        """Creates a new ``Grade``.

        :param grade_form: the form for this ``Grade``
        :type grade_form: ``osid.grading.GradeForm``
        :return: the new ``Grade``
        :rtype: ``osid.grading.Grade``
        :raise: ``IllegalState`` -- ``grade_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``grade_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_form`` did not originate from ``get_grade_form_for_create()``

        """
        return # osid.grading.Grade

    def can_update_grades(self, grade_system_id):
        """Tests if this user can update ``Grades``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Grade``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: ``false`` if ``Grade`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        """
        return # boolean

    def get_grade_form_for_update(self, grade_id):
        """Gets the grade form for updating an existing grade.

        A new grade form should be requested for each update
        transaction.

        :param grade_id: the ``Id`` of the ``Grade``
        :type grade_id: ``osid.id.Id``
        :return: the grade form
        :rtype: ``osid.grading.GradeForm``
        :raise: ``NotFound`` -- ``grade_id`` is not found
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeForm

    def update_grade(self, grade_form):
        """Updates an existing grade.

        :param grade_form: the form containing the elements to be updated
        :type grade_form: ``osid.grading.GradeForm``
        :raise: ``IllegalState`` -- ``grade_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``grade_id`` or ``grade_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_form`` did not originate from ``get_grade_form_for_update()``

        """
        pass

    def can_delete_grades(self, grade_system_id):
        """Tests if this user can delete grades.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Grade``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :param grade_system_id: the ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: ``false`` if ``Grade`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``

        """
        return # boolean

    def delete_grade(self, grade_id):
        """Deletes a ``Grade``.

        :param grade_id: the ``Id`` of the ``Grade`` to remove
        :type grade_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``grade_id`` not found
        :raise: ``NullArgument`` -- ``grade_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_grade_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Grades``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Grade`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_grade(self, grade_id, alias_id):
        """Adds an ``Id`` to a ``Grade`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Grade`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade, it is
        reassigned to the given grade ``Id``.

        :param grade_id: the ``Id`` of a ``Grade``
        :type grade_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``grade_id`` not found
        :raise: ``NullArgument`` -- ``grade_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradeSystemNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``GradeSystems`` and the Grades defined within.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_register_for_grade_system_notifications(self):
        """Tests if this user can register for ``GradeSystem`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for grade systems in
        gradebooks which are children of this gradebook in the gradebook
        hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this gradebook only.



        """
        pass

    def register_for_new_grade_systems(self):
        """Register for notifications of new grade systems.

        ``GradeSystemReceiver.newGradeSystem()`` is invoked when a new
        ``GradeSystem`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_grade_systems(self):
        """Registers for notification of updated grade systems.

        ``GradeSystemReceiver.changedGradeSystem()`` is invoked when a
        system is changed or grades are changed within it.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_grade_system(self, grade_system_id):
        """Registers for notification of an updated grade system.

        ``GradeSystemReceiver.changedGradeSystem()`` is invoked when the
        specified grade system is changed or grades are changed within
        it.

        :param grade_system_id: the ``Id`` of the grade system to monitor
        :type grade_system_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``grade_system_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_grade_systems(self):
        """Registers for notification of deleted grade systems.

        ``GradeSystemReceiver.deletedGradeSystem()`` is invoked when a
        grade system is removed from this gradebook.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_grade_system(self, grade_system_id):
        """Registers for notification of a deleted grade system.

        ``GradeSystemReceiver.deletedGradeSystem()`` is invoked when the
        specified system is removed from this gradebook.

        :param grade_system_id: the ``Id`` of the grade system to monitor
        :type grade_system_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``grade_system_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradeSystemGradebookSession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``GradeSystem`` to ``Gradebook`` mappings.

    A ``GradeSystem`` may appear in multiple ``Gradebooks``. Each
    ``Gradebook`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_gradebook_view(self):
        """A complete view of the ``GradebookColumn`` and ``Gradebook`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def can_lookup_grade_system_gradebook_mappings(self):
        """Tests if this user can perform lookups of gradebook/grade system mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_system_ids_by_gradebook(self, gradebook_id):
        """Gets the list of ``GradeSystem``  ``Ids`` associated with a ``Gradebook``.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of related grade system ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_grade_systems_by_gradebook(self, gradebook_id):
        """Gets the list of grade systems associated with a ``Gradebook``.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of related grade systems
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystemList

    def get_grade_system_ids_by_gradebooks(self, gradebook_ids):
        """Gets the list of ``GradeSystem Ids`` corresponding to a list of ``Gradebooks``.

        :param gradebook_ids: list of gradebook ``Ids``
        :type gradebook_ids: ``osid.id.IdList``
        :return: list of grade systems ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_grade_systems_by_gradebooks(self, gradebook_ids):
        """Gets the list of grade systems corresponding to a list of ``Gradebooks``.

        :param gradebook_ids: list of gradebook ``Ids``
        :type gradebook_ids: ``osid.id.IdList``
        :return: list of grade systems
        :rtype: ``osid.grading.GradeSystemList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeSystemList

    def get_gradebook_ids_by_grade_system(self, grade_system_id):
        """Gets the list of ``Gradebook``  ``Ids`` mapped to a ``GradeSystem``.

        :param grade_system_id: ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: list of gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``grade_system_id`` is not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_gradebooks_by_grade_system(self, grade_system_id):
        """Gets the list of ``Gradebooks`` mapped to a ``GradeSystem``.

        :param grade_system_id: ``Id`` of a ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: list of gradebooks
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- ``grade_system_id`` is not found
        :raise: ``NullArgument`` -- ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList


class GradeSystemGradebookAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign grade systems to ``Gradebooks``.

    A ``GradeSystem`` may map to multiple ``Gradebooks`` and removing
    the last reference to a ``GradeSystem`` is the equivalent of
    deleting it. Each ``Gradebook`` may have its own authorizations
    governing who is allowed to operate on it.

    Moving or adding a reference of a ``GradeSystem`` to another
    ``Gradebook`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    def can_assign_grade_system(self):
        """Tests if this user can alter grade system/gradebook mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_assign_grade_systems_to_gradebook(self, gradebook_id):
        """Tests if this user can alter grade system/gradebook mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        """
        return # boolean

    def get_assignable_gradebook_ids(self, gradebook_id):
        """Gets a list of gradebooks including and under the given gradebook node in which any grade system can be assigned.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of assignable gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def get_assignable_gradebook_ids_for_grade_system(self, gradebook_id, grade_system_id):
        """Gets a list of gradebooks including and under the given gradebook node in which a specific grade system can be assigned.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param grade_system_id: the ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :return: list of assignable gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``grade_system_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def assign_grade_system_to_gradebook(self, grade_system_id, gradebook_id):
        """Adds an existing ``GradeSystem`` to a ``Gradebook``.

        :param grade_system_id: the ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``grade_system_id`` is already assigned to ``gradebook_id``
        :raise: ``NotFound`` -- ``grade_system_id`` or ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def unassign_grade_system_from_gradebook(self, grade_system_id, gradebook_id):
        """Removes a ``GradeSystem`` from a ``Gradebook``.

        :param grade_system_id: the ``Id`` of the ``GradeSystem``
        :type grade_system_id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``grade_system_id`` or ``gradebook_id`` not found or ``grade_system_id`` not assigned to ``gradebook_id``
        :raise: ``NullArgument`` -- ``grade_system_id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradeSystemSmartGradebookSession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``GradeSystemQuery`` can be retrieved from this session and mapped
    to this ``Gradebook`` to create a virtual collection of
    ``GradeSystems``. The entries may be sequenced using the
    ``GradeSystemSearchOrder`` from this session.

    This ``Gradebook`` has a default query that matches any grade system
    and a default search order that specifies no sequencing. The queries
    may be examined using a ``GradeSystemQueryInspector``. The query may
    be modified by converting the inspector back to a
    ``GradeSystemQuery``.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_manage_smart_gradebooks(self):
        """Tests if this user can manage smart gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        :return: ``false`` if smart gradebook methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_system_query(self):
        """Gets a grade system query.

        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``

        """
        return # osid.grading.GradeSystemQuery

    grade_system_query = property(fget=get_grade_system_query)

    def get_grade_system_search_order(self):
        """Gets a grade system search order.

        :return: the grade system search order
        :rtype: ``osid.grading.GradeSystemSearchOrder``

        """
        return # osid.grading.GradeSystemSearchOrder

    grade_system_search_order = property(fget=get_grade_system_search_order)

    def apply_grade_system_query(self, grade_system_query):
        """Applies a grade system query to this gradebook.

        :param grade_system_query: the grade system query
        :type grade_system_query: ``osid.grading.GradeSystemQuery``
        :raise: ``NullArgument`` -- ``grade_system_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``grade_system_query`` not of this service

        """
        pass

    def inspect_grade_system_query(self):
        """Gets a grade system query inspector for this gradebook.

        :return: the grade system query inspector
        :rtype: ``osid.grading.GradeSystemQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.grading.GradeSystemQueryInspector

    def apply_grade_system_sequencing(self, grade_system_search_order):
        """Applies a grade system search order to this gradebook.

        :param grade_system_search_order: the grade system search order
        :type grade_system_search_order: ``osid.grading.GradeSystemSearchOrder``
        :raise: ``NullArgument`` -- ``grade_system_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``grade_system_search_order`` not of this service

        """
        pass

    def get_grade_system_query_from_inspector(self, grade_system_query_inspector):
        """Gets a grade system query from an inspector.

        :param grade_system_query_inspector: a grade system query inspector
        :type grade_system_query_inspector: ``osid.grading.GradeSystemQueryInspector``
        :return: the grade system query
        :rtype: ``osid.grading.GradeSystemQuery``
        :raise: ``NullArgument`` -- ``grade_system_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``grade_system_query_inspector`` is not of this service

        """
        return # osid.grading.GradeSystemQuery


class GradeEntryLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``GradeEntrie`` s."""
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_lookup_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_grade_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_grade_entry_view(self):
        """A complete view of the ``GradeEntry`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.



        """
        pass

    def use_effective_grade_entry_view(self):
        """Only grade entries whose effective dates are current are returned by methods in this session."""
        pass

    def use_any_effective_grade_entry_view(self):
        """All grade entries of any effective dates are returned by methods in this session."""
        pass

    def get_grade_entry(self, grade_entry_id):
        """Gets the ``GradeEntry`` specified by its ``Id``.

        :param grade_entry_id: ``Id`` of the ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``
        :return: the grade entry
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``NotFound`` -- ``grade_entry_id`` not found
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntry

    def get_grade_entries_by_ids(self, grade_entry_ids):
        """Gets a ``GradeEntryList`` corresponding to the given ``IdList``.

        :param grade_entry_ids: the list of ``Ids`` to retrieve
        :type grade_entry_ids: ``osid.id.IdList``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``grade_entry_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` which does not include grade entries of genus types derived from the specified ``Type``.

        :param grade_entry_genus_type: a grade entry genus type
        :type grade_entry_genus_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_parent_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` and include any additional grade entry with genus types derived from the specified ``Type``.

        :param grade_entry_genus_type: a grade entry genus type
        :type grade_entry_genus_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_record_type(self, grade_entry_record_type):
        """Gets a ``GradeEntryList`` containing the given grade entry record ``Type``.

        :param grade_entry_record_type: a grade entry record type
        :type grade_entry_record_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_on_date(self, from_, to):
        """Gets a ``GradeEntryList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column(self, gradebook_column_id):
        """Gets a ``GradeEntryList`` for the gradebook column.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column_on_date(self, gradebook_column_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column and effective during the entire given date range inclusive but not confined to the date range.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``gradebook_column_id, from, or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_resource(self, resource_id):
        """Gets a ``GradeEntryList`` for the given key key resource.

        :param resource_id: a key resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_resource_on_date(self, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given key resource and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from, or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column_and_resource(self, gradebook_column_id, resource_id):
        """Gets a ``GradeEntryList`` for the gradebook column and key resource.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param resource_id: a key resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column_and_resource_on_date(self, gradebook_column_id, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column, resource, and effective during the entire given date range inclusive but not confined to the date range.

        :param gradebook_column_id: a gradebook column ``Id``
        :type gradebook_column_id: ``osid.id.Id``
        :param resource_id: a key resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``gradebook_column_id, resource, from, or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_grader(self, resource_id):
        """Gets a ``GradeEntryList`` for the given grader.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    def get_grade_entries(self):
        """Gets all grade entries.

        :return: a ``GradeEntryList``
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryList

    grade_entries = property(fget=get_grade_entries)


class GradeEntryQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching ``GradeEntry`` objects.

    The search query is constructed using the ``GradeEntryQuery``. The
    grade entry record ``Type`` also specifies the record interface for
    the grade entry query.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated gradebook view: searches include grade entries in
        gradebooks of which this gradebook is a ancestor in the
        gradebook hierarchy
      * isolated gradebook view: searches are restricted to grade
        entries in this gradebook

    
    Grade entries may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradeEntryQuery``.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_search_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.



        """
        pass

    def get_grade_entry_query(self):
        """Gets a grade entry query.

        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``

        """
        return # osid.grading.GradeEntryQuery

    grade_entry_query = property(fget=get_grade_entry_query)

    def get_grade_entries_by_query(self, grade_entry_query):
        """Gets a list of entries matching the given grade entry query.

        :param grade_entry_query: the grade entry query
        :type grade_entry_query: ``osid.grading.GradeEntryQuery``
        :return: the returned ``GradeEntryList``
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_query`` is not of this service

        """
        return # osid.grading.GradeEntryList


class GradeEntrySearchSession(GradeEntryQuerySession):
    """This session provides methods for searching ``GradeEntry`` objects.

    The search query is constructed using the ``GradeEntryQuery``.

    ``get_grade_entries_by_query()`` is the basic search method and
    returns a list of ``GradeEntry`` objects.A more advanced search may
    be performed with ``getGradeEntriesBySearch()``. It accepts a
    ``GradeEntrySearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_grade_entries_by_search()`` returns a
    ``GradeEntrySearchResults`` that can be used to access the resulting
    ``GradeEntryList`` or be used to perform a search within the result
    set through ``GradeEntrySearch``.
    
    This session defines views that offer differing behaviors for
    searching.
    
      * federated gradebook view: searches include grade entries in
        gradebooks of which this gradebook is a ancestor in the
        gradebook hierarchy
      * isolated gradebook view: searches are restricted to grade
        entries in this gradebook

    
    Grade entries may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradeEntryQuery``.

    """
    def get_grade_entry_search(self):
        """Gets a grade entry search.

        :return: the grade entry search
        :rtype: ``osid.grading.GradeEntrySearch``

        """
        return # osid.grading.GradeEntrySearch

    grade_entry_search = property(fget=get_grade_entry_search)

    def get_grade_entry_search_order(self):
        """Gets a grade entry search order.

        The ``GradeEntrySearchOrder`` is supplied to a
        ``GradeEntrySearch`` to specify the ordering of results.

        :return: the grade entry search order
        :rtype: ``osid.grading.GradeEntrySearchOrder``

        """
        return # osid.grading.GradeEntrySearchOrder

    grade_entry_search_order = property(fget=get_grade_entry_search_order)

    def get_grade_entries_by_search(self, grade_entry_query, grade_entry_search):
        """Gets the search results matching the given search query using the given search.

        :param grade_entry_query: the grade entry query
        :type grade_entry_query: ``osid.grading.GradeEntryQuery``
        :param grade_entry_search: the grade entry search
        :type grade_entry_search: ``osid.grading.GradeEntrySearch``
        :return: the grade entry search results
        :rtype: ``osid.grading.GradeEntrySearchResults``
        :raise: ``NullArgument`` -- ``grade_entry_query`` or ``grade_entry_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_search`` or ``grade_entry_query`` is not of this service

        """
        return # osid.grading.GradeEntrySearchResults

    def get_grade_entry_query_from_inspector(self, grade_entry_query_inspector):
        """Gets a grade entry query from an inspector.

        The inspector is available from an ``GradeEntrySearchResults``.

        :param grade_entry_query_inspector: a grade entry query inspector
        :type grade_entry_query_inspector: ``osid.grading.GradeEntryQueryInspector``
        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``
        :raise: ``NullArgument`` -- ``grade_entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``grade_entry_query_inspector`` is not of this service

        """
        return # osid.grading.GradeEntryQuery


class GradeEntryAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``GradeEntries``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``GradeEntry,`` a ``GradeEntryForm`` is requested using
    ``get_grade_entry_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradeEntryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``GradeEntryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``GradeEntryForm``
    corresponds to an attempted transaction.
    
    For updates, ``GradeEntryForms`` are requested to the ``GradeEntry``
    ``Id`` that is to be updated using ``getGradeEntryFormForUpdate()``.
    Similarly, the ``GradeEntryForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``GradeEntryForm`` can only be used once for a
    successful update and cannot be reused.
    
    The delete operations delete ``GradeEntries``. To unmap a
    ``GradeEntry`` from the current ``Gradebook,`` the
    ``GradeEntryGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradeEntry`` itself thus
    removing it from all known ``Gradebook`` catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_create_grade_entries(self):
        """Tests if this user can create grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_grade_entry_with_record_types(self, grade_entry_record_types):
        """Tests if this user can create a single ``GradeEntry`` using the desired record types.

        While ``GradingManager.getGradeEntryRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``GradeEntry``.
        Providing an empty array tests if a ``GradeEntry`` can be
        created with no records.

        :param grade_entry_record_types: array of grade entry record types
        :type grade_entry_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``GradeEntry`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_record_types`` is ``null``

        """
        return # boolean

    def get_grade_entry_form_for_create(self, gradebook_column_id, resource_id, grade_entry_record_types):
        """Gets the grade entry form for creating new grade entries.

        A new form should be requested for each create transaction.

        :param gradebook_column_id: the gradebook column
        :type gradebook_column_id: ``osid.id.Id``
        :param resource_id: the key resource
        :type resource_id: ``osid.id.Id``
        :param grade_entry_record_types: array of grade entry record types
        :type grade_entry_record_types: ``osid.type.Type[]``
        :return: the grade entry form
        :rtype: ``osid.grading.GradeEntryForm``
        :raise: ``NotFound`` -- ``gradebook_column_id or resource_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_id, resource_id,`` or ``grade_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.grading.GradeEntryForm

    def create_grade_entry(self, grade_entry_form):
        """Creates a new ``GradeEntry``.

        :param grade_entry_form: the form for this ``GradeEntry``
        :type grade_entry_form: ``osid.grading.GradeEntryForm``
        :return: the new ``GradeEntry``
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``IllegalState`` -- ``grade_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``grade_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_form`` did not originate from ``get_grade_entry_form_for_create()``

        """
        return # osid.grading.GradeEntry

    def can_overridecalculated_grade_entries(self):
        """Tests if this user can override grade entries calculated from another.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` override is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_entry_form_for_override(self, grade_entry_id, grade_entry_record_types):
        """Gets the grade entry form for overriding calculated grade entries.

        A new form should be requested for each create transaction.

        :param grade_entry_id: the ``Id`` of the grade entry to be overridden
        :type grade_entry_id: ``osid.id.Id``
        :param grade_entry_record_types: array of grade entry record types
        :type grade_entry_record_types: ``osid.type.Type[]``
        :return: the grade entry form
        :rtype: ``osid.grading.GradeEntryForm``
        :raise: ``AlreadyExists`` -- ``grade_entry_id`` is already overridden
        :raise: ``NotFound`` -- ``grade_entry_id`` not found or ``grade_entry_id`` is not a calculated entry
        :raise: ``NullArgument`` -- ``grade_entry_id`` or ``grade_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.grading.GradeEntryForm

    def override_calculated_grade_entry(self, grade_entry_form):
        """Creates a new overriding ``GradeEntry``.

        :param grade_entry_form: the form for this ``GradeEntry``
        :type grade_entry_form: ``osid.grading.GradeEntryForm``
        :return: the new ``GradeEntry``
        :rtype: ``osid.grading.GradeEntry``
        :raise: ``IllegalState`` -- ``grade_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``grade_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_form`` did not originate from ``get_grade_entry_form_for_override()``

        """
        return # osid.grading.GradeEntry

    def can_update_grade_entries(self):
        """Tests if this user can update grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if grade entry modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_grade_entry_form_for_update(self, grade_entry_id):
        """Gets the grade entry form for updating an existing entry.

        A new grade entry form should be requested for each update
        transaction.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``
        :return: the grade entry form
        :rtype: ``osid.grading.GradeEntryForm``
        :raise: ``NotFound`` -- ``grade_entry_id`` is not found
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradeEntryForm

    def update_grade_entry(self, grade_entry_form):
        """Updates an existing grade entry.

        :param grade_entry_form: the form containing the elements to be updated
        :type grade_entry_form: ``osid.grading.GradeEntryForm``
        :raise: ``IllegalState`` -- ``grade_entry_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``grade_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``grade_entry_form`` did not originate from ``get_grade_entry_form_for_update()``

        """
        pass

    def can_delete_grade_entries(self):
        """Tests if this user can delete grade entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradeEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_grade_entry(self, grade_entry_id):
        """Deletes the ``GradeEntry`` identified by the given ``Id``.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry`` to delete
        :type grade_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``GradeEntry`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``grade_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_grade_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradeEntries``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradeEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_grade_entry(self, grade_entry_id, alias_id):
        """Adds an ``Id`` to a ``GradeEntry`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradeEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another grade entry, it is
        reassigned to the given grade entry ``Id``.

        :param grade_entry_id: the ``Id`` of a ``GradeEntry``
        :type grade_entry_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``grade_entry_id`` not found
        :raise: ``NullArgument`` -- ``grade_entry_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradeEntryNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive asynchronous notifications on adds/changes to ``GradeEntry`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The views defined in this session correspond to the views in the
    ``GradeEntryLookupSession``.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_register_for_grade_entry_notifications(self):
        """Tests if this user can register for ``GradeEntry`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for grade entries in
        gradebooks which are children of this gradebook in the gradebook
        hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this gradebook only.



        """
        pass

    def register_for_new_grade_entries(self):
        """Register for notifications of new grade entries.

        ``GradeEntryReceiver.newGradeEntry()`` is invoked when a new
        grade entry is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_grade_entries_in_column(self, gradebook_column_id):
        """Registers for notification of a new grade entry for the specified gradebook column.

        ``GradeEntryReceiver.newGradeEntry()`` is invoked when a new
        entry for the resource is created.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_grade_entries_for_resource(self, resource_id):
        """Registers for notification of a new grade entry for the specified resource.

        ``GradeEntryReceiver.newGradeEntry()`` is invoked when a new
        entry for the resource is created.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_grade_entries_by_grader(self, resource_id):
        """Registers for notification of a new grade entry for the specified grader agent.

        ``GradeEntryReceiver.newGradeEntry()`` is invoked when a new
        entry for the grader is created.

        :param resource_id: the ``Id`` of the ``Agent`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_grade_entries(self):
        """Registers for notification of updated grade entries.

        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when a
        grade entry is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_grade_entries_in_column(self, gradebook_column_id):
        """Registers for notification of an updated grade entry for the specified gradebook column.

        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the column is updated.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_grade_entries_for_resource(self, resource_id):
        """Registers for notification of an updated grade entry for the specified key resource.

        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the resource is updated.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_grade_entries_by_grader(self, resource_id):
        """Registers for notification of an updated grade entry for the specified grader.

        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the agent is updated.

        :param resource_id: the ``Id`` of the ``Agent`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_grade_entry(self, grade_entry_id):
        """Registers for notification of an updated grade entry.

        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when the
        specified grade entry is changed.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry`` to monitor
        :type grade_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``grade_entry_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_grade_entries(self):
        """Registers for notification of deleted grade entries.

        ``GradeEntryReceiver.deletedGradeEntry()`` is invoked when a
        grade entry is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_grade_entries_in_column(self, gradebook_column_id):
        """Registers for notification of a deleted grade entry for the specified gradebook column.

        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the column is removed from this gradebook.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_grade_entries_for_resource(self, resource_id):
        """Registers for notification of a deleted grade entry for the specified key resource.

        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the resource is removed from this gradebook.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_grade_entries_by_grader(self, resource_id):
        """Registers for notification of a deleted grade entry for the specified grader.

        ``GradeEntryReceiver.changedGradeEntry()`` is invoked when an
        entry for the agent is removed from this gradebook.

        :param resource_id: the ``Id`` of the ``Agent`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_grade_entry(self, grade_entry_id):
        """Registers for notification of a deleted grade entry.

        ``GradeEntryReceiver.deletedGradeEntry()`` is invoked when the
        specified entry is deleted.

        :param grade_entry_id: the ``Id`` of the ``GradeEntry`` to monitor
        :type grade_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``grade_entry_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradebookColumnLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``GradebookColumns``."""
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_lookup_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_gradebook_column_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_gradebook_column_view(self):
        """A complete view of the ``GradebookColumn`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this gradebook only.



        """
        pass

    def get_gradebook_column(self, gradebook_column_id):
        """Gets the ``GradebookColumn`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``GradebookColumn`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``GradebookColumn`` and
        retained for compatibility.

        :param gradebook_column_id: ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the gradebook column
        :rtype: ``osid.grading.GradebookColumn``
        :raise: ``NotFound`` -- ``gradebook_column_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumn

    def get_gradebook_columns_by_ids(self, gradebook_column_ids):
        """Gets a ``GradebookColumnList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the gradebook
        columns specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if a ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible gradeboook columns may be omitted from the list.

        :param gradebook_column_ids: the list of ``Ids`` to retrieve
        :type gradebook_column_ids: ``osid.id.IdList``
        :return: the returned ``GradebookColumn`` list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``grade_book_column_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_columns_by_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` which does not include gradebook columns of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :param gradebook_column_genus_type: a gradebook column genus type
        :type gradebook_column_genus_type: ``osid.type.Type``
        :return: the returned ``GradebookColumn`` list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_column_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_columns_by_parent_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` and include any additional columns with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :param gradebook_column_genus_type: a gradebook column genus type
        :type gradebook_column_genus_type: ``osid.type.Type``
        :return: the returned ``GradebookColumn`` list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_column_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_columns_by_record_type(self, gradebook_column_record_type):
        """Gets a ``GradebookColumnList`` containing the given gradebook column record ``Type``.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :param gradebook_column_record_type: a gradebook column record type
        :type gradebook_column_record_type: ``osid.type.Type``
        :return: the returned ``GradebookColumn`` list
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_column_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_columns(self):
        """Gets all gradebook columns.

        In plenary mode, the returned list contains all known gradebook
        columns or an error results. Otherwise, the returned list may
        contain only those gradebook columns that are accessible through
        this session.

        :return: a ``GradebookColumn``
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumnList

    gradebook_columns = property(fget=get_gradebook_columns)

    def supports_summary(self):
        """Tests if a summary entry is available.

        :return: ``true`` if a summary entry is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_column_summary(self, gradebook_column_id):
        """Gets the ``GradebookColumnSummary`` for summary results.

        :param gradebook_column_id: ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the gradebook column summary
        :rtype: ``osid.grading.GradebookColumnSummary``
        :raise: ``NotFound`` -- ``gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unimplemented`` -- ``has_summary()`` is ``false``

        """
        return # osid.grading.GradebookColumnSummary


class GradebookColumnQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching ``GradebookColumn`` objects.

    The search query is constructed using the ``GradebookColumnQuery``.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated gradebook view: searches include columns in gradebooks
        of which this gradebook is a ancestor in the gradebook hierarchy
      * isolated gradebook view: searches are restricted to columns in
        this gradebook

    
    Gradebook columns may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``GradebookColumnQuery``.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_search_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this gradebook only.



        """
        pass

    def get_gradebook_column_query(self):
        """Gets a gradebook column query.

        :return: the gradebook column
        :rtype: ``osid.grading.GradebookColumnQuery``

        """
        return # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)

    def get_gradebook_columns_by_query(self, gradebook_column_query):
        """Gets a list of gradebook columns matching the given query.

        :param gradebook_column_query: the gradebook column query
        :type gradebook_column_query: ``osid.grading.GradebookColumnQuery``
        :return: the returned ``GradebookColumnList``
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_column_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_query`` is not of this service

        """
        return # osid.grading.GradebookColumnList


class GradebookColumnSearchSession(GradebookColumnQuerySession):
    """This session provides methods for searching ``GradebookColumn`` objects.

    The search query is constructed using the ``GradebookColumnQuery``.

    ``get_gradebook_columns_by_query()`` is the basic search method and
    returns a list of ``GradebookColumn`` objects.A more advanced search
    may be performed with ``getGradebookColumnsBySearch()``. It accepts
    a ``GradebookColumnSearch`` in addition to the query for the purpose
    of specifying additional options affecting the entire search, such
    as ordering. ``get_gradebook_columns_by_search()`` returns a
    ``GradebookColumnSearchResults`` that can be used to access the
    resulting ``GradebookColumnList`` or be used to perform a search
    within the result set through ``GradebookColumnSearch``.
    
    This session defines views that offer differing behaviors for
    searching.
    
      * federated gradebook view: searches include columns in gradebooks
        of which this gradebook is a ancestor in the gradebook hierarchy
      * isolated gradebook view: searches are restricted to columns in
        this gradebook

    
    Gradebook columns may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``GradebookColumnQuery``.

    """
    def get_gradebook_column_search(self):
        """Gets a gradebook column search.

        :return: the gradebook column search
        :rtype: ``osid.grading.GradebookColumnSearch``

        """
        return # osid.grading.GradebookColumnSearch

    gradebook_column_search = property(fget=get_gradebook_column_search)

    def get_gradebook_column_search_order(self):
        """Gets a gradebook column search order.

        The ``GradebookColumnSearchOrder`` is supplied to a
        ``GradebookColumnSearch`` to specify the ordering of results.

        :return: the gradebook column search order
        :rtype: ``osid.grading.GradebookColumnSearchOrder``

        """
        return # osid.grading.GradebookColumnSearchOrder

    gradebook_column_search_order = property(fget=get_gradebook_column_search_order)

    def get_gradebook_columns_by_search(self, gradebook_column_query, gradebook_column_search):
        """Gets the search results matching the given search query using the given search.

        :param gradebook_column_query: the gradebook column query
        :type gradebook_column_query: ``osid.grading.GradebookColumnQuery``
        :param gradebook_column_search: the gradebook column search
        :type gradebook_column_search: ``osid.grading.GradebookColumnSearch``
        :return: the gradebook column search results
        :rtype: ``osid.grading.GradebookColumnSearchResults``
        :raise: ``NullArgument`` -- ``gradebook_column_query`` or ``gradebook_column_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_search`` or ``gradebook_column_query`` is not of this service

        """
        return # osid.grading.GradebookColumnSearchResults

    def get_gradebook_column_query_from_inspector(self, gradebook_column_query_inspector):
        """Gets a gradebook column query from an inspector.

        The inspector is available from an
        ``GradebookColumnSearchResults``.

        :param gradebook_column_query_inspector: a gradebook column query inspector
        :type gradebook_column_query_inspector: ``osid.grading.GradebookColumnQueryInspector``
        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``NullArgument`` -- ``gradebook_column_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``gradebook_column_query_inspector`` is not of this service

        """
        return # osid.grading.GradebookColumnQuery


class GradebookColumnAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``GradebookColumns``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``GradebookColumn,`` a ``GradebookColumnForm`` is requested using
    ``get_gradebook_column_form_for_create()`` specifying the desired
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``GradebookColumnForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``GradebookColumnForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``GradebookColumnForm`` corresponds to an attempted transaction.
    
    For updates, ``GradebookColumnForms`` are requested to the
    ``GradebookColumn``  ``Id`` that is to be updated using
    ``getGradebookColumnFormForUpdate()``. Similarly, the
    ``GradebookColumnForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``GradebookColumnForm`` can only be used once for a successful
    update and cannot be reused.
    
    The delete operations delete ``GradebookColumns`` To unmap a
    ``GradebookColumn`` from the current ``Gradebook,`` the
    ``GradebookColumnGradebookAssignmentSession`` should be used. These
    delete operations attempt to remove the ``GradebookColumnForm``
    itself thus removing it from all known ``Gradebook`` catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_create_gradebook_columns(self):
        """Tests if this user can create gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a gradebook
        column will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_gradebook_column_with_record_types(self, gradebook_column_record_types):
        """Tests if this user can create a single ``GradebookColumn`` using the desired record types.

        While ``GradingManager.getGradebookColumnRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``GradebookColumn``. Providing an empty array tests if a
        ``GradebookColumn`` can be created with no records.

        :param gradebook_column_record_types: array of gradebook column record types
        :type gradebook_column_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``GradebookColumn`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_types`` is ``null``

        """
        return # boolean

    def get_gradebook_column_form_for_create(self, gradebook_column_record_types):
        """Gets the gradebook column form for creating new gradebook columns.

        A new form should be requested for each create transaction.

        :param gradebook_column_record_types: array of gradebook column record types
        :type gradebook_column_record_types: ``osid.type.Type[]``
        :return: the gradebook column form
        :rtype: ``osid.grading.GradebookColumnForm``
        :raise: ``NullArgument`` -- ``gradebook_column_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.grading.GradebookColumnForm

    def create_gradebook_column(self, gradebook_column_form):
        """Creates a new ``GradebookColumn``.

        :param gradebook_column_form: the form for this ``GradebookColumn``
        :type gradebook_column_form: ``osid.grading.GradebookColumnForm``
        :return: the new ``GradebookColumn``
        :rtype: ``osid.grading.GradebookColumn``
        :raise: ``IllegalState`` -- ``gradebook_column_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``gradebook_column_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_form`` did not originate from ``get_gradebook_column_form_for_create()``

        """
        return # osid.grading.GradebookColumn

    def can_update_gradebook_columns(self):
        """Tests if this user can update gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if gradebook column modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_column_form_for_update(self, gradebook_column_id):
        """Gets the gradebook column form for updating an existing gradebook column.

        A new gradebook column form should be requested for each update
        transaction.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: the gradebook column form
        :rtype: ``osid.grading.GradebookColumnForm``
        :raise: ``NotFound`` -- ``gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumnForm

    def update_gradebook_column(self, gradebook_column_form):
        """Updates an existing gradebook column.

        :param gradebook_column_form: the form containing the elements to be updated
        :type gradebook_column_form: ``osid.grading.GradebookColumnForm``
        :raise: ``IllegalState`` -- ``gradebook_column_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``gradebook_column_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_column_form`` did not originate from ``get_gradebook_column_form_for_update()``

        """
        pass

    def sequence_gradebook_columns(self, gradebook_column_ids):
        """Resequences the gradebook columns.

        :param gradebook_column_ids: the ``Ids`` of the ``GradebookColumns``
        :type gradebook_column_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_column_id_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def move_gradebook_column(self, front_gradebook_column_id, back_gradebook_column_id):
        """Moves a gradebook column in front of another.

        :param front_gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type front_gradebook_column_id: ``osid.id.Id``
        :param back_gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type back_gradebook_column_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``front_gradebook_column_id or back_gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``front_gradebook_column_id or back_gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def copy_gradebook_column_entries(self, source_gradebook_column_id, target_gradebook_column_id):
        """Copies gradebook column entries from one column to another.

        If the target grade column grade system differs from the source,
        the grades in the entries are transformed to the new grade
        system.

        :param source_gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type source_gradebook_column_id: ``osid.id.Id``
        :param target_gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type target_gradebook_column_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``source_gradebook_column_id ortarget_gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``source_gradebook_column_id target_gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_delete_gradebook_columns(self):
        """Tests if this user can delete gradebook columns.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``GradebookColumn`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_gradebook_column(self, gradebook_column_id):
        """Deletes the ``GradebookColumn`` identified by the given ``Id``.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to delete
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``GradebookColumn`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_gradebook_column_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``GradebookColumns``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``GradebookColumn`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_gradebook_column(self, gradebook_column_id, alias_id):
        """Adds an ``Id`` to a ``GradebookColumn`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``GradebookColumn`` is determined by
        the provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another gradebook column,
        it is reassigned to the given gradebook column ``Id``.

        :param gradebook_column_id: the ``Id`` of a ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``gradebook_column_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradebookColumnNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive asynchronous notifications on adds/changes to ``GradebookColumn`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The views defined in this session correspond to the views in the
    ``GradebookColumnLookupSession``.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_register_for_gradebook_column_notifications(self):
        """Tests if this user can register for ``GradebookColumn`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for gradebook
        columns in gradebooks which are children of this gradebook in
        the gradebook hierarchy.



        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this gradebook only.



        """
        pass

    def register_for_new_gradebook_columns(self):
        """Register for notifications of new gradebook columns.

        ``GradebookColumnReceiver.newGradebookColumny()`` is invoked
        when a new column is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_gradebook_columns(self):
        """Registers for notification of updated gradebook columns.

        ``GradebookColumnReceiver.changedGradebookColumn()`` is invoked
        when a gradebook column is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_gradebook_column(self, gradebook_column_id):
        """Registers for notification of an updated gradebook column.

        ``GradebookColumnReceiver.changedGradebookColumn()`` is invoked
        when the specified gradebook column is changed.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_gradebook_columns(self):
        """Registers for notification of deleted gradebook columns.

        ``GradebookColumnReceiver.deletedGradebookColumn()`` is invoked
        when a gradebook column is removed from this gradebook.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_gradebook_column(self, gradebook_column_id):
        """Registers for notification of a deleted gradebook column.

        ``GradebookColumnReceiver.deletedGradebookColumn()`` is invoked
        when the specified column is removed from thia gradebook.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn`` to monitor
        :type gradebook_column_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_column_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradebookColumnGradebookSession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``GradebookColumn`` to ``Gradebook`` mappings.

    A ``GradebookColumn`` may appear in multiple ``Gradebooks``. Each
    ``Gradebook`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_gradebook_view(self):
        """A complete view of the ``GradebookColumn`` and ``Gradebook`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def can_lookup_gradebook_column_gradebook_mappings(self):
        """Tests if this user can perform lookups of gradebook/column mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_column_ids_by_gradebook(self, gradebook_id):
        """Gets the list of ``GradebookColumn``  ``Ids`` associated with a ``Gradebook``.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of related gradebook column ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_gradebook_columns_by_gradebook(self, gradebook_id):
        """Gets the list of gradebook columns associated with a ``Gradebook``.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of related gradebook columns
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_column_ids_by_gradebooks(self, gradebook_ids):
        """Gets the list of ``GradebookColumn Ids`` corresponding to a list of ``Gradebooks``.

        :param gradebook_ids: list of gradebook ``Ids``
        :type gradebook_ids: ``osid.id.IdList``
        :return: list of gradebook column ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_gradebook_columns_by_gradebooks(self, gradebook_ids):
        """Gets the list of gradebook columns corresponding to a list of ``Gradebooks``.

        :param gradebook_ids: list of gradebook ``Ids``
        :type gradebook_ids: ``osid.id.IdList``
        :return: list of gradebook columns
        :rtype: ``osid.grading.GradebookColumnList``
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_ids_by_gradebook_column(self, gradebook_column_id):
        """Gets the list of ``Gradebook``  ``Ids`` mapped to a ``GradebookColumn``.

        :param gradebook_column_id: ``Id`` of a ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: list of gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_gradebooks_by_gradebook_column(self, gradebook_column_id):
        """Gets the list of ``Gradebooks`` mapped to a ``GradebookColumn``.

        :param gradebook_column_id: ``Id`` of a ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: list of gradebooks
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- ``gradebook_column_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList


class GradebookColumnGradebookAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign gradebook columns to ``Gradebooks``.

    A ``GradebookColumn`` may map to multiple ``Gradebooks`` and
    removing the last reference to a ``GradebookColumn`` is the
    equivalent of deleting it. Each ``Gradebook`` may have its own
    authorizations governing who is allowed to operate on it.

    Moving or adding a reference of a ``GradebookColumn`` to another
    ``Gradebook`` is not a copy operation (eg: does not change its
    ``Id`` ).

    """
    def can_assign_gradebook_columns(self):
        """Tests if this user can alter gradebook column/gradebook mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_assign_gradebook_columns_to_gradebook(self, gradebook_id):
        """Tests if this user can alter gradebook column/gradebook mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``

        """
        return # boolean

    def get_assignable_gradebook_ids(self, gradebook_id):
        """Gets a list of gradebook ``Ids`` including and under the given gradebook node in which any gradebook column can be assigned.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: list of assignable gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def get_assignable_gradebook_ids_for_gradebook_column(self, gradebook_id, gradebook_column_id):
        """Gets a list of gradebooks including and under the given gradebook node in which a specific gradebook column can be assigned.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param gradebook_column_id: the ``Id`` of the ``GradebokColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :return: list of assignable gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``gradebook_column_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def assign_gradebook_column_to_gradebook(self, gradebook_column_id, gradebook_id):
        """Adds an existing ``GradebookColumn`` to a ``Gradebook``.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``gradebook_column_id`` is already assigned to ``gradebook_id``
        :raise: ``NotFound`` -- ``gradebook_column_id`` or ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_column_id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def unassign_gradebook_column_from_gradebook(self, gradebook_column_id, gradebook_id):
        """Removes a ``GradebookColumn`` from a ``Gradebook``.

        :param gradebook_column_id: the ``Id`` of the ``GradebookColumn``
        :type gradebook_column_id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_column_id`` or ``gradebook_id`` not found or ``gradebook_column_id`` not assigned to ``gradebook_id``
        :raise: ``NullArgument`` -- ``gradebook_column_id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradebookColumnSmartGradebookSession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``GradebookColumnQuery`` can be retrieved from this session and
    mapped to this ``Gradebook`` to create a virtual collection of
    ``GradebookColumns``. The entries may be sequenced using the
    ``GradebookColumnSearchOrder`` from this session.

    This ``Gradebook`` has a default query that matches any gradebook
    column and a default search order that specifies no sequencing. The
    queries may be examined using a ``GradebookColumnQueryInspector``.
    The query may be modified by converting the inspector back to a
    ``GradebookColumnQuery``.

    """
    def get_gradebook_id(self):
        """Gets the ``Gradebook``  ``Id`` associated with this session.

        :return: the ``Gradebook Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        """Gets the ``Gradebook`` associated with this session.

        :return: the ``Gradebook`` associated with this session
        :rtype: ``osid.grading.Gradebook``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    gradebook = property(fget=get_gradebook)

    def can_manage_smart_gradebooks(self):
        """Tests if this user can manage smart gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        :return: ``false`` if smart gradebook methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_column_query(self):
        """Gets a gradebook column query.

        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``

        """
        return # osid.grading.GradebookColumnQuery

    gradebook_column_query = property(fget=get_gradebook_column_query)

    def get_gradebook_column_search_order(self):
        """Gets a gradebook column search order.

        :return: the gradebook column search order
        :rtype: ``osid.grading.GradebookColumnSearchOrder``

        """
        return # osid.grading.GradebookColumnSearchOrder

    gradebook_column_search_order = property(fget=get_gradebook_column_search_order)

    def apply_gradebook_column_query(self, gradebook_column_query):
        """Applies a gradebook column query to this gradebook.

        :param gradebook_column_query: the gradebook column query
        :type gradebook_column_query: ``osid.grading.GradebookColumnQuery``
        :raise: ``NullArgument`` -- ``gradebook_column_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``gradebook_column_query`` not of this service

        """
        pass

    def inspect_gradebook_column_query(self):
        """Gets a gradebook column query inspector for this gradebook.

        :return: the gradebook column query inspector
        :rtype: ``osid.grading.GradebookColumnQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.grading.GradebookColumnQueryInspector

    def apply_gradebook_column_sequencing(self, gradebook_column_search_order):
        """Applies a gradebook column search order to this gradebook.

        :param gradebook_column_search_order: the gradebook column search order
        :type gradebook_column_search_order: ``osid.grading.GradebookColumnSearchOrder``
        :raise: ``NullArgument`` -- ``gradebook_column_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``gradebook_column_search_order`` not of this service

        """
        pass

    def get_gradebook_column_query_from_inspector(self, gradebook_column_query_inspector):
        """Gets a gradebook column query from an inspector.

        :param gradebook_column_query_inspector: a gradebook column query inspector
        :type gradebook_column_query_inspector: ``osid.grading.GradebookColumnQuery``
        :return: the gradebook column query
        :rtype: ``osid.grading.GradebookColumnQuery``
        :raise: ``NullArgument`` -- ``gradebook_column_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``gradebook_column_query_inspector`` is not of this service

        """
        return # osid.grading.GradebookColumnQuery


class GradebookLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Gradebook`` objects.

    The ``Gradebook`` represents a collection of grade systems, entries,
    and gradebook columns.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Gradebooks`` it can access, without breaking
    execution. However, an administrative application may require all
    ``Gradebook`` elements to be available.
    
    Gradebooks may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Gradebook``.

    """
    def can_lookup_gradebooks(self):
        """Tests if this user can perform ``Gradebook`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_gradebook_view(self):
        """A complete view of the ``Gradebook`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_gradebook(self, gradebook_id):
        """Gets the ``Gradebook`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Gradebook`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Gradebook`` and retained
        for compatility.

        :param gradebook_id: ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: the gradebook
        :rtype: ``osid.grading.Gradebook``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.Gradebook

    def get_gradebooks_by_ids(self, gradebook_ids):
        """Gets a ``GradebookList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        gradebooks specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Gradebook`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :param gradebook_ids: the list of ``Ids`` to retrieve
        :type gradebook_ids: ``osid.id.IdList``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``gradebook_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not include gradebooks of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :param gradebook_genus_type: a gradebook genus type
        :type gradebook_genus_type: ``osid.type.Type``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``gradebook_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_parent_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any additional gradebooks with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :param gradebook_genus_type: a gradebook genus type
        :type gradebook_genus_type: ``osid.type.Type``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``gradebook_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_record_type(self, gradebook_record_type):
        """Gets a ``GradebookList`` containing the given gradebook record ``Type``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :param gradebook_record_type: a gradebook record type
        :type gradebook_record_type: ``osid.type.Type``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``gradebook_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_provider(self, resource_id):
        """Gets a ``GradebookList`` for the given provider ````.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Gradebook`` list
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    def get_gradebooks(self):
        """Gets all ``Gradebooks``.

        In plenary mode, the returned list contains all known gradebooks
        or an error results. Otherwise, the returned list may contain
        only those gradebooks that are accessible through this session.

        :return: a ``GradebookList``
        :rtype: ``osid.grading.GradebookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    gradebooks = property(fget=get_gradebooks)


class GradebookQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Gradebook`` objects.

    The search query is constructed using the ``GradebookQuery``.

    Gradebooks may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradebookQuery``.

    """
    def can_search_gradebooks(self):
        """Tests if this user can perform ``Gradebook`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_query(self):
        """Gets a gradebook query.

        :return: a gradebook query
        :rtype: ``osid.grading.GradebookQuery``

        """
        return # osid.grading.GradebookQuery

    gradebook_query = property(fget=get_gradebook_query)

    def get_gradebooks_by_query(self, gradebook_query):
        """Gets a list of ``Gradebook`` objects matching the given gradebook query.

        :param gradebook_query: the gradebook query
        :type gradebook_query: ``osid.grading.GradebookQuery``
        :return: the returned ``GradebookList``
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NullArgument`` -- ``gradebook_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_query`` is not of this service

        """
        return # osid.grading.GradebookList


class GradebookSearchSession(GradebookQuerySession):
    """This session provides methods for searching among ``Gradebook`` objects.

    The search query is constructed using the ``GradebookQuery``.

    ``get_gradebooks_by_query()`` is the basic search method and returns
    a list of ``Gradebook`` objects.A more advanced search may be
    performed with ``getGradebooksBySearch()``. It accepts a
    ``GradebookSearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_gradebooks_by_search()`` returns a
    ``GradebookSearchResults`` that can be used to access the resulting
    ``GradebookList`` or be used to perform a search within the result
    set through ``GradebookSearch``.
    
    Gradebooks may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``GradebookQuery``.

    """
    def get_gradebook_search(self):
        """Gets a gradebook search.

        :return: a gradebook search
        :rtype: ``osid.grading.GradebookSearch``

        """
        return # osid.grading.GradebookSearch

    gradebook_search = property(fget=get_gradebook_search)

    def get_gradebook_search_order(self):
        """Gets a gradebook search order.

        The ``GradebookSearchOrder`` is supplied to a
        ``GradebookSearch`` to specify the ordering of results.

        :return: the gradebook search order
        :rtype: ``osid.grading.GradebookSearchOrder``

        """
        return # osid.grading.GradebookSearchOrder

    gradebook_search_order = property(fget=get_gradebook_search_order)

    def get_gradebooks_by_search(self, gradebook_query, gradebook_search):
        """Gets the search results matching the given search query using the given search.

        :param gradebook_query: the gradebook query
        :type gradebook_query: ``osid.grading.GradebookQuery``
        :param gradebook_search: the gradebook search
        :type gradebook_search: ``osid.grading.GradebookSearch``
        :return: the gradebook search results
        :rtype: ``osid.grading.GradebookSearchResults``
        :raise: ``NullArgument`` -- ``gradebook_query`` or ``gradebook_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_query`` or ``gradebook_search`` is not of this service

        """
        return # osid.grading.GradebookSearchResults

    def get_gradebook_query_from_inspector(self, gradebook_query_inspector):
        """Gets a gradebook query from an inspector.

        The inspector is available from an ``GradenookSearchResults``.

        :param gradebook_query_inspector: a gradebook query inspector
        :type gradebook_query_inspector: ``osid.grading.GradebookQueryInspector``
        :return: the gradebook query
        :rtype: ``osid.grading.GradebookQuery``
        :raise: ``NullArgument`` -- ``gradebook_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``gradebook_query_inspector`` is not of this service

        """
        return # osid.grading.GradebookQuery


class GradebookAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Gradebooks``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Gradebook,`` a ``GradebookForm`` is requested using
    ``get_gradebook_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``GradebookForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``GradebookForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``GradebookForm``
    corresponds to an attempted transaction.
    
    For updates, ``GradebookForms`` are requested to the ``Gradebook``
    ``Id`` that is to be updated using ``getGradebookFormForUpdate()``.
    Similarly, the ``GradebookForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``GradebookForm`` can only be used once for a successful
    update and cannot be reused.
    
    The delete operations delete ``Gradebooks``.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def can_create_gradebooks(self):
        """Tests if this user can create ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_gradebook_with_record_types(self, gradebook_record_types):
        """Tests if this user can create a single ``Gradebook`` using the desired record types.

        While ``GradingManager.getGradebookRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Gradebook``.
        Providing an empty array tests if a ``Gradebook`` can be created
        with no records.

        :param gradebook_record_types: array of gradebook record types
        :type gradebook_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Gradebook`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_record_types`` is ``null``

        """
        return # boolean

    def get_gradebook_form_for_create(self, gradebook_record_types):
        """Gets the gradebook form for creating new gradebooks.

        A new form should be requested for each create transaction.

        :param gradebook_record_types: array of gradebook record types
        :type gradebook_record_types: ``osid.type.Type[]``
        :return: the gradebook form
        :rtype: ``osid.grading.GradebookForm``
        :raise: ``NullArgument`` -- ``gradebook_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.grading.GradebookForm

    def create_gradebook(self, gradebook_form):
        """Creates a new ``Gradebook``.

        :param gradebook_form: the form for this ``Gradebook``
        :type gradebook_form: ``osid.grading.GradebookForm``
        :return: the new ``Gradebook``
        :rtype: ``osid.grading.Gradebook``
        :raise: ``IllegalState`` -- ``gradebook_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``gradebook_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_form`` did not originate from ``get_gradebook_form_for_create()``

        """
        return # osid.grading.Gradebook

    def can_update_gradebooks(self):
        """Tests if this user can update ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_gradebook_form_for_update(self, gradebook_id):
        """Gets the gradebook form for updating an existing gradebook.

        A new gradebook form should be requested for each update
        transaction.

        :param gradebook_id: the ``Id`` of the ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :return: the gradebook form
        :rtype: ``osid.grading.GradebookForm``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookForm

    def update_gradebook(self, gradebook_form):
        """Updates an existing gradebook.

        :param gradebook_form: the form containing the elements to be updated
        :type gradebook_form: ``osid.grading.GradebookForm``
        :raise: ``IllegalState`` -- ``gradebook_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``gradebook_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``gradebook_form did not originate from get_gradebook_form_for_update()``

        """
        pass

    def can_delete_gradebooks(self):
        """Tests if this user can delete gradebooks.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Gradebook`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Gradebook`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_gradebook(self, gradebook_id):
        """Deletes a ``Gradebook``.

        :param gradebook_id: the ``Id`` of the ``Gradebook`` to remove
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_gradebook_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Gradebooks``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Gradebook`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_gradebook(self, gradebook_id, alias_id):
        """Adds an ``Id`` to a ``Gradebook`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Gradebook`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another gradebook, it is
        reassigned to the given gradebook ``Id``.

        :param gradebook_id: the ``Id`` of a ``Gradebook``
        :type gradebook_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradebookNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Gradebook`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    def can_register_for_gradebook_notifications(self):
        """Tests if this user can register for ``Gradebook`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def register_for_new_gradebooks(self):
        """Register for notifications of new gradebooks.

        ``GradebookReceiver.newGradebook()`` is invoked when a new
        ``Gradebook`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_gradebook_ancestors(self, gradebook_id):
        """Registers for notification if an ancestor is added to the specified gradebook in the gradebook hierarchy.

        ``GradebookReceiver.newGradebookAncestor()`` is invoked when the
        specified gradebook experiences an addition in ancestry.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_gradebook_descendants(self, gradebook_id):
        """Registers for notification if a descendant is added to the specified gradebook in the gradebook hierarchy.

        ``GradebookReceiver.newGradebookDescendant()`` is invoked when
        the specified gradebook experiences an addition in descendants.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_gradebooks(self):
        """Registers for notification of updated gradebooks.

        ``GradebookReceiver.changedGradebook()`` is invoked when a
        gradebook is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_gradebook(self, gradebook_id):
        """Registers for notification of an updated gradebook.

        ``GradebookReceiver.changedGradebook()`` is invoked when the
        specified gradebook is changed.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_gradebooks(self):
        """Registers for notification of deleted gradebooks.

        ``GradebookReceiver.deletedGradebook()`` is invoked when a
        calenedar is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_gradebook(self, gradebook_id):
        """Registers for notification of a deleted gradebook.

        ``GradebookReceiver.deletedGradebook()`` is invoked when the
        specified gradebook is deleted.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_gradebook_ancestors(self, gradebook_id):
        """Registers for notification if an ancestor is removed from the specified gradebook in the gradebook hierarchy.

        ``GradebookReceiver.deletedGradebookAncestor()`` is invoked when
        the specified gradebook experiences a removal of an ancestor.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_gradebook_descendants(self, gradebook_id):
        """Registers for notification if a descendant is removed from fthe specified gradebook in the calndar hierarchy.

        ``GradebookReceiver.deletedGradebookDescednant()`` is invoked
        when the specified gradebook experiences a removal of one of its
        descendants.

        :param gradebook_id: the ``Id`` of the gradebook to monitor
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``gradebook_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class GradebookHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Gradebook`` objects.

    Each node in the hierarchy is a unique ``Gradebook``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parent_gradebooks()`` and ``getChildGradebooks()``. To relate
    these ``Ids`` to another OSID, ``get_gradebook_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Gradebook`` available in the Gradebooking OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_gradebooks()`` or ``get_child_gradebooks()``
    in lieu of a ``PermissionDenied`` error that may disrupt the
    traversal through authorized pathways.
    
    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: gradebook elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition


    """
    def get_gradebook_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_hierarchy_id = property(fget=get_gradebook_hierarchy_id)

    def get_gradebook_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    gradebook_hierarchy = property(fget=get_gradebook_hierarchy)

    def can_access_gradebook_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_gradebook_view(self):
        """The returns from the gradebook methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_gradebook_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_root_gradebook_ids(self):
        """Gets the root gradebook ``Ids`` in this hierarchy.

        :return: the root gradebook ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    root_gradebook_ids = property(fget=get_root_gradebook_ids)

    def get_root_gradebooks(self):
        """Gets the root gradebooks in this gradebook hierarchy.

        :return: the root gradebooks
        :rtype: ``osid.grading.GradebookList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    root_gradebooks = property(fget=get_root_gradebooks)

    def has_parent_gradebooks(self, gradebook_id):
        """Tests if the ``Gradebook`` has any parents.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if the gradebook has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_parent_of_gradebook(self, id_, gradebook_id):
        """Tests if an ``Id`` is a direct parent of a gradebook.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``gradebook_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_parent_gradebook_ids(self, gradebook_id):
        """Gets the parent ``Ids`` of the given gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the gradebook
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_parent_gradebooks(self, gradebook_id):
        """Gets the parents of the given gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: the parents of the gradebook
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    def is_ancestor_of_gradebook(self, id_, gradebook_id):
        """Tests if an ``Id`` is an ancestor of a gradebook.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``gradebook_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def has_child_gradebooks(self, gradebook_id):
        """Tests if a gradebook has any children.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if the ``gradebook_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_child_of_gradebook(self, id_, gradebook_id):
        """Tests if a gradebook is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``gradebook_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_child_gradebook_ids(self, gradebook_id):
        """Gets the child ``Ids`` of the given gradebook.

        :param gradebook_id: the ``Id`` to query
        :type gradebook_id: ``osid.id.Id``
        :return: the children of the gradebook
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_child_gradebooks(self, gradebook_id):
        """Gets the children of the given gradebook.

        :param gradebook_id: the ``Id`` to query
        :type gradebook_id: ``osid.id.Id``
        :return: the children of the gradebook
        :rtype: ``osid.grading.GradebookList``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookList

    def is_descendant_of_gradebook(self, id_, gradebook_id):
        """Tests if an ``Id`` is a descendant of a gradebook.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``gradebook_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_gradebook_node_ids(self, gradebook_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given gradebook.

        :param gradebook_id: the ``Id`` to query
        :type gradebook_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a gradebook node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Node

    def get_gradebook_nodes(self, gradebook_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given gradebook.

        :param gradebook_id: the ``Id`` to query
        :type gradebook_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a gradebook node
        :rtype: ``osid.grading.GradebookNode``
        :raise: ``NotFound`` -- ``gradebook_id`` is not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.grading.GradebookNode


class GradebookHierarchyDesignSession(osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Gradebook`` objects.

    Each node in the hierarchy is a unique ``Gradebook``.

    """
    def get_gradebook_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    gradebook_hierarchy_id = property(fget=get_gradebook_hierarchy_id)

    def get_gradebook_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    gradebook_hierarchy = property(fget=get_gradebook_hierarchy)

    def can_modify_gradebook_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def add_root_gradebook(self, gradebook_id):
        """Adds a root gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``gradebook_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``gradebook_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_root_gradebook(self, gradebook_id):
        """Removes a root gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` is not a root
        :raise: ``NullArgument`` -- ``gradebook_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def add_child_gradebook(self, gradebook_id, child_id):
        """Adds a child to a gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``gradebook_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``gradebook_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_gradebook(self, gradebook_id, child_id):
        """Removes a child from a gradebook.

        :param gradebook_id: the ``Id`` of a gradebook
        :type gradebook_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``gradebook_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``gradebook_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

