
.. currentmodule:: dlkit.type.managers
.. automodule:: dlkit.type.managers

Managers
========


Type Profile
------------

.. autoclass:: TypeProfile
   :show-inheritance:

   .. automethod:: TypeProfile.supports_type_lookup

   .. automethod:: TypeProfile.supports_type_admin

Type Manager
------------

.. autoclass:: TypeManager
   :show-inheritance:

   .. autoattribute:: TypeManager.type_lookup_session

   .. autoattribute:: TypeManager.type_admin_session

Type Proxy Manager
------------------

.. autoclass:: TypeProxyManager
   :show-inheritance:

   .. automethod:: TypeProxyManager.get_type_lookup_session

   .. automethod:: TypeProxyManager.get_type_admin_session

