"""Mongodb implementations of proxy managers."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package mongo package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from . import profile
from . import sessions
from .. import utilities
from ..primitives import Type
from ..type.objects import TypeList
from dlkit.abstract_osid.osid import errors
from dlkit.manager_impls.proxy import managers as proxy_managers
from dlkit.mongo.osid import managers as osid_managers




class ProxyProfile(osid_managers.OsidProfile, proxy_managers.ProxyProfile):
    """The ``ProxyProfile`` describes the interoperability among proxy services."""

    def supports_proxy(self):
        """Tests if a proxy session is supported.


        return: (boolean) - ``true`` if proxy is supported ``,``
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceProfile.supports_resource_lookup
        return 'supports_proxy' in profile.SUPPORTS

    def get_proxy_record_types(self):
        """Gets the supported ``Proxy`` record interface types.


        return: (osid.type.TypeList) - a list containing the supported
                ``Proxy`` record types
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = self._get_registry('PROXY_RECORD_TYPES')
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    proxy_record_types = property(fget=get_proxy_record_types)

    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.


        return: (osid.type.TypeList) - a list containing the supported
                ``ProxyCondition`` record types
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for
        # osid.resource.ResourceProfile.get_resource_record_types_template
        record_type_maps = self._get_registry('PROXY_CONDITION_RECORD_TYPES')
        record_types = []
        for record_type_map in record_type_maps:
            record_types.append(Type(**record_type_maps[record_type_map]))
        return TypeList(record_types)

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)


class ProxyManager(osid_managers.OsidManager, ProxyProfile, proxy_managers.ProxyManager):
    """The proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of
        this
    service.


    The sessions included in this manager are:




      * ``ProxySession:`` a session to acquire proxy interfaces


    """


    def __init__(self):
        osid_managers.OsidManager.__init__(self)
    def get_proxy_session(self):
        """Gets a ``ProxySession`` which is responsible for acquiring authentication credentials on behalf of a service
            client.


        return: (osid.proxy.ProxySession) - a proxy session for this
                service
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proxy()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proxy()`` is ``true``.*


        """
        if not self.supports_proxy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProxySession(runtime=self._runtime)

    proxy_session = property(fget=get_proxy_session)


class ProxyProxyManager(osid_managers.OsidProxyManager, ProxyProfile, proxy_managers.ProxyProxyManager):
    """The proxy proxy manager provides access to proxy sessions and provides interoperability tests for various aspects
        of
    this service.


    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:




      * ``ProxySession:`` a session to acquire proxies


    """


    def __init__(self):
        osid_managers.OsidProxyManager.__init__(self)
    @utilities.arguments_not_none
    def get_proxy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``ProxySession`` using the supplied ``Proxy``.


        arg:    proxy (osid.proxy.Proxy): proxy
        return: (osid.proxy.ProxySession) - a ``ProxySession``
        raise:  NullArgument - ``proxy`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unimplemented - ``supports_proxy()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_proxy()`` is ``true``.*


        """
        if not self.supports_proxy():
            raise errors.Unimplemented()
        # pylint: disable=no-member
        return sessions.ProxySession(proxy=proxy, runtime=self._runtime)


