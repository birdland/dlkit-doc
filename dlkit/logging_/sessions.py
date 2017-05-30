
from ..osid import sessions as osid_sessions


class LoggingSession(osid_sessions.OsidSession):
    """This session is used to log entries to a log."""

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the log
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.Log

    log = property(fget=get_log)

    def can_log(self):
        """Tests if this user can log.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer logging
        operations.

        :return: ``false`` if logging methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def log(self, content, content_type):
        """Logs an item.

        This method is a shortcut to ``createLogEntry()``.

        :param content: the entry to log
        :type content: ``object``
        :param content_type: the type of this entry which must be one of the types returned by ``LoggingManager.getContentTypes()``
        :type content_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``content`` is not of ``content_type``
        :raise: ``NullArgument`` -- ``content`` or ``content_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``LoggingManager.supportsContentType(contentType)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def log_at_priority(self, priority_type, content, content_type):
        """Logs an item.

        :param priority_type: the entry priority
        :type priority_type: ``osid.type.Type``
        :param content: the entry to log
        :type content: ``object``
        :param content_type: the type of this entry which must be one of the types returned by ``LoggingManager.getContentTypes()``
        :type content_type: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``content`` is not of ``content_type``
        :raise: ``NullArgument`` -- ``content`` , ``content_type`` or ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``LoggingManager.supportsContentType(contentType)`` is ``false`` or ``LoggingManager.supportsPriorityType(priorityType)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def get_log_entry_form(self):
        """Gets a log entry form for creating a log entry.

        :return: the log entry form
        :rtype: ``osid.logging.LogEntryForm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryForm

    log_entry_form = property(fget=get_log_entry_form)

    def create_log_entry(self, log_entry_form):
        """Logs an entry through the log entry form.

        :param log_entry_form: the log entry form
        :type log_entry_form: ``osid.logging.LogEntryForm``
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``log_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_form`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LogEntryLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``log entries``."""

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the log
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.Log

    log = property(fget=get_log)

    def can_read_log(self):
        """Tests if this user can read the log.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer reading
        operations.

        :return: ``false`` if reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_log_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_log_entry_view(self):
        """A complete view of the ``LogEntry`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_log_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in logs which are children
        of this log in the log hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this log only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_log_entry(self, log_entry_id):
        """Gets the ``LogEntry`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``LogEntry`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``LogEntry`` and retained for
        compatibility.

        :param log_entry_id: the ``Id`` of the ``LogEntry`` to retrieve
        :type log_entry_id: ``osid.id.Id``
        :return: the returned ``LogEntry``
        :rtype: ``osid.logging.LogEntry``
        :raise: ``NotFound`` -- no ``LogEntry`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntry

    def get_log_entries_by_ids(self, log_entry_ids):
        """Gets a ``LogEntryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the entries
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible logentries may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param log_entry_ids: the list of ``Ids`` to retrieve
        :type log_entry_ids: ``osid.id.IdList``
        :return: the returned ``LogEntry list``
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``log_entry_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_by_genus_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` corresponding to the given log entry genus ``Type`` which doe snot include entries of genus types derived form the specified ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session

        :param log_entry_genus_type: a log entry genus type
        :type log_entry_genus_type: ``osid.type.Type``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_by_parent_genus_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` corresponding to the given log entry genus ``Type`` and include any additional entries with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param log_entry_genus_type: a log entry genus type
        :type log_entry_genus_type: ``osid.type.Type``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_by_record_type(self, log_entry_genus_type):
        """Gets a ``LogEntryList`` containing the given log entry record ``Type``.

        In plenary mode, the returned list contains all known log
        entries or an error results. Otherwise, the returned list may
        contain only those log entries that are accessible through this
        session.

        :param log_entry_genus_type: a log entry genus type
        :type log_entry_genus_type: ``osid.type.Type``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_entry_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_by_priority_type(self, priority_type):
        """Gets a ``LogEntryList`` filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param priority_type: a log entry priority type
        :type priority_type: ``osid.type.Type``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_by_date(self, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param start: a starting time
        :type start: ``osid.calendaring.DateTime``
        :param end: a starting time
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_by_priority_type_and_date(self, priority_type, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param priority_type: a log entry priority type
        :type priority_type: ``osid.type.Type``
        :param start: a starting time
        :type start: ``osid.calendaring.DateTime``
        :param end: a starting time
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``priority_type, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_for_resource(self, resource_id):
        """Gets a ``LogEntryList`` for an agent associated with the given resource.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_by_date_for_resource(self, resource_id, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive for an agent associated with the given resource.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param start: a starting time
        :type start: ``osid.calendaring.DateTime``
        :param end: a starting time
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``resource_id, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries_by_priority_type_and_date_for_resource(self, resource_id, priority_type, start, end):
        """Gets a ``LogEntryList`` corresponding to the given time interval inclusive for an agent associated with the given resource filtering the list to log entries including and above the given priority ``Type``.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param priority_type: a log entry priority type
        :type priority_type: ``osid.type.Type``
        :param start: a starting time
        :type start: ``osid.calendaring.DateTime``
        :param end: a starting time
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``LogEntry`` list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``InvalidArgument`` -- ``start`` is greater than ``end``
        :raise: ``NullArgument`` -- ``resource_id, priority_type, start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    def get_log_entries(self):
        """Gets all log entries.

        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :return: a list of log entries
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList

    log_entries = property(fget=get_log_entries)


class LogEntryQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among log entries.

    The search query is constructed using the ``LogEntryQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated log view: searches include entries in logs of which
        this log is an ancestor in the log hierarchy
      * isolated log view: searches are restricted to entries in this
        log only

    """

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the ``Log`` associated with this session
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.Log

    log = property(fget=get_log)

    def can_search_log_entries(self):
        """Tests if this user can perform ``LogEntry`` searches.

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

    def use_federated_log_view(self):
        """Federates the view for methods in this session.

        A federated view will include entries in logs which are children
        of this log in the log hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this log only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_log_entry_query(self):
        """Gets a log entry query.

        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryQuery

    log_entry_query = property(fget=get_log_entry_query)

    def get_log_entries_by_query(self, log_entry_query):
        """Gets a list of log entries matching the given log entry query.

        :param log_entry_query: the log entry query
        :type log_entry_query: ``osid.logging.LogEntryQuery``
        :return: the returned ``LogEntryList``
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryList


class LogEntryAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``LogEntries``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``LogEntry,`` a ``LogEntryForm`` is requested using
    ``get_log_entry_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``LogEntryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``LogEntryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``LogEntryForm``
    corresponds to an attempted transaction.

    For updates, ``LogEntryForms`` are requested to the ``LogEntry``
    ``Id`` that is to be updated using ``getLogEntryFormForUpdate()``.
    Similarly, the ``LogEntryForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``LogEntryForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``LogEntries``. To unmap a ``LogEntry``
    from the current ``Log,`` the ``LogEntryLogAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``LogEntry`` itself thus removing it from all known ``Log``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the ``Log`` associated with this session
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.Log

    log = property(fget=get_log)

    def can_create_log_entries(self):
        """Tests if this user can create log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_log_entry_with_record_types(self, log_entry_record_types):
        """Tests if this user can create a single ``LogEntry`` using the desired record types.

        While ``LoggingManager.getLogEntryRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``LogEntry``.
        Providing an empty array tests if a ``LogEntry`` can be created
        with no records.

        :param log_entry_record_types: array of log entry record types
        :type log_entry_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``LogEntry`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_entry_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_log_entry_form_for_create(self, log_entry_record_types):
        """Gets the log entry form for creating new log entries.

        A new form should be requested for each create transaction.

        :param log_entry_record_types: array of log entry record types
        :type log_entry_record_types: ``osid.type.Type[]``
        :return: the log entry form
        :rtype: ``osid.logging.LogEntryForm``
        :raise: ``NullArgument`` -- ``log_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryForm

    def create_log_entry(self, log_entry_form):
        """Creates a new ``LogEntry``.

        :param log_entry_form: the form for this ``LogEntry``
        :type log_entry_form: ``osid.logging.LogEntryForm``
        :return: the new ``LogEntry``
        :rtype: ``osid.logging.LogEntry``
        :raise: ``IllegalState`` -- ``log_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``log_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_form`` did not originate from ``get_log_entry_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntry

    def can_update_log_entries(self):
        """Tests if this user can update log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_log_entry_form_for_update(self, log_entry_id):
        """Gets the log entry form for updating an existing log.

        A new log entry form should be requested for each update
        transaction.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: the log entry form
        :rtype: ``osid.logging.LogEntryForm``
        :raise: ``NotFound`` -- ``log_entry_id`` is not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogEntryForm

    def update_log_entry(self, log_entry_form):
        """Updates an existing log entry.

        :param log_entry_form: the form containing the elements to be updated
        :type log_entry_form: ``osid.logging.LogEntryForm``
        :raise: ``IllegalState`` -- ``log_entry_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``log_entry_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_form`` did not originate from ``get_log_entry_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_log_entries(self):
        """Tests if this user can delete log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_log_entry(self, log_entry_id):
        """Deletes a ``LogEntry``.

        :param log_entry_id: the ``Id`` of the ``log_entry_id`` to remove
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_entry_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_log_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for log entries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``LogEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_log_entry(self, log_entry_id, alias_id):
        """Adds an ``Id`` to a ``LogEntry`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``LogEntry`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another log entry, it is
        reassigned to the given log entry ``Id``.

        :param log_entry_id: the ``Id`` of a ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``log_entry_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class LogLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Log`` objects.

    The ``Log`` represents a collection of log entries.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Logs`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Logs`` referenced
    by it are available, and a test-taking applicationmay sacrifice some
    interoperability for the sake of precision.

    """

    def can_lookup_logs(self):
        """Tests if this user can perform ``Log`` lookups.

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

    def use_comparative_log_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_log_view(self):
        """A complete view of the ``Log`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_log(self, log_id):
        """Gets the ``Log`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Log`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Log`` and retained for compatibility.

        :param log_id: ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: the log
        :rtype: ``osid.logging.Log``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.logging.Log

    def get_logs_by_ids(self, log_ids):
        """Gets a ``LogList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the logs
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Logs`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param log_ids: the list of ``Ids`` to retrieve
        :type log_ids: ``osid.id.IdList``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``log_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogList

    def get_logs_by_genus_type(self, log_genus_type):
        """Gets a ``LogList`` corresponding to the given log genus ``Type`` which does not include logs of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :param log_genus_type: a log genus type
        :type log_genus_type: ``osid.type.Type``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogList

    def get_logs_by_parent_genus_type(self, log_genus_type):
        """Gets a ``LogList`` corresponding to the given log genus ``Type`` and include any additional logs with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :param log_genus_type: a log genus type
        :type log_genus_type: ``osid.type.Type``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogList

    def get_logs_by_record_type(self, log_record_type):
        """Gets a ``LogList`` containing the given log record ``Type``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :param log_record_type: a log record type
        :type log_record_type: ``osid.type.Type``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogList

    def get_logs_by_provider(self, resource_id):
        """Gets a ``LogList`` for a given provider.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Log list``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogList

    def get_logs(self):
        """Gets all ``Logs``.

        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :return: a list of ``Logs``
        :rtype: ``osid.logging.LogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogList

    logs = property(fget=get_logs)


class LogAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Logs``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Log,`` a ``LogForm`` is requested using
    ``get_log_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``LogForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``LogForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``LogForm`` corresponds
    to an attempted transaction.

    For updates, ``LogForms`` are requested to the ``Log``  ``Id`` that
    is to be updated using ``getLogFormForUpdate()``. Similarly, the
    ``LogForm`` has metadata about the data that can be updated and it
    can perform validation before submitting the update. The ``LogForm``
    can only be used once for a successful update and cannot be reused.

    The delete operations delete ``Logs``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

    def can_create_logs(self):
        """Tests if this user can create ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Log`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_log_with_record_types(self, log_record_types):
        """Tests if this user can create a single ``Log`` using the desired record types.

        While ``LoggingManager.getLogRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Log``.
        Providing an empty array tests if a ``Log`` can be created with
        no records.

        :param log_record_types: array of log record types
        :type log_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Log`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_log_form_for_create(self, log_record_types):
        """Gets the log form for creating new logs.

        A new form should be requested for each create transaction.

        :param log_record_types: array of log record types
        :type log_record_types: ``osid.type.Type[]``
        :return: the log form
        :rtype: ``osid.logging.LogForm``
        :raise: ``NullArgument`` -- ``log_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogForm

    def create_log(self, log_form):
        """Creates a new ``Log``.

        :param log_form: the form for this ``Log``
        :type log_form: ``osid.logging.LogForm``
        :return: the new ``Log``
        :rtype: ``osid.logging.Log``
        :raise: ``IllegalState`` -- ``log_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``log_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_form`` did not originate from ``get_log_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.Log

    def can_update_logs(self):
        """Tests if this user can update ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Log`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_log_form_for_update(self, log_id):
        """Gets the log form for updating an existing log.

        A new log form should be requested for each update transaction.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: the log form
        :rtype: ``osid.logging.LogForm``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.LogForm

    def update_log(self, log_form):
        """Updates an existing log.

        :param log_form: the form containing the elements to be updated
        :type log_form: ``osid.logging.LogForm``
        :raise: ``IllegalState`` -- ``log_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``log_id`` or ``log_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_form`` did not originate from ``get_log_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_logs(self):
        """Tests if this user can delete ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Log`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_log(self, log_id):
        """Deletes a ``Log``.

        :param log_id: the ``Id`` of the ``Log`` to remove
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_log_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Logs``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Log`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_log(self, log_id, alias_id):
        """Adds an ``Id`` to a ``Log`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Log`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another log, it is reassigned to the
        given log ``Id``.

        :param log_id: the ``Id`` of a ``Log``
        :type log_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


