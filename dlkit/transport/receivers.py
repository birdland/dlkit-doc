from ..osid import receivers as osid_receivers


class StreamReceiver(osid_receivers.OsidReceiver):
    """The ``StreamReceiver`` is used to receive incoming connections.

    The receiver is provided to the service via the
    ``InboundStreamSession`` and invoked by the transport provider when
    a new association is created.

    """
    def dispatch(self, session):
        """Invoked by the transport provider when a new connection request or datagram is received.

        :param session: a session to send and receive data
        :type session: ``osid.transport.OutboundStreamSession``

        """
        pass


class MessageReceiver(osid_receivers.OsidReceiver):
    """The ``MessageReceiver`` is used to receive incoming connections.

    The receiver is provided to the service via the
    ``InboundMessageSession`` and invoked by the transport provider when
    a new association is created.

    """
    def dispatch(self, session):
        """Invoked by the transport provider when a new connection request or datagram is received.

        :param session: a session to send and receive messages
        :type session: ``osid.transport.OutboundMessageSession``

        """
        pass


