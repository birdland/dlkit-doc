.. currentmodule:: dlkit.resource.receivers
.. automodule:: dlkit.resource.receivers

Receivers
=========


Resource Receiver
-----------------

.. autoclass:: ResourceReceiver
   :show-inheritance:

   .. automethod:: ResourceReceiver.new_resource

   .. automethod:: ResourceReceiver.changed_resource

   .. automethod:: ResourceReceiver.changed_resource_membership

   .. automethod:: ResourceReceiver.deleted_resource



Group Receiver
--------------

.. autoclass:: GroupReceiver
   :show-inheritance:

   .. automethod:: GroupReceiver.new_member

   .. automethod:: GroupReceiver.deleted_member



Resource Relationship Receiver
------------------------------

.. autoclass:: ResourceRelationshipReceiver
   :show-inheritance:

   .. automethod:: ResourceRelationshipReceiver.new_resource_relationship

   .. automethod:: ResourceRelationshipReceiver.changed_resource_relationship

   .. automethod:: ResourceRelationshipReceiver.deleted_resource_relationship



Bin Receiver
------------

.. autoclass:: BinReceiver
   :show-inheritance:

   .. automethod:: BinReceiver.new_bin

   .. automethod:: BinReceiver.new_ancestor_bin

   .. automethod:: BinReceiver.new_descendant_bin

   .. automethod:: BinReceiver.changed_bin

   .. automethod:: BinReceiver.deleted_bin

   .. automethod:: BinReceiver.deleted_ancestor_bin

   .. automethod:: BinReceiver.deleted_descendant_bin



