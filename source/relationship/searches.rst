
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



Family Lookup Methods
---------------------

   .. automethod:: FamilyLookupSession.can_lookup_families

   .. automethod:: FamilyLookupSession.use_comparative_family_view

   .. automethod:: FamilyLookupSession.use_plenary_family_view

   .. automethod:: FamilyLookupSession.get_family

   .. automethod:: FamilyLookupSession.get_families_by_ids

   .. automethod:: FamilyLookupSession.get_families_by_genus_type

   .. automethod:: FamilyLookupSession.get_families_by_parent_genus_type

   .. automethod:: FamilyLookupSession.get_families_by_record_type

   .. automethod:: FamilyLookupSession.get_families_by_provider

   .. autoattribute:: FamilyLookupSession.families



Family Admin Methods
--------------------

   .. automethod:: FamilyAdminSession.can_create_families

   .. automethod:: FamilyAdminSession.can_create_family_with_record_types

   .. automethod:: FamilyAdminSession.get_family_form_for_create

   .. automethod:: FamilyAdminSession.create_family

   .. automethod:: FamilyAdminSession.can_update_families

   .. automethod:: FamilyAdminSession.get_family_form_for_update

   .. automethod:: FamilyAdminSession.update_family

   .. automethod:: FamilyAdminSession.can_delete_families

   .. automethod:: FamilyAdminSession.delete_family

   .. automethod:: FamilyAdminSession.can_manage_family_aliases

   .. automethod:: FamilyAdminSession.alias_family



Family Hierarchy Methods
------------------------

   .. autoattribute:: FamilyHierarchySession.family_hierarchy_id

   .. autoattribute:: FamilyHierarchySession.family_hierarchy

   .. automethod:: FamilyHierarchySession.can_access_family_hierarchy

   .. automethod:: FamilyHierarchySession.use_comparative_family_view

   .. automethod:: FamilyHierarchySession.use_plenary_family_view

   .. autoattribute:: FamilyHierarchySession.root_family_ids

   .. autoattribute:: FamilyHierarchySession.root_families

   .. automethod:: FamilyHierarchySession.has_parent_families

   .. automethod:: FamilyHierarchySession.is_parent_of_family

   .. automethod:: FamilyHierarchySession.get_parent_family_ids

   .. automethod:: FamilyHierarchySession.get_parent_families

   .. automethod:: FamilyHierarchySession.is_ancestor_of_family

   .. automethod:: FamilyHierarchySession.has_child_families

   .. automethod:: FamilyHierarchySession.is_child_of_family

   .. automethod:: FamilyHierarchySession.get_child_family_ids

   .. automethod:: FamilyHierarchySession.get_child_families

   .. automethod:: FamilyHierarchySession.is_descendant_of_family

   .. automethod:: FamilyHierarchySession.get_family_node_ids

   .. automethod:: FamilyHierarchySession.get_family_nodes



Family Hierarchy Design Methods
-------------------------------

   .. autoattribute:: FamilyHierarchyDesignSession.family_hierarchy_id

   .. autoattribute:: FamilyHierarchyDesignSession.family_hierarchy

   .. automethod:: FamilyHierarchyDesignSession.can_modify_family_hierarchy

   .. automethod:: FamilyHierarchyDesignSession.add_root_family

   .. automethod:: FamilyHierarchyDesignSession.remove_root_family

   .. automethod:: FamilyHierarchyDesignSession.add_child_family

   .. automethod:: FamilyHierarchyDesignSession.remove_child_family

   .. automethod:: FamilyHierarchyDesignSession.remove_child_families



Relationship Lookup Methods
---------------------------

   .. autoattribute:: RelationshipLookupSession.family_id

   .. autoattribute:: RelationshipLookupSession.family

   .. automethod:: RelationshipLookupSession.can_lookup_relationships

   .. automethod:: RelationshipLookupSession.use_comparative_relationship_view

   .. automethod:: RelationshipLookupSession.use_plenary_relationship_view

   .. automethod:: RelationshipLookupSession.use_federated_family_view

   .. automethod:: RelationshipLookupSession.use_isolated_family_view

   .. automethod:: RelationshipLookupSession.use_effective_relationship_view

   .. automethod:: RelationshipLookupSession.use_any_effective_relationship_view

   .. automethod:: RelationshipLookupSession.get_relationship

   .. automethod:: RelationshipLookupSession.get_relationships_by_ids

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type

   .. automethod:: RelationshipLookupSession.get_relationships_by_parent_genus_type

   .. automethod:: RelationshipLookupSession.get_relationships_by_record_type

   .. automethod:: RelationshipLookupSession.get_relationships_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_source

   .. automethod:: RelationshipLookupSession.get_relationships_for_source_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_source

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_destination

   .. automethod:: RelationshipLookupSession.get_relationships_for_destination_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_destination

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_destination_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_peers

   .. automethod:: RelationshipLookupSession.get_relationships_for_peers_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_peers

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_peers_on_date

   .. autoattribute:: RelationshipLookupSession.relationships



