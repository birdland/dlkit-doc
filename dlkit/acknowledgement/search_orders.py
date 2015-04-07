from ..osid import search_orders as osid_search_orders


class CreditSearchOrder(osid_search_orders.OsidRelationshipSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_reference(self, style):
        """Specifies a preference for ordering the result set by the reference.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_resource(self, style):
        """Specifies a preference for ordering the result set by the resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_resource_search_order(self):
        """Tests if a resource search order is available.

        :return: ``true`` if a resource search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_resource_search_order(self):
        """Gets the resource search order.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_resource_search_order()`` is ``false``

        """
        return # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    def get_credit_search_order_record(self, credit_record_type):
        """Gets the credit search order record corresponding to the given credit record ``Type``.

        Multiple retrievals return the same underlying object.

        :param credit_record_type: a credit record type
        :type credit_record_type: ``osid.type.Type``
        :return: the credit search order record
        :rtype: ``osid.acknowledgement.records.CreditSearchOrderRecord``
        :raise: ``NullArgument`` -- ``credit_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(credit_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.CreditSearchOrderRecord


class BillingSearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_billing_search_order_record(self, billing_record_type):
        """Gets the billing search record order corresponding to the given billing record Type.

        Multiple retrievals return the same underlying object.

        :param billing_record_type: a billing record type
        :type billing_record_type: ``osid.type.Type``
        :return: the billing search order record
        :rtype: ``osid.acknowledgement.records.BillingSearchOrderRecord``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(billing_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.BillingSearchOrderRecord


