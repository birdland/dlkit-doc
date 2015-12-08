
.. currentmodule:: dlkit.repository.objects
.. automodule:: dlkit.repository.objects

Objects
=======


Asset
-----

.. autoclass:: Asset
   :show-inheritance:

   .. autoattribute:: Asset.title

   .. automethod:: Asset.is_copyright_status_known

   .. automethod:: Asset.is_public_domain

   .. autoattribute:: Asset.copyright

   .. autoattribute:: Asset.copyright_registration

   .. automethod:: Asset.can_distribute_verbatim

   .. automethod:: Asset.can_distribute_alterations

   .. automethod:: Asset.can_distribute_compositions

   .. autoattribute:: Asset.source_id

   .. autoattribute:: Asset.source

   .. autoattribute:: Asset.provider_link_ids

   .. autoattribute:: Asset.provider_links

   .. autoattribute:: Asset.created_date

   .. automethod:: Asset.is_published

   .. autoattribute:: Asset.published_date

   .. autoattribute:: Asset.principal_credit_string

   .. autoattribute:: Asset.asset_content_ids

   .. autoattribute:: Asset.asset_contents

   .. automethod:: Asset.is_composition

   .. autoattribute:: Asset.composition_id

   .. autoattribute:: Asset.composition

   .. automethod:: Asset.get_asset_record



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Asset Form
----------

.. autoclass:: AssetForm
   :show-inheritance:

   .. autoattribute:: AssetForm.title_metadata

   .. autoattribute:: AssetForm.title

   .. autoattribute:: AssetForm.public_domain_metadata

   .. autoattribute:: AssetForm.public_domain

   .. autoattribute:: AssetForm.copyright_metadata

   .. autoattribute:: AssetForm.copyright

   .. autoattribute:: AssetForm.copyright_registration_metadata

   .. autoattribute:: AssetForm.copyright_registration

   .. autoattribute:: AssetForm.distribute_verbatim_metadata

   .. autoattribute:: AssetForm.distribute_verbatim

   .. autoattribute:: AssetForm.distribute_alterations_metadata

   .. autoattribute:: AssetForm.distribute_alterations

   .. autoattribute:: AssetForm.distribute_compositions_metadata

   .. autoattribute:: AssetForm.distribute_compositions

   .. autoattribute:: AssetForm.source_metadata

   .. autoattribute:: AssetForm.source

   .. autoattribute:: AssetForm.provider_links_metadata

   .. autoattribute:: AssetForm.provider_links

   .. autoattribute:: AssetForm.created_date_metadata

   .. autoattribute:: AssetForm.created_date

   .. autoattribute:: AssetForm.published_metadata

   .. autoattribute:: AssetForm.published

   .. autoattribute:: AssetForm.published_date_metadata

   .. autoattribute:: AssetForm.published_date

   .. autoattribute:: AssetForm.principal_credit_string_metadata

   .. autoattribute:: AssetForm.principal_credit_string

   .. autoattribute:: AssetForm.composition_metadata

   .. autoattribute:: AssetForm.composition

   .. automethod:: AssetForm.get_asset_form_record



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Asset List
----------

.. autoclass:: AssetList
   :show-inheritance:

   .. autoattribute:: AssetList.next_asset

   .. automethod:: AssetList.get_next_assets



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Asset Content
-------------

.. autoclass:: AssetContent
   :show-inheritance:

   .. autoattribute:: AssetContent.asset_id

   .. autoattribute:: AssetContent.asset

   .. autoattribute:: AssetContent.accessibility_types

   .. automethod:: AssetContent.has_data_length

   .. autoattribute:: AssetContent.data_length

   .. autoattribute:: AssetContent.data

   .. automethod:: AssetContent.has_url

   .. autoattribute:: AssetContent.url

   .. automethod:: AssetContent.get_asset_content_record



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Asset Content Form
------------------

