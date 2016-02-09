# -*- coding: utf-8 -*-
"""Proxy Open Service Interface Definitions
proxy version 3.0.0

The Proxy OSID helps a consumer map external data, such as that received
    via a server request, into a Proxy that can be used with OSID proxy
    managers. Then purpose of this OSID is to modularize assumptions made
    about the input data into another OSID Provider, such as the
    authentication or localization information.


The ``Proxy`` represents the ``OsidResult`` of an evaluation of the
    input ``OsidCondition`` performed by the Proxy OSID Provider. The
    resulting Proxy is meant to be passed to ``OsidProxyManagers``. The
    Proxy OSID is the glue between the application server environment and
    the OSID services.


The input data may be anything acceptable to a ``ProxyCondition`` record
    Type. The ``ProxyCondition`` record ``Types`` are aligned with the
    application server environment while the ``Proxy`` record ``Types`` are
    aligned with OSID Providers. This alignment poses various
    interoperability issues and as such it might be helpful to be very broad
    in what may be specified in a ``ProxyCondition`` so that this service
    may produce the variety of ``Proxy`` records needed by the services in
    the OSID environment.


Some data is defined in the ``ProxyCondition``. This in no way implies
    support of this input by an OSID Provider. The resulting ``OsidSession``
    indicates what actually happened.


Example


An example using a specifier record for an http request:
  ProxyCondition condition = proxySession.getProxyCondition();
  HttpRequestRecord record = condition.getProxyConditionRecord(httpRequestRecordType);
  record.setHttpRequest(servletRequest);


  Proxy proxy = proxySession.getProxy(condition);



"""

from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import rules as osid_rules
from ..osid import records as osid_records


class ProxyProfile(osid_managers.OsidProfile):
    """The ``ProxyProfile`` describes the interoperability among proxy services."""


    def __init__(self):
        self._provider_manager = None


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

    def supports_proxy_record_type(self, proxy_record_type):
        """Tests if the given ``Proxy`` record interface type is supported.


        :param proxy_record_type: a ``Type`` indicating a ``Proxy`` record type
        :type proxy_record_type: ``osid.type.Type``
        :return: ``true`` if the given type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proxy_record_type`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.


        :return: a list containing the supported ``ProxyCondition`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)

    def supports_proxy_condition_record_type(self, proxy_condition_record_type):
        """Tests if the given ``ProxyCondition`` record interface type is supported.


        :param proxy_condition_record_type: a ``Type`` indicating a ``ProxyCondition`` record type
        :type proxy_condition_record_type: ``osid.type.Type``
        :return: ``true`` if the given type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proxy_condition_record_type`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean
##
# The following methods are from osid.proxy.ProxySession

    def get_proxy_condition(self):
        """Gets a proxy condition for acquiring a proxy.


        A new proxy condition should be acquired for each proxy request.


        :return: a proxy condiiton
        :rtype: ``osid.proxy.ProxyCondition``




        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.proxy.ProxyCondition

    proxy_condition = property(fget=get_proxy_condition)

    def get_proxy(self, input_):
        """Gets a proxy.


        :param input: a proxy condition
        :type input: ``osid.proxy.ProxyCondition``
        :return: a proxy
        :rtype: ``osid.proxy.Proxy``
        :raise: ``NullArgument`` -- ``input`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``input`` is not of this service


        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.proxy.Proxy




class ProxyManager(osid_managers.OsidManager, osid_sessions.OsidSession, ProxyProfile):
    """The proxy manager provides access to proxy sessions and provides interoperability tests for
        various
    aspects of this service.


    The sessions included in this manager are:




      * ``ProxySession:`` a session to acquire proxy interfaces


    """




    def __init__(self):
        import settings
        import importlib
        provider_module = importlib.import_module(settings.PROXY_PROVIDER_MANAGER_PATH,
            settings.ANCHOR_PATH)
        provider_manager_class = getattr(provider_module, 'ProxyManager')
        self._provider_manager = provider_manager_class()
        self._provider_sessions = dict()


    def _get_provider_session(self, session):
        if session in self._provider_sessions:
            return self._provider_sessions[session]
        else:
            try:
                get_session = getattr(self._provider_manager, 'get_' + session)
            except:
                raise # Unimplemented???
            else:
                self._provider_sessions[session] = get_session()
            return self._provider_sessions[session]


    def get_proxy_session(self):
        """Gets a ``ProxySession`` which is responsible for acquiring authentication credentials on
            behalf of a service client.


        :return: a proxy session for this service
        :rtype: ``osid.proxy.ProxySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proxy()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_proxy()`` is ``true``.*


        """
        return # osid.proxy.ProxySession

    proxy_session = property(fget=get_proxy_session)
##
# The following methods are from osid.proxy.ProxySession

    def get_proxy_condition(self):
        """Gets a proxy condition for acquiring a proxy.


        A new proxy condition should be acquired for each proxy request.


        :return: a proxy condiiton
        :rtype: ``osid.proxy.ProxyCondition``




        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.proxy.ProxyCondition

    proxy_condition = property(fget=get_proxy_condition)

    def get_proxy(self, input_):
        """Gets a proxy.


        :param input: a proxy condition
        :type input: ``osid.proxy.ProxyCondition``
        :return: a proxy
        :rtype: ``osid.proxy.Proxy``
        :raise: ``NullArgument`` -- ``input`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``input`` is not of this service


        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.proxy.Proxy




class ProxyProxyManager(osid_managers.OsidProxyManager, ProxyProfile):
    """The proxy proxy manager provides access to proxy sessions and provides interoperability tests
        for
    various aspects of this service.


    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:




      * ``ProxySession:`` a session to acquire proxies


    """

    def get_proxy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``ProxySession`` using the supplied
            ``Proxy``.


        :param proxy: proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ProxySession``
        :rtype: ``osid.proxy.ProxySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proxy()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_proxy()`` is ``true``.*


        """
        return # osid.proxy.ProxySession
##
# The following methods are from osid.proxy.ProxySession

    def get_proxy_condition(self):
        """Gets a proxy condition for acquiring a proxy.


        A new proxy condition should be acquired for each proxy request.


        :return: a proxy condiiton
        :rtype: ``osid.proxy.ProxyCondition``




        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.proxy.ProxyCondition

    proxy_condition = property(fget=get_proxy_condition)

    def get_proxy(self, input_):
        """Gets a proxy.


        :param input: a proxy condition
        :type input: ``osid.proxy.ProxyCondition``
        :return: a proxy
        :rtype: ``osid.proxy.Proxy``
        :raise: ``NullArgument`` -- ``input`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``input`` is not of this service


        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.proxy.Proxy




