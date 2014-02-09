.. currentmodule:: dlkit.services.relationship
.. automodule:: dlkit.services.relationship

Services
========


Relationship Manager
--------------------

.. autoclass:: RelationshipManager
   :show-inheritance:

   .. autoattribute:: RelationshipManager.relationship_batch_manager

   .. autoattribute:: RelationshipManager.relationship_rules_manager



Relationship Profile Methods
____________________

   .. automethod:: RelationshipManager.supports_visible_federation

   .. automethod:: RelationshipManager.supports_relationship_lookup

   .. automethod:: RelationshipManager.supports_relationship_query

   .. automethod:: RelationshipManager.supports_relationship_search

   .. automethod:: RelationshipManager.supports_relationship_admin

   .. automethod:: RelationshipManager.supports_relationship_notification

   .. automethod:: RelationshipManager.supports_relationship_family

   .. automethod:: RelationshipManager.supports_relationship_family_assignment

   .. automethod:: RelationshipManager.supports_relationship_smart_family

   .. automethod:: RelationshipManager.supports_family_lookup

   .. automethod:: RelationshipManager.supports_family_query

   .. automethod:: RelationshipManager.supports_family_search

   .. automethod:: RelationshipManager.supports_family_admin

   .. automethod:: RelationshipManager.supports_family_notification

   .. automethod:: RelationshipManager.supports_family_hierarchy

   .. automethod:: RelationshipManager.supports_family_hierarchy_design

   .. automethod:: RelationshipManager.supports_relationship_batch

   .. automethod:: RelationshipManager.supports_relationship_rules

   .. autoattribute:: RelationshipManager.relationship_record_types

   .. automethod:: RelationshipManager.supports_relationship_record_type

   .. autoattribute:: RelationshipManager.relationship_search_record_types

   .. automethod:: RelationshipManager.supports_relationship_search_record_type

   .. autoattribute:: RelationshipManager.family_record_types

   .. automethod:: RelationshipManager.supports_family_record_type

   .. autoattribute:: RelationshipManager.family_search_record_types

   .. automethod:: RelationshipManager.supports_family_search_record_type



Family Lookup
_____________

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



Family Query
____________

   .. automethod:: RelationshipManager.can_search_families

   .. autoattribute:: RelationshipManager.family_query

   .. automethod:: RelationshipManager.get_families_by_query



Family Search
_____________

   .. autoattribute:: RelationshipManager.family_search

   .. autoattribute:: RelationshipManager.family_search_order

   .. automethod:: RelationshipManager.get_families_by_search

   .. automethod:: RelationshipManager.get_family_query_from_inspector



Family Admin
____________

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



Family Notification
___________________

   .. automethod:: RelationshipManager.can_register_for_family_notifications

   .. automethod:: RelationshipManager.register_for_new_families

   .. automethod:: RelationshipManager.register_for_new_family_ancestors

   .. automethod:: RelationshipManager.register_for_new_family_descendants

   .. automethod:: RelationshipManager.register_for_changed_families

   .. automethod:: RelationshipManager.register_for_changed_family

   .. automethod:: RelationshipManager.register_for_deleted_families

   .. automethod:: RelationshipManager.register_for_deleted_family

   .. automethod:: RelationshipManager.register_for_deleted_family_ancestors

   .. automethod:: RelationshipManager.register_for_deleted_family_descendants



Family Hierarchy
________________

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



Family Hierarchy Design
_______________________

   .. autoattribute:: RelationshipManager.family_hierarchy_id

   .. autoattribute:: RelationshipManager.family_hierarchy

   .. automethod:: RelationshipManager.can_modify_family_hierarchy

   .. automethod:: RelationshipManager.add_root_family

   .. automethod:: RelationshipManager.remove_root_family

   .. automethod:: RelationshipManager.add_child_family

   .. automethod:: RelationshipManager.remove_child_family

   .. automethod:: RelationshipManager.remove_child_families



Relationship Proxy Manager
--------------------------

.. autoclass:: RelationshipProxyManager
   :show-inheritance:

   .. autoattribute:: RelationshipProxyManager.relationship_batch_proxy_manager

   .. autoattribute:: RelationshipProxyManager.relationship_rules_proxy_manager



Relationship Profile Methods
____________________

   .. automethod:: RelationshipProxyManager.supports_visible_federation

   .. automethod:: RelationshipProxyManager.supports_relationship_lookup

   .. automethod:: RelationshipProxyManager.supports_relationship_query

   .. automethod:: RelationshipProxyManager.supports_relationship_search

   .. automethod:: RelationshipProxyManager.supports_relationship_admin

   .. automethod:: RelationshipProxyManager.supports_relationship_notification

   .. automethod:: RelationshipProxyManager.supports_relationship_family

   .. automethod:: RelationshipProxyManager.supports_relationship_family_assignment

   .. automethod:: RelationshipProxyManager.supports_relationship_smart_family

   .. automethod:: RelationshipProxyManager.supports_family_lookup

   .. automethod:: RelationshipProxyManager.supports_family_query

   .. automethod:: RelationshipProxyManager.supports_family_search

   .. automethod:: RelationshipProxyManager.supports_family_admin

   .. automethod:: RelationshipProxyManager.supports_family_notification

   .. automethod:: RelationshipProxyManager.supports_family_hierarchy

   .. automethod:: RelationshipProxyManager.supports_family_hierarchy_design

   .. automethod:: RelationshipProxyManager.supports_relationship_batch

   .. automethod:: RelationshipProxyManager.supports_relationship_rules

   .. autoattribute:: RelationshipProxyManager.relationship_record_types

   .. automethod:: RelationshipProxyManager.supports_relationship_record_type

   .. autoattribute:: RelationshipProxyManager.relationship_search_record_types

   .. automethod:: RelationshipProxyManager.supports_relationship_search_record_type

   .. autoattribute:: RelationshipProxyManager.family_record_types

   .. automethod:: RelationshipProxyManager.supports_family_record_type

   .. autoattribute:: RelationshipProxyManager.family_search_record_types

   .. automethod:: RelationshipProxyManager.supports_family_search_record_type



