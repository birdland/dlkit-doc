from ..osid import receivers as osid_receivers


class ObjectiveReceiver(osid_receivers.OsidReceiver):
    """The objective receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Objectives``."""
    def new_objective(self, objective_id):
        """The callback for notifications of new objectives.

        :param objective_id: the ``Id`` of the new ``Objective``
        :type objective_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_objective(self, objective_id, ancestor_id):
        """The callback for notifications of new objective ancestors.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Objective`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_objective(self, objective_id, descendant_id):
        """The callback for notifications of new objective descendants.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Objective`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_objective(self, objective_id):
        """The callback for notification of updated objectives.

        :param objective_id: the ``Id`` of the updated ``Objective``
        :type objective_id: ``osid.id.Id``

        """
        pass

    def deleted_objective(self, objective_id):
        """The callback for notification of deleted objectives.

        :param objective_id: the ``Id`` of the deleted ``Objective``
        :type objective_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_objective(self, objective_id, ancestor_id):
        """The callback for notifications of deleted objective ancestors.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Objective`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_objective(self, objective_id, descendant_id):
        """The callback for notifications of deleted objective descendants.

        :param objective_id: the ``Id`` of the ``Objective``
        :type objective_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Objective`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


class ActivityReceiver(osid_receivers.OsidReceiver):
    """The activity receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Activities``."""
    def new_activity(self, activity_id):
        """The callback for notifications of new activities.

        :param activity_id: the ``Id`` of the new ``Activity``
        :type activity_id: ``osid.id.Id``

        """
        pass

    def changed_activity(self, activity_id):
        """The callback for notification of updated activities.

        :param activity_id: the ``Id`` of the updated ``Activity``
        :type activity_id: ``osid.id.Id``

        """
        pass

    def deleted_activity(self, activity_id):
        """The callback for notification of deleted activities.

        :param activity_id: the ``Id`` of the deleted ``Activity``
        :type activity_id: ``osid.id.Id``

        """
        pass


class ProficiencyReceiver(osid_receivers.OsidReceiver):
    """The proficiency receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted proficiencies."""
    def new_proficiency(self, proficiency_id):
        """The callback for notifications of new proficiencies.

        :param proficiency_id: the ``Id`` of the new ``Proficiency``
        :type proficiency_id: ``osid.id.Id``

        """
        pass

    def changed_proficiency(self, proficiency_id):
        """The callback for notification of updated proficiencies.

        :param proficiency_id: the ``Id`` of the updated ``Proficiency``
        :type proficiency_id: ``osid.id.Id``

        """
        pass

    def deleted_proficiency(self, proficiency_id):
        """The callback for notification of deleted proficiencies.

        :param proficiency_id: the ``Id`` of the deleted ``Proficiency``
        :type proficiency_id: ``osid.id.Id``

        """
        pass


class ObjectiveBankReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``ObjectiveBank`` objects."""
    def new_objective_bank(self, objective_bank_id):
        """The callback for notifications of new objective banks.

        :param objective_bank_id: the ``Id`` of the new ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_objective_bank(self, objective_bank_id, ancestor_id):
        """The callback for notifications of new objective bank ancestors.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``ObjectiveBank`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_objective_bank(self, objective_bank_id, descendant_id):
        """The callback for notifications of new objective bank descendants.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``ObjectiveBank`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_objective_bank(self, objective_bank_id):
        """The callback for notification of updated objective banks.

        :param objective_bank_id: the ``Id`` of the updated ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``

        """
        pass

    def deleted_objective_bank(self, objective_bank_id):
        """The callback for notification of deleted objective banks.

        :param objective_bank_id: the ``Id`` of the deleted ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_objective_bank(self, objective_bank_id, ancestor_id):
        """The callback for notifications of deleted objective bank ancestors.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``ObjectiveBank`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_objective_bank(self, objective_bank_id, descendant_id):
        """The callback for notifications of deleted objective bank descendants.

        :param objective_bank_id: the ``Id`` of the ``ObjectiveBank``
        :type objective_bank_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``ObjectiveBank`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


