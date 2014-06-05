from ..osid import objects as osid_objects
from ..osid import markers as osid_markers


class JournalEntry(osid_objects.OsidObject, osid_markers.Subjugateable):
    """A ``JournalEntry`` represents an entry in a journal."""
    def get_branch_id(self):
        """Gets the branch ``Id`` for this entry.

        :return: the branch ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    branch_id = property(fget=get_branch_id)

    def get_branch(self):
        """Gets the branch for this entry.

        :return: the branch
        :rtype: ``osid.journaling.Branch``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.Branch

    branch = property(fget=get_branch)

    def get_source_id(self):
        """Gets the principal ``Id`` of the journaled object.

        :return: the source ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    source_id = property(fget=get_source_id)

    def get_version_id(self):
        """Gets the version ``Id`` of the journaled object.

        :return: the version ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    version_id = property(fget=get_version_id)

    def get_timestamp(self):
        """Gets the ``timestamp`` of this journal entry.

        :return: the time of this entry
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    timestamp = property(fget=get_timestamp)

    def get_resource_id(self):
        """Gets the Id of the resource who created this entry.

        :return: the ``Resource``  ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the resource who created this entry.

        :return: the ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    resource = property(fget=get_resource)

    def get_agent_id(self):
        """Gets the Id of the agent who created this entry.

        :return: the ``Agent``  ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    agent_id = property(fget=get_agent_id)

    def get_agent(self):
        """Gets the agent who created this entry.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.authentication.Agent

    agent = property(fget=get_agent)

    def get_journal_entry_record(self, journal_entry_record_type):
        """Gets the journal entry record corresponding to the given ``JournalEntry`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``journal_entry_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(journal_entry_record_type)`` is ``true`` .

        :param journal_entry_record_type: the type of journal entry record to retrieve
        :type journal_entry_record_type: ``osid.type.Type``
        :return: the journal entry record
        :rtype: ``osid.journaling.records.JournalEntryRecord``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_entry_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalEntryRecord


class JournalEntryForm(osid_objects.OsidObjectForm, osid_objects.OsidSubjugateableForm):
    """This is the form for creating and updating ``JournalEntry`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``JournalEntryAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_journal_entry_form_record(self, journal_entry_record_type):
        """Gets the ``JournalEntryFormRecord`` corresponding to the given journal entry record ``Type``.

        :param journal_entry_record_type: the journal entry record type
        :type journal_entry_record_type: ``osid.type.Type``
        :return: the journal entry form record
        :rtype: ``osid.journaling.records.JournalEntryFormRecord``
        :raise: ``NullArgument`` -- ``journal_entry_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_entry_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalEntryFormRecord


class JournalEntryList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``JournalEntryList`` provides a means for accessing ``JournalEntry`` elements sequentially either one at a time or many at a time.

    Examples: while (jel.hasNext()) { JournalEntry entry =
    jel.getNextJournalEntry(); }

    or
      while (jel.hasNext()) {
           JournalEntry[] entries = jel.getNextJournalEntries(jel.available());
      }
    


    """
    def get_next_journal_entry(self):
        """Gets the next ``JournalEntry`` in this list.

        :return: the next ``JournalEntry`` in this list. The ``has_next()`` method should be used to test that a next ``JournalEntry`` is available before calling this method.
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.JournalEntry

    next_journal_entry = property(fget=get_next_journal_entry)

    def get_next_journal_entries(self, n):
        """Gets the next set of ``JournalEntry`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``JournalEntry`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``JournalEntry`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.JournalEntry


class Branch(osid_objects.OsidObject, osid_markers.Operable):
    """A ``Branch`` is a new version chain from an existing version chain."""
    def get_origin_journal_entry_id(self):
        """Gets the journal entry ``Id`` from which this branch was started.

        :return: the journal entry ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    origin_journal_entry_id = property(fget=get_origin_journal_entry_id)

    def get_origin_journal_entry(self):
        """Gets the journal entry from which this branch was started.

        :return: the journal entry
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.JournalEntry

    origin_journal_entry = property(fget=get_origin_journal_entry)

    def get_latest_journal_entry_id(self):
        """Gets the latest journal entry ``Id`` in this branch.

        :return: the journal entry ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    latest_journal_entry_id = property(fget=get_latest_journal_entry_id)

    def get_latest_journal_entry(self):
        """Gets the latest journal entry in this branch.

        :return: the journal entry
        :rtype: ``osid.journaling.JournalEntry``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.JournalEntry

    latest_journal_entry = property(fget=get_latest_journal_entry)

    def get_branch_record(self, branch_record_type):
        """Gets the branch record corresponding to the given ``Pollstem`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``branch_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(branch_record_type)``
        is ``true`` .

        :param branch_record_type: the branch record type
        :type branch_record_type: ``osid.type.Type``
        :return: the branch record
        :rtype: ``osid.journaling.records.BranchRecord``
        :raise: ``NullArgument`` -- ``branch_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(branch_record_type)`` is ``false``

        """
        return # osid.journaling.records.BranchRecord


