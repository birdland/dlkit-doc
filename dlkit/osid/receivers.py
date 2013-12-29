


class OsidReceiver:
    """An ``OsidReceiver`` is used to receive asynchronous notifications from a service.

    The receiver defines the interface to be implemented by the
    consumer.

    """
    def up(self):
        """The callback for notifications that the notification bus is operational."""
        pass

    def down(self):
        """The callback for notifications that the notification bus is not operating."""
        pass


