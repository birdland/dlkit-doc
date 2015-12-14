
.. currentmodule:: dlkit.services.repository
.. automodule:: dlkit.services.repository

Service Managers
================


Repository Manager
------------------

.. autoclass:: RepositoryManager
   :show-inheritance:

   .. autoattribute:: RepositoryManager.asset_lookup_session

   .. automethod:: RepositoryManager.get_asset_lookup_session_for_repository

   .. autoattribute:: RepositoryManager.asset_query_session

   .. automethod:: RepositoryManager.get_asset_query_session_for_repository

   .. autoattribute:: RepositoryManager.asset_search_session

   .. automethod:: RepositoryManager.get_asset_search_session_for_repository

   .. autoattribute:: RepositoryManager.asset_admin_session

   .. automethod:: RepositoryManager.get_asset_admin_session_for_repository

   .. automethod:: RepositoryManager.get_asset_notification_session

   .. automethod:: RepositoryManager.get_asset_notification_session_for_repository

   .. autoattribute:: RepositoryManager.asset_repository_session

   .. autoattribute:: RepositoryManager.asset_repository_assignment_session

   .. automethod:: RepositoryManager.get_asset_smart_repository_session

   .. autoattribute:: RepositoryManager.asset_temporal_session

   .. automethod:: RepositoryManager.get_asset_temporal_session_for_repository

   .. autoattribute:: RepositoryManager.asset_temporal_assignment_session

   .. automethod:: RepositoryManager.get_asset_temporal_assignment_session_for_repository

   .. autoattribute:: RepositoryManager.asset_spatial_session

   .. automethod:: RepositoryManager.get_asset_spatial_session_for_repository

   .. autoattribute:: RepositoryManager.asset_spatial_assignment_session

   .. automethod:: RepositoryManager.get_asset_spatial_assignment_session_for_repository

   .. autoattribute:: RepositoryManager.asset_composition_session

   .. autoattribute:: RepositoryManager.asset_composition_design_session

   .. autoattribute:: RepositoryManager.composition_lookup_session

   .. automethod:: RepositoryManager.get_composition_lookup_session_for_repository

   .. autoattribute:: RepositoryManager.composition_query_session

   .. automethod:: RepositoryManager.get_composition_query_session_for_repository

   .. autoattribute:: RepositoryManager.composition_search_session

   .. automethod:: RepositoryManager.get_composition_search_session_for_repository

   .. autoattribute:: RepositoryManager.composition_admin_session

   .. automethod:: RepositoryManager.get_composition_admin_session_for_repository

   .. automethod:: RepositoryManager.get_composition_notification_session

   .. automethod:: RepositoryManager.get_composition_notification_session_for_repository

   .. autoattribute:: RepositoryManager.composition_repository_session

   .. autoattribute:: RepositoryManager.composition_repository_assignment_session

   .. automethod:: RepositoryManager.get_composition_smart_repository_session

   .. autoattribute:: RepositoryManager.repository_lookup_session

   .. autoattribute:: RepositoryManager.repository_query_session

   .. autoattribute:: RepositoryManager.repository_search_session

   .. autoattribute:: RepositoryManager.repository_admin_session

   .. automethod:: RepositoryManager.get_repository_notification_session

   .. autoattribute:: RepositoryManager.repository_hierarchy_session

   .. autoattribute:: RepositoryManager.repository_hierarchy_design_session

   .. autoattribute:: RepositoryManager.repository_batch_manager

   .. autoattribute:: RepositoryManager.repository_rules_manager



