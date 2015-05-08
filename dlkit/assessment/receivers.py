from ..osid import receivers as osid_receivers


class ItemReceiver(osid_receivers.OsidReceiver):
    """The item receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Items``."""
    def new_items(self, notification_id, item_ids):
        """The callback for notifications of new items.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param item_ids: the Id of the new ``Items``
        :type item_ids: ``osid.id.IdList``

        """
        pass

    def changed_items(self, notification_id, item_ids):
        """The callback for notification of updated items.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param item_ids: the Id of the updated ``Items``
        :type item_ids: ``osid.id.IdList``

        """
        pass

    def deleted_items(self, notification_id, item_ids):
        """The callback for notification of deleted items.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param item_ids: the Id of the deleted ``Items``
        :type item_ids: ``osid.id.IdList``

        """
        pass


class AssessmentReceiver(osid_receivers.OsidReceiver):
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Assessment`` objects."""
    def new_assessments(self, notification_id, assessment_ids):
        """The callback for notifications of new assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_ids: the ``Ids`` of the new ``Assessments``
        :type assessment_ids: ``osid.id.IdList``

        """
        pass

    def changed_assessments(self, notification_id, assessment_ids):
        """The callback for notification of updated assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_ids: the ``Ids`` of the updated ``Assessments``
        :type assessment_ids: ``osid.id.IdList``

        """
        pass

    def deleted_assessments(self, notification_id, assessment_ids):
        """the callback for notification of deleted assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_ids: the ``Ids`` of the deleted ``Assessments``
        :type assessment_ids: ``osid.id.IdList``

        """
        pass


class AssessmentOfferedReceiver(osid_receivers.OsidReceiver):
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``AssessmentOffered`` objects."""
    def new_assessments_offered(self, notification_id, assessment_offered_ids):
        """The callback for notifications of new offered assessments.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param assessment_offered_ids: the ``Id`` of the new ``AssessmentsOffered``
        :type assessment_offered_ids: ``osid.id.IdList``

        """
        pass

    def changed_assessments_offered(self, notification_id, assessment_offered_ids):
        """The callback for notification of updated offered assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_offered_ids: the ``Id`` of the updated ``AssessmentsOffered``
        :type assessment_offered_ids: ``osid.id.IdList``

        """
        pass

    def deleted_assessments_offered(self, notification_id, assessment_offered_ids):
        """the callback for notification of deleted offered assessments.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param assessment_offered_ids: the ``Id`` of the deleted ``AssessmentsOffered``
        :type assessment_offered_ids: ``osid.id.IdList``

        """
        pass


class AssessmentTakenReceiver(osid_receivers.OsidReceiver):
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``AssessmentTaken`` objects."""
    def new_assessments_taken(self, notification_id, assessment_taken_ids):
        """The callback for notifications of new taken assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_taken_ids: the ``Ids`` of the new ``AssessmentsTaken``
        :type assessment_taken_ids: ``osid.id.IdList``

        """
        pass

    def changed_assessmenst_taken(self, notification_id, assessment_taken_ids):
        """The callback for notification of updated taken assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_taken_ids: the ``Ids`` of the updated ``AssessmentsTaken``
        :type assessment_taken_ids: ``osid.id.IdList``

        """
        pass

    def deleted_assessmenst_taken(self, notification_id, assessment_taken_ids):
        """the callback for notification of deleted taken assessments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param assessment_taken_ids: the ``Ids`` of the deleted ``AssessmentsTaken``
        :type assessment_taken_ids: ``osid.id.IdList``

        """
        pass


class BankReceiver(osid_receivers.OsidReceiver):
    """The bank receiver is the consumer supplied interface for receiving notifications pertaining to new, updated, or deleted Bank objects."""
    def new_banks(self, notification_id, bank_ids):
        """The callback for notifications of new banks.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param bank_ids: the ``Ids`` of the ``Banks``
        :type bank_ids: ``osid.id.IdList``

        """
        pass

    def changed_banks(self, notification_id, bank_ids):
        """The callback for notification of updated banks.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param bank_ids: the ``Ids`` of the ``Banks``
        :type bank_ids: ``osid.id.IdList``

        """
        pass

    def deleted_banks(self, notification_id, bank_ids):
        """The callback for notification of deleted banks.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param bank_ids: the ``Ids`` of the ``Banks``
        :type bank_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_banks(self, notification_id, bank_ids):
        """The callback for notifications of changes to children of bank hierarchy nodes.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param bank_ids: the ``Ids`` of the ``Banks`` whose children have changed
        :type bank_ids: ``osid.id.IdList``

        """
        pass


