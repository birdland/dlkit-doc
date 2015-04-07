from ..osid import query_inspectors as osid_query_inspectors


class CreditQueryInspector(osid_query_inspectors.OsidRelationshipQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    def get_reference_id_terms(self):
        """Gets the reference ``Id`` query terms.

        :return: the reference ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    reference_id_terms = property(fget=get_reference_id_terms)

    def get_resource_id_terms(self):
        """Gets the resource ``Id`` query terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    resource_id_terms = property(fget=get_resource_id_terms)

    def get_resource_terms(self):
        """Gets the resource query terms.

        :return: the resource terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    resource_terms = property(fget=get_resource_terms)

    def get_billing_id_terms(self):
        """Gets the billing ``Id`` query terms.

        :return: the billing ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    billing_id_terms = property(fget=get_billing_id_terms)

    def get_billing_terms(self):
        """Gets the billing query terms.

        :return: the billing terms
        :rtype: ``osid.acknowledgement.BillingQueryInspector``

        """
        return # osid.acknowledgement.BillingQueryInspector

    billing_terms = property(fget=get_billing_terms)

    def get_credit_query_inspector_record(self, credit_record_type):
        """Gets the credit query inspector record corresponding to the given ``Credit`` record ``Type``.

        :param credit_record_type: a credit record type
        :type credit_record_type: ``osid.type.Type``
        :return: the credit inspector query record
        :rtype: ``osid.acknowledgement.records.CreditQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``credit_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(credit_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.CreditQueryInspectorRecord


class BillingQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to ``OsidQuery`` interfaces for reuse or
    modification in the search sessions.

    """
    def get_credit_id_terms(self):
        """Gets the credit ``Id`` query terms.

        :return: the credit ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    credit_id_terms = property(fget=get_credit_id_terms)

    def get_credit_terms(self):
        """Gets the credit query terms.

        :return: the credit terms
        :rtype: ``osid.acknowledgement.CreditQueryInspector``

        """
        return # osid.acknowledgement.CreditQueryInspector

    credit_terms = property(fget=get_credit_terms)

    def get_ancestor_billing_id_terms(self):
        """Gets the ancestor billing ``Id`` query terms.

        :return: the ancestor billing ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_billing_id_terms = property(fget=get_ancestor_billing_id_terms)

    def get_ancestor_billing_terms(self):
        """Gets the ancestor billing query terms.

        :return: the ancestor billing terms
        :rtype: ``osid.acknowledgement.BillingQueryInspector``

        """
        return # osid.acknowledgement.BillingQueryInspector

    ancestor_billing_terms = property(fget=get_ancestor_billing_terms)

    def get_descendant_billing_id_terms(self):
        """Gets the descendant billing ``Id`` query terms.

        :return: the descendant billing ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_billing_id_terms = property(fget=get_descendant_billing_id_terms)

    def get_descendant_billing_terms(self):
        """Gets the descendant billing query terms.

        :return: the descendant billing terms
        :rtype: ``osid.acknowledgement.BillingQueryInspector``

        """
        return # osid.acknowledgement.BillingQueryInspector

    descendant_billing_terms = property(fget=get_descendant_billing_terms)

    def get_billing_query_inspector_record(self, billing_record_type):
        """Gets the record query inspector record corresponding to the given ``Billing`` record ``Type``.

        :param billing_record_type: a billing record type
        :type billing_record_type: ``osid.type.Type``
        :return: the billing query inspector record
        :rtype: ``osid.acknowledgement.records.BillingQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(billing_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.BillingQueryInspectorRecord


