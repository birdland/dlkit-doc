
.. currentmodule:: dlkit.services.osid
.. automodule:: dlkit.services.osid

Service Managers
================


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



