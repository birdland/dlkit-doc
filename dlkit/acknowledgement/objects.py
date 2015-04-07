from ..osid import objects as osid_objects


class Credit(osid_objects.OsidRelationship):
    """A ``Credit`` relates a ``Resource`` with a reference to an ``Id``."""
    def get_reference_id(self):
        """Gets the ``Id`` of the referenced object.

        :return: the reference ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    reference_id = property(fget=get_reference_id)

    def get_resource_id(self):
        """Gets the ``Id`` of the resource in this credit.

        :return: the ``Resource``  ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the resource in this credit.

        :return: the ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    resource = property(fget=get_resource)

    def get_credit_record(self, credit_record_type):
        """Gets the record corresponding to the given ``Credit`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``credit_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(credit_record_type)``
        is ``true`` .

        :param credit_record_type: the type of credit record to retrieve
        :type credit_record_type: ``osid.type.Type``
        :return: the credit record
        :rtype: ``osid.acknowledgement.records.CreditRecord``
        :raise: ``NullArgument`` -- ``credit_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(credit_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.CreditRecord


class CreditForm(osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Credit`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CreditAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_credit_form_record(self, credit_record_type):
        """Gets the ``CreditFormRecord`` interface corresponding to the given credit record ``Type``.

        :param credit_record_type: the credit record type
        :type credit_record_type: ``osid.type.Type``
        :return: the record
        :rtype: ``osid.acknowledgement.records.CreditFormRecord``
        :raise: ``NullArgument`` -- ``credit_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(credit_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.CreditFormRecord


class CreditList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CreditList`` provides a means for accessing ``Credit`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Credit credit = cl.getNextCredit();
    }

    or
      while (cl.hasNext()) {
           Credit[] credits = cl.getNextCredits(cl.available());
      }
    


    """
    def get_next_credit(self):
        """Gets the next ``Credit`` in this list.

        :return: the next ``Credit`` in this list. The ``has_next()`` method should be used to test that a next ``Credit`` is available before calling this method.
        :rtype: ``osid.acknowledgement.Credit``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.acknowledgement.Credit

    next_credit = property(fget=get_next_credit)

    def get_next_credits(self, n):
        """Gets the next set of ``Credit`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Credit`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Credit`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.acknowledgement.Credit``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.acknowledgement.Credit


class Billing(osid_objects.OsidCatalog):
    """A ``Billing`` represents a collection of credits.

    Like all OSID objects, a ``Billing`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    def get_billing_record(self, billing_record_type):
        """Gets the record corresponding to the given ``Billing`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``billing_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(billing_record_type)`` is ``true`` .

        :param billing_record_type: the type of billing record to retrieve
        :type billing_record_type: ``osid.type.Type``
        :return: the billing record
        :rtype: ``osid.acknowledgement.records.BillingRecord``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(billing_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.BillingRecord


class BillingForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Billings``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``BillingAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_billing_form_record(self, billing_record_type):
        """Gets the ``BillingFormRecord`` interface corresponding to the given billing record ``Type``.

        :param billing_record_type: the billing record type
        :type billing_record_type: ``osid.type.Type``
        :return: the record
        :rtype: ``osid.acknowledgement.records.BillingFormRecord``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(billing_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.BillingFormRecord


class BillingList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BillingList`` provides a means for accessing ``Billing`` elements sequentially either one at a time or many at a time.

    Examples: while (bl.hasNext()) { Billing billing =
    bl.getNextBilling(); }

    or
      while (bl.hasNext()) {
           Billing[] billing = bl.getNextBillings(bl.available());
      }
    


    """
    def get_next_billing(self):
        """Gets the next ``Billing`` in this list.

        :return: the next ``Billing`` in this list. The ``has_next()`` method should be used to test that a next ``Billing`` is available before calling this method.
        :rtype: ``osid.acknowledgement.Billing``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.acknowledgement.Billing

    next_billing = property(fget=get_next_billing)

    def get_next_billings(self, n):
        """Gets the next set of ``Billing`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Billing`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Billing`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.acknowledgement.Billing``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.acknowledgement.Billing


class BillingNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BillingHierarchySession``.

    """
    def get_billing(self):
        """Gets the ``Billing`` at this node.

        :return: the billing represented by this node
        :rtype: ``osid.acknowledgement.Billing``

        """
        return # osid.acknowledgement.Billing

    billing = property(fget=get_billing)

    def get_parent_billing_nodes(self):
        """Gets the parents of this billing.

        :return: the parents of this billing
        :rtype: ``osid.acknowledgement.BillingNodeList``

        """
        return # osid.acknowledgement.BillingNodeList

    parent_billing_nodes = property(fget=get_parent_billing_nodes)

    def get_child_billing_nodes(self):
        """Gets the children of this billing.

        :return: the children of this billing
        :rtype: ``osid.acknowledgement.BillingNodeList``

        """
        return # osid.acknowledgement.BillingNodeList

    child_billing_nodes = property(fget=get_child_billing_nodes)


class BillingNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BillingNodeList`` provides a means for accessing ``BillingNode`` elements sequentially either one at a time or many at a time.

    Examples: while (bnl.hasNext()) { BillingNode node =
    bnl.getNextBillingNode(); }

    or
      while (bnl.hasNext()) {
           BillingNode[] nodes = bnl.getNextBillingNodes(bnl.available());
      }
    


    """
    def get_next_billing_node(self):
        """Gets the next ``BillingNode`` in this list.

        :return: the next ``BillingNode`` in this list. The ``has_next()`` method should be used to test that a next ``BillingNode`` is available before calling this method.
        :rtype: ``osid.acknowledgement.BillingNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.acknowledgement.BillingNode

    next_billing_node = property(fget=get_next_billing_node)

    def get_next_billing_nodes(self, n):
        """Gets the next set of ``BillingNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``BillingNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``BillingNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.acknowledgement.BillingNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.acknowledgement.BillingNode


