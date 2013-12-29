.. currentmodule:: dlkit.services.mapping
.. automodule:: dlkit.services.mapping

Map
===


Map
---

.. autoclass:: Map
   :show-inheritance:

.. automethod:: Map.get_map_record



Location Lookup Methods
-----------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_lookup_locations

.. automethod:: Map.use_comparative_location_view

.. automethod:: Map.use_plenary_location_view

.. automethod:: Map.use_federated_map_view

.. automethod:: Map.use_isolated_map_view

.. automethod:: Map.get_location

.. automethod:: Map.get_locations_by_ids

.. automethod:: Map.get_locations_by_genus_type

.. automethod:: Map.get_locations_by_parent_genus_type

.. automethod:: Map.get_locations_by_record_type

.. autoattribute:: Map.locations



Location Query Methods
----------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_search_locations

.. automethod:: Map.use_federated_map_view

.. automethod:: Map.use_isolated_map_view

.. autoattribute:: Map.location_query

.. automethod:: Map.get_locations_by_query



Location Search Methods
-----------------------

.. autoattribute:: Map.location_search

.. autoattribute:: Map.location_search_order

.. automethod:: Map.get_locations_by_search

.. automethod:: Map.get_location_query_from_inspector



Location Admin Methods
----------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_create_locations

.. automethod:: Map.can_create_location_with_record_types

.. automethod:: Map.get_location_form_for_create

.. automethod:: Map.create_location

.. automethod:: Map.can_update_locations

.. automethod:: Map.get_location_form_for_update

.. automethod:: Map.update_location

.. automethod:: Map.can_delete_locations

.. automethod:: Map.delete_location

.. automethod:: Map.can_manage_location_aliases

.. automethod:: Map.alias_location



Location Notification Methods
-----------------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_register_for_location_notifications

.. automethod:: Map.use_federated_map_view

.. automethod:: Map.use_isolated_map_view

.. automethod:: Map.register_for_new_locations

.. automethod:: Map.register_for_new_location_ancestors

.. automethod:: Map.register_for_new_location_descendants

.. automethod:: Map.register_for_changed_locations

.. automethod:: Map.register_for_changed_location

.. automethod:: Map.register_for_deleted_locations

.. automethod:: Map.register_for_deleted_location

.. automethod:: Map.register_for_deleted_location_ancestors

.. automethod:: Map.register_for_deleted_location_descendants



Location Hierarchy Methods
--------------------------

.. autoattribute:: Map.location_hierarchy_id

.. autoattribute:: Map.location_hierarchy

.. automethod:: Map.can_access_location_hierarchy

.. automethod:: Map.use_comparative_location_view

.. automethod:: Map.use_plenary_location_view

.. autoattribute:: Map.root_location_ids

.. autoattribute:: Map.root_locations

.. automethod:: Map.has_parent_locations

.. automethod:: Map.is_parent_of_location

.. automethod:: Map.get_parent_location_ids

.. automethod:: Map.get_parent_locations

.. automethod:: Map.is_ancestor_of_location

.. automethod:: Map.has_child_locations

.. automethod:: Map.is_child_of_location

.. automethod:: Map.get_child_location_ids

.. automethod:: Map.get_child_locations

.. automethod:: Map.is_descendant_of_location

.. automethod:: Map.get_location_node_ids

.. automethod:: Map.get_location_nodes



Location Hierarchy Design Methods
---------------------------------

.. autoattribute:: Map.location_hierarchy_id

.. autoattribute:: Map.location_hierarchy

.. automethod:: Map.can_modify_location_hierarchy

.. automethod:: Map.add_root_location

.. automethod:: Map.add_child_location



Location Map Methods
--------------------

.. automethod:: Map.can_lookup_location_map_locations

.. automethod:: Map.use_comparative_location_map_view

.. automethod:: Map.use_plenary_location_map_view

.. automethod:: Map.get_location_ids_by_map

.. automethod:: Map.get_locations_by_map

.. automethod:: Map.get_location_ids_by_maps

.. automethod:: Map.get_locations_by_maps

.. automethod:: Map.get_map_ids_by_location

.. automethod:: Map.get_maps_by_location



