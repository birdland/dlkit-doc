
.. currentmodule:: dlkit.repository.managers
.. automodule:: dlkit.repository.managers

Managers
========


Repository Profile
------------------

.. autoclass:: RepositoryProfile
   :show-inheritance:

   .. automethod:: RepositoryProfile.supports_visible_federation

   .. automethod:: RepositoryProfile.supports_asset_lookup

   .. automethod:: RepositoryProfile.supports_asset_query

   .. automethod:: RepositoryProfile.supports_asset_search

   .. automethod:: RepositoryProfile.supports_asset_admin

   .. automethod:: RepositoryProfile.supports_asset_notification

   .. automethod:: RepositoryProfile.supports_asset_repository

   .. automethod:: RepositoryProfile.supports_asset_repository_assignment

   .. automethod:: RepositoryProfile.supports_asset_smart_repository

   .. automethod:: RepositoryProfile.supports_asset_temporal

   .. automethod:: RepositoryProfile.supports_asset_temporal_assignment

   .. automethod:: RepositoryProfile.supports_asset_spatial

   .. automethod:: RepositoryProfile.supports_asset_spatial_assignment

   .. automethod:: RepositoryProfile.supports_asset_composition

   .. automethod:: RepositoryProfile.supports_asset_composition_design

   .. automethod:: RepositoryProfile.supports_composition_lookup

   .. automethod:: RepositoryProfile.supports_composition_query

   .. automethod:: RepositoryProfile.supports_composition_search

   .. automethod:: RepositoryProfile.supports_composition_admin

   .. automethod:: RepositoryProfile.supports_composition_notification

   .. automethod:: RepositoryProfile.supports_composition_repository

   .. automethod:: RepositoryProfile.supports_composition_repository_assignment

   .. automethod:: RepositoryProfile.supports_composition_smart_repository

   .. automethod:: RepositoryProfile.supports_repository_lookup

   .. automethod:: RepositoryProfile.supports_repository_query

   .. automethod:: RepositoryProfile.supports_repository_search

   .. automethod:: RepositoryProfile.supports_repository_admin

   .. automethod:: RepositoryProfile.supports_repository_notification

   .. automethod:: RepositoryProfile.supports_repository_hierarchy

   .. automethod:: RepositoryProfile.supports_repository_hierarchy_design

   .. automethod:: RepositoryProfile.supports_repository_batch

   .. automethod:: RepositoryProfile.supports_repository_rules

   .. autoattribute:: RepositoryProfile.asset_record_types

   .. automethod:: RepositoryProfile.supports_asset_record_type

   .. autoattribute:: RepositoryProfile.asset_search_record_types

   .. automethod:: RepositoryProfile.supports_asset_search_record_type

   .. autoattribute:: RepositoryProfile.asset_content_record_types

   .. automethod:: RepositoryProfile.supports_asset_content_record_type

   .. autoattribute:: RepositoryProfile.composition_record_types

   .. automethod:: RepositoryProfile.supports_composition_record_type

   .. autoattribute:: RepositoryProfile.composition_search_record_types

   .. automethod:: RepositoryProfile.supports_composition_search_record_type

   .. autoattribute:: RepositoryProfile.repository_record_types

   .. automethod:: RepositoryProfile.supports_repository_record_type

   .. autoattribute:: RepositoryProfile.repository_search_record_types

   .. automethod:: RepositoryProfile.supports_repository_search_record_type

   .. autoattribute:: RepositoryProfile.spatial_unit_record_types

   .. automethod:: RepositoryProfile.supports_spatial_unit_record_type

   .. autoattribute:: RepositoryProfile.coordinate_types

   .. automethod:: RepositoryProfile.supports_coordinate_type

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

