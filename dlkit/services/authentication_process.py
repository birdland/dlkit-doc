# -*- coding: utf-8 -*-
"""Authentication Process Open Service Interface Definitions
authentication.process version 3.0.0

The Authentication Process OSID conducts an authentication process.

Authentication Process

The Authentication OSID helps an OSID Consumer acquire and validate
authentication credentials without having to manage the details of a
particular authentication environment. Authentication is generally a two
step process. A user wishing to authenticate acquires a set of
credentials and transports those credentials to a remote peer. The
remote peer then validates those credentials and determines the identity
of the user represented. This process is reflected in the Authentication
OSID with the definition of two OSID sessions:

  * ``AuthenticationAcquisitionSession:`` A session to acquire
    credentials from a user and serialize them for transport to a remote
    peer for authentication.
  * ``AuthenticationValidationSession:`` A session to receive and
    validate authentication credentials from a remote peer wishing to
    authenticate.


The transport of authentication credentials is the responsibility of the
consumer of the Authentication OSID as authentication generally supports
an existing application protocol enviornment. Methods exist to extract
and supply credentials at each end. An Authentication OSID Provider may
support either or both sessions, and one or more credential formats.
Methods also exist to support a challenge-response mechanism.

Circle of Trust

In the Authorization OSID, Authorizations may be managed for a set of
Agents related to a Resource. The set of ``Agents`` may be filtered
based on the level of confidence upon the authentication mechanism. A
``Trust`` is a category of ``Agents`` produced from an authentication
mechanism that represent a level of confidence on which to specify an
Authorization.

``Trusts`` are not explicitly managed in the Authentication Process
OSID. They serve to facilitate the orchestration between an
Authentication OSID Provider and an Authorization OSID Provider. An
Authorization OSID Provider may query the ``CircleOfTrustSession`` to
determine if an ``Agent`` it has received belongs to a ``Trust``
specified in one of its Authorizations.

For example, an ``Authorization`` may be created by specifying a
``Resource``. The ``Resource`` may be an individual person or a group of
employees. While employees might be authorized to read their company
email using their GMail account, requisitions in the ERP system must be
made using the company authentication system and even perhaps a specific
specific type of credential. An ``Authorization`` can be created for a
set of employees based but restricted to a ``Trust`` where the Trust
represents any ``Agent`` related to the set of employees that have
authenticated in the desired fashion.

The multiplicity of ``Agents`` per Resource as aell as the alignment
with an Authorization OSID Provider is a consideration in the design of
an Authentication OSID Provider. It does only identify the
authentication principal as a singular entity, but may also represent
something about the authentication style that is used to perform an
authorization.

Examples

Client side authentication:
  if (manager.supportsAuthenticationAcquisition() &amp;&amp;
      manager.supportsAcquisitionInputType(krb5ServiceType) &amp;&amp;
      manager.supportsCredentialType(serialKRB5Type)) {
      AuthenticationAcquisitionSession aas = manager.getAuthenticationAcquisitionSession();
  
      // specify input parameters (interface extension)
      KRB5Service kService = new KRB5Service();
      kService.setName("host");
      kService.setInstance("server.osid.org");
      kService.setRealm("OSID.ORG");
  
      // get Credential (interface type) 
      Authentication auth = aas.getAuthentication(kService, krb5ServiceType);
      SerializedKRB5Ticket ticket = (SerializedKRB5Ticket)        auth.getCredential(serialKRB5Type);
      send_data_to_peer(ticket); // app specific protocol
  }





Server side authentication:
  if (manager.supportsAuthenticationValidation() &amp;&amp;
      manager.supportsCredentialType(serialSAML2Type)) {
      AuthenticationValidationSession avs = manager.getAuthenticationValidationSession();
  
      Authentication auth = authenticate(SAML2Token, serialSAML2Type);
  
      if (auth.isValid()) {
          Agent agent = auth.getAgent(); // identity established
      }
  }



"""

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



