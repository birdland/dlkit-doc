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
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..process import managers as process_managers
from ..osid import sessions as osid_sessions


class AuthenticationProcessProfile(osid_managers.OsidProfile):

    def supports_authentication_acquisition(self):
        """Tests if authentication acquisition is supported.
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

    def supports_trust_lookup(self):
        """Tests if a trust look up session is supported.

        :return: ``true`` if trust lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_circle_of_trust(self):
        """Tests if a session to examine agent and trust relationships is supported.

        :return: ``true`` if a circle of trust is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_challenge(self):
        """Tests if this authentication service supports a challenge- response mechanism where credential validation service must implement a means to generate challenge data.

        :return: ``true`` if this is a challenge-response system, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_authentication_record_types(self):
        """Gets the supported authentication record types.

        :return: a list containing the supported authentication record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    authentication_record_types = property(fget=get_authentication_record_types)

    def supports_authentication_record_type(self, authentication_record_type):
        """Tests if the given authentication record type is supported.

        :param authentication_record_type: a ``Type`` indicating an authentication record type
        :type authentication_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authentication_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_authentication_input_record_types(self):
        """Gets the supported authentication input record types.

        :return: a list containing the supported authentication input record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    authentication_input_record_types = property(fget=get_authentication_input_record_types)

    def supports_authentication_input_record_type(self, authentication_input_record_type):
        """Tests if the given authentication input record type is supported.

        :param authentication_input_record_type: a ``Type`` indicating an authentication input record type
        :type authentication_input_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``authentication_input_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_challenge_record_types(self):
        """Gets the supported challenge types.

        :return: a list containing the supported challenge types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    challenge_record_types = property(fget=get_challenge_record_types)

    def supports_challenge_record_type(self, challenge_record_type):
        """Tests if the given challenge data type is supported.

        :param challenge_record_type: a ``Type`` indicating a challenge record type
        :type challenge_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``challenge_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def supports_credential_export(self):
        """Tests if ``Authentication`` objects can export serialzied credentials for transport.

        :return: ``true`` if the given credentials export is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_credential_types(self):
        """Gets the supported credential types.

        :return: a list containing the supported credential types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    credential_types = property(fget=get_credential_types)

    def supports_credential_type(self, credential_type):
        """Tests if the given credential type is supported.

        :param credential_type: a ``Type`` indicating a credential type
        :type credential_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``credential_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_trust_types(self):
        """Gets the supported trust types.

        :return: a list containing the supported trust types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    trust_types = property(fget=get_trust_types)

    def supports_trust_type(self, trust_type):
        """Tests if the given trust type is supported.

        :param trust_type: a ``Type`` indicating a trust type
        :type trust_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``trust_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class AuthenticationProcessManager(osid_managers.OsidManager, osid_sessions.OsidSession, process_managers.AuthenticationProcessProfile):

    def get_authentication_acquisition_session(self):
        """Gets an ``AuthenticationAcquisitionSession`` which is responsible for acquiring authentication credentials on behalf of a service client.

        :return: an acquisition session for this service
        :rtype: ``osid.authentication.process.AuthenticationAcquisitionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_acquisition()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authentication_acquisition_session = property(fget=get_authentication_acquisition_session)

    def get_authentication_validation_session(self):
        """Gets the ``OsidSession`` associated with the ``AuthenticationValidation`` service.

        :return: an ``AuthenticationValidationSession``
        :rtype: ``osid.authentication.process.AuthenticationValidationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_validation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    authentication_validation_session = property(fget=get_authentication_validation_session)

    def get_trust_lookup_session(self):
        """Gets the ``OsidSession`` associated with the trust lookup service.

        :return: a ``TrustLookupSession``
        :rtype: ``osid.authentication.process.TrustLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_trust_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    trust_lookup_session = property(fget=get_trust_lookup_session)

    def get_trust_lookup_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the trust lookup service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: a ``TrustLookupSession``
        :rtype: ``osid.authentication.process.TrustLookupSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_trust_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_circle_of_trust_session(self):
        """Gets the ``OsidSession`` associated with the trust circle service.

        :return: a ``CircleOfTrustSession``
        :rtype: ``osid.authentication.process.CircleOfTrustSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_circle_of_trust()`` is ``false``

        """
        raise UNIMPLEMENTED()

    circle_of_trust_session = property(fget=get_circle_of_trust_session)

    def get_circle_of_trust_session_for_agency(self, agency_id):
        """Gets the ``OsidSession`` associated with the trust circle service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :return: a ``CircleOfTrustSession``
        :rtype: ``osid.authentication.process.CircleOfTrustSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_ciirle_of_trust()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()



class AuthenticationProcessProxyManager(osid_managers.OsidProxyManager, process_managers.AuthenticationProcessProfile):

    def get_authentication_acquisition_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``AuthenticationAcquisitionSession`` using the supplied ``Authentication``.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthenticationAcquisitionSession``
        :rtype: ``osid.authentication.process.AuthenticationAcquisitionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_acquisition()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_authentication_validation_session(self, proxy):
        """Gets the ``OsidSession`` associated with the ``AuthenticationValidation`` service using the supplied ``Authentication``.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``AuthenticationValidationSession``
        :rtype: ``osid.authentication.process.AuthenticationValidationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_authentication_validation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_trust_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the trust lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TrustLookupSession``
        :rtype: ``osid.authentication.process.TrustLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_trust_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_trust_lookup_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the trust lookup service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TrustLookupSession``
        :rtype: ``osid.authentication.process.TrustLookupSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_trust_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_circle_of_trust_session(self, proxy):
        """Gets the ``OsidSession`` associated with the trust circle service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CircleOfTrustSession``
        :rtype: ``osid.authentication.process.CircleOfTrustSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_circle_of_trust()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_circle_of_trust_session_for_agency(self, agency_id, proxy):
        """Gets the ``OsidSession`` associated with the trust circle service for the given agency.

        :param agency_id: the ``Id`` of the agency
        :type agency_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CircleOfTrustSession``
        :rtype: ``osid.authentication.process.CircleOfTrustSession``
        :raise: ``NotFound`` -- ``agency_id`` not found
        :raise: ``NullArgument`` -- ``agency_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_ciirle_of_trust()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()



class Agencies(Authentication.ProcessManager):
    pass


