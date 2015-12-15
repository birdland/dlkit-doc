

Queries
=======


Asset Query
-----------

.. py:class:: AssetQuery(abc_repository_queries.AssetQuery, osid_queries.OsidObjectQuery, osid_queries.OsidAggregateableQuery, osid_queries.OsidSourceableQuery)
    This is the query for searching assets.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``. The query record is
    identified by the ``Asset Type``.





    .. py:method:: match_title(title, string_match_type, match):
        :noindex:


    .. py:method:: match_any_title(match):
        :noindex:


    .. py:method:: clear_title_terms():
        :noindex:


    .. py:attribute:: title_terms
        :noindex:


    .. py:method:: match_public_domain(public_domain):
        :noindex:


    .. py:method:: match_any_public_domain(match):
        :noindex:


    .. py:method:: clear_public_domain_terms():
        :noindex:


    .. py:attribute:: public_domain_terms
        :noindex:


    .. py:method:: match_copyright(copyright_, string_match_type, match):
        :noindex:


    .. py:method:: match_any_copyright(match):
        :noindex:


    .. py:method:: clear_copyright_terms():
        :noindex:


    .. py:attribute:: copyright_terms
        :noindex:


    .. py:method:: match_copyright_registration(registration, string_match_type, match):
        :noindex:


    .. py:method:: match_any_copyright_registration(match):
        :noindex:


    .. py:method:: clear_copyright_registration_terms():
        :noindex:


    .. py:attribute:: copyright_registration_terms
        :noindex:


    .. py:method:: match_distribute_verbatim(distributable):
        :noindex:


    .. py:method:: clear_distribute_verbatim_terms():
        :noindex:


    .. py:attribute:: distribute_verbatim_terms
        :noindex:


    .. py:method:: match_distribute_alterations(alterable):
        :noindex:


    .. py:method:: clear_distribute_alterations_terms():
        :noindex:


    .. py:attribute:: distribute_alterations_terms
        :noindex:


    .. py:method:: match_distribute_compositions(composable):
        :noindex:


    .. py:method:: clear_distribute_compositions_terms():
        :noindex:


    .. py:attribute:: distribute_compositions_terms
        :noindex:


    .. py:method:: match_source_id(source_id, match):
        :noindex:


    .. py:method:: clear_source_id_terms():
        :noindex:


    .. py:attribute:: source_id_terms
        :noindex:


    .. py:method:: supports_source_query():
        :noindex:


    .. py:method:: get_source_query():
        :noindex:


    .. py:attribute:: source_query
        :noindex:


    .. py:method:: match_any_source(match):
        :noindex:


    .. py:method:: clear_source_terms():
        :noindex:


    .. py:attribute:: source_terms
        :noindex:


    .. py:method:: match_created_date(start, end, match):
        :noindex:


    .. py:method:: match_any_created_date(match):
        :noindex:


    .. py:method:: clear_created_date_terms():
        :noindex:


    .. py:attribute:: created_date_terms
        :noindex:


    .. py:method:: match_published(published):
        :noindex:


    .. py:method:: clear_published_terms():
        :noindex:


    .. py:attribute:: published_terms
        :noindex:


    .. py:method:: match_published_date(start, end, match):
        :noindex:


    .. py:method:: match_any_published_date(match):
        :noindex:


    .. py:method:: clear_published_date_terms():
        :noindex:


    .. py:attribute:: published_date_terms
        :noindex:


    .. py:method:: match_principal_credit_string(credit, string_match_type, match):
        :noindex:


    .. py:method:: match_any_principal_credit_string(match):
        :noindex:


    .. py:method:: clear_principal_credit_string_terms():
        :noindex:


    .. py:attribute:: principal_credit_string_terms
        :noindex:


    .. py:method:: match_temporal_coverage(start, end, match):
        :noindex:


    .. py:method:: match_any_temporal_coverage(match):
        :noindex:


    .. py:method:: clear_temporal_coverage_terms():
        :noindex:


    .. py:attribute:: temporal_coverage_terms
        :noindex:


    .. py:method:: match_location_id(location_id, match):
        :noindex:


    .. py:method:: clear_location_id_terms():
        :noindex:


    .. py:attribute:: location_id_terms
        :noindex:


    .. py:method:: supports_location_query():
        :noindex:


    .. py:method:: get_location_query():
        :noindex:


    .. py:attribute:: location_query
        :noindex:


    .. py:method:: match_any_location(match):
        :noindex:


    .. py:method:: clear_location_terms():
        :noindex:


    .. py:attribute:: location_terms
        :noindex:


    .. py:method:: match_spatial_coverage(spatial_unit, match):
        :noindex:


    .. py:method:: clear_spatial_coverage_terms():
        :noindex:


    .. py:attribute:: spatial_coverage_terms
        :noindex:


    .. py:method:: match_spatial_coverage_overlap(spatial_unit, match):
        :noindex:


    .. py:method:: match_any_spatial_coverage(match):
        :noindex:


    .. py:method:: clear_spatial_coverage_overlap_terms():
        :noindex:


    .. py:attribute:: spatial_coverage_overlap_terms
        :noindex:


    .. py:method:: match_asset_content_id(asset_content_id, match):
        :noindex:


    .. py:method:: clear_asset_content_id_terms():
        :noindex:


    .. py:attribute:: asset_content_id_terms
        :noindex:


    .. py:method:: supports_asset_content_query():
        :noindex:


    .. py:method:: get_asset_content_query():
        :noindex:


    .. py:attribute:: asset_content_query
        :noindex:


    .. py:method:: match_any_asset_content(match):
        :noindex:


    .. py:method:: clear_asset_content_terms():
        :noindex:


    .. py:attribute:: asset_content_terms
        :noindex:


    .. py:method:: match_composition_id(composition_id, match):
        :noindex:


    .. py:method:: clear_composition_id_terms():
        :noindex:


    .. py:attribute:: composition_id_terms
        :noindex:


    .. py:method:: supports_composition_query():
        :noindex:


    .. py:method:: get_composition_query():
        :noindex:


    .. py:attribute:: composition_query
        :noindex:


    .. py:method:: match_any_composition(match):
        :noindex:


    .. py:method:: clear_composition_terms():
        :noindex:


    .. py:attribute:: composition_terms
        :noindex:


    .. py:method:: match_repository_id(repository_id, match):
        :noindex:


    .. py:method:: clear_repository_id_terms():
        :noindex:


    .. py:attribute:: repository_id_terms
        :noindex:


    .. py:method:: supports_repository_query():
        :noindex:


    .. py:method:: get_repository_query():
        :noindex:


    .. py:attribute:: repository_query
        :noindex:


    .. py:method:: clear_repository_terms():
        :noindex:


    .. py:attribute:: repository_terms
        :noindex:


    .. py:method:: get_asset_query_record(asset_record_type):
        :noindex:


