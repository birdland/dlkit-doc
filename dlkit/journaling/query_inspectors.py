from ..osid import query_inspectors as osid_query_inspectors


class JournalEntryQueryInspector(osid_query_inspectors.OsidObjectQueryInspector, osid_query_inspectors.OsidSubjugateableQueryInspector):
    """This is the query inspector for examining journal entry queries."""
    def get_branch_id_terms(self):
        """Gets the branch ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    branch_id_terms = property(fget=get_branch_id_terms)

    def get_branch_terms(self):
        """Gets the branch query terms.

        :return: the query terms
        :rtype: ``osid.journaling.BranchQueryInspector``

        """
        return # osid.journaling.BranchQueryInspector

    branch_terms = property(fget=get_branch_terms)

    def get_source_id_terms(self):
        """Gets the source ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    source_id_terms = property(fget=get_source_id_terms)

    def get_version_id_terms(self):
        """Gets the version ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    version_id_terms = property(fget=get_version_id_terms)

    def get_timestamp_terms(self):
        """Gets the timestamp query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``

        """
        return # osid.search.terms.DateTimeRangeTerm

    timestamp_terms = property(fget=get_timestamp_terms)

    def get_entries_since_terms(self):
        """Gets the entries since query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeTerm``

        """
        return # osid.search.terms.DateTimeTerm

    entries_since_terms = property(fget=get_entries_since_terms)

    def get_resource_id_terms(self):
        """Gets the resource ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    def get_resource_terms(self):
        """Gets the resource query terms.

        :return: the query terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    def get_agent_id_terms(self):
        """Gets the agent ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    agent_id_terms = property(fget=get_agent_id_terms)

    def get_agent_terms(self):
        """Gets the agent query terms.

        :return: the query terms
        :rtype: ``osid.authentication.AgentQueryInspector``

        """
        return # osid.authentication.AgentQueryInspector

    agent_terms = property(fget=get_agent_terms)

    def get_journal_id_terms(self):
        """Gets the journal ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    journal_id_terms = property(fget=get_journal_id_terms)

    def get_journal_terms(self):
        """Gets the journal query terms.

        :return: the query terms
        :rtype: ``osid.journaling.JournalQueryInspector``

        """
        return # osid.journaling.JournalQueryInspector

    journal_terms = property(fget=get_journal_terms)

    def get_journal_entry_query_inspector_record(self, journal_entry_record_type):
        """Gets the journal entry query inspector record corresponding to the given ``JournalEntry`` record ``Type``.

        :param journal_entry_record_type: a journal entry record type
        :type journal_entry_record_type: ``osid.type.Type``
        :return: the journal entry query inspector record
        :rtype: ``osid.journaling.records.JournalEntryQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_entry_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalEntryQueryInspectorRecord


class BranchQueryInspector(osid_query_inspectors.OsidObjectQueryInspector, osid_query_inspectors.OsidOperableQueryInspector):
    """This is the query inspector for examining branch queries."""
    def get_origin_journal_entry_id_terms(self):
        """Gets the origin journal entry ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    origin_journal_entry_id_terms = property(fget=get_origin_journal_entry_id_terms)

    def get_origin_journal_entry_terms(self):
        """Gets the origin journal entry query terms.

        :return: the query terms
        :rtype: ``osid.journaling.JournalEntryQueryInspector``

        """
        return # osid.journaling.JournalEntryQueryInspector

    origin_journal_entry_terms = property(fget=get_origin_journal_entry_terms)

    def get_latest_journal_entry_id_terms(self):
        """Gets the latest journal entry ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    latest_journal_entry_id_terms = property(fget=get_latest_journal_entry_id_terms)

    def get_latest_journal_entry_terms(self):
        """Gets the latest journal entry query terms.

        :return: the query terms
        :rtype: ``osid.journaling.JournalEntryQueryInspector``

        """
        return # osid.journaling.JournalEntryQueryInspector

    latest_journal_entry_terms = property(fget=get_latest_journal_entry_terms)

    def get_branch_query_inspector_record(self, branch_record_type):
        """Gets the branch query inspector record corresponding to the given ``Branch`` record ``Type``.

        :param branch_record_type: a branch record type
        :type branch_record_type: ``osid.type.Type``
        :return: the branch query inspector record
        :rtype: ``osid.journaling.records.BranchQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``branch_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(branch_record_type)`` is ``false``

        """
        return # osid.journaling.records.BranchQueryInspectorRecord


class JournalQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining journal searches."""
    def get_journal_entry_id_terms(self):
        """Gets the journal entry ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    journal_entry_id_terms = property(fget=get_journal_entry_id_terms)

    def get_journal_entry_terms(self):
        """Gets the journal entry query terms.

        :return: the query terms
        :rtype: ``osid.journaling.JournalEntryQueryInspector``

        """
        return # osid.journaling.JournalEntryQueryInspector

    journal_entry_terms = property(fget=get_journal_entry_terms)

    def get_branch_id_terms(self):
        """Gets the branch ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    branch_id_terms = property(fget=get_branch_id_terms)

    def get_branch_terms(self):
        """Gets the branch query terms.

        :return: the query terms
        :rtype: ``osid.journaling.BranchQueryInspector``

        """
        return # osid.journaling.BranchQueryInspector

    branch_terms = property(fget=get_branch_terms)

    def get_ancestor_journal_id_terms(self):
        """Gets the ancestor journal ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_journal_id_terms = property(fget=get_ancestor_journal_id_terms)

    def get_ancestor_journal_terms(self):
        """Gets the ancestor journal query terms.

        :return: the query terms
        :rtype: ``osid.journaling.JournalQueryInspector``

        """
        return # osid.journaling.JournalQueryInspector

    ancestor_journal_terms = property(fget=get_ancestor_journal_terms)

    def get_descendant_journal_id_terms(self):
        """Gets the descendant journal ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_journal_id_terms = property(fget=get_descendant_journal_id_terms)

    def get_descendant_journal_terms(self):
        """Gets the descendant journal query terms.

        :return: the query terms
        :rtype: ``osid.journaling.JournalQueryInspector``

        """
        return # osid.journaling.JournalQueryInspector

    descendant_journal_terms = property(fget=get_descendant_journal_terms)

    def get_journal_query_inspector_record(self, journal_record_type):
        """Gets the journal query inspector record corresponding to the given ``Journal`` record ``Type``.

        :param journal_record_type: a journal record type
        :type journal_record_type: ``osid.type.Type``
        :return: the journal query inspector record
        :rtype: ``osid.journaling.records.JournalQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalQueryInspectorRecord


