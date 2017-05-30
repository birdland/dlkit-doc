
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import records as osid_records


class AuthenticationProcessProfile(osid_managers.OsidProfile):
    """The ``AuthenticationProcessProfile`` describes the interoperability among authentication process services."""

    def __init__(self):
        self._provider_manager = None


    def get_authentication_record_types(self):
        """Gets the supported authentication record types.

        :return: a list containing the supported authentication record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    authentication_record_types = property(fget=get_authentication_record_types)

    def get_authentication_input_record_types(self):
        """Gets the supported authentication input record types.

        :return: a list containing the supported authentication input record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    authentication_input_record_types = property(fget=get_authentication_input_record_types)

    def get_challenge_record_types(self):
        """Gets the supported challenge types.

        :return: a list containing the supported challenge types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    challenge_record_types = property(fget=get_challenge_record_types)

    def get_credential_types(self):
        """Gets the supported credential types.

        :return: a list containing the supported credential types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    credential_types = property(fget=get_credential_types)

    def get_trust_types(self):
        """Gets the supported trust types.

        :return: a list containing the supported trust types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    trust_types = property(fget=get_trust_types)


class AuthenticationProcessManager(osid_managers.OsidManager, osid_sessions.OsidSession, AuthenticationProcessProfile):
    """The authentication process manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``AuthenticationAcquisitionSession:`` a session to acquire
        credentials from a user and serialize them for transport to a
        remote peer for authentication
      * ``AuthenticationValidationSession: a`` session to receive and
        validate authentication credentials from a remote peer wishing
        to authenticate
      * ``TrustLookupSession:`` a session to look up authentication
        circles of trust
      * ``CircleOfTrustSession:`` a session to examine agent circles of
        trust

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
        parameter_id = Id('parameter:authentication_processProviderImpl@dlkit_service')
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




class AuthenticationProcessProxyManager(osid_managers.OsidProxyManager, AuthenticationProcessProfile):
    """The authentication process proxy manager provides access to authentication sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` object.
    The sessions included in this manager are:

      * ``AuthenticationAcquisitionSession:`` session to acquire
        credentials from a user and serialize them for transport to a
        remote peer for authentication
      * ``AuthenticationValidationSession:`` session to receive and
        validate authentication credentials from a remote peer wishing
        to authenticate
      * ``TrustLookupSession:`` a session to look up authentication
        circles of trust
      * ``CircleOfTrustSession:`` a session to examine agent circles of
        trust

    """
    pass



