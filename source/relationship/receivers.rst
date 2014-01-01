.. currentmodule:: dlkit.relationship.receivers
.. automodule:: dlkit.relationship.receivers

Receivers
=========


Relationship Receiver
---------------------

.. autoclass:: RelationshipReceiver
   :show-inheritance:

   .. automethod:: RelationshipReceiver.new_relationship

   .. automethod:: RelationshipReceiver.changed_relationship

   .. automethod:: RelationshipReceiver.deleted_relationship



Family Receiver
---------------

.. autoclass:: FamilyReceiver
   :show-inheritance:

   .. automethod:: FamilyReceiver.new_family

   .. automethod:: FamilyReceiver.new_ancestor_family

   .. automethod:: FamilyReceiver.new_descendant_family

   .. automethod:: FamilyReceiver.changed_family

   .. automethod:: FamilyReceiver.deleted_family

   .. automethod:: FamilyReceiver.deleted_ancestor_family

   .. automethod:: FamilyReceiver.deleted_descendant_family



