
.. currentmodule:: dlkit.proxy.managers
.. automodule:: dlkit.proxy.managers

Managers
========


Proxy Profile
-------------

.. autoclass:: ProxyProfile
   :show-inheritance:

   .. automethod:: ProxyProfile.supports_proxy

   .. autoattribute:: ProxyProfile.proxy_record_types

   .. automethod:: ProxyProfile.supports_proxy_record_type

   .. autoattribute:: ProxyProfile.proxy_condition_record_types

   .. automethod:: ProxyProfile.supports_proxy_condition_record_type

Proxy Manager
-------------

.. autoclass:: ProxyManager
   :show-inheritance:

   .. autoattribute:: ProxyManager.proxy_session

Proxy Proxy Manager
-------------------

.. autoclass:: ProxyProxyManager
   :show-inheritance:

   .. automethod:: ProxyProxyManager.get_proxy_session

