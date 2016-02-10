
.. currentmodule:: dlkit.services.hierarchy
.. automodule:: dlkit.services.hierarchy

Service Managers
================


Hierarchy Profile
-----------------

.. autoclass:: HierarchyProfile
   :show-inheritance:

   .. automethod:: HierarchyProfile.supports_hierarchy_traversal

   .. automethod:: HierarchyProfile.supports_hierarchy_design

   .. automethod:: HierarchyProfile.supports_hierarchy_lookup

   .. automethod:: HierarchyProfile.supports_hierarchy_admin

   .. autoattribute:: HierarchyProfile.hierarchy_record_types

   .. autoattribute:: HierarchyProfile.hierarchy_search_record_types

Hierarchy Manager
-----------------

.. autoclass:: HierarchyManager
   :show-inheritance:





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



