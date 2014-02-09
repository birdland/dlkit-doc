.. currentmodule:: dlkit.resource.queries
.. automodule:: dlkit.resource.queries

Queries
=======


Resource Query
--------------

.. autoclass:: ResourceQuery
   :show-inheritance:

   .. automethod:: ResourceQuery.match_group

   .. autoattribute:: ResourceQuery.group_terms

   .. automethod:: ResourceQuery.match_demographic

   .. autoattribute:: ResourceQuery.demographic_terms

   .. automethod:: ResourceQuery.match_containing_group_id

   .. autoattribute:: ResourceQuery.containing_group_id_terms

   .. automethod:: ResourceQuery.supports_containing_group_query

   .. autoattribute:: ResourceQuery.containing_group_query

   .. automethod:: ResourceQuery.match_any_containing_group

   .. autoattribute:: ResourceQuery.containing_group_terms

   .. automethod:: ResourceQuery.match_avatar_id

   .. autoattribute:: ResourceQuery.avatar_id_terms

   .. automethod:: ResourceQuery.supports_avatar_query

   .. autoattribute:: ResourceQuery.avatar_query

   .. automethod:: ResourceQuery.match_any_avatar

   .. autoattribute:: ResourceQuery.avatar_terms

   .. automethod:: ResourceQuery.match_agent_id

   .. autoattribute:: ResourceQuery.agent_id_terms

   .. automethod:: ResourceQuery.supports_agent_query

   .. autoattribute:: ResourceQuery.agent_query

   .. automethod:: ResourceQuery.match_any_agent

   .. autoattribute:: ResourceQuery.agent_terms

   .. automethod:: ResourceQuery.match_resource_relationship_id

   .. autoattribute:: ResourceQuery.resource_relationship_id_terms

   .. automethod:: ResourceQuery.supports_resource_relationship_query

   .. autoattribute:: ResourceQuery.resource_relationship_query

   .. automethod:: ResourceQuery.match_any_resource_relationship

   .. autoattribute:: ResourceQuery.resource_relationship_terms

   .. automethod:: ResourceQuery.match_bin_id

   .. autoattribute:: ResourceQuery.bin_id_terms

   .. automethod:: ResourceQuery.supports_bin_query

   .. autoattribute:: ResourceQuery.bin_query

   .. autoattribute:: ResourceQuery.bin_terms

   .. automethod:: ResourceQuery.get_resource_query_record



Resource Relationship Query
---------------------------

.. autoclass:: ResourceRelationshipQuery
   :show-inheritance:

   .. automethod:: ResourceRelationshipQuery.match_source_resource_id

   .. autoattribute:: ResourceRelationshipQuery.source_resource_id_terms

   .. automethod:: ResourceRelationshipQuery.supports_source_resource_query

   .. autoattribute:: ResourceRelationshipQuery.source_resource_query

   .. autoattribute:: ResourceRelationshipQuery.source_resource_terms

   .. automethod:: ResourceRelationshipQuery.match_destination_resource_id

   .. autoattribute:: ResourceRelationshipQuery.destination_resource_id_terms

   .. automethod:: ResourceRelationshipQuery.supports_destination_resource_query

   .. autoattribute:: ResourceRelationshipQuery.destination_resource_query

   .. autoattribute:: ResourceRelationshipQuery.destination_resource_terms

   .. automethod:: ResourceRelationshipQuery.match_same_resource

   .. autoattribute:: ResourceRelationshipQuery.same_resource_terms

   .. automethod:: ResourceRelationshipQuery.match_bin_id

   .. autoattribute:: ResourceRelationshipQuery.bin_id_terms

   .. automethod:: ResourceRelationshipQuery.supports_bin_query

   .. autoattribute:: ResourceRelationshipQuery.bin_query

   .. autoattribute:: ResourceRelationshipQuery.bin_terms

   .. automethod:: ResourceRelationshipQuery.get_resource_relationship_query_record



Bin Query
---------

.. autoclass:: BinQuery
   :show-inheritance:

   .. automethod:: BinQuery.match_resource_id

   .. autoattribute:: BinQuery.resource_id_terms

   .. automethod:: BinQuery.supports_resource_query

   .. autoattribute:: BinQuery.resource_query

   .. automethod:: BinQuery.match_any_resource

   .. autoattribute:: BinQuery.resource_terms

   .. automethod:: BinQuery.match_ancestor_bin_id

   .. autoattribute:: BinQuery.ancestor_bin_id_terms

   .. automethod:: BinQuery.supports_ancestor_bin_query

   .. autoattribute:: BinQuery.ancestor_bin_query

   .. automethod:: BinQuery.match_any_ancestor_bin

   .. autoattribute:: BinQuery.ancestor_bin_terms

   .. automethod:: BinQuery.match_descendant_bin_id

   .. autoattribute:: BinQuery.descendant_bin_id_terms

   .. automethod:: BinQuery.supports_descendant_bin_query

   .. autoattribute:: BinQuery.descendant_bin_query

   .. automethod:: BinQuery.match_any_descendant_bin

   .. autoattribute:: BinQuery.descendant_bin_terms

   .. automethod:: BinQuery.get_bin_query_record