Family Lookup
_____________

   .. automethod:: RelationshipProxyManager.can_lookup_families

   .. automethod:: RelationshipProxyManager.use_comparative_family_view

   .. automethod:: RelationshipProxyManager.use_plenary_family_view

   .. automethod:: RelationshipProxyManager.get_family

   .. automethod:: RelationshipProxyManager.get_families_by_ids

   .. automethod:: RelationshipProxyManager.get_families_by_genus_type

   .. automethod:: RelationshipProxyManager.get_families_by_parent_genus_type

   .. automethod:: RelationshipProxyManager.get_families_by_record_type

   .. automethod:: RelationshipProxyManager.get_families_by_provider

   .. autoattribute:: RelationshipProxyManager.families



Family Query
____________

   .. automethod:: RelationshipProxyManager.can_search_families

   .. autoattribute:: RelationshipProxyManager.family_query

   .. automethod:: RelationshipProxyManager.get_families_by_query



Family Search
_____________

   .. autoattribute:: RelationshipProxyManager.family_search

   .. autoattribute:: RelationshipProxyManager.family_search_order

   .. automethod:: RelationshipProxyManager.get_families_by_search

   .. automethod:: RelationshipProxyManager.get_family_query_from_inspector



Family Admin
____________

   .. automethod:: RelationshipProxyManager.can_create_families

   .. automethod:: RelationshipProxyManager.can_create_family_with_record_types

   .. automethod:: RelationshipProxyManager.get_family_form_for_create

   .. automethod:: RelationshipProxyManager.create_family

   .. automethod:: RelationshipProxyManager.can_update_families

   .. automethod:: RelationshipProxyManager.get_family_form_for_update

   .. automethod:: RelationshipProxyManager.update_family

   .. automethod:: RelationshipProxyManager.can_delete_families

   .. automethod:: RelationshipProxyManager.delete_family

   .. automethod:: RelationshipProxyManager.can_manage_family_aliases

   .. automethod:: RelationshipProxyManager.alias_family



Family Notification
___________________

   .. automethod:: RelationshipProxyManager.can_register_for_family_notifications

   .. automethod:: RelationshipProxyManager.register_for_new_families

   .. automethod:: RelationshipProxyManager.register_for_new_family_ancestors

   .. automethod:: RelationshipProxyManager.register_for_new_family_descendants

   .. automethod:: RelationshipProxyManager.register_for_changed_families

   .. automethod:: RelationshipProxyManager.register_for_changed_family

   .. automethod:: RelationshipProxyManager.register_for_deleted_families

   .. automethod:: RelationshipProxyManager.register_for_deleted_family

   .. automethod:: RelationshipProxyManager.register_for_deleted_family_ancestors

   .. automethod:: RelationshipProxyManager.register_for_deleted_family_descendants



Family Hierarchy
________________

   .. autoattribute:: RelationshipProxyManager.family_hierarchy_id

   .. autoattribute:: RelationshipProxyManager.family_hierarchy

   .. automethod:: RelationshipProxyManager.can_access_family_hierarchy

   .. automethod:: RelationshipProxyManager.use_comparative_family_view

   .. automethod:: RelationshipProxyManager.use_plenary_family_view

   .. autoattribute:: RelationshipProxyManager.root_family_ids

   .. autoattribute:: RelationshipProxyManager.root_families

   .. automethod:: RelationshipProxyManager.has_parent_families

   .. automethod:: RelationshipProxyManager.is_parent_of_family

   .. automethod:: RelationshipProxyManager.get_parent_family_ids

   .. automethod:: RelationshipProxyManager.get_parent_families

   .. automethod:: RelationshipProxyManager.is_ancestor_of_family

   .. automethod:: RelationshipProxyManager.has_child_families

   .. automethod:: RelationshipProxyManager.is_child_of_family

   .. automethod:: RelationshipProxyManager.get_child_family_ids

   .. automethod:: RelationshipProxyManager.get_child_families

   .. automethod:: RelationshipProxyManager.is_descendant_of_family

   .. automethod:: RelationshipProxyManager.get_family_node_ids

   .. automethod:: RelationshipProxyManager.get_family_nodes



Family Hierarchy Design
_______________________

   .. autoattribute:: RelationshipProxyManager.family_hierarchy_id

   .. autoattribute:: RelationshipProxyManager.family_hierarchy

   .. automethod:: RelationshipProxyManager.can_modify_family_hierarchy

   .. automethod:: RelationshipProxyManager.add_root_family

   .. automethod:: RelationshipProxyManager.remove_root_family

   .. automethod:: RelationshipProxyManager.add_child_family

   .. automethod:: RelationshipProxyManager.remove_child_family

   .. automethod:: RelationshipProxyManager.remove_child_families