Asset Repository Methods
------------------------

   .. automethod:: RepositoryManager.can_lookup_asset_repository_mappings

   .. automethod:: RepositoryManager.use_comparative_repository_view

   .. automethod:: RepositoryManager.use_plenary_repository_view

   .. automethod:: RepositoryManager.get_asset_ids_by_repository

   .. automethod:: RepositoryManager.get_assets_by_repository

   .. automethod:: RepositoryManager.get_asset_ids_by_repositories

   .. automethod:: RepositoryManager.get_assets_by_repositories

   .. automethod:: RepositoryManager.get_repository_ids_by_asset

   .. automethod:: RepositoryManager.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: RepositoryManager.can_assign_assets

   .. automethod:: RepositoryManager.can_assign_assets_to_repository

   .. automethod:: RepositoryManager.get_assignable_repository_ids

   .. automethod:: RepositoryManager.get_assignable_repository_ids_for_asset

   .. automethod:: RepositoryManager.assign_asset_to_repository

   .. automethod:: RepositoryManager.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: RepositoryManager.use_comparative_composition_repository_view

   .. automethod:: RepositoryManager.use_plenary_composition_repository_view

   .. automethod:: RepositoryManager.can_lookup_composition_repository_mappings

   .. automethod:: RepositoryManager.get_composition_ids_by_repository

   .. automethod:: RepositoryManager.get_compositions_by_repository

   .. automethod:: RepositoryManager.get_composition_ids_by_repositories

   .. automethod:: RepositoryManager.get_compoitions_by_repositories

   .. automethod:: RepositoryManager.get_repository_ids_by_composition

   .. automethod:: RepositoryManager.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: RepositoryManager.can_assign_compositions

   .. automethod:: RepositoryManager.can_assign_compositions_to_repository

   .. automethod:: RepositoryManager.get_assignable_repository_ids

   .. automethod:: RepositoryManager.get_assignable_repository_ids_for_composition

   .. automethod:: RepositoryManager.assign_composition_to_repository

   .. automethod:: RepositoryManager.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryManager.can_lookup_repositories

   .. automethod:: RepositoryManager.use_comparative_repository_view

   .. automethod:: RepositoryManager.use_plenary_repository_view

   .. automethod:: RepositoryManager.get_repository

   .. automethod:: RepositoryManager.get_repositories_by_ids

   .. automethod:: RepositoryManager.get_repositories_by_genus_type

   .. automethod:: RepositoryManager.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryManager.get_repositories_by_record_type

   .. automethod:: RepositoryManager.get_repositories_by_provider

   .. autoattribute:: RepositoryManager.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryManager.can_search_repositories

   .. autoattribute:: RepositoryManager.repository_query

   .. automethod:: RepositoryManager.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryManager.can_create_repositories

   .. automethod:: RepositoryManager.can_create_repository_with_record_types

   .. automethod:: RepositoryManager.get_repository_form_for_create

   .. automethod:: RepositoryManager.create_repository

   .. automethod:: RepositoryManager.can_update_repositories

   .. automethod:: RepositoryManager.get_repository_form_for_update

   .. automethod:: RepositoryManager.update_repository

   .. automethod:: RepositoryManager.can_delete_repositories

   .. automethod:: RepositoryManager.delete_repository

   .. automethod:: RepositoryManager.can_manage_repository_aliases

   .. automethod:: RepositoryManager.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryManager.repository_hierarchy_id

   .. autoattribute:: RepositoryManager.repository_hierarchy

   .. automethod:: RepositoryManager.can_access_repository_hierarchy

   .. automethod:: RepositoryManager.use_comparative_repository_view

   .. automethod:: RepositoryManager.use_plenary_repository_view

   .. autoattribute:: RepositoryManager.root_repository_ids

   .. autoattribute:: RepositoryManager.root_repositories

   .. automethod:: RepositoryManager.has_parent_repositories

   .. automethod:: RepositoryManager.is_parent_of_repository

   .. automethod:: RepositoryManager.get_parent_repository_ids

   .. automethod:: RepositoryManager.get_parent_repositories

   .. automethod:: RepositoryManager.is_ancestor_of_repository

   .. automethod:: RepositoryManager.has_child_repositories

   .. automethod:: RepositoryManager.is_child_of_repository

   .. automethod:: RepositoryManager.get_child_repository_ids

   .. automethod:: RepositoryManager.get_child_repositories

   .. automethod:: RepositoryManager.is_descendant_of_repository

   .. automethod:: RepositoryManager.get_repository_node_ids

   .. automethod:: RepositoryManager.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryManager.repository_hierarchy_id

   .. autoattribute:: RepositoryManager.repository_hierarchy

   .. automethod:: RepositoryManager.can_modify_repository_hierarchy

   .. automethod:: RepositoryManager.add_root_repository

   .. automethod:: RepositoryManager.remove_root_repository

   .. automethod:: RepositoryManager.add_child_repository

   .. automethod:: RepositoryManager.remove_child_repository

   .. automethod:: RepositoryManager.remove_child_repositories



Repository Proxy Manager
------------------------

