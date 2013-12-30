from ..osid import receivers as osid_receivers


class AssessmentPartReceiver(osid_receivers.OsidReceiver):
    """The assessment part receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted assessment parts."""
    def new_assessment_part(self, assessment_part_id):
        """The callback for notifications of new assessment parts.

        :param assessment_part_id: the ``Id`` of the new ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``

        """
        pass

    def changed_assessment_part(self, assessment_part_id):
        """The callback for notification of updated assessment parts.

        :param assessment_part_id: the ``Id`` of the updated ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``

        """
        pass

    def deleted_assessment_part(self, assessment_part_id):
        """The callback for notification of deleted assessment parts.

        :param assessment_part_id: the ``Id`` of the deleted ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``

        """
        pass


class SequenceRuleReceiver(osid_receivers.OsidReceiver):
    """The sequence rule receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted sequence rules."""
    def new_sequence_rule(self, sequence_rule_id):
        """The callback for notifications of new sequence rules.

        :param sequence_rule_id: the ``Id`` of the new ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``

        """
        pass

    def changed_sequence_rule(self, sequence_rule_id):
        """The callback for notification of updated sequence rules.

        :param sequence_rule_id: the ``Id`` of the updated ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``

        """
        pass

    def deleted_sequence_rule(self, sequence_rule_id):
        """The callback for notification of deleted sequence rules.

        :param sequence_rule_id: the ``Id`` of the deleted ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``

        """
        pass


class SequenceRuleEnablerReceiver(osid_receivers.OsidReceiver):
    """The sequence rule enabler receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted sequence rule enablers."""
    def new_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """The callback for notifications of new sequence rule enablers.

        :param sequence_rule_enabler_id: the ``Id`` of the new ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``

        """
        pass

    def changed_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """The callback for notification of updated sequence rule enablers.

        :param sequence_rule_enabler_id: the ``Id`` of the updated ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``

        """
        pass

    def deleted_sequence_rule_enabler(self, sequence_rule_enabler_id):
        """The callback for notification of deleted sequence rule enablers.

        :param sequence_rule_enabler_id: the ``Id`` of the deleted ``SequenceRuleEnabler``
        :type sequence_rule_enabler_id: ``osid.id.Id``

        """
        pass


