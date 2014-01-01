.. currentmodule:: dlkit.services.mapping
.. automodule:: dlkit.services.mapping

Services
========


Mapping Manager
---------------

.. autoclass:: MappingManager
   :show-inheritance:

   .. autoattribute:: MappingManager.mapping_batch_manager

   .. autoattribute:: MappingManager.mapping_path_manager

   .. autoattribute:: MappingManager.mapping_route_manager



Mapping Profile Methods
_______________

   .. automethod:: MappingManager.supports_visible_federation

   .. automethod:: MappingManager.supports_location_lookup

   .. automethod:: MappingManager.supports_location_query

   .. automethod:: MappingManager.supports_location_search

   .. automethod:: MappingManager.supports_location_admin

   .. automethod:: MappingManager.supports_location_notification

   .. automethod:: MappingManager.supports_location_hierarchy

   .. automethod:: MappingManager.supports_location_hierarchy_design

   .. automethod:: MappingManager.supports_location_map

   .. automethod:: MappingManager.supports_location_map_assignment

   .. automethod:: MappingManager.supports_location_smart_map

   .. automethod:: MappingManager.supports_location_adjacency

   .. automethod:: MappingManager.supports_location_spatial

   .. automethod:: MappingManager.supports_resource_location

   .. automethod:: MappingManager.supports_resource_location_update

   .. automethod:: MappingManager.supports_resource_location_notification

   .. automethod:: MappingManager.supports_resource_position_notification

   .. automethod:: MappingManager.supports_my_location

   .. automethod:: MappingManager.supports_map_lookup

   .. automethod:: MappingManager.supports_map_query

   .. automethod:: MappingManager.supports_map_search

   .. automethod:: MappingManager.supports_map_admin

   .. automethod:: MappingManager.supports_map_notification

   .. automethod:: MappingManager.supports_map_hierarchy

   .. automethod:: MappingManager.supports_map_hierarchy_design

   .. automethod:: MappingManager.supports_mapping_batch

   .. automethod:: MappingManager.supports_mapping_path

   .. automethod:: MappingManager.supports_mapping_route

   .. autoattribute:: MappingManager.location_record_types

   .. automethod:: MappingManager.supports_location_record_type

   .. autoattribute:: MappingManager.location_search_record_types

   .. automethod:: MappingManager.supports_location_search_record_type

   .. autoattribute:: MappingManager.map_record_types

   .. automethod:: MappingManager.supports_map_record_type

   .. autoattribute:: MappingManager.map_search_record_types

   .. automethod:: MappingManager.supports_map_search_record_type

   .. autoattribute:: MappingManager.resource_location_record_types

   .. automethod:: MappingManager.supports_resource_location_record_type

   .. autoattribute:: MappingManager.coordinate_types

   .. automethod:: MappingManager.supports_coordinate_type

   .. autoattribute:: MappingManager.heading_types

   .. automethod:: MappingManager.supports_heading_type

   .. autoattribute:: MappingManager.spatial_unit_record_types

   .. automethod:: MappingManager.supports_spatial_unit_record_type



Map Lookup
__________

   .. automethod:: MappingManager.can_lookup_maps

   .. automethod:: MappingManager.use_comparative_map_view

   .. automethod:: MappingManager.use_plenary_map_view

   .. automethod:: MappingManager.get_map

   .. automethod:: MappingManager.get_maps_by_ids

   .. automethod:: MappingManager.get_maps_by_genus_type

   .. automethod:: MappingManager.get_maps_by_parent_genus_type

   .. automethod:: MappingManager.get_maps_by_record_type

   .. automethod:: MappingManager.get_maps_by_provider

   .. autoattribute:: MappingManager.maps



Map Query
_________

   .. automethod:: MappingManager.can_search_maps

   .. autoattribute:: MappingManager.map_query

   .. automethod:: MappingManager.get_maps_by_query



Map Search
__________

   .. autoattribute:: MappingManager.map_search

   .. autoattribute:: MappingManager.map_search_order

   .. automethod:: MappingManager.get_maps_by_search

   .. automethod:: MappingManager.get_map_query_from_inspector



Map Admin
_________

   .. automethod:: MappingManager.can_create_maps

   .. automethod:: MappingManager.can_create_map_with_record_types

   .. automethod:: MappingManager.get_map_form_for_create

   .. automethod:: MappingManager.create_map

   .. automethod:: MappingManager.can_update_maps

   .. automethod:: MappingManager.get_map_form_for_update

   .. automethod:: MappingManager.update_map

   .. automethod:: MappingManager.can_delete_maps

   .. automethod:: MappingManager.delete_map

   .. automethod:: MappingManager.can_manage_map_aliases

   .. automethod:: MappingManager.alias_map



Map Notification
________________

   .. automethod:: MappingManager.can_register_for_map_notifications

   .. automethod:: MappingManager.register_for_new_maps

   .. automethod:: MappingManager.register_for_new_map_ancestors

   .. automethod:: MappingManager.register_for_new_map_descendants

   .. automethod:: MappingManager.register_for_changed_maps

   .. automethod:: MappingManager.register_for_changed_map

   .. automethod:: MappingManager.register_for_deleted_maps

   .. automethod:: MappingManager.register_for_deleted_map

   .. automethod:: MappingManager.register_for_deleted_map_ancestors

   .. automethod:: MappingManager.register_for_deleted_map_descendants



