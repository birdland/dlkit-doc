Summary
=======
.. currentmodule:: dlkit.services.rules
.. automodule:: dlkit.services.rules

Service_Managers
================


Rules Manager
-------------

.. autoclass:: RulesManager
   :show-inheritance:

   .. autoattribute:: RulesManager.rules_check_manager



Rules Profile Methods
_____________

   .. automethod:: RulesManager.supports_visible_federation

   .. automethod:: RulesManager.supports_rules

   .. automethod:: RulesManager.supports_rule_lookup

   .. automethod:: RulesManager.supports_rule_query

   .. automethod:: RulesManager.supports_rule_search

   .. automethod:: RulesManager.supports_rule_admin

   .. automethod:: RulesManager.supports_rule_notification

   .. automethod:: RulesManager.supports_rule_engine

   .. automethod:: RulesManager.supports_rule_engine_assignment

   .. automethod:: RulesManager.supports_rule_smart_engine

   .. automethod:: RulesManager.supports_engine_lookup

   .. automethod:: RulesManager.supports_engine_query

   .. automethod:: RulesManager.supports_engine_search

   .. automethod:: RulesManager.supports_engine_admin

   .. automethod:: RulesManager.supports_engine_notification

   .. automethod:: RulesManager.supports_engine_hierarchy

   .. automethod:: RulesManager.supports_engine_hierarchy_design

   .. automethod:: RulesManager.supports_rules_check

   .. autoattribute:: RulesManager.rule_record_types

   .. automethod:: RulesManager.supports_rule_record_type

   .. autoattribute:: RulesManager.rule_search_record_types

   .. automethod:: RulesManager.supports_rule_search_record_type

   .. autoattribute:: RulesManager.engine_record_types

   .. automethod:: RulesManager.supports_engine_record_type

   .. autoattribute:: RulesManager.engine_search_record_types

   .. automethod:: RulesManager.supports_engine_search_record_type



Engine Lookup
_____________

   .. automethod:: RulesManager.can_lookup_engines

   .. automethod:: RulesManager.use_comparative_engine_view

   .. automethod:: RulesManager.use_plenary_engine_view

   .. automethod:: RulesManager.get_engine

   .. automethod:: RulesManager.get_engines_by_ids

   .. automethod:: RulesManager.get_engines_by_genus_type

   .. automethod:: RulesManager.get_engines_by_parent_genus_type

   .. automethod:: RulesManager.get_engines_by_record_type

   .. automethod:: RulesManager.get_engines_by_provider

   .. autoattribute:: RulesManager.engines



Engine Query
____________

   .. automethod:: RulesManager.can_search_engines

   .. autoattribute:: RulesManager.engine_query

   .. automethod:: RulesManager.get_engines_by_query



Engine Search
_____________

   .. autoattribute:: RulesManager.engine_search

   .. autoattribute:: RulesManager.engine_search_order

   .. automethod:: RulesManager.get_engines_by_search

   .. automethod:: RulesManager.get_engine_query_from_inspector



Engine Admin
____________

   .. automethod:: RulesManager.can_create_engines

   .. automethod:: RulesManager.can_create_engine_with_record_types

   .. automethod:: RulesManager.get_engine_form_for_create

   .. automethod:: RulesManager.create_engine

   .. automethod:: RulesManager.can_update_engines

   .. automethod:: RulesManager.get_engine_form_for_update

   .. automethod:: RulesManager.update_engine

   .. automethod:: RulesManager.can_delete_engines

   .. automethod:: RulesManager.delete_engine

   .. automethod:: RulesManager.can_manage_engine_aliases

   .. automethod:: RulesManager.alias_engine



Engine Notification
___________________

   .. automethod:: RulesManager.can_register_for_engine_notifications

   .. automethod:: RulesManager.register_for_new_engines

   .. automethod:: RulesManager.register_for_new_engine_ancestors

   .. automethod:: RulesManager.register_for_new_engine_descendants

   .. automethod:: RulesManager.register_for_changed_engines

   .. automethod:: RulesManager.register_for_changed_engine

   .. automethod:: RulesManager.register_for_deleted_engines

   .. automethod:: RulesManager.register_for_deleted_engine

   .. automethod:: RulesManager.register_for_deleted_engine_ancestors

   .. automethod:: RulesManager.register_for_deleted_engine_descendants



