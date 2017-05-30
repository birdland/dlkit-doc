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

    def __init__(self):
        self._provider_manager = None


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

    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._agency_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_agency_view(self, session):
        """Sets the underlying agency view to match current view"""
        if self._agency_view == COMPARATIVE:
            try:
                session.use_comparative_agency_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_agency_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_agency_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                proxy=self._proxy,
                                                manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:authenticationProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('AUTHENTICATION', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('AUTHENTICATION', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()

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


