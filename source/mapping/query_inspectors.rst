.. currentmodule:: dlkit.mapping.query_inspectors
.. automodule:: dlkit.mapping.query_inspectors

Query Inspectors
================


Location Query Inspector
------------------------

.. autoclass:: LocationQueryInspector
   :show-inheritance:

   .. autoattribute:: LocationQueryInspector.coordinate_terms

   .. autoattribute:: LocationQueryInspector.contained_spatial_unit_terms

   .. autoattribute:: LocationQueryInspector.overlapping_spatial_unit_terms

   .. autoattribute:: LocationQueryInspector.spatial_unit_terms

   .. autoattribute:: LocationQueryInspector.route_id_terms

   .. autoattribute:: LocationQueryInspector.route_terms

   .. autoattribute:: LocationQueryInspector.path_id_terms

   .. autoattribute:: LocationQueryInspector.path_terms

   .. autoattribute:: LocationQueryInspector.containing_location_id_terms

   .. autoattribute:: LocationQueryInspector.containing_location_terms

   .. autoattribute:: LocationQueryInspector.contained_location_id_terms

   .. autoattribute:: LocationQueryInspector.contained_location_terms

   .. autoattribute:: LocationQueryInspector.map_id_terms

   .. autoattribute:: LocationQueryInspector.map_terms

   .. automethod:: LocationQueryInspector.get_location_query_inspector_record



Map Query Inspector
-------------------

.. autoclass:: MapQueryInspector
   :show-inheritance:

   .. autoattribute:: MapQueryInspector.location_id_terms

   .. autoattribute:: MapQueryInspector.location_terms

   .. autoattribute:: MapQueryInspector.path_id_terms

   .. autoattribute:: MapQueryInspector.path_terms

   .. autoattribute:: MapQueryInspector.route_id_terms

   .. autoattribute:: MapQueryInspector.route_terms

   .. autoattribute:: MapQueryInspector.ancestor_map_id_terms

   .. autoattribute:: MapQueryInspector.ancestor_map_terms

   .. autoattribute:: MapQueryInspector.descendant_map_id_terms

   .. autoattribute:: MapQueryInspector.descendant_map_terms

   .. automethod:: MapQueryInspector.get_map_query_inspector_record



