
.. currentmodule:: dlkit.relationship.searches
.. automodule:: dlkit.relationship.searches

Searches
========


Relationship Search
-------------------

.. autoclass:: RelationshipSearch
   :show-inheritance:

   .. automethod:: RelationshipSearch.search_among_relationships

   .. automethod:: RelationshipSearch.order_relationship_results

   .. automethod:: RelationshipSearch.get_relationship_search_record

Relationship Search Results
---------------------------

.. autoclass:: RelationshipSearchResults
   :show-inheritance:

   .. autoattribute:: RelationshipSearchResults.relationships

   .. autoattribute:: RelationshipSearchResults.relationship_query_inspector

   .. automethod:: RelationshipSearchResults.get_relationship_search_results_record

Family Search
-------------

.. autoclass:: FamilySearch
   :show-inheritance:

   .. automethod:: FamilySearch.search_among_families

   .. automethod:: FamilySearch.order_family_results

   .. automethod:: FamilySearch.get_family_search_record

Family Search Results
---------------------

.. autoclass:: FamilySearchResults
   :show-inheritance:

   .. autoattribute:: FamilySearchResults.families

   .. autoattribute:: FamilySearchResults.family_query_inspector

   .. automethod:: FamilySearchResults.get_family_search_results_record

