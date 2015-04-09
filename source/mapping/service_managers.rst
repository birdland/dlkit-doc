Summary
=======
.. currentmodule:: dlkit.services.mapping
.. automodule:: dlkit.services.mapping

Service_Managers
================


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

   .. autoattribute:: MappingProxyManager.mapping_batch_proxy_manager

   .. autoattribute:: MappingProxyManager.mapping_path_proxy_manager

   .. autoattribute:: MappingProxyManager.mapping_route_proxy_manager



Mapping Profile Methods
_______________

   .. automethod:: MappingProxyManager.supports_visible_federation

   .. automethod:: MappingProxyManager.supports_location_lookup

   .. automethod:: MappingProxyManager.supports_location_query

   .. automethod:: MappingProxyManager.supports_location_search

   .. automethod:: MappingProxyManager.supports_location_admin

   .. automethod:: MappingProxyManager.supports_location_notification

   .. automethod:: MappingProxyManager.supports_location_hierarchy

   .. automethod:: MappingProxyManager.supports_location_hierarchy_design

   .. automethod:: MappingProxyManager.supports_location_map

   .. automethod:: MappingProxyManager.supports_location_map_assignment

   .. automethod:: MappingProxyManager.supports_location_smart_map

   .. automethod:: MappingProxyManager.supports_location_adjacency

   .. automethod:: MappingProxyManager.supports_location_spatial

   .. automethod:: MappingProxyManager.supports_resource_location

   .. automethod:: MappingProxyManager.supports_resource_location_update

   .. automethod:: MappingProxyManager.supports_resource_location_notification

   .. automethod:: MappingProxyManager.supports_resource_position_notification

   .. automethod:: MappingProxyManager.supports_my_location

   .. automethod:: MappingProxyManager.supports_map_lookup

   .. automethod:: MappingProxyManager.supports_map_query

   .. automethod:: MappingProxyManager.supports_map_search

   .. automethod:: MappingProxyManager.supports_map_admin

   .. automethod:: MappingProxyManager.supports_map_notification

   .. automethod:: MappingProxyManager.supports_map_hierarchy

   .. automethod:: MappingProxyManager.supports_map_hierarchy_design

   .. automethod:: MappingProxyManager.supports_mapping_batch

   .. automethod:: MappingProxyManager.supports_mapping_path

   .. automethod:: MappingProxyManager.supports_mapping_route

   .. autoattribute:: MappingProxyManager.location_record_types

   .. automethod:: MappingProxyManager.supports_location_record_type

   .. autoattribute:: MappingProxyManager.location_search_record_types

   .. automethod:: MappingProxyManager.supports_location_search_record_type

   .. autoattribute:: MappingProxyManager.map_record_types

   .. automethod:: MappingProxyManager.supports_map_record_type

   .. autoattribute:: MappingProxyManager.map_search_record_types

   .. automethod:: MappingProxyManager.supports_map_search_record_type

   .. autoattribute:: MappingProxyManager.resource_location_record_types

   .. automethod:: MappingProxyManager.supports_resource_location_record_type

   .. autoattribute:: MappingProxyManager.coordinate_types

   .. automethod:: MappingProxyManager.supports_coordinate_type

   .. autoattribute:: MappingProxyManager.heading_types

   .. automethod:: MappingProxyManager.supports_heading_type

   .. autoattribute:: MappingProxyManager.spatial_unit_record_types

   .. automethod:: MappingProxyManager.supports_spatial_unit_record_type



Map Lookup
__________

   .. automethod:: MappingProxyManager.can_lookup_maps

   .. automethod:: MappingProxyManager.use_comparative_map_view

   .. automethod:: MappingProxyManager.use_plenary_map_view

   .. automethod:: MappingProxyManager.get_map

   .. automethod:: MappingProxyManager.get_maps_by_ids

   .. automethod:: MappingProxyManager.get_maps_by_genus_type

   .. automethod:: MappingProxyManager.get_maps_by_parent_genus_type

   .. automethod:: MappingProxyManager.get_maps_by_record_type

   .. automethod:: MappingProxyManager.get_maps_by_provider

   .. autoattribute:: MappingProxyManager.maps



