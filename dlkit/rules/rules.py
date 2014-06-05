from ..osid import rules as osid_rules


class Condition(osid_rules.OsidCondition):
    """The ``Condition`` is used to input conditions into a rule execution."""
    def get_condition_record(self, condition_record_type):
        """Gets the condition record corresponding to the given ``Condition`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``condition_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(condition_record_type)`` is ``true`` .

        :param condition_record_type: the type of condition record to retrieve
        :type condition_record_type: ``osid.type.Type``
        :return: the condition record
        :rtype: ``osid.rules.records.ConditionRecord``
        :raise: ``NullArgument`` -- ``condition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_condition_record_type(condition_record_type)`` is ``false``

        """
        return # osid.rules.records.ConditionRecord


class Result(osid_rules.OsidResult):
    """The ``Result`` is the output of a rule execution."""
    def get_boolean_value(self):
        """Gets a boolean result from the rule evaluation.

        Based on the definition of the Rule, the result may be a simple
        boolean value or something more complex defined in the record
        type.

        :return: ``true`` or ``false``
        :rtype: ``boolean``

        """
        return # boolean

    boolean_value = property(fget=get_boolean_value)

    def get_result_record(self, result_record_type):
        """Gets the result record corresponding to the given ``ResultRecord`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``result_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(result_record_type)``
        is ``true`` .

        :param result_record_type: the type of result record to retrieve
        :type result_record_type: ``osid.type.Type``
        :return: the result record
        :rtype: ``osid.rules.records.ResultRecord``
        :raise: ``NullArgument`` -- ``result_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(result_record_type)`` is ``false``

        """
        return # osid.rules.records.ResultRecord


