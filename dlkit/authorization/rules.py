from ..osid import rules as osid_rules


class AuthorizationCondition(osid_rules.OsidCondition):
    """An authorization condition interface."""
    def get_authorization_condition_record(self, authorization_condition_record_type):
        """Gets the authorization condition record corresponding to the given ``AuthorizationCondition`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``authorization_condition_record_type``
        may be the ``Type`` returned in ``get_condition_record_types()``
        or any of its parents in a ``Type`` hierarchy where
        ``has_condition_record_typ
        e(authorization_condition_record_type)`` is ``true`` .

        :param authorization_condition_record_type: an authorization condition record type
        :type authorization_condition_record_type: ``osid.type.Type``
        :return: the authorization condition record
        :rtype: ``osid.authorization.records.AuthorizationConditionRecord``
        :raise: ``NullArgument`` -- ``authorization_condition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(authorization_condition_record_type)`` is ``false``

        """
        return # osid.authorization.records.AuthorizationConditionRecord


