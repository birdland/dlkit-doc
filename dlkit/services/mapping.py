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
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions


class MappingProfile(osid_managers.OsidProfile):

    def get_location_record_types(self):
        """Gets the supported ``Location`` record types.

        :return: a list containing the supported ``Location`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    location_record_types = property(fget=get_location_record_types)

    def get_location_search_record_types(self):
        """Gets the supported ``Location`` search types.

        :return: a list containing the supported ``Location`` search types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    location_search_record_types = property(fget=get_location_search_record_types)

    def get_map_record_types(self):
        """Gets the supported ``Map`` record types.

        :return: a list containing the supported ``Map`` types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    map_record_types = property(fget=get_map_record_types)

    def get_map_search_record_types(self):
        """Gets the supported ``Map`` search record types.

        :return: a list containing the supported ``Map`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    map_search_record_types = property(fget=get_map_search_record_types)

    def get_resource_location_record_types(self):
        """Gets the supported ``ResourceLocation`` record types.

        :return: a list containing the supported ``ResourceLocation`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    resource_location_record_types = property(fget=get_resource_location_record_types)

    def get_coordinate_types(self):
        """Gets the supported ``Coordinate`` types.

        :return: a list containing the supported ``Coordinate`` types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    coordinate_types = property(fget=get_coordinate_types)

    def get_heading_types(self):
        """Gets the supported ``Heading`` types.

        :return: a list containing the supported ``Heading`` types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    heading_types = property(fget=get_heading_types)

    def get_spatial_unit_record_types(self):
        """Gets the supported ``SpatialUnit`` record types.

        :return: a list containing the supported ``SpatialUnit`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)



class MappingManager(osid_managers.OsidManager, osid_sessions.OsidSession, MappingProfile):

    def get_mapping_batch_manager(self):
        """Gets the mapping batch manager.

        :return: a ``MappingBatchManager`` for paths
        :rtype: ``osid.mapping.batch.MappingBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_batch()`` is ``false``

        """
        return # osid.mapping.batch.MappingBatchManager

    mapping_batch_manager = property(fget=get_mapping_batch_manager)

    def get_mapping_path_manager(self):
        """Gets the mapping path manager.

        :return: a ``MappingPathManager`` for paths
        :rtype: ``osid.mapping.path.MappingPathManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_path()`` is ``false``

        """
        return # osid.mapping.path.MappingPathManager

    mapping_path_manager = property(fget=get_mapping_path_manager)

    def get_mapping_route_manager(self):
        """Gets the mapping route manager.

        :return: a ``MappingRouteManager`` for routes
        :rtype: ``osid.mapping.route.MappingRouteManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_route()`` is ``false``

        """
        return # osid.mapping.route.MappingRouteManager

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
        return # boolean

    def use_comparative_map_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_map_view(self):
        """A complete view of the ``Map`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

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
        return # osid.mapping.Map

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # boolean

    def get_map_query(self):
        """Gets a map query.

        :return: the map query
        :rtype: ``osid.mapping.MapQuery``

        """
        return # osid.mapping.MapQuery

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
        return # osid.mapping.MapList


##
# The following methods are from osid.mapping.MapSearchSession

    def get_map_search(self):
        """Gets a map search.

        :return: the map search
        :rtype: ``osid.mapping.MapSearch``

        """
        return # osid.mapping.MapSearch

    map_search = property(fget=get_map_search)

    def get_map_search_order(self):
        """Gets a map search order.
        The ``MapSearchOrder`` is supplied to a ``MapSearch`` to specify
        the ordering of results.

        :return: the map search order
        :rtype: ``osid.mapping.MapSearchOrder``

        """
        return # osid.mapping.MapSearchOrder

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
        return # osid.mapping.MapSearchResults

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
        return # osid.mapping.MapQuery


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
        return # boolean

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
        return # boolean

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
        return # osid.mapping.MapForm

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
        return # osid.mapping.Map

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
        return # boolean

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
        return # osid.mapping.MapForm

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
        pass

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
        return # boolean

    def delete_map(self, map_id):
        """Deletes a ``Map``.

        :param map_id: the ``Id`` of the ``Map`` to remove
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        return # boolean

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
        pass


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
        return # boolean

    def reliable_map_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_map_notification()`` .



        """
        pass

    def unreliable_map_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        pass

    def acknowledge_map_notification(self, notification_id):
        """Acknowledge a map notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_maps(self):
        """Register for notifications of new maps.
        ``MapReceiver.newMaps()`` is invoked when a new ``Map`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_maps(self):
        """Registers for notification of updated maps.
        ``MapReceiver.changedMaps()`` is invoked when a map is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_map(self, map_id):
        """Registers for notification of an updated map.
        ``MapReceiver.changedMaps()`` is invoked when the specified map
        is changed.

        :param map_id: the Id of the ``Map`` to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``E``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_maps(self):
        """Registers for notification of deleted maps.
        ``MapReceiver.deletedMaps()`` is invoked when a map is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_map(self, map_id):
        """Registers for notification of a deleted map.
        ``MapReceiver.deletedMaps()`` is invoked when the specified map
        is deleted.

        :param map_id: the ``Id`` of the ``Map`` to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_map_hierarchy(self):
        """Registers for notification of an updated map hierarchy structure.
        ``MapReceiver.changedChildOfMaps()`` is invoked when a node
        experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_map_hierarchy_for_ancestors(self, map_id):
        """Registers for notification of an updated map hierarchy structure.
        ``MapReceiver.changedChildOfMaps()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param map_id: the ``Id`` of the ``Map`` node to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_map_hierarchy_for_descendants(self, map_id):
        """Registers for notification of an updated map hierarchy structure.
        ``MapReceiver.changedChildOfMaps()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param map_id: the ``Id`` of the ``Map`` node to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


##
# The following methods are from osid.mapping.MapHierarchySession

    def get_map_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    map_hierarchy_id = property(fget=get_map_hierarchy_id)

    def get_map_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

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
        return # boolean

    def get_root_map_ids(self):
        """Gets the root map ``Ids`` in this hierarchy.

        :return: the root map ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

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
        return # osid.mapping.MapList

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.mapping.MapList

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
        return # boolean

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.mapping.MapList

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
        return # boolean

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
        return # osid.hierarchy.Node

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
        return # osid.mapping.MapNode


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
        return # boolean

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
        pass

    def remove_root_map(self, map_id):
        """Removes a root map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not a root
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

    def remove_child_maps(self, map_id):
        """Removes all children from a map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass



