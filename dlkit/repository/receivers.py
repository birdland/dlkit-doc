from ..osid import receivers as osid_receivers


class AssetReceiver(osid_receivers.OsidReceiver):
    """The asset receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Asset`` objects."""
    def new_assets(self, asset_ids):
        """The callback for notifications of new assets.

        :param asset_ids: the ``Ids`` of the new ``Assets``
        :type asset_ids: ``osid.id.IdList``

        """
        pass

    def changed_assets(self, asset_ids):
        """The callback for notification of updated assets.

        :param asset_ids: the ``Ids`` of the updated ``Assets``
        :type asset_ids: ``osid.id.IdList``

        """
        pass

    def deleted_assets(self, asset_ids):
        """the callback for notification of deleted assets.

        :param asset_ids: the ``Ids`` of the deleted ``Assets``
        :type asset_ids: ``osid.id.IdList``

        """
        pass


class CompositionReceiver(osid_receivers.OsidReceiver):
    """The composition receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Composition`` objects."""
    def new_compositions(self, composition_ids):
        """The callback for notifications of new compositions.

        :param composition_ids: the ``Ids`` of the new ``Compositions``
        :type composition_ids: ``osid.id.IdList``

        """
        pass

    def changed_compositions(self, composition_ids):
        """The callback for notification of updated compositions.

        :param composition_ids: the ``Ids`` of the updated ``Compositions``
        :type composition_ids: ``osid.id.IdList``

        """
        pass

    def deleted_compositions(self, composition_ids):
        """the callback for notification of deleted compositions.

        :param composition_ids: the ``Ids`` of the deleted ``Compositions``
        :type composition_ids: ``osid.id.IdList``

        """
        pass


class RepositoryReceiver(osid_receivers.OsidReceiver):
    """The repository receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Repository`` objects."""
    def new_repositories(self, repository_ids):
        """The callback for notifications of new repositories.

        :param repository_ids: the ``Ids`` of the new ``Repositories``
        :type repository_ids: ``osid.id.IdList``

        """
        pass

    def new_ancestor_repository(self, repository_id, ancestor_id):
        """The callback for notifications of new repository ancestors.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Repository`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_repository(self, repository_id, descendant_id):
        """The callback for notifications of new repository descendants.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Repository`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_repositories(self, repository_ids):
        """The callback for notification of updated repositories.

        :param repository_ids: the ``Ids`` of the updated ``Repositories``
        :type repository_ids: ``osid.id.IdList``

        """
        pass

    def deleted_repositories(self, repository_ids):
        """The callback for notification of deleted repositories.

        :param repository_ids: the ``Ids`` of the deleted ``Repositories``
        :type repository_ids: ``osid.id.IdList``

        """
        pass

    def deleted_ancestor_repository(self, repository_id, ancestor_id):
        """The callback for notifications of deleted repository ancestors.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Repository`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_repository(self, repository_id, descendant_id):
        """The callback for notifications of deleted repository descendants.

        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Repository`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def restructured_repository_hierarchy(self):
        """The callback for notifications of changes to a respository hierarchy where the hierarchy needs to refreshed."""
        pass


