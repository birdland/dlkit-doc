from ..osid import search_orders as osid_search_orders


class LocationSearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidFederateableSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_distance(self, style):
        """Orders the results by distance.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def get_location_search_order_record(self, location_record_type):
        """Gets the location search order record corresponding to the given location record ``Type``.

        Multiple retrievals return the same underlying object.

        :param location_record_type: a location record type
        :type location_record_type: ``osid.type.Type``
        :return: the location search order record
        :rtype: ``osid.mapping.records.LocationSearchOrderRecord``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_record_type)`` is ``false``

        """
        return # osid.mapping.records.LocationSearchOrderRecord


class MapSearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_map_search_order_record(self, map_record_type):
        """Gets the map search order record corresponding to the given map ``Type``.

        Multiple retrievals return the same underlying object.

        :param map_record_type: a map record type
        :type map_record_type: ``osid.type.Type``
        :return: the map search order record
        :rtype: ``osid.mapping.records.MapSearchOrderRecord``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_record_type)`` is ``false``

        """
        return # osid.mapping.records.MapSearchOrderRecord


