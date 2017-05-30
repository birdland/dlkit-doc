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

    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.

        :return: a list containing the supported ``ProxyCondition`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)


class ProxyManager(osid_managers.OsidManager, osid_sessions.OsidSession, ProxyProfile):
    """The proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``ProxySession:`` a session to acquire proxy interfaces

    """


    def __init__(self):
        import settings
        import importlib
        provider_module = importlib.import_module(settings.PROXY_PROVIDER_MANAGER_PATH, settings.ANCHOR_PATH)
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
                raise  # Unimplemented???
            else:
                self._provider_sessions[session] = get_session()
            return self._provider_sessions[session]




class ProxyProxyManager(osid_managers.OsidProxyManager, ProxyProfile):
    """The proxy proxy manager provides access to proxy sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:

      * ``ProxySession:`` a session to acquire proxies

    """
    pass



