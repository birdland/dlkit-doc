
from ..osid import receivers as osid_receivers


class HierarchyStructureReceiver(osid_receivers.OsidReceiver):
    """The hierarchy receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or
        deleted hierarchy nodes."""

    def new_nodes(self, notification_id, node_ids):
        """The callback for notifications of new hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param node_ids: the ``Ids`` of the new nodes
        :type node_ids: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_nodes(self, notification_id, node_ids):
        """the callback for notification of deleted hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param node_ids: the ``Ids`` of the deleted nodes
        :type node_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def changed_child_of_nodes(self, notification_id, node_ids):
        """The callback for notifications of changes to children of hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param node_ids: the ``Ids`` of the nodes whose children have changed
        :type node_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class HierarchyReceiver(osid_receivers.OsidReceiver):
    """The hierarchy receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or
        deleted ``Hierarchy`` objects."""

    def new_hierarchies(self, notification_id, hierarchy_ids):
        """The callback for notifications of new hierarchies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param hierarchy_ids: the ``Ids`` of the new ``Hierarchies``
        :type hierarchy_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def changed_hierarchies(self, notification_id, hierarchy_ids):
        """The callback for notification of updated hierarchies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param hierarchy_ids: the ``Ids`` of the updated ``Hierarchies``
        :type hierarchy_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def deleted_hierarchies(self, notification_id, hierarchy_ids):
        """the callback for notification of deleted hierarchies.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param hierarchy_ids: the ``Ids`` of the deleted ``Hierarchies``
        :type hierarchy_ids: ``osid.id.IdList``


        *compliance: mandatory -- This method must be implemented.*

        """
        pass


