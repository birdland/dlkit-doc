from ..osid import query_inspectors as osid_query_inspectors


class LocationQueryInspector(osid_query_inspectors.OsidObjectQueryInspector, osid_query_inspectors.OsidFederateableQueryInspector):
    """This is the query inspector for searching locations."""
    def get_coordinate_terms(self):
        """Gets the coordinate query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.CoordinateTerm``

        """
        return # osid.search.terms.CoordinateTerm

    coordinate_terms = property(fget=get_coordinate_terms)

    def get_contained_spatial_unit_terms(self):
        """Gets the contained spatial unit query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``

        """
        return # osid.search.terms.SpatialUnitTerm

    contained_spatial_unit_terms = property(fget=get_contained_spatial_unit_terms)

    def get_overlapping_spatial_unit_terms(self):
        """Gets the overlapping spatial unit query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``

        """
        return # osid.search.terms.SpatialUnitTerm

    overlapping_spatial_unit_terms = property(fget=get_overlapping_spatial_unit_terms)

    def get_spatial_unit_terms(self):
        """Gets the spatial unit query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.SpatialUnitTerm``

        """
        return # osid.search.terms.SpatialUnitTerm

    spatial_unit_terms = property(fget=get_spatial_unit_terms)

    def get_route_id_terms(self):
        """Gets the route ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    route_id_terms = property(fget=get_route_id_terms)

    def get_route_terms(self):
        """Gets the route query terms.

        :return: the query terms
        :rtype: ``osid.mapping.route.RouteQueryInspector``

        """
        return # osid.mapping.route.RouteQueryInspector

    route_terms = property(fget=get_route_terms)

    def get_path_id_terms(self):
        """Gets the path ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    path_id_terms = property(fget=get_path_id_terms)

    def get_path_terms(self):
        """Gets the path query terms.

        :return: the query terms
        :rtype: ``osid.mapping.path.PathQueryInspector``

        """
        return # osid.mapping.path.PathQueryInspector

    path_terms = property(fget=get_path_terms)

    def get_containing_location_id_terms(self):
        """Gets the containing location ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    containing_location_id_terms = property(fget=get_containing_location_id_terms)

    def get_containing_location_terms(self):
        """Gets the containing location query terms.

        :return: the query terms
        :rtype: ``osid.mapping.LocationQueryInspector``

        """
        return # osid.mapping.LocationQueryInspector

    containing_location_terms = property(fget=get_containing_location_terms)

    def get_contained_location_id_terms(self):
        """Gets the contained location ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    contained_location_id_terms = property(fget=get_contained_location_id_terms)

    def get_contained_location_terms(self):
        """Gets the contained location query terms.

        :return: the query terms
        :rtype: ``osid.mapping.LocationQueryInspector``

        """
        return # osid.mapping.LocationQueryInspector

    contained_location_terms = property(fget=get_contained_location_terms)

    def get_map_id_terms(self):
        """Gets the map ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    map_id_terms = property(fget=get_map_id_terms)

    def get_map_terms(self):
        """Gets the map query terms.

        :return: the query terms
        :rtype: ``osid.mapping.MapQueryInspector``

        """
        return # osid.mapping.MapQueryInspector

    map_terms = property(fget=get_map_terms)

    def get_location_query_inspector_record(self, location_record_type):
        """Gets the location query inspector record corresponding to the given ``Location`` record ``Type``.

        :param location_record_type: a location record type
        :type location_record_type: ``osid.type.Type``
        :return: the location query inspector record
        :rtype: ``osid.mapping.records.LocationQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_record_type)`` is ``false``

        """
        return # osid.mapping.records.LocationQueryInspectorRecord


class MapQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for searching maps."""
    def get_location_id_terms(self):
        """Gets the location ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    location_id_terms = property(fget=get_location_id_terms)

    def get_location_terms(self):
        """Gets the location query terms.

        :return: the query terms
        :rtype: ``osid.mapping.LocationQueryInspector``

        """
        return # osid.mapping.LocationQueryInspector

    location_terms = property(fget=get_location_terms)

    def get_path_id_terms(self):
        """Gets the path ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    path_id_terms = property(fget=get_path_id_terms)

    def get_path_terms(self):
        """Gets the path query terms.

        :return: the query terms
        :rtype: ``osid.mapping.path.PathQueryInspector``

        """
        return # osid.mapping.path.PathQueryInspector

    path_terms = property(fget=get_path_terms)

    def get_route_id_terms(self):
        """Gets the route ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    route_id_terms = property(fget=get_route_id_terms)

    def get_route_terms(self):
        """Gets the route query terms.

        :return: the query terms
        :rtype: ``osid.mapping.route.RouteQueryInspector``

        """
        return # osid.mapping.route.RouteQueryInspector

    route_terms = property(fget=get_route_terms)

    def get_ancestor_map_id_terms(self):
        """Gets the ancestor map ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_map_id_terms = property(fget=get_ancestor_map_id_terms)

    def get_ancestor_map_terms(self):
        """Gets the ancestor map query terms.

        :return: the query terms
        :rtype: ``osid.mapping.MapQueryInspector``

        """
        return # osid.mapping.MapQueryInspector

    ancestor_map_terms = property(fget=get_ancestor_map_terms)

    def get_descendant_map_id_terms(self):
        """Gets the descendant map ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_map_id_terms = property(fget=get_descendant_map_id_terms)

    def get_descendant_map_terms(self):
        """Gets the descendant map query terms.

        :return: the query terms
        :rtype: ``osid.mapping.MapQueryInspector``

        """
        return # osid.mapping.MapQueryInspector

    descendant_map_terms = property(fget=get_descendant_map_terms)

    def get_map_query_inspector_record(self, map_record_type):
        """Gets the record query inspector interface corresponding to the given ``Map`` record ``Type``.

        :param map_record_type: a map record type
        :type map_record_type: ``osid.type.Type``
        :return: the map query inspector record
        :rtype: ``osid.mapping.records.MapQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_record_type)`` is ``false``

        """
        return # osid.mapping.records.MapQueryInspectorRecord


