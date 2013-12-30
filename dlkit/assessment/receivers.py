from ..osid import receivers as osid_receivers


class ItemReceiver(osid_receivers.OsidReceiver):
    """The item receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Items``."""
    def new_item(self, item_id):
        """The callback for notifications of new items.

        :param item_id: the Id of the new ``Item``
        :type item_id: ``osid.id.Id``

        """
        pass

    def changed_item(self, item_id):
        """The callback for notification of updated items.

        :param item_id: the Id of the updated ``Item``
        :type item_id: ``osid.id.Id``

        """
        pass

    def deleted_item(self, item_id):
        """The callback for notification of deleted items.

        :param item_id: the Id of the deleted ``Item``
        :type item_id: ``osid.id.Id``

        """
        pass


class AssessmentReceiver(osid_receivers.OsidReceiver):
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Assessment`` objects."""
    def new_assessment(self, assessment_id):
        """The callback for notifications of new assessments.

        :param assessment_id: the ``Id`` of the new ``Assessment``
        :type assessment_id: ``osid.id.Id``

        """
        pass

    def changed_assessment(self, assessment_id):
        """The callback for notification of updated assessments.

        :param assessment_id: the ``Id`` of the updated ``Assessment``
        :type assessment_id: ``osid.id.Id``

        """
        pass

    def deleted_assessment(self, assessment_id):
        """the callback for notification of deleted assessments.

        :param assessment_id: the ``Id`` of the deleted ``Assessment``
        :type assessment_id: ``osid.id.Id``

        """
        pass


class AssessmentOfferedReceiver(osid_receivers.OsidReceiver):
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``AssessmentOffered`` objects."""
    def new_assessment_offered(self, assessment_offered_id):
        """The callback for notifications of new offered assessments.

        :param assessment_offered_id: the ``Id`` of the new ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``

        """
        pass

    def changed_assessment_offered(self, assessment_offered_id):
        """The callback for notification of updated offered assessments.

        :param assessment_offered_id: the ``Id`` of the updated ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``

        """
        pass

    def deleted_assessment_offered(self, assessment_offered_id):
        """the callback for notification of deleted offered assessments.

        :param assessment_offered_id: the ``Id`` of the deleted ``AssessmentOffered``
        :type assessment_offered_id: ``osid.id.Id``

        """
        pass


class AssessmentTakenReceiver(osid_receivers.OsidReceiver):
    """The assessment receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``AssessmentTaken`` objects."""
    def new_assessment_taken(self, assessment_taken_id):
        """The callback for notifications of new taken assessments.

        :param assessment_taken_id: the ``Id`` of the new ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``

        """
        pass

    def changed_assessment_taken(self, assessment_taken_id):
        """The callback for notification of updated taken assessments.

        :param assessment_taken_id: the ``Id`` of the updated ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``

        """
        pass

    def deleted_assessment_taken(self, assessment_taken_id):
        """the callback for notification of deleted taken assessments.

        :param assessment_taken_id: the ``Id`` of the deleted ``AssessmentTaken``
        :type assessment_taken_id: ``osid.id.Id``

        """
        pass


class BankReceiver(osid_receivers.OsidReceiver):
    """The bank receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted Bank objects."""
    def new_bank(self, bank_id):
        """The callback for notifications of new banks.

        :param bank_id: the Id of the new ``Bank``
        :type bank_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_bank(self, bank_id, ancestor_id):
        """The callback for notifications of new bank ancestors.

        :param bank_id: the Id of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(bank_record_type) is false``
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_bank(self, bank_id, descendant_id):
        """The callback for notifications of new bank descendants.

        :param bank_id: the Id of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param descendant_id: the Id of the new ``Bank`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_bank(self, bank_id):
        """The callback for notification of updated banks.

        :param bank_id: the Id of the updated ``Bank``
        :type bank_id: ``osid.id.Id``

        """
        pass

    def deleted_bank(self, bank_id):
        """The callback for notification of deleted banks.

        :param bank_id: the Id of the deleted ``Bank``
        :type bank_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_bank(self, bank_id, ancestor_id):
        """The callback for notifications of deleted bank ancestors.

        :param bank_id: the Id of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param ancestor_id: the Id of the removed ``Bank`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_bank(self, bank_id, descendant_id):
        """The callback for notifications of deleted bank descendants.

        :param bank_id: the Id of the ``Bank``
        :type bank_id: ``osid.id.Id``
        :param descendant_id: the Id of the removed ``Bank`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


