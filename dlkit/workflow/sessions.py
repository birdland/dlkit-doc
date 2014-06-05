from ..osid import sessions as osid_sessions


class ProcessLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Process`` objects."""
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_lookup_processes(self):
        """Tests if this user can perform ``Process`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_process_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_process_view(self):
        """A complete view of the ``Process`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include processes in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this office only.



        """
        pass

    def use_active_process_view(self):
        """Only active processes are returned from methods in this session."""
        pass

    def use_any_status_process_view(self):
        """Borth active and inactive processes are returned from methods in this session."""
        pass

    def get_process(self, process_id):
        """Gets the ``Process`` specified by its ``Id``.

        :param process_id: ``Id`` of the ``Process``
        :type process_id: ``osid.id.Id``
        :return: the process
        :rtype: ``osid.workflow.Process``
        :raise: ``NotFound`` -- ``process_id`` not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Process

    def get_processes_by_ids(self, process_ids):
        """Gets a ``ProcessList`` corresponding to the given ``IdList``.

        :param process_ids: the list of ``Ids`` to retrieve
        :type process_ids: ``osid.id.IdList``
        :return: the returned ``Process`` list
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``process_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    def get_processes_by_genus_type(self, process_genus_type):
        """Gets a ``ProcessList`` corresponding to the given process genus ``Type`` which does not include processes of genus types derived from the specified ``Type``.

        :param process_genus_type: a process genus type
        :type process_genus_type: ``osid.type.Type``
        :return: the returned ``Process`` list
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NullArgument`` -- ``process_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    def get_processes_by_parent_genus_type(self, process_genus_type):
        """Gets a ``ProcessList`` corresponding to the given process genus ``Type`` and include any additional processes with genus types derived from the specified ``Type``.

        :param process_genus_type: a process genus type
        :type process_genus_type: ``osid.type.Type``
        :return: the returned ``Process`` list
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NullArgument`` -- ``process_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    def get_processes_by_record_type(self, process_record_type):
        """Gets a ``ProcessList`` containing the given process record ``Type``.

        :param process_record_type: a process record type
        :type process_record_type: ``osid.type.Type``
        :return: the returned ``Process`` list
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NullArgument`` -- ``process_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    def get_processes_by_provider(self, resource_id):
        """Gets a ``ProcessList`` from the given provider.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Process`` list
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    def get_processes(self):
        """Gets all ``Processes``.

        :return: a list of ``Processes``
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    processes = property(fget=get_processes)


class ProcessQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Process`` objects.

    The search query is constructed using the ``ProcessQuery``.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated office view: searches include processes in offices of
        which this office is an ancestor in the office hierarchy
      * isolated office view: searches are restricted to processes in
        this office

    
    Process may have a query record indicated by their respective record
    types. The query record is accessed via the ``ProcessQuery``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_search_processes(self):
        """Tests if this user can perform ``Process`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include processes in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this office only.



        """
        pass

    def get_process_query(self):
        """Gets a process query.

        :return: the process query
        :rtype: ``osid.workflow.ProcessQuery``

        """
        return # osid.workflow.ProcessQuery

    process_query = property(fget=get_process_query)

    def get_processes_by_query(self, process_query):
        """Gets a list of ``Processes`` matching the given process query.

        :param process_query: the process query
        :type process_query: ``osid.workflow.ProcessQuery``
        :return: the returned ``ProcessList``
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NullArgument`` -- ``process_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``process_query`` is not of this service

        """
        return # osid.workflow.ProcessList


class ProcessSearchSession(ProcessQuerySession):
    """This session provides methods for searching among ``Process`` objects.

    The search query is constructed using the ``ProcessQuery``.

    ``get_processs_by_query()`` is the basic search method and returns a
    list of ``Processes``. A more advanced search may be performed with
    ``getProcessesBySearch()``. It accepts a ``ProcessSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_processes_by_search()`` returns a ``ProcessSearchResults``
    that can be used to access the resulting ``ProcessList`` or be used
    to perform a search within the result set through ``ProcessSearch``.
    
    This session defines views that offer differing behaviors for
    searching.
    
      * federated office view: searches include processes in offices of
        which this office is an ancestor in the office hierarchy
      * isolated office view: searches are restricted to processes in
        this office

    
    Processes may have a query record indicated by their respective
    record types. The query record is accessed via the ``ProcessQuery``.

    """
    def get_process_search(self):
        """Gets a process search.

        :return: the process search
        :rtype: ``osid.workflow.ProcessSearch``

        """
        return # osid.workflow.ProcessSearch

    process_search = property(fget=get_process_search)

    def get_process_search_order(self):
        """Gets a process search order.

        The ``ProcessSearchOrder`` is supplied to a ``ProcessSearch`` to
        specify the ordering of results.

        :return: the process search order
        :rtype: ``osid.workflow.ProcessSearchOrder``

        """
        return # osid.workflow.ProcessSearchOrder

    process_search_order = property(fget=get_process_search_order)

    def get_processes_by_search(self, process_query, process_search):
        """Gets the search results matching the given search query using the given search.

        :param process_query: the process query
        :type process_query: ``osid.workflow.ProcessQuery``
        :param process_search: the process search
        :type process_search: ``osid.workflow.ProcessSearch``
        :return: the process search results
        :rtype: ``osid.workflow.ProcessSearchResults``
        :raise: ``NullArgument`` -- ``process_query`` or ``process_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``process_query`` or ``process_search`` is not of this service

        """
        return # osid.workflow.ProcessSearchResults

    def get_process_query_from_inspector(self, process_query_inspector):
        """Gets a process query from an inspector.

        The inspector is available from a ``ProcessSearchResults``.

        :param process_query_inspector: a process query inspector
        :type process_query_inspector: ``osid.workflow.ProcessQueryInspector``
        :return: the process query
        :rtype: ``osid.workflow.ProcessQuery``
        :raise: ``NullArgument`` -- ``process_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``process_query_inspector`` is not of this service

        """
        return # osid.workflow.ProcessQuery


class ProcessAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Processes``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Process,`` a ``ProcessForm`` is requested using
    ``get_process_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``ProcessForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``ProcessForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ProcessForm``
    corresponds to an attempted transaction.
    
    For updates, ``ProcessForms`` are requested to the ``Process``
    ``Id`` that is to be updated using ``getProcessFormForUpdate()``.
    Similarly, the ``ProcessForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``ProcessForm`` can only be used once for a successful
    update and cannot be reused.
    
    The delete operations delete ``Processes``. To unmap a ``Process``
    from the current ``Office,`` the ``ProcessOfficeAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Process`` itself thus removing it from all known ``Office``
    catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_create_processes(self):
        """Tests if this user can create ``Process``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Process`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Process`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_process_with_record_types(self, process_record_types):
        """Tests if this user can create a single ``Process`` using the desired record types.

        While ``WorkflowManager.getProcessRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Process``.
        Providing an empty array tests if a ``Process`` can be created
        with no records.

        :param process_record_types: array of process record types
        :type process_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Process`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``process_record_types`` is ``null``

        """
        return # boolean

    def get_process_form_for_create(self, process_record_types):
        """Gets the process form for creating new processes.

        A new form should be requested for each create transaction.

        :param process_record_types: array of process record types
        :type process_record_types: ``osid.type.Type[]``
        :return: the process form
        :rtype: ``osid.workflow.ProcessForm``
        :raise: ``NullArgument`` -- ``process_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.workflow.ProcessForm

    def create_process(self, process_form):
        """Creates a new ``Process``.

        :param process_form: the form for this ``Process``
        :type process_form: ``osid.workflow.ProcessForm``
        :return: the new ``Process``
        :rtype: ``osid.workflow.Process``
        :raise: ``IllegalState`` -- ``process_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``process_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``process_form`` did not originate from ``get_process_form_for_create()``

        """
        return # osid.workflow.Process

    def can_update_processes(self):
        """Tests if this user can update ``Processes``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Process`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Process`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_process_form_for_update(self, process_id):
        """Gets the process form for updating an existing process.

        A new process form should be requested for each update
        transaction.

        :param process_id: the ``Id`` of the ``Process``
        :type process_id: ``osid.id.Id``
        :return: the process form
        :rtype: ``osid.workflow.ProcessForm``
        :raise: ``NotFound`` -- ``process_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessForm

    def update_process(self, process_form):
        """Updates an existing process.

        :param process_form: the form containing the elements to be updated
        :type process_form: ``osid.workflow.ProcessForm``
        :raise: ``IllegalState`` -- ``process_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``process_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``process_form`` did not originate from ``get_process_form_for_update()``

        """
        pass

    def can_delete_processes(self):
        """Tests if this user can delete ``Processes``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Process`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Process`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_process(self, process_id):
        """Deletes a ``Process``.

        :param process_id: the ``Id`` of the ``Process`` to remove
        :type process_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_process_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Process``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Process`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_process(self, process_id, alias_id):
        """Adds an ``Id`` to a ``Process`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Process`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another process, it is
        reassigned to the given process ``Id``.

        :param process_id: the ``Id`` of a ``Process``
        :type process_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``process_id`` not found
        :raise: ``NullArgument`` -- ``process_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_assign_competencies(self):
        """Tests if this user can assign competencies to process.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known assigning a
        competency will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        competency operations to an unauthorized user.

        :return: ``false`` if competency assignment is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def add_competency(self, process_id, competency_id):
        """Adds a competency to a process.

        :param process_id: the processId ``Id``
        :type process_id: ``osid.id.Id``
        :param competency_id: the competency ``Id``
        :type competency_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- competency already part of work
        :raise: ``NotFound`` -- ``competency_id`` or ``process_id`` is not found
        :raise: ``NullArgument`` -- ``competency_id`` or ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_competency(self, process_id, competency_id):
        """Removes a competency from a process.

        :param process_id: the process ``Id``
        :type process_id: ``osid.id.Id``
        :param competency_id: the competency ``Id``
        :type competency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- competency is not part of process
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_competencies(self, process_id):
        """Removes all competency from a process.

        :param process_id: the process ``Id``
        :type process_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class ProcessNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Process`` objects in this ``Office``.

    This also includes existing process that may appear or disappear due
    to changes in the ``Office`` hierarchy, This session is intended for
    consumers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.

    The two views defined in this session correspond to the views in the
    ``ProcessLookupSession``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_register_for_process_notifications(self):
        """Tests if this user can register for ``Process`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include process in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this office only.



        """
        pass

    def register_for_new_processes(self):
        """Register for notifications of new processes.

        ``ProcessReceiver.newProcess()`` is invoked when a new
        ``Process`` appears in this office.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_processes(self):
        """Registers for notification of updated processes.

        ``ProcessReceiver.changedProcess()`` is invoked when a process
        in this office is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_process(self, process_id):
        """Registers for notification of an updated process.

        ``ProcessReceiver.changedProcess()`` is invoked when the
        specified process in this office is changed.

        :param process_id: the ``Id`` of the ``Process`` to monitor
        :type process_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_processes(self):
        """Registers for notification of deleted processes.

        ``ProcessReceiver.deletedProcess()`` is invoked when a process
        is deleted or removed from this office.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_process(self, process_id):
        """Registers for notification of a deleted process.

        ``ProcessReceiver.deletedProcess()`` is invoked when the
        specified process is deleted or removed from this office.

        :param process_id: the ``Id`` of the ``Process`` to monitor
        :type process_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class ProcessOfficeSession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Process`` to ``Office`` workflows.

    A ``Process`` may appear in multiple ``Office`` objects. Each office
    may have its own authorizations governing who is allowed to look at
    it.

    This lookup session defines several views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
    def can_lookup_process_office_mappings(self):
        """Tests if this user can perform lookups of process/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_process_office_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_process_office_view(self):
        """A complete view of the ``Process`` and ``Office`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_process_ids_by_office(self, office_id):
        """Gets the list of ``Process Ids`` associated with a ``Office``.

        :param office_id: ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of related process ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_processes_by_office(self, office_id):
        """Gets the list of ``Processes`` associated with a ``Office``.

        :param office_id: ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of related processes
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    def get_process_ids_by_offices(self, office_ids):
        """Gets the list of ``Process Ids`` corresponding to a list of ``Offices``.

        :param office_ids: list of office ``Ids``
        :type office_ids: ``osid.id.IdList``
        :return: list of process ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_processes_by_offices(self, office_ids):
        """Gets the list of ``Processes`` corresponding to a list of ``Offices``.

        :param office_ids: list of office ``Ids``
        :type office_ids: ``osid.id.IdList``
        :return: list of processes
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NullArgument`` -- ``office_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    def get_office_ids_by_process(self, process_id):
        """Gets the ``Office``  ``Ids`` mapped to a ``Process``.

        :param process_id: ``Id`` of a ``Process``
        :type process_id: ``osid.id.Id``
        :return: list of offices
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``process_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_offices_by_process(self, process_id):
        """Gets the ``Offices`` mapped to a ``Process``.

        :param process_id: ``Id`` of a ``Process``
        :type process_id: ``osid.id.Id``
        :return: list of offices
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NotFound`` -- ``process_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList


class ProcessOfficeAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Process`` to ``Office`` mappings.

    A ``Process`` may appear in multiple ``Office`` objects and removing
    the last reference to a ``Process`` is the equivalent of deleting
    it. Each ``Office`` may have its own authorizations governing who is
    allowed to operate on it.

    Adding a reference of a ``Process`` to another ``Office`` is not a
    copy operation (eg: does not change its ``Id`` ).

    """
    def can_assign_processes(self):
        """Tests if this user can alter process/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_assign_processes_to_office(self, office_id):
        """Tests if this user can alter process/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``

        """
        return # boolean

    def get_assignable_office_ids(self, office_id):
        """Gets a list of offices including and under the given office node in which any process can be assigned.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of assignable office ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def get_assignable_office_ids_for_process(self, office_id, process_id):
        """Gets a list of offices including and under the given office node in which a specific process can be assigned.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param process_id: the ``Id`` of the ``Process``
        :type process_id: ``osid.id.Id``
        :return: list of assignable office ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_id`` or ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def assign_process_to_office(self, process_id, office_id):
        """Adds an existing ``Process`` to a ``Office``.

        :param process_id: the ``Id`` of the ``Process``
        :type process_id: ``osid.id.Id``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``process_id`` is already assigned to ``office_id``
        :raise: ``NotFound`` -- ``process_id`` or ``office_id`` not found
        :raise: ``NullArgument`` -- ``process_id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def unassign_process_from_office(self, process_id, office_id):
        """Removes a ``Process`` from a ``Office``.

        :param process_id: the ``Id`` of the ``Process``
        :type process_id: ``osid.id.Id``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` or ``office_id`` not found or ``process_id`` is not assigned to ``office_id``
        :raise: ``NullArgument`` -- ``process_id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class ProcessSmartOfficeSession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``ProcessQuery`` can be retrieved from this session and mapped to
    this ``Office`` to create a virtual collection of ``Processes``. The
    process may be sequenced using the ``ProcessSearchOrder`` from this
    session.

    This ``Office`` has a default query that matches any process and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``ProcessQueryInspector``. The query may be
    modified by converting the inspector back to a ``ProcessQuery``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_manage_smart_offices(self):
        """Tests if this user can manage smart offices.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart office management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_process_query(self):
        """Gets a process query.

        :return: the process query
        :rtype: ``osid.workflow.ProcessQuery``

        """
        return # osid.workflow.ProcessQuery

    process_query = property(fget=get_process_query)

    def get_process_search_order(self):
        """Gets a process search order.

        :return: the process search order
        :rtype: ``osid.workflow.ProcessSearchOrder``

        """
        return # osid.workflow.ProcessSearchOrder

    process_search_order = property(fget=get_process_search_order)

    def apply_process_query(self, process_query):
        """Applies a process query to this office.

        :param process_query: the process query
        :type process_query: ``osid.workflow.ProcessQuery``
        :raise: ``NullArgument`` -- ``process_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``process_query`` not of this service

        """
        pass

    def inspect_process_query(self):
        """Gets a process query inspector for this office.

        :return: the process query inspector
        :rtype: ``osid.workflow.ProcessQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.workflow.ProcessQueryInspector

    def apply_process_sequencing(self, process_search_order):
        """Applies a process search order to this office.

        :param process_search_order: the process search order
        :type process_search_order: ``osid.workflow.ProcessSearchOrder``
        :raise: ``NullArgument`` -- ``process_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``process_search_order`` not of this service

        """
        pass

    def get_process_query_from_inspector(self, process_query_inspector):
        """Gets a process query from an inspector.

        :param process_query_inspector: a process query inspector
        :type process_query_inspector: ``osid.workflow.ProcessQueryInspector``
        :return: the process query
        :rtype: ``osid.workflow.ProcessQuery``
        :raise: ``NullArgument`` -- ``process_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``process_query_inspector`` is not of this service

        """
        return # osid.workflow.ProcessQuery


class StepLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Step`` objects.

    The ``Step`` represents a fixed connection between two
    ``Availabilities``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * isolated office view: All step methods in this session operate,
        retrieve and pertain to steps defined explicitly in the current
        office. Using an isolated view is useful for managing ``Steps``
        with the ``StepAdminSession.``
      * federated office view: All step methods in this session operate,
        retrieve and pertain to all steps defined in this office and any
        other steps implicitly available in this office through office
        inheritence.
      * active step view: active steps are returned from methods in this
        session
      * any status step view: active and inactive steps are returned
        from methods in this session

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. The methods ``use_federated_office_view()`` and
    ``use_isolated_office_view()`` behave as a radio group and one
    should be selected before invoking any lookup methods.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_lookup_steps(self):
        """Tests if this user can perform ``Step`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_step_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_step_view(self):
        """A complete view of the ``Step`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include steps in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this office only.



        """
        pass

    def use_active_step_view(self):
        """Only active steps are returned from methods in this session."""
        pass

    def use_any_status_step_view(self):
        """Borth active and inactive steps are returned from methods in this session."""
        pass

    def get_step(self, step_id):
        """Gets the ``Step`` specified by its ``Id``.

        :param step_id: ``Id`` of the ``Step``
        :type step_id: ``osid.id.Id``
        :return: the step
        :rtype: ``osid.workflow.Step``
        :raise: ``NotFound`` -- ``step_id`` not found
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Step

    def get_steps_by_ids(self, step_ids):
        """Gets a ``StepList`` corresponding to the given ``IdList``.

        :param step_ids: the list of ``Ids`` to retrieve
        :type step_ids: ``osid.id.IdList``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``step_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_steps_by_genus_type(self, step_genus_type):
        """Gets a ``StepList`` corresponding to the given step genus ``Type`` which does not include steps of genus types derived from the specified ``Type``.

        :param step_genus_type: a step genus type
        :type step_genus_type: ``osid.type.Type``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NullArgument`` -- ``step_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_steps_by_parent_genus_type(self, step_genus_type):
        """Gets a ``StepList`` corresponding to the given step genus ``Type`` and include any additional steps with genus types derived from the specified ``Type``.

        :param step_genus_type: a step genus type
        :type step_genus_type: ``osid.type.Type``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NullArgument`` -- ``step_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_steps_by_record_type(self, step_record_type):
        """Gets a ``StepList`` containing the given step record ``Type``.

        :param step_record_type: a step record type
        :type step_record_type: ``osid.type.Type``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NullArgument`` -- ``step_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_steps_by_provider(self, resource_id):
        """Gets a ``StepList`` from the given provider.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_steps_for_process(self, process_id):
        """Gets a list of steps by process.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_steps_by_state(self, state_id):
        """Gets a list of steps for which the given state is valid.

        The steps returned are the states specified in the previous step
        or the process.

        In plenary mode, the returned list contains all known steps or
        an error results. Otherwise, the returned list may contain only
        those steps that are accessible through this session.
        
        In active mode, steps are returned that are currently active. In
        any status mode, active and inactive steps are returned.

        :param state_id: a stateId ``Id``
        :type state_id: ``osid.id.Id``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NullArgument`` -- ``state_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_steps(self):
        """Gets all ``Steps``.

        :return: a list of ``Steps``
        :rtype: ``osid.workflow.StepList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    steps = property(fget=get_steps)


class StepQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Step`` objects.

    The search query is constructed using the ``StepQuery``.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated office view: searches include steps in offices of
        which this office is an ancestor in the office hierarchy
      * isolated office view: searches are restricted to steps in this
        office

    
    Steps may have a query record indicated by their respective record
    types. The query record is accessed via the ``StepQuery``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_search_steps(self):
        """Tests if this user can perform ``Step`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include steps in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this office only.



        """
        pass

    def get_step_query(self):
        """Gets a step query.

        :return: the step query
        :rtype: ``osid.workflow.StepQuery``

        """
        return # osid.workflow.StepQuery

    step_query = property(fget=get_step_query)

    def get_steps_by_query(self, step_query):
        """Gets a list of ``Steps`` matching the given step query.

        :param step_query: the step query
        :type step_query: ``osid.workflow.StepQuery``
        :return: the returned ``StepList``
        :rtype: ``osid.workflow.StepList``
        :raise: ``NullArgument`` -- ``step_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``step_query`` is not of this service

        """
        return # osid.workflow.StepList


class StepSearchSession(StepQuerySession):
    """This session provides methods for searching among ``Step`` objects.

    The search query is constructed using the ``StepQuery``.

    ``get_steps_by_query()`` is the basic search method and returns a
    list of ``Steps``. A more advanced search may be performed with
    ``getStepsBySearch()``. It accepts a ``StepSearch`` in addition to
    the query for the purpose of specifying additional options affecting
    the entire search, such as ordering. ``get_steps_by_search()``
    returns a ``StepSearchResults`` that can be used to access the
    resulting ``StepList`` or be used to perform a search within the
    result set through ``StepSearch``.
    
    This session defines views that offer differing behaviors for
    searching.
    
      * federated office view: searches include steps in offices of
        which this office is an ancestor in the office hierarchy
      * isolated office view: searches are restricted to steps in this
        office

    
    Steps may have a query record indicated by their respective record
    types. The query record is accessed via the ``StepQuery``.

    """
    def get_step_search(self):
        """Gets a step search.

        :return: the step search
        :rtype: ``osid.workflow.StepSearch``

        """
        return # osid.workflow.StepSearch

    step_search = property(fget=get_step_search)

    def get_step_search_order(self):
        """Gets a step search order.

        The ``StepSearchOrder`` is supplied to a ``StepSearch`` to
        specify the ordering of results.

        :return: the step search order
        :rtype: ``osid.workflow.StepSearchOrder``

        """
        return # osid.workflow.StepSearchOrder

    step_search_order = property(fget=get_step_search_order)

    def get_steps_by_search(self, step_query, step_search):
        """Gets the search results matching the given search query using the given search.

        :param step_query: the step query
        :type step_query: ``osid.workflow.StepQuery``
        :param step_search: the step search
        :type step_search: ``osid.workflow.StepSearch``
        :return: the step search results
        :rtype: ``osid.workflow.StepSearchResults``
        :raise: ``NullArgument`` -- ``step_query`` or ``step_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``step_query`` or ``step_search`` is not of this service

        """
        return # osid.workflow.StepSearchResults

    def get_step_query_from_inspector(self, step_query_inspector):
        """Gets a step query from an inspector.

        The inspector is available from a ``StepSearchResults``.

        :param step_query_inspector: a step query inspector
        :type step_query_inspector: ``osid.workflow.StepQueryInspector``
        :return: the step query
        :rtype: ``osid.workflow.StepQuery``
        :raise: ``NullArgument`` -- ``step_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``step_query_inspector`` is not of this service

        """
        return # osid.workflow.StepQuery


class StepAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Steps``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Step,`` a ``StepForm`` is requested using
    ``get_step_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``StepForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``StepForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``StepForm`` corresponds
    to an attempted transaction.
    
    For updates, ``StepForms`` are requested to the ``Step``  ``Id``
    that is to be updated using ``getStepFormForUpdate()``. Similarly,
    the ``StepForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``StepForm`` can only be used once for a successful update and
    cannot be reused.
    
    The delete operations delete ``Steps``. To unmap a ``Step`` from the
    current ``Office,`` the ``StepOfficeAssignmentSession`` should be
    used. These delete operations attempt to remove the ``Step`` itself
    thus removing it from all known ``Office`` catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_create_steps(self):
        """Tests if this user can create ``Steps``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Step``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Step`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_step_with_record_types(self, step_record_types):
        """Tests if this user can create a single ``Step`` using the desired record types.

        While ``WorkflowManager.getStepRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Step``.
        Providing an empty array tests if a ``Step`` can be created with
        no records.

        :param step_record_types: array of step record types
        :type step_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Step`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``step_record_types`` is ``null``

        """
        return # boolean

    def get_step_form_for_create(self, process_id, step_record_types):
        """Gets the step form for creating new steps.

        A new form should be requested for each create transaction.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param step_record_types: array of step record types
        :type step_record_types: ``osid.type.Type[]``
        :return: the step form
        :rtype: ``osid.workflow.StepForm``
        :raise: ``NotFound`` -- ``process_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` or ``step_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.workflow.StepForm

    def create_step(self, step_form):
        """Creates a new ``Step``.

        :param step_form: the form for this ``Step``
        :type step_form: ``osid.workflow.StepForm``
        :return: the new ``Step``
        :rtype: ``osid.workflow.Step``
        :raise: ``IllegalState`` -- ``step_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``step_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``step_form`` did not originate from ``get_step_form_for_create()``

        """
        return # osid.workflow.Step

    def can_update_steps(self):
        """Tests if this user can update ``Steps``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Step``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if ``Step`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_step_form_for_update(self, step_id):
        """Gets the step form for updating an existing step.

        A new step form should be requested for each update transaction.

        :param step_id: the ``Id`` of the ``Step``
        :type step_id: ``osid.id.Id``
        :return: the step form
        :rtype: ``osid.workflow.StepForm``
        :raise: ``NotFound`` -- ``step_id`` is not found
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepForm

    def update_step(self, step_form):
        """Updates an existing step.

        :param step_form: the form containing the elements to be updated
        :type step_form: ``osid.workflow.StepForm``
        :raise: ``IllegalState`` -- ``step_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``step_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``step_form`` did not originate from ``get_step_form_for_update()``

        """
        pass

    def can_delete_steps(self):
        """Tests if this user can delete ``Steps``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Step``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Step`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_step(self, step_id):
        """Deletes a ``Step``.

        :param step_id: the ``Id`` of the ``Step`` to remove
        :type step_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``step_id`` not found
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_step_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Steps``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Step`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_step(self, step_id, alias_id):
        """Adds an ``Id`` to a ``Step`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Step`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another step, it is
        reassigned to the given step ``Id``.

        :param step_id: the ``Id`` of a ``Step``
        :type step_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``step_id`` not found
        :raise: ``NullArgument`` -- ``step_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class StepNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Step`` objects in this ``Office``.

    This also includes existing steps that may appear or disappear due
    to changes in the ``Office`` hierarchy, This session is intended for
    consumers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.

    The two views defined in this session correspond to the views in the
    ``StepLookupSession``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_register_for_step_notifications(self):
        """Tests if this user can register for ``Step`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include steps in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this office only.



        """
        pass

    def register_for_new_steps(self):
        """Register for notifications of new steps.

        ``StepReceiver.newStep()`` is invoked when a new ``Step``
        appears in this office.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_steps_for_process(self, process_id):
        """Register for notifications of new steps in the given process ``Id``.

        ``StepReceiver.newStep()`` is invoked when a new ``Step`` is
        created.

        :param process_id: the ``Id`` of the process to monitor
        :type process_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_steps(self):
        """Registers for notification of updated steps.

        ``StepReceiver.changedStep()`` is invoked when a step in this
        office is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_steps_for_process(self, process_id):
        """Register for notifications of updated steps for the given process ``Id``.

        ``StepReceiver.changedStep()`` is invoked when a step in this
        office is changed.

        :param process_id: the ``Id`` of the process to monitor
        :type process_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_step(self, step_id):
        """Registers for notification of an updated step.

        ``StepReceiver.changedStep()`` is invoked when the specified
        step in this office is changed.

        :param step_id: the ``Id`` of the ``Step`` to monitor
        :type step_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_steps(self):
        """Registers for notification of deleted steps.

        ``StepReceiver.deletedStep()`` is invoked when a step is deleted
        or removed from this office.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_steps_for_process(self, process_id):
        """Register for notifications of deleted steps for the given process ``Id``.

        ``StepReceiver.deletedStep()`` is invoked when a step in this
        office is removed or deleted.

        :param process_id: the ``Id`` of the process to monitor
        :type process_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_step(self, step_id):
        """Registers for notification of a deleted step.

        ``StepReceiver.deletedStep()`` is invoked when the specified
        step is deleted or removed from this office.

        :param step_id: the ``Id`` of the ``Step`` to monitor
        :type step_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class StepOfficeSession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Step`` to ``Office`` workflows.

    A ``Step`` may appear in multiple ``Office`` objects. Each office
    may have its own authorizations governing who is allowed to look at
    it.

    This lookup session defines several views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
    def can_lookup_step_office_mappings(self):
        """Tests if this user can perform lookups of step/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_step_office_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_step_office_view(self):
        """A complete view of the ``Step`` and ``Office`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_step_ids_by_office(self, office_id):
        """Gets the list of ``Step Ids`` associated with a ``Office``.

        :param office_id: ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of related step ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_stepes_by_office(self, office_id):
        """Gets the list of ``Steps`` associated with a ``Office``.

        :param office_id: ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of related steps
        :rtype: ``osid.workflow.StepList``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_step_ids_by_offices(self, office_ids):
        """Gets the list of ``Step Ids`` corresponding to a list of ``Offices``.

        :param office_ids: list of office ``Ids``
        :type office_ids: ``osid.id.IdList``
        :return: list of step ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_steps_by_offices(self, office_ids):
        """Gets the list of ``Steps`` corresponding to a list of ``Offices``.

        :param office_ids: list of office ``Ids``
        :type office_ids: ``osid.id.IdList``
        :return: list of steps
        :rtype: ``osid.workflow.StepList``
        :raise: ``NullArgument`` -- ``office_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_office_ids_by_step(self, step_id):
        """Gets the ``Office``  ``Ids`` mapped to a ``Step``.

        :param step_id: ``Id`` of a ``Step``
        :type step_id: ``osid.id.Id``
        :return: list of offices
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``step_id`` is not found
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_offices_by_step(self, step_id):
        """Gets the ``Offices`` mapped to a ``Step``.

        :param step_id: ``Id`` of a ``Step``
        :type step_id: ``osid.id.Id``
        :return: list of offices
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NotFound`` -- ``step_id`` is not found
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList


class StepOfficeAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Step`` to ``Office`` mappings.

    A ``Step`` may appear in multiple ``Office`` objects and removing
    the last reference to a ``Step`` is the equivalent of deleting it.
    Each ``Office`` may have its own authorizations governing who is
    allowed to operate on it.

    Adding a reference of a ``Step`` to another ``Office`` is not a copy
    operation (eg: does not change its ``Id`` ).

    """
    def can_assign_stepes(self):
        """Tests if this user can alter step/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_assign_stepes_to_office(self, office_id):
        """Tests if this user can alter step/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``

        """
        return # boolean

    def get_assignable_office_ids(self, office_id):
        """Gets a list of offices including and under the given office node in which any step can be assigned.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of assignable office ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def get_assignable_office_ids_for_step(self, office_id, step_id):
        """Gets a list of offices including and under the given office node in which a specific step can be assigned.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param step_id: the ``Id`` of the ``Step``
        :type step_id: ``osid.id.Id``
        :return: list of assignable office ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_id`` or ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def assign_step_to_office(self, step_id, office_id):
        """Adds an existing ``Step`` to a ``Office``.

        :param step_id: the ``Id`` of the ``Step``
        :type step_id: ``osid.id.Id``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``step_id`` is already assigned to ``office_id``
        :raise: ``NotFound`` -- ``step_id`` or ``office_id`` not found
        :raise: ``NullArgument`` -- ``step_id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def unassign_step_from_office(self, step_id, office_id):
        """Removes a ``Step`` from a ``Office``.

        :param step_id: the ``Id`` of the ``Step``
        :type step_id: ``osid.id.Id``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``step_id`` or ``office_id`` not found or ``step_id`` is not assigned to ``office_id``
        :raise: ``NullArgument`` -- ``step_id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class StepSmartOfficeSession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``StepQuery`` can be retrieved from this session and mapped to
    this ``Office`` to create a virtual collection of ``Steps``. The
    step may be sequenced using the ``StepSearchOrder`` from this
    session.

    This ``Office`` has a default query that matches any step and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``StepQueryInspector``. The query may be
    modified by converting the inspector back to a ``StepQuery``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_manage_smart_offices(self):
        """Tests if this user can manage smart offices.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart office management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_step_query(self):
        """Gets a step query.

        :return: the step query
        :rtype: ``osid.workflow.StepQuery``

        """
        return # osid.workflow.StepQuery

    step_query = property(fget=get_step_query)

    def get_step_search_order(self):
        """Gets a step search order.

        :return: the step search order
        :rtype: ``osid.workflow.StepSearchOrder``

        """
        return # osid.workflow.StepSearchOrder

    step_search_order = property(fget=get_step_search_order)

    def apply_step_query(self, step_query):
        """Applies a step query to this office.

        :param step_query: the step query
        :type step_query: ``osid.workflow.StepQuery``
        :raise: ``NullArgument`` -- ``step_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``step_query`` not of this service

        """
        pass

    def inspect_step_query(self):
        """Gets a step query inspector for this office.

        :return: the step query inspector
        :rtype: ``osid.workflow.StepQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.workflow.StepQueryInspector

    def apply_step_sequencing(self, step_search_order):
        """Applies a step search order to this office.

        :param step_search_order: the step search order
        :type step_search_order: ``osid.workflow.StepSearchOrder``
        :raise: ``NullArgument`` -- ``step_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``step_search_order`` not of this service

        """
        pass

    def get_step_query_from_inspector(self, step_query_inspector):
        """Gets a step query from an inspector.

        :param step_query_inspector: a step query inspector
        :type step_query_inspector: ``osid.workflow.StepQueryInspector``
        :return: the step query
        :rtype: ``osid.workflow.StepQuery``
        :raise: ``NullArgument`` -- ``step_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``step_query_inspector`` is not of this service

        """
        return # osid.workflow.StepQuery


class WorkLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Work`` objects.

    The ``Work`` represents a fixed connection between two
    ``Availabilities``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition
      * isolated office view: All work methods in this session operate,
        retrieve and pertain to works defined explicitly in the current
        office. Using an isolated view is useful for managing ``Works``
        with the ``WorkAdminSession.``
      * federated office view: All work methods in this session operate,
        retrieve and pertain to all works defined in this office and any
        other works implicitly available in this office through office
        inheritence.

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. The methods ``use_federated_office_view()`` and
    ``use_isolated_office_view()`` behave as a radio group and one
    should be selected before invoking any lookup methods.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_lookup_works(self):
        """Tests if this user can perform ``Work`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_work_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_work_view(self):
        """A complete view of the ``Work`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include works in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this office only.



        """
        pass

    def get_work(self, work_id):
        """Gets the ``Work`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Work`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Work`` and retained for compatibility.

        :param work_id: ``Id`` of the ``Work``
        :type work_id: ``osid.id.Id``
        :return: the work
        :rtype: ``osid.workflow.Work``
        :raise: ``NotFound`` -- ``work_id`` not found
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Work

    def get_works_by_ids(self, work_ids):
        """Gets a ``WorkList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the works
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Works`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param work_ids: the list of ``Ids`` to retrieve
        :type work_ids: ``osid.id.IdList``
        :return: the returned ``Work`` list
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``work_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_works_by_genus_type(self, work_genus_type):
        """Gets a ``WorkList`` corresponding to the given work genus ``Type`` which does not include works of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known works or
        an error results. Otherwise, the returned list may contain only
        those works that are accessible through this session.

        :param work_genus_type: a work genus type
        :type work_genus_type: ``osid.type.Type``
        :return: the returned ``Work`` list
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NullArgument`` -- ``work_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_works_by_parent_genus_type(self, work_genus_type):
        """Gets a ``WorkList`` corresponding to the given work genus ``Type`` and include any additional works with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known works or
        an error results. Otherwise, the returned list may contain only
        those works that are accessible through this session

        :param work_genus_type: a work genus type
        :type work_genus_type: ``osid.type.Type``
        :return: the returned ``Work`` list
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NullArgument`` -- ``work_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_works_by_record_type(self, work_record_type):
        """Gets a ``WorkList`` containing the given work record ``Type``.

        In plenary mode, the returned list contains all known works or
        an error results. Otherwise, the returned list may contain only
        those works that are accessible through this session.

        :param work_record_type: a work record type
        :type work_record_type: ``osid.type.Type``
        :return: the returned ``Work`` list
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NullArgument`` -- ``work_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_works(self):
        """Gets all ``Works``.

        In plenary mode, the returned list contains all known works or
        an error results. Otherwise, the returned list may contain only
        those works that are accessible through this session.

        :return: a list of ``Works``
        :rtype: ``osid.workflow.WorkList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    works = property(fget=get_works)


class WorkQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Work`` objects.

    The search query is constructed using the ``WorkQuery``.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated office view: searches include works in offices of
        which this office is an ancestor in the office hierarchy
      * isolated office view: searches are restricted to works in this
        office

    
    Works may have a query record indicated by their respective record
    types. The query record is accessed via the ``WorkQuery``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_search_works(self):
        """Tests if this user can perform ``Work`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include works in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this office only.



        """
        pass

    def get_work_query(self):
        """Gets a work query.

        :return: the work query
        :rtype: ``osid.workflow.WorkQuery``

        """
        return # osid.workflow.WorkQuery

    work_query = property(fget=get_work_query)

    def get_works_by_query(self, work_query):
        """Gets a list of ``Works`` matching the given work query.

        :param work_query: the work query
        :type work_query: ``osid.workflow.WorkQuery``
        :return: the returned ``WorkList``
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NullArgument`` -- ``work_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``work_query`` is not of this service

        """
        return # osid.workflow.WorkList


class WorkSearchSession(WorkQuerySession):
    """This session provides methods for searching among ``Work`` objects.

    The search query is constructed using the ``WorkQuery``.

    ``get_works_by_query()`` is the basic search method and returns a
    list of ``Works``. A more advanced search may be performed with
    ``getWorksBySearch()``. It accepts a ``WorkSearch`` in addition to
    the query for the purpose of specifying additional options affecting
    the entire search, such as ordering. ``get_works_by_search()``
    returns a ``WorkSearchResults`` that can be used to access the
    resulting ``WorkList`` or be used to perform a search within the
    result set through ``WorkSearch``.
    
    This session defines views that offer differing behaviors for
    searching.
    
      * federated office view: searches include works in offices of
        which this office is an ancestor in the office hierarchy
      * isolated office view: searches are restricted to works in this
        office

    
    Works may have a query record indicated by their respective record
    types. The query record is accessed via the ``WorkQuery``.

    """
    def get_work_search(self):
        """Gets a work search.

        :return: the work search
        :rtype: ``osid.workflow.WorkSearch``

        """
        return # osid.workflow.WorkSearch

    work_search = property(fget=get_work_search)

    def get_work_search_order(self):
        """Gets a work search order.

        The ``WorkSearchOrder`` is supplied to a ``WorkSearch`` to
        specify the ordering of results.

        :return: the work search order
        :rtype: ``osid.workflow.WorkSearchOrder``

        """
        return # osid.workflow.WorkSearchOrder

    work_search_order = property(fget=get_work_search_order)

    def get_works_by_search(self, work_query, work_search):
        """Gets the search results matching the given search query using the given search.

        :param work_query: the work query
        :type work_query: ``osid.workflow.WorkQuery``
        :param work_search: the work search
        :type work_search: ``osid.workflow.WorkSearch``
        :return: the work search results
        :rtype: ``osid.workflow.WorkSearchResults``
        :raise: ``NullArgument`` -- ``work_query`` or ``work_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``work_query`` or ``work_search`` is not of this service

        """
        return # osid.workflow.WorkSearchResults

    def get_work_query_from_inspector(self, work_query_inspector):
        """Gets a work query from an inspector.

        The inspector is available from a ``WorkSearchResults``.

        :param work_query_inspector: a work query inspector
        :type work_query_inspector: ``osid.workflow.WorkQueryInspector``
        :return: the work query
        :rtype: ``osid.workflow.WorkQuery``
        :raise: ``NullArgument`` -- ``work_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``work_query_inspector`` is not of this service

        """
        return # osid.workflow.WorkQuery


class WorkAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Works``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Work,`` a ``WorkForm`` is requested using
    ``get_work_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``WorkForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``WorkForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``WorkForm`` corresponds
    to an attempted transaction.
    
    For updates, ``WorkForms`` are requested to the ``Work``  ``Id``
    that is to be updated using ``getWorkFormForUpdate()``. Similarly,
    the ``WorkForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``WorkForm`` can only be used once for a successful update and
    cannot be reused.
    
    The delete operations delete ``Works``. To unmap a ``Work`` from the
    current ``Office,`` the ``WorkOfficeAssignmentSession`` should be
    used. These delete operations attempt to remove the ``Work`` itself
    thus removing it from all known ``Office`` catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_create_works(self):
        """Tests if this user can create ``Works``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Work``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Work`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_work_with_record_types(self, work_record_types):
        """Tests if this user can create a single ``Work`` using the desired record types.

        While ``WorkflowManager.getWorkRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Work``.
        Providing an empty array tests if a ``Work`` can be created with
        no records.

        :param work_record_types: array of work record types
        :type work_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Work`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``work_record_types`` is ``null``

        """
        return # boolean

    def get_work_form_for_create(self, work_record_types):
        """Gets the work form for creating new works.

        A new form should be requested for each create transaction.

        :param work_record_types: array of work record types
        :type work_record_types: ``osid.type.Type[]``
        :return: the work form
        :rtype: ``osid.workflow.WorkForm``
        :raise: ``NullArgument`` -- ``work_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.workflow.WorkForm

    def create_work(self, work_form):
        """Creates a new ``Work``.

        :param work_form: the form for this ``Work``
        :type work_form: ``osid.workflow.WorkForm``
        :return: the new ``Work``
        :rtype: ``osid.workflow.Work``
        :raise: ``IllegalState`` -- ``work_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``work_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``work_form`` did not originate from ``get_work_form_for_create()``

        """
        return # osid.workflow.Work

    def can_update_works(self):
        """Tests if this user can update ``Works``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Work``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if ``Work`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_work_form_for_update(self, work_id):
        """Gets the work form for updating an existing work.

        A new work form should be requested for each update transaction.

        :param work_id: the ``Id`` of the ``Work``
        :type work_id: ``osid.id.Id``
        :return: the work form
        :rtype: ``osid.workflow.WorkForm``
        :raise: ``NotFound`` -- ``work_id`` is not found
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkForm

    def update_work(self, work_form):
        """Updates an existing work.

        :param work_form: the form containing the elements to be updated
        :type work_form: ``osid.workflow.WorkForm``
        :raise: ``IllegalState`` -- ``work_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``work_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``work_form`` did not originate from ``get_work_form_for_update()``

        """
        pass

    def can_delete_works(self):
        """Tests if this user can delete ``Works``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Work``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Work`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_work(self, work_id):
        """Deletes a ``Work``.

        :param work_id: the ``Id`` of the ``Work`` to remove
        :type work_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``work_id`` not found
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_work_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Works``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Work`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_work(self, work_id, alias_id):
        """Adds an ``Id`` to a ``Work`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Work`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another work, it is
        reassigned to the given work ``Id``.

        :param work_id: the ``Id`` of a ``Work``
        :type work_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``work_id`` not found
        :raise: ``NullArgument`` -- ``work_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_move_work(self):
        """Tests if this user can move ``Work`` among process.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Work``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer move operations
        to an unauthorized user.

        :return: ``false`` if ``Work`` moving is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def move_work(self, work_id, process_id):
        """Moves work to another process.

        :param work_id: the work ``Id``
        :type work_id: ``osid.id.Id``
        :param process_id: the new process ``Id``
        :type process_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- work already part of process
        :raise: ``NotFound`` -- ``process_id`` or ``work_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_work_status(self):
        """Tests if this user can change ``Work`` status.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Work``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer status
        operations to an unauthorized user.

        :return: ``false`` if ``Work`` status is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def complete_work(self, work_id):
        """Marks work as complete.

        :param work_id: the work ``Id``
        :type work_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``work_id`` is not found
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def reopen_work(self, work_id):
        """Marks work as incomplete.

        :param work_id: the work ``Id``
        :type work_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``work_id`` is not found
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class WorkNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Work`` objects in this ``Office``.

    This also includes existing works that may appear or disappear due
    to changes in the ``Office`` hierarchy, This session is intended for
    consumers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.

    The two views defined in this session correspond to the views in the
    ``WorkLookupSession``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_register_for_work_notifications(self):
        """Tests if this user can register for ``Work`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include works in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this office only.



        """
        pass

    def register_for_new_works(self):
        """Register for notifications of new works.

        ``WorkReceiver.newWork()`` is invoked when a new ``Work``
        appears in this office.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_works(self):
        """Registers for notification of updated works.

        ``WorkReceiver.changedWork()`` is invoked when a work in this
        office is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_work(self, work_id):
        """Registers for notification of an updated work.

        ``WorkReceiver.changedWork()`` is invoked when the specified
        work in this office is changed.

        :param work_id: the ``Id`` of the ``Work`` to monitor
        :type work_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_works(self):
        """Registers for notification of deleted works.

        ``WorkReceiver.deletedWork()`` is invoked when a work is deleted
        or removed from this office.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_work(self, work_id):
        """Registers for notification of a deleted work.

        ``WorkReceiver.deletedWork()`` is invoked when the specified
        work is deleted or removed from this office.

        :param work_id: the ``Id`` of the ``Work`` to monitor
        :type work_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class WorkOfficeSession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Work`` to ``Office`` workflows.

    A ``Work`` may appear in multiple ``Office`` objects. Each office
    may have its own authorizations governing who is allowed to look at
    it.

    This lookup session defines several views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
    def can_lookup_work_office_availabilities(self):
        """Tests if this user can perform lookups of work/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_work_office_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_work_office_view(self):
        """A complete view of the ``Work`` and ``Office`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_work_ids_by_office(self, office_id):
        """Gets the list of ``Work Ids`` associated with a ``Office``.

        :param office_id: ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of related work ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_works_by_office(self, office_id):
        """Gets the list of ``Works`` associated with a ``Office``.

        :param office_id: ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of related works
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_work_ids_by_offices(self, office_ids):
        """Gets the list of ``Work Ids`` corresponding to a list of ``Offices``.

        :param office_ids: list of office ``Ids``
        :type office_ids: ``osid.id.IdList``
        :return: list of work ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_works_by_offices(self, office_ids):
        """Gets the list of ``Work`` corresponding to a list of ``Offices``.

        :param office_ids: list of office ``Ids``
        :type office_ids: ``osid.id.IdList``
        :return: list of works
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NullArgument`` -- ``office_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_office_ids_by_work(self, work_id):
        """Gets the ``Office``  ``Ids`` mapped to a ``Work``.

        :param work_id: ``Id`` of a ``Work``
        :type work_id: ``osid.id.Id``
        :return: list of offices
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``work_id`` is not found
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_offices_by_work(self, work_id):
        """Gets the ``Offices`` mapped to a ``Work``.

        :param work_id: ``Id`` of a ``Work``
        :type work_id: ``osid.id.Id``
        :return: list of offices
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NotFound`` -- ``work_id`` is not found
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList


class WorkOfficeAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Works`` to ``Office`` mappings.

    A ``Work`` may appear in multiple ``Office`` objects and removing
    the last reference to a ``Work`` is the equivalent of deleting it.
    Each ``Office`` may have its own authorizations governing who is
    allowed to operate on it.

    Adding a reference of a ``Work`` to another ``Office`` is not a copy
    operation (eg: does not change its ``Id`` ).

    """
    def can_assign_works(self):
        """Tests if this user can alter work/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_assign_works_to_office(self, office_id):
        """Tests if this user can alter work/office mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: ``false`` if workflow is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``

        """
        return # boolean

    def get_assignable_office_ids(self, office_id):
        """Gets a list of offices including and under the given office node in which any work can be assigned.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: list of assignable office ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def get_assignable_office_ids_for_work(self, office_id, work_id):
        """Gets a list of offices including and under the given office node in which a specific work can be assigned.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :param work_id: the ``Id`` of the ``Work``
        :type work_id: ``osid.id.Id``
        :return: list of assignable office ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``office_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def assign_work_to_office(self, work_id, office_id):
        """Adds an existing ``Work`` to a ``Office``.

        :param work_id: the ``Id`` of the ``Work``
        :type work_id: ``osid.id.Id``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``work_id`` is already assigned to ``office_id``
        :raise: ``NotFound`` -- ``work_id`` or ``office_id`` not found
        :raise: ``NullArgument`` -- ``work_id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def unassign_work_from_office(self, work_id, office_id):
        """Removes a ``Work`` from a ``Office``.

        :param work_id: the ``Id`` of the ``Work``
        :type work_id: ``osid.id.Id``
        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``work_id`` or ``office_id`` not found or ``work_id`` not assigned to ``office_id``
        :raise: ``NullArgument`` -- ``work_id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class WorkSmartOfficeSession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``WorkQuery`` can be retrieved from this session and mapped to
    this ``Office`` to create a virtual collection of ``Works``. The
    works may be sequenced using the ``WorkSearchOrder`` from this
    session.

    This ``Office`` has a default query that matches any work and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``WorkQueryInspector``. The query may be
    modified by converting the inspector back to a ``WorkQuery``.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_manage_smart_offices(self):
        """Tests if this user can manage smart offices.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart office management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_work_query(self):
        """Gets a work query.

        :return: the work query
        :rtype: ``osid.workflow.WorkQuery``

        """
        return # osid.workflow.WorkQuery

    work_query = property(fget=get_work_query)

    def get_work_search_order(self):
        """Gets a work search order.

        :return: the work search order
        :rtype: ``osid.workflow.WorkSearchOrder``

        """
        return # osid.workflow.WorkSearchOrder

    work_search_order = property(fget=get_work_search_order)

    def apply_work_query(self, work_query):
        """Applies a work query to this office.

        :param work_query: the work query
        :type work_query: ``osid.workflow.WorkQuery``
        :raise: ``NullArgument`` -- ``work_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``work_query`` not of this service

        """
        pass

    def inspect_work_query(self):
        """Gets a work query inspector for this office.

        :return: the work query inspector
        :rtype: ``osid.workflow.WorkQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.workflow.WorkQueryInspector

    def apply_work_sequencing(self, work_search_order):
        """Applies a work search order to this office.

        :param work_search_order: the work search order
        :type work_search_order: ``osid.workflow.WorkSearchOrder``
        :raise: ``NullArgument`` -- ``work_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``work_search_order`` not of this service

        """
        pass

    def get_work_query_from_inspector(self, work_query_inspector):
        """Gets a work query from an inspector.

        :param work_query_inspector: a work query inspector
        :type work_query_inspector: ``osid.workflow.WorkQueryInspector``
        :return: the work query
        :rtype: ``osid.workflow.WorkQuery``
        :raise: ``NullArgument`` -- ``work_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``work_query_inspector`` is not of this service

        """
        return # osid.workflow.WorkQuery


class WorkflowSession(osid_sessions.OsidSession):
    """This session provides methods for looking at a workflow."""
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_access_workflow(self):
        """Tests if this user can access a workflow.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer workflow
        operations to unauthorized users.

        :return: ``false`` if workflow initiation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_access_workflow_for_process(self, process_id):
        """Tests if this user can access a workflow in a process.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer workflow
        operations to unauthorized users.

        :param process_id: a process Id
        :type process_id: ``osid.id.Id``
        :return: ``false`` if workflow initiation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``

        """
        return # boolean

    def get_processes_for_work(self, work_id):
        """Gets the processes a work is in.

        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the ``Processes``
        :rtype: ``osid.workflow.ProcessList``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.ProcessList

    def get_step_for_work(self, process_id, work_id):
        """Gets the step corresponding to a work in a process.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the returned ``Step``
        :rtype: ``osid.workflow.Step``
        :raise: ``NotFound`` -- ``process_id`` not found or ``work_id`` is not active in the process
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Step

    def get_work_at_step(self, step_id):
        """Getsall the work at a step in a process.

        :param step_id: a step ``Id``
        :type step_id: ``osid.id.Id``
        :return: the returned ``Work`` List
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NotFound`` -- ``step_id`` is not found
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_suspended_work(self, process_id):
        """Gets all the suspended work in a process.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: the returned ``Work`` List
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NotFound`` -- ``process_id`` not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_suspended_work_at_step(self, step_id):
        """Gets the suspended work at a step in a process.

        :param step_id: a step ``Id``
        :type step_id: ``osid.id.Id``
        :return: the returned ``Work`` List
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NotFound`` -- ``step_id`` is not found
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_canceled_work(self, process_id):
        """Gets the work canceled in a process.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: the returned ``Work`` List
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NotFound`` -- ``process_id`` not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_canceled_work_by_date(self, process_id, start, end):
        """Gets the work canceled in a process within the given date range inclusive.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``Work`` List
        :rtype: ``osid.workflow.WorkList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NotFound`` -- ``process_id`` not found
        :raise: ``NullArgument`` -- ``process_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def get_statuses_for_work(self, work_id):
        """Gets the statuses of the work across all processes.

        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the current list of statuses
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_status_for_work(self, process_id, work_id):
        """Gets the status of a work in a process.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the status
        :rtype: ``osid.workflow.WorkflowEvent``
        :raise: ``NotFound`` -- ``process_id`` not found or ``work_id`` is not active in the process
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEvent

    def get_statuses_for_works(self, process_id, work_ids):
        """Gets the status of a works in a process.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_ids: a list of work ``Ids``
        :type work_ids: ``osid.id.IdList``
        :return: the current list of statuses
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``process_id`` or ``work_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList


class WorkflowInitiationSession(osid_sessions.OsidSession):
    """This session provides methods for initiating a workflow."""
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_initiate_workflow(self):
        """Tests if this user can initiate a workflow.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer workflow
        operations to unauthorized users.

        :return: ``false`` if workflow initiation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_initiate_workflow_for_process(self, process_id):
        """Tests if this user can initiate a workflow in a process.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer workflow
        operations to unauthorized users.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: ``false`` if workflow initiation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``

        """
        return # boolean

    def get_available_work(self, process_id):
        """Gets the list of available work for this workflow.

        Available work is ``Work`` that is compatible with this
        ``Process`` but not currently part of this ``Process``.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: the returned ``Work`` list
        :rtype: ``osid.workflow.WorkList``
        :raise: ``NotFound`` -- ``process_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkList

    def start_workflow(self, process_id, work_id):
        """Starts a work in the workflow at the initial step of the process.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` or ``work_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class WorkflowManagementSession(osid_sessions.OsidSession):
    """This session provides methods for managing a workflow."""
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_manage_workflow(self):
        """Tests if this user can manage a workflow.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer workflow
        operations to unauthorized users.

        :return: ``false`` if workflow management methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_manage_workflow_for_process(self, process_id):
        """Tests if this user can manage a workflow for a process.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer workflow
        operations to unauthorized users.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: ``false`` if workflow management methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``

        """
        return # boolean

    def suspend_work(self, process_id, work_id):
        """Suspends a work in this process leaving it at its current step.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` or ``work_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def resume_work(self, process_id, work_id):
        """Resumes a work in this process.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` or ``work_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def cancel_work(self, process_id, work_id):
        """Cancels a work in this process removing it from the workflow.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` or ``work_id`` is not found
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class ManualWorkflowSession(WorkflowManagementSession):
    """This session provides methods for manually moving work through a workflow."""
    def can_operate_workflow(self):
        """Tests if this user can operate a workflow.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer workflow
        operations to unauthorized users.

        :return: ``false`` if workflow operation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_operate_workflow_for_process(self, process_id):
        """Tests if this user can operate a workflow.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer workflow
        operations to unauthorized users.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: ``false`` if workflow operation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``

        """
        return # boolean

    def advance_work(self, process_id, work_id):
        """Advances work to a next step in the workflow based on the work and the input conditions of the next steps.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` is not found or ``work_id`` is in process
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def get_valid_next_steps_for_work(self, process_id, work_id):
        """Gets the valid next steps in this process in which the given work can be manually advanced.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NotFound`` -- ``process_id`` is not found or ``work_id`` is in process
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def get_all_valid_steps_for_work(self, process_id, work_id):
        """Gets the all valid steps in this process the given work can be manually assigned and includes the steps previous to the work's current step.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the returned ``Step`` list
        :rtype: ``osid.workflow.StepList``
        :raise: ``NotFound`` -- ``process_id`` is not found or ``work_id`` is in process
        :raise: ``NullArgument`` -- ``process_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.StepList

    def assign_work_to_step(self, process_id, work_id, step_id):
        """Manually assigns a work to a step.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :param step_id: a step ``Id``
        :type step_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``process_id`` is not found or ``work_id`` or ``step_id`` is not found in this process
        :raise: ``NullArgument`` -- ``process_id, work_id,`` or ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class WorkflowEventLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``WorkflowEvents``."""
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def can_lookup_workflow_events(self):
        """Tests if this user can look up workflow events.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing a step
        sequence in a ``PermissionDenied``. This is intended as a hint
        to an application that may opt not to offer lookup operations to
        an unauthorized user.

        :return: ``false`` if workflow event lookups is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_workflow_event_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_workflow_event_view(self):
        """A complete view of the ``WorkflowEvent`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include workflow events in offices which
        are children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this office only.



        """
        pass

    def get_workflow_event(self, workflow_event_id):
        """Gets the ``WorkflowEvent`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``WorkflowEvent`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``WorkflowEvent`` and
        retained for compatibility.

        :param workflow_event_id: ``Id`` of the ``WorkflowEvent``
        :type workflow_event_id: ``osid.id.Id``
        :return: the workflow event
        :rtype: ``osid.workflow.WorkflowEvent``
        :raise: ``NotFound`` -- ``workflow_event_id`` not found
        :raise: ``NullArgument`` -- ``workflow_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEvent

    def get_workflow_events_by_ids(self, workflow_event_ids):
        """Gets a ``WorkflowEventList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the workflow
        events specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``WorkflowEvents`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param workflow_event_ids: the list of ``Ids`` to retrieve
        :type workflow_event_ids: ``osid.id.IdList``
        :return: the returned ``WorkflowEvent`` list
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``workflow_event_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_genus_type(self, workflow_event_genus_type):
        """Gets a ``WorkflowEventList`` corresponding to the given workflow event genus ``Type`` which does not include workflow events of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param workflow_event_genus_type: a workflow event genus type
        :type workflow_event_genus_type: ``osid.type.Type``
        :return: the returned ``WorkflowEvent`` list
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``workflow_event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_parent_genus_type(self, workflow_event_genus_type):
        """Gets a ``WorkflowEventList`` corresponding to the given workflow event genus ``Type`` and include any additional workflow events with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param workflow_event_genus_type: a workflow event genus type
        :type workflow_event_genus_type: ``osid.type.Type``
        :return: the returned ``WorkflowEvent`` list
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``workflow_event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_record_type(self, workflow_event_record_type):
        """Gets a ``WorkflowEventList`` containing the given workflow event record ``Type``.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param workflow_event_record_type: a workflow event record type
        :type workflow_event_record_type: ``osid.type.Type``
        :return: the returned ``WorkflowEvent`` list
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``workflow_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_date(self, start, end):
        """Gets the entire workflow log within the given date range inclusive.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_for_process(self, process_id):
        """Gets the entire workflow log for a process.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_date_for_process(self, process_id, start, end):
        """Gets the entire workflow log for this process within the given date range inclusive.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``process_id, start,`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_for_step(self, step_id):
        """Gets the workflow log for a step.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param step_id: a step ``Id``
        :type step_id: ``osid.id.Id``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_date_for_step(self, step_id, start, end):
        """Gets the workflow log for a step within the given date range inclusive.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param step_id: a step ``Id``
        :type step_id: ``osid.id.Id``
        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``step_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_for_work(self, work_id):
        """Gets the workflow log for a work.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_date_for_work(self, work_id, start, end):
        """Gets the workflow log for a work within the given date range inclusive.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``work_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_for_work_and_process(self, process_id, work_id):
        """Gets the workflow log for a work in a process.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_date_for_work_and_process(self, process_id, work_id, start, end):
        """Gets the workflow log for a work in a process within the given date range inclusive.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``work_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_for_step_and_work(self, step_id, work_id):
        """Gets the workflow log for a work in this process.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param step_id: a step ``Id``
        :type step_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``step_id`` or ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_date_for_step_and_work(self, step_id, work_id, start, end):
        """Gets the workflow log for a work in this process within the given date range inclusive.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param step_id: a step ``Id``
        :type step_id: ``osid.id.Id``
        :param work_id: a work ``Id``
        :type work_id: ``osid.id.Id``
        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``step_id, work_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_for_worker(self, resource_id):
        """Gets the workflow log by an agent in this process.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_date_for_worker(self, resource_id, start, end):
        """Gets the workflow log by the resource in this process within the given date range inclusive.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``resource_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_for_worker_and_process(self, resource_id, process_id):
        """Gets the workflow log by an agent in this process.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events_by_date_for_worker_and_process(self, resource_id, process_id, start, end):
        """Gets the workflow log by the resource in this process within the given date range inclusive.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param start: start range
        :type start: ``osid.calendaring.DateTime``
        :param end: end range
        :type end: ``osid.calendaring.DateTime``
        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``resource_id, process_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    def get_workflow_events(self):
        """Gets the entire workflow log.

        In plenary mode, the returned list contains all known workflow
        events or an error results. Otherwise, the returned list may
        contain only those workflow events that are accessible through
        this session.

        :return: the workflow events
        :rtype: ``osid.workflow.WorkflowEventList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.WorkflowEventList

    workflow_events = property(fget=get_workflow_events)


class WorkflowEventNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``WorkflowEvent`` objects in this ``Process``.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    def get_office_id(self):
        """Gets the ``Office``  ``Id`` associated with this session.

        :return: the ``Office Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_id = property(fget=get_office_id)

    def get_office(self):
        """Gets the ``Office`` associated with this session.

        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    office = property(fget=get_office)

    def use_federated_office_view(self):
        """Federates the view for methods in this session.

        A federated view will include events in offices which are
        children of this office in the office hierarchy.



        """
        pass

    def use_isolated_office_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this office only.



        """
        pass

    def can_register_for_workflow_event_notifications(self):
        """Tests if this user can register for ``WorkflowEvent`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def register_for_new_workflow_events(self):
        """Register for notifications of new workflow events.

        ``WorkflowEventReceiver.newWorkflowEvent()`` is invoked when a
        new ``WorkflowEvent`` appears in this process.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_workflow_events_for_process(self, process_id):
        """Register for notifications of new workflow events for the given process.

        ``WorkflowEventReceiver.newWorkflowEvent()`` is invoked when a
        new ``WorkflowEvent`` appears in this process.

        :param process_id: the ``Id`` of the ``Process`` to monitor
        :type process_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``process_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_workflow_events_for_step(self, step_id):
        """Register for notifications of new workflow events for the given step.

        ``WorkflowEventReceiver.newWorkflowEvent()`` is invoked when a
        new ``WorkflowEvent`` appears in this process.

        :param step_id: the ``Id`` of the ``Step`` to monitor
        :type step_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``step_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_workflow_events_for_work(self, work_id):
        """Register for notifications of new workflow events for the given work.

        ``WorkflowEventReceiver.newWorkflowEvent()`` is invoked when a
        new ``WorkflowEvent`` appears in this process.

        :param work_id: the ``Id`` of the ``Work`` to monitor
        :type work_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``work_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_workflow_events_for_worker(self, resource_id):
        """Register for notifications of new workflow events for the given resource.

        ``WorkflowEventReceiver.newWorkflowEvent()`` is invoked when a
        new ``WorkflowEvent`` appears in this process.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class OfficeLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Office`` objects.

    The ``Office`` represents a collection of processes and steps.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Offices`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Offices``
    referenced by it are available, and a test-taking application may
    sacrifice some interoperability for the sake of precision.

    """
    def can_lookup_offices(self):
        """Tests if this user can perform ``Office`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_office_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_office_view(self):
        """A complete view of the ``Office`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_office(self, office_id):
        """Gets the ``Office`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Office`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Office`` and retained for compatibility.

        :param office_id: ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: the office
        :rtype: ``osid.workflow.Office``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.Office

    def get_offices_by_ids(self, office_ids):
        """Gets an ``OfficeList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the offices
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Offices`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param office_ids: the list of ``Ids`` to retrieve
        :type office_ids: ``osid.id.IdList``
        :return: the returned ``Office`` list
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``office_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    def get_offices_by_genus_type(self, office_genus_type):
        """Gets an ``OfficeList`` corresponding to the given office genus ``Type`` which does not include offices of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known offices or
        an error results. Otherwise, the returned list may contain only
        those offices that are accessible through this session.

        :param office_genus_type: an office genus type
        :type office_genus_type: ``osid.type.Type``
        :return: the returned ``Office`` list
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NullArgument`` -- ``office_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    def get_offices_by_parent_genus_type(self, office_genus_type):
        """Gets an ``OfficeList`` corresponding to the given office genus ``Type`` and include any additional offices with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known offices or
        an error results. Otherwise, the returned list may contain only
        those offices that are accessible through this session.

        :param office_genus_type: an office genus type
        :type office_genus_type: ``osid.type.Type``
        :return: the returned ``Office`` list
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NullArgument`` -- ``office_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    def get_offices_by_record_type(self, office_record_type):
        """Gets an ``OfficeList`` containing the given office record ``Type``.

        In plenary mode, the returned list contains all known offices or
        an error results. Otherwise, the returned list may contain only
        those offices that are accessible through this session.

        :param office_record_type: an office record type
        :type office_record_type: ``osid.type.Type``
        :return: the returned ``Office`` list
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NullArgument`` -- ``office_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    def get_offices_by_provider(self, resource_id):
        """Gets an ``OfficeList`` from the given provider.

        In plenary mode, the returned list contains all known offices or
        an error results. Otherwise, the returned list may contain only
        those offices that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Office`` list
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    def get_offices(self):
        """Gets all ``Offices``.

        In plenary mode, the returned list contains all known offices or
        an error results. Otherwise, the returned list may contain only
        those offices that are accessible through this session.

        :return: a list of ``Offices``
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    offices = property(fget=get_offices)


class OfficeQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Office`` objects.

    The search query is constructed using the ``OfficeQuery``.

    Offices may have a query record indicated by their respective record
    types. The query record is accessed via the ``OfficeQuery``.

    """
    def can_search_offices(self):
        """Tests if this user can perform ``Office`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_office_query(self):
        """Gets an office query.

        :return: the office query
        :rtype: ``osid.workflow.OfficeQuery``

        """
        return # osid.workflow.OfficeQuery

    office_query = property(fget=get_office_query)

    def get_offices_by_query(self, office_query):
        """Gets a list of ``Offices`` matching the given office query.

        :param office_query: the office query
        :type office_query: ``osid.workflow.OfficeQuery``
        :return: the returned ``OfficeList``
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NullArgument`` -- ``office_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``office_query`` is not of this service

        """
        return # osid.workflow.OfficeList


class OfficeSearchSession(OfficeQuerySession):
    """This session provides methods for searching among ``Office`` objects.

    The search query is constructed using the ``OfficeQuery``.

    ``get_offices_by_query()`` is the basic search method and returns a
    list of ``Offices``. A more advanced search may be performed with
    ``getOfficesBySearch()``. It accepts an ``OfficeSearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_offices_by_search()`` returns an ``OfficeSearchResults`` that
    can be used to access the resulting ``OfficeList`` or be used to
    perform a search within the result set through ``OfficeSearch``.
    
    Offices may have a query record indicated by their respective record
    types. The query record is accessed via the ``OfficeQuery``.

    """
    def get_office_search(self):
        """Gets an office search.

        :return: the office search
        :rtype: ``osid.workflow.OfficeSearch``

        """
        return # osid.workflow.OfficeSearch

    office_search = property(fget=get_office_search)

    def get_office_search_order(self):
        """Gets an office search order.

        The ``OfficeSearchOrder`` is supplied to an ``OfficeSearch`` to
        specify the ordering of results.

        :return: the office search order
        :rtype: ``osid.workflow.OfficeSearchOrder``

        """
        return # osid.workflow.OfficeSearchOrder

    office_search_order = property(fget=get_office_search_order)

    def get_offices_by_search(self, office_query, office_search):
        """Gets the search results matching the given search query using the given search.

        :param office_query: the office query
        :type office_query: ``osid.workflow.OfficeQuery``
        :param office_search: the office search
        :type office_search: ``osid.workflow.OfficeSearch``
        :return: the returned search results
        :rtype: ``osid.workflow.OfficeSearchResults``
        :raise: ``NullArgument`` -- ``office_query`` or ``office_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``office_query`` or ``office_search`` is not of this service

        """
        return # osid.workflow.OfficeSearchResults

    def get_office_query_from_inspector(self, office_query_inspector):
        """Gets an office query from an inspector.

        The inspector is available from an ``OfficeSearchResults``.

        :param office_query_inspector: an office query inspector
        :type office_query_inspector: ``osid.workflow.OfficeQueryInspector``
        :return: the office query
        :rtype: ``osid.workflow.OfficeQuery``
        :raise: ``NullArgument`` -- ``office_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``office_query_inspector`` is not of this service

        """
        return # osid.workflow.OfficeQuery


class OfficeAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Offices``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Office,`` an ``OfficeForm`` is requested using
    ``get_office_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``OfficeForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``OfficeForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``OfficeForm``
    corresponds to an attempted transaction.
    
    For updates, ``OfficeForms`` are requested to the ``Office``  ``Id``
    that is to be updated using ``getOfficeFormForUpdate()``. Similarly,
    the ``OfficeForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``OfficeForm`` can only be used once for a successful update and
    cannot be reused.
    
    The delete operations delete ``Offices``.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def can_create_offices(self):
        """Tests if this user can create ``Offices``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Office``. will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Office`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_office_with_record_types(self, office_record_types):
        """Tests if this user can create a single ``Office`` using the desired record types.

        While ``WorkflowManager.getOfficeRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Office``.
        Providing an empty array tests if an ``Office`` can be created
        with no records.

        :param office_record_types: array of office record types
        :type office_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Office`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``office_record_types`` is ``null``

        """
        return # boolean

    def get_office_form_for_create(self, office_record_types):
        """Gets the office form for creating new offices.

        A new form should be requested for each create transaction.

        :param office_record_types: array of office record types
        :type office_record_types: ``osid.type.Type[]``
        :return: the office form
        :rtype: ``osid.workflow.OfficeForm``
        :raise: ``NullArgument`` -- ``office_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.workflow.OfficeForm

    def create_office(self, office_form):
        """Creates a new ``Office``.

        :param office_form: the form for this ``Office``
        :type office_form: ``osid.workflow.OfficeForm``
        :return: the new ``Office``
        :rtype: ``osid.workflow.Office``
        :raise: ``IllegalState`` -- ``office_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``office_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``office_form`` did not originate from ``get_office_form_for_create()``

        """
        return # osid.workflow.Office

    def can_update_offices(self):
        """Tests if this user can update ``Offices``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Office`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Office`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_office_form_for_update(self, office_id):
        """Gets the office form for updating an existing office.

        A new office form should be requested for each update
        transaction.

        :param office_id: the ``Id`` of the ``Office``
        :type office_id: ``osid.id.Id``
        :return: the office form
        :rtype: ``osid.workflow.OfficeForm``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeForm

    def update_office(self, office_form):
        """Updates an existing office.

        :param office_form: the form containing the elements to be updated
        :type office_form: ``osid.workflow.OfficeForm``
        :raise: ``IllegalState`` -- ``office_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``office_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``office_form`` did not originate from ``get_office_form_for_update()``

        """
        pass

    def can_delete_offices(self):
        """Tests if this user can delete ``Offices``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Office`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Office`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_office(self, office_id):
        """Deletes an ``Office``.

        :param office_id: the ``Id`` of the ``Office`` to remove
        :type office_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_office_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Offices``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Office`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_office(self, office_id, alias_id):
        """Adds an ``Id`` to an ``Office`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Office`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``.

        :param office_id: the ``Id`` of an ``Office``
        :type office_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class OfficeNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Office`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    def can_register_for_office_notifications(self):
        """Tests if this user can register for ``Office`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def register_for_new_offices(self):
        """Register for notifications of new offices.

        ``OfficeReceiver.newOffice()`` is invoked when a new ``Office``
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_office_ancestors(self, office_id):
        """Registers for notification if an ancestor is added to the specified office in the office hierarchy.

        ``OfficeReceiver.newOfficeAncestor()`` is invoked when the
        specified office experiences an addition in ancestry.

        :param office_id: the ``Id`` of the office to monitor
        :type office_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``office_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_office_descendants(self, office_id):
        """Registers for notification if a descendant is added to the specified office in the office hierarchy.

        ``OfficeReceiver.newOfficeDescendant()`` is invoked when the
        specified office experiences an addition in descendants.

        :param office_id: the ``Id`` of the office to monitor
        :type office_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``office_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_offices(self):
        """Registers for notification of updated offices.

        ``OfficeReceiver.changedOffice()`` is invoked when an office is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_office(self, office_id):
        """Registers for notification of an updated office.

        ``OfficeReceiver.changedOffice()`` is invoked when the specified
        office is changed.

        :param office_id: the Id of the ``Office`` to monitor
        :type office_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``office_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_offices(self):
        """Registers for notification of deleted offices.

        ``OfficeReceiver.deletedOffice()`` is invoked when an office is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_office(self, office_id):
        """Registers for notification of a deleted office.

        ``OfficeReceiver.deletedOffice()`` is invoked when the specified
        office is deleted.

        :param office_id: the ``Id`` of the ``Office`` to monitor
        :type office_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``office_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_office_ancestors(self, office_id):
        """Registers for notification if an ancestor is removed from the specified office in the office hierarchy.

        ``OfficeReceiver.deletedOfficeAncestor()`` is invoked when the
        specified office experiences a removal of an ancestor.

        :param office_id: the ``Id`` of the office to monitor
        :type office_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``office_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_office_descendants(self, office_id):
        """Registers for notification if a descendant is removed from fthe specified office in the office hierarchy.

        ``OfficeReceiver.deletedOfficeDescednant()`` is invoked when the
        specified office experiences a removal of one of its
        descdendents.

        :param office_id: the ``Id`` of the office to monitor
        :type office_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``office_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class OfficeHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Office`` objects.

    Each node in the hierarchy is a unique ``Office``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_offices()`` and ``getChildOffices()``. To relate these
    ``Ids`` to another OSID, ``get_office_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Office`` available in the Workflow OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    availability or a child of another availability.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_offices()`` or ``get_child_offices()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized stepways.
    
    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative office view: office elements may be silently omitted
        or re-ordered
      * plenary office view: provides a complete set or is an error
        condition


    """
    def get_office_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_hierarchy_id = property(fget=get_office_hierarchy_id)

    def get_office_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    office_hierarchy = property(fget=get_office_hierarchy)

    def can_access_office_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_office_view(self):
        """The returns from the office methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_office_view(self):
        """A complete view of the ``Offices`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_root_office_ids(self):
        """Gets the root office ``Ids`` in this hierarchy.

        :return: the root office ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    root_office_ids = property(fget=get_root_office_ids)

    def get_root_offices(self):
        """Gets the root office in the office hierarchy.

        A availability with no parents is an orphan. While all office
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root availability or
        child of another availability.

        :return: the root offices
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    root_offices = property(fget=get_root_offices)

    def has_parent_offices(self, office_id):
        """Tests if the ``Office`` has any parents.

        :param office_id: an office ``Id``
        :type office_id: ``osid.id.Id``
        :return: ``true`` if the office has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_parent_of_office(self, id_, office_id):
        """Tests if an ``Id`` is a direct parent of office.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``office_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_parent_office_ids(self, office_id):
        """Gets the parent ``Ids`` of the given office.

        :param office_id: an office ``Id``
        :type office_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the office
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_parent_offices(self, office_id):
        """Gets the parents of the given office.

        :param office_id: the ``Id`` to query
        :type office_id: ``osid.id.Id``
        :return: the parents of the office
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    def is_ancestor_of_office(self, id_, office_id):
        """Tests if an ``Id`` is an ancestor of an office.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``office_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def has_child_offices(self, office_id):
        """Tests if an office has any children.

        :param office_id: an office ``Id``
        :type office_id: ``osid.id.Id``
        :return: ``true`` if the ``office_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_child_of_office(self, id_, office_id):
        """Tests if an office is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :return: ``true`` if the ``Id`` is a child of ``office_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_child_office_ids(self, office_id):
        """Gets the child ``Ids`` of the given office.

        :param office_id: the ``Id`` to query
        :type office_id: ``osid.id.Id``
        :return: the children of the office
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_child_offices(self, office_id):
        """Gets the children of the given office.

        :param office_id: the ``Id`` to query
        :type office_id: ``osid.id.Id``
        :return: the children of the office
        :rtype: ``osid.workflow.OfficeList``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeList

    def is_descendant_of_office(self, id_, office_id):
        """Tests if an ``Id`` is a descendant of an office.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``office_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_office_node_ids(self, office_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given office.

        :param office_id: the ``Id`` to query
        :type office_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the availability.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the availability.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given availability, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an office node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Node

    def get_office_nodes(self, office_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given office.

        :param office_id: the ``Id`` to query
        :type office_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the availability.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the availability.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given availability, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an office node
        :rtype: ``osid.workflow.OfficeNode``
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.workflow.OfficeNode


class OfficeHierarchyDesignSession(osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Office`` objects.

    Each node in the hierarchy is a unique ``Office``.

    """
    def get_office_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    office_hierarchy_id = property(fget=get_office_hierarchy_id)

    def get_office_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    office_hierarchy = property(fget=get_office_hierarchy)

    def can_modify_office_hierarchy(self):
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

    def add_root_office(self, office_id):
        """Adds a root office.

        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``office_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``office_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_root_office(self, office_id):
        """Removes a root office.

        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``office_id`` is not a root
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def add_child_office(self, office_id, child_id):
        """Adds a child to an office.

        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``office_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``office_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``office_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_office(self, office_id, child_id):
        """Removes a child from an office.

        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``office_id`` is not parent of ``child_id``
        :raise: ``NullArgument`` -- ``office_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_offices(self, office_id):
        """Removes all children from an office.

        :param office_id: the ``Id`` of an office
        :type office_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``office_id`` is not found
        :raise: ``NullArgument`` -- ``office_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