.. autoclass:: RepositoryProxyManager
   :show-inheritance:

   .. automethod:: RepositoryProxyManager.get_asset_lookup_session

   .. automethod:: RepositoryProxyManager.get_asset_lookup_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_query_session

   .. automethod:: RepositoryProxyManager.get_asset_query_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_search_session

   .. automethod:: RepositoryProxyManager.get_asset_search_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_admin_session

   .. automethod:: RepositoryProxyManager.get_asset_admin_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_notification_session

   .. automethod:: RepositoryProxyManager.get_asset_notification_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_repository_session

   .. automethod:: RepositoryProxyManager.get_asset_repository_assignment_session

   .. automethod:: RepositoryProxyManager.get_asset_smart_repository_session

   .. automethod:: RepositoryProxyManager.get_asset_temporal_session

   .. automethod:: RepositoryProxyManager.get_asset_temporal_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_temporal_assignment_session

   .. automethod:: RepositoryProxyManager.get_asset_temporal_assignment_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_spatial_session

   .. automethod:: RepositoryProxyManager.get_asset_spatial_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_spatial_assignment_session

   .. automethod:: RepositoryProxyManager.get_asset_spatial_assignment_session_for_repository

   .. automethod:: RepositoryProxyManager.get_asset_composition_session

   .. automethod:: RepositoryProxyManager.get_asset_composition_design_session

   .. automethod:: RepositoryProxyManager.get_composition_lookup_session

   .. automethod:: RepositoryProxyManager.get_composition_lookup_session_for_repository

   .. automethod:: RepositoryProxyManager.get_composition_query_session

   .. automethod:: RepositoryProxyManager.get_composition_query_session_for_repository

   .. automethod:: RepositoryProxyManager.get_composition_search_session

   .. automethod:: RepositoryProxyManager.get_composition_search_session_for_repository

   .. automethod:: RepositoryProxyManager.get_composition_admin_session

   .. automethod:: RepositoryProxyManager.get_composition_admin_session_for_repository

   .. automethod:: RepositoryProxyManager.get_composition_notification_session

   .. automethod:: RepositoryProxyManager.get_composition_notification_session_for_repository

   .. automethod:: RepositoryProxyManager.get_composition_repository_session

   .. automethod:: RepositoryProxyManager.get_composition_repository_assignment_session

   .. automethod:: RepositoryProxyManager.get_composition_smart_repository_session

   .. automethod:: RepositoryProxyManager.get_repository_lookup_session

   .. automethod:: RepositoryProxyManager.get_repository_query_session

   .. automethod:: RepositoryProxyManager.get_repository_search_session

   .. automethod:: RepositoryProxyManager.get_repository_admin_session

   .. automethod:: RepositoryProxyManager.get_repository_notification_session

   .. automethod:: RepositoryProxyManager.get_repository_hierarchy_session

   .. automethod:: RepositoryProxyManager.get_repository_hierarchy_design_session

   .. autoattribute:: RepositoryProxyManager.repository_batch_proxy_manager

   .. autoattribute:: RepositoryProxyManager.repository_rules_proxy_manager



