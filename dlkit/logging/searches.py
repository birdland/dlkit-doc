from ..osid import searches as osid_searches


class LogEntrySearch(osid_searches.OsidSearch):
    """The search interface for governing log entry searches."""
    def search_among_log_entries(self, log_entry_ids):
        """Execute this search among the given list of log entries.

        :param log_entry_ids: list of log entries
        :type log_entry_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_entry_ids`` is ``null``

        """
        pass

    def order_log_entry_results(self, log_entry_search_order):
        """Specify an ordering to the search results.

        :param log_entry_search_order: log entry search order
        :type log_entry_search_order: ``osid.logging.LogEntrySearchOrder``
        :raise: ``NullArgument`` -- ``log_entry_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``log_entry_search_order`` is not of this service

        """
        pass

    def get_log_entry_search_record(self, log_entry_search_record_type):
        """Gets the log search record corresponding to the given log entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param log_entry_search_record_type: a log entry search record type
        :type log_entry_search_record_type: ``osid.type.Type``
        :return: the log entry search record
        :rtype: ``osid.logging.records.LogEntrySearchRecord``
        :raise: ``NullArgument`` -- ``log_entry_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_entry_search_record_type)`` is ``false``

        """
        return # osid.logging.records.LogEntrySearchRecord


class LogEntrySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_log_entries(self):
        """Gets the log entry list resulting from a search.

        :return: the log entry list
        :rtype: ``osid.logging.LogEntryList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.logging.LogEntryList

    log_entries = property(fget=get_log_entries)

    def get_log_entry_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the log entry query inspector
        :rtype: ``osid.logging.LogEntryQueryInspector``

        """
        return # osid.logging.LogEntryQueryInspector

    log_entry_query_inspector = property(fget=get_log_entry_query_inspector)

    def get_log_entry_search_results_record(self, log_entry_search_record_type):
        """Gets the log entry search results record corresponding to the given log entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param log_entry_search_record_type: a log entry search record type
        :type log_entry_search_record_type: ``osid.type.Type``
        :return: the log entry search results record
        :rtype: ``osid.logging.records.LogEntrySearchResultsRecord``
        :raise: ``NullArgument`` -- ``log_entry_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_entry_search_record_type)`` is ``false``

        """
        return # osid.logging.records.LogEntrySearchResultsRecord


class LogSearch(osid_searches.OsidSearch):
    """The search interface for governing log searches."""
    def search_among_logs(self, log_ids):
        """Execute this search among the given list of logs.

        :param log_ids: list of logs
        :type log_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``log_ids`` is ``null``

        """
        pass

    def order_log_results(self, log_search_order):
        """Specify an ordering to the search results.

        :param log_search_order: log search order
        :type log_search_order: ``osid.logging.LogSearchOrder``
        :raise: ``NullArgument`` -- ``log_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``log_search_order`` is not of this service

        """
        pass

    def get_log_search_record(self, log_search_record_type):
        """Gets the log search record corresponding to the given log search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param log_search_record_type: a log search record type
        :type log_search_record_type: ``osid.type.Type``
        :return: the log search record
        :rtype: ``osid.logging.records.LogSearchRecord``
        :raise: ``NullArgument`` -- ``log_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_search_record_type)`` is ``false``

        """
        return # osid.logging.records.LogSearchRecord


class LogSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_logs(self):
        """Gets the log list resulting from a search.

        :return: the log list
        :rtype: ``osid.logging.LogList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.logging.LogList

    logs = property(fget=get_logs)

    def get_log_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the log query inspector
        :rtype: ``osid.logging.LogQueryInspector``

        """
        return # osid.logging.LogQueryInspector

    log_query_inspector = property(fget=get_log_query_inspector)

    def get_log_search_results_record(self, log_search_record_type):
        """Gets the log search results record corresponding to the given log search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param log_search_record_type: a log search record type
        :type log_search_record_type: ``osid.type.Type``
        :return: the log search results record
        :rtype: ``osid.logging.records.LogSearchResultsRecord``
        :raise: ``NullArgument`` -- ``log_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_search_record_type)`` is ``false``

        """
        return # osid.logging.records.LogSearchResultsRecord