class MappingProxyManager(osid_managers.OsidProxyManager, MappingProfile):

    def get_mapping_batch_proxy_manager(self):
        """Gets the mapping batch manager.

        :return: a ``MappingBatchProxyManager`` for paths
        :rtype: ``osid.mapping.batch.MappingBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_batch()`` is ``false``

        """
        return # osid.mapping.batch.MappingBatchProxyManager

    mapping_batch_proxy_manager = property(fget=get_mapping_batch_proxy_manager)

    def get_mapping_path_proxy_manager(self):
        """Gets the mapping path manager.

        :return: a ``MappingPathProxyManager`` for paths
        :rtype: ``osid.mapping.path.MappingPathProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_path()`` is ``false``

        """
        return # osid.mapping.path.MappingPathProxyManager

    mapping_path_proxy_manager = property(fget=get_mapping_path_proxy_manager)

    def get_mapping_route_proxy_manager(self):
        """Gets the mapping route manager.

        :return: a ``MappingRouteProxyManager`` for routes
        :rtype: ``osid.mapping.route.MappingRouteProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_mapping_route()`` is ``false``

        """
        return # osid.mapping.route.MappingRouteProxyManager

    mapping_route_proxy_manager = property(fget=get_mapping_route_proxy_manager)


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
        return # boolean

    def use_comparative_map_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        pass

    def use_plenary_map_view(self):
        """A complete view of the ``Map`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        pass

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
        return # osid.mapping.Map

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # osid.mapping.MapList

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
        return # boolean

    def get_map_query(self):
        """Gets a map query.

        :return: the map query
        :rtype: ``osid.mapping.MapQuery``

        """
        return # osid.mapping.MapQuery

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
        return # osid.mapping.MapList


##
# The following methods are from osid.mapping.MapSearchSession

    def get_map_search(self):
        """Gets a map search.

        :return: the map search
        :rtype: ``osid.mapping.MapSearch``

        """
        return # osid.mapping.MapSearch

    map_search = property(fget=get_map_search)

    def get_map_search_order(self):
        """Gets a map search order.
        The ``MapSearchOrder`` is supplied to a ``MapSearch`` to specify
        the ordering of results.


        :return: the map search order
        :rtype: ``osid.mapping.MapSearchOrder``

        """
        return # osid.mapping.MapSearchOrder

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
        return # osid.mapping.MapSearchResults

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
        return # osid.mapping.MapQuery


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
        return # boolean

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
        return # boolean

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
        return # osid.mapping.MapForm

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
        return # osid.mapping.Map

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
        return # boolean

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
        return # osid.mapping.MapForm

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
        pass

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
        return # boolean

    def delete_map(self, map_id):
        """Deletes a ``Map``.

        :param map_id: the ``Id`` of the ``Map`` to remove
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        return # boolean

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
        pass


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
        return # boolean

    def reliable_map_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_map_notification()`` .




        """
        pass

    def unreliable_map_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.




        """
        pass

    def acknowledge_map_notification(self, notification_id):
        """Acknowledge a map notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_maps(self):
        """Register for notifications of new maps.
        ``MapReceiver.newMaps()`` is invoked when a new ``Map`` is
        created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_maps(self):
        """Registers for notification of updated maps.
        ``MapReceiver.changedMaps()`` is invoked when a map is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_map(self, map_id):
        """Registers for notification of an updated map.
        ``MapReceiver.changedMaps()`` is invoked when the specified map
        is changed.


        :param map_id: the Id of the ``Map`` to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``E``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_maps(self):
        """Registers for notification of deleted maps.
        ``MapReceiver.deletedMaps()`` is invoked when a map is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_map(self, map_id):
        """Registers for notification of a deleted map.
        ``MapReceiver.deletedMaps()`` is invoked when the specified map
        is deleted.


        :param map_id: the ``Id`` of the ``Map`` to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_map_hierarchy(self):
        """Registers for notification of an updated map hierarchy structure.
        ``MapReceiver.changedChildOfMaps()`` is invoked when a node
        experiences a change in its children.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_map_hierarchy_for_ancestors(self, map_id):
        """Registers for notification of an updated map hierarchy structure.
        ``MapReceiver.changedChildOfMaps()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.


        :param map_id: the ``Id`` of the ``Map`` node to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_map_hierarchy_for_descendants(self, map_id):
        """Registers for notification of an updated map hierarchy structure.
        ``MapReceiver.changedChildOfMaps()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.


        :param map_id: the ``Id`` of the ``Map`` node to monitor
        :type map_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


##
# The following methods are from osid.mapping.MapHierarchySession

    def get_map_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    map_hierarchy_id = property(fget=get_map_hierarchy_id)

    def get_map_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

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
        return # boolean

    def get_root_map_ids(self):
        """Gets the root map ``Ids`` in this hierarchy.

        :return: the root map ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

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
        return # osid.mapping.MapList

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.mapping.MapList

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
        return # boolean

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.mapping.MapList

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
        return # boolean

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
        return # osid.hierarchy.Node

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
        return # osid.mapping.MapNode


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
        return # boolean

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
        pass

    def remove_root_map(self, map_id):
        """Removes a root map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not a root
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

    def remove_child_maps(self, map_id):
        """Removes all children from a map.

        :param map_id: the ``Id`` of a map
        :type map_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``map_id`` is not found
        :raise: ``NullArgument`` -- ``map_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass



class Maps(MappingManager):
    pass


