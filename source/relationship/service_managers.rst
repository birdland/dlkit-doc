
.. currentmodule:: dlkit.services.relationship
.. automodule:: dlkit.services.relationship

Service Managers
================


Relationship Manager
--------------------

.. autoclass:: RelationshipManager
   :show-inheritance:

   .. autoattribute:: RelationshipManager.relationship_lookup_session

   .. automethod:: RelationshipManager.get_relationship_lookup_session_for_family

   .. autoattribute:: RelationshipManager.relationship_query_session

   .. automethod:: RelationshipManager.get_relationship_query_session_for_family

   .. autoattribute:: RelationshipManager.relationship_search_session

   .. automethod:: RelationshipManager.get_relationship_search_session_for_family

   .. autoattribute:: RelationshipManager.relationship_admin_session

   .. automethod:: RelationshipManager.get_relationship_admin_session_for_family

   .. automethod:: RelationshipManager.get_relationship_notification_session

   .. automethod:: RelationshipManager.get_relationship_notification_session_for_family

   .. autoattribute:: RelationshipManager.relationship_family_session

   .. autoattribute:: RelationshipManager.relationship_family_assignment_session

   .. automethod:: RelationshipManager.get_relationship_smart_family_session

   .. autoattribute:: RelationshipManager.family_lookup_session

   .. autoattribute:: RelationshipManager.family_query_session

   .. autoattribute:: RelationshipManager.family_search_session

   .. autoattribute:: RelationshipManager.family_admin_session

   .. automethod:: RelationshipManager.get_family_notification_session

   .. autoattribute:: RelationshipManager.family_hierarchy_session

   .. autoattribute:: RelationshipManager.family_hierarchy_design_session

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



Relationship Proxy Manager
--------------------------

.. autoclass:: RelationshipProxyManager
   :show-inheritance:

   .. automethod:: RelationshipProxyManager.get_relationship_lookup_session

   .. automethod:: RelationshipProxyManager.get_relationship_lookup_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_query_session

   .. automethod:: RelationshipProxyManager.get_relationship_query_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_search_session

   .. automethod:: RelationshipProxyManager.get_relationship_search_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_admin_session

   .. automethod:: RelationshipProxyManager.get_relationship_admin_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_notification_session

   .. automethod:: RelationshipProxyManager.get_relationship_notification_session_for_family

   .. automethod:: RelationshipProxyManager.get_relationship_family_session

   .. automethod:: RelationshipProxyManager.get_relationship_family_assignment_session

   .. automethod:: RelationshipProxyManager.get_relationship_smart_family_session

   .. automethod:: RelationshipProxyManager.get_family_lookup_session

   .. automethod:: RelationshipProxyManager.get_family_query_session

   .. automethod:: RelationshipProxyManager.get_family_search_session

   .. automethod:: RelationshipProxyManager.get_family_admin_session

   .. automethod:: RelationshipProxyManager.get_family_notification_session

   .. automethod:: RelationshipProxyManager.get_family_hierarchy_session

   .. automethod:: RelationshipProxyManager.get_family_hierarchy_design_session

   .. autoattribute:: RelationshipProxyManager.relationship_batch_proxy_manager

   .. autoattribute:: RelationshipProxyManager.relationship_rules_proxy_manager



Family Lookup Methods
---------------------

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



Family Admin Methods
--------------------

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



Family Hierarchy Methods
------------------------

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



Family Hierarchy Design Methods
-------------------------------

   .. autoattribute:: RelationshipProxyManager.family_hierarchy_id

   .. autoattribute:: RelationshipProxyManager.family_hierarchy

   .. automethod:: RelationshipProxyManager.can_modify_family_hierarchy

   .. automethod:: RelationshipProxyManager.add_root_family

   .. automethod:: RelationshipProxyManager.remove_root_family

   .. automethod:: RelationshipProxyManager.add_child_family

   .. automethod:: RelationshipProxyManager.remove_child_family

   .. automethod:: RelationshipProxyManager.remove_child_families



