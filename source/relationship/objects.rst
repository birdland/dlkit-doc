.. currentmodule:: dlkit.relationship.objects
.. automodule:: dlkit.relationship.objects

Objects
=======


Relationship
------------

.. autoclass:: Relationship
   :show-inheritance:

.. autoattribute:: Relationship.source_id

.. autoattribute:: Relationship.destination_id

.. automethod:: Relationship.get_relationship_record



Relationship Form
-----------------

.. autoclass:: RelationshipForm
   :show-inheritance:

.. automethod:: RelationshipForm.get_relationship_form_record



Relationship List
-----------------

.. autoclass:: RelationshipList
   :show-inheritance:

.. autoattribute:: RelationshipList.next_relationship

.. automethod:: RelationshipList.get_next_relationships



Family Form
-----------

.. autoclass:: FamilyForm
   :show-inheritance:

.. automethod:: FamilyForm.get_family_form_record



Family List
-----------

.. autoclass:: FamilyList
   :show-inheritance:

.. autoattribute:: FamilyList.next_family

.. automethod:: FamilyList.get_next_families



Family Node
-----------

.. autoclass:: FamilyNode
   :show-inheritance:

.. autoattribute:: FamilyNode.family

.. autoattribute:: FamilyNode.parent_family_nodes

.. autoattribute:: FamilyNode.child_family_nodes



Family Node List
----------------

.. autoclass:: FamilyNodeList
   :show-inheritance:

.. autoattribute:: FamilyNodeList.next_family_node

.. automethod:: FamilyNodeList.get_next_family_nodes



