from ..osid import receivers as osid_receivers


class LocationReceiver(osid_receivers.OsidReceiver):
    """The location receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted locations."""
    def new_location(self, location_id):
        """The callback for notifications of new locations.

        :param location_id: the ``Id`` of the new ``Location``
        :type location_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_location(self, location_id, ancestor_id):
        """The callback for notifications of new location ancestors.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Location`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_location(self, location_id, descendant_id):
        """The callback for notifications of new location descendants.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Location`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_location(self, location_id):
        """The callback for notification of updated locations.

        :param location_id: the ``Id`` of the updated ``Location``
        :type location_id: ``osid.id.Id``

        """
        pass

    def deleted_location(self, location_id):
        """The callback for notification of deleted locations.

        :param location_id: the ``Id`` of the deleted ``Location``
        :type location_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_location(self, location_id, ancestor_id):
        """The callback for notifications of deleted location ancestors.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Location`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_location(self, location_id, descendant_id):
        """The callback for notifications of deleted location descendants.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Location`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


class MapReceiver(osid_receivers.OsidReceiver):
    """The map receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Map`` objects."""
    def new_map(self, map_id):
        """The callback for notifications of new maps.

        :param map_id: the ``Id`` of the new ``Map``
        :type map_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_map(self, map_id, ancestor_id):
        """The callback for notifications of new map ancestors.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``Map`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_map(self, map_id, descendant_id):
        """The callback for notifications of new map descendants.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Map`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_map(self, map_id):
        """The callback for notification of updated map.

        :param map_id: the ``Id`` of the updated ``Map``
        :type map_id: ``osid.id.Id``

        """
        pass

    def deleted_map(self, map_id):
        """The callback for notification of deleted maps.

        :param map_id: the ``Id`` of the deleted ``Map``
        :type map_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_map(self, map_id, ancestor_id):
        """The callback for notifications of deleted map ancestors.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Map`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_map(self, map_id, descendant_id):
        """The callback for notifications of deleted map descendants.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Map`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


class ResourceLocationReceiver(osid_receivers.OsidReceiver):
    """The resource location receiver is the consumer supplied interface for receiving notifications pertaining to location changes of resources."""
    def entered_location(self, location_id, resource_id):
        """The callback for notifications of resources entering locations.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass

    def exited_location(self, route_id, resource_id):
        """The callback for notifications of resources exiting locations.

        :param route_id: the ``Id`` of the ``Location``
        :type route_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass

    def new_resource_coordinate(self, coordinate, resource_id):
        """The callback for notifications of resources changing coordinates.

        :param coordinate: the new coordinate
        :type coordinate: ``osid.mapping.Coordinate``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass


class ResourcePositionReceiver(osid_receivers.OsidReceiver):
    """The resource location receiver is the consumer supplied interface for receiving notifications pertaining to position changes of resources."""
    def moved_resource(self, resource_id, coordinate):
        """The callback for notifications of resources entering locations.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param coordinate: the ``Id`` of the ``Coordinate``
        :type coordinate: ``osid.mapping.Coordinate``

        """
        pass

    def entered_spatial_unit(self, resource_id, spatial_unit):
        """The callback for notifications of resources entering spatial units.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param spatial_unit: the ``Id`` of the ``SpatialUnit``
        :type spatial_unit: ``osid.mapping.SpatialUnit``

        """
        pass

    def exited_spatial_unit(self, resource_id, spatial_unit):
        """The callback for notifications of resources exiting spatial units.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param spatial_unit: the ``Id`` of the ``SpatialUnit``
        :type spatial_unit: ``osid.mapping.SpatialUnit``

        """
        pass


