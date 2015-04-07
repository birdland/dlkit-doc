from ..osid import receivers as osid_receivers


class LogEntryReceiver(osid_receivers.OsidReceiver):
    """The log entry receiver is the consumer supplied interface for receiving notifications pertaining to new log entries."""
    def new_log_entries(self, notification_id, entry_ids):
        """The callback for notifications of new log entries.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param entry_ids: the ``Ids`` of the new entries
        :type entry_ids: ``osid.id.IdList``

        """
        pass

    def changed_log_entries(self, notification_id, entry_ids):
        """The callback for notifications of changed log entries.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param entry_ids: the ``Ids`` of the changed entries
        :type entry_ids: ``osid.id.IdList``

        """
        pass

    def deleted_log_entries(self, notification_id, entry_ids):
        """the callback for notification of deleted log entries.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param entry_ids: the ``Ids`` of the deleted entries
        :type entry_ids: ``osid.id.IdList``

        """
        pass


class LogReceiver(osid_receivers.OsidReceiver):
    """The log receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Log`` objects."""
    def new_logs(self, notification_id, log_ids):
        """The callback for notifications of new logs.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param log_ids: the ``Ids`` of the new ``Logs``
        :type log_ids: ``osid.id.IdList``

        """
        pass

    def changed_logs(self, notification_id, log_ids):
        """The callback for notification of updated logs.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param log_ids: the ``Ids`` of the updated ``Logs``
        :type log_ids: ``osid.id.IdList``

        """
        pass

    def deleted_logs(self, notification_id, log_ids):
        """the callback for notification of deleted logs.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param log_ids: the ``Ids`` of the registered ``Logs``
        :type log_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_logs(self, notification_id, log_ids):
        """The callback for notifications of changes to children of log hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param log_ids: the ``Ids`` of the ``Logs`` whose children have changed
        :type log_ids: ``osid.id.IdList``

        """
        pass