.. autoclass:: AssetContentForm
   :show-inheritance:

   .. autoattribute:: AssetContentForm.accessibility_type_metadata

   .. automethod:: AssetContentForm.add_accessibility_type

   .. automethod:: AssetContentForm.remove_accessibility_type

   .. autoattribute:: AssetContentForm.accessibility_types

   .. autoattribute:: AssetContentForm.data_metadata

   .. autoattribute:: AssetContentForm.data

   .. autoattribute:: AssetContentForm.url_metadata

   .. autoattribute:: AssetContentForm.url

   .. automethod:: AssetContentForm.get_asset_content_form_record



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Asset Content List
------------------

.. autoclass:: AssetContentList
   :show-inheritance:

   .. autoattribute:: AssetContentList.next_asset_content

   .. automethod:: AssetContentList.get_next_asset_contents



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Composition
-----------

.. autoclass:: Composition
   :show-inheritance:

   .. autoattribute:: Composition.children_ids

   .. autoattribute:: Composition.children

   .. automethod:: Composition.get_composition_record



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Composition Form
----------------

.. autoclass:: CompositionForm
   :show-inheritance:

   .. automethod:: CompositionForm.get_composition_form_record



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Composition List
----------------

.. autoclass:: CompositionList
   :show-inheritance:

   .. autoattribute:: CompositionList.next_composition

   .. automethod:: CompositionList.get_next_compositions



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Repository Form
---------------

.. autoclass:: RepositoryForm
   :show-inheritance:

   .. automethod:: RepositoryForm.get_repository_form_record



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Repository List
---------------

.. autoclass:: RepositoryList
   :show-inheritance:

   .. autoattribute:: RepositoryList.next_repository

   .. automethod:: RepositoryList.get_next_repositories



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Repository Node
---------------

.. autoclass:: RepositoryNode
   :show-inheritance:

   .. autoattribute:: RepositoryNode.repository

   .. autoattribute:: RepositoryNode.parent_repository_nodes

   .. autoattribute:: RepositoryNode.child_repository_nodes



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



Repository Node List
--------------------

.. autoclass:: RepositoryNodeList
   :show-inheritance:

   .. autoattribute:: RepositoryNodeList.next_repository_node

   .. automethod:: RepositoryNodeList.get_next_repository_nodes



Asset Repository Methods
------------------------

   .. automethod:: AssetRepositorySession.can_lookup_asset_repository_mappings

   .. automethod:: AssetRepositorySession.use_comparative_repository_view

   .. automethod:: AssetRepositorySession.use_plenary_repository_view

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repository

   .. automethod:: AssetRepositorySession.get_assets_by_repository

   .. automethod:: AssetRepositorySession.get_asset_ids_by_repositories

   .. automethod:: AssetRepositorySession.get_assets_by_repositories

   .. automethod:: AssetRepositorySession.get_repository_ids_by_asset

   .. automethod:: AssetRepositorySession.get_repositories_by_asset



Asset Repository Assignment Methods
-----------------------------------

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets

   .. automethod:: AssetRepositoryAssignmentSession.can_assign_assets_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: AssetRepositoryAssignmentSession.get_assignable_repository_ids_for_asset

   .. automethod:: AssetRepositoryAssignmentSession.assign_asset_to_repository

   .. automethod:: AssetRepositoryAssignmentSession.unassign_asset_from_repository



Composition Repository Methods
------------------------------

   .. automethod:: CompositionRepositorySession.use_comparative_composition_repository_view

   .. automethod:: CompositionRepositorySession.use_plenary_composition_repository_view

   .. automethod:: CompositionRepositorySession.can_lookup_composition_repository_mappings

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repository

   .. automethod:: CompositionRepositorySession.get_compositions_by_repository

   .. automethod:: CompositionRepositorySession.get_composition_ids_by_repositories

   .. automethod:: CompositionRepositorySession.get_compoitions_by_repositories

   .. automethod:: CompositionRepositorySession.get_repository_ids_by_composition

   .. automethod:: CompositionRepositorySession.get_repositories_by_composition



Composition Repository Assignment Methods
-----------------------------------------

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions

   .. automethod:: CompositionRepositoryAssignmentSession.can_assign_compositions_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids

   .. automethod:: CompositionRepositoryAssignmentSession.get_assignable_repository_ids_for_composition

   .. automethod:: CompositionRepositoryAssignmentSession.assign_composition_to_repository

   .. automethod:: CompositionRepositoryAssignmentSession.unassign_composition_from_repository



