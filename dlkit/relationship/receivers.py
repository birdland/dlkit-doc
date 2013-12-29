from ..osid import receivers as osid_receivers


class RelationshipReceiver(osid_receivers.OsidReceiver):
    """The relationship receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Relationship`` objects."""
    def new_relationship(self, relationship_id):
        """The callback for notifications of new relationships.

        :param relationship_id: the ``Id`` of the new ``Relationship``
        :type relationship_id: ``osid.id.Id``

        """
        pass

    def changed_relationship(self, relationship_id):
        """The callback for notification of updated relationships.

        :param relationship_id: the ``Id`` of the updated ``Relationship``
        :type relationship_id: ``osid.id.Id``

        """
        pass

    def deleted_relationship(self, relationship_id):
        """the callback for notification of deleted relationships.

        :param relationship_id: the ``Id`` of the deleted ``Relationship``
        :type relationship_id: ``osid.id.Id``

        """
        pass


class FamilyReceiver(osid_receivers.OsidReceiver):
    """The family receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Family`` objects."""
    def new_family(self, family_id):
        """The callback for notifications of new families.

        :param family_id: the ``Id`` of the new ``Family``
        :type family_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_family(self, family_id, ancestor_id):
        """The callback for notifications of new ancestors of an family.

        :param family_id: the ``Id`` of the registered ``Family``
        :type family_id: ``osid.id.Id``
        :param ancestor_id: the Id of the new ancestor family
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_family(self, family_id, descendant_id):
        """The callback for notifications of new descendant of an family.

        :param family_id: the ``Id`` of the registered ``Family``
        :type family_id: ``osid.id.Id``
        :param descendant_id: the Id of the new descendant family
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_family(self, family_id):
        """The callback for notification of updated families.

        :param family_id: the ``Id`` of the updated ``Family``
        :type family_id: ``osid.id.Id``

        """
        pass

    def deleted_family(self, family_id):
        """the callback for notification of deleted familys.

        :param family_id: the ``Id`` of the registered ``Family``
        :type family_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_family(self, family_id, ancestor_id):
        """The callback for notifications of deleted ancestors of an family.

        :param family_id: the ``Id`` of the registered ``Family``
        :type family_id: ``osid.id.Id``
        :param ancestor_id: the Id of the removed ancestor family
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_family(self, family_id, descendant_id):
        """The callback for notifications of deleted descendants of an family.

        :param family_id: the ``Id`` of the registered ``Family``
        :type family_id: ``osid.id.Id``
        :param descendant_id: the Id of the deleted descendant family
        :type descendant_id: ``osid.id.Id``

        """
        pass


