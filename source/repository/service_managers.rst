Summary
=======
.. currentmodule:: dlkit.services.repository
.. automodule:: dlkit.services.repository

Service Managers
================


Repository Manager
------------------

.. autoclass:: RepositoryManager
   :show-inheritance:

   .. autoattribute:: RepositoryManager.repository_batch_manager

   .. autoattribute:: RepositoryManager.repository_rules_manager



Repository Profile Methods
__________________

   .. automethod:: RepositoryManager.supports_visible_federation

   .. automethod:: RepositoryManager.supports_asset_lookup

   .. automethod:: RepositoryManager.supports_asset_query

   .. automethod:: RepositoryManager.supports_asset_search

   .. automethod:: RepositoryManager.supports_asset_admin

   .. automethod:: RepositoryManager.supports_asset_notification

   .. automethod:: RepositoryManager.supports_asset_repository

   .. automethod:: RepositoryManager.supports_asset_repository_assignment

   .. automethod:: RepositoryManager.supports_asset_smart_repository

   .. automethod:: RepositoryManager.supports_asset_temporal

   .. automethod:: RepositoryManager.supports_asset_temporal_assignment

   .. automethod:: RepositoryManager.supports_asset_spatial

   .. automethod:: RepositoryManager.supports_asset_spatial_assignment

   .. automethod:: RepositoryManager.supports_asset_composition

   .. automethod:: RepositoryManager.supports_asset_composition_design

   .. automethod:: RepositoryManager.supports_composition_lookup

   .. automethod:: RepositoryManager.supports_composition_query

   .. automethod:: RepositoryManager.supports_composition_search

   .. automethod:: RepositoryManager.supports_composition_admin

   .. automethod:: RepositoryManager.supports_composition_notification

   .. automethod:: RepositoryManager.supports_composition_repository

   .. automethod:: RepositoryManager.supports_composition_repository_assignment

   .. automethod:: RepositoryManager.supports_composition_smart_repository

   .. automethod:: RepositoryManager.supports_repository_lookup

   .. automethod:: RepositoryManager.supports_repository_query

   .. automethod:: RepositoryManager.supports_repository_search

   .. automethod:: RepositoryManager.supports_repository_admin

   .. automethod:: RepositoryManager.supports_repository_notification

   .. automethod:: RepositoryManager.supports_repository_hierarchy

   .. automethod:: RepositoryManager.supports_repository_hierarchy_design

   .. automethod:: RepositoryManager.supports_repository_batch

   .. automethod:: RepositoryManager.supports_repository_rules

   .. autoattribute:: RepositoryManager.asset_record_types

   .. automethod:: RepositoryManager.supports_asset_record_type

   .. autoattribute:: RepositoryManager.asset_search_record_types

   .. automethod:: RepositoryManager.supports_asset_search_record_type

   .. autoattribute:: RepositoryManager.asset_content_record_types

   .. automethod:: RepositoryManager.supports_asset_content_record_type

   .. autoattribute:: RepositoryManager.composition_record_types

   .. automethod:: RepositoryManager.supports_composition_record_type

   .. autoattribute:: RepositoryManager.composition_search_record_types

   .. automethod:: RepositoryManager.supports_composition_search_record_type

   .. autoattribute:: RepositoryManager.repository_record_types

   .. automethod:: RepositoryManager.supports_repository_record_type

   .. autoattribute:: RepositoryManager.repository_search_record_types

   .. automethod:: RepositoryManager.supports_repository_search_record_type

   .. autoattribute:: RepositoryManager.spatial_unit_record_types

   .. automethod:: RepositoryManager.supports_spatial_unit_record_type

   .. autoattribute:: RepositoryManager.coordinate_types

   .. automethod:: RepositoryManager.supports_coordinate_type



Repository Lookup
_________________

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



Repository Admin
________________

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



Repository Proxy Manager
------------------------

