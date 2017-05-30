
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


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


