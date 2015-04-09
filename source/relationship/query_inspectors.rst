.. currentmodule:: dlkit.relationship.query_inspectors
.. automodule:: dlkit.relationship.query_inspectors

Query Inspectors
================


Relationship Query Inspector
----------------------------

.. autoclass:: RelationshipQueryInspector
   :show-inheritance:

   .. autoattribute:: RelationshipQueryInspector.source_id_terms

   .. autoattribute:: RelationshipQueryInspector.destination_id_terms

   .. autoattribute:: RelationshipQueryInspector.same_peer_id_terms

   .. autoattribute:: RelationshipQueryInspector.family_id_terms

   .. autoattribute:: RelationshipQueryInspector.family_terms

   .. automethod:: RelationshipQueryInspector.get_relationship_query_inspector_record



Family Query Inspector
----------------------

.. autoclass:: FamilyQueryInspector
   :show-inheritance:

   .. autoattribute:: FamilyQueryInspector.relationship_id_terms

   .. autoattribute:: FamilyQueryInspector.relationship_terms

   .. autoattribute:: FamilyQueryInspector.ancestor_family_id_terms

   .. autoattribute:: FamilyQueryInspector.ancestor_family_terms

   .. autoattribute:: FamilyQueryInspector.descendant_family_id_terms

   .. autoattribute:: FamilyQueryInspector.descendant_family_terms

   .. automethod:: FamilyQueryInspector.get_family_query_inspector_record



