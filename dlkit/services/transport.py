# -*- coding: utf-8 -*-
"""Transport Open Service Interface Definitions
transport version 3.0.0

The transport OSID provides a means of moving data to or from the local
endpoint.

Service Endpoints

The transport OSID defines an inbound and an outbound service. An
outbound transport service is used from a local endpoint to a single
remote endpoint. The remote endpoint may represent one or more physical
endpoints, such as a multicast network, but presents itself as a single
enpoint to the consumer. The inbound service is used to receive and
process data from multiple remote endpoints and is implemented using a
callback mechanism when a new request for association arrives.

An association or connection between two endpoints is represented by the
session itself. The Transport OSID defines two flavors of transport. One
is stream oriented that makes use of ``DataInputStream`` and
``DataOutputStream`` for reading and writing data. The other is message
oriented that makes use of ``Request`` and ``Response`` for structuring
data.

Stream-oriented Service

In the stream-oriented case, the transport OSID does not describe the
format or sequence of the data which must be agreed upon at both ends.
The OSID simply acts as a cover for specific transport or session
related APIs, and provides a means for modular handling of service
location for the purpose implementing a redundancy or load balancing
scheme. The transport OSID may be used within another OSID to handle the
transport of serialized data that can be transformed to a higher level
OSID object.

The data streams defined in the transport OSID are also used in other
OSIDs where a data stream is required such as the filing OSID or an
Asset that contains arbitrary serialized data.

Message-oriented Service

The message oriented services provide additional structure that can be
used to specify fields, organize streams, or provide data to object
conversions. ``Requests`` may be sent synchronously so that each request
waits for a ``Response,`` or asynchronously where each response is sent
to a registered callback. A message ``Type`` describes both the
structure of the ``Request`` and ``Response`` messages.

Outbound Example
  OutboundStreamSession session = manager.getOutboundStreamSession();
  
  // simplified example of handling an authenticated service within the streams 
  DataOutputStream auth = session.sendData();
  DataInputStream credential = authentication.getCredential(credentialViaStreamType);
  auth.writeStream(credential);
  DataInputStream authResponse = session.receiveData();
  
  // sending an rpc-style command in the stream
  DataOutputStream out = session.sendData();
  String cmd = "<call><command>getSongs</command><params><param>" + album + "</param></call>";
  out.write(cmd.length(), cmd);
  out.close();
  
  while(session.hasDataAvailable()) {
      DataInputStream in = session.receiveData();
      addSongToPlayQueue(in);
  }



Inbound Example
  public void dispatch(OutboundStreamSession session) {
      Authentication auth = authenticateSession(session.receiveData());
      if (authzSession.isAuthorized(auth.getAgentId, fId, qId)) {
          String argv = parseCommandFromStream(session.receiveData());
          if (argv[0].equals("getSongs")) {
              Song songs = getSongsFromAlbum(argv[1]);
              for (song: songs) {
                  DataOutputStream out = session.sendData();
                  out.write(song.data(), song.size());
              }
          }
      }
  }



Message Example
  OutboundMessageSession session = manager.getOutboundMessageSession();
  
  Request request = session.getRequest();
  RequestHeader header = (HeaderRequestRecord) request.getRequestRecord(headerRequestRecordType);
  header.setAuthentication(authentication);
  // the message structure may also define interoperability cues 
  // for the consumer
  if (header.supportsLanguage()) {
      header.setLanguage(languageType);
  }
  
  Response response = session.makeRequest(request);
  
  if (response.ok()) {
      request = session.getRequest();
      ListSongsRequest cmd = (ListSongsRequestRecord) request.getRequestRecord(listSongsMessageType);
      cmd.setAlbum(albumName);
      response = session.makeRequest(request);
      if (response.ok()) {
          ListSongsResponse songs = (ListSongsResponseRecord) response.getResponseRecord(listSongsResponseRecordType);
  
          // the transport provider can return data in the message, or be used
          // to return usable objects as specified by its type
          for (Song song : songs.getSongs()) {
              Audio.play(song);
          }
      } else error(response.getStatusMessage());
  } else error (response.getStatusMessage());



"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class TransportProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any transport endpoint federation is exposed.
        Federation is exposed when a specific endpoint may be used.
        Federation is not exposed when a set of endpoints appears as a
        single endpoint.

        :return: ``true`` if federation is visible ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_outbound_stream(self):
        """Tests if outbound stream transport is supported.

        :return: ``true`` if outbound stream transport is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_inbound_stream(self):
        """Tests if inbound stream transport is supported.

        :return: ``true`` if incoming stream transport is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_outbound_message(self):
        """Tests if outbound message transport is supported.

        :return: ``true`` if outbound message transport is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_inbound_message(self):
        """Tests if inbound message transport is supported.

        :return: ``true`` if incoming message transport is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_endpoint_lookup(self):
        """Tests if endpoint lookup is supported.

        :return: ``true`` if endpoint lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_endpoint_record_types(self):
        """Gets a list of supported endpoint record types.

        :return: a list of supported endpoint record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    endpoint_record_types = property(fget=get_endpoint_record_types)

    def supports_endpoint_record_type(self, endpoint_record_type):
        """Tests if an endpoint record type is supported.

        :param endpoint_record_type: an endpoint record type
        :type endpoint_record_type: ``osid.type.Type``
        :return: ``true`` if the endpoint record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``endpoint_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_request_record_types(self):
        """Gets a list of supported request record types.

        :return: a list of supported request record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    request_record_types = property(fget=get_request_record_types)

    def supports_request_record_type(self, request_record_type):
        """Tests if a request record type is supported.

        :param request_record_type: a request record type
        :type request_record_type: ``osid.type.Type``
        :return: ``true`` if the request record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``request_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_response_record_types(self):
        """Gets a list of supported response record types.

        :return: a list of supported response record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    response_record_types = property(fget=get_response_record_types)

    def supports_response_record_type(self, response_record_type):
        """Tests if a response record type is supported.

        :param response_record_type: a response record type
        :type response_record_type: ``osid.type.Type``
        :return: ``true`` if the response record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``response_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class TransportManager(osid_managers.OsidManager, osid_sessions.OsidSession, TransportProfile):

    def get_outbound_stream_session(self):
        """Gets a service for outbound stream transport.

        :return: an ``OutboundStreamSession``
        :rtype: ``osid.transport.OutboundStreamSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_outbound_stream()`` is ``false``

        """
        raise UNIMPLEMENTED()

    outbound_stream_session = property(fget=get_outbound_stream_session)

    def get_outbound_stream_session_for_endpoint(self, endpoint_id):
        """Gets a service for outbound stream transport using a specified ``Endpoint``.

        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :return: an ``OutboundStreamSession``
        :rtype: ``osid.transport.OutboundStreamSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_outbound_stream()`` or ``supports_visible_federation_i()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_inbound_stream_session(self, stream_receiver):
        """Gets a service for inbound stream transport.

        :param stream_receiver: a stream receiver
        :type stream_receiver: ``osid.transport.StreamReceiver``
        :return: an ``InboundStreamSession``
        :rtype: ``osid.transport.InboundStreamSession``
        :raise: ``NullArgument`` -- ``stream_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound_stream()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_inbound_stream_session_for_endpoint(self, stream_receiver, endpoint_id):
        """Gets a service for inbound stream transport using a specified ``Endpoint``.

        :param stream_receiver: a stream receiver
        :type stream_receiver: ``osid.transport.StreamReceiver``
        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :return: an ``InboundStreamSession``
        :rtype: ``osid.transport.InboundStreamSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``stream_receiver`` or ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_inbound_stream()`` or ``supports_visible_federation_i()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_outbound_message_session(self):
        """Gets a service for outbound message transport.

        :return: an ``OutboundMessageSession``
        :rtype: ``osid.transport.OutboundMessageSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_outbound_message() is false``

        """
        raise UNIMPLEMENTED()

    outbound_message_session = property(fget=get_outbound_message_session)

    def get_outbound_message_session_for_endpoint(self, endpoint_id):
        """Gets a service for outbound message transport using a specified Endpoint.

        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :return: an ``OutboundMessageSession``
        :rtype: ``osid.transport.OutboundMessageSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_outbound_message() or supports_visible_federation_i() is false``

        """
        raise UNIMPLEMENTED()

    def get_inbound_message_session(self, message_receiver):
        """Gets a service for inbound message transport.

        :param message_receiver: a message receiver
        :type message_receiver: ``osid.transport.MessageReceiver``
        :return: an ``InboundMessageSession``
        :rtype: ``osid.transport.InboundMessageSession``
        :raise: ``NullArgument`` -- ``message_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound_message() is false``

        """
        raise UNIMPLEMENTED()

    def get_inbound_message_session_for_endpoint(self, message_receiver, endpoint_id):
        """Gets a service for inbound message transport using a specified Endpoint.

        :param message_receiver: a message receiver
        :type message_receiver: ``osid.transport.MessageReceiver``
        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :return: an ``InboundMessageSession``
        :rtype: ``osid.transport.InboundMessageSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``message_receiver`` or ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_inbound_message() or supports_visible_federation_i() is false``

        """
        raise UNIMPLEMENTED()

    def get_endpoint_lookup_session(self):
        """Gets the endpoint lookup service.

        :return: an ``EndpointLookupSesson``
        :rtype: ``osid.transport.EndpointLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound()`` is ``false``

        """
        raise UNIMPLEMENTED()

    endpoint_lookup_session = property(fget=get_endpoint_lookup_session)


##
# The following methods are from osid.transport.EndpointLookupSession

    def can_lookup_endpoints(self):
        """Tests if this user can perform ``Endpoint`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_endpoint_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_endpoint_view(self):
        """A complete view of the ``Endpoint`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_endpoint(self, endpoint_id):
        """Gets the ``Endpoint`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Endpoint`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Endpoint`` and retained for
        compatibility.

        :param endpoint_id: the ``Id`` of the ``Endpoint`` to retrieve
        :type endpoint_id: ``osid.id.Id``
        :return: the ``Endpoint``
        :rtype: ``osid.transport.Endpoint``
        :raise: ``NotFound`` -- no ``Endpoint`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``Id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_ids(self, endpoint_ids):
        """Gets an ``EndpointList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the endpoints
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Endpoint`` elements may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :param endpoint_ids: the list of ``Ids`` to retrieve
        :type endpoint_ids: ``osid.id.IdList``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``endpoint_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_genus_type(self, endpoint_genus_type):
        """Gets an ``EndpointList`` corresponding to the given endpoint genus ``Type`` which does not include endpoints of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :param endpoint_genus_type: an endpoint genus type
        :type endpoint_genus_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_parent_genus_type(self, endpoints_genus_type):
        """Gets an ``EndpointList`` corresponding to the given endpoint genus ``Type`` and include any additional endpoints with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :param endpoints_genus_type: an endpoint genus type
        :type endpoints_genus_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_record_type(self, endpoints_record_type):
        """Gets an ``EndpointList`` containing the given endpoint record ``Type``.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :param endpoints_record_type: an endpoint record type
        :type endpoints_record_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_provider(self, resource_id):
        """Gets an ``EndpointList`` containing the given endpoint record ``Type``.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints(self):
        """Gets all ``Endpoint`` elements.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.

        :return: a list of endpoints
        :rtype: ``osid.transport.EndpointList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    endpoints = property(fget=get_endpoints)



class TransportProxyManager(osid_managers.OsidProxyManager, TransportProfile):

    def get_outbound_stream_session(self, proxy):
        """Gets a service for outbound stream transport.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OutboundStreamSession``
        :rtype: ``osid.transport.OutboundStreamSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_outbound_stream()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_outbound_stream_session_for_endpoint(self, endpoint_id, proxy):
        """Gets a service for outbound stream transport using a specified ``Endpoint``.

        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OutboundStreamSession``
        :rtype: ``osid.transport.OutboundStreamSession``
        :raise: ``NotFound`` -- ``endpoint_id`` or ``proxy`` is not found
        :raise: ``NullArgument`` -- ``endpoint_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_outbound_stream()`` or ``supports_visible_federation_i()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_inbound_stream_session(self, stream_receiver, proxy):
        """Gets a service for inbound stream transport.

        :param stream_receiver: a stream receiver
        :type stream_receiver: ``osid.transport.StreamReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InboundStreamSession``
        :rtype: ``osid.transport.InboundStreamSession``
        :raise: ``NullArgument`` -- ``stream_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound_stream()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_inbound_stream_session_for_endpoint(self, stream_receiver, endpoint_id, proxy):
        """Gets a service for inbound stream transport using a specified ``Endpoint``.

        :param stream_receiver: a stream receiver
        :type stream_receiver: ``osid.transport.StreamReceiver``
        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InboundStreamSession``
        :rtype: ``osid.transport.InboundStreamSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``stream_receiver, endpoint_id`` or ``porxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_inbound_stream()`` or ``supports_visible_federation_i()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_outbound_message_session(self, proxy):
        """Gets a service for outbound message transport.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OutboundMessageSession``
        :rtype: ``osid.transport.OutboundMessageSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_outbound_message() is false``

        """
        raise UNIMPLEMENTED()

    def get_outbound_message_session_for_endpoint(self, endpoint_id, proxy):
        """Gets a service for outbound message transport using a specified Endpoint.

        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OutboundMessageSession``
        :rtype: ``osid.transport.OutboundMessageSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``endpoint_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_outbound_message() or supports_visible_federation_i() is false``

        """
        raise UNIMPLEMENTED()

    def get_inbound_message_session(self, message_receiver, proxy):
        """Gets a service for inbound message transport.

        :param message_receiver: a message receiver
        :type message_receiver: ``osid.transport.MessageReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InboundMessageSession``
        :rtype: ``osid.transport.InboundMessageSession``
        :raise: ``NullArgument`` -- ``message_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound_message() is false``

        """
        raise UNIMPLEMENTED()

    def get_inbound_message_session_for_endpoint(self, message_receiver, endpoint_id, proxy):
        """Gets a service for inbound message transport using a specified Endpoint.

        :param message_receiver: a message receiver
        :type message_receiver: ``osid.transport.MessageReceiver``
        :param endpoint_id: a transport endpoint
        :type endpoint_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``InboundMessageSession``
        :rtype: ``osid.transport.InboundMessageSession``
        :raise: ``NotFound`` -- ``endpoint_id`` is not found
        :raise: ``NullArgument`` -- ``message_receiver, endpoint_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_inbound_message() or supports_visible_federation_i() is false``

        """
        raise UNIMPLEMENTED()

    def get_endpoint_lookup_session(self, proxy):
        """Gets the endpoint lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EndpointLookupSesson``
        :rtype: ``osid.transport.EndpointLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_inbound()`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.transport.EndpointLookupSession

    def can_lookup_endpoints(self):
        """Tests if this user can perform ``Endpoint`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_endpoint_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_endpoint_view(self):
        """A complete view of the ``Endpoint`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_endpoint(self, endpoint_id):
        """Gets the ``Endpoint`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Endpoint`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Endpoint`` and retained for
        compatibility.


        :param endpoint_id: the ``Id`` of the ``Endpoint`` to retrieve
        :type endpoint_id: ``osid.id.Id``
        :return: the ``Endpoint``
        :rtype: ``osid.transport.Endpoint``
        :raise: ``NotFound`` -- no ``Endpoint`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``Id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_ids(self, endpoint_ids):
        """Gets an ``EndpointList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the endpoints
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Endpoint`` elements may be omitted from the list
        and may present the elements in any order including returning a
        unique set.


        :param endpoint_ids: the list of ``Ids`` to retrieve
        :type endpoint_ids: ``osid.id.IdList``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``endpoint_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_genus_type(self, endpoint_genus_type):
        """Gets an ``EndpointList`` corresponding to the given endpoint genus ``Type`` which does not include endpoints of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.


        :param endpoint_genus_type: an endpoint genus type
        :type endpoint_genus_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_parent_genus_type(self, endpoints_genus_type):
        """Gets an ``EndpointList`` corresponding to the given endpoint genus ``Type`` and include any additional endpoints with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.


        :param endpoints_genus_type: an endpoint genus type
        :type endpoints_genus_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_record_type(self, endpoints_record_type):
        """Gets an ``EndpointList`` containing the given endpoint record ``Type``.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.


        :param endpoints_record_type: an endpoint record type
        :type endpoints_record_type: ``osid.type.Type``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``endpoint_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints_by_provider(self, resource_id):
        """Gets an ``EndpointList`` containing the given endpoint record ``Type``.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Endpoint`` list
        :rtype: ``osid.transport.EndpointList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_endpoints(self):
        """Gets all ``Endpoint`` elements.
        In plenary mode, the returned list contains all known endpoints
        or an error results. Otherwise, the returned list may contain
        only those endpoints that are accessible through this session.


        :return: a list of endpoints
        :rtype: ``osid.transport.EndpointList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    endpoints = property(fget=get_endpoints)



class Endpoint(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_endpoint_record(self, endpoint_record_type):
        """Gets the endpoint record corresponding to the given ``Endpoint`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record.

        :param endpoint_record_type: an endpoint record type
        :type endpoint_record_type: ``osid.type.Type``
        :return: the endpoint record
        :rtype: ``osid.transport.records.EndpointRecord``
        :raise: ``NullArgument`` -- ``endpoint_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(endpoint_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.transport.OutboundStreamSession

    def get_endpoint_id(self):
        """Gets the ``Endpoint``  ``Id`` associated with this session.

        :return: the ``Endpoint``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    endpoint_id = property(fget=get_endpoint_id)

    def get_endpoint(self):
        """Gets the ``Endpoint`` associated with this session.

        :return: the ``Endpoint`` associated with this session
        :rtype: ``osid.transport.Endpoint``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    endpoint = property(fget=get_endpoint)

    def send_data(self):
        """Sends data to the remote transport endpoint.

        :return: the output stream in which to send data
        :rtype: ``osid.transport.DataOutputStream``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def has_data_available(self):
        """Tests to see if an input stream is available for retrieval.

        :return: ``true`` if a stream is available for reading, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def receive_data(self):
        """Receives data from the remote transport endpoint.

        :return: the input stream containing the received data
        :rtype: ``osid.transport.DataInputStream``
        :raise: ``IllegalState`` -- ``has_data_available()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.transport.InboundStreamSession

    def register_callback(self, receiver):
        """Registers a callback to receive incoming data.

        :param receiver: a stream receievr
        :type receiver: ``osid.transport.StreamReceiver``
        :raise: ``NullArgument`` -- ``receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.transport.OutboundMessageSession

    def get_request(self):
        """Gets a ``Request`` for use with ``sendRequest()``.
        This is not a receive call.

        :return: a request
        :rtype: ``osid.transport.Request``

        """
        raise UNIMPLEMENTED()

    request = property(fget=get_request)

    def make_request(self, request, response):
        """Sends a request to the remote transport endpoint and waits for a response.

        :param request: the request
        :type request: ``osid.transport.Request``
        :param response: callback for the response
        :type response: ``osid.transport.Response``
        :raise: ``NullArgument`` -- ``request`` or ``receiver`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``request`` is not supported

        """
        raise UNIMPLEMENTED()

    def send_request(self, request, callback):
        """Sends data to the remote transport endpoint and sends the response to the callback.

        :param request: the request
        :type request: ``osid.transport.Request``
        :param callback: callback for the response
        :type callback: ``osid.transport.MessageReceiver``
        :raise: ``NullArgument`` -- ``request`` or ``callback`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``request`` is not supported

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.transport.InboundMessageSession





class EndpointList(osid_objects.OsidList):

    def get_next_endpoint(self):
        """Gets the next ``Endpoint`` in this list.

        :return: the next ``Endpoint`` in this list. The ``has_next()`` method should be used to test that a next ``Endpoint`` is available before calling this method.
        :rtype: ``osid.transport.Endpoint``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_endpoint = property(fget=get_next_endpoint)

    def get_next_endpoints(self, n):
        """Gets the next set of ``Endpoint`` objects in this lis which must be less than or equal to whst is returned from ``available()``.

        :param n: the number of ``Endpoint`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Endpoint`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.transport.Endpoint``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Endpoints(TransportManager):
    pass


