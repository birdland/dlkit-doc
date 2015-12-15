

Managers
========


Proxy Profile
-------------

.. py:class:: ProxyProfile(osid_managers.OsidProfile, proxy_managers.ProxyProfile)
    The ``ProxyProfile`` describes the interoperability among proxy services.

    .. py:method:: supports_proxy():
        :noindex:


    .. py:method:: get_proxy_record_types():
        :noindex:


    .. py:attribute:: proxy_record_types
        :noindex:


    .. py:method:: supports_proxy_record_type(proxy_record_type):
        :noindex:


    .. py:method:: get_proxy_condition_record_types():
        :noindex:


    .. py:attribute:: proxy_condition_record_types
        :noindex:


    .. py:method:: supports_proxy_condition_record_type(proxy_condition_record_type):
        :noindex:


Proxy Manager
-------------

.. py:class:: ProxyManager(osid_managers.OsidManager, ProxyProfile, proxy_managers.ProxyManager)
        :noindex:

    .. py:method:: get_proxy_session():
        :noindex:


    .. py:attribute:: proxy_session
        :noindex:


Proxy Proxy Manager
-------------------

.. py:class:: ProxyProxyManager(osid_managers.OsidProxyManager, ProxyProfile, proxy_managers.ProxyProxyManager)
        :noindex:

    .. py:method:: get_proxy_session(proxy):
        :noindex:


