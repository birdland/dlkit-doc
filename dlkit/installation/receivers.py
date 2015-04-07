from ..osid import receivers as osid_receivers


class PackageReceiver(osid_receivers.OsidReceiver):
    """The package receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Packages``."""
    def new_package(self, package_id):
        """The callback for notifications of new packages.

        :param package_id: the ``Id`` of the new ``Package``
        :type package_id: ``osid.id.Id``

        """
        pass

    def changed_package(self, package_id):
        """The callback for notification of updated packages.

        :param package_id: the ``Id`` of the updated ``Package``
        :type package_id: ``osid.id.Id``

        """
        pass

    def deleted_package(self, package_id):
        """The callback for notification of deleted packages.

        :param package_id: the ``Id`` of the deleted ``Package``
        :type package_id: ``osid.id.Id``

        """
        pass


class DepotReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Depot`` objects."""
    def new_depot(self, depot_id):
        """The callback for notifications of new depots.

        :param depot_id: the ``Id`` of the new ``Depot``
        :type depot_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_depot(self, depot_id, ancestor_id):
        """The callback for notifications of new depot ancestors.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(depot_record_type) is false``
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_depot(self, depot_id, descendant_id):
        """The callback for notifications of new depot descendants.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Depot`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_depot(self, depot_id):
        """The callback for notification of updated depots.

        :param depot_id: the ``Id`` of the updated ``Depot``
        :type depot_id: ``osid.id.Id``

        """
        pass

    def deleted_depot(self, depot_id):
        """The callback for notification of deleted depots.

        :param depot_id: the ``Id`` of the deleted ``Depot``
        :type depot_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_depot(self, depot_id, ancestor_id):
        """The callback for notifications of deleted depot ancestors.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Depot`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_depot(self, depot_id, descendant_id):
        """The callback for notifications of deleted depot descendants.

        :param depot_id: the ``Id`` of the ``Depot``
        :type depot_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Depot`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


class InstallationReceiver(osid_receivers.OsidReceiver):
    """The installation receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Installations``."""
    def new_installation(self, installation_id):
        """The callback for notifications of new installations.

        :param installation_id: the ``Id`` of the new ``Installation``
        :type installation_id: ``osid.id.Id``

        """
        pass

    def deleted_installation(self, installation_id):
        """The callback for notification of deleted installations.

        :param installation_id: the ``Id`` of the deleted ``Installation``
        :type installation_id: ``osid.id.Id``

        """
        pass


