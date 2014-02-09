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
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class LoggingProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if visible federation is supported.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_logging(self):
        """Tests if logging is supported.

        :return: ``true`` if logging is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_entry_lookup(self):
        """Tests if reading logs is supported.

        :return: ``true`` if reading logs is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_entry_query(self):
        """Tests if querying log entries is supported.

        :return: ``true`` if querying log entries is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_entry_search(self):
        """Tests if searching log entries is supported.

        :return: ``true`` if searching log entries is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_entry_notification(self):
        """Tests if log entry notification is supported,.

        :return: ``true`` if log entry notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_entry_log(self):
        """Tests if looking up log entry log mappings is supported.

        :return: ``true`` if log entry logs is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_entry_log_assignment(self):
        """Tests if managing log entry log mappings is supported.

        :return: ``true`` if log entry logs mapping assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_entry_smart_log(self):
        """Tests if smart logs is supported.

        :return: ``true`` if smart logs is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_lookup(self):
        """Tests for the availability of a log lookup service.

        :return: ``true`` if log lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_query(self):
        """Tests if querying logs is available.

        :return: ``true`` if log query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_search(self):
        """Tests if searching for logs is available.

        :return: ``true`` if log search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_admin(self):
        """Tests for the availability of a log administrative service for creating and deleting logs.

        :return: ``true`` if log administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_notification(self):
        """Tests for the availability of a log notification service.

        :return: ``true`` if log notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_hierarchy(self):
        """Tests for the availability of a log hierarchy traversal service.

        :return: ``true`` if log hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_log_hierarchy_design(self):
        """Tests for the availability of a log hierarchy design service.

        :return: ``true`` if log hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_logging_batch(self):
        """Tests for the availability of a logging batch service.

        :return: ``true`` if loggin batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_record_types(self):
        """Gets the supported ``Log`` record types.

        :return: a list containing the supported log record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    log_entry_record_types = property(fget=get_log_entry_record_types)

    def supports_log_entry_record_type(self, log_entry_record_type):
        """Tests if the given ``LogEntry`` record type is supported.

        :param log_entry_record_type: a ``Type`` indicating a ``LogEntry`` record type
        :type log_entry_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_entry_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_search_record_types(self):
        """Gets the supported log entry search record types.

        :return: a list containing the supported log entry search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    log_entry_search_record_types = property(fget=get_log_entry_search_record_types)

    def supports_log_entry_search_record_type(self, log_entry_search_record_type):
        """Tests if the given log entry search record type is supported.

        :param log_entry_search_record_type: a ``Type`` indicating a log entry record type
        :type log_entry_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_entry_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_log_record_types(self):
        """Gets the supported ``Log`` record types.

        :return: a list containing the supported log record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    log_record_types = property(fget=get_log_record_types)

    def supports_log_record_type(self, log_record_type):
        """Tests if the given ``Log`` record type is supported.

        :param log_record_type: a ``Type`` indicating a ``Log`` record type
        :type log_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_log_search_record_types(self):
        """Gets the supported log search record types.

        :return: a list containing the supported log search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    log_search_record_types = property(fget=get_log_search_record_types)

    def supports_log_search_record_type(self, log_search_record_type):
        """Tests if the given log search record type is supported.

        :param log_search_record_type: a ``Type`` indicating a log record type
        :type log_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_priority_types(self):
        """Gets the priority types supported, in ascending order of the priority level.

        :return: a list containing the supported priority types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    priority_types = property(fget=get_priority_types)

    def supports_priority_type(self, priority_type):
        """Tests if the priority type is supported.

        :param priority_type: a ``Type`` indicating a priority type
        :type priority_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_content_types(self):
        """Gets the content types supported.

        :return: a list containing the supported content types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    content_types = property(fget=get_content_types)

    def supports_content_type(self, content_type):
        """Tests if the content type is supported.

        :param content_type: a ``Type`` indicating a content type
        :type content_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``content_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class LoggingManager(osid_managers.OsidManager, osid_sessions.OsidSession, LoggingProfile):

    def get_logging_session(self):
        """Gets the ``OsidSession`` associated with the logging service.

        :return: a ``LoggingSession``
        :rtype: ``osid.logging.LoggingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging()`` is ``false``

        """
        raise UNIMPLEMENTED()

    logging_session = property(fget=get_logging_session)

    def get_logging_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the logging service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LoggingSession``
        :rtype: ``osid.logging.LoggingSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_lookup_session(self):
        """Gets the ``OsidSession`` associated with the log reading service.

        :return: a ``LogEntryLookupSession``
        :rtype: ``osid.logging.LogEntryLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_entry_lookup_session = property(fget=get_log_entry_lookup_session)

    def get_log_entry_lookup_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the log reading service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntryLookupSession``
        :rtype: ``osid.logging.LogEntryLookupSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_query_session(self):
        """Gets the ``OsidSession`` associated with the logging entry query service.

        :return: a ``LogEntryQuerySession``
        :rtype: ``osid.logging.LogEntryQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_entry_query_session = property(fget=get_log_entry_query_session)

    def get_log_entry_query_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the log entry query service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntryQuerySession``
        :rtype: ``osid.logging.LogEntryQuerySession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_search_session(self):
        """Gets the ``OsidSession`` associated with the logging entry search service.

        :return: a ``LogEntrySearchSession``
        :rtype: ``osid.logging.LogEntrySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_entry_search_session = property(fget=get_log_entry_search_session)

    def get_log_entry_search_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the log entry search service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntrySearchSession``
        :rtype: ``osid.logging.LogEntrySearchSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_admin_session(self):
        """Gets the ``OsidSession`` associated with the logging entry administrative service.

        :return: a ``LogEntryAdminSession``
        :rtype: ``osid.logging.LogEntryAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_entry_admin_session = property(fget=get_log_entry_admin_session)

    def get_log_entry_admin_session_for_log(self, log_id):
        """Gets the ``OsidSession`` associated with the log entry administrative service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntryAdminSession``
        :rtype: ``osid.logging.LogEntryAdminSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_notification_session(self, log_entry_receiver):
        """Gets the ``OsidSession`` associated with the logging entry notification service.

        :param log_entry_receiver: the receiver
        :type log_entry_receiver: ``osid.logging.LogEntryReceiver``
        :return: a ``LogEntryNotificationSession``
        :rtype: ``osid.logging.LogEntryNotificationSession``
        :raise: ``NullArgument`` -- ``log_entry_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_notification_session_for_log(self, log_entry_receiver, log_id):
        """Gets the ``OsidSession`` associated with the log entry notification service for the given log.

        :param log_entry_receiver: the receiver
        :type log_entry_receiver: ``osid.logging.LogEntryReceiver``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntryNotificationSession``
        :rtype: ``osid.logging.LogEntryNotificationSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_entry_receiver`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_log_session(self):
        """Gets the session for retrieving log entry to log mappings.

        :return: a ``LogEntryLogSession``
        :rtype: ``osid.logging.LogEntryLogSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_log()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_entry_log_session = property(fget=get_log_entry_log_session)

    def get_log_entry_log_assignment_session(self):
        """Gets the session for assigning log entry to logs mappings.

        :return: a ``LogEntryLogAssignmentSession``
        :rtype: ``osid.logging.LogEntryLogAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_log_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_entry_log_assignment_session = property(fget=get_log_entry_log_assignment_session)

    def get_log_entry_smart_log_session(self, log_id):
        """Gets the session for managing dynamic logEntry log.

        :param log_id: the ``Id`` of the log
        :type log_id: ``osid.id.Id``
        :return: a ``LogEntrySmartLogSession``
        :rtype: ``osid.logging.LogEntrySmartLogSession``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_smart_log()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_lookup_session(self):
        """Gets the ``OsidSession`` associated with the log lookup service.

        :return: a ``LogLookupSession``
        :rtype: ``osid.logging.LogLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_lookup_session = property(fget=get_log_lookup_session)

    def get_log_query_session(self):
        """Gets the ``OsidSession`` associated with the log query service.

        :return: a ``LogQuerySession``
        :rtype: ``osid.logging.LogQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_query_session = property(fget=get_log_query_session)

    def get_log_search_session(self):
        """Gets the ``OsidSession`` associated with the log search service.

        :return: a ``LogSearchSession``
        :rtype: ``osid.logging.LogSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_search_session = property(fget=get_log_search_session)

    def get_log_admin_session(self):
        """Gets the ``OsidSession`` associated with the log administrative service.

        :return: a ``LogAdminSession``
        :rtype: ``osid.logging.LogAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_admin_session = property(fget=get_log_admin_session)

    def get_log_notification_session(self, log_receiver):
        """Gets the ``OsidSession`` associated with the log notification service.

        :param log_receiver: the receiver
        :type log_receiver: ``osid.logging.LogReceiver``
        :return: a ``LogNotificationSession``
        :rtype: ``osid.logging.LogNotificationSession``
        :raise: ``NullArgument`` -- ``log_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the log hierarchy service.

        :return: a ``LogHierarchySession`` for logs
        :rtype: ``osid.logging.LogHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_hierarchy_session = property(fget=get_log_hierarchy_session)

    def get_log_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the log hierarchy design service.

        :return: a ``HierarchyDesignSession`` for logs
        :rtype: ``osid.logging.LogHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    log_hierarchy_design_session = property(fget=get_log_hierarchy_design_session)

    def get_logging_batch_manager(self):
        """Gets a ``LoggingBatchManager``.

        :return: a ``LoggingBatchManager``
        :rtype: ``osid.logging.batch.LoggingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    logging_batch_manager = property(fget=get_logging_batch_manager)