Asset Content Query
-------------------

.. py:class:: AssetContentQuery(abc_repository_queries.AssetContentQuery, osid_queries.OsidObjectQuery, osid_queries.OsidSubjugateableQuery)
    This is the query for searching asset contents.


    Each method forms an ``AND`` term while multiple invocations of the
    same method produce a nested ``OR``.





    .. py:method:: match_accessibility_type(accessibility_type, match):
        :noindex:


    .. py:method:: match_any_accessibility_type(match):
        :noindex:


    .. py:method:: clear_accessibility_type_terms():
        :noindex:


    .. py:attribute:: accessibility_type_terms
        :noindex:


    .. py:method:: match_data_length(low, high, match):
        :noindex:


    .. py:method:: match_any_data_length(match):
        :noindex:


    .. py:method:: clear_data_length_terms():
        :noindex:


    .. py:attribute:: data_length_terms
        :noindex:


    .. py:method:: match_data(data, match, partial):
        :noindex:


    .. py:method:: match_any_data(match):
        :noindex:


    .. py:method:: clear_data_terms():
        :noindex:


    .. py:attribute:: data_terms
        :noindex:


    .. py:method:: match_url(url, string_match_type, match):
        :noindex:


    .. py:method:: match_any_url(match):
        :noindex:


    .. py:method:: clear_url_terms():
        :noindex:


    .. py:attribute:: url_terms
        :noindex:


    .. py:method:: get_asset_content_query_record(asset_content_record_type):
        :noindex:


Composition Query
-----------------

