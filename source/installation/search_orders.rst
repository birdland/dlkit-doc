.. currentmodule:: dlkit.installation.search_orders
.. automodule:: dlkit.installation.search_orders

Search_Orders
=============


Package Search Order
--------------------

.. autoclass:: PackageSearchOrder
   :show-inheritance:

   .. automethod:: PackageSearchOrder.order_by_version

   .. automethod:: PackageSearchOrder.order_by_copyright

   .. automethod:: PackageSearchOrder.order_by_requires_license_acknowledgement

   .. automethod:: PackageSearchOrder.order_by_creator

   .. automethod:: PackageSearchOrder.supports_creator_search_order

   .. autoattribute:: PackageSearchOrder.creator_search_order

   .. automethod:: PackageSearchOrder.order_by_release_date

   .. automethod:: PackageSearchOrder.order_by_url

   .. automethod:: PackageSearchOrder.get_package_search_order_record



Depot Search Order
------------------

.. autoclass:: DepotSearchOrder
   :show-inheritance:

   .. automethod:: DepotSearchOrder.get_depot_search_order_record



Installation Search Order
-------------------------

.. autoclass:: InstallationSearchOrder
   :show-inheritance:

   .. automethod:: InstallationSearchOrder.order_by_site

   .. automethod:: InstallationSearchOrder.supports_site_search_order

   .. autoattribute:: InstallationSearchOrder.site_search_order

   .. automethod:: InstallationSearchOrder.order_by_package

   .. automethod:: InstallationSearchOrder.supports_package_search_order

   .. autoattribute:: InstallationSearchOrder.package_search_order

   .. automethod:: InstallationSearchOrder.order_by_install_date

   .. automethod:: InstallationSearchOrder.order_by_agent

   .. automethod:: InstallationSearchOrder.supports_agent_search_order

   .. autoattribute:: InstallationSearchOrder.agent_search_order

   .. automethod:: InstallationSearchOrder.order_by_last_check_date

   .. automethod:: InstallationSearchOrder.get_installation_search_order_record



Site Search Order
-----------------

.. autoclass:: SiteSearchOrder
   :show-inheritance:

   .. automethod:: SiteSearchOrder.get_site_search_order_record



