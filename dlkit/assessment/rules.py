
from ..osid import rules as osid_rules


class Response(osid_rules.OsidCondition):
    """A response to an assessment item.


    This interface contains methods to set values in response to an
    assessmet item and mirrors the item record structure with the
    corresponding setters.


    """

    def get_item_id(self):
        """Gets the ``Id`` of the ``Item``.


        :return: the assessment item ``Id``
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    item_id = property(fget=get_item_id)

    def get_item(self):
        """Gets the ``Item``.


        :return: the assessment item
        :rtype: ``osid.assessment.Item``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.assessment.Item

    item = property(fget=get_item)

    def get_response_record(self, item_record_type):
        """Gets the response record corresponding to the given ``Item`` record ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``item_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(item_record_type)``
        is ``true`` .


        :param item_record_type: an item record type
        :type item_record_type: ``osid.type.Type``
        :return: the response record
        :rtype: ``osid.assessment.records.ResponseRecord``
        :raise: ``NullArgument`` -- ``item_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(item_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.assessment.records.ResponseRecord


