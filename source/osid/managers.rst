
.. currentmodule:: dlkit.osid.managers
.. automodule:: dlkit.osid.managers

Managers
========


Osid Profile
------------

.. autoclass:: OsidProfile
   :show-inheritance:

   .. autoattribute:: OsidProfile.ident

   .. autoattribute:: OsidProfile.display_name

   .. autoattribute:: OsidProfile.description

   .. autoattribute:: OsidProfile.version

   .. autoattribute:: OsidProfile.release_date

   .. automethod:: OsidProfile.supports_osid_version

   .. autoattribute:: OsidProfile.locales

   .. automethod:: OsidProfile.supports_journal_rollback

   .. automethod:: OsidProfile.supports_journal_branching

   .. autoattribute:: OsidProfile.branch_id

   .. autoattribute:: OsidProfile.branch

   .. autoattribute:: OsidProfile.proxy_record_types

   .. automethod:: OsidProfile.supports_proxy_record_type

Osid Manager
------------

.. autoclass:: OsidManager
   :show-inheritance:

   .. automethod:: OsidManager.initialize

   .. automethod:: OsidManager.rollback_service

   .. automethod:: OsidManager.change_branch

Osid Proxy Manager
------------------

.. autoclass:: OsidProxyManager
   :show-inheritance:

   .. automethod:: OsidProxyManager.initialize

   .. automethod:: OsidProxyManager.rollback_service

   .. automethod:: OsidProxyManager.change_branch

Osid Runtime Profile
--------------------

.. autoclass:: OsidRuntimeProfile
   :show-inheritance:

   .. automethod:: OsidRuntimeProfile.supports_configuration

Osid Runtime Manager
--------------------

.. autoclass:: OsidRuntimeManager
   :show-inheritance:

   .. automethod:: OsidRuntimeManager.get_manager

   .. automethod:: OsidRuntimeManager.get_proxy_manager

   .. autoattribute:: OsidRuntimeManager.configuration

