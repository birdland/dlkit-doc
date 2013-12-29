.. currentmodule:: dlkit.abstract_osid.mapping.objects
.. automodule:: dlkit.abstract_osid.mapping.objects

Objects
=======


Location
--------

.. autoclass:: Location
   :show-inheritance:

.. automethod:: Location.has_spatial_unit

.. autoattribute:: Location.spatial_unit

.. automethod:: Location.get_location_record



Location Form
-------------

.. autoclass:: LocationForm
   :show-inheritance:

.. autoattribute:: LocationForm.spatial_unit_metadata

.. autoattribute:: LocationForm.spatial_unit

.. automethod:: LocationForm.get_location_form_record



Location List
-------------

.. autoclass:: LocationList
   :show-inheritance:

.. autoattribute:: LocationList.next_location

.. automethod:: LocationList.get_next_locations



Location Node
-------------

.. autoclass:: LocationNode
   :show-inheritance:

.. autoattribute:: LocationNode.location

.. autoattribute:: LocationNode.parent_location_nodes

.. autoattribute:: LocationNode.child_location_nodes



Location Node List
------------------

.. autoclass:: LocationNodeList
   :show-inheritance:

.. autoattribute:: LocationNodeList.next_location_node

.. automethod:: LocationNodeList.get_next_location_nodes



Map Form
--------

.. autoclass:: MapForm
   :show-inheritance:

.. automethod:: MapForm.get_map_form_record



Map List
--------

.. autoclass:: MapList
   :show-inheritance:

.. autoattribute:: MapList.next_map

.. automethod:: MapList.get_next_maps



Map Node
--------

.. autoclass:: MapNode
   :show-inheritance:

.. autoattribute:: MapNode.map

.. autoattribute:: MapNode.parent_map_nodes

.. autoattribute:: MapNode.child_map_nodes



Map Node List
-------------

.. autoclass:: MapNodeList
   :show-inheritance:

.. autoattribute:: MapNodeList.next_map_node

.. automethod:: MapNodeList.get_next_map_nodes



Resource Location List
----------------------

.. autoclass:: ResourceLocationList
   :show-inheritance:

.. autoattribute:: ResourceLocationList.next_resource_location

.. automethod:: ResourceLocationList.get_next_resource_locations



Coordinate List
---------------

.. autoclass:: CoordinateList
   :show-inheritance:

.. autoattribute:: CoordinateList.next_coordinate

.. automethod:: CoordinateList.get_next_coordinates



Spatial Unit List
-----------------

.. autoclass:: SpatialUnitList
   :show-inheritance:

.. autoattribute:: SpatialUnitList.next_spatial_unit

.. automethod:: SpatialUnitList.get_next_spatial_units



