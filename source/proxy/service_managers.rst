

Service Managers
================


Proxy Manager
-------------

.. py:class:: ProxyManager(osid_managers.OsidManager, ProxyProfile, proxy_managers.ProxyManager)
    The proxy manager provides access to proxy sessions and provides interoperability tests for
        various
    aspects of this service.


    The sessions included in this manager are:




      * ``ProxySession:`` a session to acquire proxy interfaces





    .. py:method:: get_proxy_session():
        :noindex:


    .. py:attribute:: proxy_session
        :noindex:




Proxy Methods
-------------

    .. py:method:: get_proxy_condition():
        Gets a proxy condition for acquiring a proxy.

        A new proxy condition should be acquired for each proxy request.

        :return: (osid.proxy.ProxyCondition) - a proxy condiiton
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: proxy_condition


    .. py:method:: get_proxy(input_):
        Gets a proxy.

        :arg:    input (osid.proxy.ProxyCondition): a proxy condition
        :return: (osid.proxy.Proxy) - a proxy
        :raises:  NullArgument - ``input`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``input`` is not of this service
        *compliance: mandatory -- This method is must be implemented.*






Proxy Proxy Manager
-------------------

.. py:class:: ProxyProxyManager(osid_managers.OsidProxyManager, ProxyProfile, proxy_managers.ProxyProxyManager)
    The proxy proxy manager provides access to proxy sessions and provides interoperability tests
        for
    various aspects of this service.


    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:




      * ``ProxySession:`` a session to acquire proxies





    .. py:method:: get_proxy_session(proxy):
        :noindex:




Proxy Methods
-------------

    .. py:method:: get_proxy_condition():
        Gets a proxy condition for acquiring a proxy.

        A new proxy condition should be acquired for each proxy request.

        :return: (osid.proxy.ProxyCondition) - a proxy condiiton
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: proxy_condition


    .. py:method:: get_proxy(input_):
        Gets a proxy.

        :arg:    input (osid.proxy.ProxyCondition): a proxy condition
        :return: (osid.proxy.Proxy) - a proxy
        :raises:  NullArgument - ``input`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``input`` is not of this service
        *compliance: mandatory -- This method is must be implemented.*






