
.. currentmodule:: dlkit.services.hierarchy
.. automodule:: dlkit.services.hierarchy

Service Managers
================


Hierarchy Manager
-----------------

.. autoclass:: HierarchyManager
   :show-inheritance:

   .. autoattribute:: HierarchyManager.hierarchy_traversal_session

   .. automethod:: HierarchyManager.get_hierarchy_traversal_session_for_hierarchy

   .. autoattribute:: HierarchyManager.hierarchy_design_session

   .. automethod:: HierarchyManager.get_hierarchy_design_session_for_hierarchy

   .. autoattribute:: HierarchyManager.hierarchy_sequencing_session

   .. automethod:: HierarchyManager.get_hierarchy_sequencing_session_for_hierarchy

   .. automethod:: HierarchyManager.get_hierarchy_structure_notification_session

   .. automethod:: HierarchyManager.get_hierarchy_structure_notification_session_for_hierarchy

   .. autoattribute:: HierarchyManager.hierarchy_lookup_session

   .. autoattribute:: HierarchyManager.hierarchy_query_session

   .. autoattribute:: HierarchyManager.hierarchy_search_session

   .. autoattribute:: HierarchyManager.hierarchy_admin_session

   .. automethod:: HierarchyManager.get_hierarchy_notification_session



Hierarchy Traversal Methods
---------------------------

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



Hierarchy Design Methods
------------------------

   .. autoattribute:: HierarchyManager.hierarchy_id

   .. autoattribute:: HierarchyManager.hierarchy

   .. automethod:: HierarchyManager.can_modify_hierarchy

   .. automethod:: HierarchyManager.add_root

   .. automethod:: HierarchyManager.add_child

   .. automethod:: HierarchyManager.remove_root

   .. automethod:: HierarchyManager.remove_child

   .. automethod:: HierarchyManager.remove_children



Hierarchy Lookup Methods
------------------------

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



Hierarchy Admin Methods
-----------------------

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



Hierarchy Traversal Methods
---------------------------

   .. autoattribute:: HierarchyProxyManager.hierarchy_id

   .. autoattribute:: HierarchyProxyManager.hierarchy

   .. automethod:: HierarchyProxyManager.can_access_hierarchy

   .. autoattribute:: HierarchyProxyManager.roots

   .. automethod:: HierarchyProxyManager.has_parents

   .. automethod:: HierarchyProxyManager.is_parent

   .. automethod:: HierarchyProxyManager.get_parents

   .. automethod:: HierarchyProxyManager.is_ancestor

   .. automethod:: HierarchyProxyManager.has_children

   .. automethod:: HierarchyProxyManager.is_child

   .. automethod:: HierarchyProxyManager.get_children

   .. automethod:: HierarchyProxyManager.is_descendant

   .. automethod:: HierarchyProxyManager.get_nodes



Hierarchy Design Methods
------------------------

   .. autoattribute:: HierarchyProxyManager.hierarchy_id

   .. autoattribute:: HierarchyProxyManager.hierarchy

   .. automethod:: HierarchyProxyManager.can_modify_hierarchy

   .. automethod:: HierarchyProxyManager.add_root

   .. automethod:: HierarchyProxyManager.add_child

   .. automethod:: HierarchyProxyManager.remove_root

   .. automethod:: HierarchyProxyManager.remove_child

   .. automethod:: HierarchyProxyManager.remove_children



Hierarchy Lookup Methods
------------------------

   .. automethod:: HierarchyProxyManager.can_lookup_hierarchies

   .. automethod:: HierarchyProxyManager.use_comparative_hierarchy_view

   .. automethod:: HierarchyProxyManager.use_plenary_hierarchy_view

   .. automethod:: HierarchyProxyManager.get_hierarchy

   .. automethod:: HierarchyProxyManager.get_hierarchies_by_ids

   .. automethod:: HierarchyProxyManager.get_hierarchies_by_genus_type

   .. automethod:: HierarchyProxyManager.get_hierarchies_by_parent_genus_type

   .. automethod:: HierarchyProxyManager.get_hierarchies_by_record_type

   .. automethod:: HierarchyProxyManager.get_hierarchies_by_provider

   .. autoattribute:: HierarchyProxyManager.hierarchies



Hierarchy Admin Methods
-----------------------

   .. automethod:: HierarchyProxyManager.can_create_hierarchies

   .. automethod:: HierarchyProxyManager.can_create_hierarchy_with_record_types

   .. automethod:: HierarchyProxyManager.get_hierarchy_form_for_create

   .. automethod:: HierarchyProxyManager.create_hierarchy

   .. automethod:: HierarchyProxyManager.can_update_hierarchies

   .. automethod:: HierarchyProxyManager.get_hierarchy_form_for_update

   .. automethod:: HierarchyProxyManager.update_hierarchy

   .. automethod:: HierarchyProxyManager.can_delete_hierarchies

   .. automethod:: HierarchyProxyManager.delete_hierarchy

   .. automethod:: HierarchyProxyManager.can_manage_hierarchy_aliases

   .. automethod:: HierarchyProxyManager.alias_hierarchy



