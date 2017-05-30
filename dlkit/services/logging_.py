# -*- coding: utf-8 -*-
"""Logging Open Service Interface Definitions
logging version 3.0.0

The Logging OSID provides a means to read and wite to logs. A Log
represents a collection of log entries. Each log entry is composed of a
priority ``Type,`` timestamp, ``Agent,`` the agent's associated
``Resource,`` and a record.

Logs can be organized into hierarchies for federation. A log that is a
parent of another log makes visible the log entries of its children.

Example
  LoggingSession out = manager.getLoggingSession();
  out.log(warningLogEntryPriorityType, "hello world", stringLogEntryContentType);
  
  LogReadingSession in = manager.getLogReadingSession();
  LogEntryList entries = inn.getLogEntries();
  while (entries.hasNext()) {
      LogEntry entry = entries.getNextLogEntry();
      printEntry(entry);
  }



"""

from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class LoggingProfile(osid_managers.OsidProfile):
    """The logging profile describes the interoperability among logging services."""

    def __init__(self):
        self._provider_manager = None


    def supports_logging(self):
        """Tests if logging is supported.

        :return: ``true`` if logging is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_log_entry_lookup(self):
        """Tests if reading logs is supported.

        :return: ``true`` if reading logs is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_log_entry_query(self):
        """Tests if querying log entries is supported.

        :return: ``true`` if querying log entries is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_log_lookup(self):
        """Tests for the availability of a log lookup service.

        :return: ``true`` if log lookup is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def supports_log_admin(self):
        """Tests for the availability of a log administrative service for creating and deleting logs.

        :return: ``true`` if log administration is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_log_entry_record_types(self):
        """Gets the supported ``Log`` record types.

        :return: a list containing the supported log record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    log_entry_record_types = property(fget=get_log_entry_record_types)

    def get_log_entry_search_record_types(self):
        """Gets the supported log entry search record types.

        :return: a list containing the supported log entry search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    log_entry_search_record_types = property(fget=get_log_entry_search_record_types)

    def get_log_record_types(self):
        """Gets the supported ``Log`` record types.

        :return: a list containing the supported log record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    log_record_types = property(fget=get_log_record_types)

    def get_log_search_record_types(self):
        """Gets the supported log search record types.

        :return: a list containing the supported log search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    log_search_record_types = property(fget=get_log_search_record_types)

    def get_priority_types(self):
        """Gets the priority types supported, in ascending order of the priority level.

        :return: a list containing the supported priority types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    priority_types = property(fget=get_priority_types)

    def get_content_types(self):
        """Gets the content types supported.

        :return: a list containing the supported content types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    content_types = property(fget=get_content_types)

    def supports_log_entry_admin(self):
        """Tests if log entry admin is supported.

        :return: ``true`` if log entry admin is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean
##
# The following methods are from osid.logging.LoggingSession

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


##
# The following methods are from osid.logging.LogEntryLookupSession

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


##
# The following methods are from osid.logging.LogEntryQuerySession

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


##
# The following methods are from osid.logging.LogEntryAdminSession

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


##
# The following methods are from osid.logging.LogLookupSession

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


##
# The following methods are from osid.logging.LogAdminSession

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