Map Hierarchy
_____________

   .. autoattribute:: MappingManager.map_hierarchy_id

   .. autoattribute:: MappingManager.map_hierarchy

   .. automethod:: MappingManager.can_access_map_hierarchy

   .. automethod:: MappingManager.use_comparative_map_view

   .. automethod:: MappingManager.use_plenary_map_view

   .. autoattribute:: MappingManager.root_map_ids

   .. autoattribute:: MappingManager.root_maps

   .. automethod:: MappingManager.has_parent_maps

   .. automethod:: MappingManager.is_parent_of_map

   .. automethod:: MappingManager.get_parent_map_ids

   .. automethod:: MappingManager.get_parent_maps

   .. automethod:: MappingManager.is_ancestor_of_map

   .. automethod:: MappingManager.has_child_maps

   .. automethod:: MappingManager.is_child_of_map

   .. automethod:: MappingManager.get_child_map_ids

   .. automethod:: MappingManager.get_child_maps

   .. automethod:: MappingManager.is_descendant_of_map

   .. automethod:: MappingManager.get_map_node_ids

   .. automethod:: MappingManager.get_map_nodes



Map Hierarchy Design
____________________

   .. autoattribute:: MappingManager.map_hierarchy_id

   .. autoattribute:: MappingManager.map_hierarchy

   .. automethod:: MappingManager.can_modify_map_hierarchy

   .. automethod:: MappingManager.add_root_map

   .. automethod:: MappingManager.remove_root_map

   .. automethod:: MappingManager.add_child_map

   .. automethod:: MappingManager.remove_child_map

   .. automethod:: MappingManager.remove_child_maps



Mapping Proxy Manager
---------------------

.. autoclass:: MappingProxyManager
   :show-inheritance:

   .. automethod:: MappingProxyManager.get_location_lookup_session

   .. automethod:: MappingProxyManager.get_location_lookup_session_for_map

   .. automethod:: MappingProxyManager.get_location_query_session

   .. automethod:: MappingProxyManager.get_location_query_session_for_map

   .. automethod:: MappingProxyManager.get_location_search_session

   .. automethod:: MappingProxyManager.get_location_search_session_for_map

   .. automethod:: MappingProxyManager.get_location_admin_session

   .. automethod:: MappingProxyManager.get_location_admin_session_for_map

   .. automethod:: MappingProxyManager.get_location_notification_session

   .. automethod:: MappingProxyManager.get_location_notification_session_for_map

   .. automethod:: MappingProxyManager.get_location_hierarchy_session

   .. automethod:: MappingProxyManager.get_location_hierarchy_session_for_map

   .. automethod:: MappingProxyManager.get_location_hierarchy_design_session

   .. automethod:: MappingProxyManager.get_location_hierarchy_design_session_for_map

   .. automethod:: MappingProxyManager.get_location_map_session

   .. automethod:: MappingProxyManager.get_location_map_assignment_session

   .. automethod:: MappingProxyManager.get_location_smart_map_session

   .. automethod:: MappingProxyManager.get_location_adjacency_session

   .. automethod:: MappingProxyManager.get_location_adjacency_session_for_map

   .. automethod:: MappingProxyManager.get_location_spatial_session

   .. automethod:: MappingProxyManager.get_location_spatial_session_for_map

   .. automethod:: MappingProxyManager.get_resource_location_session

   .. automethod:: MappingProxyManager.get_resource_location_session_for_map

   .. automethod:: MappingProxyManager.get_resource_location_update_session

   .. automethod:: MappingProxyManager.get_resource_location_update_session_for_map

   .. automethod:: MappingProxyManager.get_resource_location_notification_session

   .. automethod:: MappingProxyManager.get_resource_location_notification_session_for_map

   .. automethod:: MappingProxyManager.get_resource_position_notification_session

   .. automethod:: MappingProxyManager.get_resource_position_notification_session_for_map

   .. automethod:: MappingProxyManager.get_my_location_session

   .. automethod:: MappingProxyManager.get_my_location_session_for_map

   .. automethod:: MappingProxyManager.get_map_lookup_session

   .. automethod:: MappingProxyManager.get_map_query_session

   .. automethod:: MappingProxyManager.get_map_search_session

   .. automethod:: MappingProxyManager.get_map_admin_session

   .. automethod:: MappingProxyManager.get_map_notification_session

   .. automethod:: MappingProxyManager.get_map_hierarchy_session

   .. automethod:: MappingProxyManager.get_map_hierarchy_design_session

   .. autoattribute:: MappingProxyManager.mapping_batch_proxy_manager

   .. autoattribute:: MappingProxyManager.mapping_path_proxy_manager

   .. autoattribute:: MappingProxyManager.mapping_route_proxy_manager



