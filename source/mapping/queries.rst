.. currentmodule:: dlkit.mapping.queries
.. automodule:: dlkit.mapping.queries

Queries
=======


Location Query
--------------

.. autoclass:: LocationQuery
   :show-inheritance:

   .. automethod:: LocationQuery.match_coordinate

   .. automethod:: LocationQuery.match_any_coordinate

   .. autoattribute:: LocationQuery.coordinate_terms

   .. automethod:: LocationQuery.match_contained_spatial_unit

   .. autoattribute:: LocationQuery.contained_spatial_unit_terms

   .. automethod:: LocationQuery.match_overlapping_spatial_unit

   .. autoattribute:: LocationQuery.overlapping_spatial_unit_terms

   .. automethod:: LocationQuery.match_any_spatial_unit

   .. autoattribute:: LocationQuery.spatial_unit_terms

   .. automethod:: LocationQuery.match_route_id

   .. autoattribute:: LocationQuery.route_id_terms

   .. automethod:: LocationQuery.supports_route_query

   .. autoattribute:: LocationQuery.route_query

   .. automethod:: LocationQuery.match_any_route

   .. autoattribute:: LocationQuery.route_terms

   .. automethod:: LocationQuery.match_path_id

   .. autoattribute:: LocationQuery.path_id_terms

   .. automethod:: LocationQuery.supports_path_query

   .. autoattribute:: LocationQuery.path_query

   .. automethod:: LocationQuery.match_any_path

   .. autoattribute:: LocationQuery.path_terms

   .. automethod:: LocationQuery.match_containing_location_id

   .. autoattribute:: LocationQuery.containing_location_id_terms

   .. automethod:: LocationQuery.supports_containing_location_query

   .. autoattribute:: LocationQuery.containing_location_query

   .. automethod:: LocationQuery.match_any_containing_location

   .. autoattribute:: LocationQuery.containing_location_terms

   .. automethod:: LocationQuery.match_contained_location_id

   .. autoattribute:: LocationQuery.contained_location_id_terms

   .. automethod:: LocationQuery.supports_contained_location_query

   .. autoattribute:: LocationQuery.contained_location_query

   .. automethod:: LocationQuery.match_any_contained_location

   .. autoattribute:: LocationQuery.contained_location_terms

   .. automethod:: LocationQuery.match_map_id

   .. autoattribute:: LocationQuery.map_id_terms

   .. automethod:: LocationQuery.supports_map_query

   .. autoattribute:: LocationQuery.map_query

   .. autoattribute:: LocationQuery.map_terms

   .. automethod:: LocationQuery.get_location_query_record



Map Query
---------

.. autoclass:: MapQuery
   :show-inheritance:

   .. automethod:: MapQuery.match_location_id

   .. autoattribute:: MapQuery.location_id_terms

   .. automethod:: MapQuery.supports_location_query

   .. autoattribute:: MapQuery.location_query

   .. automethod:: MapQuery.match_any_location

   .. autoattribute:: MapQuery.location_terms

   .. automethod:: MapQuery.match_path_id

   .. autoattribute:: MapQuery.path_id_terms

   .. automethod:: MapQuery.supports_path_query

   .. autoattribute:: MapQuery.path_query

   .. automethod:: MapQuery.match_any_path

   .. autoattribute:: MapQuery.path_terms

   .. automethod:: MapQuery.match_route_id

   .. autoattribute:: MapQuery.route_id_terms

   .. automethod:: MapQuery.supports_route_query

   .. autoattribute:: MapQuery.route_query

   .. automethod:: MapQuery.match_any_route

   .. autoattribute:: MapQuery.route_terms

   .. automethod:: MapQuery.match_ancestor_map_id

   .. autoattribute:: MapQuery.ancestor_map_id_terms

   .. automethod:: MapQuery.supports_ancestor_map_query

   .. autoattribute:: MapQuery.ancestor_map_query

   .. automethod:: MapQuery.match_any_ancestor_map

   .. autoattribute:: MapQuery.ancestor_map_terms

   .. automethod:: MapQuery.match_descendant_map_id

   .. autoattribute:: MapQuery.descendant_map_id_terms

   .. automethod:: MapQuery.supports_descendant_map_query

   .. autoattribute:: MapQuery.descendant_map_query

   .. automethod:: MapQuery.match_any_descendant_map

   .. autoattribute:: MapQuery.descendant_map_terms

   .. automethod:: MapQuery.get_map_query_record



