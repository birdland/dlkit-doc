.. currentmodule:: dlkit.services.repository
.. automodule:: dlkit.services.repository

Repository
==========


Repository
----------

.. autoclass:: Repository
   :show-inheritance:

.. automethod:: Repository.get_repository_record



Asset Lookup Methods
--------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_lookup_assets

.. automethod:: Repository.use_comparative_asset_view

.. automethod:: Repository.use_plenary_asset_view

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. automethod:: Repository.get_asset

.. automethod:: Repository.get_assets_by_ids

.. automethod:: Repository.get_assets_by_genus_type

.. automethod:: Repository.get_assets_by_parent_genus_type

.. automethod:: Repository.get_assets_by_record_type

.. automethod:: Repository.get_assets_by_provider

.. autoattribute:: Repository.assets



Asset Query Methods
-------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_search_assets

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. autoattribute:: Repository.asset_query

.. automethod:: Repository.get_assets_by_query



Asset Search Methods
--------------------

.. autoattribute:: Repository.asset_search

.. autoattribute:: Repository.asset_search_order

.. automethod:: Repository.get_assets_by_search

.. automethod:: Repository.get_asset_query_from_inspector



Asset Admin Methods
-------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_create_assets

.. automethod:: Repository.can_create_asset_with_record_types

.. automethod:: Repository.get_asset_form_for_create

.. automethod:: Repository.create_asset

.. automethod:: Repository.can_update_assets

.. automethod:: Repository.get_asset_form_for_update

.. automethod:: Repository.update_asset

.. automethod:: Repository.can_delete_assets

.. automethod:: Repository.delete_asset

.. automethod:: Repository.can_manage_asset_aliases

.. automethod:: Repository.alias_asset

.. automethod:: Repository.can_create_asset_content

.. automethod:: Repository.can_create_asset_content_with_record_types

.. automethod:: Repository.get_asset_content_form_for_create

.. automethod:: Repository.create_asset_content

.. automethod:: Repository.can_update_asset_contents

.. automethod:: Repository.get_asset_content_form_for_update

.. automethod:: Repository.update_asset_content

.. automethod:: Repository.can_delete_asset_contents

.. automethod:: Repository.delete_asset_content



Asset Notification Methods
--------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_register_for_asset_notifications

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. automethod:: Repository.register_for_new_assets

.. automethod:: Repository.register_for_new_assets_by_genus_type

.. automethod:: Repository.register_for_changed_assets

.. automethod:: Repository.register_for_changed_assets_by_genus_type

.. automethod:: Repository.register_for_changed_asset

.. automethod:: Repository.register_for_deleted_assets

.. automethod:: Repository.register_for_deleted_assets_by_genus_type

.. automethod:: Repository.register_for_deleted_asset



Asset Repository Methods
------------------------

.. automethod:: Repository.can_lookup_asset_repository_mappings

.. automethod:: Repository.use_comparative_repository_view

.. automethod:: Repository.use_plenary_repository_view

.. automethod:: Repository.get_asset_ids_by_repository

.. automethod:: Repository.get_assets_by_repository

.. automethod:: Repository.get_asset_ids_by_repositories

.. automethod:: Repository.get_assets_by_repositories

.. automethod:: Repository.get_repository_ids_by_asset

.. automethod:: Repository.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

.. automethod:: Repository.can_assign_assets

.. automethod:: Repository.can_assign_assets_to_repository

.. automethod:: Repository.get_assignable_repository_ids

.. automethod:: Repository.get_assignable_repository_ids_for_asset

.. automethod:: Repository.assign_asset_to_repository

.. automethod:: Repository.unassign_asset_from_repository



Asset Smart Repository Methods
------------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_manage_smart_repository

.. autoattribute:: Repository.asset_query

.. autoattribute:: Repository.asset_search_order

.. automethod:: Repository.apply_asset_query

.. automethod:: Repository.inspect_asset_query

.. automethod:: Repository.apply_asset_sequencing

.. automethod:: Repository.get_asset_query_from_inspector



Asset Temporal Methods
----------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_lookup_temporal_coverage

.. automethod:: Repository.use_comparative_asset_view

.. automethod:: Repository.use_plenary_asset_view

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. automethod:: Repository.get_temporal_coverage

.. automethod:: Repository.get_asset_ids_by_temporal_coverage

.. automethod:: Repository.get_assets_by_temporal_coverage



Asset Temporal Assignment Methods
---------------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_assign_temporal_coverage

.. automethod:: Repository.add_temporal_coverage

.. automethod:: Repository.remove_temporal_coverage



Asset Spatial Methods
---------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_lookup_spatial_coverage

.. automethod:: Repository.use_comparative_asset_view

.. automethod:: Repository.use_plenary_asset_view

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. automethod:: Repository.get_asset_location_ids

.. automethod:: Repository.get_asset_locations

.. automethod:: Repository.get_asset_spatial_coverage

.. automethod:: Repository.get_asset_ids_by_location

.. automethod:: Repository.get_assets_by_location

.. automethod:: Repository.get_asset_ids_by_spatial_coverage

