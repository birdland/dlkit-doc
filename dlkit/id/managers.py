
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class IdProfile(osid_managers.OsidProfile):
    """The ``IdProfile`` describes the interoperability among id services."""




class IdManager(osid_managers.OsidManager, osid_sessions.OsidSession, IdProfile):
    """This manager provides access to the available sessions of the Id service.

    ``Ids`` are created through the ``IdAdminSession`` which provides
    the means for creating a unique identifier.

    The ``IdLookupSession`` can be used for mapping one ``Id`` to
    another in addition to getting a list of the assigned identifiers.

    """

    def get_id_batch_manager(self):
        """Gets an ``IdBatchManager``.

        :return: an ``IdBatchManager``
        :rtype: ``osid.id.batch.IdBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_batch()`` is ``true``.*

        """
        return # osid.id.batch.IdBatchManager

    id_batch_manager = property(fget=get_id_batch_manager)


class IdProxyManager(osid_managers.OsidProxyManager, IdProfile):
    """This manager provides access to the available sessions of the Id service.

    Methods in this manager support the passing of a ``Proxy`` object
    for the purpose of pasisng information from a server envrionment.

    ``Ids`` are created through the ``IdAdminSession`` which provides
    the means for creating a unique identifier. The ``IdBrowserSession``
    can be used for mapping one ``Id`` to another in addition to getting
    a list of the assigned identifiers.

    """

    def get_id_batch_proxy_manager(self):
        """Gets an ``IdnProxyManager``.

        :return: an ``IdBatchProxyManager``
        :rtype: ``osid.id.batch.IdBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_id_batch()`` is ``true``.*

        """
        return # osid.id.batch.IdBatchProxyManager

    id_batch_proxy_manager = property(fget=get_id_batch_proxy_manager)