class LoggingManager(osid_managers.OsidManager, osid_sessions.OsidSession, LoggingProfile):
    """The logging manager provides access to logging sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``LoggingSession:`` a session to write to a log
      * ``LogEntryLookupSession:`` a session to read a log
      * ``LogEntryQuerySession:`` a session to search a log
      * ``LogEntrySearchSession:`` a session to search a log
      * ``LogEntryAdminSession:`` a session to manage log entries in a
        log
      * ``LogEntryNotificationSession:`` a session to subscribe to
        notifications of new log entries
      * ``LogEntryLogSession:`` a session to examine log entry to log
        mappings
      * ``LogEntryLogAssignmentSession:`` a session to manage log entry
        to log mappings
      * ``LogEntrySmartLogSession:`` a session to manage dynamic logs
      * ``LogLookupSession:`` a session to retrieve log objects
      * ``LogQuerySession:`` a session to search for logs
      * ``LogSearchSession:`` a session to search for logs
      * ``LogAdminSession:`` a session to create, update and delete logs
      * ``LogNotificationSession:`` a session to receive notifications
        for changes in logs
      * ``LogHierarchyTraversalSession:`` a session to traverse
        hierarchies of logs
      * ``LogHierarchyDesignSession:`` a session to manage hierarchies
        of logs


    The logging manager also provides a profile for determing the
    supported search types supported by this service.

    """

    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._log_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_log_view(self, session):
        """Sets the underlying log view to match current view"""
        if self._log_view == COMPARATIVE:
            try:
                session.use_comparative_log_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_log_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_log_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                proxy=self._proxy,
                                                manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:loggingProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('LOGGING', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('LOGGING', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()

    def get_logging_batch_manager(self):
        """Gets a ``LoggingBatchManager``.

        :return: a ``LoggingBatchManager``
        :rtype: ``osid.logging.batch.LoggingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_logging_batch()`` is ``true``.*

        """
        return # osid.logging.batch.LoggingBatchManager

    logging_batch_manager = property(fget=get_logging_batch_manager)
##
# The following methods are from osid.logging.LoggingSession

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


##
# The following methods are from osid.logging.LogEntryLookupSession

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


##
# The following methods are from osid.logging.LogEntryQuerySession

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


##
# The following methods are from osid.logging.LogEntryAdminSession

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


##
# The following methods are from osid.logging.LogLookupSession

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


##
# The following methods are from osid.logging.LogAdminSession

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




class LoggingProxyManager(osid_managers.OsidProxyManager, LoggingProfile):
    """The logging manager provides access to logging sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` for the
    purposes of passing information from server environments. The
    sessions included in this manager are:

      * ``LoggingSession:`` a session to write to a log
      * ``LogEntryLookupSession:`` a session to read a log
      * ``LogEntryQuerySession:`` a session to search a log
      * ``LogEntrySearchSession:`` a session to search a log
      * ``LogEntryAdminSession:`` a session to manage log entries in a
        log
      * ``LogEntryNotificationSession:`` a session to subscribe to
        notifications of new log entries
      * ``LogEntryLogSession:`` a session to examine log entry to log
        mappings
      * ``LogEntryLogAssignmentSession:`` a session to manage log entry
        to log mappings
      * ``LogEntrySmartLogSession:`` a session to manage dynamic logs
      * ``LogLookupSession:`` a session to retrieve log objects
      * ``LogQuerySession:`` a session to search for logs
      * ``LogSearchSession:`` a session to search for logs
      * ``LogAdminSession:`` a session to create, update and delete logs
      * ``LogNotificationSession:`` a session to receive notifications
        for changes in logs
      * ``LogHierarchyTraversalSession:`` a session to traverse
        hierarchies of logs
      * ``LogHierarchyDesignSession:`` a session to manage hierarchies
        of logs


    The logging manager also provides a profile for determing the
    supported search types supported by this service.

    """

    def get_logging_batch_proxy_manager(self):
        """Gets a ``LoggingBatchProxyManager``.

        :return: a ``LoggingBatchProxyManager``
        :rtype: ``osid.logging.batch.LoggingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_logging_batch()`` is ``true``.*

        """
        return # osid.logging.batch.LoggingBatchProxyManager

    logging_batch_proxy_manager = property(fget=get_logging_batch_proxy_manager)
##
# The following methods are from osid.logging.LoggingSession

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


##
# The following methods are from osid.logging.LogEntryLookupSession

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


##
# The following methods are from osid.logging.LogEntryQuerySession

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


##
# The following methods are from osid.logging.LogEntryAdminSession

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


##
# The following methods are from osid.logging.LogLookupSession

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


##
# The following methods are from osid.logging.LogAdminSession

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




class Log(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A ``Log`` represents a collection of entries.

    Like all ``OsidObjects,`` a ``Log`` is identified by its Id and any
    persisted references should use the ``Id``.

    """

    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, runtime, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        self._runtime = runtime
        osid.OsidObject.__init__(self, self._catalog)  # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy)  # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._log_view = DEFAULT
        self._object_views = dict()
        self._operable_views = dict()
        self._containable_views = dict()

    def _set_log_view(self, session):
        """Sets the underlying log view to match current view"""
        if self._log_view == FEDERATED:
            try:
                session.use_federated_log_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_log_view()
            except AttributeError:
                pass

    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_operable_view(self, session):
        """Sets the underlying operable views to match current view"""
        for obj_name in self._operable_views:
            if self._operable_views[obj_name] == ACTIVE:
                try:
                    getattr(session, 'use_active_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_any_status_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _set_containable_view(self, session):
        """Sets the underlying containable views to match current view"""
        for obj_name in self._containable_views:
            if self._containable_views[obj_name] == SEQUESTERED:
                try:
                    getattr(session, 'use_sequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_unsequestered_' + obj_name + '_view')()
                except AttributeError:
                    pass

    def _get_provider_session(self, session_name):
        """Returns the requested provider session.

        Instantiates a new one if the named session is not already known.

        """
        agent_key = self._get_agent_key()
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_log')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_log_view(session)
            self._set_object_view(session)
            self._set_operable_view(session)
            self._set_containable_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def get_log_id(self):
        """Gets the Id of this log."""
        return self._catalog_id

    def get_log(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self

    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id

    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self

    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError

    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        else:
            raise IllegalState()

    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()

    def get_log_record(self, log_record_type):
        """Gets the record corresponding to the given ``Log`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``log_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(log_record_type)`` is
        ``true`` .

        :param log_record_type: the type of log record to retrieve
        :type log_record_type: ``osid.type.Type``
        :return: the log record
        :rtype: ``osid.logging.records.LogRecord``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.records.LogRecord


class LogList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LogList`` provides a means for accessing ``Log`` elements sequentially either one at a time or many at a time.

    Examples: while (ll.hasNext()) { Log log = ll.getNextLog(); }

    or
      while (ll.hasNext()) {
           Log[] logs = ll.getNextLogs(ll.available());
      }

    """

    def get_next_log(self):
        """Gets the next ``Log`` in this list.

        :return: the next ``Log`` in this list. The ``has_next()`` method should be used to test that a next ``Log`` is available before calling this method.
        :rtype: ``osid.logging.Log``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.Log

    next_log = property(fget=get_next_log)

    def get_next_logs(self, n):
        """Gets the next set of ``Log`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Log`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Log`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.logging.Log``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.logging.Log