Relationship Query Methods
--------------------------

   .. autoattribute:: RelationshipQuerySession.family_id

   .. autoattribute:: RelationshipQuerySession.family

   .. automethod:: RelationshipQuerySession.use_federated_family_view

   .. automethod:: RelationshipQuerySession.use_isolated_family_view

   .. automethod:: RelationshipQuerySession.can_search_relationships

   .. autoattribute:: RelationshipQuerySession.relationship_query

   .. automethod:: RelationshipQuerySession.get_relationships_by_query



Relationship Admin Methods
--------------------------

   .. autoattribute:: RelationshipAdminSession.family_id

   .. autoattribute:: RelationshipAdminSession.family

   .. automethod:: RelationshipAdminSession.can_create_relationships

   .. automethod:: RelationshipAdminSession.can_create_relationship_with_record_types

   .. automethod:: RelationshipAdminSession.get_relationship_form_for_create

   .. automethod:: RelationshipAdminSession.create_relationship

   .. automethod:: RelationshipAdminSession.can_update_relationships

   .. automethod:: RelationshipAdminSession.get_relationship_form_for_update

   .. automethod:: RelationshipAdminSession.update_relationship

   .. automethod:: RelationshipAdminSession.can_delete_relationships

   .. automethod:: RelationshipAdminSession.delete_relationship

   .. automethod:: RelationshipAdminSession.can_manage_relationship_aliases

   .. automethod:: RelationshipAdminSession.alias_relationship



Relationship Search Results
---------------------------

.. autoclass:: RelationshipSearchResults
   :show-inheritance:

   .. autoattribute:: RelationshipSearchResults.relationships

   .. autoattribute:: RelationshipSearchResults.relationship_query_inspector

   .. automethod:: RelationshipSearchResults.get_relationship_search_results_record



Family Lookup Methods
---------------------

   .. automethod:: FamilyLookupSession.can_lookup_families

   .. automethod:: FamilyLookupSession.use_comparative_family_view

   .. automethod:: FamilyLookupSession.use_plenary_family_view

   .. automethod:: FamilyLookupSession.get_family

   .. automethod:: FamilyLookupSession.get_families_by_ids

   .. automethod:: FamilyLookupSession.get_families_by_genus_type

   .. automethod:: FamilyLookupSession.get_families_by_parent_genus_type

   .. automethod:: FamilyLookupSession.get_families_by_record_type

   .. automethod:: FamilyLookupSession.get_families_by_provider

   .. autoattribute:: FamilyLookupSession.families



Family Admin Methods
--------------------

   .. automethod:: FamilyAdminSession.can_create_families

   .. automethod:: FamilyAdminSession.can_create_family_with_record_types

   .. automethod:: FamilyAdminSession.get_family_form_for_create

   .. automethod:: FamilyAdminSession.create_family

   .. automethod:: FamilyAdminSession.can_update_families

   .. automethod:: FamilyAdminSession.get_family_form_for_update

   .. automethod:: FamilyAdminSession.update_family

   .. automethod:: FamilyAdminSession.can_delete_families

   .. automethod:: FamilyAdminSession.delete_family

   .. automethod:: FamilyAdminSession.can_manage_family_aliases

   .. automethod:: FamilyAdminSession.alias_family



