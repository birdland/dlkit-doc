from ..osid import managers as osid_managers


class ProxyProfile(osid_managers.OsidProfile):
    """The ``ProxyProfile`` describes the interoperability among proxy services."""
    def supports_proxy(self):
        """Tests if a proxy session is supported.

        :return: ``true`` if proxy is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_proxy_record_types(self):
        """Gets the supported ``Proxy`` record interface types.

        :return: a list containing the supported ``Proxy`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    proxy_record_types = property(fget=get_proxy_record_types)

    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.

        :return: a list containing the supported ``ProxyCondition`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)


class ProxyManager(osid_managers.OsidManager, ProxyProfile):
    """The proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``ProxySession:`` a session to acquire proxy interfaces


    """
    def get_proxy_session(self):
        """Gets a ``ProxySession`` which is responsible for acquiring authentication credentials on behalf of a service client.

        :return: a proxy session for this service
        :rtype: ``osid.proxy.ProxySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proxy()`` is ``false``

        """
        return # osid.proxy.ProxySession

    proxy_session = property(fget=get_proxy_session)


class ProxyProxyManager(osid_managers.OsidProxyManager, ProxyProfile):
    """The proxy proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:

      * ``ProxySession:`` a session to acquire proxies


    """
    def get_proxy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``ProxySession`` using the supplied ``Proxy``.

        :param proxy: proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProxySession``
        :rtype: ``osid.proxy.ProxySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proxy()`` is ``false``

        """
        return # osid.proxy.ProxySession


