
from ..osid import objects as osid_objects


class Authentication(osid_objects.OsidObject):
    """``Authentication`` represents an authentication credential which contains set of ``bytes`` and a format Type.

    Once an ``Authentication`` is created from the
    ``AuthenticationValidationSession,`` the credential data can be
    extracted and sent to the remote peer for validation. The remote
    peer gets another ``Authentication`` object as a result of
    validating the serialized credential data.

    An ``Authentication`` may or may not be valid. ``is_valid()`` should
    be checked before acting upon the ``Agent`` identity to which the
    credential is mapped.

    """

    def get_agent_id(self):
        """Gets the ``Id`` of the ``Agent`` identified in this authentication credential.

        :return: the ``Agent Id``
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: The Agent should be determined at the
        time this credential is created.

        """
        return # osid.id.Id

    agent_id = property(fget=get_agent_id)

    def get_agent(self):
        """Gets the ``Agent`` identified in this authentication credential.

        :return: the ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    agent = property(fget=get_agent)

    def is_valid(self):
        """Tests whether or not the credential represented by this ``Authentication`` is currently valid.

        A credential may be invalid because it has been destroyed,
        expired, or is somehow no longer able to be used.

        :return: ``true`` if this authentication credential is valid, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: Any problem in determining the validity
        of this credential should result in ``false``.

        """
        return # boolean

    def has_expiration(self):
        """Tests if this authentication has an expiration.

        :return: ``true`` if this authentication has an expiration, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_expiration(self):
        """Gets the expiration date associated with this authentication credential.

        Consumers should check for the existence of a an expiration
        mechanism via ``hasExpiration()``.

        :return: the expiration date of this authentication credential
        :rtype: ``timestamp``
        :raise: ``IllegalState`` -- ``has_expiration()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # timestamp

    expiration = property(fget=get_expiration)

    def has_credential(self):
        """Tests if this authentication has a credential for export.

        :return: ``true`` if this authentication has a credential, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_credential(self, credential_type):
        """Gets the credential represented by the given ``Type`` for transport to a remote service.

        :param credential_type: the credential format ``Type``
        :type credential_type: ``osid.type.Type``
        :return: the credential
        :rtype: ``object``
        :raise: ``IllegalState`` -- ``has_credential()`` is ``false``
        :raise: ``NullArgument`` -- ``credential_type`` is ``null``
        :raise: ``Unsupported`` -- the given ``credential_type`` is not supported

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: A provider may support multiple
        credential formats for a variety of applications.

        """
        return # object

    def get_authentication_record(self, authentication_record_type):
        """Gets the authentication record corresponding to the given authentication record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``authentication_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(authentication_record_type)`` is ``true`` .

        :param authentication_record_type: the type of authentication record to retrieve
        :type authentication_record_type: ``osid.type.Type``
        :return: the authentication record
        :rtype: ``osid.authentication.process.records.AuthenticationRecord``
        :raise: ``NullArgument`` -- ``authentication_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(authenticaton_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.process.records.AuthenticationRecord