Family Hierarchy Methods
------------------------

   .. autoattribute:: FamilyHierarchySession.family_hierarchy_id

   .. autoattribute:: FamilyHierarchySession.family_hierarchy

   .. automethod:: FamilyHierarchySession.can_access_family_hierarchy

   .. automethod:: FamilyHierarchySession.use_comparative_family_view

   .. automethod:: FamilyHierarchySession.use_plenary_family_view

   .. autoattribute:: FamilyHierarchySession.root_family_ids

   .. autoattribute:: FamilyHierarchySession.root_families

   .. automethod:: FamilyHierarchySession.has_parent_families

   .. automethod:: FamilyHierarchySession.is_parent_of_family

   .. automethod:: FamilyHierarchySession.get_parent_family_ids

   .. automethod:: FamilyHierarchySession.get_parent_families

   .. automethod:: FamilyHierarchySession.is_ancestor_of_family

   .. automethod:: FamilyHierarchySession.has_child_families

   .. automethod:: FamilyHierarchySession.is_child_of_family

   .. automethod:: FamilyHierarchySession.get_child_family_ids

   .. automethod:: FamilyHierarchySession.get_child_families

   .. automethod:: FamilyHierarchySession.is_descendant_of_family

   .. automethod:: FamilyHierarchySession.get_family_node_ids

   .. automethod:: FamilyHierarchySession.get_family_nodes



Family Hierarchy Design Methods
-------------------------------

   .. autoattribute:: FamilyHierarchyDesignSession.family_hierarchy_id

   .. autoattribute:: FamilyHierarchyDesignSession.family_hierarchy

   .. automethod:: FamilyHierarchyDesignSession.can_modify_family_hierarchy

   .. automethod:: FamilyHierarchyDesignSession.add_root_family

   .. automethod:: FamilyHierarchyDesignSession.remove_root_family

   .. automethod:: FamilyHierarchyDesignSession.add_child_family

   .. automethod:: FamilyHierarchyDesignSession.remove_child_family

   .. automethod:: FamilyHierarchyDesignSession.remove_child_families



Relationship Lookup Methods
---------------------------

   .. autoattribute:: RelationshipLookupSession.family_id

   .. autoattribute:: RelationshipLookupSession.family

   .. automethod:: RelationshipLookupSession.can_lookup_relationships

   .. automethod:: RelationshipLookupSession.use_comparative_relationship_view

   .. automethod:: RelationshipLookupSession.use_plenary_relationship_view

   .. automethod:: RelationshipLookupSession.use_federated_family_view

   .. automethod:: RelationshipLookupSession.use_isolated_family_view

   .. automethod:: RelationshipLookupSession.use_effective_relationship_view

   .. automethod:: RelationshipLookupSession.use_any_effective_relationship_view

   .. automethod:: RelationshipLookupSession.get_relationship

   .. automethod:: RelationshipLookupSession.get_relationships_by_ids

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type

   .. automethod:: RelationshipLookupSession.get_relationships_by_parent_genus_type

   .. automethod:: RelationshipLookupSession.get_relationships_by_record_type

   .. automethod:: RelationshipLookupSession.get_relationships_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_source

   .. automethod:: RelationshipLookupSession.get_relationships_for_source_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_source

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_destination

   .. automethod:: RelationshipLookupSession.get_relationships_for_destination_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_destination

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_destination_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_peers

   .. automethod:: RelationshipLookupSession.get_relationships_for_peers_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_peers

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_peers_on_date

   .. autoattribute:: RelationshipLookupSession.relationships



Relationship Query Methods
--------------------------

   .. autoattribute:: RelationshipQuerySession.family_id

   .. autoattribute:: RelationshipQuerySession.family

   .. automethod:: RelationshipQuerySession.use_federated_family_view

   .. automethod:: RelationshipQuerySession.use_isolated_family_view

   .. automethod:: RelationshipQuerySession.can_search_relationships

   .. autoattribute:: RelationshipQuerySession.relationship_query

   .. automethod:: RelationshipQuerySession.get_relationships_by_query



Relationship Admin Methods
--------------------------

   .. autoattribute:: RelationshipAdminSession.family_id

   .. autoattribute:: RelationshipAdminSession.family

   .. automethod:: RelationshipAdminSession.can_create_relationships

   .. automethod:: RelationshipAdminSession.can_create_relationship_with_record_types

   .. automethod:: RelationshipAdminSession.get_relationship_form_for_create

   .. automethod:: RelationshipAdminSession.create_relationship

   .. automethod:: RelationshipAdminSession.can_update_relationships

   .. automethod:: RelationshipAdminSession.get_relationship_form_for_update

   .. automethod:: RelationshipAdminSession.update_relationship

   .. automethod:: RelationshipAdminSession.can_delete_relationships

   .. automethod:: RelationshipAdminSession.delete_relationship

   .. automethod:: RelationshipAdminSession.can_manage_relationship_aliases

   .. automethod:: RelationshipAdminSession.alias_relationship



Family Search
-------------

.. autoclass:: FamilySearch
   :show-inheritance:

   .. automethod:: FamilySearch.search_among_families

   .. automethod:: FamilySearch.order_family_results

   .. automethod:: FamilySearch.get_family_search_record



Family Lookup Methods
---------------------

   .. automethod:: FamilyLookupSession.can_lookup_families

   .. automethod:: FamilyLookupSession.use_comparative_family_view

   .. automethod:: FamilyLookupSession.use_plenary_family_view

   .. automethod:: FamilyLookupSession.get_family

   .. automethod:: FamilyLookupSession.get_families_by_ids

   .. automethod:: FamilyLookupSession.get_families_by_genus_type

   .. automethod:: FamilyLookupSession.get_families_by_parent_genus_type

   .. automethod:: FamilyLookupSession.get_families_by_record_type

   .. automethod:: FamilyLookupSession.get_families_by_provider

   .. autoattribute:: FamilyLookupSession.families



Family Admin Methods
--------------------

   .. automethod:: FamilyAdminSession.can_create_families

   .. automethod:: FamilyAdminSession.can_create_family_with_record_types

   .. automethod:: FamilyAdminSession.get_family_form_for_create

   .. automethod:: FamilyAdminSession.create_family

   .. automethod:: FamilyAdminSession.can_update_families

   .. automethod:: FamilyAdminSession.get_family_form_for_update

   .. automethod:: FamilyAdminSession.update_family

   .. automethod:: FamilyAdminSession.can_delete_families

   .. automethod:: FamilyAdminSession.delete_family

   .. automethod:: FamilyAdminSession.can_manage_family_aliases

   .. automethod:: FamilyAdminSession.alias_family



Family Hierarchy Methods
------------------------

   .. autoattribute:: FamilyHierarchySession.family_hierarchy_id

   .. autoattribute:: FamilyHierarchySession.family_hierarchy

   .. automethod:: FamilyHierarchySession.can_access_family_hierarchy

   .. automethod:: FamilyHierarchySession.use_comparative_family_view

   .. automethod:: FamilyHierarchySession.use_plenary_family_view

   .. autoattribute:: FamilyHierarchySession.root_family_ids

   .. autoattribute:: FamilyHierarchySession.root_families

   .. automethod:: FamilyHierarchySession.has_parent_families

   .. automethod:: FamilyHierarchySession.is_parent_of_family

   .. automethod:: FamilyHierarchySession.get_parent_family_ids

   .. automethod:: FamilyHierarchySession.get_parent_families

   .. automethod:: FamilyHierarchySession.is_ancestor_of_family

   .. automethod:: FamilyHierarchySession.has_child_families

   .. automethod:: FamilyHierarchySession.is_child_of_family

   .. automethod:: FamilyHierarchySession.get_child_family_ids

   .. automethod:: FamilyHierarchySession.get_child_families

   .. automethod:: FamilyHierarchySession.is_descendant_of_family

   .. automethod:: FamilyHierarchySession.get_family_node_ids

   .. automethod:: FamilyHierarchySession.get_family_nodes



Family Hierarchy Design Methods
-------------------------------

   .. autoattribute:: FamilyHierarchyDesignSession.family_hierarchy_id

   .. autoattribute:: FamilyHierarchyDesignSession.family_hierarchy

   .. automethod:: FamilyHierarchyDesignSession.can_modify_family_hierarchy

   .. automethod:: FamilyHierarchyDesignSession.add_root_family

   .. automethod:: FamilyHierarchyDesignSession.remove_root_family

   .. automethod:: FamilyHierarchyDesignSession.add_child_family

   .. automethod:: FamilyHierarchyDesignSession.remove_child_family

   .. automethod:: FamilyHierarchyDesignSession.remove_child_families



Relationship Lookup Methods
---------------------------

   .. autoattribute:: RelationshipLookupSession.family_id

   .. autoattribute:: RelationshipLookupSession.family

   .. automethod:: RelationshipLookupSession.can_lookup_relationships

   .. automethod:: RelationshipLookupSession.use_comparative_relationship_view

   .. automethod:: RelationshipLookupSession.use_plenary_relationship_view

   .. automethod:: RelationshipLookupSession.use_federated_family_view

   .. automethod:: RelationshipLookupSession.use_isolated_family_view

   .. automethod:: RelationshipLookupSession.use_effective_relationship_view

   .. automethod:: RelationshipLookupSession.use_any_effective_relationship_view

   .. automethod:: RelationshipLookupSession.get_relationship

   .. automethod:: RelationshipLookupSession.get_relationships_by_ids

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type

   .. automethod:: RelationshipLookupSession.get_relationships_by_parent_genus_type

   .. automethod:: RelationshipLookupSession.get_relationships_by_record_type

   .. automethod:: RelationshipLookupSession.get_relationships_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_source

   .. automethod:: RelationshipLookupSession.get_relationships_for_source_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_source

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_destination

   .. automethod:: RelationshipLookupSession.get_relationships_for_destination_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_destination

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_destination_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_peers

   .. automethod:: RelationshipLookupSession.get_relationships_for_peers_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_peers

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_peers_on_date

   .. autoattribute:: RelationshipLookupSession.relationships