Repository Lookup Methods
-------------------------

   .. automethod:: RepositoryLookupSession.can_lookup_repositories

   .. automethod:: RepositoryLookupSession.use_comparative_repository_view

   .. automethod:: RepositoryLookupSession.use_plenary_repository_view

   .. automethod:: RepositoryLookupSession.get_repository

   .. automethod:: RepositoryLookupSession.get_repositories_by_ids

   .. automethod:: RepositoryLookupSession.get_repositories_by_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_parent_genus_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_record_type

   .. automethod:: RepositoryLookupSession.get_repositories_by_provider

   .. autoattribute:: RepositoryLookupSession.repositories



Repository Query Methods
------------------------

   .. automethod:: RepositoryQuerySession.can_search_repositories

   .. autoattribute:: RepositoryQuerySession.repository_query

   .. automethod:: RepositoryQuerySession.get_repositories_by_query



Repository Admin Methods
------------------------

   .. automethod:: RepositoryAdminSession.can_create_repositories

   .. automethod:: RepositoryAdminSession.can_create_repository_with_record_types

   .. automethod:: RepositoryAdminSession.get_repository_form_for_create

   .. automethod:: RepositoryAdminSession.create_repository

   .. automethod:: RepositoryAdminSession.can_update_repositories

   .. automethod:: RepositoryAdminSession.get_repository_form_for_update

   .. automethod:: RepositoryAdminSession.update_repository

   .. automethod:: RepositoryAdminSession.can_delete_repositories

   .. automethod:: RepositoryAdminSession.delete_repository

   .. automethod:: RepositoryAdminSession.can_manage_repository_aliases

   .. automethod:: RepositoryAdminSession.alias_repository



Repository Hierarchy Methods
----------------------------

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchySession.repository_hierarchy

   .. automethod:: RepositoryHierarchySession.can_access_repository_hierarchy

   .. automethod:: RepositoryHierarchySession.use_comparative_repository_view

   .. automethod:: RepositoryHierarchySession.use_plenary_repository_view

   .. autoattribute:: RepositoryHierarchySession.root_repository_ids

   .. autoattribute:: RepositoryHierarchySession.root_repositories

   .. automethod:: RepositoryHierarchySession.has_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_parent_of_repository

   .. automethod:: RepositoryHierarchySession.get_parent_repository_ids

   .. automethod:: RepositoryHierarchySession.get_parent_repositories

   .. automethod:: RepositoryHierarchySession.is_ancestor_of_repository

   .. automethod:: RepositoryHierarchySession.has_child_repositories

   .. automethod:: RepositoryHierarchySession.is_child_of_repository

   .. automethod:: RepositoryHierarchySession.get_child_repository_ids

   .. automethod:: RepositoryHierarchySession.get_child_repositories

   .. automethod:: RepositoryHierarchySession.is_descendant_of_repository

   .. automethod:: RepositoryHierarchySession.get_repository_node_ids

   .. automethod:: RepositoryHierarchySession.get_repository_nodes



Repository Hierarchy Design Methods
-----------------------------------

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy_id

   .. autoattribute:: RepositoryHierarchyDesignSession.repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.can_modify_repository_hierarchy

   .. automethod:: RepositoryHierarchyDesignSession.add_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_root_repository

   .. automethod:: RepositoryHierarchyDesignSession.add_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repository

   .. automethod:: RepositoryHierarchyDesignSession.remove_child_repositories



Asset Lookup Methods
--------------------

   .. autoattribute:: AssetLookupSession.repository_id

   .. autoattribute:: AssetLookupSession.repository

   .. automethod:: AssetLookupSession.can_lookup_assets

   .. automethod:: AssetLookupSession.use_comparative_asset_view

   .. automethod:: AssetLookupSession.use_plenary_asset_view

   .. automethod:: AssetLookupSession.use_federated_repository_view

   .. automethod:: AssetLookupSession.use_isolated_repository_view

   .. automethod:: AssetLookupSession.get_asset

   .. automethod:: AssetLookupSession.get_assets_by_ids

   .. automethod:: AssetLookupSession.get_assets_by_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_parent_genus_type

   .. automethod:: AssetLookupSession.get_assets_by_record_type

   .. automethod:: AssetLookupSession.get_assets_by_provider

   .. autoattribute:: AssetLookupSession.assets



