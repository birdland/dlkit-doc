.. currentmodule:: dlkit_doc.hierarchy
.. automodule:: dlkit_doc.hierarchy

Services
========


Hierarchy Manager
-----------------

.. autoclass:: HierarchyManager
   :show-inheritance:





Hierarchy Profile Methods
_________________

.. automethod:: HierarchyManager.supports_visible_federation

.. automethod:: HierarchyManager.supports_hierarchy_traversal

.. automethod:: HierarchyManager.supports_hierarchy_design

.. automethod:: HierarchyManager.supports_hierarchy_sequencing

.. automethod:: HierarchyManager.supports_hierarchy_structure_notification

.. automethod:: HierarchyManager.supports_hierarchy_lookup

.. automethod:: HierarchyManager.supports_hierarchy_query

.. automethod:: HierarchyManager.supports_hierarchy_search

.. automethod:: HierarchyManager.supports_hierarchy_admin

.. automethod:: HierarchyManager.supports_hierarchy_notification

.. autoattribute:: HierarchyManager.hierarchy_record_types

.. automethod:: HierarchyManager.supports_hierarchy_record_type

.. autoattribute:: HierarchyManager.hierarchy_search_record_types

.. automethod:: HierarchyManager.supports_hierarchy_search_record_type



Hierarchy Traversal
___________________

.. autoattribute:: HierarchyManager.hierarchy_id

.. autoattribute:: HierarchyManager.hierarchy

.. automethod:: HierarchyManager.can_access_hierarchy

.. autoattribute:: HierarchyManager.roots

.. automethod:: HierarchyManager.has_parents

.. automethod:: HierarchyManager.is_parent

.. automethod:: HierarchyManager.get_parents

.. automethod:: HierarchyManager.is_ancestor

.. automethod:: HierarchyManager.has_children

.. automethod:: HierarchyManager.is_child

.. automethod:: HierarchyManager.get_children

.. automethod:: HierarchyManager.is_descendant

.. automethod:: HierarchyManager.get_nodes



Hierarchy Design
________________

.. autoattribute:: HierarchyManager.hierarchy_id

.. autoattribute:: HierarchyManager.hierarchy

.. automethod:: HierarchyManager.can_modify_hierarchy

.. automethod:: HierarchyManager.add_root

.. automethod:: HierarchyManager.add_child

.. automethod:: HierarchyManager.remove_root

.. automethod:: HierarchyManager.remove_child

.. automethod:: HierarchyManager.remove_children



Hierarchy Sequencing
____________________

.. autoattribute:: HierarchyManager.hierarchy_id

.. autoattribute:: HierarchyManager.hierarchy

.. automethod:: HierarchyManager.can_sequence_hierarchy

.. automethod:: HierarchyManager.move_node_ahead

.. automethod:: HierarchyManager.move_node_behind

.. automethod:: HierarchyManager.sequence_nodes



Hierarchy Structure Notification
________________________________

.. autoattribute:: HierarchyManager.hierarchy_id

.. autoattribute:: HierarchyManager.hierarchy

.. automethod:: HierarchyManager.can_register_for_hierarchy_structure_notifications

.. automethod:: HierarchyManager.register_for_new_hierarchy_nodes

.. automethod:: HierarchyManager.register_for_changed_ancestor

.. automethod:: HierarchyManager.register_for_changed_descendant

.. automethod:: HierarchyManager.register_for_deleted_hierarchy_nodes

.. automethod:: HierarchyManager.register_for_deleted_hierarchy_node



Hierarchy Lookup
________________

.. automethod:: HierarchyManager.can_lookup_hierarchies

.. automethod:: HierarchyManager.use_comparative_hierarchy_view

.. automethod:: HierarchyManager.use_plenary_hierarchy_view

.. automethod:: HierarchyManager.get_hierarchy

.. automethod:: HierarchyManager.get_hierarchies_by_ids

.. automethod:: HierarchyManager.get_hierarchies_by_genus_type

.. automethod:: HierarchyManager.get_hierarchies_by_parent_genus_type

.. automethod:: HierarchyManager.get_hierarchies_by_record_type

.. automethod:: HierarchyManager.get_hierarchies_by_provider

.. autoattribute:: HierarchyManager.hierarchies



Hierarchy Query
_______________

.. automethod:: HierarchyManager.can_search_hierarchies

.. autoattribute:: HierarchyManager.hierarchy_query

.. automethod:: HierarchyManager.get_hierarchies_by_query



Hierarchy Search
________________

.. autoattribute:: HierarchyManager.hierarchy_search

.. autoattribute:: HierarchyManager.hierarchy_search_order

.. automethod:: HierarchyManager.get_hierarchies_by_search

.. automethod:: HierarchyManager.get_hierarchy_query_from_inspector



Hierarchy Admin
_______________

.. automethod:: HierarchyManager.can_create_hierarchies

.. automethod:: HierarchyManager.can_create_hierarchy_with_record_types

.. automethod:: HierarchyManager.get_hierarchy_form_for_create

.. automethod:: HierarchyManager.create_hierarchy

.. automethod:: HierarchyManager.can_update_hierarchies

.. automethod:: HierarchyManager.get_hierarchy_form_for_update

.. automethod:: HierarchyManager.update_hierarchy

.. automethod:: HierarchyManager.can_delete_hierarchies

.. automethod:: HierarchyManager.delete_hierarchy

.. automethod:: HierarchyManager.can_manage_hierarchy_aliases

.. automethod:: HierarchyManager.alias_hierarchy



Hierarchy Notification
______________________

.. automethod:: HierarchyManager.can_register_for_hierarchy_notifications

.. automethod:: HierarchyManager.register_for_new_hierarchies

.. automethod:: HierarchyManager.register_for_changed_hierarchies

.. automethod:: HierarchyManager.register_for_changed_hierarchy

.. automethod:: HierarchyManager.register_for_deleted_hierarchies

.. automethod:: HierarchyManager.register_for_deleted_hierarchy



Hierarchy Proxy Manager
-----------------------

.. autoclass:: HierarchyProxyManager
   :show-inheritance:

.. automethod:: HierarchyProxyManager.get_hierarchy_traversal_session

.. automethod:: HierarchyProxyManager.get_hierarchy_traversal_session_for_hierarchy

.. automethod:: HierarchyProxyManager.get_hierarchy_design_session

.. automethod:: HierarchyProxyManager.get_hierarchy_design_session_for_hierarchy

.. automethod:: HierarchyProxyManager.get_hierarchy_sequencing_session

.. automethod:: HierarchyProxyManager.get_hierarchy_sequencing_session_for_hierarchy

.. automethod:: HierarchyProxyManager.get_hierarchy_structure_notification_session

.. automethod:: HierarchyProxyManager.get_hierarchy_structure_notification_session_for_hierarchy

.. automethod:: HierarchyProxyManager.get_hierarchy_lookup_session

.. automethod:: HierarchyProxyManager.get_hierarchy_query_session

.. automethod:: HierarchyProxyManager.get_hierarchy_search_session

.. automethod:: HierarchyProxyManager.get_hierarchy_admin_session

.. automethod:: HierarchyProxyManager.get_hierarchy_notification_session



