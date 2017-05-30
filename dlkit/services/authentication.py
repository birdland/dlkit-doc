# -*- coding: utf-8 -*-
"""Authentication Open Service Interface Definitions
authentication version 3.0.0

The Authentication OSID manages authenticated entities.

Agent

The Authentication OSID defines an ``Agent`` to represent the identity
of the authenticated entity. An Agent may map to a specific
authentication principal while some providers may elect to hide multiple
authentication principals behind a single ``Agent``. Because principal
identities tend not to be durable and persistent, consumers should
always persist the ``Id``.

Resource Mapping

An ``Agent`` may be mapped to a ``Resource`` in the Resource OSID. A
``Resource`` may map to multiple ``Agents`` but an ``Agent`` may only
map to a single Resource. In the case of a person, a person may be
utilize a number of authentication technologies each with a different
authentication identity. Decoupling the authentication identity from
that of ther person is to provide a means of integrating multiple
services where different authentication identities exist for a person
that impact the handling of authorization.

Authorization

Authorization is a separate service. The Authorization OSID manages what
functions the ``Agent`` is authorized to perform and references the
``Agent``  ``Id``. The Authentication OSID is only responsible for
identity management of the ``Agent``.

Each ``Agent`` of a ``Resource`` may be used to define distinct security
levels of assurance (although the paranoid may opt for defining a
pseudo-resource for each ``Agent`` ). These security levels of assurance
can be linked to the ``Agent``  ``Type`` and managed in the
Authorization OSID. The ``Agent``  ``Type`` would be an indicator of the
authentication strength and although it may correlate to a specific
authentication technology, coupling it too tightly to a particular
technology may limit flexibility.

Certain consumers may wish to be notified of changes within the service.
Authentication supports notifications via an
``AgentNotificationSession``.
  if (manager.supportsAgentNotification()) {
      AgentNotificationSession ans = manager.getAgentNotificationSession(receiver);
      ans.registerForNewAgents();
      hangAround();
  }
  
  AgentReceiver receiver {
      newAgent(Id agentId) { print("new agent"); }
      changedAgent(Id agentId) { print("updated agent"); }
      deletedAgent(Id agentId) { print("deleted agent"); }
  }



Agency Cataloging

``Agents`` are organized into federateable ``Agency``  ``OsidCatalogs``.

Sub Packages

The Authentication OSID includes an Authentication Key OSID for managing
private keys associated with an ``Agent`` and an Authentication Process
OSID for acquiring and validating authentication credentials. It slaos
includes an Authentication Batch OSID for managing ``Agents`` and
``Agencies`` in bulk.

"""

from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class AuthenticationProfile(osid_managers.OsidProfile):
    """The ``AuthenticationProfile`` describes the interoperability among authentication services."""

    def supports_agent_lookup(self):
        """Tests if an agent lookup service is supported.

        An agent lookup service defines methods to access agents.

        :return: ``true`` if agent lookup is supported, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_agent_record_types(self):
        """Gets the supported ``Agent`` record types.

        :return: a list containing the supported ``Agent`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    agent_record_types = property(fget=get_agent_record_types)

    def get_agent_search_record_types(self):
        """Gets the supported ``Agent`` search record types.

        :return: a list containing the supported ``Agent`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    agent_search_record_types = property(fget=get_agent_search_record_types)

    def get_agency_record_types(self):
        """Gets the supported ``Agency`` record types.

        :return: a list containing the supported ``Agency`` record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    agency_record_types = property(fget=get_agency_record_types)

    def get_agency_search_record_types(self):
        """Gets the supported ``Agency`` search record types.

        :return: a list containing the supported ``Agency`` search record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    agency_search_record_types = property(fget=get_agency_search_record_types)


