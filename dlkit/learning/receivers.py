from ..osid import receivers as osid_receivers


class ObjectiveReceiver(osid_receivers.OsidReceiver):
    """The objective receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Objectives``."""
    def new_objectives(self, notification_id, objective_ids):
        """The callback for notifications of new objectives.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param objective_ids: the ``Ids`` of the new ``Objectives``
        :type objective_ids: ``osid.id.IdList``

        """
        pass

    def changed_objectives(self, notification_id, objective_ids):
        """The callback for notification of updated objectives.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param objective_ids: the ``Ids`` of the updated ``Objectives``
        :type objective_ids: ``osid.id.IdList``

        """
        pass

    def deleted_objectives(self, notification_id, objective_ids):
        """The callback for notification of deleted objectives.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param objective_ids: the ``Ids`` of the deleted ``Objectives``
        :type objective_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_objectives(self, notification_id, objective_ids):
        """The callback for notifications of changes to children of objective hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param objective_ids: the ``Ids`` of the ``Objectives`` whose children have changed
        :type objective_ids: ``osid.id.IdList``

        """
        pass


class ActivityReceiver(osid_receivers.OsidReceiver):
    """The activity receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Activities``."""
    def new_activities(self, notification_id, activity_ids):
        """The callback for notifications of new activities.

        :param notification_id: the notification Id
        :type notification_id: ``osid.id.Id``
        :param activity_ids: the ``Id`` of the new ``Activities``
        :type activity_ids: ``osid.id.IdList``

        """
        pass

    def changed_activities(self, notification_id, activity_ids):
        """The callback for notification of updated activities.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param activity_ids: the ``Id`` of the updated ``Activities``
        :type activity_ids: ``osid.id.IdList``

        """
        pass

    def deleted_activities(self, notification_id, activity_ids):
        """The callback for notification of deleted activities.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param activity_ids: the ``Id`` of the deleted ``Activities``
        :type activity_ids: ``osid.id.IdList``

        """
        pass


class ProficiencyReceiver(osid_receivers.OsidReceiver):
    """The proficiency receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted proficiencies."""
    def new_proficiencies(self, notification_id, proficiency_ids):
        """The callback for notifications of new proficiencies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param proficiency_ids: the ``Ids`` of the new ``Proficiencies``
        :type proficiency_ids: ``osid.id.IdList``

        """
        pass

    def changed_proficiencies(self, notification_id, proficiency_ids):
        """The callback for notification of updated proficiencies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param proficiency_ids: the ``Ids`` of the updated ``Proficiencies``
        :type proficiency_ids: ``osid.id.IdList``

        """
        pass

    def deleted_proficiencies(self, notification_id, proficiency_ids):
        """The callback for notification of deleted proficiencies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param proficiency_ids: the ``Ids`` of the deleted ``Proficiencies``
        :type proficiency_ids: ``osid.id.IdList``

        """
        pass


class ObjectiveBankReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``ObjectiveBank`` objects."""
    def new_objective_banks(self, notification_id, objective_bank_ids):
        """The callback for notifications of new objective banks.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param objective_bank_ids: the ``Ids`` of the new ``ObjectiveBanks``
        :type objective_bank_ids: ``osid.id.IdList``

        """
        pass

    def changed_objective_banks(self, notification_id, objective_bank_ids):
        """The callback for notification of updated objective banks.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param objective_bank_ids: the ``Ids`` of the updated ``ObjectiveBanks``
        :type objective_bank_ids: ``osid.id.IdList``

        """
        pass

    def deleted_objective_banks(self, notification_id, objective_bank_ids):
        """The callback for notification of deleted objective banks.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param objective_bank_ids: the ``Ids`` of the deleted ``ObjectiveBanks``
        :type objective_bank_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_objective_banks(self, notification_id, objective_bank_ids):
        """The callback for notifications of changes to children of objective bank hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param objective_bank_ids: the ``Ids`` of the ``ObjectiveBanks`` whose children have changed
        :type objective_bank_ids: ``osid.id.IdList``

        """
        pass


