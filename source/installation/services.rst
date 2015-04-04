.. currentmodule:: dlkit.services.installation
.. automodule:: dlkit.services.installation

Services
========


Installation Manager
--------------------

.. autoclass:: InstallationManager
   :show-inheritance:

   .. autoattribute:: InstallationManager.installation_batch_manager



Installation Profile Methods
____________________

   .. automethod:: InstallationManager.supports_visible_federation

   .. automethod:: InstallationManager.supports_installation_lookup

   .. automethod:: InstallationManager.supports_installation_query

   .. automethod:: InstallationManager.supports_installation_search

   .. automethod:: InstallationManager.supports_installation_management

   .. automethod:: InstallationManager.supports_installation_update

   .. automethod:: InstallationManager.supports_installation_notification

   .. automethod:: InstallationManager.supports_site_lookup

   .. automethod:: InstallationManager.supports_package_lookup

   .. automethod:: InstallationManager.supports_package_query

   .. automethod:: InstallationManager.supports_package_search

   .. automethod:: InstallationManager.supports_package_admin

   .. automethod:: InstallationManager.supports_package_notification

   .. automethod:: InstallationManager.supports_package_depot

   .. automethod:: InstallationManager.supports_package_depot_assignment

   .. automethod:: InstallationManager.supports_package_smart_depot

   .. automethod:: InstallationManager.supports_depot_lookup

   .. automethod:: InstallationManager.supports_depot_query

   .. automethod:: InstallationManager.supports_depot_search

   .. automethod:: InstallationManager.supports_depot_admin

   .. automethod:: InstallationManager.supports_depot_notification

   .. automethod:: InstallationManager.supports_depot_hierarchy

   .. automethod:: InstallationManager.supports_depot_hierarchy_design

   .. automethod:: InstallationManager.supports_installation_batch

   .. autoattribute:: InstallationManager.installation_record_types

   .. automethod:: InstallationManager.supports_installation_record_type

   .. autoattribute:: InstallationManager.installation_search_record_types

   .. automethod:: InstallationManager.supports_installation_search_record_type

   .. autoattribute:: InstallationManager.site_record_types

   .. automethod:: InstallationManager.supports_site_record_type

   .. autoattribute:: InstallationManager.package_record_types

   .. automethod:: InstallationManager.supports_package_record_type

   .. autoattribute:: InstallationManager.package_search_record_types

   .. automethod:: InstallationManager.supports_package_search_record_type

   .. autoattribute:: InstallationManager.installation_content_record_types

   .. automethod:: InstallationManager.supports_installation_content_record_type

   .. autoattribute:: InstallationManager.depot_record_types

   .. automethod:: InstallationManager.supports_depot_record_type

   .. autoattribute:: InstallationManager.depot_search_record_types

   .. automethod:: InstallationManager.supports_depot_search_record_type



Depot Lookup
____________

   .. automethod:: InstallationManager.can_lookup_depots

   .. automethod:: InstallationManager.use_comparative_depot_view

   .. automethod:: InstallationManager.use_plenary_depot_view

   .. automethod:: InstallationManager.get_depot

   .. automethod:: InstallationManager.get_depots_by_ids

   .. automethod:: InstallationManager.get_depots_by_genus_type

   .. automethod:: InstallationManager.get_depots_by_parent_genus_type

   .. automethod:: InstallationManager.get_depots_by_record_type

   .. automethod:: InstallationManager.get_depots_by_provider

   .. autoattribute:: InstallationManager.depots



Depot Query
___________

   .. automethod:: InstallationManager.can_search_depots

   .. autoattribute:: InstallationManager.depot_query

   .. automethod:: InstallationManager.get_depots_by_query



Depot Search
____________

   .. autoattribute:: InstallationManager.depot_search

   .. autoattribute:: InstallationManager.depot_search_order

   .. automethod:: InstallationManager.get_depots_by_search

   .. automethod:: InstallationManager.get_depot_query_from_inspector



Depot Admin
___________

   .. automethod:: InstallationManager.can_create_depots

   .. automethod:: InstallationManager.can_create_depot_with_record_types

   .. automethod:: InstallationManager.get_depot_form_for_create

   .. automethod:: InstallationManager.create_depot

   .. automethod:: InstallationManager.can_update_depots

   .. automethod:: InstallationManager.can_update_depot

   .. automethod:: InstallationManager.get_depot_form_for_update

   .. automethod:: InstallationManager.update_depot

   .. automethod:: InstallationManager.can_delete_depots

   .. automethod:: InstallationManager.can_delete_depot

   .. automethod:: InstallationManager.delete_depot

   .. automethod:: InstallationManager.can_manage_depot_aliases

   .. automethod:: InstallationManager.alias_depot



