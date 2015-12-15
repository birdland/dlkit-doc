

Managers
========


Repository Profile
------------------

.. py:class:: RepositoryProfile(osid_managers.OsidProfile, repository_managers.RepositoryProfile)
    The repository profile describes interoperability among repository services.

    .. py:method:: supports_visible_federation():
        :noindex:


    .. py:method:: supports_asset_lookup():
        :noindex:


    .. py:method:: supports_asset_query():
        :noindex:


    .. py:method:: supports_asset_search():
        :noindex:


    .. py:method:: supports_asset_admin():
        :noindex:


    .. py:method:: supports_asset_notification():
        :noindex:


    .. py:method:: supports_asset_repository():
        :noindex:


    .. py:method:: supports_asset_repository_assignment():
        :noindex:


    .. py:method:: supports_asset_smart_repository():
        :noindex:


    .. py:method:: supports_asset_temporal():
        :noindex:


    .. py:method:: supports_asset_temporal_assignment():
        :noindex:


    .. py:method:: supports_asset_spatial():
        :noindex:


    .. py:method:: supports_asset_spatial_assignment():
        :noindex:


    .. py:method:: supports_asset_composition():
        :noindex:


    .. py:method:: supports_asset_composition_design():
        :noindex:


    .. py:method:: supports_composition_lookup():
        :noindex:


    .. py:method:: supports_composition_query():
        :noindex:


    .. py:method:: supports_composition_search():
        :noindex:


    .. py:method:: supports_composition_admin():
        :noindex:


    .. py:method:: supports_composition_notification():
        :noindex:


    .. py:method:: supports_composition_repository():
        :noindex:


    .. py:method:: supports_composition_repository_assignment():
        :noindex:


    .. py:method:: supports_composition_smart_repository():
        :noindex:


    .. py:method:: supports_repository_lookup():
        :noindex:


    .. py:method:: supports_repository_query():
        :noindex:


    .. py:method:: supports_repository_search():
        :noindex:


    .. py:method:: supports_repository_admin():
        :noindex:


    .. py:method:: supports_repository_notification():
        :noindex:


    .. py:method:: supports_repository_hierarchy():
        :noindex:


    .. py:method:: supports_repository_hierarchy_design():
        :noindex:


    .. py:method:: supports_repository_batch():
        :noindex:


    .. py:method:: supports_repository_rules():
        :noindex:


    .. py:method:: get_asset_record_types():
        :noindex:


    .. py:attribute:: asset_record_types
        :noindex:


    .. py:method:: supports_asset_record_type(asset_record_type):
        :noindex:


    .. py:method:: get_asset_search_record_types():
        :noindex:


    .. py:attribute:: asset_search_record_types
        :noindex:


    .. py:method:: supports_asset_search_record_type(asset_search_record_type):
        :noindex:


    .. py:method:: get_asset_content_record_types():
        :noindex:


    .. py:attribute:: asset_content_record_types
        :noindex:


    .. py:method:: supports_asset_content_record_type(asset_content_record_type):
        :noindex:


    .. py:method:: get_composition_record_types():
        :noindex:


    .. py:attribute:: composition_record_types
        :noindex:


    .. py:method:: supports_composition_record_type(composition_record_type):
        :noindex:


    .. py:method:: get_composition_search_record_types():
        :noindex:


    .. py:attribute:: composition_search_record_types
        :noindex:


    .. py:method:: supports_composition_search_record_type(composition_search_record_type):
        :noindex:


    .. py:method:: get_repository_record_types():
        :noindex:


    .. py:attribute:: repository_record_types
        :noindex:


    .. py:method:: supports_repository_record_type(repository_record_type):
        :noindex:


    .. py:method:: get_repository_search_record_types():
        :noindex:


    .. py:attribute:: repository_search_record_types
        :noindex:


    .. py:method:: supports_repository_search_record_type(repository_search_record_type):
        :noindex:


    .. py:method:: get_spatial_unit_record_types():
        :noindex:


    .. py:attribute:: spatial_unit_record_types
        :noindex:


    .. py:method:: supports_spatial_unit_record_type(spatial_unit_record_type):
        :noindex:


    .. py:method:: get_coordinate_types():
        :noindex:


    .. py:attribute:: coordinate_types
        :noindex:


    .. py:method:: supports_coordinate_type(coordinate_type):
        :noindex:


