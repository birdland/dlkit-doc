.. currentmodule:: dlkit.services.installation


Depot
=====


Depot
-----

.. autoclass:: Depot
   :show-inheritance:

   .. automethod:: Depot.get_depot_record



Installation Lookup Methods
---------------------------

   .. autoattribute:: Depot.site_id

   .. autoattribute:: Depot.site

   .. automethod:: Depot.can_lookup_installations

   .. automethod:: Depot.use_comparative_installation_view

   .. automethod:: Depot.use_plenary_installation_view

   .. automethod:: Depot.use_normalized_version_view

   .. automethod:: Depot.use_denormalized_version_view

   .. automethod:: Depot.get_installation

   .. automethod:: Depot.get_installations_by_ids

   .. automethod:: Depot.get_installations_by_genus_type

   .. automethod:: Depot.get_installations_by_parent_genus_type

   .. automethod:: Depot.get_installations_by_record_type

   .. automethod:: Depot.get_installations_by_package

   .. autoattribute:: Depot.installations



Installation Query Methods
--------------------------

   .. autoattribute:: Depot.site_id

   .. autoattribute:: Depot.site

   .. automethod:: Depot.can_search_installations

   .. automethod:: Depot.use_normalized_version_view

   .. automethod:: Depot.use_denormalized_version_view

   .. automethod:: Depot.use_normalized_dependency_view

   .. automethod:: Depot.use_denormalized_dependency_view

   .. autoattribute:: Depot.installation_query

   .. automethod:: Depot.get_installations_by_query



Installation Search Methods
---------------------------

   .. autoattribute:: Depot.installation_search

   .. autoattribute:: Depot.installation_search_order

   .. automethod:: Depot.get_installations_by_search

   .. automethod:: Depot.get_installations_query_from_inspector



Installation Management Methods
-------------------------------

   .. autoattribute:: Depot.site_id

   .. autoattribute:: Depot.site

   .. automethod:: Depot.can_manage_installations

   .. automethod:: Depot.install_package

   .. automethod:: Depot.remove_installation

   .. automethod:: Depot.remove_installations



Installation Update Methods
---------------------------

   .. autoattribute:: Depot.site_id

   .. autoattribute:: Depot.site

   .. automethod:: Depot.can_get_installation_updates

   .. automethod:: Depot.is_installation_current

   .. autoattribute:: Depot.installations_to_update

   .. autoattribute:: Depot.current_packages

   .. automethod:: Depot.get_current_packages_for_installation

   .. automethod:: Depot.is_installation_obsolete

   .. autoattribute:: Depot.obsolete_installations

   .. automethod:: Depot.update_installation

   .. automethod:: Depot.synchronize_installations



Installation Notification Methods
---------------------------------

   .. autoattribute:: Depot.site_id

   .. autoattribute:: Depot.site

   .. automethod:: Depot.can_register_for_installation_notifications

   .. automethod:: Depot.register_for_new_installations

   .. automethod:: Depot.register_for_deleted_installations

   .. automethod:: Depot.register_for_deleted_installation



Site Lookup Methods
-------------------

   .. automethod:: Depot.can_lookup_sites

   .. automethod:: Depot.use_comparative_site_view

   .. automethod:: Depot.use_plenary_site_view

   .. automethod:: Depot.get_site

   .. autoattribute:: Depot.sites



Package Lookup Methods
----------------------

   .. autoattribute:: Depot.depot_id

   .. autoattribute:: Depot.depot

   .. automethod:: Depot.can_lookup_packages

   .. automethod:: Depot.use_comparative_package_view

   .. automethod:: Depot.use_plenary_package_view

   .. automethod:: Depot.use_federated_depot_view

   .. automethod:: Depot.use_isolated_depot_view

   .. automethod:: Depot.use_normalized_version_view

   .. automethod:: Depot.use_denormalized_version_view

   .. automethod:: Depot.get_package

   .. automethod:: Depot.get_packages_by_ids

   .. automethod:: Depot.get_packages_by_genus_type

   .. automethod:: Depot.get_packages_by_parent_genus_type

   .. automethod:: Depot.get_packages_by_record_type

   .. automethod:: Depot.get_packages_by_provider

   .. automethod:: Depot.get_dependent_packages

   .. automethod:: Depot.get_package_versions

   .. autoattribute:: Depot.packages



Package Query Methods
---------------------

   .. autoattribute:: Depot.depot_id

   .. autoattribute:: Depot.depot

   .. automethod:: Depot.can_search_packages

   .. automethod:: Depot.use_federated_depot_view

   .. automethod:: Depot.use_isolated_depot_view

   .. automethod:: Depot.use_normalized_version_view

   .. automethod:: Depot.use_denormalized_version_view

   .. automethod:: Depot.use_normalized_dependency_view

   .. automethod:: Depot.use_denormalized_dependency_view

   .. autoattribute:: Depot.package_query

   .. automethod:: Depot.get_packages_by_query



Package Search Methods
----------------------

   .. autoattribute:: Depot.package_search

   .. autoattribute:: Depot.package_search_order

   .. automethod:: Depot.get_packages_by_search

   .. automethod:: Depot.get_package_query_from_inspector



Package Admin Methods
---------------------

   .. autoattribute:: Depot.depot_id

   .. autoattribute:: Depot.depot

   .. automethod:: Depot.can_create_packages

   .. automethod:: Depot.can_create_package_with_record_types

   .. automethod:: Depot.get_package_form_for_create

   .. automethod:: Depot.create_package

   .. automethod:: Depot.can_update_packages

   .. automethod:: Depot.can_update_package

   .. automethod:: Depot.get_package_form_for_update

   .. automethod:: Depot.update_package

   .. automethod:: Depot.can_delete_packages

   .. automethod:: Depot.can_delete_package

   .. automethod:: Depot.delete_package

   .. automethod:: Depot.can_manage_package_aliases

   .. automethod:: Depot.alias_package

   .. automethod:: Depot.can_create_installation_content

   .. automethod:: Depot.can_create_installation_content_with_record_types

   .. automethod:: Depot.get_installation_content_form_for_create

   .. automethod:: Depot.create_installation_content

   .. automethod:: Depot.can_update_installation_contents

   .. automethod:: Depot.get_installation_content_form_for_update

   .. automethod:: Depot.update_installation_content

   .. automethod:: Depot.can_delete_installation_contents

   .. automethod:: Depot.delete_installation_content

   .. automethod:: Depot.can_manage_package_versions

   .. automethod:: Depot.add_package_version

   .. automethod:: Depot.remove_package_version



Package Notification Methods
----------------------------

   .. autoattribute:: Depot.depot_id

   .. autoattribute:: Depot.depot

   .. automethod:: Depot.can_register_for_package_notifications

   .. automethod:: Depot.use_federated_depot_view

   .. automethod:: Depot.use_isolated_depot_view

   .. automethod:: Depot.register_for_new_packages

   .. automethod:: Depot.register_for_changed_packages

   .. automethod:: Depot.register_for_changed_package

   .. automethod:: Depot.register_for_deleted_packages

   .. automethod:: Depot.register_for_deleted_package



Package Depot Methods
---------------------

   .. automethod:: Depot.can_lookup_package_depot_mappings

   .. automethod:: Depot.use_comparative_depot_view

   .. automethod:: Depot.use_plenary_depot_view

   .. automethod:: Depot.use_normalized_version_view

   .. automethod:: Depot.use_denormalized_version_view

   .. automethod:: Depot.use_normalized_dependency_view

   .. automethod:: Depot.use_denormalized_dependency_view

   .. automethod:: Depot.get_package_ids_by_depot

   .. automethod:: Depot.get_packages_by_depot

   .. automethod:: Depot.get_package_ids_by_depots

   .. automethod:: Depot.get_packages_by_depots

   .. automethod:: Depot.get_depot_ids_by_package

   .. automethod:: Depot.get_depots_by_package



Package Depot Assignment Methods
--------------------------------

   .. automethod:: Depot.can_assign_packages

   .. automethod:: Depot.can_assign_packages_to_depot

   .. automethod:: Depot.get_assignable_depot_ids

   .. automethod:: Depot.get_assignable_depot_ids_for_package

   .. automethod:: Depot.assign_package_to_depot

   .. automethod:: Depot.unassign_package_from_depot



Package Smart Depot Methods
---------------------------

   .. autoattribute:: Depot.depot_id

   .. autoattribute:: Depot.depot

   .. automethod:: Depot.can_manage_smart_depot

   .. autoattribute:: Depot.package_query

   .. autoattribute:: Depot.package_search_order

   .. automethod:: Depot.apply_package_query

   .. automethod:: Depot.inspect_package_query

   .. automethod:: Depot.apply_package_sequencing

   .. automethod:: Depot.get_package_query_from_inspector



