from ..osid import objects as osid_objects


class LogEntry(osid_objects.OsidObject):
    """A log entry consists of a time, an agent, and a priority type."""
    def get_priority(self):
        """Gets the priority level of this entry.

        :return: the priority level
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    priority = property(fget=get_priority)

    def get_timestamp(self):
        """Gets the time this entry was logged.

        :return: the time stamp of this entry
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    timestamp = property(fget=get_timestamp)

    def get_resource_id(self):
        """Gets the resource ``Id`` who created this entry.

        :return: the resource ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the ``Resource`` who created this entry.

        :return: the ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    resource = property(fget=get_resource)

    def get_agent_id(self):
        """Gets the agent ``Id`` who created this entry.

        :return: the agent ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    agent_id = property(fget=get_agent_id)

    def get_agent(self):
        """Gets the ``Agent`` who created this entry.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.authentication.Agent

    agent = property(fget=get_agent)

    def get_log_entry_record(self, log_entry_record_type):
        """Gets the log entry record corresponding to the given ``LogEntry`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``log_entry_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(log_entry_record_type)`` is ``true`` .

        :param log_entry_record_type: the type of log entry record to retrieve
        :type log_entry_record_type: ``osid.type.Type``
        :return: the log entry record
        :rtype: ``osid.logging.records.LogEntryRecord``
        :raise: ``NullArgument`` -- ``log_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_entry_record_type)`` is ``false``

        """
        return # osid.logging.records.LogEntryRecord


class LogEntryForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating log entries.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``LogEntryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_priority_metadata(self):
        """Gets the metadata for a priority type.

        :return: metadata for the priority
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    priority_metadata = property(fget=get_priority_metadata)

    def set_priority(self, priority):
        """Sets the priority.

        :param priority: the new priority
        :type priority: ``osid.type.Type``
        :raise: ``InvalidArgument`` -- ``priority`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``priority`` is ``null``

        """
        pass

    def clear_priority(self):
        """Removes the priority.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    priority = property(fset=set_priority, fdel=clear_priority)

    def get_timestamp_metadata(self):
        """Gets the metadata for a timestamp.

        :return: metadata for the timestamp
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    timestamp_metadata = property(fget=get_timestamp_metadata)

    def set_timestamp(self, timestamp):
        """Sets the timestamp.

        :param timestamp: the new timestamp
        :type timestamp: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``timestamp`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``timestamp`` is ``null``

        """
        pass

    timestamp = property(fset=set_timestamp)

    def get_agent_metadata(self):
        """Gets the metadata for the agent.

        :return: metadata for the agent
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    agent_metadata = property(fget=get_agent_metadata)

    def set_agent(self, agent_id):
        """Sets the agent.

        :param agent_id: the new agent
        :type agent_id: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``agent_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        pass

    agent = property(fset=set_agent)

    def get_log_entry_form_record(self, log_entry_record_type):
        """Gets the ``LogEntryFormRecord`` corresponding to the given log entry record ``Type``.

        :param log_entry_record_type: the log entry record type
        :type log_entry_record_type: ``osid.type.Type``
        :return: the log entry form record
        :rtype: ``osid.logging.records.LogEntryFormRecord``
        :raise: ``NullArgument`` -- ``log_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_entry_record_type)`` is ``false``

        """
        return # osid.logging.records.LogEntryFormRecord


class LogEntryList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LogList`` provides a means for accessing ``LogEntry`` elements sequentially either one at a time or many at a time.

    Examples: while (lel.hasNext()) { LogEntry entry =
    lel.getNextLogEntry(); }

    or
      while (lel.hasNext()) {
           LogEntry[] entries = lel.getNextLogEntries(lel.available());
      }
    


    """
    def get_next_log_entry(self):
        """Gets the next ``LogEntry`` in this list.

        :return: the next ``LogEntry`` in this list. The ``has_next()`` method should be used to test that a next ``LogEntry`` is available before calling this method.
        :rtype: ``osid.logging.LogEntry``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.logging.LogEntry

    next_log_entry = property(fget=get_next_log_entry)

    def get_next_log_entries(self, n):
        """Gets the next set of ``LogEntry elements`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``LogEntry`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``LogEntry`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.logging.LogEntry``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.logging.LogEntry


class Log(osid_objects.OsidCatalog):
    """A ``Log`` represents a collection of entries.

    Like all ``OsidObjects,`` a ``Log`` is identified by its Id and any
    persisted references should use the ``Id``.

    """
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
        return # osid.logging.records.LogRecord


class LogForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Logs``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the ``LogAdminSession``.
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """
    def get_log_form_record(self, log_record_type):
        """Gets the ``LogFormRecord`` corresponding to the given log record ``Type``.

        :param log_record_type: the log record type
        :type log_record_type: ``osid.type.Type``
        :return: the log form record
        :rtype: ``osid.logging.records.LogFormRecord``
        :raise: ``NullArgument`` -- ``log_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(log_record_type)`` is ``false``

        """
        return # osid.logging.records.LogFormRecord


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

        """
        return # osid.logging.Log


class LogNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``LogHierarchySession``.

    """
    def get_log(self):
        """Gets the ``Log`` at this node.

        :return: the log represented by this node
        :rtype: ``osid.logging.Log``

        """
        return # osid.logging.Log

    log = property(fget=get_log)

    def get_parent_log_nodes(self):
        """Gets the parents of this log.

        :return: the parents of this log
        :rtype: ``osid.logging.LogNodeList``

        """
        return # osid.logging.LogNodeList

    parent_log_nodes = property(fget=get_parent_log_nodes)

    def get_child_log_nodes(self):
        """Gets the children of this log.

        :return: the children of this log
        :rtype: ``osid.logging.LogNodeList``

        """
        return # osid.logging.LogNodeList

    child_log_nodes = property(fget=get_child_log_nodes)


class LogNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LogNodeList`` provides a means for accessing ``LogNode`` elements sequentially either one at a time or many at a time.

    Examples: while (lnl.hasNext()) { LogNode node =
    lnl.getNextLogNode(); }

    or
      while (lnl.hasNext()) {
           LogNode[] nodes = lnl.getNextLogNodes(lnl.available());
      }
    


    """
    def get_next_log_node(self):
        """Gets the next ``LogNode`` in this list.

        :return: the next ``LogNode`` in this list. The ``has_next()`` method should be used to test that a next ``LogNode`` is available before calling this method.
        :rtype: ``osid.logging.LogNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.logging.LogNode

    next_log_node = property(fget=get_next_log_node)

    def get_next_log_nodes(self, n):
        """Gets the next set of ``LogNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``LogNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``LogNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.logging.LogNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.logging.LogNode