Repository Manager
------------------

.. py:class:: RepositoryManager(osid_managers.OsidManager, RepositoryProfile, repository_managers.RepositoryManager)
        :noindex:

    .. py:method:: get_asset_lookup_session():
        :noindex:


    .. py:attribute:: asset_lookup_session
        :noindex:


    .. py:method:: get_asset_lookup_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_query_session():
        :noindex:


    .. py:attribute:: asset_query_session
        :noindex:


    .. py:method:: get_asset_query_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_search_session():
        :noindex:


    .. py:attribute:: asset_search_session
        :noindex:


    .. py:method:: get_asset_search_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_admin_session():
        :noindex:


    .. py:attribute:: asset_admin_session
        :noindex:


    .. py:method:: get_asset_admin_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_notification_session(asset_receiver):
        :noindex:


    .. py:method:: get_asset_notification_session_for_repository(asset_receiver, repository_id):
        :noindex:


    .. py:method:: get_asset_repository_session():
        :noindex:


    .. py:attribute:: asset_repository_session
        :noindex:


    .. py:method:: get_asset_repository_assignment_session():
        :noindex:


    .. py:attribute:: asset_repository_assignment_session
        :noindex:


    .. py:method:: get_asset_smart_repository_session(repository_id):
        :noindex:


    .. py:method:: get_asset_temporal_session():
        :noindex:


    .. py:attribute:: asset_temporal_session
        :noindex:


    .. py:method:: get_asset_temporal_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_temporal_assignment_session():
        :noindex:


    .. py:attribute:: asset_temporal_assignment_session
        :noindex:


    .. py:method:: get_asset_temporal_assignment_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_spatial_session():
        :noindex:


    .. py:attribute:: asset_spatial_session
        :noindex:


    .. py:method:: get_asset_spatial_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_spatial_assignment_session():
        :noindex:


    .. py:attribute:: asset_spatial_assignment_session
        :noindex:


    .. py:method:: get_asset_spatial_assignment_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_composition_session():
        :noindex:


    .. py:attribute:: asset_composition_session
        :noindex:


    .. py:method:: get_asset_composition_design_session():
        :noindex:


    .. py:attribute:: asset_composition_design_session
        :noindex:


    .. py:method:: get_composition_lookup_session():
        :noindex:


    .. py:attribute:: composition_lookup_session
        :noindex:


    .. py:method:: get_composition_lookup_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_query_session():
        :noindex:


    .. py:attribute:: composition_query_session
        :noindex:


    .. py:method:: get_composition_query_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_search_session():
        :noindex:


    .. py:attribute:: composition_search_session
        :noindex:


    .. py:method:: get_composition_search_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_admin_session():
        :noindex:


    .. py:attribute:: composition_admin_session
        :noindex:


    .. py:method:: get_composition_admin_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_notification_session(composition_receiver):
        :noindex:


    .. py:method:: get_composition_notification_session_for_repository(composition_receiver, repository_id):
        :noindex:


    .. py:method:: get_composition_repository_session():
        :noindex:


    .. py:attribute:: composition_repository_session
        :noindex:


    .. py:method:: get_composition_repository_assignment_session():
        :noindex:


    .. py:attribute:: composition_repository_assignment_session
        :noindex:


    .. py:method:: get_composition_smart_repository_session(repository_id):
        :noindex:


    .. py:method:: get_repository_lookup_session():
        :noindex:


    .. py:attribute:: repository_lookup_session
        :noindex:


    .. py:method:: get_repository_query_session():
        :noindex:


    .. py:attribute:: repository_query_session
        :noindex:


    .. py:method:: get_repository_search_session():
        :noindex:


    .. py:attribute:: repository_search_session
        :noindex:


    .. py:method:: get_repository_admin_session():
        :noindex:


    .. py:attribute:: repository_admin_session
        :noindex:


    .. py:method:: get_repository_notification_session(repository_receiver):
        :noindex:


    .. py:method:: get_repository_hierarchy_session():
        :noindex:


    .. py:attribute:: repository_hierarchy_session
        :noindex:


    .. py:method:: get_repository_hierarchy_design_session():
        :noindex:


    .. py:attribute:: repository_hierarchy_design_session
        :noindex:


    .. py:method:: get_repository_batch_manager():
        :noindex:


    .. py:attribute:: repository_batch_manager
        :noindex:


    .. py:method:: get_repository_rules_manager():
        :noindex:


    .. py:attribute:: repository_rules_manager
        :noindex:


