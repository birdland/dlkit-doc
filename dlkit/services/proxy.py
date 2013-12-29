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
from . import osid
from .osid_errors import Unimplemented, IllegalState, OperationFailed


class ProxyProfile(osid.OsidProfile):

    def supports_proxy(self):
        """Tests if a proxy session is supported.

        :return: ``true`` if proxy is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_proxy_record_types(self):
        """Gets the supported ``Proxy`` record interface types.

        :return: a list containing the supported ``Proxy`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    proxy_record_types = property(fget=get_proxy_record_types)

    def supports_proxy_record_type(self, proxy_record_type):
        """Tests if the given ``Proxy`` record interface type is supported.

        :param proxy_record_type: a ``Type`` indicating a ``Proxy`` record type
        :type proxy_record_type: ``osid.type.Type``
        :return: ``true`` if the given type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proxy_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_proxy_condition_record_types(self):
        """Gets the supported ``ProxyCondition`` record interface types.

        :return: a list containing the supported ``ProxyCondition`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    proxy_condition_record_types = property(fget=get_proxy_condition_record_types)

    def supports_proxy_condition_record_type(self, proxy_condition_record_type):
        """Tests if the given ``ProxyCondition`` record interface type is supported.

        :param proxy_condition_record_type: a ``Type`` indicating a ``ProxyCondition`` record type
        :type proxy_condition_record_type: ``osid.type.Type``
        :return: ``true`` if the given type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``proxy_condition_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class ProxyManager(osid.OsidManager, osid.OsidSession, ProxyProfile):

    def get_proxy_session(self):
        """Gets a ``ProxySession`` which is responsible for acquiring authentication credentials on behalf of a service client.

        :return: a proxy session for this service
        :rtype: ``osid.proxy.ProxySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_proxy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    proxy_session = property(fget=get_proxy_session)



class ProxyProxyManager(osid.OsidProxyManager, ProxyProfile):

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
        raise UNIMPLEMENTED()



