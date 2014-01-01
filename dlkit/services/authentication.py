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
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class AuthenticationProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authentication_acquisition(self):
        """Tests is authentication acquisition is supported.
        Authentication acquisition is responsible for acquiring client
        side authentication credentials.

        :return: ``true`` if authentication acquisiiton is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authentication_validation(self):
        """Tests if authentication validation is supported.
        Authentication validation verifies given authentication
        credentials and maps to an agent identity.

        :return: ``true`` if authentication validation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agent_lookup(self):
        """Tests if an agent lookup service is supported.
        An agent lookup service defines methods to access agents.

        :return: ``true`` if agent lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agent_query(self):
        """Tests if an agent query service is supported.

        :return: ``true`` if agent query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agent_search(self):
        """Tests if an agent search service is supported.

        :return: ``true`` if agent search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agent_admin(self):
        """Tests if an agent administrative service is supported.

        :return: ``true`` if agent admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agent_notification(self):
        """Tests if agent notification is supported.
        Messages may be sent when agents are created, modified, or
        deleted.

        :return: ``true`` if agent notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agent_agency(self):
        """Tests if retrieving mappings of agents and agencies is supported.

        :return: ``true`` if agent agency mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agent_agency_assignment(self):
        """Tests if managing mappings of agents and agencies is supported.

        :return: ``true`` if agent agency assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agent_smart_agency(self):
        """Tests if agent smart agency is available.

        :return: ``true`` if agent smart agency is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agency_lookup(self):
        """Tests if an agency lookup service is supported.
        An agency lookup service defines methods to access agencies.

        :return: ``true`` if agency lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agency_query(self):
        """Tests if an agency query service is supported.

        :return: ``true`` if agency query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agency_search(self):
        """Tests if an agency search service is supported.

        :return: ``true`` if agency search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agency_admin(self):
        """Tests if an agency administrative service is supported.

        :return: ``true`` if agency admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agency_notification(self):
        """Tests if agency notification is supported.
        Messages may be sent when agencies are created, modified, or
        deleted.

        :return: ``true`` if agency notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agency_hierarchy(self):
        """Tests if an agency hierarchy traversal is supported.

        :return: ``true`` if an agency hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_agency_hierarchy_design(self):
        """Tests if an agency hierarchy design is supported.

        :return: ``true`` if an agency hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authentication_keys(self):
        """Tests if an authentication key service is available.

        :return: ``true`` if an authentication key service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_authentication_process(self):
        """Tests if an authentication process service is available.

        :return: ``true`` if an authentication process service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_agent_record_types(self):
        """Gets the supported ``Agent`` record types.

        :return: a list containing the supported ``Agent`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    agent_record_types = property(fget=get_agent_record_types)

    def supports_agent_record_type(self, agent_record_type):
        """Tests if the given ``Agent`` record type is supported.

        :param agent_record_type: a ``Type`` indicating an ``Agent`` record type
        :type agent_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_agent_search_record_types(self):
        """Gets the supported ``Agent`` search record types.

        :return: a list containing the supported ``Agent`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    agent_search_record_types = property(fget=get_agent_search_record_types)

    def supports_agent_search_record_type(self, agent_search_record_type):
        """Tests if the given ``Agent`` search record type is supported.

        :param agent_search_record_type: a ``Type`` indicating an ``Agent`` search record type
        :type agent_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_agency_record_types(self):
        """Gets the supported ``Agency`` record types.

        :return: a list containing the supported ``Agency`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    agency_record_types = property(fget=get_agency_record_types)

    def supports_agency_record_type(self, agency_record_type):
        """Tests if the given ``Agency`` record type is supported.

        :param agency_record_type: a ``Type`` indicating an ``Agency`` record type
        :type agency_record_type: ``osid.type.Type``
        :return: ``true`` if the given record Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_agency_search_record_types(self):
        """Gets the supported ``Agency`` search record types.

        :return: a list containing the supported ``Agency`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    agency_search_record_types = property(fget=get_agency_search_record_types)

    def supports_agency_search_record_type(self, agency_search_record_type):
        """Tests if the given ``Agency`` search record type is supported.

        :param agency_search_record_type: a ``Type`` indicating an ``Agency`` search record type
        :type agency_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agency_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class AuthenticationManager(osid_managers.OsidManager, osid_sessions.OsidSession, AuthenticationProfile):

    def get_agent_lookup_session(self):
        """Gets the ``OsidSession`` associated with the agent lookup service.

        :return: an ``AgentLookupSession``
        :rtype: ``osid.authentication.AgentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agent_lookup_session = property(fget=get_agent_lookup_session)

    def get_agent_lookup_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent lookup service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_lookup_session``
        :rtype: ``osid.authentication.AgentLookupSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_query_session(self):
        """Gets the ``OsidSession`` associated with the agent query service.

        :return: an ``AgentQuerySession``
        :rtype: ``osid.authentication.AgentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agent_query_session = property(fget=get_agent_query_session)

    def get_agent_query_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent query service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_query_session``
        :rtype: ``osid.authentication.AgentQuerySession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_search_session(self):
        """Gets the ``OsidSession`` associated with the agent search service.

        :return: an ``AgentSearchSession``
        :rtype: ``osid.authentication.AgentSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agent_search_session = property(fget=get_agent_search_session)

    def get_agent_search_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent search service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_search_session``
        :rtype: ``osid.authentication.AgentSearchSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_admin_session(self):
        """Gets the ``OsidSession`` associated with the agent administration service.

        :return: an ``AgentAdminSession``
        :rtype: ``osid.authentication.AgentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agent_admin_session = property(fget=get_agent_admin_session)

    def get_agent_admin_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent admin service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_admin_session``
        :rtype: ``osid.authentication.AgentAdminSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_notification_session(self, agent_receiver):
        """Gets the notification session for notifications pertaining to service changes.

        :param agent_receiver: the agent receiver
        :type agent_receiver: ``osid.authentication.AgentReceiver``
        :return: an ``AgentNotificationSession``
        :rtype: ``osid.authentication.AgentNotificationSession``
        :raise: ``NullArgument`` -- ``agent_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_notification_session_for_agency(self, agent_receiver, agency_id):
        """Gets the ``OsidSession`` associated with the agent notification service for the given agency.

        :param agent_receiver: the agent receiver
        :type agent_receiver: ``osid.authentication.AgentReceiver``
        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: ``an _agent_notification_session``
        :rtype: ``osid.authentication.AgentNotificationSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agent_receiver`` or ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_agency_session(self):
        """Gets the session for retrieving agent to agency mappings.

        :return: an ``AgentAgencySession``
        :rtype: ``osid.authentication.AgentAgencySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_agency()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agent_agency_session = property(fget=get_agent_agency_session)

    def get_agent_agency_assignment_session(self):
        """Gets the session for assigning agent to agency mappings.

        :return: a ``AgentAgencyAsignmentSession``
        :rtype: ``osid.authentication.AgentAgencyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_agency_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agent_agency_assignment_session = property(fget=get_agent_agency_assignment_session)

    def get_agent_smart_agency_session(self, agency_id):
        """Gets the ``OsidSession`` associated with the agent smart agency service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: an ``AgentSmartAgencySession``
        :rtype: ``osid.authentication.AgentSmartAgencySession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_smart_agency()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agency_lookup_session(self):
        """Gets the ``OsidSession`` associated with the agency lookup service.

        :return: an ``AgencyLookupSession``
        :rtype: ``osid.authentication.AgencyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agency_lookup_session = property(fget=get_agency_lookup_session)

    def get_agency_search_session(self):
        """Gets the ``OsidSession`` associated with the agency search service.

        :return: an ``AgencySearchSession``
        :rtype: ``osid.authentication.AgencySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agency_search_session = property(fget=get_agency_search_session)

    def get_agency_admin_session(self):
        """Gets the ``OsidSession`` associated with the agency administration service.

        :return: an ``AgencyAdminSession``
        :rtype: ``osid.authentication.AgencyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agency_admin_session = property(fget=get_agency_admin_session)

    def get_agency_notification_session(self, agency_receiver):
        """Gets the notification session for notifications pertaining to agency service changes.

        :param agency_receiver: the agency receiver
        :type agency_receiver: ``osid.authentication.AgencyReceiver``
        :return: an ``AgencyNotificationSession``
        :rtype: ``osid.authentication.AgencyNotificationSession``
        :raise: ``NullArgument`` -- ``agency_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agency_hierarchy_session(self):
        """Gets the session traversing agency hierarchies.

        :return: an ``AgencyHierarchySession``
        :rtype: ``osid.authentication.AgencyHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agency_hierarchy_session = property(fget=get_agency_hierarchy_session)

    def get_agency_hierarchy_design_session(self):
        """Gets the session designing agency hierarchies.

        :return: an ``AgencyHierarchyDesignSession``
        :rtype: ``osid.authentication.AgencyHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    agency_hierarchy_design_session = property(fget=get_agency_hierarchy_design_session)

    def get_authentication_batch_manager(self):
        """Gets an ``AuthenticationBatchManager``.

        :return: an ``AuthenticationBatchManager``.
        :rtype: ``osid.authentication.batch.AuthenticationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authentication_batch_manager = property(fget=get_authentication_batch_manager)

    def get_authentication_keys_manager(self):
        """Gets an ``AuthenticationKeysManager``.

        :return: an ``AuthenticationKeysManager``.
        :rtype: ``osid.authentication.keys.AuthenticationKeysManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_keys()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authentication_keys_manager = property(fget=get_authentication_keys_manager)

    def get_authentication_process_manager(self):
        """Gets an ``AuthenticationProcessManager``.

        :return: an ``AuthenticationProcessManager``.
        :rtype: ``osid.authentication.process.AuthenticationProcessManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_process()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authentication_process_manager = property(fget=get_authentication_process_manager)


##
# The following methods are from osid.authentication.AgencyLookupSession

    def can_lookup_agencies(self):
        """Tests if this user can perform ``Agency`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_agency_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_agency_view(self):
        """A complete view of the ``Agency`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_agency(self, agency_id):
        """Gets the ``Agency`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Agency`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Agency`` and retained for compatibility.

        :param agency_id: ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: the agency
        :rtype: ``osid.authentication.Agency``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agencies_by_ids(self, agency_ids):
        """Gets an ``AgencyList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the agencies
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Agency`` objects may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param agency_ids: a list of agency ``Ids``
        :type agency_ids: ``osid.id.IdList``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``agency_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agencies_by_genus_type(self, agency_genus_type):
        """Gets an ``AgencyList`` corresponding to the given agency genus ``Type`` which does not include agencies of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :param agency_genus_type: an agency genus type
        :type agency_genus_type: ``osid.type.Type``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``agency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agencies_by_parent_genus_type(self, agency_genus_type):
        """Gets an ``AgencyList`` corresponding to the given agency genus ``Type`` and include any additional agencies with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :param agency_genus_type: an agency genus type
        :type agency_genus_type: ``osid.type.Type``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``agency_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agencies_by_record_type(self, agency_record_type):
        """Gets an ``AgencyList`` containing the given agency record ``Type``.
        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agencies_by_provider(self, resource_id):
        """Gets an ``AgencyList`` from the given provider.
        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Agency`` list
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agencies(self):
        """Gets all ``Agencies``.
        In plenary mode, the returned list contains all known agencies
        or an error results. Otherwise, the returned list may contain
        only those agencies that are accessible through this session.

        :return: an ``AgencyList``
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    agencies = property(fget=get_agencies)


##
# The following methods are from osid.authentication.AgencyQuerySession

    def can_search_agencies(self):
        """Tests if this user can perform ``Agency`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an app

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_agency_query(self):
        """Gets an agency query.

        :return: an agency query
        :rtype: ``osid.authentication.AgencyQuery``

        """
        raise UNIMPLEMENTED()

    agency_query = property(fget=get_agency_query)

    def get_agencies_by_query(self, agency_query):
        """Gets a list of ``Agency`` objects matching the given agency query.

        :param agency_query: the agency query
        :type agency_query: ``osid.authentication.AgencyQuery``
        :return: the returned ``AgencyList``
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NullArgument`` -- ``agency_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agency_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgencySearchSession

    def get_agency_search(self):
        """Gets an agency search.

        :return: an agency search
        :rtype: ``osid.authentication.AgencySearch``

        """
        raise UNIMPLEMENTED()

    agency_search = property(fget=get_agency_search)

    def get_agency_search_order(self):
        """Gets an agency search order.
        The ``AgencySearchOrder`` is supplied to a ``AgencySearch`` to
        specify the ordering of results.

        :return: the agency search order
        :rtype: ``osid.authentication.AgencySearchOrder``

        """
        raise UNIMPLEMENTED()

    agency_search_order = property(fget=get_agency_search_order)

    def get_agencies_by_search(self, agency_query, agency_search):
        """Gets the search results matching the given search query using the given search.

        :param agency_query: the agency query
        :type agency_query: ``osid.authentication.AgencyQuery``
        :param agency_search: the agency search
        :type agency_search: ``osid.authentication.AgencySearch``
        :return: the search results
        :rtype: ``osid.authentication.AgencySearchResults``
        :raise: ``NullArgument`` -- ``agency_query`` or ``agency_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agency_query`` or ``agency_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_agency_query_from_inspector(self, agency_query_inspector):
        """Gets an agency query from an inspector.
        The inspector is available from an ``AgencySearchResults``.

        :param agency_query_inspector: an agency query inspector
        :type agency_query_inspector: ``osid.authentication.AgencyQueryInspector``
        :return: the agency query
        :rtype: ``osid.authentication.AgencyQuery``
        :raise: ``NullArgument`` -- ``agency_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``agency_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgencyAdminSession

    def can_create_agencies(self):
        """Tests if this user can create ``Agencies``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Agency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Agency`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_agency_with_record_types(self, agency_record_types):
        """Tests if this user can create a single ``Agency`` using the desired record types.
        While ``AuthenticationManager.getAgencyRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific ``Agency``.
        Providing an empty array tests if an ``Agency`` can be created
        with no records.

        :param agency_record_types: array of agency record types
        :type agency_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Agency`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agency_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_agency_form_for_create(self, agency_record_types):
        """Gets the agency form for creating new agencies.
        A new form should be requested for each create transaction.

        :param agency_record_types: array of agency record types
        :type agency_record_types: ``osid.type.Type[]``
        :return: the agency form
        :rtype: ``osid.authentication.AgencyForm``
        :raise: ``NullArgument`` -- ``agency_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_agency(self, agency_form):
        """Creates a new ``Agency``.

        :param agency_form: the form for this ``Agency``
        :type agency_form: ``osid.authentication.AgencyForm``
        :return: the new ``Agency``
        :rtype: ``osid.authentication.Agency``
        :raise: ``IllegalState`` -- ``agency_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``agency_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agency_form`` did not originate from ``get_agency_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_agencies(self):
        """Tests if this user can update ``Agencies``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Agency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Agency`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_agency_form_for_update(self, agency_id):
        """Gets the agency form for updating an existing agency.
        A new agency form should be requested for each update
        transaction.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: the agency form
        :rtype: ``osid.authentication.AgencyForm``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_agency(self, agency_form):
        """Updates an existing agency.

        :param agency_form: the form containing the elements to be updated
        :type agency_form: ``osid.authentication.AgencyForm``
        :raise: ``IllegalState`` -- ``agency_form`` already used for an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``agency_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agency_form`` did not originate from ``get_agency_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_agencies(self):
        """Tests if this user can delete agencies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Agency`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Agency`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_agency(self, agency_id):
        """Deletes an ``Agency``.

        :param agency_id: the ``Id`` of the ``Agency`` to remove
        :type agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_agency_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Agencies``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Agency`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_agency(self, agency_id, alias_id):
        """Adds an ``Id`` to an ``Agency`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Agency`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another agency, it is
        reassigned to the given entry ``Id``.

        :param agency_id: the ``Id`` of an ``Agency``
        :type agency_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgencyNotificationSession

    def can_register_for_agency_notifications(self):
        """Tests if this user can register for ``Agency`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_agencies(self):
        """Register for notifications of new agencies.
        ``AgencyReceiver.newAgency()`` is invoked when a new ``Agency``
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_agency_ancestors(self, agency_id):
        """Registers for notification if an ancestor is added to the specified agency in the agency hierarchy.
        ``AgencyReceiver.newAgencyAncestor()`` is invoked when the
        specified agency experiences an addition in ancestry.

        :param agency_id: the ``Id`` of the agency to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_agency_descendants(self, agency_id):
        """Registers for notification if a descendant is added to the specified agency in the agency hierarchy.
        ``AgencyReceiver.newAgencyDescendant()`` is invoked when the
        specified agency experiences an addition in descendants.

        :param agency_id: the ``Id`` of the agency to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_agencies(self):
        """Registers for notification of updated agencies.
        ``AgencyReceiver.changedAgency()`` is invoked when an agency is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_agency(self, agency_id):
        """Registers for notification of an updated agency.
        ``AgencyReceiver.changedAgency()`` is invoked when the specified
        agency is changed.

        :param agency_id: the ``Id`` of the agency to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_agencies(self):
        """Registers for notification of deleted agencies.
        ``AgencyReceiver.deletedAgency()`` is invoked when an agency is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_agency(self, agency_id):
        """Registers for notification of a deleted agency.
        ``AgencyReceiver.deletedAgency()`` is invoked when the specified
        agency is deleted.

        :param agency_id: the ``Id`` of the agency to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_agency_ancestors(self, agency_id):
        """Registers for notification if an ancestor is removed from the specified agency in the agency hierarchy.
        ``AgencyReceiver.deletedAgencyAncestor()`` is invoked when the
        specified agency experiences a removal of an ancestor.

        :param agency_id: the ``Id`` of the agency to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_agency_descendants(self, agency_id):
        """Registers for notification if a descendant is removed from fthe specified agency in the agency hierarchy.
        ``AgencyReceiver.deletedAgencyDescednant()`` is invoked when the
        specified agency experiences a removal of one of its
        descendants.

        :param agency_id: the ``Id`` of the agency to monitor
        :type agency_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgencyHierarchySession

    def get_agency_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    agency_hierarchy_id = property(fget=get_agency_hierarchy_id)

    def get_agency_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    agency_hierarchy = property(fget=get_agency_hierarchy)

    def can_access_agency_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_agency_ids(self):
        """Gets the root agency ``Ids`` in this hierarchy.

        :return: the root agency ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_agency_ids = property(fget=get_root_agency_ids)

    def get_root_agencies(self):
        """Gets the root agencies in this agency hierarchy.

        :return: the root agencies
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_agencies = property(fget=get_root_agencies)

    def has_parent_agencies(self, agency_id):
        """Tests if the ``Agency`` has any parents.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if the agency has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_agency(self, id_, agency_id):
        """Tests if an ``Id`` is a direct parent of an agency.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``agency_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_agency_ids(self, agency_id):
        """Gets the parent ``Ids`` of the given agency.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the agency
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_agencies(self, agency_id):
        """Gets the parents of the given agency.

        :param agency_id: an agency ``Id``
        :type agency_id: ``osid.id.Id``
        :return: the parents of the agency
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_agency(self, id_, agency_id):
        """Tests if an ``Id`` is an ancestor of an agency.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``agency_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_agencies(self, agency_id):
        """Tests if an agency has any children.

        :param agency_id: an ``agency_id``
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if the ``agency_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_agency(self, id_, agency_id):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``agency_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_agency_ids(self, agency_id):
        """Gets the child ``Ids`` of the given agency.

        :param agency_id: the ``Id`` to query
        :type agency_id: ``osid.id.Id``
        :return: the children of the agency
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_agencies(self, agency_id):
        """Gets the children of the given agency.

        :param agency_id: the ``Id`` to query
        :type agency_id: ``osid.id.Id``
        :return: the children of the agency
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_agency(self, id_, agency_id):
        """Tests if an ``Id`` is a descendant of an agency.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``agency_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agency_node_ids(self, agency_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given agency.

        :param agency_id: the ``Id`` to query
        :type agency_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an agency node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agency_nodes(self, agency_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given agency.

        :param agency_id: the ``Id`` to query
        :type agency_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an agency node
        :rtype: ``osid.authentication.AgencyNode``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgencyHierarchyDesignSession

    def can_modify_agency_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_agency(self, agency_id):
        """Adds a root agency.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``agency_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``agency`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_agency(self, agency_id):
        """Removes a root agency from this hierarchy.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agency_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``agency_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_agency(self, agency_id, child_id):
        """Adds a child to an agency.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``agency_id`` already a parent of ``child_id``
        :raise: ``NotFound`` -- ``agency_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_agency(self, agency_id, child_id):
        """Removes a child from an agency.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agency_id is`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``agency_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_agencies(self, agency_id):
        """Removes all children from an agency.

        :param agency_id: the ``Id`` of an agency
        :type agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agency_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class AuthenticationProxyManager(osid_managers.OsidProxyManager, AuthenticationProfile):

    def get_agent_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentLookupSession``
        :rtype: ``osid.authentication.AgentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_lookup_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent lookup service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _agent_lookup_session``
        :rtype: ``osid.authentication.AgentLookupSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentQuerySession``
        :rtype: ``osid.authentication.AgentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_query_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent query service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentQuerySession``
        :rtype: ``osid.authentication.AgentQuerySession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentSearchSession``
        :rtype: ``osid.authentication.AgentSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_search_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent search service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _agent_search_session``
        :rtype: ``osid.authentication.AgentSearchSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agent administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentAdminSession``
        :rtype: ``osid.authentication.AgentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_admin_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent admin service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _agent_admin_session``
        :rtype: ``osid.authentication.AgentAdminSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_notification_session(self, agent_receiver, proxy):
        """Gets the messaging receiver session for notifications pertaining to agent changes.

        :param agent_receiver: the agent receiver
        :type agent_receiver: ``osid.authentication.AgentReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentNotificationSession``
        :rtype: ``osid.authentication.AgentNotificationSession``
        :raise: ``NullArgument`` -- ``proxy`` or ``agent_receiver`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_notification_session_for_agency(self, agent_receiver, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent notification service for the given agency.

        :param agent_receiver: the agent receiver
        :type agent_receiver: ``osid.authentication.AgentReceiver``
        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _agent_notification_session``
        :rtype: ``osid.authentication.AgentNotificationSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agent_receiver, agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_agent_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_agency_session(self, proxy):
        """Gets the session for retrieving agent to agency mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentAgencySession``
        :rtype: ``osid.authentication.AgentAgencySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_agency()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_agency_assignment_session(self, proxy):
        """Gets the session for assigning agent to agency mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentAgencyAssignmentSession``
        :rtype: ``osid.authentication.AgentAgencyAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_agency_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agent_smart_agency_session(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the agent smart agency service for the given agency.

        :param agency_id: the ``Id`` of the bank
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgentSmartAgencySession``
        :rtype: ``osid.authentication.AgentSmartAgencySession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agent_smart_agency()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agency_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agency lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyLookupSession``
        :rtype: ``osid.authentication.AgencyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agency_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agency search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencySearchSession``
        :rtype: ``osid.authentication.AgencySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agency_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the agency administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyAdminSession``
        :rtype: ``osid.authentication.AgencyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agency_notification_session(self, agency_receiver, proxy):
        """Gets the messaging receiver session for notifications pertaining to agency changes.

        :param agency_receiver: the agency receiver
        :type agency_receiver: ``osid.authentication.AgencyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyNotificationSession``
        :rtype: ``osid.authentication.AgencyNotificationSession``
        :raise: ``NullArgument`` -- ``agency_receiver`` or ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agency_hierarchy_session(self, proxy):
        """Gets the session traversing agency hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyHierarchySession``
        :rtype: ``osid.authentication.AgencyHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_agency_hierarchy_design_session(self, proxy):
        """Gets the session designing agency hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AgencyHierarchyDesignSession``
        :rtype: ``osid.authentication.AgencyHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_agency_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authentication_batch_proxy_manager(self):
        """Gets an ``AuthenticationBatchProxyManager``.

        :return: an ``AuthenticationBatchProxyManager``.
        :rtype: ``osid.authentication.batch.AuthenticationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authentication_batch_proxy_manager = property(fget=get_authentication_batch_proxy_manager)

    def get_authentication_keys_proxy_manager(self):
        """Gets an ``AuthenticationKeysProxyManager``.

        :return: an ``AuthenticationKeysProxyManager``.
        :rtype: ``osid.authentication.keys.AuthenticationKeysProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_keys()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authentication_keys_proxy_manager = property(fget=get_authentication_keys_proxy_manager)

    def get_authentication_process_proxy_manager(self):
        """Gets an ``AuthenticationProcessProxyManager``.

        :return: an ``AuthenticationProcessproxyManager``.
        :rtype: ``osid.authentication.process.AuthenticationProcessProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_process()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authentication_process_proxy_manager = property(fget=get_authentication_process_proxy_manager)



class Agency(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_agency_record(self, agency_record_type):
        """Gets the agency record corresponding to the given ``Agency`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``agency_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(agency_record_type)``
        is ``true`` .

        :param agency_record_type: an agency record type
        :type agency_record_type: ``osid.type.Type``
        :return: the agency record
        :rtype: ``osid.authentication.records.AgencyRecord``
        :raise: ``NullArgument`` -- ``agency_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agency_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgentLookupSession

    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    agency_id = property(fget=get_agency_id)

    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    agency = property(fget=get_agency)

    def can_lookup_agents(self):
        """Tests if this user can perform ``Agent`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_agent_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_agent_view(self):
        """A complete view of the ``Agent`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_agency_view(self):
        """Federates the view for methods in this session.
        A federated view will include agents in agencies which are
        children of this agency in the agency hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_agency_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this agency only.



        """
        raise UNIMPLEMENTED()

    def get_agent(self, agent_id):
        """Gets the ``Agent`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Agent`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Agent`` and retained for compatibility.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: the returned ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``NotFound`` -- no ``Agent`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agents_by_ids(self, agent_ids):
        """Gets an ``AgentList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the agents
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Agents`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param agent_ids: a list of agent ``Ids``
        :type agent_ids: ``osid.id.IdList``
        :return: the returned ``Agent list``
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``agent_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agents_by_genus_type(self, agent_genus_type):
        """Gets an ``AgentList`` corresponding to the given agent genus ``Type`` which does not include agents of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_genus_type: an agent genus type
        :type agent_genus_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agents_by_parent_genus_type(self, agent_genus_type):
        """Gets an ``AgentList`` corresponding to the given agent genus ``Type`` and include any additional agents with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_genus_type: an agent genus type
        :type agent_genus_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agents_by_record_type(self, agent_record_type):
        """Gets an ``AgentList`` containing the given agent record ``Type``.
        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_record_type: an agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agents(self):
        """Gets all ``Agents``.
        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :return: a list of ``Agents``
        :rtype: ``osid.authentication.AgentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    agents = property(fget=get_agents)