Repository Proxy Manager
------------------------

.. py:class:: RepositoryProxyManager(osid_managers.OsidProxyManager, RepositoryProfile, repository_managers.RepositoryProxyManager)
        :noindex:

    .. py:method:: get_asset_lookup_session(proxy):
        :noindex:


    .. py:method:: get_asset_lookup_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_query_session(proxy):
        :noindex:


    .. py:method:: get_asset_query_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_search_session(proxy):
        :noindex:


    .. py:method:: get_asset_search_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_admin_session(proxy):
        :noindex:


    .. py:method:: get_asset_admin_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_notification_session(asset_receiver, proxy):
        :noindex:


    .. py:method:: get_asset_notification_session_for_repository(asset_receiver, repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_repository_session(proxy):
        :noindex:


    .. py:method:: get_asset_repository_assignment_session(proxy):
        :noindex:


    .. py:method:: get_asset_smart_repository_session(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_temporal_session(proxy):
        :noindex:


    .. py:method:: get_asset_temporal_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_temporal_assignment_session(proxy):
        :noindex:


    .. py:method:: get_asset_temporal_assignment_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_spatial_session(proxy):
        :noindex:


    .. py:method:: get_asset_spatial_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_spatial_assignment_session(proxy):
        :noindex:


    .. py:method:: get_asset_spatial_assignment_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_composition_session(proxy):
        :noindex:


    .. py:method:: get_asset_composition_design_session(proxy):
        :noindex:


    .. py:method:: get_composition_lookup_session(proxy):
        :noindex:


    .. py:method:: get_composition_lookup_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_query_session(proxy):
        :noindex:


    .. py:method:: get_composition_query_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_search_session(proxy):
        :noindex:


    .. py:method:: get_composition_search_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_admin_session(proxy):
        :noindex:


    .. py:method:: get_composition_admin_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_notification_session(composition_receiver, proxy):
        :noindex:


    .. py:method:: get_composition_notification_session_for_repository(composition_receiver, repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_repository_session(proxy):
        :noindex:


    .. py:method:: get_composition_repository_assignment_session(proxy):
        :noindex:


    .. py:method:: get_composition_smart_repository_session(repository_id, proxy):
        :noindex:


    .. py:method:: get_repository_lookup_session(proxy):
        :noindex:


    .. py:method:: get_repository_query_session(proxy):
        :noindex:


    .. py:method:: get_repository_search_session(proxy):
        :noindex:


    .. py:method:: get_repository_admin_session(proxy):
        :noindex:


    .. py:method:: get_repository_notification_session(repository_receiver, proxy):
        :noindex:


    .. py:method:: get_repository_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_repository_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_repository_batch_proxy_manager():
        :noindex:


    .. py:attribute:: repository_batch_proxy_manager
        :noindex:


    .. py:method:: get_repository_rules_proxy_manager():
        :noindex:


    .. py:attribute:: repository_rules_proxy_manager
        :noindex:


