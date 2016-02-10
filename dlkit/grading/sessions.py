
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

    def can_lookup_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` lookups.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_comparative_grade_system_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_grade_system_view(self):
        """A complete view of the ``GradeSystem`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.


        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this gradebook only.






        *compliance: mandatory -- This method is must be implemented.*


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


        *compliance: mandatory -- This method is must be implemented.*


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


        *compliance: mandatory -- This method is must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeSystemList

    def get_grade_systems_by_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` which does not include
            systems of genus types derived from the specified ``Type``.


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeSystemList

    def get_grade_systems_by_parent_genus_type(self, grade_system_genus_type):
        """Gets a ``GradeSystemList`` corresponding to the given grade system genus ``Type`` and include any additional
            systems with genus types derived from the specified ``Type``.


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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

    def can_search_grade_systems(self):
        """Tests if this user can perform ``GradeSystem`` searches.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.


        A federated view will include grades in gradebooks which are
        children of this gradebook in the gradebook hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts searches to this gradebook only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_grade_system_query(self):
        """Gets a grade system query.


        :return: a grade system query
        :rtype: ``osid.grading.GradeSystemQuery``




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeSystemList


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

    def can_create_grade_systems(self):
        """Tests if this user can create ``GradeSystems``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``GradeSystem`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``GradeSystem`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class GradeEntryLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``GradeEntrie`` s."""

    def can_lookup_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` lookups.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_comparative_grade_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_grade_entry_view(self):
        """A complete view of the ``GradeEntry`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.


        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this gradebook only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_effective_grade_entry_view(self):
        """Only grade entries whose effective dates are current are returned by methods in this session.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_any_effective_grade_entry_view(self):
        """All grade entries of any effective dates are returned by methods in this session.






        *compliance: mandatory -- This method is must be implemented.*


        """
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


        *compliance: mandatory -- This method is must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` which does not include grade
            entries of genus types derived from the specified ``Type``.


        :param grade_entry_genus_type: a grade entry genus type
        :type grade_entry_genus_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_by_parent_genus_type(self, grade_entry_genus_type):
        """Gets a ``GradeEntryList`` corresponding to the given grade entry genus ``Type`` and include any additional
            grade entry with genus types derived from the specified ``Type``.


        :param grade_entry_genus_type: a grade entry genus type
        :type grade_entry_genus_type: ``osid.type.Type``
        :return: the returned ``GradeEntry`` list
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``NullArgument`` -- ``grade_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_on_date(self, from_, to):
        """Gets a ``GradeEntryList`` effective during the entire given date range inclusive but not confined to the date
            range.


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column_on_date(self, gradebook_column_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column and effective during the entire given date range
            inclusive but not confined to the date range.


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_resource_on_date(self, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given key resource and effective during the entire given date range
            inclusive but not confined to the date range.


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeEntryList

    def get_grade_entries_for_gradebook_column_and_resource_on_date(self, gradebook_column_id, resource_id, from_, to):
        """Gets a ``GradeEntryList`` for the given gradebook column, resource, and effective during the entire given
            date range inclusive but not confined to the date range.


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeEntryList

    def get_grade_entries(self):
        """Gets all grade entries.


        :return: a ``GradeEntryList``
        :rtype: ``osid.grading.GradeEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


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

    def can_search_grade_entries(self):
        """Tests if this user can perform ``GradeEntry`` searches.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.


        A federated view will include grade entries in gradebooks which
        are children of this gradebook in the gradebook hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts searches to this gradebook only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_grade_entry_query(self):
        """Gets a grade entry query.


        :return: the grade entry query
        :rtype: ``osid.grading.GradeEntryQuery``




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradeEntryList


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

    def can_create_grade_entries(self):
        """Tests if this user can create grade entries.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a grade
        entry will result in a ``PermissionDenied``. This is intended as
        a hint to an application that may opt not to offer create
        operations to an unauthorized user.


        :return: ``false`` if ``GradeEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


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
        :return: ``true`` if ``GradeEntry`` creation using the specified record ``Types`` is supported, ``false``
            otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``grade_entry_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class GradebookColumnLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``GradebookColumns``."""

    def can_lookup_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` lookups.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_comparative_gradebook_column_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_gradebook_column_view(self):
        """A complete view of the ``GradebookColumn`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.


        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this gradebook only.






        *compliance: mandatory -- This method is must be implemented.*


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


        *compliance: mandatory -- This method is must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_columns_by_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` which does not
            include gradebook columns of genus types derived from the specified ``Type``.


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradebookColumnList

    def get_gradebook_columns_by_parent_genus_type(self, gradebook_column_genus_type):
        """Gets a ``GradebookColumnList`` corresponding to the given gradebook column genus ``Type`` and include any
            additional columns with genus types derived from the specified ``Type``.


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradebookColumnList

    gradebook_columns = property(fget=get_gradebook_columns)

    def supports_summary(self):
        """Tests if a summary entry is available.


        :return: ``true`` if a summary entry is available, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method is must be implemented.*


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

    def can_search_gradebook_columns(self):
        """Tests if this user can perform ``GradebookColumn`` searches.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_federated_gradebook_view(self):
        """Federates the view for methods in this session.


        A federated view will include gradebook columns in gradebooks
        which are children of this gradebook in the gradebook hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_gradebook_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts searches to this gradebook only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_gradebook_column_query(self):
        """Gets a gradebook column query.


        :return: the gradebook column
        :rtype: ``osid.grading.GradebookColumnQuery``




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradebookColumnList


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

    def can_create_gradebook_columns(self):
        """Tests if this user can create gradebook columns.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a gradebook
        column will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer create
        operations to an unauthorized user.


        :return: ``false`` if ``GradebookColumn`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


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
        :return: ``true`` if ``GradebookColumn`` creation using the specified record ``Types`` is supported, ``false``
            otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``gradebook_column_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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
        :raise: ``Unsupported`` -- ``gradebook_column_form`` did not originate from
            ``get_gradebook_column_form_for_create()``


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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
        :raise: ``Unsupported`` -- ``gradebook_column_form`` did not originate from
            ``get_gradebook_column_form_for_update()``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def sequence_gradebook_columns(self, gradebook_column_ids):
        """Resequences the gradebook columns.


        :param gradebook_column_ids: the ``Ids`` of the ``GradebookColumns``
        :type gradebook_column_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``gradebook_column_id_list`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


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




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_comparative_gradebook_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_gradebook_view(self):
        """A complete view of the ``Gradebook`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` which does not include
            gradebooks of types derived from the specified ``Type``.


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradebookList

    def get_gradebooks_by_parent_genus_type(self, gradebook_genus_type):
        """Gets a ``GradebookList`` corresponding to the given gradebook genus ``Type`` and include any additional
            gradebooks with genus types derived from the specified ``Type``.


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.grading.GradebookList

    gradebooks = property(fget=get_gradebooks)


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


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




        *compliance: mandatory -- This method must be implemented.*


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


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


