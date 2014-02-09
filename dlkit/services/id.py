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
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions


class IdProfile(osid_managers.OsidProfile):

    def supports_id_lookup(self):
        """Tests if ``Id`` lookup is supported.

        :return: ``true`` if ``Id`` lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_id_issue(self):
        """Tests if an ``Id`` issue service is supported.

        :return: ``true`` if ``Id`` issuing is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_id_admin(self):
        """Tests if an ``Id`` administrative service is supported.

        :return: ``true`` if ``Id`` administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_id_batch(self):
        """Tests for the availability of an Id batch service.

        :return: ``true`` if an Id batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()



class IdManager(osid_managers.OsidManager, osid_sessions.OsidSession, IdProfile):

    def get_id_lookup_session(self):
        """Gets the session associated with the id lookup service.

        :return: an ``IdLookupSession``
        :rtype: ``osid.id.IdLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    id_lookup_session = property(fget=get_id_lookup_session)

    def get_id_issue_session(self):
        """Gets the session associated with the id issue service.

        :return: an ``IdIssueSession``
        :rtype: ``osid.id.IdIssueSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_issue()`` is ``false``

        """
        raise UNIMPLEMENTED()

    id_issue_session = property(fget=get_id_issue_session)

    def get_id_admin_session(self):
        """Gets the session associated with the id admin service.

        :return: an ``IdAdminSession``
        :rtype: ``osid.id.IdAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    id_admin_session = property(fget=get_id_admin_session)

    def get_id_batch_manager(self):
        """Gets an ``IdBatchManager``.

        :return: an ``IdBatchManager``
        :rtype: ``osid.id.batch.IdBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    id_batch_manager = property(fget=get_id_batch_manager)



class IdProxyManager(osid_managers.OsidProxyManager, IdProfile):

    def get_id_lookup_session(self, proxy):
        """Gets the session associated with the id lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``IdLookupSession``
        :rtype: ``osid.id.IdLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_id_issue_session(self, proxy):
        """Gets the session associated with the id issue service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``IdIssueSession``
        :rtype: ``osid.id.IdIssueSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_id_issue()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_id_admin_session(self, proxy):
        """Gets the session associated with the id administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``IdAdminSession``
        :rtype: ``osid.id.IdAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_id_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_id_batch_proxy_manager(self):
        """Gets an ``IdnProxyManager``.

        :return: an ``IdBatchProxyManager``
        :rtype: ``osid.id.batch.IdBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_id_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    id_batch_proxy_manager = property(fget=get_id_batch_proxy_manager)



