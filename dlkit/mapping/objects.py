from ..osid import objects as osid_objects
from ..osid import markers as osid_markers


class Location(osid_objects.OsidObject, osid_markers.Federateable):
    """A ``Location`` represents a location in a ``Map``."""
    def has_spatial_unit(self):
        """Tests if a spatial unit is available for this location.

        :return: ``true`` if a spatial unit is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_spatial_unit(self):
        """Gets the spatial unit corresponding to this location.

        :return: the spatial unit for this location
        :rtype: ``osid.mapping.SpatialUnit``
        :raise: ``IllegalState`` -- ``has_spatial_unit()`` is ``false``

        """
        return # osid.mapping.SpatialUnit

    spatial_unit = property(fget=get_spatial_unit)

    def get_location_record(self, location_record_type):
        """Gets the location record corresponding to the given ``Location`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.. The ``location_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(location_record_type)`` is ``true`` .

        :param location_record_type: the type of location record to retrieve
        :type location_record_type: ``osid.type.Type``
        :return: the location record
        :rtype: ``osid.mapping.records.LocationRecord``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_record_type)`` is ``false``

        """
        return # osid.mapping.records.LocationRecord


class LocationForm(osid_objects.OsidObjectForm, osid_objects.OsidFederateableForm):
    """This is the form for creating and updating ``Locations``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``LocationAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_spatial_unit_metadata(self):
        """Gets the metadata for a spatial unit.

        :return: metadata for the spatial unit
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    spatial_unit_metadata = property(fget=get_spatial_unit_metadata)

    def set_spatial_unit(self, spatial_unit):
        """Sets the spatial unit.

        :param spatial_unit: the new spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``InvalidArgument`` -- ``spatial_unit`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``Unsupported`` -- ``spatial_unit`` type is not supported

        """
        pass

    def clear_spatial_unit(self):
        """Removes the spatial unit.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` is ``true`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    spatial_unit = property(fset=set_spatial_unit, fdel=clear_spatial_unit)

    def get_location_form_record(self, location_record_type):
        """Gets the ``LocationFormRecord`` corresponding to the given location record ``Type``.

        :param location_record_type: a location record type
        :type location_record_type: ``osid.type.Type``
        :return: the location form record
        :rtype: ``osid.mapping.records.LocationFormRecord``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(location_record_type)`` is ``false``

        """
        return # osid.mapping.records.LocationFormRecord


class LocationList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LocationList`` provides a means for accessing ``Location`` elements sequentially either one at a time or many at a time.

    Examples: while (ll.hasNext()) { Location location =
    ll.getNextLocation(); }

    or
      while (ll.hasNext()) {
           Location[] locations = ll.getNextLocations(ll.available());
      }
    


    """
    def get_next_location(self):
        """Gets the next ``Location`` in this list.

        :return: the next ``Location`` in this list. The ``has_next()`` method should be used to test that a next ``Location`` is available before calling this method.
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Location

    next_location = property(fget=get_next_location)

    def get_next_locations(self, n):
        """Gets the next set of ``Location`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Location`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Location`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Location


class LocationNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``LocationHierarchySession``.

    """
    def get_location(self):
        """Gets the ``Location`` at this node.

        :return: the location represented by this node
        :rtype: ``osid.mapping.Location``

        """
        return # osid.mapping.Location

    location = property(fget=get_location)

    def get_parent_location_nodes(self):
        """Gets the parents of this location.

        :return: the parents of the ``id``
        :rtype: ``osid.mapping.LocationNodeList``

        """
        return # osid.mapping.LocationNodeList

    parent_location_nodes = property(fget=get_parent_location_nodes)

    def get_child_location_nodes(self):
        """Gets the children of this location.

        :return: the children of this location
        :rtype: ``osid.mapping.LocationNodeList``

        """
        return # osid.mapping.LocationNodeList

    child_location_nodes = property(fget=get_child_location_nodes)


class LocationNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``LocationNodeList`` provides a means for accessing ``LocationNode`` elements sequentially either one at a time or many at a time.

    Examples: while (lnl.hasNext()) { LocationNode locationNode =
    lnl.getNextLocationNode(); }

    or
      while (lnl.hasNext()) {
           LocationNode[] locationNodes = lnl.getNextLocationNodes(lnl.available());
      }
    


    """
    def get_next_location_node(self):
        """Gets the next ``LocationNode`` in this list.

        :return: the next ``LocationNode`` in this list. The ``has_next()`` method should be used to test that a next ``LocationNode`` is available before calling this method.
        :rtype: ``osid.mapping.LocationNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.LocationNode

    next_location_node = property(fget=get_next_location_node)

    def get_next_location_nodes(self, n):
        """Gets the next set of ``LocationNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``LocationNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``LocationNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.mapping.LocationNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.LocationNode


class Map(osid_objects.OsidCatalog):
    """A ``Map`` represents a collection of locations and paths."""
    def get_map_record(self, map_record_type):
        """Gets the map record corresponding to the given ``Map`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``map_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(map_record_type)`` is
        ``true`` .

        :param map_record_type: the type of map record to retrieve
        :type map_record_type: ``osid.type.Type``
        :return: the map record
        :rtype: ``osid.mapping.records.MapRecord``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_record_type)`` is ``false``

        """
        return # osid.mapping.records.MapRecord


class MapForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating maps.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the ``MapAdminSession``.
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """
    def get_map_form_record(self, map_record_type):
        """Gets the ``MapFormRecord`` interface corresponding to the given map record interface ``Type``.

        :param map_record_type: a map record type
        :type map_record_type: ``osid.type.Type``
        :return: the map form record
        :rtype: ``osid.mapping.records.MapFormRecord``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(map_record_type)`` is ``false``

        """
        return # osid.mapping.records.MapFormRecord


class MapList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``MapList`` provides a means for accessing ``Map`` elements sequentially either one at a time or many at a time.

    Examples: while (ml.hasNext()) { Map map = ml.getNextMap(); }

    or
      while (ml.hasNext()) {
           Map[] maps = ml.getNextMaps(ml.available());
      }
    


    """
    def get_next_map(self):
        """Gets the next ``Map`` in this list.

        :return: the next ``Map`` in this list. The ``has_next()`` method should be used to test that a next ``Map`` is available before calling this method.
        :rtype: ``osid.mapping.Map``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Map

    next_map = property(fget=get_next_map)

    def get_next_maps(self, n):
        """Gets the next set of ``Map`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Map`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Map`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.mapping.Map``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Map


class MapNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``MapHierarchySession``.

    """
    def get_map(self):
        """Gets the ``Map`` at this node.

        :return: the map represented by this node
        :rtype: ``osid.mapping.Map``

        """
        return # osid.mapping.Map

    map = property(fget=get_map)

    def get_parent_map_nodes(self):
        """Gets the parents of this map.

        :return: the parents of this map
        :rtype: ``osid.mapping.MapNodeList``

        """
        return # osid.mapping.MapNodeList

    parent_map_nodes = property(fget=get_parent_map_nodes)

    def get_child_map_nodes(self):
        """Gets the children of this map.

        :return: the children of this map
        :rtype: ``osid.mapping.MapNodeList``

        """
        return # osid.mapping.MapNodeList

    child_map_nodes = property(fget=get_child_map_nodes)


class MapNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``MapNodeList`` provides a means for accessing ``MapNode`` elements sequentially either one at a time or many at a time.

    Examples: while (mnl.hasNext()) { MapNode node =
    mnl.getNextMapNode(Node); }

    or
      while (mnl.hasNext()) {
           MapNode[] nodes = ml.getNextMapNodes(mnl.available());
      }
    


    """
    def get_next_map_node(self):
        """Gets the next ``MapNode`` in this list.

        :return: the next ``MapNode`` in this list. The ``has_next()`` method should be used to test that a next ``MapNode`` is available before calling this method.
        :rtype: ``osid.mapping.MapNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.MapNode

    next_map_node = property(fget=get_next_map_node)

    def get_next_map_nodes(self, n):
        """Gets the next set of ``MapNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``MapNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``MapNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.mapping.MapNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.MapNode


class ResourceLocationList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ResourceLocationList`` provides a means for accessing ``ResourceLocation`` elements sequentially either one at a time or many at a time.

    Examples: while (rll.hasNext()) { ResourceLocation location =
    rll.getNextRouteResourceLocation(); }

    or
      while (rll.hasNext()) {
           ResourceLocation[] locations = rll.getNextResourceLocations(rll.available());
      }
    


    """
    def get_next_resource_location(self):
        """Gets the next ``ResourceLocation`` in this list.

        :return: the next ``ResourceLocation`` in this list. The ``has_next()`` method should be used to test that a next ``ResourceLocation`` is available before calling this method.
        :rtype: ``osid.mapping.ResourceLocation``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.ResourceLocation

    next_resource_location = property(fget=get_next_resource_location)

    def get_next_resource_locations(self, n):
        """Gets the next set of ``ResourceLocation`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``ResourceLocation`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ResourceLocation`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.mapping.ResourceLocation``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.ResourceLocation


class CoordinateList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CoordinateList`` provides a means for accessing ``Coordinate`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Coordinate coordinate =
    cl.getNextCoordinate(); }

    or
      while (cl.hasNext()) {
           Coordinate[] coordinates = cl.getNextCoordinates(cl.available());
      }
    


    """
    def get_next_coordinate(self):
        """Gets the next ``Coordinate`` in this list.

        :return: the next ``Coordinate`` in this list. The ``has_next()`` method should be used to test that a next ``Coordinate`` is available before calling this method.
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Coordinate

    next_coordinate = property(fget=get_next_coordinate)

    def get_next_coordinates(self, n):
        """Gets the next set of ``Coordinate`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Coordinate`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Coordinate`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Coordinate


class SpatialUnitList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``SpatialUnitList`` provides a means for accessing ``SpatialUnit`` elements sequentially either one at a time or many at a time.

    Examples: while (sul.hasNext()) { SpatialUnit unit =
    sul.getNextSpatialUnit(); }

    or
      while (sul.hasNext()) {
           SpatialUnit[] units = sul.getNextSpatialUnits(sul.available());
      }
    


    """
    def get_next_spatial_unit(self):
        """Gets the next ``SpatialUnit`` in this list.

        :return: the next ``SpatialUnit`` in this list. The ``has_next()`` method should be used to test that a next ``SpatialUnit`` is available before calling this method.
        :rtype: ``osid.mapping.SpatialUnit``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.SpatialUnit

    next_spatial_unit = property(fget=get_next_spatial_unit)

    def get_next_spatial_units(self, n):
        """Gets the next set of ``SpatialUnit`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``SpatialUnit`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``SpatialUnit`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.mapping.SpatialUnit``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.SpatialUnit