Relationship Query Methods
--------------------------

   .. autoattribute:: RelationshipQuerySession.family_id

   .. autoattribute:: RelationshipQuerySession.family

   .. automethod:: RelationshipQuerySession.use_federated_family_view

   .. automethod:: RelationshipQuerySession.use_isolated_family_view

   .. automethod:: RelationshipQuerySession.can_search_relationships

   .. autoattribute:: RelationshipQuerySession.relationship_query

   .. automethod:: RelationshipQuerySession.get_relationships_by_query



Relationship Admin Methods
--------------------------

   .. autoattribute:: RelationshipAdminSession.family_id

   .. autoattribute:: RelationshipAdminSession.family

   .. automethod:: RelationshipAdminSession.can_create_relationships

   .. automethod:: RelationshipAdminSession.can_create_relationship_with_record_types

   .. automethod:: RelationshipAdminSession.get_relationship_form_for_create

   .. automethod:: RelationshipAdminSession.create_relationship

   .. automethod:: RelationshipAdminSession.can_update_relationships

   .. automethod:: RelationshipAdminSession.get_relationship_form_for_update

   .. automethod:: RelationshipAdminSession.update_relationship

   .. automethod:: RelationshipAdminSession.can_delete_relationships

   .. automethod:: RelationshipAdminSession.delete_relationship

   .. automethod:: RelationshipAdminSession.can_manage_relationship_aliases

   .. automethod:: RelationshipAdminSession.alias_relationship



Family Search Results
---------------------

.. autoclass:: FamilySearchResults
   :show-inheritance:

   .. autoattribute:: FamilySearchResults.families

   .. autoattribute:: FamilySearchResults.family_query_inspector

   .. automethod:: FamilySearchResults.get_family_search_results_record



Family Lookup Methods
---------------------

   .. automethod:: FamilyLookupSession.can_lookup_families

   .. automethod:: FamilyLookupSession.use_comparative_family_view

   .. automethod:: FamilyLookupSession.use_plenary_family_view

   .. automethod:: FamilyLookupSession.get_family

   .. automethod:: FamilyLookupSession.get_families_by_ids

   .. automethod:: FamilyLookupSession.get_families_by_genus_type

   .. automethod:: FamilyLookupSession.get_families_by_parent_genus_type

   .. automethod:: FamilyLookupSession.get_families_by_record_type

   .. automethod:: FamilyLookupSession.get_families_by_provider

   .. autoattribute:: FamilyLookupSession.families



Family Admin Methods
--------------------

   .. automethod:: FamilyAdminSession.can_create_families

   .. automethod:: FamilyAdminSession.can_create_family_with_record_types

   .. automethod:: FamilyAdminSession.get_family_form_for_create

   .. automethod:: FamilyAdminSession.create_family

   .. automethod:: FamilyAdminSession.can_update_families

   .. automethod:: FamilyAdminSession.get_family_form_for_update

   .. automethod:: FamilyAdminSession.update_family

   .. automethod:: FamilyAdminSession.can_delete_families

   .. automethod:: FamilyAdminSession.delete_family

   .. automethod:: FamilyAdminSession.can_manage_family_aliases

   .. automethod:: FamilyAdminSession.alias_family



