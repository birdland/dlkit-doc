.. currentmodule:: dlkit.relationship.queries
.. automodule:: dlkit.relationship.queries

Queries
=======


Relationship Query
------------------

.. autoclass:: RelationshipQuery
   :show-inheritance:

   .. automethod:: RelationshipQuery.match_source_id

   .. autoattribute:: RelationshipQuery.source_id_terms

   .. automethod:: RelationshipQuery.match_destination_id

   .. autoattribute:: RelationshipQuery.destination_id_terms

   .. automethod:: RelationshipQuery.match_same_peer_id

   .. autoattribute:: RelationshipQuery.same_peer_id_terms

   .. automethod:: RelationshipQuery.match_family_id

   .. autoattribute:: RelationshipQuery.family_id_terms

   .. automethod:: RelationshipQuery.supports_family_query

   .. autoattribute:: RelationshipQuery.family_query

   .. autoattribute:: RelationshipQuery.family_terms

   .. automethod:: RelationshipQuery.get_relationship_query_record



Family Query
------------

.. autoclass:: FamilyQuery
   :show-inheritance:

   .. automethod:: FamilyQuery.match_relationship_id

   .. autoattribute:: FamilyQuery.relationship_id_terms

   .. automethod:: FamilyQuery.supports_relationship_query

   .. autoattribute:: FamilyQuery.relationship_query

   .. automethod:: FamilyQuery.match_any_relationship

   .. autoattribute:: FamilyQuery.relationship_terms

   .. automethod:: FamilyQuery.match_ancestor_family_id

   .. autoattribute:: FamilyQuery.ancestor_family_id_terms

   .. automethod:: FamilyQuery.supports_ancestor_family_query

   .. autoattribute:: FamilyQuery.ancestor_family_query

   .. automethod:: FamilyQuery.match_any_ancestor_family

   .. autoattribute:: FamilyQuery.ancestor_family_terms

   .. automethod:: FamilyQuery.match_descendant_family_id

   .. autoattribute:: FamilyQuery.descendant_family_id_terms

   .. automethod:: FamilyQuery.supports_descendant_family_query

   .. autoattribute:: FamilyQuery.descendant_family_query

   .. automethod:: FamilyQuery.match_any_descendant_family

   .. autoattribute:: FamilyQuery.descendant_family_terms

   .. automethod:: FamilyQuery.get_family_query_record