##
# The following methods are from osid.logging.LoggingSession

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the log
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_log_entry_form(self):
        """Gets a log entry form for creating a log entry.

        :return: the log entry form
        :rtype: ``osid.logging.LogEntryForm``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryLookupSession

    def can_read_log(self):
        """Tests if this user can read the log.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer reading
        operations.

        :return: ``false`` if reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_log_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_log_entry_view(self):
        """A complete view of the ``LogEntry`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_log_view(self):
        """Federates the view for methods in this session.
        A federated view will include entries in logs which are children
        of this log in the log hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this log only.



        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_log_entries(self):
        """Gets all log entries.
        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.

        :return: a list of log entries
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    log_entries = property(fget=get_log_entries)


##
# The following methods are from osid.logging.LogEntryQuerySession

    def can_search_log_entries(self):
        """Tests if this user can perform ``LogEntry`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_query(self):
        """Gets a log entry query.

        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntrySearchSession

    def get_log_entry_search(self):
        """Gets a log entry search.

        :return: the log entry search
        :rtype: ``osid.logging.LogEntrySearch``

        """
        raise UNIMPLEMENTED()

    log_entry_search = property(fget=get_log_entry_search)

    def get_log_entry_search_order(self):
        """Gets a log entry search order.
        The ``LogEntrySearchOrder`` is supplied to a ``LogEntrySearch``
        to specify the ordering of results.

        :return: the log entry search order
        :rtype: ``osid.logging.LogEntrySearchOrder``

        """
        raise UNIMPLEMENTED()

    log_entry_search_order = property(fget=get_log_entry_search_order)

    def get_log_entries_by_search(self, log_entry_query, log_entry_search):
        """Gets the search results matching the given search query using the given search.

        :param log_entry_query: the log entry query
        :type log_entry_query: ``osid.logging.LogEntryQuery``
        :param log_entry_search: the log entry search
        :type log_entry_search: ``osid.logging.LogEntrySearch``
        :return: the returned search results
        :rtype: ``osid.logging.LogEntrySearchResults``
        :raise: ``NullArgument`` -- ``log_entry_query`` or ``log_entry_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_query`` or ``log_entry_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_log_entry_query_from_inspector(self, log_entry_query_inspector):
        """Gets a log entry query from an inspector.
        The inspector is available from a ``LogEntrySearchResults``.

        :param log_entry_query_inspector: a log entry query inspector
        :type log_entry_query_inspector: ``osid.logging.LogQueryInspector``
        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``
        :raise: ``NullArgument`` -- ``log_entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``log_entry_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryAdminSession

    def can_create_log_entries(self):
        """Tests if this user can create log entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_log_entry_form_for_create(self, log_entry_record_types):
        """Gets the log entry form for creating new log entries.
        A new form should be requested for each create transaction.

        :param log_entry_record_types: array of log entry record types
        :type log_entry_record_types: ``osid.type.Type[]``
        :return: the log entry form
        :rtype: ``osid.logging.LogForm``
        :raise: ``NullArgument`` -- ``log_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def can_update_log_entries(self):
        """Tests if this user can update log entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def can_delete_log_entries(self):
        """Tests if this user can delete log entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``LogEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_log_entry(self, log_entry_id):
        """Deletes a ``LogEntry``.

        :param log_entry_id: the ``Id`` of the ``log_entry_id`` to remove
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_entry_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_log_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for log entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``LogEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryNotificationSession

    def can_register_for_log_entry_notifications(self):
        """Tests if this user can register for ``Log`` entry notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_entries(self):
        """Register for notifications of new log entries.
        ``LogEntryReceiver.newLogEntry()`` is invoked when a new
        ``LogEntry`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_entries_at_priority(self, priority_type):
        """Register for notifications of new log entries at or above the given priority type.
        ``LogEntryReceiver.newLogEntry()`` is invoked when a new
        ``LogEntry`` is created.

        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_entries_for_resource(self, resource_id):
        """Register for notifications of new log entries logged by an agent associated with the given resource.
        ``LogEntryReceiver.newLogEntry()`` is invoked when a new
        ``LogEntry`` is created.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_log_entries(self):
        """Register for notifications of updated log entries.
        ``LogEntryReceiver.changedLogEntry()`` is invoked when a
        ``LogEntry`` iin this log is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_changed_entries_at_priority(self, priority_type):
        """Register for notifications of updated log entries at or above the given priority type.
        ``LogEntryReceiver.changedLogEntry()`` is invoked when a
        ``LogEntry`` in this log is changed.

        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_changed_entries_for_resource(self, resource_id):
        """Register for notifications of updated log entries logged by an agent associated with the given resource.
        ``LogEntryReceiver.changedLogEntry()`` is invoked when a
        ``LogEntry`` in this log is changed.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_log_entry(self, log_entry_id):
        """Registers for notification of an updated log entry.
        ``LogEntryReceiver.changedLogENtry()`` is invoked when the
        specified log entry is changed.

        :param log_entry_id: the ``Id`` of the ``LogEntry`` to monitor
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_entries(self):
        """Registers for notification of deleted log entries.
        ``LogEntryReceiver.deletedLogEntry()`` is invoked when a log
        entry is deleted or removed from this log.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_entries_at_priority(self, priority_type):
        """Register for notifications of deleted log entries at or above the given priority type.
        ``LogEntryReceiver.deletedLogEntry()`` is invoked when a
        ``LogEntry`` is deleted or removed from this log.

        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_entries_for_resource(self, resource_id):
        """Register for notifications of deleted log entries logged by an agent associated with the given resource.
        ``LogEntryReceiver.deletedLogEntry()`` is invoked when a
        ``LogEntry`` is deleted or removed from this log.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_entry(self, log_entry_id):
        """Registers for notification of a deleted log entry.
        ``LogEntryReceiver.deleteddLogENtry()`` is invoked when the
        specified log entry is deleted or removed from this log.

        :param log_entry_id: the ``Id`` of the ``LogEntry`` to monitor
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryLogSession

    def use_comparative_log_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_log_view(self):
        """A complete view of the ``LogEntry`` and ``Log`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def can_lookup_log_entry_log_mappings(self):
        """Tests if this user can perform lookups of logEntry/log mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_ids_by_log(self, log_id):
        """Gets the list of ``LogEntry``  ``Ids`` associated with a ``Log``.

        :param log_id: ``Id`` of a ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of related logEntry ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_entries_by_log(self, log_id):
        """Gets the list of log entries associated with a ``Log``.

        :param log_id: ``Id`` of a ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of related logEntry
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_entrie_by_log(self, log_ids):
        """Gets the list of log entries corresponding to a list of ``Log``.

        :param log_ids: list of log ``Ids``
        :type log_ids: ``osid.id.IdList``
        :return: list of log entries
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_ids_by_log_entry(self, log_entry_id):
        """Gets the list of ``Log``  ``Ids`` mapped to a ``LogEntry``.

        :param log_entry_id: ``Id`` of a ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_entry_id`` is not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_by_log_entry(self, log_entry_id):
        """Gets the list of ``Log`` objects mapped to a ``LogEntry``.

        :param log_entry_id: ``Id`` of a ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of log
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- ``log_entry_id`` is not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryLogAssignmentSession

    def can_assign_log_entries(self):
        """Tests if this user can alter log entry/log mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_log_entries_to_log(self, log_id):
        """Tests if this user can alter log entry/log mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_log_ids(self, log_id):
        """Gets a list of log including and under the given log node in which any log entry can be assigned.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of assignable log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_log_ids_for_log_entry(self, log_id, log_entry_id):
        """Gets a list of log including and under the given log node in which a specific log entry can be assigned.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of assignable log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_id`` or ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_log_entry_to_log(self, log_entry_id, log_id):
        """Adds an existing ``LogEntry`` to a ``Log``.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_entry_id`` is already assigned to ``log_id``
        :raise: ``NotFound`` -- ``log_entry_id`` or ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_log_entry_from_log(self, log_entry_id, log_id):
        """Removes a ``LogEntry`` from a ``Log``.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_entry_id`` or ``log_id`` not found or ``log_entry_id`` not assigned to ``log_id``
        :raise: ``NullArgument`` -- ``log_entry_id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntrySmartLogSession

    def can_manage_smart_log(self):
        """Tests if this user can manage smart log.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart log management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_log_entry_query(self, log_entry_query):
        """Applies a logEntry query to this log.

        :param log_entry_query: the logEntry query
        :type log_entry_query: ``osid.logging.LogEntryQuery``
        :raise: ``NullArgument`` -- ``log_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``log_entry_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_log_entry_query(self):
        """Gets a logEntry query inspector for this log.

        :return: the logEntry query inspector
        :rtype: ``osid.logging.LogEntryQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_log_entry_sequencing(self, log_entry_search_order):
        """Applies a logEntry search order to this log.

        :param log_entry_search_order: the logEntry search order
        :type log_entry_search_order: ``osid.logging.LogEntrySearchOrder``
        :raise: ``NullArgument`` -- ``log_entry_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``log_entry_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_logs(self):
        """Gets all ``Logs``.
        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.

        :return: a list of ``Logs``
        :rtype: ``osid.logging.LogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    logs = property(fget=get_logs)