Engine Hierarchy
________________

   .. autoattribute:: RulesManager.engine_hierarchy_id

   .. autoattribute:: RulesManager.engine_hierarchy

   .. automethod:: RulesManager.can_access_engine_hierarchy

   .. automethod:: RulesManager.use_comparative_engine_view

   .. automethod:: RulesManager.use_plenary_engine_view

   .. autoattribute:: RulesManager.root_engine_ids

   .. autoattribute:: RulesManager.root_engines

   .. automethod:: RulesManager.has_parent_engines

   .. automethod:: RulesManager.is_parent_of_engine

   .. automethod:: RulesManager.get_parent_engine_ids

   .. automethod:: RulesManager.get_parent_engines

   .. automethod:: RulesManager.is_ancestor_of_engine

   .. automethod:: RulesManager.has_child_engines

   .. automethod:: RulesManager.is_child_of_engine

   .. automethod:: RulesManager.get_child_engine_ids

   .. automethod:: RulesManager.get_child_engines

   .. automethod:: RulesManager.is_descendant_of_engine

   .. automethod:: RulesManager.get_engine_node_ids

   .. automethod:: RulesManager.get_engine_nodes



Engine Hierarchy Design
_______________________

   .. autoattribute:: RulesManager.engine_hierarchy_id

   .. autoattribute:: RulesManager.engine_hierarchy

   .. automethod:: RulesManager.can_modify_engine_hierarchy

   .. automethod:: RulesManager.add_root_engine

   .. automethod:: RulesManager.remove_root_engine

   .. automethod:: RulesManager.add_child_engine

   .. automethod:: RulesManager.remove_child_engine

   .. automethod:: RulesManager.remove_child_engines



Rules Proxy Manager
-------------------

.. autoclass:: RulesProxyManager
   :show-inheritance:

   .. autoattribute:: RulesProxyManager.rules_check_proxy_manager



Rules Profile Methods
_____________

   .. automethod:: RulesProxyManager.supports_visible_federation

   .. automethod:: RulesProxyManager.supports_rules

   .. automethod:: RulesProxyManager.supports_rule_lookup

   .. automethod:: RulesProxyManager.supports_rule_query

   .. automethod:: RulesProxyManager.supports_rule_search

   .. automethod:: RulesProxyManager.supports_rule_admin

   .. automethod:: RulesProxyManager.supports_rule_notification

   .. automethod:: RulesProxyManager.supports_rule_engine

   .. automethod:: RulesProxyManager.supports_rule_engine_assignment

   .. automethod:: RulesProxyManager.supports_rule_smart_engine

   .. automethod:: RulesProxyManager.supports_engine_lookup

   .. automethod:: RulesProxyManager.supports_engine_query

   .. automethod:: RulesProxyManager.supports_engine_search

   .. automethod:: RulesProxyManager.supports_engine_admin

   .. automethod:: RulesProxyManager.supports_engine_notification

   .. automethod:: RulesProxyManager.supports_engine_hierarchy

   .. automethod:: RulesProxyManager.supports_engine_hierarchy_design

   .. automethod:: RulesProxyManager.supports_rules_check

   .. autoattribute:: RulesProxyManager.rule_record_types

   .. automethod:: RulesProxyManager.supports_rule_record_type

   .. autoattribute:: RulesProxyManager.rule_search_record_types

   .. automethod:: RulesProxyManager.supports_rule_search_record_type

   .. autoattribute:: RulesProxyManager.engine_record_types

   .. automethod:: RulesProxyManager.supports_engine_record_type

   .. autoattribute:: RulesProxyManager.engine_search_record_types

   .. automethod:: RulesProxyManager.supports_engine_search_record_type



Engine Lookup
_____________

   .. automethod:: RulesProxyManager.can_lookup_engines

   .. automethod:: RulesProxyManager.use_comparative_engine_view

   .. automethod:: RulesProxyManager.use_plenary_engine_view

   .. automethod:: RulesProxyManager.get_engine

   .. automethod:: RulesProxyManager.get_engines_by_ids

   .. automethod:: RulesProxyManager.get_engines_by_genus_type

   .. automethod:: RulesProxyManager.get_engines_by_parent_genus_type

   .. automethod:: RulesProxyManager.get_engines_by_record_type

   .. automethod:: RulesProxyManager.get_engines_by_provider

   .. autoattribute:: RulesProxyManager.engines