.. automethod:: Repository.get_assets_by_spatial_coverage



Asset Spatial Assignment Methods
--------------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_assign_spatial_coverage

.. automethod:: Repository.add_asset_location

.. automethod:: Repository.add_asset_spatial_coverage

.. automethod:: Repository.remove_asset_location

.. automethod:: Repository.remove_asset_spatial_coverage



Asset Composition Methods
-------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_access_asset_compositions

.. automethod:: Repository.use_comparative_asset_composition_view

.. automethod:: Repository.use_plenary_asset_composition_view

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. automethod:: Repository.get_composition_assets

.. automethod:: Repository.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_compose_assets

.. automethod:: Repository.add_asset

.. automethod:: Repository.move_asset_ahead

.. automethod:: Repository.move_asset_behind

.. automethod:: Repository.order_assets

.. automethod:: Repository.remove_asset



Composition Lookup Methods
--------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_lookup_compositions

.. automethod:: Repository.use_comparative_composition_view

.. automethod:: Repository.use_plenary_composition_view

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. automethod:: Repository.use_active_composition_view

.. automethod:: Repository.use_any_status_composition_view

.. automethod:: Repository.use_sequestered_composition_view

.. automethod:: Repository.use_unsequestered_composition_view

.. automethod:: Repository.get_composition

.. automethod:: Repository.get_compositions_by_ids

.. automethod:: Repository.get_compositions_by_genus_type

.. automethod:: Repository.get_compositions_by_parent_genus_type

.. automethod:: Repository.get_compositions_by_record_type

.. automethod:: Repository.get_compositions_by_provider

.. autoattribute:: Repository.compositions



Composition Query Methods
-------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_search_compositions

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. automethod:: Repository.use_sequestered_composition_view

.. automethod:: Repository.use_unsequestered_composition_view

.. autoattribute:: Repository.composition_query

.. automethod:: Repository.get_compositions_by_query



Composition Search Methods
--------------------------

.. autoattribute:: Repository.composition_search

.. autoattribute:: Repository.composition_search_order

.. automethod:: Repository.get_compositions_by_search

.. automethod:: Repository.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_create_compositions

.. automethod:: Repository.can_create_composition_with_record_types

.. automethod:: Repository.get_composition_form_for_create

.. automethod:: Repository.create_composition

.. automethod:: Repository.can_update_compositions

.. automethod:: Repository.get_composition_form_for_update

.. automethod:: Repository.update_composition

.. automethod:: Repository.can_delete_compositions

.. automethod:: Repository.delete_composition

.. automethod:: Repository.delete_composition_node

.. automethod:: Repository.add_composition_child

.. automethod:: Repository.remove_composition_child

.. automethod:: Repository.can_manage_composition_aliases

.. automethod:: Repository.alias_composition



Composition Notification Methods
--------------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_register_for_composition_notifications

.. automethod:: Repository.use_federated_repository_view

.. automethod:: Repository.use_isolated_repository_view

.. automethod:: Repository.use_federated_composition_view

.. automethod:: Repository.use_isolated_composition_view

.. automethod:: Repository.register_for_new_compositions

.. automethod:: Repository.register_for_assigned_assets_in_composition

.. automethod:: Repository.register_for_new_composition_ancestor

.. automethod:: Repository.register_for_new_composition_descendants

.. automethod:: Repository.register_for_changed_compositions

.. automethod:: Repository.register_for_changed_composition

.. automethod:: Repository.register_for_deleted_compositions

.. automethod:: Repository.register_for_deleted_composition

.. automethod:: Repository.register_for_unassigned_assets_in_composition

.. automethod:: Repository.register_for_deleted_composition_ancestors

.. automethod:: Repository.register_for_deleted_composition_descendants



Composition Repository Methods
------------------------------

.. automethod:: Repository.use_comparative_composition_repository_view

.. automethod:: Repository.use_plenary_composition_repository_view

.. automethod:: Repository.can_lookup_composition_repository_mappings

.. automethod:: Repository.get_composition_ids_by_repository

.. automethod:: Repository.get_compositions_by_repository

.. automethod:: Repository.get_composition_ids_by_repositories

.. automethod:: Repository.get_compoitions_by_repositories

.. automethod:: Repository.get_repository_ids_by_composition

.. automethod:: Repository.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

.. automethod:: Repository.can_assign_compositions

.. automethod:: Repository.can_assign_compositions_to_repository

.. automethod:: Repository.get_assignable_repository_ids

.. automethod:: Repository.get_assignable_repository_ids_for_composition

.. automethod:: Repository.assign_composition_to_repository

.. automethod:: Repository.unassign_composition_from_repository



Composition Smart Repository Methods
------------------------------------

.. autoattribute:: Repository.repository_id

.. autoattribute:: Repository.repository

.. automethod:: Repository.can_manage_smart_repository

.. autoattribute:: Repository.composition_query

.. autoattribute:: Repository.composition_search_order

.. automethod:: Repository.apply_composition_query

.. automethod:: Repository.inspect_composition_query

.. automethod:: Repository.apply_composition_sequencing

.. automethod:: Repository.get_composition_query_from_inspector



