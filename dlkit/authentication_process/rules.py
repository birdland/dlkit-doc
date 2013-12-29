from ..osid import rules as osid_rules


class AuthenticationInput(osid_rules.OsidCondition):
    """An authorization condition interface."""
    def get_authentication_input_record(self, authentication_input_record_type):
        """Gets the record corresponding to the given ``AuthenticationInput`` record ``Type``.

        This method must be used to retrieve an object implementing the
        requested record interface along with all of its ancestor
        interfaces. The ``authentication_input_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(authentication_input_record_type)`` is
        ``true`` .

        :param authentication_input_record_type: an authentication input record type
        :type authentication_input_record_type: ``osid.type.Type``
        :return: the authentication input record
        :rtype: ``osid.authentication.process.records.AuthenticationInputRecord``
        :raise: ``NullArgument`` -- ``authentication_input_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(authentication_input_record_type)`` is ``false``

        """
        return # osid.authentication.process.records.AuthenticationInputRecord