Location Map Assignment Methods
-------------------------------

.. automethod:: Map.can_assign_locations

.. automethod:: Map.can_assign_locations_to_map

.. automethod:: Map.get_assignable_map_ids

.. automethod:: Map.get_assignable_map_ids_for_location

.. automethod:: Map.assign_location_to_map

.. automethod:: Map.unassign_location_from_map



Location Smart Map Methods
--------------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_manage_smart_maps

.. autoattribute:: Map.location_query

.. autoattribute:: Map.location_search_order

.. automethod:: Map.apply_location_query

.. automethod:: Map.inspec_location_query

.. automethod:: Map.apply_location_sequencing

.. automethod:: Map.get_location_query_from_inspector



Location Adjacency Methods
--------------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_lookup_location_adjacencies

.. automethod:: Map.use_comparative_location_view

.. automethod:: Map.use_plenary_location_view

.. automethod:: Map.use_federated_map_view

.. automethod:: Map.use_isolated_map_view

.. automethod:: Map.get_adjacent_locations

.. automethod:: Map.is_adjacent



Location Spatial Methods
------------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_lookup_locations

.. automethod:: Map.use_comparative_location_view

.. automethod:: Map.use_plenary_location_view

.. automethod:: Map.use_federated_map_view

.. automethod:: Map.use_isolated_map_view

.. automethod:: Map.get_location_by_coordinate

.. automethod:: Map.get_locations_by_coordinates

.. automethod:: Map.get_locations_in_spatial_unit

.. automethod:: Map.get_locations_overlapping_spatial_unit



Resource Location Methods
-------------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_access_resource_locations

.. automethod:: Map.use_comparative_resource_location_view

.. automethod:: Map.use_plenary_resource_location_view

.. automethod:: Map.use_federated_map_view

.. automethod:: Map.use_isolated_map_view

.. automethod:: Map.get_resource_location

.. automethod:: Map.get_resource_locations

.. automethod:: Map.get_resources_at_location

.. automethod:: Map.get_resources_at_location_by_genus_type

.. automethod:: Map.get_resources_at_spatial_unit

.. automethod:: Map.get_resources_at_spatial_unit_by_genus_type



Resource Location Update Methods
--------------------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_update_resource_locations

.. automethod:: Map.update_resource_location

.. automethod:: Map.update_resource_coordinate



Resource Location Notification Methods
--------------------------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_register_for_resource_location_notifications

.. automethod:: Map.use_federated_map_view

.. automethod:: Map.use_isolated_map_view

.. automethod:: Map.register_for_entered_locations

.. automethod:: Map.register_for_entered_location

.. automethod:: Map.register_for_entered_locations_for_resource

.. automethod:: Map.register_for_entered_locations_for_resources_by_genus_type

.. automethod:: Map.register_for_exited_locations

.. automethod:: Map.register_for_exited_location

.. automethod:: Map.register_for_exited_locations_for_resource

.. automethod:: Map.register_for_exited_locations_for_resources_by_genus_type



Resource Position Notification Methods
--------------------------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_register_for_resource_path_notifications

.. automethod:: Map.use_federated_map_view

.. automethod:: Map.use_isolated_map_view

.. automethod:: Map.register_for_moved_resources

.. automethod:: Map.register_for_moved_resource

.. automethod:: Map.register_for_moved_resources_by_genus_type

.. automethod:: Map.register_for_entered_spatial_unit

.. automethod:: Map.register_for_entered_spatial_unit_for_resource

.. automethod:: Map.register_for_entered_spatial_unit_for_resource_by_genus_type

.. automethod:: Map.register_for_exited_spatial_unit

.. automethod:: Map.register_for_exited_spatial_unit_for_resource

.. automethod:: Map.register_for_exited_spatial_unit_for_resources_by_genus_type



My Location Methods
-------------------

.. autoattribute:: Map.map_id

.. autoattribute:: Map.map

.. automethod:: Map.can_access_my_location

.. automethod:: Map.at_designated_location

.. autoattribute:: Map.my_location

.. autoattribute:: Map.my_coordinate

.. autoattribute:: Map.nearest_locations_to_me

.. automethod:: Map.get_nearest_location_to_me_by_genus_type



