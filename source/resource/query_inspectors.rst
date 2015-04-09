.. currentmodule:: dlkit.resource.query_inspectors
.. automodule:: dlkit.resource.query_inspectors

Query Inspectors
================


Resource Query Inspector
------------------------

.. autoclass:: ResourceQueryInspector
   :show-inheritance:

   .. autoattribute:: ResourceQueryInspector.group_terms

   .. autoattribute:: ResourceQueryInspector.demographic_terms

   .. autoattribute:: ResourceQueryInspector.containing_group_id_terms

   .. autoattribute:: ResourceQueryInspector.containing_group_terms

   .. autoattribute:: ResourceQueryInspector.avatar_id_terms

   .. autoattribute:: ResourceQueryInspector.avatar_terms

   .. autoattribute:: ResourceQueryInspector.agent_id_terms

   .. autoattribute:: ResourceQueryInspector.agent_terms

   .. autoattribute:: ResourceQueryInspector.resource_relationship_id_terms

   .. autoattribute:: ResourceQueryInspector.resource_relationship_terms

   .. autoattribute:: ResourceQueryInspector.bin_id_terms

   .. autoattribute:: ResourceQueryInspector.bin_terms

   .. automethod:: ResourceQueryInspector.get_resource_query_inspector_record



Resource Relationship Query Inspector
-------------------------------------

.. autoclass:: ResourceRelationshipQueryInspector
   :show-inheritance:

   .. autoattribute:: ResourceRelationshipQueryInspector.source_resource_id_terms

   .. autoattribute:: ResourceRelationshipQueryInspector.source_resource_terms

   .. autoattribute:: ResourceRelationshipQueryInspector.destination_resource_id_terms

   .. autoattribute:: ResourceRelationshipQueryInspector.destination_resource_terms

   .. autoattribute:: ResourceRelationshipQueryInspector.same_resource_terms

   .. autoattribute:: ResourceRelationshipQueryInspector.bin_id_terms

   .. autoattribute:: ResourceRelationshipQueryInspector.bin_terms

   .. automethod:: ResourceRelationshipQueryInspector.get_resource_relationship_query_inspector_record



Bin Query Inspector
-------------------

.. autoclass:: BinQueryInspector
   :show-inheritance:

   .. autoattribute:: BinQueryInspector.resource_id_terms

   .. autoattribute:: BinQueryInspector.resource_terms

   .. autoattribute:: BinQueryInspector.ancestor_bin_id_terms

   .. autoattribute:: BinQueryInspector.ancestor_bin_terms

   .. autoattribute:: BinQueryInspector.descendant_bin_id_terms

   .. autoattribute:: BinQueryInspector.descendant_bin_terms

   .. automethod:: BinQueryInspector.get_bin_query_inspector_record