Asset Repository Methods
------------------------

   .. automethod:: RepositoryProxyManager.can_lookup_asset_repository_mappings

   .. automethod:: RepositoryProxyManager.use_comparative_repository_view

   .. automethod:: RepositoryProxyManager.use_plenary_repository_view

   .. automethod:: RepositoryProxyManager.get_asset_ids_by_repository

   .. automethod:: RepositoryProxyManager.get_assets_by_repository

   .. automethod:: RepositoryProxyManager.get_asset_ids_by_repositories

   .. automethod:: RepositoryProxyManager.get_assets_by_repositories

   .. automethod:: RepositoryProxyManager.get_repository_ids_by_asset

   .. automethod:: RepositoryProxyManager.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: RepositoryProxyManager.can_assign_assets

   .. automethod:: RepositoryProxyManager.can_assign_assets_to_repository

   .. automethod:: RepositoryProxyManager.get_assignable_repository_ids

   .. automethod:: RepositoryProxyManager.get_assignable_repository_ids_for_asset

   .. automethod:: RepositoryProxyManager.assign_asset_to_repository

   .. automethod:: RepositoryProxyManager.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: RepositoryProxyManager.use_comparative_composition_repository_view

   .. automethod:: RepositoryProxyManager.use_plenary_composition_repository_view

   .. automethod:: RepositoryProxyManager.can_lookup_composition_repository_mappings

   .. automethod:: RepositoryProxyManager.get_composition_ids_by_repository

   .. automethod:: RepositoryProxyManager.get_compositions_by_repository

   .. automethod:: RepositoryProxyManager.get_composition_ids_by_repositories

   .. automethod:: RepositoryProxyManager.get_compoitions_by_repositories

   .. automethod:: RepositoryProxyManager.get_repository_ids_by_composition

   .. automethod:: RepositoryProxyManager.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: RepositoryProxyManager.can_assign_compositions

   .. automethod:: RepositoryProxyManager.can_assign_compositions_to_repository

   .. automethod:: RepositoryProxyManager.get_assignable_repository_ids

   .. automethod:: RepositoryProxyManager.get_assignable_repository_ids_for_composition

   .. automethod:: RepositoryProxyManager.assign_composition_to_repository

   .. automethod:: RepositoryProxyManager.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryProxyManager.can_lookup_repositories

   .. automethod:: RepositoryProxyManager.use_comparative_repository_view

   .. automethod:: RepositoryProxyManager.use_plenary_repository_view

   .. automethod:: RepositoryProxyManager.get_repository

   .. automethod:: RepositoryProxyManager.get_repositories_by_ids

   .. automethod:: RepositoryProxyManager.get_repositories_by_genus_type

   .. automethod:: RepositoryProxyManager.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryProxyManager.get_repositories_by_record_type

   .. automethod:: RepositoryProxyManager.get_repositories_by_provider

   .. autoattribute:: RepositoryProxyManager.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryProxyManager.can_search_repositories

   .. autoattribute:: RepositoryProxyManager.repository_query

   .. automethod:: RepositoryProxyManager.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryProxyManager.can_create_repositories

   .. automethod:: RepositoryProxyManager.can_create_repository_with_record_types

   .. automethod:: RepositoryProxyManager.get_repository_form_for_create

   .. automethod:: RepositoryProxyManager.create_repository

   .. automethod:: RepositoryProxyManager.can_update_repositories

   .. automethod:: RepositoryProxyManager.get_repository_form_for_update

   .. automethod:: RepositoryProxyManager.update_repository

   .. automethod:: RepositoryProxyManager.can_delete_repositories

   .. automethod:: RepositoryProxyManager.delete_repository

   .. automethod:: RepositoryProxyManager.can_manage_repository_aliases

   .. automethod:: RepositoryProxyManager.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryProxyManager.repository_hierarchy_id

   .. autoattribute:: RepositoryProxyManager.repository_hierarchy

   .. automethod:: RepositoryProxyManager.can_access_repository_hierarchy

   .. automethod:: RepositoryProxyManager.use_comparative_repository_view

   .. automethod:: RepositoryProxyManager.use_plenary_repository_view

   .. autoattribute:: RepositoryProxyManager.root_repository_ids

   .. autoattribute:: RepositoryProxyManager.root_repositories

   .. automethod:: RepositoryProxyManager.has_parent_repositories

   .. automethod:: RepositoryProxyManager.is_parent_of_repository

   .. automethod:: RepositoryProxyManager.get_parent_repository_ids

   .. automethod:: RepositoryProxyManager.get_parent_repositories

   .. automethod:: RepositoryProxyManager.is_ancestor_of_repository

   .. automethod:: RepositoryProxyManager.has_child_repositories

   .. automethod:: RepositoryProxyManager.is_child_of_repository

   .. automethod:: RepositoryProxyManager.get_child_repository_ids

   .. automethod:: RepositoryProxyManager.get_child_repositories

   .. automethod:: RepositoryProxyManager.is_descendant_of_repository

   .. automethod:: RepositoryProxyManager.get_repository_node_ids

   .. automethod:: RepositoryProxyManager.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryProxyManager.repository_hierarchy_id

   .. autoattribute:: RepositoryProxyManager.repository_hierarchy

   .. automethod:: RepositoryProxyManager.can_modify_repository_hierarchy

   .. automethod:: RepositoryProxyManager.add_root_repository

   .. automethod:: RepositoryProxyManager.remove_root_repository

   .. automethod:: RepositoryProxyManager.add_child_repository

   .. automethod:: RepositoryProxyManager.remove_child_repository

   .. automethod:: RepositoryProxyManager.remove_child_repositories



