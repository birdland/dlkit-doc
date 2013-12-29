.. currentmodule:: dlkit.abstract_osid.mapping.receivers
.. automodule:: dlkit.abstract_osid.mapping.receivers

Receivers
=========


Location Receiver
-----------------

.. autoclass:: LocationReceiver
   :show-inheritance:

.. automethod:: LocationReceiver.new_location

.. automethod:: LocationReceiver.new_ancestor_location

.. automethod:: LocationReceiver.new_descendant_location

.. automethod:: LocationReceiver.changed_location

.. automethod:: LocationReceiver.deleted_location

.. automethod:: LocationReceiver.deleted_ancestor_location

.. automethod:: LocationReceiver.deleted_descendant_location



Map Receiver
------------

.. autoclass:: MapReceiver
   :show-inheritance:

.. automethod:: MapReceiver.new_map

.. automethod:: MapReceiver.new_ancestor_map

.. automethod:: MapReceiver.new_descendant_map

.. automethod:: MapReceiver.changed_map

.. automethod:: MapReceiver.deleted_map

.. automethod:: MapReceiver.deleted_ancestor_map

.. automethod:: MapReceiver.deleted_descendant_map



Resource Location Receiver
--------------------------

.. autoclass:: ResourceLocationReceiver
   :show-inheritance:

.. automethod:: ResourceLocationReceiver.entered_location

.. automethod:: ResourceLocationReceiver.exited_location

.. automethod:: ResourceLocationReceiver.new_resource_coordinate



Resource Position Receiver
--------------------------

.. autoclass:: ResourcePositionReceiver
   :show-inheritance:

.. automethod:: ResourcePositionReceiver.moved_resource

.. automethod:: ResourcePositionReceiver.entered_spatial_unit

.. automethod:: ResourcePositionReceiver.exited_spatial_unit