Engine Query
____________

   .. automethod:: RulesProxyManager.can_search_engines

   .. autoattribute:: RulesProxyManager.engine_query

   .. automethod:: RulesProxyManager.get_engines_by_query



Engine Search
_____________

   .. autoattribute:: RulesProxyManager.engine_search

   .. autoattribute:: RulesProxyManager.engine_search_order

   .. automethod:: RulesProxyManager.get_engines_by_search

   .. automethod:: RulesProxyManager.get_engine_query_from_inspector



Engine Admin
____________

   .. automethod:: RulesProxyManager.can_create_engines

   .. automethod:: RulesProxyManager.can_create_engine_with_record_types

   .. automethod:: RulesProxyManager.get_engine_form_for_create

   .. automethod:: RulesProxyManager.create_engine

   .. automethod:: RulesProxyManager.can_update_engines

   .. automethod:: RulesProxyManager.get_engine_form_for_update

   .. automethod:: RulesProxyManager.update_engine

   .. automethod:: RulesProxyManager.can_delete_engines

   .. automethod:: RulesProxyManager.delete_engine

   .. automethod:: RulesProxyManager.can_manage_engine_aliases

   .. automethod:: RulesProxyManager.alias_engine



Engine Notification
___________________

   .. automethod:: RulesProxyManager.can_register_for_engine_notifications

   .. automethod:: RulesProxyManager.register_for_new_engines

   .. automethod:: RulesProxyManager.register_for_new_engine_ancestors

   .. automethod:: RulesProxyManager.register_for_new_engine_descendants

   .. automethod:: RulesProxyManager.register_for_changed_engines

   .. automethod:: RulesProxyManager.register_for_changed_engine

   .. automethod:: RulesProxyManager.register_for_deleted_engines

   .. automethod:: RulesProxyManager.register_for_deleted_engine

   .. automethod:: RulesProxyManager.register_for_deleted_engine_ancestors

   .. automethod:: RulesProxyManager.register_for_deleted_engine_descendants



Engine Hierarchy
________________

   .. autoattribute:: RulesProxyManager.engine_hierarchy_id

   .. autoattribute:: RulesProxyManager.engine_hierarchy

   .. automethod:: RulesProxyManager.can_access_engine_hierarchy

   .. automethod:: RulesProxyManager.use_comparative_engine_view

   .. automethod:: RulesProxyManager.use_plenary_engine_view

   .. autoattribute:: RulesProxyManager.root_engine_ids

   .. autoattribute:: RulesProxyManager.root_engines

   .. automethod:: RulesProxyManager.has_parent_engines

   .. automethod:: RulesProxyManager.is_parent_of_engine

   .. automethod:: RulesProxyManager.get_parent_engine_ids

   .. automethod:: RulesProxyManager.get_parent_engines

   .. automethod:: RulesProxyManager.is_ancestor_of_engine

   .. automethod:: RulesProxyManager.has_child_engines

   .. automethod:: RulesProxyManager.is_child_of_engine

   .. automethod:: RulesProxyManager.get_child_engine_ids

   .. automethod:: RulesProxyManager.get_child_engines

   .. automethod:: RulesProxyManager.is_descendant_of_engine

   .. automethod:: RulesProxyManager.get_engine_node_ids

   .. automethod:: RulesProxyManager.get_engine_nodes



Engine Hierarchy Design
_______________________

   .. autoattribute:: RulesProxyManager.engine_hierarchy_id

   .. autoattribute:: RulesProxyManager.engine_hierarchy

   .. automethod:: RulesProxyManager.can_modify_engine_hierarchy

   .. automethod:: RulesProxyManager.add_root_engine

   .. automethod:: RulesProxyManager.remove_root_engine

   .. automethod:: RulesProxyManager.add_child_engine

   .. automethod:: RulesProxyManager.remove_child_engine

   .. automethod:: RulesProxyManager.remove_child_engines



