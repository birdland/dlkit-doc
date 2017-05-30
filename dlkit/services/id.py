# -*- coding: utf-8 -*-
"""Id Open Service Interface Definitions
id version 3.0.0

The Id OSID provides the means for creating and mapping identifiers. All
OSID objects are identified by a unique and immutable ``Id``. The ``Id``
OSID can be used to generate new ``Ids`` when creating new objects.

Consumers wishing to persist an OSID object should instead persist the
reference to the object by serializing the ``Id``.

Most OSID interfaces are used to encapsulate implementation-specific
objects from provider to consumer. ``Id`` is an ``OsidPrimitive`` and as
such cannot be used to encapsulate implementation-specific data other
than what is defined explicitly in the ``Id``. An OSID Provider must
respect any ``Id`` based on its interface alone.

The Id service can be used to assign Ids for an OSID Provider or be used
to manage Id translations for system to system compatibility.

The ``Id`` service can also be used as a means to map one identifier to
another when an object is known by multiple identifiers. Mapping
identifier spaces is often a critical part of interoperability and the
Id service can be used as a shim to bridge different systems.

Id Mapping Example
  public Asset getAsset(assetId) {
      Id id = idSession.getId(assetId);
      return (other_impl.getAsset(assetId));
  }



"""

from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import markers as osid_markers
from ..osid import objects as osid_objects


class IdProfile(osid_managers.OsidProfile):
    """The ``IdProfile`` describes the interoperability among id services."""
    pass



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


