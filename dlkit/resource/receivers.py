from ..osid import receivers as osid_receivers


class ResourceReceiver(osid_receivers.OsidReceiver):
    """The resource receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Resource`` objects."""
    def new_resources(self, resource_ids):
        """The callback for notifications of new resources.

        :param resource_ids: the ``Ids`` of the new ``Resources``
        :type resource_ids: ``osid.id.IdList``

        """
        pass

    def changed_resources(self, resource_ids):
        """The callback for notification of updated resources.

        :param resource_ids: the ``Ids`` of the updated ``Resources``
        :type resource_ids: ``osid.id.IdList``

        """
        pass

    def deleted_resources(self, resource_ids):
        """the callback for notification of deleted resources.

        :param resource_ids: the ``Ids`` of the deleted ``Resources``
        :type resource_ids: ``osid.id.IdList``

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
    def new_resource_relationships(self, resource_relationship_ids):
        """The callback for notifications of new relationships.

        :param resource_relationship_ids: the ``Ids`` of the new ``ResourceRelationships``
        :type resource_relationship_ids: ``osid.id.IdList``

        """
        pass

    def changed_resource_relationships(self, resource_relationship_ids):
        """The callback for notification of updated relationships.

        :param resource_relationship_ids: the ``Ids`` of the updated ``ResourceRelationships``
        :type resource_relationship_ids: ``osid.id.IdList``

        """
        pass

    def deleted_resource_relationships(self, resource_relationship_ids):
        """The callback for notification of deleted relationships.

        :param resource_relationship_ids: the ``Ids`` of the deleted ``ResourceRelationships``
        :type resource_relationship_ids: ``osid.id.IdList``

        """
        pass


class BinReceiver(osid_receivers.OsidReceiver):
    """The bin receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Bin`` objects."""
    def new_bins(self, bin_ids):
        """The callback for notifications of new bins.

        :param bin_ids: the ``Ids`` of the new ``Bins``
        :type bin_ids: ``osid.id.IdList``

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

    def changed_bins(self, bin_ids):
        """The callback for notification of updated bins.

        :param bin_ids: the ``Ids`` of the updated ``Bins``
        :type bin_ids: ``osid.id.IdList``

        """
        pass

    def deleted_bins(self, bin_ids):
        """The callback for notification of deleted bins.

        :param bin_ids: the ``Ids`` of the deleted ``Bins``
        :type bin_ids: ``osid.id.IdList``

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

    def restructured_bin_hierarchy(self):
        """The callback for notifications of changes to a bin hierarchy where the hierarchy needs to refreshed."""
        pass


