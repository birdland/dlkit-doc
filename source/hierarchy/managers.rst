


Hierarchy Profile
-----------------

.. autoclass:: HierarchyProfile
   :show-inheritance:

   .. automethod:: HierarchyProfile.supports_visible_federation

   .. automethod:: HierarchyProfile.supports_hierarchy_traversal

   .. automethod:: HierarchyProfile.supports_hierarchy_design

   .. automethod:: HierarchyProfile.supports_hierarchy_sequencing

   .. automethod:: HierarchyProfile.supports_hierarchy_structure_notification

   .. automethod:: HierarchyProfile.supports_hierarchy_lookup

   .. automethod:: HierarchyProfile.supports_hierarchy_query

   .. automethod:: HierarchyProfile.supports_hierarchy_search

   .. automethod:: HierarchyProfile.supports_hierarchy_admin

   .. automethod:: HierarchyProfile.supports_hierarchy_notification

   .. autoattribute:: HierarchyProfile.hierarchy_record_types

   .. automethod:: HierarchyProfile.supports_hierarchy_record_type

   .. autoattribute:: HierarchyProfile.hierarchy_search_record_types

   .. automethod:: HierarchyProfile.supports_hierarchy_search_record_type



Hierarchy Traversal Methods
---------------------------

   .. autoattribute:: HierarchyTraversalSession.hierarchy_id

   .. autoattribute:: HierarchyTraversalSession.hierarchy

   .. automethod:: HierarchyTraversalSession.can_access_hierarchy

   .. autoattribute:: HierarchyTraversalSession.roots

   .. automethod:: HierarchyTraversalSession.has_parents

   .. automethod:: HierarchyTraversalSession.is_parent

   .. automethod:: HierarchyTraversalSession.get_parents

   .. automethod:: HierarchyTraversalSession.is_ancestor

   .. automethod:: HierarchyTraversalSession.has_children

   .. automethod:: HierarchyTraversalSession.is_child

   .. automethod:: HierarchyTraversalSession.get_children

   .. automethod:: HierarchyTraversalSession.is_descendant

   .. automethod:: HierarchyTraversalSession.get_nodes



Hierarchy Design Methods
------------------------

   .. autoattribute:: HierarchyDesignSession.hierarchy_id

   .. autoattribute:: HierarchyDesignSession.hierarchy

   .. automethod:: HierarchyDesignSession.can_modify_hierarchy

   .. automethod:: HierarchyDesignSession.add_root

   .. automethod:: HierarchyDesignSession.add_child

   .. automethod:: HierarchyDesignSession.remove_root

   .. automethod:: HierarchyDesignSession.remove_child

   .. automethod:: HierarchyDesignSession.remove_children



Hierarchy Lookup Methods
------------------------

   .. automethod:: HierarchyLookupSession.can_lookup_hierarchies

   .. automethod:: HierarchyLookupSession.use_comparative_hierarchy_view

   .. automethod:: HierarchyLookupSession.use_plenary_hierarchy_view

   .. automethod:: HierarchyLookupSession.get_hierarchy

   .. automethod:: HierarchyLookupSession.get_hierarchies_by_ids

   .. automethod:: HierarchyLookupSession.get_hierarchies_by_genus_type

   .. automethod:: HierarchyLookupSession.get_hierarchies_by_parent_genus_type

   .. automethod:: HierarchyLookupSession.get_hierarchies_by_record_type

   .. automethod:: HierarchyLookupSession.get_hierarchies_by_provider

   .. autoattribute:: HierarchyLookupSession.hierarchies



Hierarchy Admin Methods
-----------------------

   .. automethod:: HierarchyAdminSession.can_create_hierarchies

   .. automethod:: HierarchyAdminSession.can_create_hierarchy_with_record_types

   .. automethod:: HierarchyAdminSession.get_hierarchy_form_for_create

   .. automethod:: HierarchyAdminSession.create_hierarchy

   .. automethod:: HierarchyAdminSession.can_update_hierarchies

   .. automethod:: HierarchyAdminSession.get_hierarchy_form_for_update

   .. automethod:: HierarchyAdminSession.update_hierarchy

   .. automethod:: HierarchyAdminSession.can_delete_hierarchies

   .. automethod:: HierarchyAdminSession.delete_hierarchy

   .. automethod:: HierarchyAdminSession.can_manage_hierarchy_aliases

   .. automethod:: HierarchyAdminSession.alias_hierarchy



