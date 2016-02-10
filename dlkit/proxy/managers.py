
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class ProxyProfile(osid_managers.OsidProfile):
    """The ``ProxyProfile`` describes the interoperability among proxy services."""

    def supports_proxy(self):
        """Tests if a proxy session is supported.

        :return: ``true`` if proxy is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_proxy_record_types(self):
        """Gets the supported ``Proxy`` record interface types.

        :return: a list containing the supported ``Proxy`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    proxy_record_types = property(fget=get_proxy_record_types)

    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.

        :return: a list containing the supported ``ProxyCondition`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)


class ProxyManager(osid_managers.OsidManager, osid_sessions.OsidSession, ProxyProfile):
    """The proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this
    service.

    The sessions included in this manager are:


      * ``ProxySession:`` a session to acquire proxy interfaces

    """




class ProxyProxyManager(osid_managers.OsidProxyManager, ProxyProfile):
    """The proxy proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of
    this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:


      * ``ProxySession:`` a session to acquire proxies

    """




