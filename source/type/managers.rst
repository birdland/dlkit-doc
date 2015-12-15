

Managers
========


Type Profile
------------

.. py:class:: TypeProfile(osid_managers.OsidProfile, type_managers.TypeProfile)
    The ``TypeProfile`` describes the interoperability among type services.

    .. py:method:: supports_type_lookup():
        :noindex:


    .. py:method:: supports_type_admin():
        :noindex:


Type Manager
------------

.. py:class:: TypeManager(osid_managers.OsidManager, TypeProfile, type_managers.TypeManager)
        :noindex:

    .. py:method:: get_type_lookup_session():
        :noindex:


    .. py:attribute:: type_lookup_session
        :noindex:


    .. py:method:: get_type_admin_session():
        :noindex:


    .. py:attribute:: type_admin_session
        :noindex:


Type Proxy Manager
------------------

.. py:class:: TypeProxyManager(osid_managers.OsidProxyManager, TypeProfile, type_managers.TypeProxyManager)
        :noindex:

    .. py:method:: get_type_lookup_session(proxy):
        :noindex:


    .. py:method:: get_type_admin_session(proxy):
        :noindex:


