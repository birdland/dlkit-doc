from ..osid import queries as osid_queries


class JournalEntryQuery(osid_queries.OsidObjectQuery, osid_queries.OsidSubjugateableQuery):
    """This is the query for searching journal entries.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_branch_id(self, branch_id, match):
        """Sets the branch ``Id`` for this query to match branches assigned to journals.

        :param branch_id: a branch ``Id``
        :type branch_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``

        """
        pass

    def clear_branch_id_terms(self):
        """Clears the branch ``Id`` terms."""
        pass

    branch_id_terms = property(fdel=clear_branch_id_terms)

    def supports_branch_query(self):
        """Tests if a branch query is available.

        :return: ``true`` if a branch query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_branch_query(self):
        """Gets the query for a branch.

        :return: the branch query
        :rtype: ``osid.journaling.BranchQuery``
        :raise: ``Unimplemented`` -- ``supports_branch_query()`` is ``false``

        """
        return # osid.journaling.BranchQuery

    branch_query = property(fget=get_branch_query)

    def clear_branch_terms(self):
        """Clears the branch terms."""
        pass

    branch_terms = property(fdel=clear_branch_terms)

    def match_source_id(self, source_id, match):
        """Sets the source ``Id``.

        :param source_id: a source ``Id``
        :type source_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``

        """
        pass

    def clear_source_id_terms(self):
        """Clears the source ``Id`` terms."""
        pass

    source_id_terms = property(fdel=clear_source_id_terms)

    def match_version_id(self, version_id, match):
        """Sets the version ``Id``.

        :param version_id: a version ``Id``
        :type version_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``version_id`` is ``null``

        """
        pass

    def clear_version_id_terms(self):
        """Clears the version ``Id`` terms."""
        pass

    version_id_terms = property(fdel=clear_version_id_terms)

    def match_timestamp(self, from_, to, match):
        """Matches entries falling between the given times inclusive.

        :param from: start time
        :type from: ``osid.calendaring.DateTime``
        :param to: end time
        :type to: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``

        """
        pass

    def clear_timestamp_terms(self):
        """Clears the timestamp terms."""
        pass

    timestamp_terms = property(fdel=clear_timestamp_terms)

    def match_entries_since(self, from_, match):
        """Matches entries following the given timestamp inclusive.

        :param from: start time
        :type from: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``from`` is ``null``

        """
        pass

    def clear_entries_since_terms(self):
        """Clears the entries since terms."""
        pass

    entries_since_terms = property(fdel=clear_entries_since_terms)

    def match_resource_id(self, resource_id, match):
        """Sets a resource ``Id``.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        pass

    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms."""
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_resource_query(self):
        """Gets the query for a resource query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    def clear_resource_terms(self):
        """Clears the resource terms."""
        pass

    resource_terms = property(fdel=clear_resource_terms)

    def match_agent_id(self, agent_id, match):
        """Sets an agent ``Id``.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        pass

    def clear_agent_id_terms(self):
        """Clears the agent ``Id`` terms."""
        pass

    agent_id_terms = property(fdel=clear_agent_id_terms)

    def supports_agent_query(self):
        """Tests if an ``AgentQuery`` is available.

        :return: ``true`` if an agent query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_agent_query(self):
        """Gets the query for an agent query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        """
        return # osid.authentication.AgentQuery

    agent_query = property(fget=get_agent_query)

    def clear_agent_terms(self):
        """Clears the agent terms."""
        pass

    agent_terms = property(fdel=clear_agent_terms)

    def match_journal_id(self, journal_id, match):
        """Sets the journal ``Id`` for this query to match entries assigned to journals.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``

        """
        pass

    def clear_journal_id_terms(self):
        """Clears the journal ``Id`` terms."""
        pass

    journal_id_terms = property(fdel=clear_journal_id_terms)

    def supports_journal_query(self):
        """Tests if a ``JournalQuery`` is available.

        :return: ``true`` if a journal query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_journal_query(self):
        """Gets the query for a journal query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the journal query
        :rtype: ``osid.journaling.JournalQuery``
        :raise: ``Unimplemented`` -- ``supports_journal_query()`` is ``false``

        """
        return # osid.journaling.JournalQuery

    journal_query = property(fget=get_journal_query)

    def clear_journal_terms(self):
        """Clears the journal terms."""
        pass

    journal_terms = property(fdel=clear_journal_terms)

    def get_journal_entry_query_record(self, journal_entry_record_type):
        """Gets the journal entry query record corresponding to the given ``JournalEntry`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param journal_entry_record_type: a journal entry record type
        :type journal_entry_record_type: ``osid.type.Type``
        :return: the journal entry query record
        :rtype: ``osid.journaling.records.JournalEntryQueryRecord``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_entry_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalEntryQueryRecord


class BranchQuery(osid_queries.OsidObjectQuery, osid_queries.OsidOperableQuery):
    """This is the query for searching branches Each method specifies an ``AND`` term while multiple invocations of the same method produce a nested ``OR``."""
    def match_origin_journal_entry_id(self, journal_entry_id, match):
        """Sets the origin journal entry ``Id`` for this query.

        :param journal_entry_id: a journal entry Id ``Id``
        :type journal_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``

        """
        pass

    def clear_origin_journal_entry_id_terms(self):
        """Clears the origin journal entry ``Id`` terms."""
        pass

    origin_journal_entry_id_terms = property(fdel=clear_origin_journal_entry_id_terms)

    def supports_origin_journal_entry_query(self):
        """Tests if a ``JournalEntryQuery`` is available.

        :return: ``true`` if a journal entry query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_origin_journal_entry_query(self):
        """Gets the query for an origin journal entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the origin journal entry query
        :rtype: ``osid.journaling.JournalEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_origin_journal_entry_query()`` is ``false``

        """
        return # osid.journaling.JournalEntryQuery

    origin_journal_entry_query = property(fget=get_origin_journal_entry_query)

    def clear_origin_journal_entry_terms(self):
        """Clears the origin journal entry terms."""
        pass

    origin_journal_entry_terms = property(fdel=clear_origin_journal_entry_terms)

    def match_latest_journal_entry_id(self, journal_entry_id, match):
        """Sets the latest journal entry ``Id`` for this query.

        :param journal_entry_id: a journal entry Id ``Id``
        :type journal_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``

        """
        pass

    def clear_latest_journal_entry_id_terms(self):
        """Clears the latest journal entry ``Id`` terms."""
        pass

    latest_journal_entry_id_terms = property(fdel=clear_latest_journal_entry_id_terms)

    def supports_latest_journal_entry_query(self):
        """Tests if a ``JournalEntryQuery`` is available.

        :return: ``true`` if a journal entry query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_latest_journal_entry_query(self):
        """Gets the query for a latest journal entry.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the latest journal entry query
        :rtype: ``osid.journaling.JournalEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_origin_journal_entry_query()`` is ``false``

        """
        return # osid.journaling.JournalEntryQuery

    latest_journal_entry_query = property(fget=get_latest_journal_entry_query)

    def clear_latest_journal_entry_terms(self):
        """Clears the latest journal entry terms."""
        pass

    latest_journal_entry_terms = property(fdel=clear_latest_journal_entry_terms)

    def get_branch_query_record(self, branch_record_type):
        """Gets the branch query record corresponding to the given ``Branch`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param branch_record_type: a branch record type
        :type branch_record_type: ``osid.type.Type``
        :return: the branch query record
        :rtype: ``osid.journaling.records.BranchQueryRecord``
        :raise: ``NullArgument`` -- ``branch_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(branch_record_type)`` is ``false``

        """
        return # osid.journaling.records.BranchQueryRecord


class JournalQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching for journals.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_journal_entry_id(self, journal_entry_id, match):
        """Sets the journal entry ``Id`` for this query to match entries assigned to journals.

        :param journal_entry_id: a journal entry ``Id``
        :type journal_entry_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``journal_entry_id`` is ``null``

        """
        pass

    def clear_journal_entry_id_terms(self):
        """Clears the journal entry ``Id`` terms."""
        pass

    journal_entry_id_terms = property(fdel=clear_journal_entry_id_terms)

    def supports_journal_entry_query(self):
        """Tests if a journal entry query is available.

        :return: ``true`` if a journal entry query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_journal_entry_query(self):
        """Gets the query for a journal.

        :return: the journal entry query
        :rtype: ``osid.journaling.JournalEntryQuery``
        :raise: ``Unimplemented`` -- ``supports_journal_entry_query()`` is ``false``

        """
        return # osid.journaling.JournalEntryQuery

    journal_entry_query = property(fget=get_journal_entry_query)

    def match_any_journal_entry(self, match):
        """Matches journals with any journal entry.

        :param match: ``true`` to match journals with any journal entry, ``false`` to match journals with no entries
        :type match: ``boolean``

        """
        pass

    def clear_journal_entry_terms(self):
        """Clears the journal entry terms."""
        pass

    journal_entry_terms = property(fdel=clear_journal_entry_terms)

    def match_branch_id(self, branch_id, match):
        """Sets the branch ``Id`` for this query to match branches assigned to journals.

        :param branch_id: a branch ``Id``
        :type branch_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``branch_id`` is ``null``

        """
        pass

    def clear_branch_id_terms(self):
        """Clears the branch ``Id`` terms."""
        pass

    branch_id_terms = property(fdel=clear_branch_id_terms)

    def supports_branch_query(self):
        """Tests if a branch query is available.

        :return: ``true`` if a branch query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_branch_query(self):
        """Gets the query for a branch.

        :return: the branch query
        :rtype: ``osid.journaling.BranchQuery``
        :raise: ``Unimplemented`` -- ``supports_branch_query()`` is ``false``

        """
        return # osid.journaling.BranchQuery

    branch_query = property(fget=get_branch_query)

    def match_any_branch(self, match):
        """Matches journals with any branches.

        :param match: ``true`` to match journals with any branch, ``false`` to match journals with no branches
        :type match: ``boolean``

        """
        pass

    def clear_branch_terms(self):
        """Clears the branch terms."""
        pass

    branch_terms = property(fdel=clear_branch_terms)

    def match_ancestor_journal_id(self, journal_id, match):
        """Sets the journal ``Id`` for this query to match journals that have the specified journal as an ancestor.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``

        """
        pass

    def clear_ancestor_journal_id_terms(self):
        """Clears the ancestor journal ``Id`` terms."""
        pass

    ancestor_journal_id_terms = property(fdel=clear_ancestor_journal_id_terms)

    def supports_ancestor_journal_query(self):
        """Tests if a ``JournalQuery`` is available.

        :return: ``true`` if a journal query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_journal_query(self):
        """Gets the query for a journal.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the journal query
        :rtype: ``osid.journaling.JournalQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_journal_query()`` is ``false``

        """
        return # osid.journaling.JournalQuery

    ancestor_journal_query = property(fget=get_ancestor_journal_query)

    def match_any_ancestor_journal(self, match):
        """Matches journals with any ancestor.

        :param match: ``true`` to match journals with any ancestor, ``false`` to match root journals
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_journal_terms(self):
        """Clears the ancestor journal terms."""
        pass

    ancestor_journal_terms = property(fdel=clear_ancestor_journal_terms)

    def match_descendant_journal_id(self, journal_id, match):
        """Sets the journal ``Id`` for this query to match journals that have the specified journal as a descendant.

        :param journal_id: a journal ``Id``
        :type journal_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``journal_id`` is ``null``

        """
        pass

    def clear_descendant_journal_id_terms(self):
        """Clears the descendant journal ``Id`` terms."""
        pass

    descendant_journal_id_terms = property(fdel=clear_descendant_journal_id_terms)

    def supports_descendant_journal_query(self):
        """Tests if a ``JournalQuery`` is available.

        :return: ``true`` if a journal query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_journal_query(self):
        """Gets the query for a journal.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the journal query
        :rtype: ``osid.journaling.JournalQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_journal_query()`` is ``false``

        """
        return # osid.journaling.JournalQuery

    descendant_journal_query = property(fget=get_descendant_journal_query)

    def match_any_descendant_journal(self, match):
        """Matches journals with any descendant.

        :param match: ``true`` to match journals with any descendant, ``false`` to match leaf journals
        :type match: ``boolean``

        """
        pass

    def clear_descendant_journal_terms(self):
        """Clears the descendant journal terms."""
        pass

    descendant_journal_terms = property(fdel=clear_descendant_journal_terms)

    def get_journal_query_record(self, journal_record_type):
        """Gets the journal query record corresponding to the given ``Journal`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param journal_record_type: a journal record type
        :type journal_record_type: ``osid.type.Type``
        :return: the journal query record
        :rtype: ``osid.journaling.records.JournalQueryRecord``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalQueryRecord


