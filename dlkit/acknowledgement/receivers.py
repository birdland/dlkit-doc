from ..osid import receivers as osid_receivers


class CreditReceiver(osid_receivers.OsidReceiver):
    """The credit receiver is the consumer supplied interface for receiving notifications pertaining to new or deleted credits."""
    def new_credits(self, notification_id, credit_ids):
        """The callback for notifications of new credits.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param credit_ids: the ``Ids`` of the new credits
        :type credit_ids: ``osid.id.IdList``

        """
        pass

    def changed_credits(self, notification_id, credit_ids):
        """The callback for notifications of updated credits.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param credit_ids: the ``Ids`` of the updated credits
        :type credit_ids: ``osid.id.IdList``

        """
        pass

    def deleted_credits(self, notification_id, credit_ids):
        """the callback for notification of deleted credits.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param credit_ids: the ``Ids`` of the deleted credits
        :type credit_ids: ``osid.id.IdList``

        """
        pass


class BillingReceiver(osid_receivers.OsidReceiver):
    """The billing receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Billing`` objects."""
    def new_billings(self, notification_id, billing_ids):
        """The callback for notifications of new billings.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param billing_ids: the ``Ids`` of the new ``Billings``
        :type billing_ids: ``osid.id.IdList``

        """
        pass

    def changed_billings(self, notification_id, billing_ids):
        """The callback for notification of updated billings.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param billing_ids: the ``Ids`` of the updated ``Billings``
        :type billing_ids: ``osid.id.IdList``

        """
        pass

    def deleted_billings(self, notification_id, billing_ids):
        """the callback for notification of deleted billings.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param billing_ids: the ``Ids`` of the registered ``Billings``
        :type billing_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_billings(self, notification_id, billing_ids):
        """The callback for notifications of changes to children of billing hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param billing_ids: the ``Ids`` of the ``Billings`` whose children have changed
        :type billing_ids: ``osid.id.IdList``

        """
        pass


