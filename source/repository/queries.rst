.. currentmodule:: dlkit.abstract_osid.repository.queries
.. automodule:: dlkit.abstract_osid.repository.queries

Queries
=======


Asset Query
-----------

.. autoclass:: AssetQuery
   :show-inheritance:

.. automethod:: AssetQuery.match_title

.. automethod:: AssetQuery.match_any_title

.. autoattribute:: AssetQuery.title_terms

.. automethod:: AssetQuery.match_public_domain

.. automethod:: AssetQuery.match_any_public_domain

.. autoattribute:: AssetQuery.public_domain_terms

.. automethod:: AssetQuery.match_copyright

.. automethod:: AssetQuery.match_any_copyright

.. autoattribute:: AssetQuery.copyright_terms

.. automethod:: AssetQuery.match_copyright_registration

.. automethod:: AssetQuery.match_any_copyright_registration

.. autoattribute:: AssetQuery.copyright_registration_terms

.. automethod:: AssetQuery.match_distribute_verbatim

.. autoattribute:: AssetQuery.distribute_verbatim_terms

.. automethod:: AssetQuery.match_distribute_alterations

.. autoattribute:: AssetQuery.distribute_alterations_terms

.. automethod:: AssetQuery.match_distribute_compositions

.. autoattribute:: AssetQuery.distribute_compositions_terms

.. automethod:: AssetQuery.match_source_id

.. autoattribute:: AssetQuery.source_id_terms

.. automethod:: AssetQuery.supports_source_query

.. autoattribute:: AssetQuery.source_query

.. automethod:: AssetQuery.match_any_source

.. autoattribute:: AssetQuery.source_terms

.. automethod:: AssetQuery.match_created_date

.. automethod:: AssetQuery.match_any_created_date

.. autoattribute:: AssetQuery.created_date_terms

.. automethod:: AssetQuery.match_published

.. autoattribute:: AssetQuery.published_terms

.. automethod:: AssetQuery.match_published_date

.. automethod:: AssetQuery.match_any_published_date

.. autoattribute:: AssetQuery.published_date_terms

.. automethod:: AssetQuery.match_principal_credit_string

.. automethod:: AssetQuery.match_any_principal_credit_string

.. autoattribute:: AssetQuery.principal_credit_string_terms

.. automethod:: AssetQuery.match_temporal_coverage

.. automethod:: AssetQuery.match_any_temporal_coverage

.. autoattribute:: AssetQuery.temporal_coverage_terms

.. automethod:: AssetQuery.match_location_id

.. autoattribute:: AssetQuery.location_id_terms

.. automethod:: AssetQuery.supports_location_query

.. autoattribute:: AssetQuery.location_query

.. automethod:: AssetQuery.match_any_location

.. autoattribute:: AssetQuery.location_terms

.. automethod:: AssetQuery.match_spatial_coverage

.. autoattribute:: AssetQuery.spatial_coverage_terms

.. automethod:: AssetQuery.match_spatial_coverage_overlap

.. automethod:: AssetQuery.match_any_spatial_coverage

.. autoattribute:: AssetQuery.spatial_coverage_overlap_terms

.. automethod:: AssetQuery.match_asset_content_id

.. autoattribute:: AssetQuery.asset_content_id_terms

.. automethod:: AssetQuery.supports_asset_content_query

.. autoattribute:: AssetQuery.asset_content_query

.. automethod:: AssetQuery.match_any_asset_content

.. autoattribute:: AssetQuery.asset_content_terms

.. automethod:: AssetQuery.match_composition_id

.. autoattribute:: AssetQuery.composition_id_terms

.. automethod:: AssetQuery.supports_composition_query

.. autoattribute:: AssetQuery.composition_query

.. automethod:: AssetQuery.match_any_composition

.. autoattribute:: AssetQuery.composition_terms

.. automethod:: AssetQuery.match_repository_id

.. autoattribute:: AssetQuery.repository_id_terms

.. automethod:: AssetQuery.supports_repository_query

.. autoattribute:: AssetQuery.repository_query

.. autoattribute:: AssetQuery.repository_terms

.. automethod:: AssetQuery.get_asset_query_record



Asset Content Query
-------------------

