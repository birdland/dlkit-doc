.. currentmodule:: dlkit.repository.query_inspectors
.. automodule:: dlkit.repository.query_inspectors

Query_Inspectors
================


Asset Query Inspector
---------------------

.. autoclass:: AssetQueryInspector
   :show-inheritance:

.. autoattribute:: AssetQueryInspector.title_terms

.. autoattribute:: AssetQueryInspector.public_domain_terms

.. autoattribute:: AssetQueryInspector.copyright_terms

.. autoattribute:: AssetQueryInspector.copyright_registration_terms

.. autoattribute:: AssetQueryInspector.distribute_verbatim_terms

.. autoattribute:: AssetQueryInspector.distribute_alterations_terms

.. autoattribute:: AssetQueryInspector.distribute_compositions_terms

.. autoattribute:: AssetQueryInspector.source_id_terms

.. autoattribute:: AssetQueryInspector.source_terms

.. autoattribute:: AssetQueryInspector.created_date_terms

.. autoattribute:: AssetQueryInspector.published_terms

.. autoattribute:: AssetQueryInspector.published_date_terms

.. autoattribute:: AssetQueryInspector.principal_credit_string_terms

.. autoattribute:: AssetQueryInspector.temporal_coverage_terms

.. autoattribute:: AssetQueryInspector.location_id_terms

.. autoattribute:: AssetQueryInspector.location_terms

.. autoattribute:: AssetQueryInspector.spatial_coverage_terms

.. autoattribute:: AssetQueryInspector.spatial_coverage_overlap_terms

.. autoattribute:: AssetQueryInspector.asset_content_id_terms

.. autoattribute:: AssetQueryInspector.asset_content_terms

.. autoattribute:: AssetQueryInspector.composition_id_terms

.. autoattribute:: AssetQueryInspector.composition_terms

.. autoattribute:: AssetQueryInspector.repository_id_terms

.. autoattribute:: AssetQueryInspector.repository_terms

.. automethod:: AssetQueryInspector.get_asset_query_inspector_record



Asset Content Query Inspector
-----------------------------

.. autoclass:: AssetContentQueryInspector
   :show-inheritance:

.. autoattribute:: AssetContentQueryInspector.accessibility_type_terms

.. autoattribute:: AssetContentQueryInspector.data_length_terms

.. autoattribute:: AssetContentQueryInspector.data_terms

.. autoattribute:: AssetContentQueryInspector.url_terms

.. automethod:: AssetContentQueryInspector.get_asset_content_query_inspector_record



Composition Query Inspector
---------------------------

.. autoclass:: CompositionQueryInspector
   :show-inheritance:

.. autoattribute:: CompositionQueryInspector.asset_id_terms

.. autoattribute:: CompositionQueryInspector.asset_terms

.. autoattribute:: CompositionQueryInspector.containing_composition_id_terms

.. autoattribute:: CompositionQueryInspector.containing_composition_terms

.. autoattribute:: CompositionQueryInspector.contained_composition_id_terms

.. autoattribute:: CompositionQueryInspector.contained_composition_terms

.. autoattribute:: CompositionQueryInspector.repository_id_terms

.. autoattribute:: CompositionQueryInspector.repository_terms

.. automethod:: CompositionQueryInspector.get_composition_query_inspector_record



Repository Query Inspector
--------------------------

.. autoclass:: RepositoryQueryInspector
   :show-inheritance:

.. autoattribute:: RepositoryQueryInspector.asset_id_terms

.. autoattribute:: RepositoryQueryInspector.asset_terms

.. autoattribute:: RepositoryQueryInspector.composition_id_terms

.. autoattribute:: RepositoryQueryInspector.composition_terms

.. autoattribute:: RepositoryQueryInspector.ancestor_repository_id_terms

.. autoattribute:: RepositoryQueryInspector.ancestor_repository_terms

.. autoattribute:: RepositoryQueryInspector.descendant_repository_id_terms

.. autoattribute:: RepositoryQueryInspector.descendant_repository_terms

.. automethod:: RepositoryQueryInspector.get_repository_query_inspector_record