##
# The following methods are from osid.authentication.AgentQuerySession

    def can_search_agents(self):
        """Tests if this user can perform ``Agent`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_agent_query(self):
        """Gets an agent query.

        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``

        """
        raise UNIMPLEMENTED()

    agent_query = property(fget=get_agent_query)

    def get_agents_by_query(self, agent_query):
        """Gets a list of ``Agents`` matching the given agent query.

        :param agent_query: the agent query
        :type agent_query: ``osid.authentication.AgentQuery``
        :return: the returned ``AgentList``
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agent_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgentSearchSession

    def get_agent_search(self):
        """Gets an agent search.

        :return: the agent search
        :rtype: ``osid.authentication.AgentSearch``

        """
        raise UNIMPLEMENTED()

    agent_search = property(fget=get_agent_search)

    def get_agent_search_order(self):
        """Gets an agent search order.
        The ``AgentSearchOrder`` is supplied to an ``AgentSearch`` to
        specify the ordering of results.

        :return: the agent search order
        :rtype: ``osid.authentication.AgentSearchOrder``

        """
        raise UNIMPLEMENTED()

    agent_search_order = property(fget=get_agent_search_order)

    def get_agents_by_search(self, agent_query, agent_search):
        """Gets the search results matching the given search query using the given search.

        :param agent_query: the agent query
        :type agent_query: ``osid.authentication.AgentQuery``
        :param agent_search: the agent search
        :type agent_search: ``osid.authentication.AgentSearch``
        :return: the returned search results
        :rtype: ``osid.authentication.AgentSearchResults``
        :raise: ``NullArgument`` -- ``agent_query`` or ``agent_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agent_search`` or ``agent_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_agent_query_from_inspector(self, agent_query_inspector):
        """Gets an agent query from an inspector.
        The inspector is available from an ``AgentSearchResults``.

        :param agent_query_inspector: an agent query inspector
        :type agent_query_inspector: ``osid.authentication.AgentQueryInspector``
        :return: the agent query
        :rtype: ``osid.authentication.AgentQuery``
        :raise: ``NullArgument`` -- ``agent_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``agent_query_inspector`` is not of thiss ervice

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgentAdminSession

    def can_create_agents(self):
        """Tests if this user can create ``Agents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Agent``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Agent`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_agent_with_record_types(self, agent_record_types):
        """Tests if this user can create a single ``Agent`` using the desired record types.
        While ``AuthenticationManager.getAgentRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific ``Agent``.
        Providing an empty array tests if an ``Agent`` can be created
        with no records.

        :param agent_record_types: array of agent record types
        :type agent_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Agent`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_agent_form_for_create(self, agent_record_types):
        """Gets the agent form for creating new agents.
        A new form should be requested for each create transaction.

        :param agent_record_types: array of agent record types
        :type agent_record_types: ``osid.type.Type[]``
        :return: the agent form
        :rtype: ``osid.authentication.AgentForm``
        :raise: ``NullArgument`` -- ``agent_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_agent(self, agent_form):
        """Creates a new ``Agent``.

        :param agent_form: the form for this ``Agent``
        :type agent_form: ``osid.authentication.AgentForm``
        :return: the new ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``agent_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``agent_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agent_form`` did not originate from ``get_agent_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_agents(self):
        """Tests if this user can update ``Agents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Agent``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if agent modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_update_agent(self, agent_id):
        """Tests if this user can update a specified agent.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the agent
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer an update
        operation to an unauthorized user for this agent.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: ``false`` if agent modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_agent_form_for_update(self, agent_id):
        """Gets the agent form for updating an existing agent.
        A new agent form should be requested for each update
        transaction.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: the agent form
        :rtype: ``osid.authentication.AgentForm``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_agent(self, agent_form):
        """Updates an existing agent.

        :param agent_form: the form containing the elements to be updated
        :type agent_form: ``osid.authentication.AgentForm``
        :raise: ``IllegalState`` -- ``agent_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``agent_id`` or ``agent_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``agent_form`` did not originate from ``get_agent_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_agents(self):
        """Tests if this user can delete ``Agents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Agent``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Agent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_delete_agent(self, agent_id):
        """Tests if this user can delete a specified ``Agent``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting the
        ``Agent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer a
        delete operation to an unauthorized user for this agent.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: ``false`` if ``Agent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def delete_agent(self, agent_id):
        """Deletes the ``Agent`` identified by the given ``Id`` removing it from all other ``Agencies`` to which this ``Agent`` is associated.

        :param agent_id: the ``Id`` of the ``Agent`` to delete
        :type agent_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Agent`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_agent_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Agents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Agent`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_agent(self, agent_id, alias_id):
        """Adds an ``Id`` to an ``Agent`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Agent`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another engine, it is
        reassigned to the given engine ``Id``.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``agent_id`` not found
        :raise: ``NullArgument`` -- ``agent_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgentNotificationSession

    def can_register_for_agent_notifications(self):
        """Tests if this user can register for ``Agent`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_agents(self):
        """Register for notifications of new agents.
        ``AgentReceiver.newAgent()`` is invoked when a new ``Agent`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_agents(self):
        """Registers for notification of updated agents.
        ``AgentReceiver.changedAgent()`` is invoked when an agent is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_agent(self, agent_id):
        """Registers for notification of an updated agent.
        ``AgentReceiver.changedAgent()`` is invoked when the specified
        agent is changed.

        :param agent_id: the ``Id`` of the ``Agent`` to monitor
        :type agent_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_agents(self):
        """Registers for notification of deleted agents.
        ``AgentReceiver.deletedAgent()`` is invoked when an agent is
        removed from this agency.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_agent(self, agent_id):
        """Registers for notification of a deleted agent.
        ``AgentReceiver.deletedAgent()`` is invoked when the specified
        agent is removed from this agency.

        :param agent_id: the ``Id`` of the ``Agent`` to monitor
        :type agent_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgentAgencySession

    def can_lookup_agent_agency_mappings(self):
        """Tests if this user can perform lookups of agent/agency mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_agency_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_agency_view(self):
        """A complete view of the ``Agent`` and ``Agency`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_agent_ids_by_agency(self, agency_id):
        """Gets the list of ``Agent``  ``Ids`` associated with an ``Agency``.

        :param agency_id: ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: list of related agent ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agents_by_agency(self, agency_id):
        """Gets the list of ``Agents`` associated with an ``Agency``.

        :param agency_id: ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: list of related agents
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NotFound`` -- ``agency_id`` is not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agent_ids_by_agencies(self, agency_ids):
        """Gets the list of ``Agent Ids`` corresponding to a list of ``Agency`` objects.

        :param agency_ids: list of agency ``Ids``
        :type agency_ids: ``osid.id.IdList``
        :return: list of agent ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``agency_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agents_by_agencies(self, agency_ids):
        """Gets the list of ``Agents`` corresponding to a list of ``Agency`` objects.

        :param agency_ids: list of agency ``Ids``
        :type agency_ids: ``osid.id.IdList``
        :return: list of agents
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agency_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agency_ids_by_agent(self, agent_id):
        """Gets the list of ``Agency``  ``Ids`` mapped to an ``Agent``.

        :param agent_id: ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: list of agency ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_agencies_by_agent(self, agent_id):
        """Gets the list of ``Agency`` objects mapped to an ``Agent``.

        :param agent_id: ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: list of agencies
        :rtype: ``osid.authentication.AgencyList``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgentAgencyAssignmentSession

    def can_assign_agents(self):
        """Tests if this user can alter agent/agency mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_agents_to_agency(self, agency_id):
        """Tests if this user can alter agent/agency mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_agency_ids(self, agency_id):
        """Gets a list of agencies including and under the given agency node in which any agent can be assigned.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :return: list of assignable agency ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_agency_ids_for_agent(self, agency_id, agent_id):
        """Gets a list of agencies including and under the given agency node in which a specific agent can be assigned.

        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: list of assignable bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``agency_id`` or ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_agent_to_agency(self, agent_id, agency_id):
        """Adds an existing ``Agent`` to an ``Agency``.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``agent_id`` is already assigned to ``agency_id``
        :raise: ``NotFound`` -- ``agent_id`` or ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agent_id`` or ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_agent_from_agency(self, agent_id, agency_id):
        """Removes an ``Agent`` from an ``Agency``.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param agency_id: the ``Id`` of the ``Agency``
        :type agency_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agent_id`` or ``agency_id`` not found or ``agent_id`` not assigned to ``agency_id``
        :raise: ``NullArgument`` -- ``agent_id`` or ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.authentication.AgentSmartAgencySession

    def can_manage_smart_agencies(self):
        """Tests if this user can manage smart agencies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart agency management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_agent_query(self, agent_query):
        """Applies an agent query to this agency.

        :param agent_query: the agent query
        :type agent_query: ``osid.authentication.AgentQuery``
        :raise: ``NullArgument`` -- ``agent_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``agent_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_agent_query(self):
        """Gets an agent query inspector for this agency.

        :return: the agent query inspector
        :rtype: ``osid.authentication.AgentQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_agent_sequencing(self, agent_search_order):
        """Applies an agent search order to this agency.

        :param agent_search_order: the agent search order
        :type agent_search_order: ``osid.authentication.AgentSearchOrder``
        :raise: ``NullArgument`` -- ``agent_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``agent_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class AgencyList(osid_objects.OsidList):

    def get_next_agency(self):
        """Gets the next ``Agency`` in this list.

        :return: the next ``Agency`` in this list. The ``has_next()`` method should be used to test that a next ``Agency`` is available before calling this method.
        :rtype: ``osid.authentication.Agency``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_agency = property(fget=get_next_agency)

    def get_next_agencies(self, n):
        """Gets the next set of ``Agency`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Agency`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Agency`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authentication.Agency``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Agencies(AuthenticationManager):
    pass


