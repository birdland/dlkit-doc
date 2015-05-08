from ..osid import receivers as osid_receivers


class PackageReceiver(osid_receivers.OsidReceiver):
    """The package receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Packages``."""
    def new_packages(self, package_ids):
        """The callback for notifications of new packages.

        :param package_ids: the ``Ids`` of the new ``Packages``
        :type package_ids: ``osid.id.IdList``

        """
        pass

    def changed_packages(self, package_ids):
        """The callback for notification of updated packages.

        :param package_ids: the ``Ids`` of the updated ``Packages``
        :type package_ids: ``osid.id.IdList``

        """
        pass

    def deleted_packages(self, package_ids):
        """The callback for notification of deleted packages.

        :param package_ids: the ``Ids`` of the deleted ``Packages``
        :type package_ids: ``osid.id.IdList``

        """
        pass


class DepotReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Depot`` objects."""
    def new_depots(self, depot_ids):
        """The callback for notifications of new depots.

        :param depot_ids: the ``Ids`` of the new ``Depots``
        :type depot_ids: ``osid.id.IdList``

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

    def changed_depots(self, depot_ids):
        """The callback for notification of updated depots.

        :param depot_ids: the ``Ids`` of the updated ``Depots``
        :type depot_ids: ``osid.id.IdList``

        """
        pass

    def deleted_depots(self, depot_ids):
        """The callback for notification of deleted depots.

        :param depot_ids: the ``Ids`` of the deleted ``Depots``
        :type depot_ids: ``osid.id.IdList``

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

    def restructured_depot_hierarchy(self):
        """The callback for notifications of changes to a depot hierarchy where the hierarchy needs to refreshed."""
        pass


class InstallationReceiver(osid_receivers.OsidReceiver):
    """The installation receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Installations``."""
    def new_installations(self, installation_ids):
        """The callback for notifications of new installations.

        :param installation_ids: the ``Ids`` of the new ``Installations``
        :type installation_ids: ``osid.id.IdList``

        """
        pass

    def deleted_installations(self, installation_ids):
        """The callback for notification of deleted installations.

        :param installation_ids: the ``Ids`` of the deleted ``Installations``
        :type installation_ids: ``osid.id.IdList``

        """
        pass


