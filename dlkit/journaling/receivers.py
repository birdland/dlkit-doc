from ..osid import receivers as osid_receivers


class JournalEntryReceiver(osid_receivers.OsidReceiver):
    """The journal entry receiver is the consumer supplied interface for receiving notifications pertaining to new or deleted journal entries."""
    def new_journal_entry(self, journal_entry_id):
        """The callback for notifications of new journal entries.

        :param journal_entry_id: the ``Id`` of the new journal entry
        :type journal_entry_id: ``osid.id.Id``

        """
        pass

    def changed_journal_entry(self, journal_entry_id):
        """The callback for notifications of updated journal entries.

        :param journal_entry_id: the ``Id`` of the updated journal entry
        :type journal_entry_id: ``osid.id.Id``

        """
        pass

    def deleted_journal_entry(self, journal_entry_id):
        """the callback for notification of deleted journal entries.

        :param journal_entry_id: the ``Id`` of the deleted journal entry
        :type journal_entry_id: ``osid.id.Id``

        """
        pass


class BranchReceiver(osid_receivers.OsidReceiver):
    """The branch receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Branch`` objects."""
    def new_branch(self, branch_id):
        """The callback for notifications of new branches.

        :param branch_id: the ``Id`` of the new ``Branch``
        :type branch_id: ``osid.id.Id``

        """
        pass

    def changed_branch(self, branch_id):
        """The callback for notification of updated branches.

        :param branch_id: the ``Id`` of the updated ``Branch``
        :type branch_id: ``osid.id.Id``

        """
        pass

    def deleted_branch(self, branch_id):
        """the callback for notification of deleted branches.

        :param branch_id: the ``Id`` of the deleted ``Branch``
        :type branch_id: ``osid.id.Id``

        """
        pass


class JournalReceiver(osid_receivers.OsidReceiver):
    """The journal receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Journal`` objects."""
    def new_journal(self, journal_id):
        """The callback for notifications of new journals.

        :param journal_id: the ``Id`` of the new ``Journal``
        :type journal_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_journal(self, journal_id, ancestor_id):
        """The callback for notifications of new ancestors of a journal.

        :param journal_id: the ``Id`` of the registered ``Journal``
        :type journal_id: ``osid.id.Id``
        :param ancestor_id: the Id of the new ancestor journal
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_journal(self, journal_id, descendant_id):
        """The callback for notifications of new descendant of a journal.

        :param journal_id: the ``Id`` of the registered ``Journal``
        :type journal_id: ``osid.id.Id``
        :param descendant_id: the Id of the new descendant journal
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_journal(self, journal_id):
        """The callback for notification of updated journals.

        :param journal_id: the ``Id`` of the updated ``Journal``
        :type journal_id: ``osid.id.Id``

        """
        pass

    def deleted_journal(self, journal_id):
        """the callback for notification of deleted journals.

        :param journal_id: the ``Id`` of the registered ``Journal``
        :type journal_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_journal(self, journal_id, ancestor_id):
        """The callback for notifications of deleted ancestors of a journal.

        :param journal_id: the ``Id`` of the registered ``Journal``
        :type journal_id: ``osid.id.Id``
        :param ancestor_id: the Id of the removed ancestor journal
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_journal(self, journal_id, descendant_id):
        """The callback for notifications of deleted descendants of a journal.

        :param journal_id: the ``Id`` of the registered ``Journal``
        :type journal_id: ``osid.id.Id``
        :param descendant_id: the Id of the deleted descendant journal
        :type descendant_id: ``osid.id.Id``

        """
        pass


