from ..osid import rules as osid_rules


class ValueCondition(osid_rules.OsidCondition):
    """A value condition interface."""
    def get_value_condition_record(self, value_condition_record_type):
        """Gets the record corresponding to the given ``ValueCondition`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``value_condition_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(value_condition_record_type)`` is ``true`` .

        :param value_condition_record_type: a value condition record type
        :type value_condition_record_type: ``osid.type.Type``
        :return: the value condition record
        :rtype: ``osid.configuration.records.ValueConditionRecord``
        :raise: ``NullArgument`` -- ``value_condition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(value_condition_record_type)`` is ``false``

        """
        return # osid.configuration.records.ValueConditionRecord


