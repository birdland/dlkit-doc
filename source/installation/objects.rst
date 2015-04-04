.. currentmodule:: dlkit.installation.objects
.. automodule:: dlkit.installation.objects

Objects
=======


Package
-------

.. autoclass:: Package
   :show-inheritance:

   .. autoattribute:: Package.version

   .. autoattribute:: Package.copyright

   .. automethod:: Package.requests_license_acknowledgement

   .. autoattribute:: Package.creator_id

   .. autoattribute:: Package.creator

   .. autoattribute:: Package.release_date

   .. autoattribute:: Package.dependency_ids

   .. autoattribute:: Package.dependencies

   .. autoattribute:: Package.url

   .. autoattribute:: Package.installation_content_ids

   .. autoattribute:: Package.installation_contents

   .. automethod:: Package.get_package_record



Package Form
------------

.. autoclass:: PackageForm
   :show-inheritance:

   .. autoattribute:: PackageForm.version_metadata

   .. autoattribute:: PackageForm.version

   .. autoattribute:: PackageForm.copyright_metadata

   .. autoattribute:: PackageForm.copyright

   .. autoattribute:: PackageForm.requires_license_acknowledgement_metadata

   .. autoattribute:: PackageForm.requires_license_acknowledgement

   .. autoattribute:: PackageForm.creator_metadata

   .. autoattribute:: PackageForm.creator

   .. autoattribute:: PackageForm.release_date_metadata

   .. autoattribute:: PackageForm.release_date

   .. autoattribute:: PackageForm.dependencies_metadata

   .. autoattribute:: PackageForm.dependencies

   .. autoattribute:: PackageForm.url_metadata

   .. autoattribute:: PackageForm.url

   .. automethod:: PackageForm.get_package_form_record



Package List
------------

.. autoclass:: PackageList
   :show-inheritance:

   .. autoattribute:: PackageList.next_package

   .. automethod:: PackageList.get_next_packages



Installation Content
--------------------

.. autoclass:: InstallationContent
   :show-inheritance:

   .. autoattribute:: InstallationContent.package_id

   .. autoattribute:: InstallationContent.package

   .. automethod:: InstallationContent.has_data_length

   .. autoattribute:: InstallationContent.data_length

   .. autoattribute:: InstallationContent.data

   .. automethod:: InstallationContent.get_installation_content_record



Installation Content Form
-------------------------

.. autoclass:: InstallationContentForm
   :show-inheritance:

   .. autoattribute:: InstallationContentForm.data_metadata

   .. autoattribute:: InstallationContentForm.data

   .. automethod:: InstallationContentForm.get_installation_content_form_record



Installation Content List
-------------------------

.. autoclass:: InstallationContentList
   :show-inheritance:

   .. autoattribute:: InstallationContentList.next_installation_content

   .. automethod:: InstallationContentList.get_next_installation_contents



Depot Form
----------

.. autoclass:: DepotForm
   :show-inheritance:

   .. automethod:: DepotForm.get_depot_form_record



Depot List
----------

.. autoclass:: DepotList
   :show-inheritance:

   .. autoattribute:: DepotList.next_depot

   .. automethod:: DepotList.get_next_depots



Depot Node
----------

.. autoclass:: DepotNode
   :show-inheritance:

   .. autoattribute:: DepotNode.depot

   .. autoattribute:: DepotNode.parent_depot_nodes

   .. autoattribute:: DepotNode.child_depot_nodes



Depot Node List
---------------

.. autoclass:: DepotNodeList
   :show-inheritance:

   .. autoattribute:: DepotNodeList.next_depot_node

   .. automethod:: DepotNodeList.get_next_depot_nodes



Installation
------------

.. autoclass:: Installation
   :show-inheritance:

   .. autoattribute:: Installation.site_id

   .. autoattribute:: Installation.site

   .. autoattribute:: Installation.package_id

   .. autoattribute:: Installation.package

   .. autoattribute:: Installation.depot_id

   .. autoattribute:: Installation.depot

   .. autoattribute:: Installation.install_date

   .. autoattribute:: Installation.agent_id

   .. autoattribute:: Installation.agent

   .. autoattribute:: Installation.last_check_date

   .. automethod:: Installation.get_installation_record



Installation List
-----------------

.. autoclass:: InstallationList
   :show-inheritance:

   .. autoattribute:: InstallationList.next_installation

   .. automethod:: InstallationList.get_next_installations



Site
----

.. autoclass:: Site
   :show-inheritance:

   .. autoattribute:: Site.path

   .. automethod:: Site.get_site_record



Site List
---------

.. autoclass:: SiteList
   :show-inheritance:

   .. autoattribute:: SiteList.next_site

   .. automethod:: SiteList.get_next_sites



