from ..osid import managers as osid_managers


class AcknowledgementProfile(osid_managers.OsidProfile):
    """The acknowledgement profile describes the interoperability among acknowledgement services."""
    def supports_visible_federation(self):
        """Tests if any billing federation is exposed.

        Federation is exposed when a specific billing may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of billings appears as a
        single billing.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_credit_lookup(self):
        """Tests for the availability of a credit lookup service.

        :return: ``true`` if credit lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_credit_query(self):
        """Tests for the availability of a credit query service.

        :return: ``true`` if credit query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_credit_search(self):
        """Tests if searching for credits is available.

        :return: ``true`` if credit search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_credit_admin(self):
        """Tests if managing for credits is available.

        :return: ``true`` if a credit adminstrative service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_credit_notification(self):
        """Tests if credit notification is available.

        :return: ``true`` if credit notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_credit_billing(self):
        """Tests if a credit to billing lookup session is available.

        :return: ``true`` if credit billing lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_credit_billing_assignment(self):
        """Tests if a credit to billing assignment session is available.

        :return: ``true`` if credit billing assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_credit_smart_billing(self):
        """Tests if a credit smart billing session is available.

        :return: ``true`` if credit smart billing is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_billing_lookup(self):
        """Tests for the availability of an billing lookup service.

        :return: ``true`` if billing lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_billing_query(self):
        """Tests if querying billings is available.

        :return: ``true`` if billing query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_billing_search(self):
        """Tests if searching for billings is available.

        :return: ``true`` if billing search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_billing_admin(self):
        """Tests for the availability of a billing administrative service for creating and deleting billings.

        :return: ``true`` if billing administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_billing_notification(self):
        """Tests for the availability of a billing notification service.

        :return: ``true`` if billing notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_billing_hierarchy(self):
        """Tests for the availability of a billing hierarchy traversal service.

        :return: ``true`` if billing hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_billing_hierarchy_design(self):
        """Tests for the availability of a billing hierarchy design service.

        :return: ``true`` if billing hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_acknowledgement_batch(self):
        """Tests for the availability of an acknowledgement batch service.

        :return: ``true`` if an acknowledgement batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_credit_record_types(self):
        """Gets the supported ``Credit`` record types.

        :return: a list containing the supported credit record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    credit_record_types = property(fget=get_credit_record_types)

    def supports_credit_record_type(self, credit_record_type):
        """Tests if the given ``Credit`` record type is supported.

        :param credit_record_type: a ``Type`` indicating a ``Credit`` record type
        :type credit_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``credit_record_type`` is ``null``

        """
        return # boolean

    def get_credit_search_record_types(self):
        """Gets the supported credit search record types.

        :return: a list containing the supported credit search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    credit_search_record_types = property(fget=get_credit_search_record_types)

    def supports_credit_search_record_type(self, credit_search_record_type):
        """Tests if the given credit search record type is supported.

        :param credit_search_record_type: a ``Type`` indicating a credit record type
        :type credit_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``credit_search_record_type`` is ``null``

        """
        return # boolean

    def get_billing_record_types(self):
        """Gets the supported ``Billing`` record types.

        :return: a list containing the supported billing record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    billing_record_types = property(fget=get_billing_record_types)

    def supports_billing_record_type(self, billing_record_type):
        """Tests if the given ``Billing`` record type is supported.

        :param billing_record_type: a ``Type`` indicating a ``Billing`` record type
        :type billing_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``

        """
        return # boolean

    def get_billing_search_record_types(self):
        """Gets the supported billing search record types.

        :return: a list containing the supported billing search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    billing_search_record_types = property(fget=get_billing_search_record_types)

    def supports_billing_search_record_type(self, billing_search_record_type):
        """Tests if the given billing search record type is supported.

        :param billing_search_record_type: a ``Type`` indicating a billing record type
        :type billing_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``billing_search_record_type`` is ``null``

        """
        return # boolean


class AcknowledgementManager(osid_managers.OsidManager, AcknowledgementProfile):
    """The acknowledgement manager provides access to acknowledgement sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``CreditLookupSession:`` a session to lookup credits
      * ``CreditQuerySession:`` a session for querying credits
      * ``CreditSearchSession:`` a session to search credits
      * ``CreditAdminSession:`` a session to manage credits
      * ``CreditNotificationSession:`` a session to subscribe to
        notifications of credit changes
      * ``CreditBillingSession:`` a session to look up credit to billing
        mappings
      * ``CreditBillingAssignmentSession:`` a session to manage credit
        to billing mappings
      * ``CreditSmartBillingSession:`` a session to manage dynamic
        credit to billing mappings
      * ``BillingLookupSession:`` a session to retrieve billings
      * ``BillingQuerySession:`` a session for querying billings
      * ``BillingSearchSession:`` a session to search for billings
      * ``BillingAdminSession:`` a session to create, update and delete
        billings
      * ``BillingNotificationSession:`` a session to receive
        notifications for changes in billings
      * ``BillingHierarchyTraversalSession:`` a session to traverse
        hierarchies of billings
      * ``BillingHierarchyDesignSession:`` a session to manage
        hierarchies of billings

    
    The acknowledgement manager also provides a profile for determing
    the supported search types supported by this service.

    """
    def get_credit_lookup_session(self):
        """Gets the ``OsidSession`` associated with the credit lookup service.

        :return: a ``CreditLookupSession``
        :rtype: ``osid.acknowledgement.CreditLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_lookup()`` is ``false``

        """
        return # osid.acknowledgement.CreditLookupSession

    credit_lookup_session = property(fget=get_credit_lookup_session)

    def get_credit_lookup_session_for_billing(self, billing_id):
        """Gets the ``OsidSession`` associated with the credit lookup service for the given billing.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: a ``CreditLookupSession``
        :rtype: ``osid.acknowledgement.CreditLookupSession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditLookupSession

    def get_credit_query_session(self):
        """Gets the ``OsidSession`` associated with the credit query service.

        :return: a ``CreditQuerySession``
        :rtype: ``osid.acknowledgement.CreditQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_query()`` is ``false``

        """
        return # osid.acknowledgement.CreditQuerySession

    credit_query_session = property(fget=get_credit_query_session)

    def get_credit_query_session_for_billing(self, billing_id):
        """Gets the ``OsidSession`` associated with the credit query service for the given billing.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: a ``CreditQuerySession``
        :rtype: ``osid.acknowledgement.CreditQuerySession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditQuerySession

    def get_credit_search_session(self):
        """Gets the ``OsidSession`` associated with the credit search service.

        :return: a ``CreditSearchSession``
        :rtype: ``osid.acknowledgement.CreditSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_search()`` is ``false``

        """
        return # osid.acknowledgement.CreditSearchSession

    credit_search_session = property(fget=get_credit_search_session)

    def get_credit_search_session_for_billing(self, billing_id):
        """Gets the ``OsidSession`` associated with the credit search service for the given billing.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: a ``CreditSearchSession``
        :rtype: ``osid.acknowledgement.CreditSearchSession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditSearchSession

    def get_credit_admin_session(self):
        """Gets the ``OsidSession`` associated with the credit administration service.

        :return: a ``CreditAdminSession``
        :rtype: ``osid.acknowledgement.CreditAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_admin()`` is ``false``

        """
        return # osid.acknowledgement.CreditAdminSession

    credit_admin_session = property(fget=get_credit_admin_session)

    def get_credit_admin_session_for_billing(self, billing_id):
        """Gets the ``OsidSession`` associated with the credit administration service for the given billing.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: a ``CreditAdminSession``
        :rtype: ``osid.acknowledgement.CreditAdminSession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditAdminSession

    def get_credit_notification_session(self, credit_receiver):
        """Gets the ``OsidSession`` associated with the credit notification service.

        :param credit_receiver: the receiver
        :type credit_receiver: ``osid.acknowledgement.CreditReceiver``
        :return: a ``CreditNotificationSession``
        :rtype: ``osid.acknowledgement.CreditNotificationSession``
        :raise: ``NullArgument`` -- ``credit_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_notification()`` is ``false``

        """
        return # osid.acknowledgement.CreditNotificationSession

    def get_credit_notification_session_for_billing(self, credit_receiver, billing_id):
        """Gets the ``OsidSession`` associated with the credit notification service for the given billing.

        :param credit_receiver: the receiver
        :type credit_receiver: ``osid.acknowledgement.CreditReceiver``
        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: a ``CreditNotificationSession``
        :rtype: ``osid.acknowledgement.CreditNotificationSession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``credit_receiver`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditNotificationSession

    def get_credit_billing_session(self):
        """Gets the session for retrieving credit to billing mappings.

        :return: a ``CreditBillingSession``
        :rtype: ``osid.acknowledgement.CreditBillingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_billing()`` is ``false``

        """
        return # osid.acknowledgement.CreditBillingSession

    credit_billing_session = property(fget=get_credit_billing_session)

    def get_credit_billing_assignment_session(self):
        """Gets the session for assigning credit to billing mappings.

        :return: a ``CreditBillingAssignmentSession``
        :rtype: ``osid.acknowledgement.CreditBillingAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_billing_assignment()`` is ``false``

        """
        return # osid.acknowledgement.CreditBillingAssignmentSession

    credit_billing_assignment_session = property(fget=get_credit_billing_assignment_session)

    def get_credit_smart_billing_session(self, billing_id):
        """Gets the session associated with the credit smart billing for the given billing.

        :param billing_id: the ``Id`` of the billing
        :type billing_id: ``osid.id.Id``
        :return: a ``CreditSmartBillingSession``
        :rtype: ``osid.acknowledgement.CreditSmartBillingSession``
        :raise: ``NotFound`` -- ``billing_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_smart_billing()`` is ``false``

        """
        return # osid.acknowledgement.CreditSmartBillingSession

    def get_billing_lookup_session(self):
        """Gets the ``OsidSession`` associated with the billing lookup service.

        :return: a ``BillingLookupSession``
        :rtype: ``osid.acknowledgement.BillingLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_lookup()`` is ``false``

        """
        return # osid.acknowledgement.BillingLookupSession

    billing_lookup_session = property(fget=get_billing_lookup_session)

    def get_billing_query_session(self):
        """Gets the ``OsidSession`` associated with the billing query service.

        :return: a ``BillingQuerySession``
        :rtype: ``osid.acknowledgement.BillingQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_query()`` is ``false``

        """
        return # osid.acknowledgement.BillingQuerySession

    billing_query_session = property(fget=get_billing_query_session)

    def get_billing_search_session(self):
        """Gets the ``OsidSession`` associated with the billing search service.

        :return: a ``BillingSearchSession``
        :rtype: ``osid.acknowledgement.BillingSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_search()`` is ``false``

        """
        return # osid.acknowledgement.BillingSearchSession

    billing_search_session = property(fget=get_billing_search_session)

    def get_billing_admin_session(self):
        """Gets the ``OsidSession`` associated with the billing administrative service.

        :return: a ``BillingAdminSession``
        :rtype: ``osid.acknowledgement.BillingAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_admin()`` is ``false``

        """
        return # osid.acknowledgement.BillingAdminSession

    billing_admin_session = property(fget=get_billing_admin_session)

    def get_billing_notification_session(self, billing_receiver):
        """Gets the ``OsidSession`` associated with the billing notification service.

        :param billing_receiver: the receiver
        :type billing_receiver: ``osid.acknowledgement.BillingReceiver``
        :return: a ``BillingNotificationSession``
        :rtype: ``osid.acknowledgement.BillingNotificationSession``
        :raise: ``NullArgument`` -- ``billing_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_notification()`` is ``false``

        """
        return # osid.acknowledgement.BillingNotificationSession

    def get_billing_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the billing hierarchy service.

        :return: a ``BillingHierarchySession``
        :rtype: ``osid.acknowledgement.BillingHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_hierarchy()`` is ``false``

        """
        return # osid.acknowledgement.BillingHierarchySession

    billing_hierarchy_session = property(fget=get_billing_hierarchy_session)

    def get_billing_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the billing hierarchy design service.

        :return: a ``BillingHierarchyDesignSession``
        :rtype: ``osid.acknowledgement.BillingHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_hierarchy_design()`` is ``false``

        """
        return # osid.acknowledgement.BillingHierarchyDesignSession

    billing_hierarchy_design_session = property(fget=get_billing_hierarchy_design_session)

    def get_acknowledgement_batch_manager(self):
        """Gets an ``AcknowledgementBatchManager``.

        :return: an ``AcknowledgementBatchManager``
        :rtype: ``osid.acknowledgement.batch.AcknowledgementBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_acknowledgement_bach()`` is ``false``

        """
        return # osid.acknowledgement.batch.AcknowledgementBatchManager

    acknowledgement_batch_manager = property(fget=get_acknowledgement_batch_manager)


class AcknowledgementProxyManager(osid_managers.OsidProxyManager, AcknowledgementProfile):
    """The acknowledgement manager provides access to acknowledgement sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager accept a ``Proxy`` interface for passing
    information from a server environment. The sessions included in this
    manager are:

      * ``CreditLookupSession:`` a session to lookup credits
      * ``CreditQuerySession:`` a session for querying credits
      * ``CreditSearchSession:`` a session to search credits
      * ``CreditAdminSession:`` a session to manage credits
      * ``CreditNotificationSession:`` a session to subscribe to
        notifications of credit changes
      * ``CreditBillingSession:`` a session to look up credit to billing
        mappings
      * ``CreditBillingAssignmentSession:`` a session to manage credit
        to billing mappings
      * ``CreditSmartBillingSession:`` a session to manage dynamic
        credit to billing mappings
      * ``BillingLookupSession:`` a session to retrieve billings
      * ``BillingQuerySession:`` a session for querying billings
      * ``BillingSearchSession:`` a session to search for billings
      * ``BillingAdminSession:`` a session to create, update and delete
        billings
      * ``BillingNotificationSession:`` a session to receive
        notifications for changes in billings
      * ``BillingHierarchyTraversalSession:`` a session to traverse
        hierarchies of billings
      * ``BillingHierarchyDesignSession:`` a session to manage
        hierarchies of billings

    
    The acknowledgement manager also provides a profile for determing
    the supported search types supported by this service.

    """
    def get_credit_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the credit lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditLookupSession``
        :rtype: ``osid.acknowledgement.CreditLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_lookup()`` is ``false``

        """
        return # osid.acknowledgement.CreditLookupSession

    def get_credit_lookup_session_for_billing(self, billing_id, proxy):
        """Gets the ``OsidSession`` associated with the credit lookup service for the given billing.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditLookupSession``
        :rtype: ``osid.acknowledgement.CreditLookupSession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``billing_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditLookupSession

    def get_credit_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the credit query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditQuerySession``
        :rtype: ``osid.acknowledgement.CreditQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_query()`` is ``false``

        """
        return # osid.acknowledgement.CreditQuerySession

    def get_credit_query_session_for_billing(self, billing_id, proxy):
        """Gets the ``OsidSession`` associated with the credit query service for the given billing.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditQuerySession``
        :rtype: ``osid.acknowledgement.CreditQuerySession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``billing_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_query()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditQuerySession

    def get_credit_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the credit search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditSearchSession``
        :rtype: ``osid.acknowledgement.CreditSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_search()`` is ``false``

        """
        return # osid.acknowledgement.CreditSearchSession

    def get_credit_search_session_for_billing(self, billing_id, proxy):
        """Gets the ``OsidSession`` associated with the credit search service for the given billing.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditSearchSession``
        :rtype: ``osid.acknowledgement.CreditSearchSession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``billing_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_search()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditSearchSession

    def get_credit_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the credit administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditAdminSession``
        :rtype: ``osid.acknowledgement.CreditAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_admin()`` is ``false``

        """
        return # osid.acknowledgement.CreditAdminSession

    def get_credit_admin_session_for_billing(self, billing_id, proxy):
        """Gets the ``OsidSession`` associated with the credit administration service for the given billing.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditAdminSession``
        :rtype: ``osid.acknowledgement.CreditAdminSession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``billing_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditAdminSession

    def get_credit_notification_session(self, credit_receiver, proxy):
        """Gets the ``OsidSession`` associated with the credit notification service.

        :param credit_receiver: the receiver
        :type credit_receiver: ``osid.acknowledgement.CreditReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditNotificationSession``
        :rtype: ``osid.acknowledgement.CreditNotificationSession``
        :raise: ``NullArgument`` -- ``credit_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_notification()`` is ``false``

        """
        return # osid.acknowledgement.CreditNotificationSession

    def get_credit_notification_session_for_billing(self, credit_receiver, billing_id, proxy):
        """Gets the ``OsidSession`` associated with the credit notification service for the given billing.

        :param credit_receiver: the receiver
        :type credit_receiver: ``osid.acknowledgement.CreditReceiver``
        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditNotificationSession``
        :rtype: ``osid.acknowledgement.CreditNotificationSession``
        :raise: ``NotFound`` -- no ``Billing`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``credit_receiver, billing_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        return # osid.acknowledgement.CreditNotificationSession

    def get_credit_billing_session(self, proxy):
        """Gets the session for retrieving credit to billing mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditBillingSession``
        :rtype: ``osid.acknowledgement.CreditBillingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_billing()`` is ``false``

        """
        return # osid.acknowledgement.CreditBillingSession

    def get_credit_billing_assignment_session(self, proxy):
        """Gets the session for assigning credit to billing mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditBillingAssignmentSession``
        :rtype: ``osid.acknowledgement.CreditBillingAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_billing_assignment()`` is ``false``

        """
        return # osid.acknowledgement.CreditBillingAssignmentSession

    def get_credit_smart_billing_session(self, billing_id, proxy):
        """Gets the session for managing dynamic credit billings for the given billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CreditSmartBillingSession``
        :rtype: ``osid.acknowledgement.CreditSmartBillingSession``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_smart_billing()`` is ``false``

        """
        return # osid.acknowledgement.CreditSmartBillingSession

    def get_billing_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the billing lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BillingLookupSession``
        :rtype: ``osid.acknowledgement.BillingLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_lookup()`` is ``false``

        """
        return # osid.acknowledgement.BillingLookupSession

    def get_billing_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the billing query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BillingQuerySession``
        :rtype: ``osid.acknowledgement.BillingQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_query()`` is ``false``

        """
        return # osid.acknowledgement.BillingQuerySession

    def get_billing_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the billing search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BillingSearchSession``
        :rtype: ``osid.acknowledgement.BillingSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_search()`` is ``false``

        """
        return # osid.acknowledgement.BillingSearchSession

    def get_billing_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the billing administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BillingAdminSession``
        :rtype: ``osid.acknowledgement.BillingAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_admin()`` is ``false``

        """
        return # osid.acknowledgement.BillingAdminSession

    def get_billing_notification_session(self, billing_receiver, proxy):
        """Gets the ``OsidSession`` associated with the billing notification service.

        :param billing_receiver: the receiver
        :type billing_receiver: ``osid.acknowledgement.BillingReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BillingNotificationSession``
        :rtype: ``osid.acknowledgement.BillingNotificationSession``
        :raise: ``NullArgument`` -- ``billing_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_notification()`` is ``false``

        """
        return # osid.acknowledgement.BillingNotificationSession

    def get_billing_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the billing hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BillingHierarchySession``
        :rtype: ``osid.acknowledgement.BillingHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_hierarchy()`` is ``false``

        """
        return # osid.acknowledgement.BillingHierarchySession

    def get_billing_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the billing hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``BillingHierarchyDesignSession``
        :rtype: ``osid.acknowledgement.BillingHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_hierarchy_design()`` is ``false``

        """
        return # osid.acknowledgement.BillingHierarchyDesignSession

    def get_acknowledgement_batch_proxy_manager(self):
        """Gets an ``AcknowledgementBatchProxyManager``.

        :return: an ``AcknowledgementBatchProxyManager``
        :rtype: ``osid.acknowledgement.batch.AcknowledgementBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_acknowledgement_bach()`` is ``false``

        """
        return # osid.acknowledgement.batch.AcknowledgementBatchProxyManager

    acknowledgement_batch_proxy_manager = property(fget=get_acknowledgement_batch_proxy_manager)


