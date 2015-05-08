from ..osid import receivers as osid_receivers


class RelationshipReceiver(osid_receivers.OsidReceiver):
    """The relationship receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Relationship`` objects."""
    def new_relationships(self, notification_id, relationship_ids):
        """The callback for notifications of new relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param relationship_ids: the ``Ids`` of the new ``Relationships``
        :type relationship_ids: ``osid.id.IdList``

        """
        pass

    def changed_relationships(self, notification_id, relationship_ids):
        """The callback for notification of updated relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param relationship_ids: the ``Ids`` of the updated ``Relationships``
        :type relationship_ids: ``osid.id.IdList``

        """
        pass

    def deleted_relationships(self, notification_id, relationship_ids):
        """the callback for notification of deleted relationships.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param relationship_ids: the ``Ids`` of the deleted ``Relationships``
        :type relationship_ids: ``osid.id.IdList``

        """
        pass


class FamilyReceiver(osid_receivers.OsidReceiver):
    """The family receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Family`` objects."""
    def new_families(self, notification_id, family_ids):
        """The callback for notifications of new families.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param family_ids: the ``Ids`` of the new ``Families``
        :type family_ids: ``osid.id.IdList``

        """
        pass

    def changed_families(self, notification_id, family_ids):
        """The callback for notification of updated families.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param family_ids: the ``Ids`` of the updated ``Families``
        :type family_ids: ``osid.id.IdList``

        """
        pass

    def deleted_families(self, notification_id, family_ids):
        """the callback for notification of deleted familys.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param family_ids: the ``Ids`` of the registered ``Families``
        :type family_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_families(self, notification_id, family_ids):
        """The callback for notifications of changes to children of family hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param family_ids: the ``Ids`` of the ``Families`` whose children have changed
        :type family_ids: ``osid.id.IdList``

        """
        pass