##
# The following methods are from osid.logging.LogQuerySession

    def can_search_logs(self):
        """Tests if this user can perform ``Log`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_log_query(self):
        """Gets a log query.

        :return: the log query
        :rtype: ``osid.logging.LogQuery``

        """
        raise UNIMPLEMENTED()

    log_query = property(fget=get_log_query)

    def get_logs_by_query(self, log_query):
        """Gets a list of ``Logs`` matching the given log query.

        :param log_query: the log query
        :type log_query: ``osid.logging.LogQuery``
        :return: the returned ``LogList``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogSearchSession

    def get_log_search(self):
        """Gets a log search.

        :return: the log search
        :rtype: ``osid.logging.LogSearch``

        """
        raise UNIMPLEMENTED()

    log_search = property(fget=get_log_search)

    def get_log_search_order(self):
        """Gets a log search order.
        The ``LogSearchOrder`` is supplied to a ``LogSearch`` to specify
        the ordering of results.

        :return: the log search order
        :rtype: ``osid.logging.LogSearchOrder``

        """
        raise UNIMPLEMENTED()

    log_search_order = property(fget=get_log_search_order)

    def get_logs_by_search(self, log_query, log_search):
        """Gets the search results matching the given search.

        :param log_query: the log query
        :type log_query: ``osid.logging.LogQuery``
        :param log_search: the log search
        :type log_search: ``osid.logging.LogSearch``
        :return: the log search results
        :rtype: ``osid.logging.LogSearchResults``
        :raise: ``NullArgument`` -- ``log_query`` or ``log_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_query`` or ``log_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_log_query_from_inspector(self, log_query_inspector):
        """Gets a log query from an inspector.
        The inspector is available from a ``LogSearchResults``.

        :param log_query_inspector: a log query inspector
        :type log_query_inspector: ``osid.logging.LogQueryInspector``
        :return: the log query
        :rtype: ``osid.logging.LogQuery``
        :raise: ``NullArgument`` -- ``log_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``log_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def can_update_logs(self):
        """Tests if this user can update ``Logs``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Log`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def can_delete_logs(self):
        """Tests if this user can delete ``Logs``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Log`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_log(self, log_id):
        """Deletes a ``Log``.

        :param log_id: the ``Id`` of the ``Log`` to remove
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_log_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Logs``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Log`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogNotificationSession

    def can_register_for_log_notifications(self):
        """Tests if this user can register for ``Log`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_logs(self):
        """Register for notifications of new logs.
        ``LogReceiver.newLog()`` is invoked when a new ``Log`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_ancestors(self, log_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified log.
        ``LogReceiver.newAncestorLog()`` is invoked when the specified
        log node gets a new ancestor.

        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_descendants(self, log_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified log.
        ``LogReceiver.newDescendantLog()`` is invoked when the specified
        log node gets a new descendant.

        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_logs(self):
        """Registers for notification of updated logs.
        ``LogReceiver.changedLog()`` is invoked when a log is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_log(self, log_id):
        """Registers for notification of an updated log.
        ``LogReceiver.changedLog()`` is invoked when the specified log
        is changed.

        :param log_id: the ``Id`` of the ``Log`` to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_logs(self):
        """Registers for notification of deleted logs.
        ``LogReceiver.deletedLog()`` is invoked when a log is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log(self, log_id):
        """Registers for notification of a deleted log.
        ``LogReceiver.deletedLog()`` is invoked when the specified log
        is deleted.

        :param log_id: the ``Id`` of the ``Log`` to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_ancestors(self, log_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified log.
        ``LogReceiver.deletedAncestor()`` is invoked when the specified
        log node loses an ancestor.

        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_descendants(self, log_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified log.
        ``LogReceiver.deletedDescendant()`` is invoked when the
        specified log node loses a descendant.

        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogHierarchySession

    def get_log_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    def get_log_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    log_hierarchy = property(fget=get_log_hierarchy)

    def can_access_log_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_log_ids(self):
        """Gets the root log ``Ids`` in this hierarchy.

        :return: the root log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_log_ids = property(fget=get_root_log_ids)

    def get_root_logs(self):
        """Gets the root logs in the log hierarchy.
        A node with no parents is an orphan. While all log ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root logs
        :rtype: ``osid.logging.LogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_logs = property(fget=get_root_logs)

    def has_parent_logs(self, log_id):
        """Tests if the ``Log`` has any parents.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the log has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a direct parent of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_log_ids(self, log_id):
        """Gets the parent ``Ids`` of the given log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the log
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_logs(self, log_id):
        """Gets the parent logs of the given ``id``.

        :param log_id: the ``Id`` of the ``Log`` to query
        :type log_id: ``osid.id.Id``
        :return: the parent logs of the ``id``
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- a ``Log`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_log(self, id_, log_id):
        """Tests if an ``Id`` is an ancestor of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is an ancestor of the ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_logs(self, log_id):
        """Tests if a log has any children.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``log_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a direct child of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a child of ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_log_ids(self, log_id):
        """Gets the child ``Ids`` of the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_logs(self, log_id):
        """Gets the child logs of the given ``id``.

        :param log_id: the ``Id`` of the ``Log`` to query
        :type log_id: ``osid.id.Id``
        :return: the child logs of the ``id``
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- a ``Log`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a descendant of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_node_ids(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a log node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_nodes(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a log node
        :rtype: ``osid.logging.LogNode``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogHierarchyDesignSession

    def can_modify_log_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_log(self, log_id):
        """Adds a root log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_log(self, log_id):
        """Removes a root log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` is not a root
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_log(self, log_id, child_id):
        """Adds a child to a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``log_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_log(self, log_id, child_id):
        """Removes a child from a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``log_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_logs(self, log_id):
        """Removes all children from a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class LoggingProxyManager(osid_managers.OsidProxyManager, LoggingProfile):

    def get_logging_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LoggingSession``
        :rtype: ``osid.logging.LoggingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_logging_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the logging service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LoggingSession``
        :rtype: ``osid.logging.LoggingSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging reading service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryLookupSession``
        :rtype: ``osid.logging.LogEntryLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_lookup_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log reading service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryLookupSession``
        :rtype: ``osid.logging.LogEntryLookupSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging entry query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryQuerySession``
        :rtype: ``osid.logging.LogEntryQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_query_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log entry query service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryQuerySession``
        :rtype: ``osid.logging.LogEntryQuerySession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging entry search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntrySearchSession``
        :rtype: ``osid.logging.LogEntrySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_search_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log entry search service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntrySearchSession``
        :rtype: ``osid.logging.LogEntrySearchSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the logging entry administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryAdminSession``
        :rtype: ``osid.logging.LogEntryAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_admin_session_for_log(self, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log entry administrative service for the given log.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryAdminSession``
        :rtype: ``osid.logging.LogEntryAdminSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_notification_session(self, log_entry_receiver, proxy):
        """Gets the ``OsidSession`` associated with the logging entry notification service.

        :param log_entry_receiver: the receiver
        :type log_entry_receiver: ``osid.logging.LogEntryReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryNotificationSession``
        :rtype: ``osid.logging.LogEntryNotificationSession``
        :raise: ``NullArgument`` -- ``log_entry_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_notification_session_for_log(self, log_entry_receiver, log_id, proxy):
        """Gets the ``OsidSession`` associated with the log entry notification service for the given log.

        :param log_entry_receiver: the receiver
        :type log_entry_receiver: ``osid.logging.LogEntryReceiver``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryNotificationSession``
        :rtype: ``osid.logging.LogEntryNotificationSession``
        :raise: ``NotFound`` -- no ``Log`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``log_entry_receiver, log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_log_session(self, proxy):
        """Gets the session for retrieving log entry to log mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryLogSession``
        :rtype: ``osid.logging.LogEntryLogSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_log()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_log_assignment_session(self, proxy):
        """Gets the session for assigning log entry to log mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntryLogAssignmentSession``
        :rtype: ``osid.logging.LogEntryLogAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_log_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_smart_log_session(self, log_id, proxy):
        """Gets the session for managing dynamic log entry logs.

        :param log_id: the ``Id`` of the log
        :type log_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogEntrySmartLogSession``
        :rtype: ``osid.logging.LogEntrySmartLogSession``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_entry_smart_log()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogLookupSession``
        :rtype: ``osid.logging.LogLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogQuerySession``
        :rtype: ``osid.logging.LogQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogSearchSession``
        :rtype: ``osid.logging.LogSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogAdminSession``
        :rtype: ``osid.logging.LogAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_notification_session(self, log_receiver, proxy):
        """Gets the ``OsidSession`` associated with the log notification service.

        :param log_receiver: the receiver
        :type log_receiver: ``osid.logging.LogReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogNotificationSession``
        :rtype: ``osid.logging.LogNotificationSession``
        :raise: ``NullArgument`` -- ``log_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LogHierarchySession`` for logs
        :rtype: ``osid.logging.LogHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_log_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the log hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession`` for logs
        :rtype: ``osid.logging.LogHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_log_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_logging_batch_proxy_manager(self):
        """Gets a ``LoggingBatchProxyManager``.

        :return: a ``LoggingBatchProxyManager``
        :rtype: ``osid.logging.batch.LoggingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_logging_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    logging_batch_proxy_manager = property(fget=get_logging_batch_proxy_manager)