.. autoclass:: AssetContentQuery
   :show-inheritance:

.. automethod:: AssetContentQuery.match_accessibility_type

.. automethod:: AssetContentQuery.match_any_accessibility_type

.. autoattribute:: AssetContentQuery.accessibility_type_terms

.. automethod:: AssetContentQuery.match_data_length

.. automethod:: AssetContentQuery.match_any_data_length

.. autoattribute:: AssetContentQuery.data_length_terms

.. automethod:: AssetContentQuery.match_data

.. automethod:: AssetContentQuery.match_any_data

.. autoattribute:: AssetContentQuery.data_terms

.. automethod:: AssetContentQuery.match_url

.. automethod:: AssetContentQuery.match_any_url

.. autoattribute:: AssetContentQuery.url_terms

.. automethod:: AssetContentQuery.get_asset_content_query_record



Composition Query
-----------------

.. autoclass:: CompositionQuery
   :show-inheritance:

.. automethod:: CompositionQuery.match_asset_id

.. autoattribute:: CompositionQuery.asset_id_terms

.. automethod:: CompositionQuery.supports_asset_query

.. autoattribute:: CompositionQuery.asset_query

.. automethod:: CompositionQuery.match_any_asset

.. autoattribute:: CompositionQuery.asset_terms

.. automethod:: CompositionQuery.match_containing_composition_id

.. autoattribute:: CompositionQuery.containing_composition_id_terms

.. automethod:: CompositionQuery.supports_containing_composition_query

.. autoattribute:: CompositionQuery.containing_composition_query

.. automethod:: CompositionQuery.match_any_containing_composition

.. autoattribute:: CompositionQuery.containing_composition_terms

.. automethod:: CompositionQuery.match_contained_composition_id

.. autoattribute:: CompositionQuery.contained_composition_id_terms

.. automethod:: CompositionQuery.supports_contained_composition_query

.. autoattribute:: CompositionQuery.contained_composition_query

.. automethod:: CompositionQuery.match_any_contained_composition

.. autoattribute:: CompositionQuery.contained_composition_terms

.. automethod:: CompositionQuery.match_repository_id

.. autoattribute:: CompositionQuery.repository_id_terms

.. automethod:: CompositionQuery.supports_repository_query

.. autoattribute:: CompositionQuery.repository_query

.. autoattribute:: CompositionQuery.repository_terms

.. automethod:: CompositionQuery.get_composition_query_record



Repository Query
----------------

.. autoclass:: RepositoryQuery
   :show-inheritance:

.. automethod:: RepositoryQuery.match_asset_id

.. autoattribute:: RepositoryQuery.asset_id_terms

.. automethod:: RepositoryQuery.supports_asset_query

.. autoattribute:: RepositoryQuery.asset_query

.. automethod:: RepositoryQuery.match_any_asset

.. autoattribute:: RepositoryQuery.asset_terms

.. automethod:: RepositoryQuery.match_composition_id

.. autoattribute:: RepositoryQuery.composition_id_terms

.. automethod:: RepositoryQuery.supports_composition_query

.. autoattribute:: RepositoryQuery.composition_query

.. automethod:: RepositoryQuery.match_any_composition

.. autoattribute:: RepositoryQuery.composition_terms

.. automethod:: RepositoryQuery.match_ancestor_repository_id

.. autoattribute:: RepositoryQuery.ancestor_repository_id_terms

.. automethod:: RepositoryQuery.supports_ancestor_repository_query

.. autoattribute:: RepositoryQuery.ancestor_repository_query

.. automethod:: RepositoryQuery.match_any_ancestor_repository

.. autoattribute:: RepositoryQuery.ancestor_repository_terms

.. automethod:: RepositoryQuery.match_descendant_repository_id

.. autoattribute:: RepositoryQuery.descendant_repository_id_terms

.. automethod:: RepositoryQuery.supports_descendant_repository_query

.. autoattribute:: RepositoryQuery.descendant_repository_query

.. automethod:: RepositoryQuery.match_any_descendant_repository

.. autoattribute:: RepositoryQuery.descendant_repository_terms

.. automethod:: RepositoryQuery.get_repository_query_record



