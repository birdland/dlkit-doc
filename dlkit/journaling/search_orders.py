from ..osid import search_orders as osid_search_orders


class JournalEntrySearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidSubjugateableSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_branch(self, style):
        """Specifies a preference for ordering the result set by the branch.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_branch_search_order(self):
        """Tests if a branch search order is available.

        :return: ``true`` if a branch order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_branch_search_order(self):
        """Gets the branch search order.

        :return: the branch search order
        :rtype: ``osid.journaling.BranchSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_branch_search_order()`` is ``false``

        """
        return # osid.journaling.BranchSearchOrder

    branch_search_order = property(fget=get_branch_search_order)

    def order_by_source(self, style):
        """Specifies a preference for ordering the result set by the source.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_timestamp(self, style):
        """Specifies a preference for ordering the result set by the timestamp.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_resource(self, style):
        """Specifies a preference for ordering the result set by the resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_resource_search_order(self):
        """Tests if a resource order is available.

        :return: ``true`` if a resource order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_resource_search_order(self):
        """Gets the resource order.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_resource_search_order()`` is ``false``

        """
        return # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    def order_by_agent(self, style):
        """Specifies a preference for ordering the result set by the agent.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_agent_search_order(self):
        """Tests if an agent order is available.

        :return: ``true`` if an agent order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_agent_search_order(self):
        """Gets the agent order.

        :return: the agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_agent_search_order()`` is ``false``

        """
        return # osid.authentication.AgentSearchOrder

    agent_search_order = property(fget=get_agent_search_order)

    def get_journal_entry_search_order_record(self, journal_entry_record_type):
        """Gets the journal entry search order record corresponding to the given journal entry record ``Type``.

        Multiple retrievals return the same underlying object.

        :param journal_entry_record_type: a journal entry record type
        :type journal_entry_record_type: ``osid.type.Type``
        :return: the journal entry search order record
        :rtype: ``osid.journaling.records.JournalEntrySearchOrderRecord``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_entry_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalEntrySearchOrderRecord


class BranchSearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidOperableSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_origin_journal_entry(self, style):
        """Specified a preference for ordering results by the origin journal entry.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_origin_journal_entry_search_order(self):
        """Tests if a ``JournalEntrySearchOrder`` is available.

        :return: ``true`` if a journal entry search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_origin_journal_entry_search_order(self):
        """Gets the search order for the origin journal entry.

        :return: the journal entry search order
        :rtype: ``osid.journaling.JournalEntrySearchOrder``
        :raise: ``Unimplemented`` -- ``supports_origin_journal_entry_search_order()`` is ``false``

        """
        return # osid.journaling.JournalEntrySearchOrder

    origin_journal_entry_search_order = property(fget=get_origin_journal_entry_search_order)

    def order_by_latest_journal_entry(self, style):
        """Specified a preference for ordering results by the latest journal entry.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_latest_journal_entry_search_order(self):
        """Tests if a ``JournalEntrySearchOrder`` is available.

        :return: ``true`` if a journal entry search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_latest_journal_entry_search_order(self):
        """Gets the search order for the latest journal entry.

        :return: the journal entry search order
        :rtype: ``osid.journaling.JournalEntrySearchOrder``
        :raise: ``Unimplemented`` -- ``supports_latest_journal_entry_search_order()`` is ``false``

        """
        return # osid.journaling.JournalEntrySearchOrder

    latest_journal_entry_search_order = property(fget=get_latest_journal_entry_search_order)

    def get_branch_search_order_record(self, branch_record_type):
        """Gets the branch search order record corresponding to the given branch record ``Type``.

        Multiple retrievals return the same underlying object.

        :param branch_record_type: a branch record type
        :type branch_record_type: ``osid.type.Type``
        :return: the branch search order record
        :rtype: ``osid.journaling.records.BranchSearchOrderRecord``
        :raise: ``NullArgument`` -- ``branch_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(branch_record_type)`` is ``false``

        """
        return # osid.journaling.records.BranchSearchOrderRecord


class JournalSearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_journal_search_order_record(self, journal_record_type):
        """Gets the journal search order record corresponding to the given journal record Type.

        Multiple retrievals return the same underlying object.

        :param journal_record_type: a journal record type
        :type journal_record_type: ``osid.type.Type``
        :return: the journal search order record
        :rtype: ``osid.journaling.records.JournalSearchOrderRecord``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalSearchOrderRecord


