.. currentmodule:: dlkit.installation.query_inspectors
.. automodule:: dlkit.installation.query_inspectors

Query Inspectors
================


Package Query Inspector
-----------------------

.. autoclass:: PackageQueryInspector
   :show-inheritance:

   .. autoattribute:: PackageQueryInspector.version_terms

   .. autoattribute:: PackageQueryInspector.version_since_terms

   .. autoattribute:: PackageQueryInspector.copyright_terms

   .. autoattribute:: PackageQueryInspector.requires_license_acknowledgement_terms

   .. autoattribute:: PackageQueryInspector.creator_id_terms

   .. autoattribute:: PackageQueryInspector.creator_terms

   .. autoattribute:: PackageQueryInspector.release_date_terms

   .. autoattribute:: PackageQueryInspector.dependency_id_terms

   .. autoattribute:: PackageQueryInspector.dependency_terms

   .. autoattribute:: PackageQueryInspector.url_terms

   .. autoattribute:: PackageQueryInspector.installation_id_terms

   .. autoattribute:: PackageQueryInspector.installation_terms

   .. autoattribute:: PackageQueryInspector.dependent_id_terms

   .. autoattribute:: PackageQueryInspector.dependent_terms

   .. autoattribute:: PackageQueryInspector.versioned_package_id_terms

   .. autoattribute:: PackageQueryInspector.versioned_package_terms

   .. autoattribute:: PackageQueryInspector.installation_content_id_terms

   .. autoattribute:: PackageQueryInspector.installation_content_terms

   .. autoattribute:: PackageQueryInspector.depot_id_terms

   .. autoattribute:: PackageQueryInspector.depot_terms

   .. automethod:: PackageQueryInspector.get_package_query_inspector_record



Installation Content Query Inspector
------------------------------------

.. autoclass:: InstallationContentQueryInspector
   :show-inheritance:

   .. autoattribute:: InstallationContentQueryInspector.data_length_terms

   .. autoattribute:: InstallationContentQueryInspector.data_terms

   .. automethod:: InstallationContentQueryInspector.get_installation_content_query_inspector_record



Depot Query Inspector
---------------------

.. autoclass:: DepotQueryInspector
   :show-inheritance:

   .. autoattribute:: DepotQueryInspector.package_id_terms

   .. autoattribute:: DepotQueryInspector.package_terms

   .. autoattribute:: DepotQueryInspector.ancestor_depot_id_terms

   .. autoattribute:: DepotQueryInspector.ancestor_depot_terms

   .. autoattribute:: DepotQueryInspector.descendant_depot_id_terms

   .. autoattribute:: DepotQueryInspector.descendant_depot_terms

   .. automethod:: DepotQueryInspector.get_depot_query_inspector_record



Installation Query Inspector
----------------------------

.. autoclass:: InstallationQueryInspector
   :show-inheritance:

   .. autoattribute:: InstallationQueryInspector.site_id_terms

   .. autoattribute:: InstallationQueryInspector.site_terms

   .. autoattribute:: InstallationQueryInspector.package_id_terms

   .. autoattribute:: InstallationQueryInspector.package_terms

   .. autoattribute:: InstallationQueryInspector.install_date_terms

   .. autoattribute:: InstallationQueryInspector.agent_id_terms

   .. autoattribute:: InstallationQueryInspector.agent_terms

   .. autoattribute:: InstallationQueryInspector.last_check_date_terms

   .. automethod:: InstallationQueryInspector.get_installation_query_inspector_record



Site Query Inspector
--------------------

.. autoclass:: SiteQueryInspector
   :show-inheritance:

   .. autoattribute:: SiteQueryInspector.installation_id_terms

   .. autoattribute:: SiteQueryInspector.installation_terms

   .. automethod:: SiteQueryInspector.get_site_query_inspector_record