Depot Notification
__________________

   .. automethod:: InstallationManager.can_register_for_depot_notifications

   .. automethod:: InstallationManager.register_for_new_depots

   .. automethod:: InstallationManager.register_for_new_depot_ancestors

   .. automethod:: InstallationManager.register_for_new_depot_descendants

   .. automethod:: InstallationManager.register_for_changed_depots

   .. automethod:: InstallationManager.register_for_changed_depot

   .. automethod:: InstallationManager.register_for_deleted_depots

   .. automethod:: InstallationManager.register_for_deleted_depot

   .. automethod:: InstallationManager.register_for_deleted_depot_ancestors

   .. automethod:: InstallationManager.register_for_deleted_depot_descendants



Depot Hierarchy
_______________

   .. autoattribute:: InstallationManager.depot_hierarchy_id

   .. autoattribute:: InstallationManager.depot_hierarchy

   .. automethod:: InstallationManager.can_access_depot_hierarchy

   .. automethod:: InstallationManager.use_comparative_depot_view

   .. automethod:: InstallationManager.use_plenary_depot_view

   .. autoattribute:: InstallationManager.root_depot_ids

   .. autoattribute:: InstallationManager.root_depots

   .. automethod:: InstallationManager.has_parent_depots

   .. automethod:: InstallationManager.is_parent_of_depot

   .. automethod:: InstallationManager.get_parent_depot_ids

   .. automethod:: InstallationManager.get_parent_depots

   .. automethod:: InstallationManager.is_ancestor_of_depot

   .. automethod:: InstallationManager.has_child_depots

   .. automethod:: InstallationManager.is_child_of_depot

   .. automethod:: InstallationManager.get_child_depot_ids

   .. automethod:: InstallationManager.get_child_depots

   .. automethod:: InstallationManager.is_descendant_of_depot

   .. automethod:: InstallationManager.get_depot_node_ids

   .. automethod:: InstallationManager.get_depot_nodes



Depot Hierarchy Design
______________________

   .. autoattribute:: InstallationManager.depot_hierarchy_id

   .. autoattribute:: InstallationManager.depot_hierarchy

   .. automethod:: InstallationManager.can_modify_depot_hierarchy

   .. automethod:: InstallationManager.add_root_depot

   .. automethod:: InstallationManager.remove_root_depot

   .. automethod:: InstallationManager.add_child_depot

   .. automethod:: InstallationManager.remove_child_depot

   .. automethod:: InstallationManager.remove_child_depots



Installation Proxy Manager
--------------------------

.. autoclass:: InstallationProxyManager
   :show-inheritance:

   .. autoattribute:: InstallationProxyManager.installation_batch_proxy_manager



Installation Profile Methods
____________________

   .. automethod:: InstallationProxyManager.supports_visible_federation

   .. automethod:: InstallationProxyManager.supports_installation_lookup

   .. automethod:: InstallationProxyManager.supports_installation_query

   .. automethod:: InstallationProxyManager.supports_installation_search

   .. automethod:: InstallationProxyManager.supports_installation_management

   .. automethod:: InstallationProxyManager.supports_installation_update

   .. automethod:: InstallationProxyManager.supports_installation_notification

   .. automethod:: InstallationProxyManager.supports_site_lookup

   .. automethod:: InstallationProxyManager.supports_package_lookup

   .. automethod:: InstallationProxyManager.supports_package_query

   .. automethod:: InstallationProxyManager.supports_package_search

   .. automethod:: InstallationProxyManager.supports_package_admin

   .. automethod:: InstallationProxyManager.supports_package_notification

   .. automethod:: InstallationProxyManager.supports_package_depot

   .. automethod:: InstallationProxyManager.supports_package_depot_assignment

   .. automethod:: InstallationProxyManager.supports_package_smart_depot

   .. automethod:: InstallationProxyManager.supports_depot_lookup

   .. automethod:: InstallationProxyManager.supports_depot_query

   .. automethod:: InstallationProxyManager.supports_depot_search

   .. automethod:: InstallationProxyManager.supports_depot_admin

   .. automethod:: InstallationProxyManager.supports_depot_notification

   .. automethod:: InstallationProxyManager.supports_depot_hierarchy

   .. automethod:: InstallationProxyManager.supports_depot_hierarchy_design

   .. automethod:: InstallationProxyManager.supports_installation_batch

   .. autoattribute:: InstallationProxyManager.installation_record_types

   .. automethod:: InstallationProxyManager.supports_installation_record_type

   .. autoattribute:: InstallationProxyManager.installation_search_record_types

   .. automethod:: InstallationProxyManager.supports_installation_search_record_type

   .. autoattribute:: InstallationProxyManager.site_record_types

   .. automethod:: InstallationProxyManager.supports_site_record_type

   .. autoattribute:: InstallationProxyManager.package_record_types

   .. automethod:: InstallationProxyManager.supports_package_record_type

   .. autoattribute:: InstallationProxyManager.package_search_record_types

   .. automethod:: InstallationProxyManager.supports_package_search_record_type

   .. autoattribute:: InstallationProxyManager.installation_content_record_types

   .. automethod:: InstallationProxyManager.supports_installation_content_record_type

   .. autoattribute:: InstallationProxyManager.depot_record_types

   .. automethod:: InstallationProxyManager.supports_depot_record_type

   .. autoattribute:: InstallationProxyManager.depot_search_record_types

   .. automethod:: InstallationProxyManager.supports_depot_search_record_type



