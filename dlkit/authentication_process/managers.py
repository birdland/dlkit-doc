
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions


class AuthenticationProcessProfile(osid_managers.OsidProfile):
    """The ``AuthenticationProcessProfile`` describes the interoperability among authentication process services."""

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




