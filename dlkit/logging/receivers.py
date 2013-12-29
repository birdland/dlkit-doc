from ..osid import receivers as osid_receivers


class LogEntryReceiver(osid_receivers.OsidReceiver):
    """The log entry receiver is the consumer supplied interface for receiving notifications pertaining to new log entries."""
    def new_log_entry(self, entry_id):
        """The callback for notifications of new log entries.

        :param entry_id: the ``Id`` of the new entry
        :type entry_id: ``osid.id.Id``

        """
        pass

    def changed_log_entry(self, entry_id):
        """The callback for notifications of changed log entries.

        :param entry_id: the ``Id`` of the changed entry
        :type entry_id: ``osid.id.Id``

        """
        pass

    def deleted_log_entry(self, entry_id):
        """the callback for notification of deleted log entries.

        :param entry_id: the ``Id`` of the deleted entry
        :type entry_id: ``osid.id.Id``

        """
        pass


class LogReceiver(osid_receivers.OsidReceiver):
    """The log receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Log`` objects."""
    def new_log(self, log_id):
        """The callback for notifications of new logs.

        :param log_id: the ``Id`` of the new ``Log``
        :type log_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_log(self, log_id, ancestor_id):
        """The callback for notifications of new ancestors of a log.

        :param log_id: the ``Id`` of the registered ``Log``
        :type log_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ancestor log
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_log(self, log_id, descendant_id):
        """The callback for notifications of new descendant of a log.

        :param log_id: the ``Id`` of the registered ``Log``
        :type log_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new descendant log
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_log(self, log_id):
        """The callback for notification of updated logs.

        :param log_id: the ``Id`` of the updated ``Log``
        :type log_id: ``osid.id.Id``

        """
        pass

    def deleted_log(self, log_id):
        """the callback for notification of deleted logs.

        :param log_id: the ``Id`` of the registered ``Log``
        :type log_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_log(self, log_id, ancestor_id):
        """The callback for notifications of deleted ancestors of a log.

        :param log_id: the ``Id`` of the registered ``Log``
        :type log_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ancestor log
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_log(self, log_id, descendant_id):
        """The callback for notifications of deleted descendants of a log.

        :param log_id: the ``Id`` of the registered ``Log``
        :type log_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the deleted descendant log
        :type descendant_id: ``osid.id.Id``

        """
        pass