Family Hierarchy Methods
------------------------

   .. autoattribute:: FamilyHierarchySession.family_hierarchy_id

   .. autoattribute:: FamilyHierarchySession.family_hierarchy

   .. automethod:: FamilyHierarchySession.can_access_family_hierarchy

   .. automethod:: FamilyHierarchySession.use_comparative_family_view

   .. automethod:: FamilyHierarchySession.use_plenary_family_view

   .. autoattribute:: FamilyHierarchySession.root_family_ids

   .. autoattribute:: FamilyHierarchySession.root_families

   .. automethod:: FamilyHierarchySession.has_parent_families

   .. automethod:: FamilyHierarchySession.is_parent_of_family

   .. automethod:: FamilyHierarchySession.get_parent_family_ids

   .. automethod:: FamilyHierarchySession.get_parent_families

   .. automethod:: FamilyHierarchySession.is_ancestor_of_family

   .. automethod:: FamilyHierarchySession.has_child_families

   .. automethod:: FamilyHierarchySession.is_child_of_family

   .. automethod:: FamilyHierarchySession.get_child_family_ids

   .. automethod:: FamilyHierarchySession.get_child_families

   .. automethod:: FamilyHierarchySession.is_descendant_of_family

   .. automethod:: FamilyHierarchySession.get_family_node_ids

   .. automethod:: FamilyHierarchySession.get_family_nodes



Family Hierarchy Design Methods
-------------------------------

   .. autoattribute:: FamilyHierarchyDesignSession.family_hierarchy_id

   .. autoattribute:: FamilyHierarchyDesignSession.family_hierarchy

   .. automethod:: FamilyHierarchyDesignSession.can_modify_family_hierarchy

   .. automethod:: FamilyHierarchyDesignSession.add_root_family

   .. automethod:: FamilyHierarchyDesignSession.remove_root_family

   .. automethod:: FamilyHierarchyDesignSession.add_child_family

   .. automethod:: FamilyHierarchyDesignSession.remove_child_family

   .. automethod:: FamilyHierarchyDesignSession.remove_child_families



Relationship Lookup Methods
---------------------------

   .. autoattribute:: RelationshipLookupSession.family_id

   .. autoattribute:: RelationshipLookupSession.family

   .. automethod:: RelationshipLookupSession.can_lookup_relationships

   .. automethod:: RelationshipLookupSession.use_comparative_relationship_view

   .. automethod:: RelationshipLookupSession.use_plenary_relationship_view

   .. automethod:: RelationshipLookupSession.use_federated_family_view

   .. automethod:: RelationshipLookupSession.use_isolated_family_view

   .. automethod:: RelationshipLookupSession.use_effective_relationship_view

   .. automethod:: RelationshipLookupSession.use_any_effective_relationship_view

   .. automethod:: RelationshipLookupSession.get_relationship

   .. automethod:: RelationshipLookupSession.get_relationships_by_ids

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type

   .. automethod:: RelationshipLookupSession.get_relationships_by_parent_genus_type

   .. automethod:: RelationshipLookupSession.get_relationships_by_record_type

   .. automethod:: RelationshipLookupSession.get_relationships_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_source

   .. automethod:: RelationshipLookupSession.get_relationships_for_source_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_source

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_source_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_destination

   .. automethod:: RelationshipLookupSession.get_relationships_for_destination_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_destination

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_destination_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_for_peers

   .. automethod:: RelationshipLookupSession.get_relationships_for_peers_on_date

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_peers

   .. automethod:: RelationshipLookupSession.get_relationships_by_genus_type_for_peers_on_date

   .. autoattribute:: RelationshipLookupSession.relationships



Relationship Query Methods
--------------------------

   .. autoattribute:: RelationshipQuerySession.family_id

   .. autoattribute:: RelationshipQuerySession.family

   .. automethod:: RelationshipQuerySession.use_federated_family_view

   .. automethod:: RelationshipQuerySession.use_isolated_family_view

   .. automethod:: RelationshipQuerySession.can_search_relationships

   .. autoattribute:: RelationshipQuerySession.relationship_query

   .. automethod:: RelationshipQuerySession.get_relationships_by_query



Relationship Admin Methods
--------------------------

   .. autoattribute:: RelationshipAdminSession.family_id

   .. autoattribute:: RelationshipAdminSession.family

   .. automethod:: RelationshipAdminSession.can_create_relationships

   .. automethod:: RelationshipAdminSession.can_create_relationship_with_record_types

   .. automethod:: RelationshipAdminSession.get_relationship_form_for_create

   .. automethod:: RelationshipAdminSession.create_relationship

   .. automethod:: RelationshipAdminSession.can_update_relationships

   .. automethod:: RelationshipAdminSession.get_relationship_form_for_update

   .. automethod:: RelationshipAdminSession.update_relationship

   .. automethod:: RelationshipAdminSession.can_delete_relationships

   .. automethod:: RelationshipAdminSession.delete_relationship

   .. automethod:: RelationshipAdminSession.can_manage_relationship_aliases

   .. automethod:: RelationshipAdminSession.alias_relationship



