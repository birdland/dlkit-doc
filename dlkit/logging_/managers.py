
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class LoggingProfile(osid_managers.OsidProfile):
    """The logging profile describes the interoperability among logging services."""

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