.. py:class:: CompositionQuery(abc_repository_queries.CompositionQuery, osid_queries.OsidObjectQuery, osid_queries.OsidContainableQuery, osid_queries.OsidOperableQuery, osid_queries.OsidSourceableQuery)
    This is the query for searching compositions.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produces a nested ``OR``.





    .. py:method:: match_asset_id(asset_id, match):
        :noindex:


    .. py:method:: clear_asset_id_terms():
        :noindex:


    .. py:attribute:: asset_id_terms
        :noindex:


    .. py:method:: supports_asset_query():
        :noindex:


    .. py:method:: get_asset_query():
        :noindex:


    .. py:attribute:: asset_query
        :noindex:


    .. py:method:: match_any_asset(match):
        :noindex:


    .. py:method:: clear_asset_terms():
        :noindex:


    .. py:attribute:: asset_terms
        :noindex:


    .. py:method:: match_containing_composition_id(composition_id, match):
        :noindex:


    .. py:method:: clear_containing_composition_id_terms():
        :noindex:


    .. py:attribute:: containing_composition_id_terms
        :noindex:


    .. py:method:: supports_containing_composition_query():
        :noindex:


    .. py:method:: get_containing_composition_query():
        :noindex:


    .. py:attribute:: containing_composition_query
        :noindex:


    .. py:method:: match_any_containing_composition(match):
        :noindex:


    .. py:method:: clear_containing_composition_terms():
        :noindex:


    .. py:attribute:: containing_composition_terms
        :noindex:


    .. py:method:: match_contained_composition_id(composition_id, match):
        :noindex:


    .. py:method:: clear_contained_composition_id_terms():
        :noindex:


    .. py:attribute:: contained_composition_id_terms
        :noindex:


    .. py:method:: supports_contained_composition_query():
        :noindex:


    .. py:method:: get_contained_composition_query():
        :noindex:


    .. py:attribute:: contained_composition_query
        :noindex:


    .. py:method:: match_any_contained_composition(match):
        :noindex:


    .. py:method:: clear_contained_composition_terms():
        :noindex:


    .. py:attribute:: contained_composition_terms
        :noindex:


    .. py:method:: match_repository_id(repository_id, match):
        :noindex:


    .. py:method:: clear_repository_id_terms():
        :noindex:


    .. py:attribute:: repository_id_terms
        :noindex:


    .. py:method:: supports_repository_query():
        :noindex:


    .. py:method:: get_repository_query():
        :noindex:


    .. py:attribute:: repository_query
        :noindex:


    .. py:method:: clear_repository_terms():
        :noindex:


    .. py:attribute:: repository_terms
        :noindex:


    .. py:method:: get_composition_query_record(composition_record_type):
        :noindex:


Repository Query
----------------

.. py:class:: RepositoryQuery(abc_repository_queries.RepositoryQuery, osid_queries.OsidCatalogQuery)
    This is the query for searching repositories.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_asset_id(asset_id, match):
        :noindex:


    .. py:method:: clear_asset_id_terms():
        :noindex:


    .. py:attribute:: asset_id_terms
        :noindex:


    .. py:method:: supports_asset_query():
        :noindex:


    .. py:method:: get_asset_query():
        :noindex:


    .. py:attribute:: asset_query
        :noindex:


    .. py:method:: match_any_asset(match):
        :noindex:


    .. py:method:: clear_asset_terms():
        :noindex:


    .. py:attribute:: asset_terms
        :noindex:


    .. py:method:: match_composition_id(composition_id, match):
        :noindex:


    .. py:method:: clear_composition_id_terms():
        :noindex:


    .. py:attribute:: composition_id_terms
        :noindex:


    .. py:method:: supports_composition_query():
        :noindex:


    .. py:method:: get_composition_query():
        :noindex:


    .. py:attribute:: composition_query
        :noindex:


    .. py:method:: match_any_composition(match):
        :noindex:


    .. py:method:: clear_composition_terms():
        :noindex:


    .. py:attribute:: composition_terms
        :noindex:


    .. py:method:: match_ancestor_repository_id(repository_id, match):
        :noindex:


    .. py:method:: clear_ancestor_repository_id_terms():
        :noindex:


    .. py:attribute:: ancestor_repository_id_terms
        :noindex:


    .. py:method:: supports_ancestor_repository_query():
        :noindex:


    .. py:method:: get_ancestor_repository_query():
        :noindex:


    .. py:attribute:: ancestor_repository_query
        :noindex:


    .. py:method:: match_any_ancestor_repository(match):
        :noindex:


    .. py:method:: clear_ancestor_repository_terms():
        :noindex:


    .. py:attribute:: ancestor_repository_terms
        :noindex:


    .. py:method:: match_descendant_repository_id(repository_id, match):
        :noindex:


    .. py:method:: clear_descendant_repository_id_terms():
        :noindex:


    .. py:attribute:: descendant_repository_id_terms
        :noindex:


    .. py:method:: supports_descendant_repository_query():
        :noindex:


    .. py:method:: get_descendant_repository_query():
        :noindex:


    .. py:attribute:: descendant_repository_query
        :noindex:


    .. py:method:: match_any_descendant_repository(match):
        :noindex:


    .. py:method:: clear_descendant_repository_terms():
        :noindex:


    .. py:attribute:: descendant_repository_terms
        :noindex:


    .. py:method:: get_repository_query_record(repository_record_type):
        :noindex:


