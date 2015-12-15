

Service Managers
================


Type Manager
------------

.. py:class:: TypeManager(osid_managers.OsidManager, TypeProfile, type_managers.TypeManager)
    This manager provides access to the available sessions of the type service.


    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.





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
    This manager provides access to the available sessions of the type service.


    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of passing information from a server environment.
    The ``TypeLookupSession`` is used for looking up ``Types`` and the
    ``TypeAdminSession`` is used for managing and registering new Types.





    .. py:method:: get_type_lookup_session(proxy):
        :noindex:


    .. py:method:: get_type_admin_session(proxy):
        :noindex:




