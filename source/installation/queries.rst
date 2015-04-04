.. currentmodule:: dlkit.installation.queries
.. automodule:: dlkit.installation.queries

Queries
=======


Package Query
-------------

.. autoclass:: PackageQuery
   :show-inheritance:

   .. automethod:: PackageQuery.match_version

   .. automethod:: PackageQuery.match_any_version

   .. autoattribute:: PackageQuery.version_terms

   .. automethod:: PackageQuery.match_version_since

   .. autoattribute:: PackageQuery.version_since_terms

   .. automethod:: PackageQuery.match_copyright

   .. automethod:: PackageQuery.match_any_copyright

   .. autoattribute:: PackageQuery.copyright_terms

   .. automethod:: PackageQuery.match_requires_license_acknowledgement

   .. automethod:: PackageQuery.match_any_requires_license_acknowledgement

   .. autoattribute:: PackageQuery.requires_license_acknowledgement_terms

   .. automethod:: PackageQuery.match_creator_id

   .. autoattribute:: PackageQuery.creator_id_terms

   .. automethod:: PackageQuery.supports_creator_query

   .. autoattribute:: PackageQuery.creator_query

   .. automethod:: PackageQuery.match_any_creator

   .. autoattribute:: PackageQuery.creator_terms

   .. automethod:: PackageQuery.match_release_date

   .. automethod:: PackageQuery.match_any_release_date

   .. autoattribute:: PackageQuery.release_date_terms

   .. automethod:: PackageQuery.match_dependency_id

   .. autoattribute:: PackageQuery.dependency_id_terms

   .. automethod:: PackageQuery.supports_dependency_query

   .. autoattribute:: PackageQuery.dependency_query

   .. automethod:: PackageQuery.match_any_dependency

   .. autoattribute:: PackageQuery.dependency_terms

   .. automethod:: PackageQuery.match_url

   .. automethod:: PackageQuery.match_any_url

   .. autoattribute:: PackageQuery.url_terms

   .. automethod:: PackageQuery.match_installation_id

   .. autoattribute:: PackageQuery.installation_id_terms

   .. automethod:: PackageQuery.supports_installation_query

   .. autoattribute:: PackageQuery.installation_query

   .. automethod:: PackageQuery.match_any_installation

   .. autoattribute:: PackageQuery.installation_terms

   .. automethod:: PackageQuery.match_dependent_id

   .. autoattribute:: PackageQuery.dependent_id_terms

   .. automethod:: PackageQuery.supports_dependent_query

   .. autoattribute:: PackageQuery.dependent_query

   .. automethod:: PackageQuery.match_any_dependent

   .. autoattribute:: PackageQuery.dependent_terms

   .. automethod:: PackageQuery.match_versioned_package_id

   .. autoattribute:: PackageQuery.versioned_package_id_terms

   .. automethod:: PackageQuery.supports_versioned_package_query

   .. autoattribute:: PackageQuery.versioned_package_query

   .. automethod:: PackageQuery.match_any_versioned_package

   .. autoattribute:: PackageQuery.versioned_package_terms

   .. automethod:: PackageQuery.match_installation_content_id

   .. autoattribute:: PackageQuery.installation_content_id_terms

   .. automethod:: PackageQuery.supports_installation_content_query

   .. autoattribute:: PackageQuery.installation_content_query

   .. automethod:: PackageQuery.match_any_installation_content

   .. autoattribute:: PackageQuery.installation_content_terms

   .. automethod:: PackageQuery.match_depot_id

   .. autoattribute:: PackageQuery.depot_id_terms

   .. automethod:: PackageQuery.supports_depot_query

   .. autoattribute:: PackageQuery.depot_query

   .. autoattribute:: PackageQuery.depot_terms

   .. automethod:: PackageQuery.get_package_query_record



Installation Content Query
--------------------------

.. autoclass:: InstallationContentQuery
   :show-inheritance:

   .. automethod:: InstallationContentQuery.match_data_length

   .. automethod:: InstallationContentQuery.match_any_data_length

   .. autoattribute:: InstallationContentQuery.data_length_terms

   .. automethod:: InstallationContentQuery.match_data

   .. automethod:: InstallationContentQuery.match_any_data

   .. autoattribute:: InstallationContentQuery.data_terms

   .. automethod:: InstallationContentQuery.get_installation_content_query_record



Depot Query
-----------

.. autoclass:: DepotQuery
   :show-inheritance:

   .. automethod:: DepotQuery.match_package_id

   .. autoattribute:: DepotQuery.package_id_terms

   .. automethod:: DepotQuery.supports_package_query

   .. autoattribute:: DepotQuery.package_query

   .. automethod:: DepotQuery.match_any_package

   .. autoattribute:: DepotQuery.package_terms

   .. automethod:: DepotQuery.match_ancestor_depot_id

   .. autoattribute:: DepotQuery.ancestor_depot_id_terms

   .. automethod:: DepotQuery.supports_ancestor_depot_query

   .. autoattribute:: DepotQuery.ancestor_depot_query

   .. automethod:: DepotQuery.match_any_ancestor_depot

   .. autoattribute:: DepotQuery.ancestor_depot_terms

   .. automethod:: DepotQuery.match_descendant_depot_id

   .. autoattribute:: DepotQuery.descendant_depot_id_terms

   .. automethod:: DepotQuery.supports_descendant_depot_query

   .. autoattribute:: DepotQuery.descendant_depot_query

   .. automethod:: DepotQuery.match_any_descendant_depot

   .. autoattribute:: DepotQuery.descendant_depot_terms

   .. automethod:: DepotQuery.get_depot_query_record



Installation Query
------------------

.. autoclass:: InstallationQuery
   :show-inheritance:

   .. automethod:: InstallationQuery.match_site_id

   .. autoattribute:: InstallationQuery.site_id_terms

   .. automethod:: InstallationQuery.supports_site_query

   .. autoattribute:: InstallationQuery.site_query

   .. autoattribute:: InstallationQuery.site_terms

   .. automethod:: InstallationQuery.match_package_id

   .. autoattribute:: InstallationQuery.package_id_terms

   .. automethod:: InstallationQuery.supports_package_query

   .. autoattribute:: InstallationQuery.package_query

   .. autoattribute:: InstallationQuery.package_terms

   .. automethod:: InstallationQuery.match_install_date

   .. autoattribute:: InstallationQuery.install_date_terms

   .. automethod:: InstallationQuery.match_agent_id

   .. autoattribute:: InstallationQuery.agent_id_terms

   .. automethod:: InstallationQuery.supports_agent_query

   .. autoattribute:: InstallationQuery.agent_query

   .. autoattribute:: InstallationQuery.agent_terms

   .. automethod:: InstallationQuery.match_last_check_date

   .. autoattribute:: InstallationQuery.last_check_date_terms

   .. automethod:: InstallationQuery.get_installation_query_record



Site Query
----------

.. autoclass:: SiteQuery
   :show-inheritance:

   .. automethod:: SiteQuery.match_installation_id

   .. autoattribute:: SiteQuery.installation_id_terms

   .. automethod:: SiteQuery.supports_installation_query

   .. autoattribute:: SiteQuery.installation_query

   .. automethod:: SiteQuery.match_any_installation

   .. autoattribute:: SiteQuery.installation_terms

   .. automethod:: SiteQuery.get_site_query_record



