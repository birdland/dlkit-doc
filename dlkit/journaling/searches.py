from ..osid import searches as osid_searches


class JournalEntrySearch(osid_searches.OsidSearch):
    """The search interface for governing journal entry searches."""
    def search_among_journal_entries(self, journal_entry_ids):
        """Execute this search among the given list of journal entries.

        :param journal_entry_ids: list of journal entries
        :type journal_entry_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``journal_entry_ids`` is ``null``

        """
        pass

    def order_journal_entry_results(self, journal_entry_search_order):
        """Specify an ordering to the search results.

        :param journal_entry_search_order: journal entry search order
        :type journal_entry_search_order: ``osid.journaling.JournalEntrySearchOrder``
        :raise: ``NullArgument`` -- ``journal_entry_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``journal_entry_search_order`` is not of this service

        """
        pass

    def get_journal_entry_search_record(self, journal_entry_search_record_type):
        """Gets the journal entry search record corresponding to the given journal entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param journal_entry_search_record_type: a journal entry search record type
        :type journal_entry_search_record_type: ``osid.type.Type``
        :return: the journal entry search record
        :rtype: ``osid.journaling.records.JournalEntrySearchRecord``
        :raise: ``NullArgument`` -- ``journal_entry_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_entry_search_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalEntrySearchRecord


class JournalEntrySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_journal_entries(self):
        """Gets the journal entry list resulting from a search.

        :return: the journal entry list
        :rtype: ``osid.journaling.JournalEntryList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.journaling.JournalEntryList

    journal_entries = property(fget=get_journal_entries)

    def get_journal_entry_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the journal entry query inspector
        :rtype: ``osid.journaling.JournalEntryQueryInspector``

        """
        return # osid.journaling.JournalEntryQueryInspector

    journal_entry_query_inspector = property(fget=get_journal_entry_query_inspector)

    def get_journal_entry_search_results_record(self, journal_entry_search_record_type):
        """Gets the journal entry search results record corresponding to the given journal entry search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param journal_entry_search_record_type: a journal entry search record type
        :type journal_entry_search_record_type: ``osid.type.Type``
        :return: the journal entry search results record
        :rtype: ``osid.journaling.records.JournalEntrySearchResultsRecord``
        :raise: ``NullArgument`` -- ``journal_entry_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_entry_search_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalEntrySearchResultsRecord


class BranchSearch(osid_searches.OsidSearch):
    """The search interface for governing branch searches."""
    def search_among_branches(self, branch_ids):
        """Execute this search among the given list of branches.

        :param branch_ids: list of branch ``Ids``
        :type branch_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``branch_ids`` is ``null``

        """
        pass

    def order_branch_results(self, branch_search_order):
        """Specify an ordering to the search results.

        :param branch_search_order: branch search order
        :type branch_search_order: ``osid.journaling.BranchSearchOrder``
        :raise: ``NullArgument`` -- ``order`` is ``null``
        :raise: ``Unsupported`` -- ``order`` is not of this service

        """
        pass

    def get_branch_search_record(self, branch_search_record_type):
        """Gets the branch search record corresponding to the given branch search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param branch_search_record_type: a branch search record type
        :type branch_search_record_type: ``osid.type.Type``
        :return: the branch search record
        :rtype: ``osid.journaling.records.BranchSearchRecord``
        :raise: ``NullArgument`` -- ``branch_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type_type(branch_search_record_type)`` is ``false``

        """
        return # osid.journaling.records.BranchSearchRecord


class BranchSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_branches(self):
        """Gets the branch list resulting from a search.

        :return: the branch list
        :rtype: ``osid.journaling.BranchList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.journaling.BranchList

    branches = property(fget=get_branches)

    def get_branch_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the branch query inspector
        :rtype: ``osid.journaling.BranchQueryInspector``

        """
        return # osid.journaling.BranchQueryInspector

    branch_query_inspector = property(fget=get_branch_query_inspector)

    def get_branch_search_results_record(self, branch_search_record_type):
        """Gets the branch search results record corresponding to the given branch search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param branch_search_record_type: a branch search record type
        :type branch_search_record_type: ``osid.type.Type``
        :return: the branch search results record
        :rtype: ``osid.journaling.records.BranchSearchResultsRecord``
        :raise: ``NullArgument`` -- ``branch_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type_type(branch_search_record_type)`` is ``false``

        """
        return # osid.journaling.records.BranchSearchResultsRecord


class JournalSearch(osid_searches.OsidSearch):
    """The search interface for governing journal searches."""
    def search_among_journals(self, journal_ids):
        """Execute this search among the given list of journals.

        :param journal_ids: list of journals
        :type journal_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``journal_ids`` is ``null``

        """
        pass

    def order_journal_results(self, journal_search_order):
        """Specify an ordering to the search results.

        :param journal_search_order: journal search order
        :type journal_search_order: ``osid.journaling.JournalSearchOrder``
        :raise: ``NullArgument`` -- ``journal_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``journal_search_order`` is not of this service

        """
        pass

    def get_journal_search_record(self, journal_search_record_type):
        """Gets the journal search record corresponding to the given journal search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param journal_search_record_type: a journal search record type
        :type journal_search_record_type: ``osid.type.Type``
        :return: the journal search record
        :rtype: ``osid.journaling.records.JournalSearchRecord``
        :raise: ``NullArgument`` -- ``journal_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_search_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalSearchRecord


class JournalSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_journals(self):
        """Gets the journal list resulting from a search.

        :return: the journal list
        :rtype: ``osid.journaling.JournalList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.journaling.JournalList

    journals = property(fget=get_journals)

    def get_journal_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the journal query inspector
        :rtype: ``osid.journaling.JournalQueryInspector``

        """
        return # osid.journaling.JournalQueryInspector

    journal_query_inspector = property(fget=get_journal_query_inspector)

    def get_journal_search_results_record(self, journal_search_record_type):
        """Gets the journal search results record corresponding to the given journal search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param journal_search_record_type: a journal search record type
        :type journal_search_record_type: ``osid.type.Type``
        :return: the journal search results record
        :rtype: ``osid.journaling.records.JournalSearchResultsRecord``
        :raise: ``NullArgument`` -- ``JournalSearchRecordType`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_search_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalSearchResultsRecord


