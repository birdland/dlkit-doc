Summary
=======
.. currentmodule:: dlkit.services.configuration
.. automodule:: dlkit.services.configuration

Service_Managers
================


Configuration Manager
---------------------

.. autoclass:: ConfigurationManager
   :show-inheritance:

   .. autoattribute:: ConfigurationManager.configuration_batch_manager

   .. autoattribute:: ConfigurationManager.configuration_rules_manager



Configuration Profile Methods
_____________________

   .. automethod:: ConfigurationManager.supports_visible_federation

   .. automethod:: ConfigurationManager.supports_value_retrieval

   .. automethod:: ConfigurationManager.supports_value_lookup

   .. automethod:: ConfigurationManager.supports_value_query

   .. automethod:: ConfigurationManager.supports_value_search

   .. automethod:: ConfigurationManager.supports_value_admin

   .. automethod:: ConfigurationManager.supports_value_notification

   .. automethod:: ConfigurationManager.supports_parameter_lookup

   .. automethod:: ConfigurationManager.supports_parameter_query

   .. automethod:: ConfigurationManager.supports_parameter_search

   .. automethod:: ConfigurationManager.supports_parameter_admin

   .. automethod:: ConfigurationManager.supports_parameter_notification

   .. automethod:: ConfigurationManager.supports_parameter_configuration

   .. automethod:: ConfigurationManager.supports_parameter_configuration_assignment

   .. automethod:: ConfigurationManager.supports_parameter_smart_configuration

   .. automethod:: ConfigurationManager.supports_configuration_lookup

   .. automethod:: ConfigurationManager.supports_configuration_query

   .. automethod:: ConfigurationManager.supports_configuration_search

   .. automethod:: ConfigurationManager.supports_configuration_admin

   .. automethod:: ConfigurationManager.supports_configuration_notification

   .. automethod:: ConfigurationManager.supports_configuration_hierarchy

   .. automethod:: ConfigurationManager.supports_configuration_hierarchy_design

   .. automethod:: ConfigurationManager.supports_configuration_batch

   .. automethod:: ConfigurationManager.supports_configuration_rules

   .. autoattribute:: ConfigurationManager.value_condition_record_types

   .. automethod:: ConfigurationManager.supports_value_condition_record_type

   .. autoattribute:: ConfigurationManager.value_record_types

   .. automethod:: ConfigurationManager.supports_value_record_type

   .. autoattribute:: ConfigurationManager.value_search_record_types

   .. automethod:: ConfigurationManager.supports_value_search_record_type

   .. autoattribute:: ConfigurationManager.parameter_record_types

   .. automethod:: ConfigurationManager.supports_parameter_record_type

   .. autoattribute:: ConfigurationManager.parameter_search_record_types

   .. automethod:: ConfigurationManager.supports_parameter_search_record_type

   .. autoattribute:: ConfigurationManager.configuration_record_types

   .. automethod:: ConfigurationManager.supports_configuration_record_type

   .. autoattribute:: ConfigurationManager.configuration_search_record_types

   .. automethod:: ConfigurationManager.supports_configuration_search_record_type



Configuration Lookup
____________________

   .. automethod:: ConfigurationManager.can_lookup_configurations

   .. automethod:: ConfigurationManager.use_comparative_configuration_view

   .. automethod:: ConfigurationManager.use_plenary_configuration_view

   .. automethod:: ConfigurationManager.get_configuration

   .. automethod:: ConfigurationManager.get_configurations_by_ids

   .. automethod:: ConfigurationManager.get_configurations_by_genus_type

   .. automethod:: ConfigurationManager.get_configurations_by_parent_genus_type

   .. automethod:: ConfigurationManager.get_configurations_by_record_type

   .. automethod:: ConfigurationManager.get_configurations_by_provider

   .. autoattribute:: ConfigurationManager.configurations



Configuration Query
___________________

   .. automethod:: ConfigurationManager.can_search_configurations

   .. autoattribute:: ConfigurationManager.configuration_query

   .. automethod:: ConfigurationManager.get_configurations_by_query



Configuration Search
____________________

   .. autoattribute:: ConfigurationManager.configuration_search

   .. autoattribute:: ConfigurationManager.configuration_search_order

   .. automethod:: ConfigurationManager.get_configurations_by_search

   .. automethod:: ConfigurationManager.get_configuration_query_from_inspector



Configuration Admin
___________________

   .. automethod:: ConfigurationManager.can_create_configurations

   .. automethod:: ConfigurationManager.can_create_configuration_with_record_types

   .. automethod:: ConfigurationManager.get_configuration_form_for_create

   .. automethod:: ConfigurationManager.create_configuration

   .. automethod:: ConfigurationManager.can_update_configurations

   .. automethod:: ConfigurationManager.get_configuration_form_for_update

   .. automethod:: ConfigurationManager.update_configuration

   .. automethod:: ConfigurationManager.can_delete_configurations

   .. automethod:: ConfigurationManager.delete_configuration

   .. automethod:: ConfigurationManager.can_manage_configuration_aliases

   .. automethod:: ConfigurationManager.alias_configuration



Configuration Notification
__________________________

   .. automethod:: ConfigurationManager.can_register_for_configuration_notifications

   .. automethod:: ConfigurationManager.register_for_new_configurations

   .. automethod:: ConfigurationManager.register_for_new_configuration_ancestors

   .. automethod:: ConfigurationManager.register_for_new_configuration_descendants

   .. automethod:: ConfigurationManager.register_for_changed_configurations

   .. automethod:: ConfigurationManager.register_for_changed_configuration

   .. automethod:: ConfigurationManager.register_for_deleted_configurations

   .. automethod:: ConfigurationManager.register_for_deleted_configuration

   .. automethod:: ConfigurationManager.register_for_deleted_configuration_ancestors

   .. automethod:: ConfigurationManager.register_for_deleted_configuration_descendants



Configuration Hierarchy
_______________________

   .. autoattribute:: ConfigurationManager.configuration_hierarchy_id

   .. autoattribute:: ConfigurationManager.configuration_hierarchy

   .. automethod:: ConfigurationManager.can_access_configuration_hierarchy

   .. automethod:: ConfigurationManager.use_comparative_configuration_view

   .. automethod:: ConfigurationManager.use_plenary_configuration_view

   .. autoattribute:: ConfigurationManager.root_configuration_ids

   .. autoattribute:: ConfigurationManager.root_configurations

   .. automethod:: ConfigurationManager.has_parent_configurations

   .. automethod:: ConfigurationManager.is_parent_of_configuration

   .. automethod:: ConfigurationManager.get_parent_configuration_ids

   .. automethod:: ConfigurationManager.get_parent_configurations

   .. automethod:: ConfigurationManager.is_ancestor_of_configuration

   .. automethod:: ConfigurationManager.has_child_configurations

   .. automethod:: ConfigurationManager.is_child_of_configuration

   .. automethod:: ConfigurationManager.get_child_configuration_ids

   .. automethod:: ConfigurationManager.get_child_configurations

   .. automethod:: ConfigurationManager.is_descendant_of_configuration

   .. automethod:: ConfigurationManager.get_configuration_node_ids

   .. automethod:: ConfigurationManager.get_configuration_nodes



Configuration Hierarchy Design
______________________________

   .. autoattribute:: ConfigurationManager.configuration_hierarchy_id

   .. autoattribute:: ConfigurationManager.configuration_hierarchy

   .. automethod:: ConfigurationManager.can_modify_configuration_hierarchy

   .. automethod:: ConfigurationManager.add_root_configuration

   .. automethod:: ConfigurationManager.remove_root_configuration

   .. automethod:: ConfigurationManager.add_child_configuration

   .. automethod:: ConfigurationManager.remove_child_configuration

   .. automethod:: ConfigurationManager.remove_child_configurations



Configuration Proxy Manager
---------------------------

.. autoclass:: ConfigurationProxyManager
   :show-inheritance:

   .. autoattribute:: ConfigurationProxyManager.configuration_batch_proxy_manager

   .. autoattribute:: ConfigurationProxyManager.configuration_rules_proxy_manager



Configuration Profile Methods
_____________________

   .. automethod:: ConfigurationProxyManager.supports_visible_federation

   .. automethod:: ConfigurationProxyManager.supports_value_retrieval

   .. automethod:: ConfigurationProxyManager.supports_value_lookup

   .. automethod:: ConfigurationProxyManager.supports_value_query

   .. automethod:: ConfigurationProxyManager.supports_value_search

   .. automethod:: ConfigurationProxyManager.supports_value_admin

   .. automethod:: ConfigurationProxyManager.supports_value_notification

   .. automethod:: ConfigurationProxyManager.supports_parameter_lookup

   .. automethod:: ConfigurationProxyManager.supports_parameter_query

   .. automethod:: ConfigurationProxyManager.supports_parameter_search

   .. automethod:: ConfigurationProxyManager.supports_parameter_admin

   .. automethod:: ConfigurationProxyManager.supports_parameter_notification

   .. automethod:: ConfigurationProxyManager.supports_parameter_configuration

   .. automethod:: ConfigurationProxyManager.supports_parameter_configuration_assignment

   .. automethod:: ConfigurationProxyManager.supports_parameter_smart_configuration

   .. automethod:: ConfigurationProxyManager.supports_configuration_lookup

   .. automethod:: ConfigurationProxyManager.supports_configuration_query

   .. automethod:: ConfigurationProxyManager.supports_configuration_search

   .. automethod:: ConfigurationProxyManager.supports_configuration_admin

   .. automethod:: ConfigurationProxyManager.supports_configuration_notification

   .. automethod:: ConfigurationProxyManager.supports_configuration_hierarchy

   .. automethod:: ConfigurationProxyManager.supports_configuration_hierarchy_design

   .. automethod:: ConfigurationProxyManager.supports_configuration_batch

   .. automethod:: ConfigurationProxyManager.supports_configuration_rules

   .. autoattribute:: ConfigurationProxyManager.value_condition_record_types

   .. automethod:: ConfigurationProxyManager.supports_value_condition_record_type

   .. autoattribute:: ConfigurationProxyManager.value_record_types

   .. automethod:: ConfigurationProxyManager.supports_value_record_type

   .. autoattribute:: ConfigurationProxyManager.value_search_record_types

   .. automethod:: ConfigurationProxyManager.supports_value_search_record_type

   .. autoattribute:: ConfigurationProxyManager.parameter_record_types

   .. automethod:: ConfigurationProxyManager.supports_parameter_record_type

   .. autoattribute:: ConfigurationProxyManager.parameter_search_record_types

   .. automethod:: ConfigurationProxyManager.supports_parameter_search_record_type

   .. autoattribute:: ConfigurationProxyManager.configuration_record_types

   .. automethod:: ConfigurationProxyManager.supports_configuration_record_type

   .. autoattribute:: ConfigurationProxyManager.configuration_search_record_types

   .. automethod:: ConfigurationProxyManager.supports_configuration_search_record_type



Configuration Lookup
____________________

   .. automethod:: ConfigurationProxyManager.can_lookup_configurations

   .. automethod:: ConfigurationProxyManager.use_comparative_configuration_view

   .. automethod:: ConfigurationProxyManager.use_plenary_configuration_view

   .. automethod:: ConfigurationProxyManager.get_configuration

   .. automethod:: ConfigurationProxyManager.get_configurations_by_ids

   .. automethod:: ConfigurationProxyManager.get_configurations_by_genus_type

   .. automethod:: ConfigurationProxyManager.get_configurations_by_parent_genus_type

   .. automethod:: ConfigurationProxyManager.get_configurations_by_record_type

   .. automethod:: ConfigurationProxyManager.get_configurations_by_provider

   .. autoattribute:: ConfigurationProxyManager.configurations



Configuration Query
___________________

   .. automethod:: ConfigurationProxyManager.can_search_configurations

   .. autoattribute:: ConfigurationProxyManager.configuration_query

   .. automethod:: ConfigurationProxyManager.get_configurations_by_query



Configuration Search
____________________

   .. autoattribute:: ConfigurationProxyManager.configuration_search

   .. autoattribute:: ConfigurationProxyManager.configuration_search_order

   .. automethod:: ConfigurationProxyManager.get_configurations_by_search

   .. automethod:: ConfigurationProxyManager.get_configuration_query_from_inspector



Configuration Admin
___________________

   .. automethod:: ConfigurationProxyManager.can_create_configurations

   .. automethod:: ConfigurationProxyManager.can_create_configuration_with_record_types

   .. automethod:: ConfigurationProxyManager.get_configuration_form_for_create

   .. automethod:: ConfigurationProxyManager.create_configuration

   .. automethod:: ConfigurationProxyManager.can_update_configurations

   .. automethod:: ConfigurationProxyManager.get_configuration_form_for_update

   .. automethod:: ConfigurationProxyManager.update_configuration

   .. automethod:: ConfigurationProxyManager.can_delete_configurations

   .. automethod:: ConfigurationProxyManager.delete_configuration

   .. automethod:: ConfigurationProxyManager.can_manage_configuration_aliases

   .. automethod:: ConfigurationProxyManager.alias_configuration



Configuration Notification
__________________________

   .. automethod:: ConfigurationProxyManager.can_register_for_configuration_notifications

   .. automethod:: ConfigurationProxyManager.register_for_new_configurations

   .. automethod:: ConfigurationProxyManager.register_for_new_configuration_ancestors

   .. automethod:: ConfigurationProxyManager.register_for_new_configuration_descendants

   .. automethod:: ConfigurationProxyManager.register_for_changed_configurations

   .. automethod:: ConfigurationProxyManager.register_for_changed_configuration

   .. automethod:: ConfigurationProxyManager.register_for_deleted_configurations

   .. automethod:: ConfigurationProxyManager.register_for_deleted_configuration

   .. automethod:: ConfigurationProxyManager.register_for_deleted_configuration_ancestors

   .. automethod:: ConfigurationProxyManager.register_for_deleted_configuration_descendants



Configuration Hierarchy
_______________________

   .. autoattribute:: ConfigurationProxyManager.configuration_hierarchy_id

   .. autoattribute:: ConfigurationProxyManager.configuration_hierarchy

   .. automethod:: ConfigurationProxyManager.can_access_configuration_hierarchy

   .. automethod:: ConfigurationProxyManager.use_comparative_configuration_view

   .. automethod:: ConfigurationProxyManager.use_plenary_configuration_view

   .. autoattribute:: ConfigurationProxyManager.root_configuration_ids

   .. autoattribute:: ConfigurationProxyManager.root_configurations

   .. automethod:: ConfigurationProxyManager.has_parent_configurations

   .. automethod:: ConfigurationProxyManager.is_parent_of_configuration

   .. automethod:: ConfigurationProxyManager.get_parent_configuration_ids

   .. automethod:: ConfigurationProxyManager.get_parent_configurations

   .. automethod:: ConfigurationProxyManager.is_ancestor_of_configuration

   .. automethod:: ConfigurationProxyManager.has_child_configurations

   .. automethod:: ConfigurationProxyManager.is_child_of_configuration

   .. automethod:: ConfigurationProxyManager.get_child_configuration_ids

   .. automethod:: ConfigurationProxyManager.get_child_configurations

   .. automethod:: ConfigurationProxyManager.is_descendant_of_configuration

   .. automethod:: ConfigurationProxyManager.get_configuration_node_ids

   .. automethod:: ConfigurationProxyManager.get_configuration_nodes



Configuration Hierarchy Design
______________________________

   .. autoattribute:: ConfigurationProxyManager.configuration_hierarchy_id

   .. autoattribute:: ConfigurationProxyManager.configuration_hierarchy

   .. automethod:: ConfigurationProxyManager.can_modify_configuration_hierarchy

   .. automethod:: ConfigurationProxyManager.add_root_configuration

   .. automethod:: ConfigurationProxyManager.remove_root_configuration

   .. automethod:: ConfigurationProxyManager.add_child_configuration

   .. automethod:: ConfigurationProxyManager.remove_child_configuration

   .. automethod:: ConfigurationProxyManager.remove_child_configurations