Asset Query Methods
-------------------

   .. autoattribute:: AssetQuerySession.repository_id

   .. autoattribute:: AssetQuerySession.repository

   .. automethod:: AssetQuerySession.can_search_assets

   .. automethod:: AssetQuerySession.use_federated_repository_view

   .. automethod:: AssetQuerySession.use_isolated_repository_view

   .. autoattribute:: AssetQuerySession.asset_query

   .. automethod:: AssetQuerySession.get_assets_by_query



Asset Search Methods
--------------------

   .. autoattribute:: AssetSearchSession.asset_search

   .. autoattribute:: AssetSearchSession.asset_search_order

   .. automethod:: AssetSearchSession.get_assets_by_search

   .. automethod:: AssetSearchSession.get_asset_query_from_inspector



Asset Admin Methods
-------------------

   .. autoattribute:: AssetAdminSession.repository_id

   .. autoattribute:: AssetAdminSession.repository

   .. automethod:: AssetAdminSession.can_create_assets

   .. automethod:: AssetAdminSession.can_create_asset_with_record_types

   .. automethod:: AssetAdminSession.get_asset_form_for_create

   .. automethod:: AssetAdminSession.create_asset

   .. automethod:: AssetAdminSession.can_update_assets

   .. automethod:: AssetAdminSession.get_asset_form_for_update

   .. automethod:: AssetAdminSession.update_asset

   .. automethod:: AssetAdminSession.can_delete_assets

   .. automethod:: AssetAdminSession.delete_asset

   .. automethod:: AssetAdminSession.can_manage_asset_aliases

   .. automethod:: AssetAdminSession.alias_asset

   .. automethod:: AssetAdminSession.can_create_asset_content

   .. automethod:: AssetAdminSession.can_create_asset_content_with_record_types

   .. automethod:: AssetAdminSession.get_asset_content_form_for_create

   .. automethod:: AssetAdminSession.create_asset_content

   .. automethod:: AssetAdminSession.can_update_asset_contents

   .. automethod:: AssetAdminSession.get_asset_content_form_for_update

   .. automethod:: AssetAdminSession.update_asset_content

   .. automethod:: AssetAdminSession.can_delete_asset_contents

   .. automethod:: AssetAdminSession.delete_asset_content



Asset Notification Methods
--------------------------

   .. autoattribute:: AssetNotificationSession.repository_id

   .. autoattribute:: AssetNotificationSession.repository

   .. automethod:: AssetNotificationSession.can_register_for_asset_notifications

   .. automethod:: AssetNotificationSession.use_federated_repository_view

   .. automethod:: AssetNotificationSession.use_isolated_repository_view

   .. automethod:: AssetNotificationSession.register_for_new_assets

   .. automethod:: AssetNotificationSession.register_for_new_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_assets

   .. automethod:: AssetNotificationSession.register_for_changed_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_changed_asset

   .. automethod:: AssetNotificationSession.register_for_deleted_assets

   .. automethod:: AssetNotificationSession.register_for_deleted_assets_by_genus_type

   .. automethod:: AssetNotificationSession.register_for_deleted_asset

   .. automethod:: AssetNotificationSession.reliable_asset_notifications

   .. automethod:: AssetNotificationSession.unreliable_asset_notifications

   .. automethod:: AssetNotificationSession.acknowledge_asset_notification



Asset Composition Methods
-------------------------

   .. autoattribute:: AssetCompositionSession.repository_id

   .. autoattribute:: AssetCompositionSession.repository

   .. automethod:: AssetCompositionSession.can_access_asset_compositions

   .. automethod:: AssetCompositionSession.use_comparative_asset_composition_view

   .. automethod:: AssetCompositionSession.use_plenary_asset_composition_view

   .. automethod:: AssetCompositionSession.use_federated_repository_view

   .. automethod:: AssetCompositionSession.use_isolated_repository_view

   .. automethod:: AssetCompositionSession.get_composition_assets

   .. automethod:: AssetCompositionSession.get_compositions_by_asset



