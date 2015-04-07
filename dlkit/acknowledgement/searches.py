from ..osid import searches as osid_searches


class CreditSearch(osid_searches.OsidSearch):
    """The search interface for governing credit searches."""
    def search_among_credits(self, credit_ids):
        """Execute this search among the given list of credits.

        :param credit_ids: list of credits
        :type credit_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``credit_ids`` is ``null``

        """
        pass

    def order_credit_results(self, credit_search_order):
        """Specify an ordering to the search results.

        :param credit_search_order: credit search order
        :type credit_search_order: ``osid.acknowledgement.CreditSearchOrder``
        :raise: ``NullArgument`` -- ``credit_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``credit_search_order`` is not of this service

        """
        pass

    def get_credit_search_record(self, credit_search_record_type):
        """Gets the record corresponding to the given credit search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param credit_search_record_type: a credit search record type
        :type credit_search_record_type: ``osid.type.Type``
        :return: the credit search record
        :rtype: ``osid.acknowledgement.records.CreditSearchRecord``
        :raise: ``NullArgument`` -- ``credit_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(credit_search_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.CreditSearchRecord


class CreditSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_credits(self):
        """Gets the credit list resulting from a search.

        :return: the credit list
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``IllegalState`` -- the list has already been retrieved

        """
        return # osid.acknowledgement.CreditList

    credits = property(fget=get_credits)

    def get_credit_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.acknowledgement.CreditQueryInspector``

        """
        return # osid.acknowledgement.CreditQueryInspector

    credit_query_inspector = property(fget=get_credit_query_inspector)

    def get_credit_search_results_record(self, credit_search_record_type):
        """Gets the record corresponding to the given credit search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param credit_search_record_type: a credit search record type
        :type credit_search_record_type: ``osid.type.Type``
        :return: the credit search results record
        :rtype: ``osid.acknowledgement.records.CreditSearchResultsRecord``
        :raise: ``NullArgument`` -- ``credit_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(credit_search_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.CreditSearchResultsRecord


class BillingSearch(osid_searches.OsidSearch):
    """The search interface for governing billing searches."""
    def search_among_billings(self, billing_ids):
        """Execute this search among the given list of billings.

        :param billing_ids: list of billings
        :type billing_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``billing_ids`` is ``null``

        """
        pass

    def order_billing_results(self, billing_search_order):
        """Specify an ordering to the search results.

        :param billing_search_order: billing search order
        :type billing_search_order: ``osid.acknowledgement.BillingSearchOrder``
        :raise: ``NullArgument`` -- ``billing_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``billing_search_order`` is not of this service

        """
        pass

    def get_billing_search_record(self, billing_search_record_type):
        """Gets the record corresponding to the given billing search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param billing_search_record_type: a billing search record type
        :type billing_search_record_type: ``osid.type.Type``
        :return: the billing search record
        :rtype: ``osid.acknowledgement.records.BillingSearchRecord``
        :raise: ``NullArgument`` -- ``billing_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(billing_search_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.BillingSearchRecord


class BillingSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_billings(self):
        """Gets the billing list resulting from a search.

        :return: the billing list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``IllegalState`` -- the list has already been retrieved

        """
        return # osid.acknowledgement.BillingList

    billings = property(fget=get_billings)

    def get_billing_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the query inspector
        :rtype: ``osid.acknowledgement.BillingQueryInspector``

        """
        return # osid.acknowledgement.BillingQueryInspector

    billing_query_inspector = property(fget=get_billing_query_inspector)

    def get_billing_search_results_record(self, billing_search_record_type):
        """Gets the record corresponding to the given billing search record Type.

        This method is used to retrieve an object implementing the
        requested record.

        :param billing_search_record_type: a billing search record type
        :type billing_search_record_type: ``osid.type.Type``
        :return: the billing search results record
        :rtype: ``osid.acknowledgement.records.BillingSearchResultsRecord``
        :raise: ``NullArgument`` -- ``billing_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(billing_search_record_type)`` is ``false``

        """
        return # osid.acknowledgement.records.BillingSearchResultsRecord