##
# The following methods are from osid.logging.LoggingSession

    def get_log_id(self):
        """Gets the ``Log``  ``Id`` associated with this session.

        :return: the ``Log Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    log_id = property(fget=get_log_id)

    def get_log(self):
        """Gets the ``Log`` associated with this session.

        :return: the log
        :rtype: ``osid.logging.Log``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_log_entry_form(self):
        """Gets a log entry form for creating a log entry.

        :return: the log entry form
        :rtype: ``osid.logging.LogEntryForm``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryLookupSession

    def can_read_log(self):
        """Tests if this user can read the log.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer reading
        operations.


        :return: ``false`` if reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_log_entry_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_log_entry_view(self):
        """A complete view of the ``LogEntry`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def use_federated_log_view(self):
        """Federates the view for methods in this session.
        A federated view will include entries in logs which are children
        of this log in the log hierarchy.




        """
        raise UNIMPLEMENTED()

    def use_isolated_log_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this log only.




        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_log_entries(self):
        """Gets all log entries.
        In plenary mode, the returned list contains all known entries or
        an error results. Otherwise, the returned list may contain only
        those entries that are accessible through this session.


        :return: a list of log entries
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    log_entries = property(fget=get_log_entries)


##
# The following methods are from osid.logging.LogEntryQuerySession

    def can_search_log_entries(self):
        """Tests if this user can perform ``LogEntry`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_query(self):
        """Gets a log entry query.

        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntrySearchSession

    def get_log_entry_search(self):
        """Gets a log entry search.

        :return: the log entry search
        :rtype: ``osid.logging.LogEntrySearch``

        """
        raise UNIMPLEMENTED()

    log_entry_search = property(fget=get_log_entry_search)

    def get_log_entry_search_order(self):
        """Gets a log entry search order.
        The ``LogEntrySearchOrder`` is supplied to a ``LogEntrySearch``
        to specify the ordering of results.


        :return: the log entry search order
        :rtype: ``osid.logging.LogEntrySearchOrder``

        """
        raise UNIMPLEMENTED()

    log_entry_search_order = property(fget=get_log_entry_search_order)

    def get_log_entries_by_search(self, log_entry_query, log_entry_search):
        """Gets the search results matching the given search query using the given search.

        :param log_entry_query: the log entry query
        :type log_entry_query: ``osid.logging.LogEntryQuery``
        :param log_entry_search: the log entry search
        :type log_entry_search: ``osid.logging.LogEntrySearch``
        :return: the returned search results
        :rtype: ``osid.logging.LogEntrySearchResults``
        :raise: ``NullArgument`` -- ``log_entry_query`` or ``log_entry_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_entry_query`` or ``log_entry_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_log_entry_query_from_inspector(self, log_entry_query_inspector):
        """Gets a log entry query from an inspector.
        The inspector is available from a ``LogEntrySearchResults``.


        :param log_entry_query_inspector: a log entry query inspector
        :type log_entry_query_inspector: ``osid.logging.LogQueryInspector``
        :return: the log entry query
        :rtype: ``osid.logging.LogEntryQuery``
        :raise: ``NullArgument`` -- ``log_entry_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``log_entry_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryAdminSession

    def can_create_log_entries(self):
        """Tests if this user can create log entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``LogEntry`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_log_entry_form_for_create(self, log_entry_record_types):
        """Gets the log entry form for creating new log entries.
        A new form should be requested for each create transaction.


        :param log_entry_record_types: array of log entry record types
        :type log_entry_record_types: ``osid.type.Type[]``
        :return: the log entry form
        :rtype: ``osid.logging.LogForm``
        :raise: ``NullArgument`` -- ``log_entry_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def can_update_log_entries(self):
        """Tests if this user can update log entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.


        :return: ``false`` if ``LogEntry`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def can_delete_log_entries(self):
        """Tests if this user can delete log entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``LogEntry`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``LogEntry`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_log_entry(self, log_entry_id):
        """Deletes a ``LogEntry``.

        :param log_entry_id: the ``Id`` of the ``log_entry_id`` to remove
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_entry_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_log_entry_aliases(self):
        """Tests if this user can manage ``Id`` aliases for log entries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``LogEntry`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryNotificationSession

    def can_register_for_log_entry_notifications(self):
        """Tests if this user can register for ``Log`` entry notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_entries(self):
        """Register for notifications of new log entries.
        ``LogEntryReceiver.newLogEntry()`` is invoked when a new
        ``LogEntry`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_entries_at_priority(self, priority_type):
        """Register for notifications of new log entries at or above the given priority type.
        ``LogEntryReceiver.newLogEntry()`` is invoked when a new
        ``LogEntry`` is created.


        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_entries_for_resource(self, resource_id):
        """Register for notifications of new log entries logged by an agent associated with the given resource.
        ``LogEntryReceiver.newLogEntry()`` is invoked when a new
        ``LogEntry`` is created.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_log_entries(self):
        """Register for notifications of updated log entries.
        ``LogEntryReceiver.changedLogEntry()`` is invoked when a
        ``LogEntry`` iin this log is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_changed_entries_at_priority(self, priority_type):
        """Register for notifications of updated log entries at or above the given priority type.
        ``LogEntryReceiver.changedLogEntry()`` is invoked when a
        ``LogEntry`` in this log is changed.


        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_changed_entries_for_resource(self, resource_id):
        """Register for notifications of updated log entries logged by an agent associated with the given resource.
        ``LogEntryReceiver.changedLogEntry()`` is invoked when a
        ``LogEntry`` in this log is changed.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_log_entry(self, log_entry_id):
        """Registers for notification of an updated log entry.
        ``LogEntryReceiver.changedLogENtry()`` is invoked when the
        specified log entry is changed.


        :param log_entry_id: the ``Id`` of the ``LogEntry`` to monitor
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_entries(self):
        """Registers for notification of deleted log entries.
        ``LogEntryReceiver.deletedLogEntry()`` is invoked when a log
        entry is deleted or removed from this log.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_entries_at_priority(self, priority_type):
        """Register for notifications of deleted log entries at or above the given priority type.
        ``LogEntryReceiver.deletedLogEntry()`` is invoked when a
        ``LogEntry`` is deleted or removed from this log.


        :param priority_type: a priority type
        :type priority_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``priority_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_entries_for_resource(self, resource_id):
        """Register for notifications of deleted log entries logged by an agent associated with the given resource.
        ``LogEntryReceiver.deletedLogEntry()`` is invoked when a
        ``LogEntry`` is deleted or removed from this log.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_entry(self, log_entry_id):
        """Registers for notification of a deleted log entry.
        ``LogEntryReceiver.deleteddLogENtry()`` is invoked when the
        specified log entry is deleted or removed from this log.


        :param log_entry_id: the ``Id`` of the ``LogEntry`` to monitor
        :type log_entry_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryLogSession

    def use_comparative_log_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_log_view(self):
        """A complete view of the ``LogEntry`` and ``Log`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def can_lookup_log_entry_log_mappings(self):
        """Tests if this user can perform lookups of logEntry/log mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.


        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_log_entry_ids_by_log(self, log_id):
        """Gets the list of ``LogEntry``  ``Ids`` associated with a ``Log``.

        :param log_id: ``Id`` of a ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of related logEntry ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_entries_by_log(self, log_id):
        """Gets the list of log entries associated with a ``Log``.

        :param log_id: ``Id`` of a ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of related logEntry
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_entrie_by_log(self, log_ids):
        """Gets the list of log entries corresponding to a list of ``Log``.

        :param log_ids: list of log ``Ids``
        :type log_ids: ``osid.id.IdList``
        :return: list of log entries
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``NullArgument`` -- ``log_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_ids_by_log_entry(self, log_entry_id):
        """Gets the list of ``Log``  ``Ids`` mapped to a ``LogEntry``.

        :param log_entry_id: ``Id`` of a ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_entry_id`` is not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_by_log_entry(self, log_entry_id):
        """Gets the list of ``Log`` objects mapped to a ``LogEntry``.

        :param log_entry_id: ``Id`` of a ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of log
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- ``log_entry_id`` is not found
        :raise: ``NullArgument`` -- ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntryLogAssignmentSession

    def can_assign_log_entries(self):
        """Tests if this user can alter log entry/log mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.


        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_log_entries_to_log(self, log_id):
        """Tests if this user can alter log entry/log mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.


        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_log_ids(self, log_id):
        """Gets a list of log including and under the given log node in which any log entry can be assigned.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :return: list of assignable log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_log_ids_for_log_entry(self, log_id, log_entry_id):
        """Gets a list of log including and under the given log node in which a specific log entry can be assigned.

        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :return: list of assignable log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_id`` or ``log_entry_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_log_entry_to_log(self, log_entry_id, log_id):
        """Adds an existing ``LogEntry`` to a ``Log``.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_entry_id`` is already assigned to ``log_id``
        :raise: ``NotFound`` -- ``log_entry_id`` or ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_entry_id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_log_entry_from_log(self, log_entry_id, log_id):
        """Removes a ``LogEntry`` from a ``Log``.

        :param log_entry_id: the ``Id`` of the ``LogEntry``
        :type log_entry_id: ``osid.id.Id``
        :param log_id: the ``Id`` of the ``Log``
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_entry_id`` or ``log_id`` not found or ``log_entry_id`` not assigned to ``log_id``
        :raise: ``NullArgument`` -- ``log_entry_id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogEntrySmartLogSession

    def can_manage_smart_log(self):
        """Tests if this user can manage smart log.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.


        :return: ``false`` if smart log management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_log_entry_query(self, log_entry_query):
        """Applies a logEntry query to this log.

        :param log_entry_query: the logEntry query
        :type log_entry_query: ``osid.logging.LogEntryQuery``
        :raise: ``NullArgument`` -- ``log_entry_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``log_entry_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_log_entry_query(self):
        """Gets a logEntry query inspector for this log.

        :return: the logEntry query inspector
        :rtype: ``osid.logging.LogEntryQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_log_entry_sequencing(self, log_entry_search_order):
        """Applies a logEntry search order to this log.

        :param log_entry_search_order: the logEntry search order
        :type log_entry_search_order: ``osid.logging.LogEntrySearchOrder``
        :raise: ``NullArgument`` -- ``log_entry_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``log_entry_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def get_logs(self):
        """Gets all ``Logs``.
        In plenary mode, the returned list contains all known logs or an
        error results. Otherwise, the returned list may contain only
        those logs that are accessible through this session.


        :return: a list of ``Logs``
        :rtype: ``osid.logging.LogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    logs = property(fget=get_logs)