Map Query
_________

   .. automethod:: MappingProxyManager.can_search_maps

   .. autoattribute:: MappingProxyManager.map_query

   .. automethod:: MappingProxyManager.get_maps_by_query



Map Search
__________

   .. autoattribute:: MappingProxyManager.map_search

   .. autoattribute:: MappingProxyManager.map_search_order

   .. automethod:: MappingProxyManager.get_maps_by_search

   .. automethod:: MappingProxyManager.get_map_query_from_inspector



Map Admin
_________

   .. automethod:: MappingProxyManager.can_create_maps

   .. automethod:: MappingProxyManager.can_create_map_with_record_types

   .. automethod:: MappingProxyManager.get_map_form_for_create

   .. automethod:: MappingProxyManager.create_map

   .. automethod:: MappingProxyManager.can_update_maps

   .. automethod:: MappingProxyManager.get_map_form_for_update

   .. automethod:: MappingProxyManager.update_map

   .. automethod:: MappingProxyManager.can_delete_maps

   .. automethod:: MappingProxyManager.delete_map

   .. automethod:: MappingProxyManager.can_manage_map_aliases

   .. automethod:: MappingProxyManager.alias_map



Map Notification
________________

   .. automethod:: MappingProxyManager.can_register_for_map_notifications

   .. automethod:: MappingProxyManager.register_for_new_maps

   .. automethod:: MappingProxyManager.register_for_new_map_ancestors

   .. automethod:: MappingProxyManager.register_for_new_map_descendants

   .. automethod:: MappingProxyManager.register_for_changed_maps

   .. automethod:: MappingProxyManager.register_for_changed_map

   .. automethod:: MappingProxyManager.register_for_deleted_maps

   .. automethod:: MappingProxyManager.register_for_deleted_map

   .. automethod:: MappingProxyManager.register_for_deleted_map_ancestors

   .. automethod:: MappingProxyManager.register_for_deleted_map_descendants



Map Hierarchy
_____________

   .. autoattribute:: MappingProxyManager.map_hierarchy_id

   .. autoattribute:: MappingProxyManager.map_hierarchy

   .. automethod:: MappingProxyManager.can_access_map_hierarchy

   .. automethod:: MappingProxyManager.use_comparative_map_view

   .. automethod:: MappingProxyManager.use_plenary_map_view

   .. autoattribute:: MappingProxyManager.root_map_ids

   .. autoattribute:: MappingProxyManager.root_maps

   .. automethod:: MappingProxyManager.has_parent_maps

   .. automethod:: MappingProxyManager.is_parent_of_map

   .. automethod:: MappingProxyManager.get_parent_map_ids

   .. automethod:: MappingProxyManager.get_parent_maps

   .. automethod:: MappingProxyManager.is_ancestor_of_map

   .. automethod:: MappingProxyManager.has_child_maps

   .. automethod:: MappingProxyManager.is_child_of_map

   .. automethod:: MappingProxyManager.get_child_map_ids

   .. automethod:: MappingProxyManager.get_child_maps

   .. automethod:: MappingProxyManager.is_descendant_of_map

   .. automethod:: MappingProxyManager.get_map_node_ids

   .. automethod:: MappingProxyManager.get_map_nodes



Map Hierarchy Design
____________________

   .. autoattribute:: MappingProxyManager.map_hierarchy_id

   .. autoattribute:: MappingProxyManager.map_hierarchy

   .. automethod:: MappingProxyManager.can_modify_map_hierarchy

   .. automethod:: MappingProxyManager.add_root_map

   .. automethod:: MappingProxyManager.remove_root_map

   .. automethod:: MappingProxyManager.add_child_map

   .. automethod:: MappingProxyManager.remove_child_map

   .. automethod:: MappingProxyManager.remove_child_maps