Asset Composition Design Methods
--------------------------------

   .. autoattribute:: AssetCompositionDesignSession.repository_id

   .. autoattribute:: AssetCompositionDesignSession.repository

   .. automethod:: AssetCompositionDesignSession.can_compose_assets

   .. automethod:: AssetCompositionDesignSession.add_asset

   .. automethod:: AssetCompositionDesignSession.move_asset_ahead

   .. automethod:: AssetCompositionDesignSession.move_asset_behind

   .. automethod:: AssetCompositionDesignSession.order_assets

   .. automethod:: AssetCompositionDesignSession.remove_asset



Composition Lookup Methods
--------------------------

   .. autoattribute:: CompositionLookupSession.repository_id

   .. autoattribute:: CompositionLookupSession.repository

   .. automethod:: CompositionLookupSession.can_lookup_compositions

   .. automethod:: CompositionLookupSession.use_comparative_composition_view

   .. automethod:: CompositionLookupSession.use_plenary_composition_view

   .. automethod:: CompositionLookupSession.use_federated_repository_view

   .. automethod:: CompositionLookupSession.use_isolated_repository_view

   .. automethod:: CompositionLookupSession.use_active_composition_view

   .. automethod:: CompositionLookupSession.use_any_status_composition_view

   .. automethod:: CompositionLookupSession.use_sequestered_composition_view

   .. automethod:: CompositionLookupSession.use_unsequestered_composition_view

   .. automethod:: CompositionLookupSession.get_composition

   .. automethod:: CompositionLookupSession.get_compositions_by_ids

   .. automethod:: CompositionLookupSession.get_compositions_by_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_parent_genus_type

   .. automethod:: CompositionLookupSession.get_compositions_by_record_type

   .. automethod:: CompositionLookupSession.get_compositions_by_provider

   .. autoattribute:: CompositionLookupSession.compositions



Composition Query Methods
-------------------------

   .. autoattribute:: CompositionQuerySession.repository_id

   .. autoattribute:: CompositionQuerySession.repository

   .. automethod:: CompositionQuerySession.can_search_compositions

   .. automethod:: CompositionQuerySession.use_federated_repository_view

   .. automethod:: CompositionQuerySession.use_isolated_repository_view

   .. automethod:: CompositionQuerySession.use_sequestered_composition_view

   .. automethod:: CompositionQuerySession.use_unsequestered_composition_view

   .. autoattribute:: CompositionQuerySession.composition_query

   .. automethod:: CompositionQuerySession.get_compositions_by_query



Composition Search Methods
--------------------------

   .. autoattribute:: CompositionSearchSession.composition_search

   .. autoattribute:: CompositionSearchSession.composition_search_order

   .. automethod:: CompositionSearchSession.get_compositions_by_search

   .. automethod:: CompositionSearchSession.get_composition_query_from_inspector



Composition Admin Methods
-------------------------

   .. autoattribute:: CompositionAdminSession.repository_id

   .. autoattribute:: CompositionAdminSession.repository

   .. automethod:: CompositionAdminSession.can_create_compositions

   .. automethod:: CompositionAdminSession.can_create_composition_with_record_types

   .. automethod:: CompositionAdminSession.get_composition_form_for_create

   .. automethod:: CompositionAdminSession.create_composition

   .. automethod:: CompositionAdminSession.can_update_compositions

   .. automethod:: CompositionAdminSession.get_composition_form_for_update

   .. automethod:: CompositionAdminSession.update_composition

   .. automethod:: CompositionAdminSession.can_delete_compositions

   .. automethod:: CompositionAdminSession.delete_composition

   .. automethod:: CompositionAdminSession.delete_composition_node

   .. automethod:: CompositionAdminSession.add_composition_child

   .. automethod:: CompositionAdminSession.remove_composition_child

   .. automethod:: CompositionAdminSession.can_manage_composition_aliases

   .. automethod:: CompositionAdminSession.alias_composition