class BranchForm(osid_objects.OsidObjectForm, osid_objects.OsidOperableForm):
    """This is the form for creating and updating branchesLike all ``OsidForm`` objects, various data elements may be set here for use in the create and update methods in the ``BranchAdminSession``.

    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """
    def get_branch_form_record(self, branch_record_type):
        """Gets the ``BranchFormRecord`` corresponding to the given branch record ``Type``.

        :param branch_record_type: the branch record type
        :type branch_record_type: ``osid.type.Type``
        :return: the branch form record
        :rtype: ``osid.journaling.records.BranchFormRecord``
        :raise: ``NullArgument`` -- ``branch_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(branch_record_type)`` is ``false``

        """
        return # osid.journaling.records.BranchFormRecord


class BranchList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BranchList`` provides a means for accessing ``Branch`` elements sequentially either one at a time or many at a time.

    Examples: while (bl.hasNext()) { Branch branch = bl.getNextBranch();
    }

    or
      while (rl.hasNext()) {
           Branch[] branches = bl.getNextBranches(bl.available());
      }
    


    """
    def get_next_branch(self):
        """Gets the next ``Branch`` in this list.

        :return: the next ``Branch`` in this list. The ``has_next()`` method should be used to test that a next ``Branch`` is available before calling this method.
        :rtype: ``osid.journaling.Branch``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.Branch

    next_branch = property(fget=get_next_branch)

    def get_next_branches(self, n):
        """Gets the next set of ``Branches`` in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Branch`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Branch`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.journaling.Branch``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.Branch


class Journal(osid_objects.OsidCatalog):
    """A ``Journal`` represents a collection of entries.

    Like all OSID objects, a ``Journal`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    def get_journal_record(self, journal_record_type):
        """Gets the journal record corresponding to the given ``Journal`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``journal_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(journal_record_type)`` is ``true`` .

        :param journal_record_type: the type of journal record to retrieve
        :type journal_record_type: ``osid.type.Type``
        :return: the journal record
        :rtype: ``osid.journaling.records.JournalRecord``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalRecord


class JournalForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Journals``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``JournalAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_journal_form_record(self, journal_record_type):
        """Gets the ``JournalFormRecord`` corresponding to the given journal record ``Type``.

        :param journal_record_type: the journal record type
        :type journal_record_type: ``osid.type.Type``
        :return: the journal form record
        :rtype: ``osid.journaling.records.JournalFormRecord``
        :raise: ``NullArgument`` -- ``journal_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(journal_record_type)`` is ``false``

        """
        return # osid.journaling.records.JournalFormRecord


class JournalList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``JournalList`` provides a means for accessing ``Journal`` elements sequentially either one at a time or many at a time.

    Examples: while (jl.hasNext()) { Journal journal =
    jl.getNextJournal(); }

    or
      while (jl.hasNext()) {
           Journal[] journal = jl.getNextJournals(jl.available());
      }
    


    """
    def get_next_journal(self):
        """Gets the next ``Journal`` in this list.

        :return: the next ``Journal`` in this list. The ``has_next()`` method should be used to test that a next ``Journal`` is available before calling this method.
        :rtype: ``osid.journaling.Journal``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.Journal

    next_journal = property(fget=get_next_journal)

    def get_next_journals(self, n):
        """Gets the next set of ``Journal`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Journal`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Journal`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.journaling.Journal``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.Journal


class JournalNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``JournalHierarchySession``.

    """
    def get_journal(self):
        """Gets the ``Journal`` at this node.

        :return: the journal represented by this node
        :rtype: ``osid.journaling.Journal``

        """
        return # osid.journaling.Journal

    journal = property(fget=get_journal)

    def get_parent_journal_nodes(self):
        """Gets the parents of this journal.

        :return: the parents of this journal
        :rtype: ``osid.journaling.JournalNodeList``

        """
        return # osid.journaling.JournalNodeList

    parent_journal_nodes = property(fget=get_parent_journal_nodes)

    def get_child_journal_nodes(self):
        """Gets the children of this journal.

        :return: the children of this journal
        :rtype: ``osid.journaling.JournalNodeList``

        """
        return # osid.journaling.JournalNodeList

    child_journal_nodes = property(fget=get_child_journal_nodes)


class JournalNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``JournalNodeList`` provides a means for accessing ``JournalNode`` elements sequentially either one at a time or many at a time.

    Examples: while (jnl.hasNext()) { JournalNode node =
    jnl.getNextJournalNode(); }

    or
      while (jnl.hasNext()) {
           JournalNode[] nodes = jnl.getNextJournalNodes(jnl.available());
      }
    


    """
    def get_next_journal_node(self):
        """Gets the next ``JournalNode`` in this list.

        :return: the next ``JournalNode`` in this list. The ``has_next()`` method should be used to test that a next ``JournalNode`` is available before calling this method.
        :rtype: ``osid.journaling.JournalNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.JournalNode

    next_journal_node = property(fget=get_next_journal_node)

    def get_next_journal_nodes(self, n):
        """Gets the next set of ``JournalNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``JournalNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``JournalNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.journaling.JournalNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.journaling.JournalNode


