from ..osid import receivers as osid_receivers


class ResourceReceiver(osid_receivers.OsidReceiver):
    """The resource receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Resource`` objects."""
    def new_resource(self, resource_id):
        """The callback for notifications of new resources.

        :param resource_id: the ``Id`` of the new ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass

    def changed_resource(self, resource_id):
        """The callback for notification of updated resources.

        :param resource_id: the ``Id`` of the updated ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass

    def changed_resource_membership(self, resource_id):
        """The callback for notification of updated resources.

        :param resource_id: the ``Id`` of the updated ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass

    def deleted_resource(self, resource_id):
        """the callback for notification of deleted resources.

        :param resource_id: the ``Id`` of the deleted ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass


class GroupReceiver(osid_receivers.OsidReceiver):
    """The resource group receiver is the consumer supplied interface for receiving notifications pertaining to new or deleted members."""
    def new_member(self, group_id, member_id):
        """The callback for notifications of new resource members.

        :param group_id: the ``Id`` of the ``Resource`` group
        :type group_id: ``osid.id.Id``
        :param member_id: the ``Id`` of the new ``Resource`` member
        :type member_id: ``osid.id.Id``

        """
        pass

    def deleted_member(self, group_id, member_id):
        """the callback for notification of deleted resource members.

        :param group_id: the ``Id`` of the ``Resource`` group
        :type group_id: ``osid.id.Id``
        :param member_id: the ``Id`` of the new ``Resource`` member
        :type member_id: ``osid.id.Id``

        """
        pass


class ResourceRelationshipReceiver(osid_receivers.OsidReceiver):
    """The resource relationship receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``ResourceRelationships``."""
    def new_resource_relationship(self, resource_relationship_id):
        """The callback for notifications of new relationships.

        :param resource_relationship_id: the ``Id`` of the new ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``

        """
        pass

    def changed_resource_relationship(self, resource_relationship_id):
        """The callback for notification of updated relationships.

        :param resource_relationship_id: the ``Id`` of the updated ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``

        """
        pass

    def deleted_resource_relationship(self, resource_relationship_id):
        """The callback for notification of deleted relationships.

        :param resource_relationship_id: the ``Id`` of the deleted ``ResourceRelationship``
        :type resource_relationship_id: ``osid.id.Id``

        """
        pass


class BinReceiver(osid_receivers.OsidReceiver):
    """The bin receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Bin`` objects."""
    def new_bin(self, bin_id):
        """The callback for notifications of new bins.

        :param bin_id: the ``Id`` of the new ``Bin``
        :type bin_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_bin(self, bin_id, ancestor_id):
        """The callback for notifications of new bin ancestors.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Bin`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_bin(self, bin_id, descendant_id):
        """The callback for notifications of new bin descendants.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Bin`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_bin(self, bin_id):
        """The callback for notification of updated bins.

        :param bin_id: the ``Id`` of the updated ``Bin``
        :type bin_id: ``osid.id.Id``

        """
        pass

    def deleted_bin(self, bin_id):
        """The callback for notification of deleted bins.

        :param bin_id: the ``Id`` of the deleted ``Bin``
        :type bin_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_bin(self, bin_id, ancestor_id):
        """The callback for notifications of deleted bin ancestors.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Bin`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_bin(self, bin_id, descendant_id):
        """The callback for notifications of deleted bin descendants.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Bin`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