##
# The following methods are from osid.logging.LogQuerySession

    def can_search_logs(self):
        """Tests if this user can perform ``Log`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_log_query(self):
        """Gets a log query.

        :return: the log query
        :rtype: ``osid.logging.LogQuery``

        """
        raise UNIMPLEMENTED()

    log_query = property(fget=get_log_query)

    def get_logs_by_query(self, log_query):
        """Gets a list of ``Logs`` matching the given log query.

        :param log_query: the log query
        :type log_query: ``osid.logging.LogQuery``
        :return: the returned ``LogList``
        :rtype: ``osid.logging.LogList``
        :raise: ``NullArgument`` -- ``log_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogSearchSession

    def get_log_search(self):
        """Gets a log search.

        :return: the log search
        :rtype: ``osid.logging.LogSearch``

        """
        raise UNIMPLEMENTED()

    log_search = property(fget=get_log_search)

    def get_log_search_order(self):
        """Gets a log search order.
        The ``LogSearchOrder`` is supplied to a ``LogSearch`` to specify
        the ordering of results.


        :return: the log search order
        :rtype: ``osid.logging.LogSearchOrder``

        """
        raise UNIMPLEMENTED()

    log_search_order = property(fget=get_log_search_order)

    def get_logs_by_search(self, log_query, log_search):
        """Gets the search results matching the given search.

        :param log_query: the log query
        :type log_query: ``osid.logging.LogQuery``
        :param log_search: the log search
        :type log_search: ``osid.logging.LogSearch``
        :return: the log search results
        :rtype: ``osid.logging.LogSearchResults``
        :raise: ``NullArgument`` -- ``log_query`` or ``log_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``log_query`` or ``log_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_log_query_from_inspector(self, log_query_inspector):
        """Gets a log query from an inspector.
        The inspector is available from a ``LogSearchResults``.


        :param log_query_inspector: a log query inspector
        :type log_query_inspector: ``osid.logging.LogQueryInspector``
        :return: the log query
        :rtype: ``osid.logging.LogQuery``
        :raise: ``NullArgument`` -- ``log_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``log_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def can_update_logs(self):
        """Tests if this user can update ``Logs``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.


        :return: ``false`` if ``Log`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()

    def can_delete_logs(self):
        """Tests if this user can delete ``Logs``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Log``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.


        :return: ``false`` if ``Log`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_log(self, log_id):
        """Deletes a ``Log``.

        :param log_id: the ``Id`` of the ``Log`` to remove
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_log_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Logs``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Log`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogNotificationSession

    def can_register_for_log_notifications(self):
        """Tests if this user can register for ``Log`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_logs(self):
        """Register for notifications of new logs.
        ``LogReceiver.newLog()`` is invoked when a new ``Log`` is
        created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_ancestors(self, log_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified log.
        ``LogReceiver.newAncestorLog()`` is invoked when the specified
        log node gets a new ancestor.


        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_log_descendants(self, log_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified log.
        ``LogReceiver.newDescendantLog()`` is invoked when the specified
        log node gets a new descendant.


        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_logs(self):
        """Registers for notification of updated logs.
        ``LogReceiver.changedLog()`` is invoked when a log is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_log(self, log_id):
        """Registers for notification of an updated log.
        ``LogReceiver.changedLog()`` is invoked when the specified log
        is changed.


        :param log_id: the ``Id`` of the ``Log`` to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_logs(self):
        """Registers for notification of deleted logs.
        ``LogReceiver.deletedLog()`` is invoked when a log is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log(self, log_id):
        """Registers for notification of a deleted log.
        ``LogReceiver.deletedLog()`` is invoked when the specified log
        is deleted.


        :param log_id: the ``Id`` of the ``Log`` to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_ancestors(self, log_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified log.
        ``LogReceiver.deletedAncestor()`` is invoked when the specified
        log node loses an ancestor.


        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_log_descendants(self, log_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified log.
        ``LogReceiver.deletedDescendant()`` is invoked when the
        specified log node loses a descendant.


        :param log_id: the ``Id`` of the ``Log`` node to monitor
        :type log_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogHierarchySession

    def get_log_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    log_hierarchy_id = property(fget=get_log_hierarchy_id)

    def get_log_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    log_hierarchy = property(fget=get_log_hierarchy)

    def can_access_log_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_log_ids(self):
        """Gets the root log ``Ids`` in this hierarchy.

        :return: the root log ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_log_ids = property(fget=get_root_log_ids)

    def get_root_logs(self):
        """Gets the root logs in the log hierarchy.
        A node with no parents is an orphan. While all log ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.


        :return: the root logs
        :rtype: ``osid.logging.LogList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_logs = property(fget=get_root_logs)

    def has_parent_logs(self, log_id):
        """Tests if the ``Log`` has any parents.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the log has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a direct parent of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_log_ids(self, log_id):
        """Gets the parent ``Ids`` of the given log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the log
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_logs(self, log_id):
        """Gets the parent logs of the given ``id``.

        :param log_id: the ``Id`` of the ``Log`` to query
        :type log_id: ``osid.id.Id``
        :return: the parent logs of the ``id``
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- a ``Log`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_log(self, id_, log_id):
        """Tests if an ``Id`` is an ancestor of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is an ancestor of the ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_logs(self, log_id):
        """Tests if a log has any children.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``log_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a direct child of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a child of ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_log_ids(self, log_id):
        """Gets the child ``Ids`` of the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :return: the children of the depot
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_logs(self, log_id):
        """Gets the child logs of the given ``id``.

        :param log_id: the ``Id`` of the ``Log`` to query
        :type log_id: ``osid.id.Id``
        :return: the child logs of the ``id``
        :rtype: ``osid.logging.LogList``
        :raise: ``NotFound`` -- a ``Log`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_log(self, id_, log_id):
        """Tests if an ``Id`` is a descendant of a log.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``log_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_node_ids(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a log node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_log_nodes(self, log_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given log.

        :param log_id: the ``Id`` to query
        :type log_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a log node
        :rtype: ``osid.logging.LogNode``
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.logging.LogHierarchyDesignSession

    def can_modify_log_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.


        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_log(self, log_id):
        """Adds a root log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``log_id`` is not found
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_log(self, log_id):
        """Removes a root log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` is not a root
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_log(self, log_id, child_id):
        """Adds a child to a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``log_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``log_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``log_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_log(self, log_id, child_id):
        """Removes a child from a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``log_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_logs(self, log_id):
        """Removes all children from a log.

        :param log_id: the ``Id`` of a log
        :type log_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``log_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``log_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Log(osid_objects.OsidCatalog, osid_sessions.OsidSession):

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

        """
        raise UNIMPLEMENTED()



class LogList(osid_objects.OsidList):

    def get_next_log(self):
        """Gets the next ``Log`` in this list.

        :return: the next ``Log`` in this list. The ``has_next()`` method should be used to test that a next ``Log`` is available before calling this method.
        :rtype: ``osid.logging.Log``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

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

        """
        raise UNIMPLEMENTED()



class Logs(LoggingManager):
    pass