.. autoclass:: RepositoryProxyManager
   :show-inheritance:

   .. autoattribute:: RepositoryProxyManager.repository_batch_proxy_manager

   .. autoattribute:: RepositoryProxyManager.repository_rules_proxy_manager



Repository Profile Methods
__________________

   .. automethod:: RepositoryProxyManager.supports_visible_federation

   .. automethod:: RepositoryProxyManager.supports_asset_lookup

   .. automethod:: RepositoryProxyManager.supports_asset_query

   .. automethod:: RepositoryProxyManager.supports_asset_search

   .. automethod:: RepositoryProxyManager.supports_asset_admin

   .. automethod:: RepositoryProxyManager.supports_asset_notification

   .. automethod:: RepositoryProxyManager.supports_asset_repository

   .. automethod:: RepositoryProxyManager.supports_asset_repository_assignment

   .. automethod:: RepositoryProxyManager.supports_asset_smart_repository

   .. automethod:: RepositoryProxyManager.supports_asset_temporal

   .. automethod:: RepositoryProxyManager.supports_asset_temporal_assignment

   .. automethod:: RepositoryProxyManager.supports_asset_spatial

   .. automethod:: RepositoryProxyManager.supports_asset_spatial_assignment

   .. automethod:: RepositoryProxyManager.supports_asset_composition

   .. automethod:: RepositoryProxyManager.supports_asset_composition_design

   .. automethod:: RepositoryProxyManager.supports_composition_lookup

   .. automethod:: RepositoryProxyManager.supports_composition_query

   .. automethod:: RepositoryProxyManager.supports_composition_search

   .. automethod:: RepositoryProxyManager.supports_composition_admin

   .. automethod:: RepositoryProxyManager.supports_composition_notification

   .. automethod:: RepositoryProxyManager.supports_composition_repository

   .. automethod:: RepositoryProxyManager.supports_composition_repository_assignment

   .. automethod:: RepositoryProxyManager.supports_composition_smart_repository

   .. automethod:: RepositoryProxyManager.supports_repository_lookup

   .. automethod:: RepositoryProxyManager.supports_repository_query

   .. automethod:: RepositoryProxyManager.supports_repository_search

   .. automethod:: RepositoryProxyManager.supports_repository_admin

   .. automethod:: RepositoryProxyManager.supports_repository_notification

   .. automethod:: RepositoryProxyManager.supports_repository_hierarchy

   .. automethod:: RepositoryProxyManager.supports_repository_hierarchy_design

   .. automethod:: RepositoryProxyManager.supports_repository_batch

   .. automethod:: RepositoryProxyManager.supports_repository_rules

   .. autoattribute:: RepositoryProxyManager.asset_record_types

   .. automethod:: RepositoryProxyManager.supports_asset_record_type

   .. autoattribute:: RepositoryProxyManager.asset_search_record_types

   .. automethod:: RepositoryProxyManager.supports_asset_search_record_type

   .. autoattribute:: RepositoryProxyManager.asset_content_record_types

   .. automethod:: RepositoryProxyManager.supports_asset_content_record_type

   .. autoattribute:: RepositoryProxyManager.composition_record_types

   .. automethod:: RepositoryProxyManager.supports_composition_record_type

   .. autoattribute:: RepositoryProxyManager.composition_search_record_types

   .. automethod:: RepositoryProxyManager.supports_composition_search_record_type

   .. autoattribute:: RepositoryProxyManager.repository_record_types

   .. automethod:: RepositoryProxyManager.supports_repository_record_type

   .. autoattribute:: RepositoryProxyManager.repository_search_record_types

   .. automethod:: RepositoryProxyManager.supports_repository_search_record_type

   .. autoattribute:: RepositoryProxyManager.spatial_unit_record_types

   .. automethod:: RepositoryProxyManager.supports_spatial_unit_record_type

   .. autoattribute:: RepositoryProxyManager.coordinate_types

   .. automethod:: RepositoryProxyManager.supports_coordinate_type



Repository Lookup
_________________

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



Repository Admin
________________

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



