
.. currentmodule:: dlkit.services.repository
.. automodule:: dlkit.services.repository

Service Managers
================


Repository Profile
------------------

.. autoclass:: RepositoryProfile
   :show-inheritance:

   .. automethod:: RepositoryProfile.supports_asset_lookup

   .. automethod:: RepositoryProfile.supports_asset_query

   .. automethod:: RepositoryProfile.supports_asset_search

   .. automethod:: RepositoryProfile.supports_asset_admin

   .. automethod:: RepositoryProfile.supports_asset_notification

   .. automethod:: RepositoryProfile.supports_asset_repository

   .. automethod:: RepositoryProfile.supports_asset_repository_assignment

   .. automethod:: RepositoryProfile.supports_asset_composition

   .. automethod:: RepositoryProfile.supports_asset_composition_design

   .. automethod:: RepositoryProfile.supports_composition_lookup

   .. automethod:: RepositoryProfile.supports_composition_query

   .. automethod:: RepositoryProfile.supports_composition_search

   .. automethod:: RepositoryProfile.supports_composition_admin

   .. automethod:: RepositoryProfile.supports_composition_repository

   .. automethod:: RepositoryProfile.supports_composition_repository_assignment

   .. automethod:: RepositoryProfile.supports_repository_lookup

   .. automethod:: RepositoryProfile.supports_repository_query

   .. automethod:: RepositoryProfile.supports_repository_admin

   .. automethod:: RepositoryProfile.supports_repository_hierarchy

   .. automethod:: RepositoryProfile.supports_repository_hierarchy_design

   .. autoattribute:: RepositoryProfile.asset_record_types

   .. autoattribute:: RepositoryProfile.asset_search_record_types

   .. autoattribute:: RepositoryProfile.asset_content_record_types

   .. autoattribute:: RepositoryProfile.composition_record_types

   .. autoattribute:: RepositoryProfile.composition_search_record_types

   .. autoattribute:: RepositoryProfile.repository_record_types

   .. autoattribute:: RepositoryProfile.repository_search_record_types

   .. autoattribute:: RepositoryProfile.spatial_unit_record_types

   .. autoattribute:: RepositoryProfile.coordinate_types

Repository Manager
------------------

.. autoclass:: RepositoryManager
   :show-inheritance:

   .. autoattribute:: RepositoryManager.repository_batch_manager

   .. autoattribute:: RepositoryManager.repository_rules_manager



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