class AuthenticationManager(osid_managers.OsidManager, osid_sessions.OsidSession, AuthenticationProfile):
    """The authentication manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AgentLookupSession:`` a session to look up ``Agents``
      * ``AgentQuerySession:`` a session to query ``Agents``
      * ``AgentSearchSession:`` a session to search ``Agents``
      * ``AgentAdminSession:`` a session to create, modify and delete
        ``Agents``
      * ``AgentNotificationSession: a`` session to receive messages
        pertaining to ``Agent`` changes

      * ``AgentAgencySession:`` a session to retrieve ``Agent`` to
        ``Agency`` mappings
      * ``AgentAgencyAssignmentSession:`` a session to manage ``Agent``
        to ``Agency`` mappings
      * ``AgentSmartAgencySession:`` a session to create dynamic
        agencies
      * ``AgencyLookupSession:`` a session to lookup agencies
      * ``AgencyQuerySession:`` a session to query agencies
      * ``AgencySearchSession`` : a session to search agencies
      * ``AgencyAdminSession`` : a session to create, modify and delete
        agencies
      * ``AgencyNotificationSession`` : a session to receive messages
        pertaining to ``Agency`` changes
      * ``AgencyHierarchySession`` : a session to traverse the
        ``Agency`` hierarchy
      * ``AgencyHierarchyDesignSession`` : a session to manage the
        ``Agency`` hierarchy

    """

    def get_authentication_batch_manager(self):
        """Gets an ``AuthenticationBatchManager``.

        :return: an ``AuthenticationBatchManager``.
        :rtype: ``osid.authentication.batch.AuthenticationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authentication_batch()`` is ``true``.*

        """
        return # osid.authentication.batch.AuthenticationBatchManager

    authentication_batch_manager = property(fget=get_authentication_batch_manager)

    def get_authentication_keys_manager(self):
        """Gets an ``AuthenticationKeysManager``.

        :return: an ``AuthenticationKeysManager``.
        :rtype: ``osid.authentication.keys.AuthenticationKeysManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_keys()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authentication_keys()`` is ``true``.*

        """
        return # osid.authentication.keys.AuthenticationKeysManager

    authentication_keys_manager = property(fget=get_authentication_keys_manager)

    def get_authentication_process_manager(self):
        """Gets an ``AuthenticationProcessManager``.

        :return: an ``AuthenticationProcessManager``.
        :rtype: ``osid.authentication.process.AuthenticationProcessManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_process()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authentication_process()`` is ``true``.*

        """
        return # osid.authentication.process.AuthenticationProcessManager

    authentication_process_manager = property(fget=get_authentication_process_manager)


class AuthenticationProxyManager(osid_managers.OsidProxyManager, AuthenticationProfile):
    """The authentication proxy manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AgentLookupSession:`` session to look up ``Agents``
      * ``AgentQuerySession`` : a session to query ``Agents``
      * ``AgentSearchSession:`` session to search ``Agents``
      * ``AgentAdminSession:`` session to create, modify and delete
        ``Agents``
      * Agent ``NotificationSession:`` session to receive messages
        pertaining to ``Agent`` changes

      * ``AgentAgencySession:`` a session to retrieve ``Agent`` to
        ``Agency`` mappings
      * ``AgentAgencyAssignmentSession:`` a session to manage ``Agent``
        to ``Agency`` mappings
      * ``AgentSmartAgencySession:`` a session to create dynamic
        agencies
      * ``AgencyLookupSession:`` a session to lookup agencies
      * ``AgencyQuerySession:`` a session to query agencies
      * ``AgencySearchSession`` : a session to search agencies
      * ``AgencyAdminSession`` : a session to create, modify and delete
        agencies
      * ``AgencyNotificationSession`` : a session to receive messages
        pertaining to ``Agency`` changes
      * ``AgencyHierarchySession`` : a session to traverse the
        ``Agency`` hierarchy
      * ``AgencyHierarchyDesignSession`` : a session to manage the
        ``Agency`` hierarchy

    """

    def get_authentication_batch_proxy_manager(self):
        """Gets an ``AuthenticationBatchProxyManager``.

        :return: an ``AuthenticationBatchProxyManager``.
        :rtype: ``osid.authentication.batch.AuthenticationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_batch()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authentication_batch()`` is ``true``.*

        """
        return # osid.authentication.batch.AuthenticationBatchProxyManager

    authentication_batch_proxy_manager = property(fget=get_authentication_batch_proxy_manager)

    def get_authentication_keys_proxy_manager(self):
        """Gets an ``AuthenticationKeysProxyManager``.

        :return: an ``AuthenticationKeysProxyManager``.
        :rtype: ``osid.authentication.keys.AuthenticationKeysProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_keys()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authentication_keys()`` is ``true``.*

        """
        return # osid.authentication.keys.AuthenticationKeysProxyManager

    authentication_keys_proxy_manager = property(fget=get_authentication_keys_proxy_manager)

    def get_authentication_process_proxy_manager(self):
        """Gets an ``AuthenticationProcessProxyManager``.

        :return: an ``AuthenticationProcessproxyManager``.
        :rtype: ``osid.authentication.process.AuthenticationProcessProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_process()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_authentication_process()`` is ``true``.*

        """
        return # osid.authentication.process.AuthenticationProcessProxyManager

    authentication_process_proxy_manager = property(fget=get_authentication_process_proxy_manager)


