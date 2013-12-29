from ..osid import receivers as osid_receivers


class AssetReceiver(osid_receivers.OsidReceiver):
    """The asset receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Asset`` objects."""
    def new_asset(self, asset_id):
        """The callback for notifications of new assets.

        :param asset_id: the ``Id`` of the new ``Asset``
        :type asset_id: ``osid.id.Id``

        """
        pass

    def changed_asset(self, asset_id):
        """The callback for notification of updated assets.

        :param asset_id: the ``Id`` of the updated ``Asset``
        :type asset_id: ``osid.id.Id``

        """
        pass

    def deleted_asset(self, asset_id):
        """the callback for notification of deleted assets.

        :param asset_id: the ``Id`` of the deleted ``Asset``
        :type asset_id: ``osid.id.Id``

        """
        pass


class CompositionReceiver(osid_receivers.OsidReceiver):
    """The composition receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Composition`` objects."""
    def new_composition(self, composition_id):
        """The callback for notifications of new compositions.

        :param composition_id: the ``Id`` of the new ``Composition``
        :type composition_id: ``osid.id.Id``

        """
        pass

    def new_composition_asset(self, asset_id):
        """The callback for notifications of new assets in the composition.

        :param asset_id: the ``Id`` of the new ``Asset``
        :type asset_id: ``osid.id.Id``

        """
        pass

    def new_composition_ancestor(self, composition_id, ancestor_id):
        """The callback for notifications of new composition ancestors.

        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Composition`` descendant
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_composition_descendant(self, composition_id, descendant_id):
        """The callback for notifications of new composition descendants.

        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Composition`` ancestor
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_composition(self, composition_id):
        """The callback for notification of updated compositions.

        :param composition_id: the ``Id`` of the updated ``Composition``
        :type composition_id: ``osid.id.Id``

        """
        pass

    def deleted_composition(self, composition_id):
        """the callback for notification of deleted compositions.

        :param composition_id: the ``Id`` of the deleted ``Composition``
        :type composition_id: ``osid.id.Id``

        """
        pass

    def deleted_composition_asset(self, asset_id):
        """The callback for notifications of deleted assets from this composition.

        :param asset_id: the ``Id`` of the removed ``Asset``
        :type asset_id: ``osid.id.Id``

        """
        pass

    def deleted_composition_ancestor(self, composition_id, ancestor_id):
        """The callback for notifications of deleted composition ancestors.

        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Composition`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_composition_descendant(self, composition_id, descendant_id):
        """The callback for notifications of deleted composition descendants.

        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Composition`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


class RepositoryReceiver(osid_receivers.OsidReceiver):
    """The repository receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Repository`` objects."""
    def new_repository(self, repository_id):
        """The callback for notifications of new repositories.

        :param repository_id: the ``Id`` of the new ``Repository``
        :type repository_id: ``osid.id.Id``

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

    def changed_repository(self, repository_id):
        """The callback for notification of updated repositories.

        :param repository_id: the ``Id`` of the updated ``Repository``
        :type repository_id: ``osid.id.Id``

        """
        pass

    def deleted_repository(self, repository_id):
        """The callback for notification of deleted repositories.

        :param repository_id: the ``Id`` of the deleted ``Repository``
        :type repository_id: ``osid.id.Id``

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


