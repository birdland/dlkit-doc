from ..osid import objects as osid_objects
from ..osid import markers as osid_markers


class Endpoint(osid_objects.OsidCatalog):
    """An ``Endpoint`` represents a transport destination."""
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
        return # osid.transport.records.EndpointRecord


class EndpointList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``EndpointList`` provides a means for accessing ``Endpoint`` elements sequentially either one at a time or many at a time.

    Examples: while (el.hasNext()) { Endpoint endpoint =
    el.getNextEndpoint(); }

    or
      while (el.hasNext()) {
           Endpoint[] endpoints = el.getNextEndpoints(el.available());
      }



    """
    def get_next_endpoint(self):
        """Gets the next ``Endpoint`` in this list.

        :return: the next ``Endpoint`` in this list. The ``has_next()`` method should be used to test that a next ``Endpoint`` is available before calling this method.
        :rtype: ``osid.transport.Endpoint``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.transport.Endpoint

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
        return # osid.transport.Endpoint


class Request(osid_markers.Suppliable, osid_markers.Extensible):
    """A ``Request`` represents a stuctured request to a service endpoint.

    The record types supported may vary on a request by request basis as
    defined in the underlying protocol.

    """
    def set_id(self, id_):
        """Sets an identifier for this request.

        :param id: an identifier
        :type id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``id`` is ``null``

        """
        pass

    id_ = property(fset=set_id)

    def get_request_record(self, request_record_type):
        """Gets the request record.

        This method is used to retrieve an object implementing the
        requested message.

        :param request_record_type: a request record type
        :type request_record_type: ``osid.type.Type``
        :return: the request record
        :rtype: ``osid.transport.records.RequestRecord``
        :raise: ``NullArgument`` -- ``request_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(request_type)`` is ``false``

        """
        return # osid.transport.records.RequestRecord


class Response(osid_objects.OsidObject):
    """A ``Response`` represents a stuctured response from a service endpoint."""
    def ok(self):
        """Tests if the request was successful.

        :return: ``true`` if the request was successful, ``false`` otherrwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_status_message(self):
        """Gets a status message.

        The returned string may be empty or may contain an error message
        is an error occurred.

        :return: an error message
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    status_message = property(fget=get_status_message)

    def get_response_record(self, response_record_type):
        """Gets the response record.

        This method is used to retrieve an object implementing the
        requested message.

        :param response_record_type: a response record type
        :type response_record_type: ``osid.type.Type``
        :return: the response record
        :rtype: ``osid.transport.records.ResponseRecord``
        :raise: ``NullArgument`` -- ``response_message_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(response_record_type)`` is ``false``

        """
        return # osid.transport.records.ResponseRecord


class DataInputStream:
    """The data input stream provides a means for reading data from a stream."""
    def at_end_of_stream(self):
        """Tests if the end of this stream has been reached.

        This may not be a permanent condition as more data may be
        available at a later time as in the case of tailing a file.

        :return: ``true`` if the end of this stream has been reached, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- this stream has been closed

        """
        return # boolean

    def available(self):
        """Gets the number of ``bytes`` available for retrieval.

        The number returned by this method may be less than or equal to
        the total number of ``bytes`` in this stream.

        :return: the number of ``bytes`` available for retrieval
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- this stream has been closed

        """
        return # cardinal

    def skip(self, n):
        """Skips a specified number of ``bytes`` in the stream.

        :param n: the number of ``bytes`` to skip
        :type n: ``cardinal``
        :return: the actual number of ``bytes`` skipped
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- this stream has been closed or ``at_end_of_stream()`` is ``true``

        """
        return # cardinal

    def read(self, buf, n):
        """Reads a specified number of ``bytes`` from this stream.

        :param buf: the buffer in which the data is read
        :type buf: ``byte[]``
        :param n: the number of ``bytes`` to read
        :type n: ``cardinal``
        :return: the actual number of ``bytes`` read
        :rtype: ``integer``
        :raise: ``IllegalState`` -- this stream has been closed or ``at_end_of_stream()`` is ``true``
        :raise: ``InvalidArgument`` -- the size of ``buf`` is less than ``n``
        :raise: ``NullArgument`` -- ``buf`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # integer

    def close(self):
        """Closes this stream and frees up any allocated resources.

        Methods in this object may not be invoked after this method is
        called.

        :raise: ``IllegalState`` -- this stream has been closed

        """
        pass


class DataOutputStream:
    """The data output stream provides a means in which data can be written to a stream."""
    def write(self, buf, n):
        """Writes ``n`` bytes to this stream.

        :param buf: the buffer containing the data to write
        :type buf: ``byte[]``
        :param n: the number of ``bytes`` to write
        :type n: ``cardinal``
        :raise: ``IllegalState`` -- this stream has been closed
        :raise: ``InvalidArgument`` -- ``buf`` does not contain ``n bytes``
        :raise: ``NullArgument`` -- ``buf`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        pass

    def write_stream(self, stream):
        """Writes a stream to this stream.

        :param stream: an input stream
        :type stream: ``osid.transport.DataInputStream``
        :raise: ``IllegalState`` -- this stream has been closed
        :raise: ``NullArgument`` -- ``stream`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        pass

    def close(self):
        """Flushes the output, closes this stream and frees up any allocated resources.

        Methods in this object may not be invoked after this method is
        called.

        :raise: ``IllegalState`` -- this stream has been closed

        """
        pass


