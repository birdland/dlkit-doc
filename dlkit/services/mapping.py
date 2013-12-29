# -*- coding: utf-8 -*-
"""Mapping Open Service Interface Definitions
mapping version 3.0.0

The Mapping OSID provides a means for managing inventories of places and
performing a variety of mapping operations.

Locations

One aspect of the Mapping OSID provides references to location places
used in other OSIDs. A ``Location`` may include a spatial coordinate or
defined boundary described in a ``SpatialUnit``. Additional sessions
provide a means to easily look up locations by ``Coordinate`` or
arbitrary ``SpatialUnit`` as well as to traverse locations through
lookups of adjacent ``Locations``.

``Locations`` may be structured in hierarchies to convey hierarchical
relationships. A room may be located inside a building, within a city
within a state.

Primitives

The data interfaces for ``Coordinates`` and ``SpatialUnits`` are defined
through their respective ``Types`` to allow for any kind of coordinate
or spatial system. A definition for distance resolution is also provided
to capture an extremely wide array of unit values. ``Distance,``
``Coordinate,``  ``Heading,`` and ``SpatialUnit`` appear to the OSID as
complex primitive interfaces which are constructed by the consumer in
order to fulfill the interface contracts. It is required that the
consumer and provider agree on the coordinate domain and spatial unit
types through testing of the ``Type`` support.

Resource Tracking

``Resources`` may be tracked spatially. Sessions are available to query
and place ``Resources`` at specific ``Locations`` and ``Coordinates,``
and receive notifications to changes in their locations.

Map Cataloging

``Locations`` may be organuzed in hierarchical ``Maps`` that offer a
means of federation or layering of map data.

Sub Packages

The Mapping OSID includes a Mapping Route OSID for creating and
navigating Routes, a Mapping Path OSID for querying and designing
physical ``Paths`` and a Mapping Batch OSID for managing locations in
bulk.

"""
from . import osid
from .osid_errors import Unimplemented, IllegalState, OperationFailed


class MappingProfile(osid.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any map federation is exposed.
        Federation is exposed when a specific map may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of maps appears as a single
        map.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_lookup(self):
        """Tests if looking up locations is supported.

        :return: ``true`` if location lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_query(self):
        """Tests if querying locations is supported.

        :return: ``true`` if location query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_search(self):
        """Tests if searching locations is supported.

        :return: ``true`` if location search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_admin(self):
        """Tests if locationadministrative service is supported.

        :return: ``true`` if location administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_notification(self):
        """Tests if a locationnotification service is supported.

        :return: ``true`` if location notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_hierarchy(self):
        """Tests if a locationhierarchy service is supported.

        :return: ``true`` if location hierarchy is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_hierarchy_design(self):
        """Tests if a location hierarchy design service is supported.

        :return: ``true`` if location hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_map(self):
        """Tests if a location map lookup service is supported.

        :return: ``true`` if a location map lookup service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_map_assignment(self):
        """Tests if a location map assignment service is supported.

        :return: ``true`` if a location to map assignment service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_smart_map(self):
        """Tests if a location smart map service is supported.

        :return: ``true`` if a location smart map service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_adjacency(self):
        """Tests if a location adjacency service is supported.

        :return: ``true`` if a location adjacency service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_location_spatial(self):
        """Tests if a location spatial service is supported.

        :return: ``true`` if a location spatial service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_location(self):
        """Tests if a resource location service is supported.

        :return: ``true`` if a resource location service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_location_update(self):
        """Tests if a resource location update service is supported.

        :return: ``true`` if a resource location update service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_location_notification(self):
        """Tests if a resource location notification service is supported.

        :return: ``true`` if a resource location notification service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_resource_position_notification(self):
        """Tests if a resource position notification service is supported.

        :return: ``true`` if a resource position notification service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_my_location(self):
        """Tests if a location service is supported for the current agent.

        :return: ``true`` if my location is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_map_lookup(self):
        """Tests if looking up maps is supported.

        :return: ``true`` if map lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_map_query(self):
        """Tests if querying maps is supported.

        :return: ``true`` if a map query service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_map_search(self):
        """Tests if searching maps is supported.

        :return: ``true`` if map search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_map_admin(self):
        """Tests if map administrative service is supported.

        :return: ``true`` if map administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_map_notification(self):
        """Tests if a mapnotification service is supported.

        :return: ``true`` if map notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_map_hierarchy(self):
        """Tests for the availability of a map hierarchy traversal service.

        :return: ``true`` if map hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_map_hierarchy_design(self):
        """Tests for the availability of a map hierarchy design service.

        :return: ``true`` if map hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_mapping_batch(self):
        """Tests if the mapping batch service is supported.

        :return: ``true`` if maping batch service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_mapping_path(self):
        """Tests if the mapping path service is supported.

        :return: ``true`` if maping path service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_mapping_route(self):
        """Tests if the mapping route service is supported.

        :return: ``true`` if maping route service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_location_record_types(self):
        """Gets the supported ``Location`` record types.

        :return: a list containing the supported ``Location`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    location_record_types = property(fget=get_location_record_types)

    def supports_location_record_type(self, location_record_type):
        """Tests if the given ``Location`` record type is supported.

        :param location_record_type: a ``Type`` indicating a ``Location`` record type
        :type location_record_type: ``osid.type.Type``
        :return: ``true`` if the given record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_location_search_record_types(self):
        """Gets the supported ``Location`` search types.

        :return: a list containing the supported ``Location`` search types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    location_search_record_types = property(fget=get_location_search_record_types)

    def supports_location_search_record_type(self, location_search_record_type):
        """Tests if the given ``Location`` search type is supported.

        :param location_search_record_type: a ``Type`` indicating a ``Location`` search type
        :type location_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``location_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_map_record_types(self):
        """Gets the supported ``Map`` record types.

        :return: a list containing the supported ``Map`` types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    map_record_types = property(fget=get_map_record_types)

    def supports_map_record_type(self, map_record_type):
        """Tests if the given ``Map`` record type is supported.

        :param map_record_type: a ``Type`` indicating a ``Map`` record type
        :type map_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_map_search_record_types(self):
        """Gets the supported ``Map`` search record types.

        :return: a list containing the supported ``Map`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    map_search_record_types = property(fget=get_map_search_record_types)

    def supports_map_search_record_type(self, map_search_record_type):
        """Tests if the given ``Map`` search record type is supported.

        :param map_search_record_type: a ``Type`` indicating a ``Map`` search record type
        :type map_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``map_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_record_types(self):
        """Gets the supported ``ResourceLocation`` record types.

        :return: a list containing the supported ``ResourceLocation`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    resource_location_record_types = property(fget=get_resource_location_record_types)

    def supports_resource_location_record_type(self, resource_location_record_type):
        """Tests if the given ``ResourceLocationRecord`` record type is supported.

        :param resource_location_record_type: a ``Type`` indicating a ``ResourceLocation`` type
        :type resource_location_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_location_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_types(self):
        """Gets the supported ``Coordinate`` types.

        :return: a list containing the supported ``Coordinate`` types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    coordinate_types = property(fget=get_coordinate_types)

    def supports_coordinate_type(self, coordinate_type):
        """Tests if the given ``Coordinate`` type is supported.

        :param coordinate_type: a ``Type`` indicating a ``Coordinate`` type
        :type coordinate_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_heading_types(self):
        """Gets the supported ``Heading`` types.

        :return: a list containing the supported ``Heading`` types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    heading_types = property(fget=get_heading_types)

    def supports_heading_type(self, heading_type):
        """Tests if the given ``Heading`` type is supported.

        :param heading_type: a ``Type`` indicating a ``Heading`` type
        :type heading_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``heading_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_spatial_unit_record_types(self):
        """Gets the supported ``SpatialUnit`` record types.

        :return: a list containing the supported ``SpatialUnit`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    def supports_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if the given ``SpatialUnit`` record type is supported.

        :param spatial_unit_record_type: a ``Type`` indicating a ``SpatialUnit`` record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class MappingManager(osid.OsidManager, osid.OsidSession, MappingProfile):

    def get_location_lookup_session(self):
        """Gets the ``OsidSession`` associated with the location lookup service.

        :return: a ``LocationLookupSession``
        :rtype: ``osid.mapping.LocationLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_lookup_session = property(fget=get_location_lookup_session)

    def get_location_lookup_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location lookup service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :return: a ``LocationLookupSession``
        :rtype: ``osid.mapping.LocationLookupSession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_query_session(self):
        """Gets the ``OsidSession`` associated with the location query service.

        :return: a ``LocationQuerySession``
        :rtype: ``osid.mapping.LocationQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_query_session = property(fget=get_location_query_session)

    def get_location_query_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location query service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationQuerySession``
        :rtype: ``osid.mapping.LocationQuerySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_search_session(self):
        """Gets the ``OsidSession`` associated with the location search service.

        :return: a ``LocationSearchSession``
        :rtype: ``osid.mapping.LocationSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_search_session = property(fget=get_location_search_session)

    def get_location_search_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location search service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationSearchSession``
        :rtype: ``osid.mapping.LocationSearchSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_admin_session(self):
        """Gets the ``OsidSession`` associated with the location administration service.

        :return: a ``LocationAdminSession``
        :rtype: ``osid.mapping.LocationAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_admin_session = property(fget=get_location_admin_session)

    def get_location_admin_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location administration service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationAdminSession``
        :rtype: ``osid.mapping.LocationAdminSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_notification_session(self, location_receiver):
        """Gets the ``OsidSession`` associated with the location notification service.

        :param location_receiver: the notification callback
        :type location_receiver: ``osid.mapping.LocationReceiver``
        :return: a ``LocationNotificationSession``
        :rtype: ``osid.mapping.LocationNotificationSession``
        :raise: ``NullArgument`` -- ``location_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_notification_session_for_map(self, location_receiver, map_id):
        """Gets the ``OsidSession`` associated with the location notification service for the given map.

        :param location_receiver: the notification callback
        :type location_receiver: ``osid.mapping.LocationReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationNotificationSession``
        :rtype: ``osid.mapping.LocationNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``location_receiver`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the location hierarchy service.

        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_hierarchy_session = property(fget=get_location_hierarchy_session)

    def get_location_hierarchy_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location hierarchy service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the location hierarchy design service.

        :return: a ``LocationHierarchyDesignSession``
        :rtype: ``osid.mapping.LocationHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_hierarchy_design_session = property(fget=get_location_hierarchy_design_session)

    def get_location_hierarchy_design_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location hierarchy design service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchyDesignSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_map_session(self):
        """Gets the ``OsidSession`` to lookup location/map mappings.

        :return: a ``LocationMapSession``
        :rtype: ``osid.mapping.LocationMapSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_map()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_map_session = property(fget=get_location_map_session)

    def get_location_map_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning locations to maps.

        :return: a ``LocationMapAssignmentSession``
        :rtype: ``osid.mapping.LocationMapAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_map_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_map_assignment_session = property(fget=get_location_map_assignment_session)

    def get_location_smart_map_session(self, map_id):
        """Gets the ``OsidSession`` to manage locatin smart maps.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationSmartMapSession``
        :rtype: ``osid.mapping.LocationSmartMapSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_smart_map()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_adjacency_session(self):
        """Gets the ``OsidSession`` associated with the location adjacency service.

        :return: a ``LocationAdjacencySession``
        :rtype: ``osid.mapping.LocationAdjacencySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_adjacency()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_adjacency_session = property(fget=get_location_adjacency_session)

    def get_location_adjacency_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location adjacency service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationAdjacencySession``
        :rtype: ``osid.mapping.LocationAdjacencySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_adjacency()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_spatial_session(self):
        """Gets the ``OsidSession`` associated with the location spatial service.

        :return: a ``LocationSpatialSession``
        :rtype: ``osid.mapping.LocationSpatialSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_spatial()`` is ``false``

        """
        raise UNIMPLEMENTED()

    location_spatial_session = property(fget=get_location_spatial_session)

    def get_location_spatial_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the location spatial service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``LocationSpatialSession``
        :rtype: ``osid.mapping.LocationSpatialSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_spatial()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_session(self):
        """Gets the ``OsidSession`` associated with the resource location service.

        :return: a ``ResourceLocationSession``
        :rtype: ``osid.mapping.ResourceLocationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_location_session = property(fget=get_resource_location_session)

    def get_resource_location_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the resource location service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``ResourceLocationSession``
        :rtype: ``osid.mapping.ResourceLocationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_update_session(self):
        """Gets the ``OsidSession`` associated with the resource location update service.

        :return: a ``ResourceLocationUpdateSession``
        :rtype: ``osid.mapping.ResourceLocationUpdateSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_update()`` is ``false``

        """
        raise UNIMPLEMENTED()

    resource_location_update_session = property(fget=get_resource_location_update_session)

    def get_resource_location_update_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the resource location update service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``ResourceLocationUpdateSession``
        :rtype: ``osid.mapping.ResourceLocationUpdateSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_update()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_notification_session(self, resource_location_receiver):
        """Gets the ``OsidSession`` associated with the resource location notification service.

        :param resource_location_receiver: the notification callback
        :type resource_location_receiver: ``osid.mapping.ResourceLocationReceiver``
        :return: a ``ResourceLocationNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NullArgument`` -- ``resource_location_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_notification_session_for_map(self, resource_location_receiver, map_id):
        """Gets the ``OsidSession`` associated with the resource location notification service for the given map.

        :param resource_location_receiver: the notification callback
        :type resource_location_receiver: ``osid.mapping.ResourceLocationReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``ResourceLocationNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_location_receiver`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_position_notification_session(self, resource_position_receiver):
        """Gets the ``OsidSession`` associated with the resource position notification service.

        :param resource_position_receiver: the notification callback
        :type resource_position_receiver: ``osid.mapping.ResourcePositionReceiver``
        :return: a ``ResourcePositionNotificationSession``
        :rtype: ``osid.mapping.ResourcePositionNotificationSession``
        :raise: ``NullArgument`` -- ``resource_position_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_position_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_position_notification_session_for_map(self, resource_position_receiver, map_id):
        """Gets the ``OsidSession`` associated with the resource position notification service for the given map.

        :param resource_position_receiver: the notification callback
        :type resource_position_receiver: ``osid.mapping.ResourcePositionReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: a ``ResourcePositionNotificationSession``
        :rtype: ``osid.mapping.ResourcePositionNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_position_receiver`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_position_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_my_location_session(self):
        """Gets the ``OsidSession`` associated with the my location service.

        :return: a ``MyLocationLookupSession``
        :rtype: ``osid.mapping.MyLocationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_location_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    my_location_session = property(fget=get_my_location_session)

    def get_my_location_session_for_map(self, map_id):
        """Gets the ``OsidSession`` associated with the my location service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :return: a ``MyLocationLookupSession``
        :rtype: ``osid.mapping.MyLocationSession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_location_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_lookup_session(self):
        """Gets the ``OsidSession`` associated with the map lookup service.

        :return: a ``MapLookupSession``
        :rtype: ``osid.mapping.MapLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    map_lookup_session = property(fget=get_map_lookup_session)

    def get_map_query_session(self):
        """Gets the ``OsidSession`` associated with the map query service.

        :return: a ``MapQuerySession``
        :rtype: ``osid.mapping.MapQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    map_query_session = property(fget=get_map_query_session)

    def get_map_search_session(self):
        """Gets the ``OsidSession`` associated with the map search service.

        :return: a ``MapSearchSession``
        :rtype: ``osid.mapping.MapSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    map_search_session = property(fget=get_map_search_session)

    def get_map_admin_session(self):
        """Gets the ``OsidSession`` associated with the map administrative service.

        :return: a ``MapAdminSession``
        :rtype: ``osid.mapping.MapAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    map_admin_session = property(fget=get_map_admin_session)

    def get_map_notification_session(self, map_receiver):
        """Gets the ``OsidSession`` associated with the map notification service.

        :param map_receiver: the notification callback
        :type map_receiver: ``osid.mapping.MapReceiver``
        :return: a ``MapNotificationSession``
        :rtype: ``osid.mapping.MapNotificationSession``
        :raise: ``NullArgument`` -- ``map_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the map hierarchy service.

        :return: a ``MapHierarchySession`` for maps
        :rtype: ``osid.mapping.MapHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    map_hierarchy_session = property(fget=get_map_hierarchy_session)

    def get_map_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the map hierarchy design service.

        :return: a ``HierarchyDesignSession`` for maps
        :rtype: ``osid.mapping.MapHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    map_hierarchy_design_session = property(fget=get_map_hierarchy_design_session)

    def get_mapping_batch_manager(self):
        """Gets the mapping batch manager.

        :return: a ``MappingBatchManager`` for paths
        :rtype: ``osid.mapping.batch.MappingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    mapping_batch_manager = property(fget=get_mapping_batch_manager)

    def get_mapping_path_manager(self):
        """Gets the mapping path manager.

        :return: a ``MappingPathManager`` for paths
        :rtype: ``osid.mapping.path.MappingPathManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_path()`` is ``false``

        """
        raise UNIMPLEMENTED()

    mapping_path_manager = property(fget=get_mapping_path_manager)

    def get_mapping_route_manager(self):
        """Gets the mapping route manager.

        :return: a ``MappingRouteManager`` for routes
        :rtype: ``osid.mapping.route.MappingRouteManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_route()`` is ``false``

        """
        raise UNIMPLEMENTED()

    mapping_route_manager = property(fget=get_mapping_route_manager)


##
# The following methods are from osid.mapping.MapLookupSession

    def can_lookup_maps(self):
        """Tests if this user can perform ``Map`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_map_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_map_view(self):
        """A complete view of the ``Map`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_map(self, map_id):
        """Gets the ``Map`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Map`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Map`` and retained for compatibility.

        :param map_id: ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_maps_by_ids(self, map_ids):
        """Gets a ``MapList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the maps
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Maps`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param map_ids: the list of ``Ids`` to retrieve
        :type map_ids: ``osid.id.IdList``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``map_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_maps_by_genus_type(self, map_genus_type):
        """Gets a ``MapList`` corresponding to the given map genus ``Type`` which does not include maps of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :param map_genus_type: a map genus type
        :type map_genus_type: ``osid.type.Type``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``map_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_maps_by_parent_genus_type(self, map_genus_type):
        """Gets a ``MapList`` corresponding to the given map genus ``Type`` and include any additional maps with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :param map_genus_type: a map genus type
        :type map_genus_type: ``osid.type.Type``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``map_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_maps_by_record_type(self, map_record_type):
        """Gets a ``MapList`` containing the given map record ``Type``.
        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :param map_record_type: a map record type
        :type map_record_type: ``osid.type.Type``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``map_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_maps_by_provider(self, resource_id):
        """Gets a ``MapList`` for the given provider.
        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Map`` list
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_maps(self):
        """Gets all ``Maps``.
        In plenary mode, the returned list contains all known maps or an
        error results. Otherwise, the returned list may contain only
        those maps that are accessible through this session.

        :return: a list of ``Maps``
        :rtype: ``osid.mapping.MapList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    maps = property(fget=get_maps)


##
# The following methods are from osid.mapping.MapQuerySession

    def can_search_maps(self):
        """Tests if this user can perform ``Map`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_map_query(self):
        """Gets a map query.

        :return: the map query
        :rtype: ``osid.mapping.MapQuery``

        """
        raise UNIMPLEMENTED()

    map_query = property(fget=get_map_query)

    def get_maps_by_query(self, map_query):
        """Gets a list of ``Maps`` matching the given map query.

        :param map_query: the map query
        :type map_query: ``osid.mapping.MapQuery``
        :return: the returned ``MapList``
        :rtype: ``osid.mapping.MapList``
        :raise: ``NullArgument`` -- ``map_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``map_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.MapSearchSession

    def get_map_search(self):
        """Gets a map search.

        :return: the map search
        :rtype: ``osid.mapping.MapSearch``

        """
        raise UNIMPLEMENTED()

    map_search = property(fget=get_map_search)

    def get_map_search_order(self):
        """Gets a map search order.
        The ``MapSearchOrder`` is supplied to a ``MapSearch`` to specify
        the ordering of results.

        :return: the map search order
        :rtype: ``osid.mapping.MapSearchOrder``

        """
        raise UNIMPLEMENTED()

    map_search_order = property(fget=get_map_search_order)

    def get_maps_by_search(self, map_query, map_search):
        """Gets the search results matching the given search query using the given search.

        :param map_query: the map query
        :type map_query: ``osid.mapping.MapQuery``
        :param map_search: the map search
        :type map_search: ``osid.mapping.MapSearch``
        :return: the returned search results
        :rtype: ``osid.mapping.MapSearchResults``
        :raise: ``NullArgument`` -- ``map_query`` or ``map_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``map_query`` or ``map_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_map_query_from_inspector(self, map_query_inspector):
        """Gets a map query from an inspector.
        The inspector is available from a ``MapSearchResults``.

        :param map_query_inspector: a map query inspector
        :type map_query_inspector: ``osid.mapping.MapQueryInspector``
        :return: the map query
        :rtype: ``osid.mapping.MapQuery``
        :raise: ``NullArgument`` -- ``map_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``map_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.MapAdminSession

    def can_create_maps(self):
        """Tests if this user can create ``Maps``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Map``.
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Map`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_map_with_record_types(self, map_record_types):
        """Tests if this user can create a single ``Map`` using the desired record types.
        While ``MappingManager.getMapRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Map``.
        Providing an empty array tests if a ``Map`` can be created with
        no records.

        :param map_record_types: array of map record types
        :type map_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Map`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``map_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_map_form_for_create(self, map_record_types):
        """Gets the map form for creating new maps.
        A new form should be requested for each create transaction.

        :param map_record_types: array of map record types
        :type map_record_types: ``osid.type.Type[]``
        :return: the map form
        :rtype: ``osid.mapping.MapForm``
        :raise: ``NullArgument`` -- ``map_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get a form with given record types

        """
        raise UNIMPLEMENTED()

    def create_map(self, map_form):
        """Creates a new ``Map``.

        :param map_form: the form for this ``Map``
        :type map_form: ``osid.mapping.MapForm``
        :return: the new ``Map``
        :rtype: ``osid.mapping.Map``
        :raise: ``IllegalState`` -- ``map_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``map_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``map_form`` did not originate from ``get_map_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_maps(self):
        """Tests if this user can update ``Maps``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Map``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Map`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_map_form_for_update(self, map_id):
        """Gets the map form for updating an existing map.
        A new map form should be requested for each update transaction.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: the map form
        :rtype: ``osid.mapping.MapForm``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_map(self, map_form):
        """Updates an existing map.

        :param map_form: the form containing the elements to be updated
        :type map_form: ``osid.mapping.MapForm``
        :raise: ``IllegalState`` -- ``map_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``map_id`` or ``map_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``map_form`` did not originate from ``get_map_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_maps(self):
        """Tests if this user can delete ``Maps``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Map``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Map`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_map(self, map_id):
        """Deletes a ``Map``.

        :param map_id: the ``Id`` of the ``Map`` to remove
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_map_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Maps``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Map`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_map(self, map_id, alias_id):
        """Adds an ``Id`` to a ``Map`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Map`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another map, it is reassigned to the
        given map ``Id``.

        :param map_id: the ``Id`` of a ``Map``
        :type map_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.MapNotificationSession

    def can_register_for_map_notifications(self):
        """Tests if this user can register for ``Map`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_maps(self):
        """Register for notifications of new maps.
        ``MapReceiver.newMap()`` is invoked when a new ``Map`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_map_ancestors(self, map_id):
        """Registers for notification if an ancestor is added to the specified map in the map hierarchy.
        ``MapReceiver.newMapAncestor()`` is invoked when the specified
        map experiences an addition in ancestry.

        :param map_id: the ``Id`` of the map to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_map_descendants(self, map_id):
        """Registers for notification if a descendant is added to the specified map in the map hierarchy.
        ``MapReceiver.newMapDescendant()`` is invoked when the specified
        map experiences an addition in descendants.

        :param map_id: the ``Id`` of the map to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_maps(self):
        """Registers for notification of updated maps.
        ``MapReceiver.changedMap()`` is invoked when a map is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_map(self, map_id):
        """Registers for notification of an updated map.
        ``MapReceiver.changedMap()`` is invoked when the specified map
        is changed.

        :param map_id: the Id of the ``Map`` to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``E``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_maps(self):
        """Registers for notification of deleted maps.
        ``MapReceiver.deletedMap()`` is invoked when a map is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_map(self, map_id):
        """Registers for notification of a deleted map.
        ``MapReceiver.deletedMap()`` is invoked when the specified map
        is deleted.

        :param map_id: the ``Id`` of the ``Map`` to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_map_ancestors(self, map_id):
        """Registers for notification if an ancestor is removed from the specified map in the map hierarchy.
        ``MapReceiver.deletedMapAncestor()`` is invoked when the
        specified map experiences a removal of an ancestor.

        :param map_id: the ``Id`` of the map to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_map_descendants(self, map_id):
        """Registers for notification if a descendant is removed from fthe specified map in the map hierarchy.
        ``MapReceiver.deletedMapDescednant()`` is invoked when the
        specified map experiences a removal of one of its descdendents.

        :param map_id: the ``Id`` of the map to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.MapHierarchySession

    def get_map_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    map_hierarchy_id = property(fget=get_map_hierarchy_id)

    def get_map_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    map_hierarchy = property(fget=get_map_hierarchy)

    def can_access_map_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_map_ids(self):
        """Gets the root map ``Ids`` in this hierarchy.

        :return: the root map ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_map_ids = property(fget=get_root_map_ids)

    def get_root_maps(self):
        """Gets the root map in the map hierarchy.
        A location with no parents is an orphan. While all map ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root location or child of
        another location.

        :return: the root maps
        :rtype: ``osid.mapping.MapList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_maps = property(fget=get_root_maps)

    def has_parent_maps(self, map_id):
        """Tests if the ``Map`` has any parents.

        :param map_id: a map ``Id``
        :type map_id: ``osid.id.Id``
        :return: ``true`` if the map has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_map(self, id_, map_id):
        """Tests if an ``Id`` is a direct parent of map.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``map_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_map_ids(self, map_id):
        """Gets the parent ``Ids`` of the given map.

        :param map_id: a map ``Id``
        :type map_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the map
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_maps(self, map_id):
        """Gets the parents of the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :return: the parents of the map
        :rtype: ``osid.mapping.MapList``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_map(self, id_, map_id):
        """Tests if an ``Id`` is an ancestor of a map.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``map_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_maps(self, map_id):
        """Tests if a map has any children.

        :param map_id: a map ``Id``
        :type map_id: ``osid.id.Id``
        :return: ``true`` if the ``map_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_map(self, id_, map_id):
        """Tests if a map is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``map_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_map_ids(self, map_id):
        """Gets the child ``Ids`` of the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :return: the children of the map
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_maps(self, map_id):
        """Gets the children of the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :return: the children of the map
        :rtype: ``osid.mapping.MapList``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_map(self, id_, map_id):
        """Tests if an ``Id`` is a descendant of a map.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``map_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_map_node_ids(self, map_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the location.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the location.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given location, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a map node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_map_nodes(self, map_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given map.

        :param map_id: the ``Id`` to query
        :type map_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the location.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the location.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given location, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a map node
        :rtype: ``osid.mapping.MapNode``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.MapHierarchyDesignSession

    def can_modify_map_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_map(self, map_id):
        """Adds a root map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``map_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_map(self, map_id):
        """Removes a root map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not a root
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_map(self, map_id, child_id):
        """Adds a child to a map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``map_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``map_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_map(self, map_id, child_id):
        """Removes a child from a map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not parent of ``child_id``
        :raise: ``NullArgument`` -- ``map_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_maps(self, map_id):
        """Removes all children from a map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class MappingProxyManager(osid.OsidProxyManager, MappingProfile):

    def get_location_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationLookupSession``
        :rtype: ``osid.mapping.LocationLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_lookup_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location lookup service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationLookupSession``
        :rtype: ``osid.mapping.LocationLookupSession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationQuerySession``
        :rtype: ``osid.mapping.LocationQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_query_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location query service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationQuerySession``
        :rtype: ``osid.mapping.LocationQuerySession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSearchSession``
        :rtype: ``osid.mapping.LocationSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_search_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location search service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSearchSession``
        :rtype: ``osid.mapping.LocationSearchSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationAdminSession``
        :rtype: ``osid.mapping.LocationAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_admin_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location administration service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationAdminSession``
        :rtype: ``osid.mapping.LocationAdminSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_notification_session(self, location_receiver, proxy):
        """Gets the ``OsidSession`` associated with the location notification service.

        :param location_receiver: the notification callback
        :type location_receiver: ``osid.mapping.LocationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationNotificationSession``
        :rtype: ``osid.mapping.LocationNotificationSession``
        :raise: ``NullArgument`` -- ``location_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_notification_session_for_map(self, location_receiver, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location notification service for the given map.

        :param location_receiver: the notification callback
        :type location_receiver: ``osid.mapping.LocationReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationNotificationSession``
        :rtype: ``osid.mapping.LocationNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``location_receiver, map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_hierarchy_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location hierarchy service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationHierarchyDesignSession``
        :rtype: ``osid.mapping.LocationHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_hierarchy_design_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location hierarchy design service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationHierarchySession``
        :rtype: ``osid.mapping.LocationHierarchyDesignSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_map_session(self, proxy):
        """Gets the ``OsidSession`` to lookup location/map mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationMapSession``
        :rtype: ``osid.mapping.LocationMapSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_map()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_map_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning locations to maps.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationMapAssignmentSession``
        :rtype: ``osid.mapping.LocationMapAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_map_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_smart_map_session(self, map_id, proxy):
        """Gets the ``OsidSession`` to manage location smart maps.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSmartMapSession``
        :rtype: ``osid.mapping.LocationSmartMapSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_smart_map()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_adjacency_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location adjacency service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationAdjacencySession``
        :rtype: ``osid.mapping.LocationAdjacencySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_adjacency()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_adjacency_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location adjacency service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationAdjacencySession``
        :rtype: ``osid.mapping.LocationAdjacencySession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_adjacency()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_spatial_session(self, proxy):
        """Gets the ``OsidSession`` associated with the location spatial service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSpatialSession``
        :rtype: ``osid.mapping.LocationSpatialSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_spatial()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_location_spatial_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the location spatial service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``LocationSpatialSession``
        :rtype: ``osid.mapping.LocationSpatialSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_location_spatial()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource location service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationSession``
        :rtype: ``osid.mapping.ResourceLocationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the resource location service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationSession``
        :rtype: ``osid.mapping.ResourceLocationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_update_session(self, proxy):
        """Gets the ``OsidSession`` associated with the resource location update service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationUpdateSession``
        :rtype: ``osid.mapping.ResourceLocationUpdateSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_update()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_update_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the resource location update service for the given map.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationUpdateSession``
        :rtype: ``osid.mapping.ResourceLocationUpdateSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_update()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_notification_session(self, resource_location_receiver, proxy):
        """Gets the ``OsidSession`` associated with the resource location notification service.

        :param resource_location_receiver: the notification callback
        :type resource_location_receiver: ``osid.mapping.ResourceLocationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NullArgument`` -- ``resource_location_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_location_notification_session_for_map(self, resource_location_receiver, map_id, proxy):
        """Gets the ``OsidSession`` associated with the resource location notification service for the given map.

        :param resource_location_receiver: the notification callback
        :type resource_location_receiver: ``osid.mapping.ResourceLocationReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourceLocationNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_location_receiver, map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_location_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_position_notification_session(self, resource_position_receiver, proxy):
        """Gets the ``OsidSession`` associated with the resource position notification service.

        :param resource_position_receiver: the notification callback
        :type resource_position_receiver: ``osid.mapping.ResourcePositionReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourcePositionNotificationSession``
        :rtype: ``osid.mapping.ResourceLocationNotificationSession``
        :raise: ``NullArgument`` -- ``resource_position_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_position_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_resource_position_notification_session_for_map(self, resource_position_receiver, map_id, proxy):
        """Gets the ``OsidSession`` associated with the resource position notification service for the given map.

        :param resource_position_receiver: the notification callback
        :type resource_position_receiver: ``osid.mapping.ResourcePositionReceiver``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ResourcePositionNotificationSession``
        :rtype: ``osid.mapping.ResourcePositionNotificationSession``
        :raise: ``NotFound`` -- no map found by the given ``Id``
        :raise: ``NullArgument`` -- ``resource_position_receiver, map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_position_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_my_location_session(self, proxy):
        """Gets the ``OsidSession`` associated with the my location service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyLocationLookupSession``
        :rtype: ``osid.mapping.MyLocationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_location_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_my_location_session_for_map(self, map_id, proxy):
        """Gets the ``OsidSession`` associated with the my location service for the given map.

        :param map_id: the ``Id`` of the map
        :type map_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MyLocationLookupSession``
        :rtype: ``osid.mapping.MyLocationSession``
        :raise: ``NotFound`` -- no ``Map`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``map_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_my_location_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapLookupSession``
        :rtype: ``osid.mapping.MapLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapQuerySession``
        :rtype: ``osid.mapping.MapQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapSearchSession``
        :rtype: ``osid.mapping.MapSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapAdminSession``
        :rtype: ``osid.mapping.MapAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_notification_session(self, map_receiver, proxy):
        """Gets the ``OsidSession`` associated with the map notification service.

        :param map_receiver: the notification callback
        :type map_receiver: ``osid.mapping.MapReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapNotificationSession``
        :rtype: ``osid.mapping.MapNotificationSession``
        :raise: ``NullArgument`` -- ``map_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``MapHierarchySession`` for maps
        :rtype: ``osid.mapping.MapHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_map_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the map hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession`` for maps
        :rtype: ``osid.mapping.MapHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_map_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_mapping_batch_proxy_manager(self):
        """Gets the mapping batch manager.

        :return: a ``MappingBatchProxyManager`` for paths
        :rtype: ``osid.mapping.batch.MappingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    mapping_batch_proxy_manager = property(fget=get_mapping_batch_proxy_manager)

    def get_mapping_path_proxy_manager(self):
        """Gets the mapping path manager.

        :return: a ``MappingPathProxyManager`` for paths
        :rtype: ``osid.mapping.path.MappingPathProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_path()`` is ``false``

        """
        raise UNIMPLEMENTED()

    mapping_path_proxy_manager = property(fget=get_mapping_path_proxy_manager)

    def get_mapping_route_proxy_manager(self):
        """Gets the mapping route manager.

        :return: a ``MappingRouteProxyManager`` for routes
        :rtype: ``osid.mapping.route.MappingRouteProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_route()`` is ``false``

        """
        raise UNIMPLEMENTED()

    mapping_route_proxy_manager = property(fget=get_mapping_route_proxy_manager)



class Map(osid.OsidCatalog, osid.OsidSession):

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationLookupSession

    def get_map_id(self):
        """Gets the ``Map``  ``Id`` associated with this session.

        :return: the ``Map Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    map_id = property(fget=get_map_id)

    def get_map(self):
        """Gets the ``Map`` associated with this session.

        :return: the map
        :rtype: ``osid.mapping.Map``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    map = property(fget=get_map)

    def can_lookup_locations(self):
        """Tests if this user can perform ``Location`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_location_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_location_view(self):
        """A complete view of the ``Location`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_map_view(self):
        """Federates the view for methods in this session.
        A federated view will include locations in maps which are
        children of this map in the map hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_map_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this map only.



        """
        raise UNIMPLEMENTED()

    def get_location(self, location_id):
        """Gets the ``Location`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Location`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Location`` and retained for
        compatibility.

        :param location_id: the ``Id`` of the ``Location`` to retrieve
        :type location_id: ``osid.id.Id``
        :return: the returned ``Location``
        :rtype: ``osid.mapping.Location``
        :raise: ``NotFound`` -- no ``Location`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_locations_by_ids(self, location_ids):
        """Gets a ``LocationList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the locations
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Locations`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param location_ids: the list of ``Ids`` to retrieve
        :type location_ids: ``osid.id.IdList``
        :return: the returned ``Location`` list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``location_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_locations_by_genus_type(self, location_genus_type):
        """Gets a ``LocationList`` corresponding to the given location genus ``Type`` which does not include locations of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known locations
        or an error results. Otherwise, the returned list may contain
        only those locations that are accessible through this session.

        :param location_genus_type: a location genus type
        :type location_genus_type: ``osid.type.Type``
        :return: the returned ``Location`` list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_locations_by_parent_genus_type(self, location_genus_type):
        """Gets a ``LocationList`` corresponding to the given location genus ``Type`` and include any additional locations with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known locations
        or an error results. Otherwise, the returned list may contain
        only those locations that are accessible through this session.

        :param location_genus_type: a location genus type
        :type location_genus_type: ``osid.type.Type``
        :return: the returned ``Location`` list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_locations_by_record_type(self, location_record_type):
        """Gets a ``LocationList`` containing the given location record ``Type``.
        In plenary mode, the returned list contains all known locations
        or an error results. Otherwise, the returned list may contain
        only those locations that are accessible through this session.

        :param location_record_type: a location record type
        :type location_record_type: ``osid.type.Type``
        :return: the returned ``Location`` list
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_locations(self):
        """Gets all ``Locations``.
        In plenary mode, the returned list contains all known locations
        or an error results. Otherwise, the returned list may contain
        only those locations that are accessible through this session.

        :return: a list of ``Locations``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    locations = property(fget=get_locations)


##
# The following methods are from osid.mapping.LocationQuerySession

    def can_search_locations(self):
        """Tests if this user can perform ``Location`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_location_query(self):
        """Gets a location query.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``

        """
        raise UNIMPLEMENTED()

    location_query = property(fget=get_location_query)

    def get_locations_by_query(self, location_query):
        """Gets a list of ``Locations`` matching the given search.

        :param location_query: the location query
        :type location_query: ``osid.mapping.LocationQuery``
        :return: the returned ``LocationList``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``location_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationSearchSession

    def get_location_search(self):
        """Gets a location search.

        :return: the location search
        :rtype: ``osid.mapping.LocationSearch``

        """
        raise UNIMPLEMENTED()

    location_search = property(fget=get_location_search)

    def get_location_search_order(self):
        """Gets a location search order.
        The ``LocationSearchOrder`` is supplied to a ``LocationSearch``
        to specify the ordering of results.

        :return: the location search order
        :rtype: ``osid.mapping.LocationSearchOrder``

        """
        raise UNIMPLEMENTED()

    location_search_order = property(fget=get_location_search_order)

    def get_locations_by_search(self, location_query, location_search):
        """Gets the search results matching the given search query using the given search.

        :param location_query: the location query
        :type location_query: ``osid.mapping.LocationQuery``
        :param location_search: the location search
        :type location_search: ``osid.mapping.LocationSearch``
        :return: the returned search results
        :rtype: ``osid.mapping.LocationSearchResults``
        :raise: ``NullArgument`` -- ``location_query`` or ``location_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``location_query`` or ``location_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_location_query_from_inspector(self, location_query_inspector):
        """Gets a location query from an inspector.
        The inspector is available from a ``LocationSearchResults``.

        :param location_query_inspector: a location query inspector
        :type location_query_inspector: ``osid.mapping.LocationQueryInspector``
        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``NullArgument`` -- ``location_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``location_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationAdminSession

    def can_create_locations(self):
        """Tests if this user can create ``Locations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Location`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Location`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_location_with_record_types(self, location_record_types):
        """Tests if this user can create a single ``Location`` using the desired record types.
        While ``MappingManager.getLocationRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Location``.
        Providing an empty array tests if a ``Location`` can be created
        with no records.

        :param location_record_types: array of location record types
        :type location_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Location`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``location_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_location_form_for_create(self, location_record_types):
        """Gets the location form for creating new locations.
        A new form should be requested for each create transaction.

        :param location_record_types: array of location record types
        :type location_record_types: ``osid.type.Type[]``
        :return: the location form
        :rtype: ``osid.mapping.LocationForm``
        :raise: ``NullArgument`` -- ``location_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get a form with given record types

        """
        raise UNIMPLEMENTED()

    def create_location(self, location_form):
        """Creates a new ``Location``.

        :param location_form: the form for this ``Location``
        :type location_form: ``osid.mapping.LocationForm``
        :return: the new ``Location``
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``location_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``location_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``location_form`` did not originate from ``get_location_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_locations(self):
        """Tests if this user can update ``Locations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Location`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Location`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_location_form_for_update(self, location_id):
        """Gets the location form for updating an existing location.
        A new location form should be requested for each update
        transaction.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :return: the location form
        :rtype: ``osid.mapping.LocationForm``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_location(self, location_form):
        """Updates an existing location.

        :param location_form: the form containing the elements to be updated
        :type location_form: ``osid.mapping.LocationForm``
        :raise: ``IllegalState`` -- ``location_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``location_id`` or ``location_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``location_form`` did not originate from ``get_location_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_locations(self):
        """Tests if this user can delete ``Locations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Location`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Location`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_location(self, location_id):
        """Deletes a ``Location``.

        :param location_id: the ``Id`` of the ``Location`` to remove
        :type location_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_location_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Locations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Location`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_location(self, location_id, alias_id):
        """Adds an ``Id`` to a ``Location`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Location`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another location, it is
        reassigned to the given location ``Id``.

        :param location_id: the ``Id`` of a ``Location``
        :type location_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationNotificationSession

    def can_register_for_location_notifications(self):
        """Tests if this user can register for ``Location`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_locations(self):
        """Register for notifications of new locations.
        ``LocationReceiver.newLocation()`` is invoked when a new
        ``Location`` appears in this map.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_location_ancestors(self, location_id):
        """Registers for notification if an ancestor is added to the specified location in the location hierarchy.
        ``LocationReceiver.newLocationAncestor()`` is invoked when the
        specified location experiences an addition in ancestry.

        :param location_id: the ``Id`` of the location to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_location_descendants(self, location_id):
        """Registers for notification if a descendant is added to the specified location in the location hierarchy.
        ``LocationReceiver.newLocationDescendant()`` is invoked when the
        specified location experiences an addition in descendants.

        :param location_id: the ``Id`` of the location to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_locations(self):
        """Registers for notification of updated locations.
        ``LocationReceiver.changedLocation()`` is invoked when a
        location in this map is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_location(self, location_id):
        """Registers for notification of an updated location.
        ``LocationReceiver.changedLocation()`` is invoked when the
        specified location in this map is changed.

        :param location_id: the ``Id`` of the ``Location`` to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_locations(self):
        """Registers for notification of deleted locations.
        ``LocationReceiver.deletedLocation()`` is invoked when a
        location is deleted or removed from this map.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_location(self, location_id):
        """Registers for notification of a deleted location.
        ``LocationReceiver.deletedLocation()`` is invoked when the
        specified location is deleted or removed from this map.

        :param location_id: the ``Id`` of the ``Location`` to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_location_ancestors(self, location_id):
        """Registers for notification if an ancestor is removed from the specified location in the location hierarchy.
        ``LocationReceiver.deletedLocationAncestor()`` is invoked when
        the specified location experiences a removal of an ancestor.

        :param location_id: the ``Id`` of the location to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_location_descendants(self, location_id):
        """Registers for notification if a descendant is removed from fthe specified location in the location hierarchy.
        ``LocationReceiver.deletedLocationDescednant()`` is invoked when
        the specified location experiences a removal of one of its
        descdendents.

        :param location_id: the ``Id`` of the location to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationHierarchySession

    def get_location_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    location_hierarchy_id = property(fget=get_location_hierarchy_id)

    def get_location_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    location_hierarchy = property(fget=get_location_hierarchy)

    def can_access_location_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_location_ids(self):
        """Gets the root location ``Ids`` in this hierarchy.

        :return: the root location ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_location_ids = property(fget=get_root_location_ids)

    def get_root_locations(self):
        """Gets the root location in the location hierarchy.
        A location with no parents is an orphan. While all location
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root location or
        child of another location.

        :return: the root locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_locations = property(fget=get_root_locations)

    def has_parent_locations(self, location_id):
        """Tests if the ``Location`` has any parents.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: ``true`` if the location has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_location(self, id_, location_id):
        """Tests if an ``Id`` is a direct parent of location.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``location_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_location_ids(self, location_id):
        """Gets the parent ``Ids`` of the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the location
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_locations(self, location_id):
        """Gets the parents of the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the parents of the location
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_location(self, id_, location_id):
        """Tests if an ``Id`` is an ancestor of a location.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``location_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_locations(self, location_id):
        """Tests if a location has any children.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: ``true`` if the ``location_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_location(self, id_, location_id):
        """Tests if a location is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``location_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_location_ids(self, location_id):
        """Gets the child ``Ids`` of the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the children of the location
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_locations(self, location_id):
        """Gets the children of the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the children of the location
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_location(self, id_, location_id):
        """Tests if an ``Id`` is a descendant of a location.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``location_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_location_node_ids(self, location_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given location.

        :param location_id: the ``Id`` to query
        :type location_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the location.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the location.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given location, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a location node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_location_nodes(self, location_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given location.

        :param location_id: the ``Id`` to query
        :type location_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the location.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the location.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given location, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a location node
        :rtype: ``osid.mapping.LocationNode``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationHierarchyDesignSession

    def can_modify_location_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_location(self, location_id):
        """Adds a root location.

        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``location_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_location(self, location_id, child_id):
        """Adds a child to a location.

        :param location_id: the ``Id`` of a location
        :type location_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``map_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationMapSession

    def can_lookup_location_map_locations(self):
        """Tests if this user can perform lookups of location/map locations.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up locations is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_location_map_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_location_map_view(self):
        """A complete view of the ``Location`` and ``Map`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_location_ids_by_map(self, map_id):
        """Gets the list of ``Location Ids`` associated with a ``Map``.

        :param map_id: ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: list of related location ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_locations_by_map(self, map_id):
        """Gets the list of ``Locations`` associated with a ``Map``.

        :param map_id: ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: list of related locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_location_ids_by_maps(self, map_ids):
        """Gets the list of ``Location Ids`` corresponding to a list of ``Maps``.

        :param map_ids: list of map ``Ids``
        :type map_ids: ``osid.id.IdList``
        :return: list of location ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``map_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_locations_by_maps(self, map_ids):
        """Gets the list of ``Locations`` corresponding to a list of ``Maps``.

        :param map_ids: list of map ``Ids``
        :type map_ids: ``osid.id.IdList``
        :return: list of locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``map_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_map_ids_by_location(self, location_id):
        """Gets the ``Map``  ``Ids`` mapped to a ``Location``.

        :param location_id: ``Id`` of a ``Location``
        :type location_id: ``osid.id.Id``
        :return: list of maps
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_maps_by_location(self, location_id):
        """Gets the ``Maps`` mapped to a ``Location``.

        :param location_id: ``Id`` of a ``Location``
        :type location_id: ``osid.id.Id``
        :return: list of maps
        :rtype: ``osid.mapping.MapList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationMapAssignmentSession

    def can_assign_locations(self):
        """Tests if this user can alter location/map mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if location is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_locations_to_map(self, map_id):
        """Tests if this user can alter location/map mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_map_ids(self, map_id):
        """Gets a list of maps including and under the given map node in which any location can be assigned.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :return: list of assignable map ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_map_ids_for_location(self, map_id, location_id):
        """Gets a list of maps including and under the given map node in which a specific location can be assigned.

        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :return: list of assignable map ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``map_id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_location_to_map(self, location_id, map_id):
        """Adds an existing ``Location`` to a ``Map``.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``location_id`` is already assigned to ``map_id``
        :raise: ``NotFound`` -- ``location_id`` or ``map_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_location_from_map(self, location_id, map_id):
        """Removes a ``Location`` from a ``Map``.

        :param location_id: the ``Id`` of the ``Location``
        :type location_id: ``osid.id.Id``
        :param map_id: the ``Id`` of the ``Map``
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``location_id`` or ``map_id`` not found or ``location_id`` not assigned to ``map_id``
        :raise: ``NullArgument`` -- ``location_id`` or ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationSmartMapSession

    def can_manage_smart_maps(self):
        """Tests if this user can manage smart maps.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart map management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_location_query(self, location_query):
        """Applies a location query to this map.

        :param location_query: the location query
        :type location_query: ``osid.mapping.LocationQuery``
        :raise: ``NullArgument`` -- ``location_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``location_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspec_location_query(self):
        """Gets a location query inspector for this map.

        :return: the location query inspector
        :rtype: ``osid.mapping.LocationQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_location_sequencing(self, location_search_order):
        """Applies a location search order to this map.

        :param location_search_order: the location search order
        :type location_search_order: ``osid.mapping.LocationSearchOrder``
        :raise: ``NullArgument`` -- ``location_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``location_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationAdjacencySession

    def can_lookup_location_adjacencies(self):
        """Tests if this user can query adjacenies of locations A return of true does not guarantee successful authorization.
        A return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if location adjacency methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_adjacent_locations(self, location_id, hops):
        """Gets a list of adjacent locations for the given location.
        The adjacent locations reflect the locations at the same level
        of the location hierarchy.

        :param location_id: the given location ``Id``
        :type location_id: ``osid.id.Id``
        :param hops: the number of hops to include. 0 returns an empty list. 1 returns the immediate adjacent locations.
        :type hops: ``cardinal``
        :return: a list of locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NotFound`` -- ``location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_adjacent(self, location_id, another_location_id):
        """Tests if two locations of the same type are adjacent.
        A location is not adjacent if contained within another location.

        :param location_id: the given location ``Id``
        :type location_id: ``osid.id.Id``
        :param another_location_id: the given location ``Id``
        :type another_location_id: ``osid.id.Id``
        :return: ``true`` of the locations are adjacent, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``location_id`` or ``another_location_id`` is not found
        :raise: ``NullArgument`` -- ``location_id`` or ``another_location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.LocationSpatialSession

    def get_location_by_coordinate(self, coordinate):
        """Gets the closest bounding location of the given coordinate.

        :param coordinate: a coordinate
        :type coordinate: ``osid.mapping.Coordinate``
        :return: the returned ``Location``
        :rtype: ``osid.mapping.Location``
        :raise: ``NullArgument`` -- ``coordinate`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- coordinate not supported

        """
        raise UNIMPLEMENTED()

    def get_locations_by_coordinates(self, coordinates):
        """Gets the closest bounding locations in the given coordinate list.
        In plenary mode, all locations are returned for each supplied
        coodrinate or an error results. In comparative mode, the
        returned list may omit inaccessible locations or reorder them.

        :param coordinates: a coordinate list
        :type coordinates: ``osid.mapping.CoordinateList``
        :return: the returned ``Locations``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``coordinates`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a coordinate is not supported

        """
        raise UNIMPLEMENTED()

    def get_locations_in_spatial_unit(self, spatial_unit):
        """Gets the locations that are included inside the given spatial unit.
        In plenary mode, all locations are returned or an error results.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :return: the returned ``Locations``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        """
        raise UNIMPLEMENTED()

    def get_locations_overlapping_spatial_unit(self, spatial_unit):
        """Gets the locations that are included inside or touch the given spatial unit.
        In plenary mode, all locations are returned or an error results.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :return: the returned ``Locations``
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.ResourceLocationSession

    def can_access_resource_locations(self):
        """Tests if this user can access the locations of resources.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer location
        operations to unauthorized users.

        :return: ``false`` if location methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_resource_location_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_resource_location_view(self):
        """A complete view of the ``Location`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_resource_location(self, resource_id):
        """Gets the current closest bounding location of the given resource.
        The returned ResourceLocation may not indicate a known location
        if no location is known.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the current location
        :rtype: ``osid.mapping.ResourceLocation``
        :raise: ``NotFound`` -- ``resource_id`` is not on map
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resource_locations(self, resource_ids):
        """Gets the current closest bounding locations of the given resources.
        In plenary mode, the returned list contains all of the locations
        of the supplied resources or an error results. In comparative
        mode, inaccessible resources may be omitted or duplicates
        suppressed or reordered.

        :param resource_ids: a resource list
        :type resource_ids: ``osid.id.IdList``
        :return: the current locations
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NotFound`` -- a resource ``Id`` is not on map
        :raise: ``NullArgument`` -- ``resource_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_at_location(self, location_id):
        """Gets the current resources at or within the given location.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the resources at the location
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_at_location_by_genus_type(self, location_id, resource_genus_type):
        """Gets the current resources at or within the given location for a resource genus type.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :param resource_genus_type: a resource genus type
        :type resource_genus_type: ``osid.type.Type``
        :return: the resources at the location
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NotFound`` -- ``location_id`` not found
        :raise: ``NullArgument`` -- ``location_id`` or ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_at_spatial_unit(self, spatial_unit):
        """Gets the current resource within the given spatial unit.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :return: the resources at the location
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_resources_at_spatial_unit_by_genus_type(self, spatial_unit, resource_genus_type):
        """Gets the current resource within the given spatial unit for a given resource genus type.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :param resource_genus_type: a resource genus type
        :type resource_genus_type: ``osid.type.Type``
        :return: the resources at the location
        :rtype: ``osid.mapping.ResourceLocationList``
        :raise: ``NullArgument`` -- ``spatial_unit`` or ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.ResourceLocationUpdateSession

    def can_update_resource_locations(self):
        """Tests if this user can set the locations of resources.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer location
        operations to unauthorized users.

        :return: ``false`` if location methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def update_resource_location(self, resource_id, location_id):
        """Updates the location of the resource.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``resource_id`` or ``location_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_resource_coordinate(self, resource_id, coordinate):
        """Updates the coordinate of the resource.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param coordinate: a coordinate
        :type coordinate: ``osid.mapping.Coordinate``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` or ``coordinate`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- coordinate not supported

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.ResourceLocationNotificationSession

    def can_register_for_resource_location_notifications(self):
        """Tests if this user can register for notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer
        notification operations to unauthorized users.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_entered_locations(self):
        """Register for notifications of entered locations for a resource.
        ``ResourceLocationReceiver.enteredLocation()`` is invoked when a
        resource appears in a new location.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_entered_location(self, location_id):
        """Register for notifications of an entered location.
        ``ResourceLocationReceiver.enteredLocation()`` is invoked when a
        resource appears in the specified location.

        :param location_id: the ``Id`` of the ``Location`` to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_entered_locations_for_resource(self, resource_id):
        """Register for notifications of entered locations.
        ``ResourceLocationReceiver.enteredLocation()`` is invoked when
        the specified resource appears in a new location.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_entered_locations_for_resources_by_genus_type(self, resource_genus_type):
        """Register for notifications of entered locations for the given resource genus type.
        ``ResourceLocationReceiver.enteredLocation()`` is invoked when a
        resource appears in a new location.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_exited_locations(self):
        """Register for notifications of exited locations for a resource.
        ``ResourceLocationReceiver.exitedLocation()`` is invoked when a
        resource exits a location.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_exited_location(self, location_id):
        """Register for notifications of an exited location.
        ``ResourceLocationReceiver.exitedLocation()`` is invoked when a
        resource exits the specified location.

        :param location_id: the ``Id`` of the ``Location`` to monitor
        :type location_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_exited_locations_for_resource(self, resource_id):
        """Register for notifications of exited locations.
        ``ResourceLocationReceiver.exitedLocation()`` is invoked when
        the specified resource exits a location.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_exited_locations_for_resources_by_genus_type(self, resource_genus_type):
        """Register for notifications of exited locations for the given resource genus type.
        . ``ResourceLocationReceiver.exitedLocation()`` is invoked when
        a resource exits a location.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.ResourcePositionNotificationSession

    def can_register_for_resource_path_notifications(self):
        """Tests if this user can register for notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer
        notification operations to unauthorized users.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_moved_resources(self):
        """Registers for notification of moved resources.
        ``ResourcePositionReceiver.movedResource()`` is invoked when a
        resource changes coordinates.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_moved_resource(self, resource_id):
        """Registers for notification of moved resources.
        ``ResourcePositionReceiver.movedResource()`` is invoked when the
        specified resource changes coordinates.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_moved_resources_by_genus_type(self, resource_genus_type):
        """Registers for notification of moved resources for the given resource genus type.
        ``ResourcePositionReceiver.movedResource()`` is invoked when a
        resource changes coordinates.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_entered_spatial_unit(self, spatial_unit):
        """Register for notifications of an entered spatial unit.
        ``ResourcePositionReceiver.enteredSpatialUnit()`` is invoked
        when a resource appears in the specified spatial unit.

        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        """
        raise UNIMPLEMENTED()

    def register_for_entered_spatial_unit_for_resource(self, resource_id, spatial_unit):
        """Register for notifications of an entered spatial unit.
        ``ResourcePositionReceiver.enteredSpatialUnit()`` is invoked
        when the specified resource appears in the specified spatial
        unit.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``resource_id`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        """
        raise UNIMPLEMENTED()

    def register_for_entered_spatial_unit_for_resource_by_genus_type(self, resource_genus_type, spatial_unit):
        """Register for notifications of an entered spatial unit for resources of the given resource genus type.
        ``ResourcePositionReceiver.enteredSpatialUnit()`` is invoked
        when the specified resource appears in the specified spatial
        unit.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.id.Id``
        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``resource_genus_type`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        """
        raise UNIMPLEMENTED()

    def register_for_exited_spatial_unit(self, spatial_unit):
        """Register for notifications of an exited spatial unit.
        ``ResourcePositionReceiver.exitedSpatialUnit()`` is invoked when
        a resource exits the specified spatial unit.

        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        """
        raise UNIMPLEMENTED()

    def register_for_exited_spatial_unit_for_resource(self, resource_id, spatial_unit):
        """Register for notifications of an exited spatial unit.
        ``ResourcePositionReceiver.exitedSpatialUnit()`` is invoked when
        the specified resource exits the specified spatial unit.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``resource_id`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        """
        raise UNIMPLEMENTED()

    def register_for_exited_spatial_unit_for_resources_by_genus_type(self, resource_genus_type, spatial_unit):
        """Register for notifications of an exited spatial unit for the given resource genus type.
        ``ResourcePositionReceiver.exitedSpatialUnit()`` is invoked when
        a resource exits the specified spatial unit.

        :param resource_genus_type: the genus type of the ``Resource`` to monitor
        :type resource_genus_type: ``osid.type.Type``
        :param spatial_unit: the ``SpatialUnit`` to monitor
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :raise: ``NullArgument`` -- ``resource_genus_t_ype`` or ``spatial_unit`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- spatial unit not supported

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.mapping.MyLocationSession

    def can_access_my_location(self):
        """Tests if this user can query own location.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer location
        operations to unauthorized users.

        :return: ``false`` if location methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def at_designated_location(self):
        """Tests if this agent is at a designated location.

        :return: ``true`` if the agent is at a designated location, ``false`` otherrwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_my_location(self):
        """Gets the current location of this agent.

        :return: the current location
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``at_designated_location()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    my_location = property(fget=get_my_location)

    def get_my_coordinate(self):
        """Gets the current coordinate of this agent.

        :return: the current coordinate
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    my_coordinate = property(fget=get_my_coordinate)

    def get_nearest_locations_to_me(self):
        """Gets the current nearest locations to this agent ordered by distance.

        :return: the nearest locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    nearest_locations_to_me = property(fget=get_nearest_locations_to_me)

    def get_nearest_location_to_me_by_genus_type(self, location_genus_type):
        """Gets the current nearest location of this agent of the specified location genus type ordered by distance.

        :param location_genus_type: a location genus type
        :type location_genus_type: ``osid.type.Type``
        :return: the nearest locations
        :rtype: ``osid.mapping.LocationList``
        :raise: ``NullArgument`` -- ``location_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class MapList(osid.OsidList):

    def get_next_map(self):
        """Gets the next ``Map`` in this list.

        :return: the next ``Map`` in this list. The ``has_next()`` method should be used to test that a next ``Map`` is available before calling this method.
        :rtype: ``osid.mapping.Map``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()



class Maps(MappingManager):
    pass


