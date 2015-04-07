from ..osid import queries as osid_queries


class CreditQuery(osid_queries.OsidRelationshipQuery):
    """This is the query for searching credits.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_reference_id(self, reference_id, match):
        """Sets reference ``Id``.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``

        """
        pass

    def clear_reference_id_terms(self):
        """Clears all reference ``Id`` terms."""
        pass

    reference_id_terms = property(fdel=clear_reference_id_terms)

    def match_resource_id(self, resource_id, match):
        """Sets a resource ``Id``.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        pass

    def clear_resource_id_terms(self):
        """Clears all resource ``Id`` terms."""
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_resource_query(self):
        """Gets the query for a resource query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    def clear_resource_terms(self):
        """Clears all resource terms."""
        pass

    resource_terms = property(fdel=clear_resource_terms)

    def match_billing_id(self, billing_id, match):
        """Sets the billing ``Id`` for this query to match credits assigned to billings.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``

        """
        pass

    def clear_billing_id_terms(self):
        """Clears all billing ``Id`` terms."""
        pass

    billing_id_terms = property(fdel=clear_billing_id_terms)

    def supports_billing_query(self):
        """Tests if a ``BillingQuery`` is available.

        :return: ``true`` if a billing query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_billing_query(self):
        """Gets the query for a billing query.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the billing query
        :rtype: ``osid.acknowledgement.BillingQuery``
        :raise: ``Unimplemented`` -- ``supports_billing_query()`` is ``false``

        """
        return # osid.acknowledgement.BillingQuery

    billing_query = property(fget=get_billing_query)

    def clear_billing_terms(self):
        """Clears all billing terms."""
        pass

    billing_terms = property(fdel=clear_billing_terms)

    def get_credit_query_record(self, credit_record_type):
        """Gets the credit query record corresponding to the given ``Credit`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param credit_record_type: a credit record type
        :type credit_record_type: ``osid.type.Type``
        :return: the credit query record
        :rtype: ``osid.acknowledgement.records.CreditQueryRecord``
        :raise: ``NullArgument`` -- ``credit_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(credit_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.CreditQueryRecord


class BillingQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching for billings.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_credit_id(self, credit_id, match):
        """Sets the credit ``Id`` for this query to match credits assigned to billings.

        :param credit_id: a credit ``Id``
        :type credit_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``

        """
        pass

    def clear_credit_id_terms(self):
        """Clears all credit ``Id`` terms."""
        pass

    credit_id_terms = property(fdel=clear_credit_id_terms)

    def supports_credit_query(self):
        """Tests if a credit query is available.

        :return: ``true`` if a credit query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_credit_query(self):
        """Gets the query for a billing.

        :return: the credit query
        :rtype: ``osid.acknowledgement.CreditQuery``
        :raise: ``Unimplemented`` -- ``supports_credit_query()`` is ``false``

        """
        return # osid.acknowledgement.CreditQuery

    credit_query = property(fget=get_credit_query)

    def match_any_credit(self, match):
        """Matches billings with any credit.

        :param match: ``true`` to match billings with any credit, ``false`` to match billings with no credits
        :type match: ``boolean``

        """
        pass

    def clear_credit_terms(self):
        """Clears all credit terms."""
        pass

    credit_terms = property(fdel=clear_credit_terms)

    def match_ancestor_billing_id(self, billing_id, match):
        """Sets the billing ``Id`` for this query to match billings that have the specified billing as an ancestor.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``

        """
        pass

    def clear_ancestor_billing_id_terms(self):
        """Clears all ancestor billing ``Id`` terms."""
        pass

    ancestor_billing_id_terms = property(fdel=clear_ancestor_billing_id_terms)

    def supports_ancestor_billing_query(self):
        """Tests if a ``BillingQuery`` is available.

        :return: ``true`` if a billing query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_billing_query(self):
        """Gets the query for a billing.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the billing query
        :rtype: ``osid.acknowledgement.BillingQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_billing_query()`` is ``false``

        """
        return # osid.acknowledgement.BillingQuery

    ancestor_billing_query = property(fget=get_ancestor_billing_query)

    def match_any_ancestor_billing(self, match):
        """Matches billings with any ancestor.

        :param match: ``true`` to match billings with any ancestor, ``false`` to match root billings
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_billing_terms(self):
        """Clears all ancestor billing terms."""
        pass

    ancestor_billing_terms = property(fdel=clear_ancestor_billing_terms)

    def match_descendant_billing_id(self, billing_id, match):
        """Sets the billing ``Id`` for this query to match billings that have the specified billing as a descendant.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``

        """
        pass

    def clear_descendant_billing_id_terms(self):
        """Clears all descendant billing ``Id`` terms."""
        pass

    descendant_billing_id_terms = property(fdel=clear_descendant_billing_id_terms)

    def supports_descendant_billing_query(self):
        """Tests if a ``BillingQuery`` is available.

        :return: ``true`` if a billing query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_billing_query(self):
        """Gets the query for a billing.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the billing query
        :rtype: ``osid.acknowledgement.BillingQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_billing_query()`` is ``false``

        """
        return # osid.acknowledgement.BillingQuery

    descendant_billing_query = property(fget=get_descendant_billing_query)

    def match_any_descendant_billing(self, match):
        """Matches billings with any descendant.

        :param match: ``true`` to match billings with any descendant, ``false`` to match leaf billings
        :type match: ``boolean``

        """
        pass

    def clear_descendant_billing_terms(self):
        """Clears all descendant billing terms."""
        pass

    descendant_billing_terms = property(fdel=clear_descendant_billing_terms)

    def get_billing_query_record(self, billing_record_type):
        """Gets the record query corresponding to the given ``Billing`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        :param billing_record_type: a billing record type
        :type billing_record_type: ``osid.type.Type``
        :return: the billing query record
        :rtype: ``osid.acknowledgement.records.BillingQueryRecord``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(billing_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.BillingQueryRecord


