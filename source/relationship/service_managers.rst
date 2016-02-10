
.. currentmodule:: dlkit.services.relationship
.. automodule:: dlkit.services.relationship

Service Managers
================


Relationship Profile
--------------------

.. autoclass:: RelationshipProfile
   :show-inheritance:

   .. automethod:: RelationshipProfile.supports_relationship_lookup

   .. automethod:: RelationshipProfile.supports_relationship_query

   .. automethod:: RelationshipProfile.supports_relationship_admin

   .. automethod:: RelationshipProfile.supports_family_lookup

   .. automethod:: RelationshipProfile.supports_family_admin

   .. automethod:: RelationshipProfile.supports_family_hierarchy

   .. automethod:: RelationshipProfile.supports_family_hierarchy_design

   .. autoattribute:: RelationshipProfile.relationship_record_types

   .. autoattribute:: RelationshipProfile.relationship_search_record_types

   .. autoattribute:: RelationshipProfile.family_record_types

   .. autoattribute:: RelationshipProfile.family_search_record_types

Relationship Manager
--------------------

.. autoclass:: RelationshipManager
   :show-inheritance:

   .. autoattribute:: RelationshipManager.relationship_batch_manager

   .. autoattribute:: RelationshipManager.relationship_rules_manager



Family Lookup Methods
---------------------

   .. automethod:: RelationshipManager.can_lookup_families

   .. automethod:: RelationshipManager.use_comparative_family_view

   .. automethod:: RelationshipManager.use_plenary_family_view

   .. automethod:: RelationshipManager.get_family

   .. automethod:: RelationshipManager.get_families_by_ids

   .. automethod:: RelationshipManager.get_families_by_genus_type

   .. automethod:: RelationshipManager.get_families_by_parent_genus_type

   .. automethod:: RelationshipManager.get_families_by_record_type

   .. automethod:: RelationshipManager.get_families_by_provider

   .. autoattribute:: RelationshipManager.families



Family Admin Methods
--------------------

   .. automethod:: RelationshipManager.can_create_families

   .. automethod:: RelationshipManager.can_create_family_with_record_types

   .. automethod:: RelationshipManager.get_family_form_for_create

   .. automethod:: RelationshipManager.create_family

   .. automethod:: RelationshipManager.can_update_families

   .. automethod:: RelationshipManager.get_family_form_for_update

   .. automethod:: RelationshipManager.update_family

   .. automethod:: RelationshipManager.can_delete_families

   .. automethod:: RelationshipManager.delete_family

   .. automethod:: RelationshipManager.can_manage_family_aliases

   .. automethod:: RelationshipManager.alias_family



Family Hierarchy Methods
------------------------

   .. autoattribute:: RelationshipManager.family_hierarchy_id

   .. autoattribute:: RelationshipManager.family_hierarchy

   .. automethod:: RelationshipManager.can_access_family_hierarchy

   .. automethod:: RelationshipManager.use_comparative_family_view

   .. automethod:: RelationshipManager.use_plenary_family_view

   .. autoattribute:: RelationshipManager.root_family_ids

   .. autoattribute:: RelationshipManager.root_families

   .. automethod:: RelationshipManager.has_parent_families

   .. automethod:: RelationshipManager.is_parent_of_family

   .. automethod:: RelationshipManager.get_parent_family_ids

   .. automethod:: RelationshipManager.get_parent_families

   .. automethod:: RelationshipManager.is_ancestor_of_family

   .. automethod:: RelationshipManager.has_child_families

   .. automethod:: RelationshipManager.is_child_of_family

   .. automethod:: RelationshipManager.get_child_family_ids

   .. automethod:: RelationshipManager.get_child_families

   .. automethod:: RelationshipManager.is_descendant_of_family

   .. automethod:: RelationshipManager.get_family_node_ids

   .. automethod:: RelationshipManager.get_family_nodes



Family Hierarchy Design Methods
-------------------------------

   .. autoattribute:: RelationshipManager.family_hierarchy_id

   .. autoattribute:: RelationshipManager.family_hierarchy

   .. automethod:: RelationshipManager.can_modify_family_hierarchy

   .. automethod:: RelationshipManager.add_root_family

   .. automethod:: RelationshipManager.remove_root_family

   .. automethod:: RelationshipManager.add_child_family

   .. automethod:: RelationshipManager.remove_child_family

   .. automethod:: RelationshipManager.remove_child_families



