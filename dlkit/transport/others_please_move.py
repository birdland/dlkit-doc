from ..osid import markers as osid_markers


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


