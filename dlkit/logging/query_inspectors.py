from ..osid import query_inspectors as osid_query_inspectors


class LogEntryQueryInspector(osid_query_inspectors.OsidObjectQueryInspector):
    """This is the query inspector for examining log entry queries."""
    def get_priority_terms(self):
        """Gets the prirority query terms.

        :return: the priority terms
        :rtype: ``osid.search.terms.TypeTerm``

        """
        return # osid.search.terms.TypeTerm

    priority_terms = property(fget=get_priority_terms)

    def get_minimum_priority_terms(self):
        """Gets the minimum prirority query terms.

        :return: the minimum priority terms
        :rtype: ``osid.search.terms.TypeTerm``

        """
        return # osid.search.terms.TypeTerm

    minimum_priority_terms = property(fget=get_minimum_priority_terms)

    def get_timestamp_terms(self):
        """Gets the timestamp query terms.

        :return: the timestamp terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``

        """
        return # osid.search.terms.DateTimeRangeTerm

    timestamp_terms = property(fget=get_timestamp_terms)

    def get_resource_id_terms(self):
        """Gets the resource ``Id`` query terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    def get_resource_terms(self):
        """Gets the resource query terms.

        :return: the resource terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    def get_agent_id_terms(self):
        """Gets the agent ``Id`` query terms.

        :return: the agent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    agent_id_terms = property(fget=get_agent_id_terms)

    def get_agent_terms(self):
        """Gets the agent query terms.

        :return: the agent terms
        :rtype: ``osid.authentication.AgentQueryInspector``

        """
        return # osid.authentication.AgentQueryInspector

    agent_terms = property(fget=get_agent_terms)

    def get_log_id_terms(self):
        """Gets the log ``Id`` query terms.

        :return: the log ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    log_id_terms = property(fget=get_log_id_terms)

    def get_log_terms(self):
        """Gets the log query terms.

        :return: the log terms
        :rtype: ``osid.logging.LogQueryInspector``

        """
        return # osid.logging.LogQueryInspector

    log_terms = property(fget=get_log_terms)

    def get_log_entry_query_inspector_record(self, log_entry_record_type):
        """Gets the log entry query inspector corresponding to the given ``LogEntry`` record ``Type``.

        :param log_entry_record_type: a log entry record type
        :type log_entry_record_type: ``osid.type.Type``
        :return: the log entry query record
        :rtype: ``osid.logging.records.LogEntryQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``log_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_entry_record_type)`` is ``false``

        """
        return # osid.logging.records.LogEntryQueryInspectorRecord


class LogQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining log queries."""
    def get_log_entry_id_terms(self):
        """Gets the log entry ``Id`` query terms.

        :return: the log entry ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    log_entry_id_terms = property(fget=get_log_entry_id_terms)

    def get_log_entry_terms(self):
        """Gets the log entry query terms.

        :return: the log entry terms
        :rtype: ``osid.logging.LogEntryQueryInspector``

        """
        return # osid.logging.LogEntryQueryInspector

    log_entry_terms = property(fget=get_log_entry_terms)

    def get_ancestor_log_id_terms(self):
        """Gets the ancestor ``Id`` query terms.

        :return: the ancestor ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_log_id_terms = property(fget=get_ancestor_log_id_terms)

    def get_ancestor_log_terms(self):
        """Gets the ancestor query terms.

        :return: the ancestor terms
        :rtype: ``osid.logging.LogQueryInspector``

        """
        return # osid.logging.LogQueryInspector

    ancestor_log_terms = property(fget=get_ancestor_log_terms)

    def get_descendant_log_id_terms(self):
        """Gets the descendant log ``Id`` query terms.

        :return: the descendant log ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_log_id_terms = property(fget=get_descendant_log_id_terms)

    def get_descendant_log_terms(self):
        """Gets the descendant log query terms.

        :return: the descendant log terms
        :rtype: ``osid.logging.LogQueryInspector``

        """
        return # osid.logging.LogQueryInspector

    descendant_log_terms = property(fget=get_descendant_log_terms)

    def get_log_query_inspector_record(self, log_record_type):
        """Gets the log query inspector record corresponding to the given ``Log`` record ``Type``.

        :param log_record_type: a log record type
        :type log_record_type: ``osid.type.Type``
        :return: the log query inspector record
        :rtype: ``osid.logging.records.LogQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_record_type)`` is ``false``

        """
        return # osid.logging.records.LogQueryInspectorRecord


