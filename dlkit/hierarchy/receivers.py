from ..osid import receivers as osid_receivers


class HierarchyStructureReceiver(osid_receivers.OsidReceiver):
    """The hierarchy receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted hierarchy nodes."""
    def new_node(self, node_id):
        """The callback for notifications of new hierarchy nodes.

        :param node_id: the ``Id`` of the new node
        :type node_id: ``osid.id.Id``

        """
        pass

    def new_ancestor(self, node_id, ancestor_id):
        """The callback for notification of a change to the node's ancestry.

        :param node_id: the ``Id`` of the registered node
        :type node_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor(self, node_id, ancestor_id):
        """The callback for notification of a change to the node's ancestry.

        :param node_id: the ``Id`` of the registered node
        :type node_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the deleted ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant(self, node_id, ancestor_id):
        """The callback for notification of a change to the node's descendants.

        :param node_id: the ``Id`` of the registered node
        :type node_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new descednant
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant(self, node_id, ancestor_id):
        """The callback for notification of a change to the node's descendants.

        :param node_id: the ``Id`` of the registered node
        :type node_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the deleted descednant
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_node(self, node_id):
        """the callback for notification of deleted hierarchy nodes.

        :param node_id: the ``Id`` of the deleted node
        :type node_id: ``osid.id.Id``

        """
        pass


class HierarchyReceiver(osid_receivers.OsidReceiver):
    """The hierarchy receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Hierarchy`` objects."""
    def new_hierarchy(self, hierarchy_id):
        """The callback for notifications of new hierarchies.

        :param hierarchy_id: the ``Id`` of the new ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``

        """
        pass

    def changed_hierarchy(self, hierarchy_id):
        """The callback for notification of updated hierarchies.

        :param hierarchy_id: the ``Id`` of the updated ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``

        """
        pass

    def deleted_hierarchy(self, hierarchy_id):
        """the callback for notification of deleted hierarchies.

        :param hierarchy_id: the ``Id`` of the deleted ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``

        """
        pass