Depot Lookup
____________

   .. automethod:: InstallationProxyManager.can_lookup_depots

   .. automethod:: InstallationProxyManager.use_comparative_depot_view

   .. automethod:: InstallationProxyManager.use_plenary_depot_view

   .. automethod:: InstallationProxyManager.get_depot

   .. automethod:: InstallationProxyManager.get_depots_by_ids

   .. automethod:: InstallationProxyManager.get_depots_by_genus_type

   .. automethod:: InstallationProxyManager.get_depots_by_parent_genus_type

   .. automethod:: InstallationProxyManager.get_depots_by_record_type

   .. automethod:: InstallationProxyManager.get_depots_by_provider

   .. autoattribute:: InstallationProxyManager.depots



Depot Query
___________

   .. automethod:: InstallationProxyManager.can_search_depots

   .. autoattribute:: InstallationProxyManager.depot_query

   .. automethod:: InstallationProxyManager.get_depots_by_query



Depot Search
____________

   .. autoattribute:: InstallationProxyManager.depot_search

   .. autoattribute:: InstallationProxyManager.depot_search_order

   .. automethod:: InstallationProxyManager.get_depots_by_search

   .. automethod:: InstallationProxyManager.get_depot_query_from_inspector



Depot Admin
___________

   .. automethod:: InstallationProxyManager.can_create_depots

   .. automethod:: InstallationProxyManager.can_create_depot_with_record_types

   .. automethod:: InstallationProxyManager.get_depot_form_for_create

   .. automethod:: InstallationProxyManager.create_depot

   .. automethod:: InstallationProxyManager.can_update_depots

   .. automethod:: InstallationProxyManager.can_update_depot

   .. automethod:: InstallationProxyManager.get_depot_form_for_update

   .. automethod:: InstallationProxyManager.update_depot

   .. automethod:: InstallationProxyManager.can_delete_depots

   .. automethod:: InstallationProxyManager.can_delete_depot

   .. automethod:: InstallationProxyManager.delete_depot

   .. automethod:: InstallationProxyManager.can_manage_depot_aliases

   .. automethod:: InstallationProxyManager.alias_depot



Depot Notification
__________________

   .. automethod:: InstallationProxyManager.can_register_for_depot_notifications

   .. automethod:: InstallationProxyManager.register_for_new_depots

   .. automethod:: InstallationProxyManager.register_for_new_depot_ancestors

   .. automethod:: InstallationProxyManager.register_for_new_depot_descendants

   .. automethod:: InstallationProxyManager.register_for_changed_depots

   .. automethod:: InstallationProxyManager.register_for_changed_depot

   .. automethod:: InstallationProxyManager.register_for_deleted_depots

   .. automethod:: InstallationProxyManager.register_for_deleted_depot

   .. automethod:: InstallationProxyManager.register_for_deleted_depot_ancestors

   .. automethod:: InstallationProxyManager.register_for_deleted_depot_descendants



Depot Hierarchy
_______________

   .. autoattribute:: InstallationProxyManager.depot_hierarchy_id

   .. autoattribute:: InstallationProxyManager.depot_hierarchy

   .. automethod:: InstallationProxyManager.can_access_depot_hierarchy

   .. automethod:: InstallationProxyManager.use_comparative_depot_view

   .. automethod:: InstallationProxyManager.use_plenary_depot_view

   .. autoattribute:: InstallationProxyManager.root_depot_ids

   .. autoattribute:: InstallationProxyManager.root_depots

   .. automethod:: InstallationProxyManager.has_parent_depots

   .. automethod:: InstallationProxyManager.is_parent_of_depot

   .. automethod:: InstallationProxyManager.get_parent_depot_ids

   .. automethod:: InstallationProxyManager.get_parent_depots

   .. automethod:: InstallationProxyManager.is_ancestor_of_depot

   .. automethod:: InstallationProxyManager.has_child_depots

   .. automethod:: InstallationProxyManager.is_child_of_depot

   .. automethod:: InstallationProxyManager.get_child_depot_ids

   .. automethod:: InstallationProxyManager.get_child_depots

   .. automethod:: InstallationProxyManager.is_descendant_of_depot

   .. automethod:: InstallationProxyManager.get_depot_node_ids

   .. automethod:: InstallationProxyManager.get_depot_nodes



Depot Hierarchy Design
______________________

   .. autoattribute:: InstallationProxyManager.depot_hierarchy_id

   .. autoattribute:: InstallationProxyManager.depot_hierarchy

   .. automethod:: InstallationProxyManager.can_modify_depot_hierarchy

   .. automethod:: InstallationProxyManager.add_root_depot

   .. automethod:: InstallationProxyManager.remove_root_depot

   .. automethod:: InstallationProxyManager.add_child_depot

   .. automethod:: InstallationProxyManager.remove_child_depot

   .. automethod:: InstallationProxyManager.remove_child_depots



