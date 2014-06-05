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