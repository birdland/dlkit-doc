# -*- coding: utf-8 -*-
"""Acknowledgement Open Service Interface Definitions
acknowledgement version 3.0.0

The Acknowledgement OSID defines and relates credits such as authors or
creators to ``OsidObjects``.

Credits

``Credits`` are relationships between what is being credited and to what
the credit applies. The enttity being credited is represented by a
``Resource``. This service does not define the entity to which the
credit applies and instead references an OSID ``Id`` external to this
service. The ``Id`` is a reference to an entity managed outside this
service.

The external ``Id`` reference positions the Acknowledgement OSID as an
auxiliary service that can be orchestrated with other OSIDs to provide
acknowledgements with any ``OsidObject``. Resource is an abstract
interface used for a variety of purposes including people. The
Acknowledgement OSID this has a very abstract feel whose primary focus
is to manage the relationships.

As with many ``OsidRelationships,`` the genus Type can be used to
describe the nature of the relationship, such as a writer or
photographer. The ``CreditRecord`` may be used to capture data related
to the relatonship itself.

``OsidRelationships`` are temporal by including effective dates.

Billing Cataloging

``Credits`` are mapped to ``Billings`` for organization. ``Billings``
can be managed hierarchically to federate multiple collections of
``Credits`` .

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class AcknowledgementProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any billing federation is exposed.
        Federation is exposed when a specific billing may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of billings appears as a
        single billing.

        :return: ``true`` if visible federation is supproted, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_credit_lookup(self):
        """Tests for the availability of a credit lookup service.

        :return: ``true`` if credit lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_credit_query(self):
        """Tests for the availability of a credit query service.

        :return: ``true`` if credit query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_credit_search(self):
        """Tests if searching for credits is available.

        :return: ``true`` if credit search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_credit_admin(self):
        """Tests if managing for credits is available.

        :return: ``true`` if a credit adminstrative service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_credit_notification(self):
        """Tests if credit notification is available.

        :return: ``true`` if credit notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_credit_billing(self):
        """Tests if a credit to billing lookup session is available.

        :return: ``true`` if credit billing lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_credit_billing_assignment(self):
        """Tests if a credit to billing assignment session is available.

        :return: ``true`` if credit billing assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_credit_smart_billing(self):
        """Tests if a credit smart billing session is available.

        :return: ``true`` if credit smart billing is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_billing_lookup(self):
        """Tests for the availability of an billing lookup service.

        :return: ``true`` if billing lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_billing_query(self):
        """Tests if querying billings is available.

        :return: ``true`` if billing query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_billing_search(self):
        """Tests if searching for billings is available.

        :return: ``true`` if billing search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_billing_admin(self):
        """Tests for the availability of a billing administrative service for creating and deleting billings.

        :return: ``true`` if billing administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_billing_notification(self):
        """Tests for the availability of a billing notification service.

        :return: ``true`` if billing notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_billing_hierarchy(self):
        """Tests for the availability of a billing hierarchy traversal service.

        :return: ``true`` if billing hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_billing_hierarchy_design(self):
        """Tests for the availability of a billing hierarchy design service.

        :return: ``true`` if billing hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_acknowledgement_batch(self):
        """Tests for the availability of an acknowledgement batch service.

        :return: ``true`` if an acknowledgement batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_credit_record_types(self):
        """Gets the supported ``Credit`` record types.

        :return: a list containing the supported credit record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    credit_record_types = property(fget=get_credit_record_types)

    def supports_credit_record_type(self, credit_record_type):
        """Tests if the given ``Credit`` record type is supported.

        :param credit_record_type: a ``Type`` indicating a ``Credit`` record type
        :type credit_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``credit_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_credit_search_record_types(self):
        """Gets the supported credit search record types.

        :return: a list containing the supported credit search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    credit_search_record_types = property(fget=get_credit_search_record_types)

    def supports_credit_search_record_type(self, credit_search_record_type):
        """Tests if the given credit search record type is supported.

        :param credit_search_record_type: a ``Type`` indicating a credit record type
        :type credit_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``credit_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_billing_record_types(self):
        """Gets the supported ``Billing`` record types.

        :return: a list containing the supported billing record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    billing_record_types = property(fget=get_billing_record_types)

    def supports_billing_record_type(self, billing_record_type):
        """Tests if the given ``Billing`` record type is supported.

        :param billing_record_type: a ``Type`` indicating a ``Billing`` record type
        :type billing_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_billing_search_record_types(self):
        """Gets the supported billing search record types.

        :return: a list containing the supported billing search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    billing_search_record_types = property(fget=get_billing_search_record_types)

    def supports_billing_search_record_type(self, billing_search_record_type):
        """Tests if the given billing search record type is supported.

        :param billing_search_record_type: a ``Type`` indicating a billing record type
        :type billing_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``billing_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class AcknowledgementManager(osid_managers.OsidManager, osid_sessions.OsidSession, AcknowledgementProfile):

    def get_credit_lookup_session(self):
        """Gets the ``OsidSession`` associated with the credit lookup service.

        :return: a ``CreditLookupSession``
        :rtype: ``osid.acknowledgement.CreditLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_credit_query_session(self):
        """Gets the ``OsidSession`` associated with the credit query service.

        :return: a ``CreditQuerySession``
        :rtype: ``osid.acknowledgement.CreditQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_credit_search_session(self):
        """Gets the ``OsidSession`` associated with the credit search service.

        :return: a ``CreditSearchSession``
        :rtype: ``osid.acknowledgement.CreditSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_credit_admin_session(self):
        """Gets the ``OsidSession`` associated with the credit administration service.

        :return: a ``CreditAdminSession``
        :rtype: ``osid.acknowledgement.CreditAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_credit_billing_session(self):
        """Gets the session for retrieving credit to billing mappings.

        :return: a ``CreditBillingSession``
        :rtype: ``osid.acknowledgement.CreditBillingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_billing()`` is ``false``

        """
        raise UNIMPLEMENTED()

    credit_billing_session = property(fget=get_credit_billing_session)

    def get_credit_billing_assignment_session(self):
        """Gets the session for assigning credit to billing mappings.

        :return: a ``CreditBillingAssignmentSession``
        :rtype: ``osid.acknowledgement.CreditBillingAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_credit_billing_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_billing_lookup_session(self):
        """Gets the ``OsidSession`` associated with the billing lookup service.

        :return: a ``BillingLookupSession``
        :rtype: ``osid.acknowledgement.BillingLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    billing_lookup_session = property(fget=get_billing_lookup_session)

    def get_billing_query_session(self):
        """Gets the ``OsidSession`` associated with the billing query service.

        :return: a ``BillingQuerySession``
        :rtype: ``osid.acknowledgement.BillingQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    billing_query_session = property(fget=get_billing_query_session)

    def get_billing_search_session(self):
        """Gets the ``OsidSession`` associated with the billing search service.

        :return: a ``BillingSearchSession``
        :rtype: ``osid.acknowledgement.BillingSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    billing_search_session = property(fget=get_billing_search_session)

    def get_billing_admin_session(self):
        """Gets the ``OsidSession`` associated with the billing administrative service.

        :return: a ``BillingAdminSession``
        :rtype: ``osid.acknowledgement.BillingAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_billing_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the billing hierarchy service.

        :return: a ``BillingHierarchySession``
        :rtype: ``osid.acknowledgement.BillingHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    billing_hierarchy_session = property(fget=get_billing_hierarchy_session)

    def get_billing_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the billing hierarchy design service.

        :return: a ``BillingHierarchyDesignSession``
        :rtype: ``osid.acknowledgement.BillingHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_billing_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    billing_hierarchy_design_session = property(fget=get_billing_hierarchy_design_session)

    def get_acknowledgement_batch_manager(self):
        """Gets an ``AcknowledgementBatchManager``.

        :return: an ``AcknowledgementBatchManager``
        :rtype: ``osid.acknowledgement.batch.AcknowledgementBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_acknowledgement_bach()`` is ``false``

        """
        raise UNIMPLEMENTED()

    acknowledgement_batch_manager = property(fget=get_acknowledgement_batch_manager)


##
# The following methods are from osid.acknowledgement.BillingLookupSession

    def can_lookup_billings(self):
        """Tests if this user can perform ``Billing`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_billing_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_billing_view(self):
        """A complete view of the ``Billing`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_billing(self, billing_id):
        """Gets the ``Billing`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Billing`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Billing`` and retained for
        compatibility.

        :param billing_id: ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: the billing
        :rtype: ``osid.acknowledgement.Billing``
        :raise: ``NotFound`` -- ``billing_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_ids(self, billing_ids):
        """Gets a ``BillingList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the billings
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Billings`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param billing_ids: the list of ``Ids`` to retrieve
        :type billing_ids: ``osid.id.IdList``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``billing_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_genus_type(self, billing_genus_type):
        """Gets a ``BillingList`` corresponding to the given billing genus ``Type`` which does not include billings of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.

        :param billing_genus_type: a billing genus type
        :type billing_genus_type: ``osid.type.Type``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``billing_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_parent_genus_type(self, billing_genus_type):
        """Gets a ``BillingList`` corresponding to the given billing genus ``Type`` and include any additional billings with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.

        :param billing_genus_type: a billing genus type
        :type billing_genus_type: ``osid.type.Type``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``billing_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_record_type(self, billing_record_type):
        """Gets a ``BillingList`` containing the given billing record ``Type``.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.

        :param billing_record_type: a billing record type
        :type billing_record_type: ``osid.type.Type``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_provider(self, provider_id):
        """Gets a ``BillingList`` from the given Provider.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.

        :param provider_id: a provider ``Id``
        :type provider_id: ``osid.id.Id``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``provider_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings(self):
        """Gets all ``Billings``.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.

        :return: a list of ``Billings``
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    billings = property(fget=get_billings)


##
# The following methods are from osid.acknowledgement.BillingQuerySession

    def can_search_billings(self):
        """Tests if this user can perform ``Billing`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_billing_query(self):
        """Gets a billing query.

        :return: the billing query
        :rtype: ``osid.acknowledgement.BillingQuery``

        """
        raise UNIMPLEMENTED()

    billing_query = property(fget=get_billing_query)

    def get_billings_by_query(self, billing_query):
        """Gets a list of ``Billings`` matching the given search.

        :param billing_query: the billing query
        :type billing_query: ``osid.acknowledgement.BillingQuery``
        :return: the returned ``BillingList``
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``billing_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``billing_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingSearchSession

    def get_billing_search(self):
        """Gets a billing search.

        :return: the billing search
        :rtype: ``osid.acknowledgement.BillingSearch``

        """
        raise UNIMPLEMENTED()

    billing_search = property(fget=get_billing_search)

    def get_billing_search_order(self):
        """Gets a billing search order.
        The ``BillingSearchOrder`` is supplied to a ``BillingSearch`` to
        specify the ordering of results.

        :return: the billing search order
        :rtype: ``osid.acknowledgement.BillingSearchOrder``

        """
        raise UNIMPLEMENTED()

    billing_search_order = property(fget=get_billing_search_order)

    def get_billings_by_search(self, billing_query, billing_search):
        """Gets the search results matching the given search.

        :param billing_query: the billing query
        :type billing_query: ``osid.acknowledgement.BillingQuery``
        :param billing_search: the billing search
        :type billing_search: ``osid.acknowledgement.BillingSearch``
        :return: the search results
        :rtype: ``osid.acknowledgement.BillingSearchResults``
        :raise: ``NullArgument`` -- ``billing_query`` or ``billing_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``billing_query`` or ``billing_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_billing_query_from_inspector(self, billing_query_inspector):
        """Gets a billing query from an inspector.
        The inspector is available from a ``BillingSearchResults``.

        :param billing_query_inspector: a billing query inspector
        :type billing_query_inspector: ``osid.acknowledgement.BillingQueryInspector``
        :return: the billing query
        :rtype: ``osid.acknowledgement.BillingQuery``
        :raise: ``NullArgument`` -- ``billing_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``ibilling_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingAdminSession

    def can_create_billings(self):
        """Tests if this user can create ``Billings``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Billing`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Billing`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_billing_with_record_types(self, billing_record_types):
        """Tests if this user can create a single ``Billing`` using the desired record types.
        While ``AcknowledgementManager.getBillingRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Billing``. Providing an empty array tests if a ``Billing`` can
        be created with no records.

        :param billing_record_types: array of types
        :type billing_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Billing`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``billing_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_billing_form_for_create(self, billing_record_types):
        """Gets the billing form for creating new billings.
        A new form should be requested for each create transaction.

        :param billing_record_types: array of types
        :type billing_record_types: ``osid.type.Type[]``
        :return: the billing form
        :rtype: ``osid.acknowledgement.BillingForm``
        :raise: ``NullArgument`` -- ``billing_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- cannot get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_billing(self, billing_form):
        """Creates a new ``Billing``.

        :param billing_form: the form for this ``Billing``
        :type billing_form: ``osid.acknowledgement.BillingForm``
        :return: the new ``Billing``
        :rtype: ``osid.acknowledgement.Billing``
        :raise: ``IllegalState`` -- ``billing_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``billing_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``billing_form`` did not originate from ``get_billing_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_billings(self):
        """Tests if this user can update ``Billings``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Billing`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Billing`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_billing_form_for_update(self, billing_id):
        """Gets the billing form for updating an existing billing.
        A new billing form should be requested for each update
        transaction.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: the billing form
        :rtype: ``osid.acknowledgement.BillingForm``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_billing(self, billing_form):
        """Updates an existing billing.

        :param billing_form: the form containing the elements to be updated
        :type billing_form: ``osid.acknowledgement.BillingForm``
        :raise: ``IllegalState`` -- ``billing_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``billing_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``billing_form did not originate from get_billing_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_billings(self):
        """Tests if this user can delete ``Billings`` A return of true does not guarantee successful authorization.
        A return of false indicates that it is known deleting a
        ``Billing`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Billing`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_billing(self, billing_id):
        """Deletes a ``Billing``.

        :param billing_id: the ``Id`` of the ``Billing`` to remove
        :type billing_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``billing_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_billing_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Billings``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Billing`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_billing(self, billing_id, alias_id):
        """Adds an ``Id`` to a ``Billing`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Item`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another billing, it is reassigned to
        the given billing ``Id``.

        :param billing_id: the ``Id`` of a ``Billing``
        :type billing_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``billing_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingNotificationSession

    def can_register_for_billing_notifications(self):
        """Tests if this user can register for ``Billing`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_billing_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_billing_notification()`` .



        """
        raise UNIMPLEMENTED()

    def unreliable_billing_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        raise UNIMPLEMENTED()

    def acknowledge_billing_notification(self, notification_id):
        """Acknowledge a billing notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_billings(self):
        """Register for notifications of new billings.
        ``BillingReceiver.newBillings()`` is invoked when a new
        ``Billing`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billings(self):
        """Registers for notification of updated billings.
        ``BillingReceiver.changedBillings()`` is invoked when a billing
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billing(self, billing_id):
        """Registers for notification of an updated billing.
        ``BillingReceiver.changedBillings()`` is invoked when the
        specified billing is changed.

        :param billing_id: the ``Id`` of the ``Billing`` to monitor
        :type billing_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_billings(self):
        """Registers for notification of deleted billings.
        ``BillingReceiver.deletedBillings()`` is invoked when a billing
        is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_billing(self, billing_id):
        """Registers for notification of a deleted billing.
        ``BillingReceiver.deletedBillings()`` is invoked when the
        specified billing is deleted.

        :param billing_id: the ``Id`` of the ``Billing`` to monitor
        :type billing_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billing_hierarchy(self):
        """Registers for notification of an updated billing hierarchy structure.
        ``BillingReceiver.changedChildOfBillings()`` is invoked when a
        node experiences a change in its children.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billing_hierarchy_for_ancestors(self, billing_id):
        """Registers for notification of an updated billing hierarchy structure.
        ``BillingReceiver.changedChildOfBillings()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.

        :param billing_id: the ``Id`` of the ``Billing`` node to monitor
        :type billing_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billing_hierarchy_for_descendants(self, billing_id):
        """Registers for notification of an updated billing hierarchy structure.
        ``BillingReceiver.changedChildOfBillings()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.

        :param billing_id: the ``Id`` of the ``Billing`` node to monitor
        :type billing_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingHierarchySession

    def get_billing_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    billing_hierarchy_id = property(fget=get_billing_hierarchy_id)

    def get_billing_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    billing_hierarchy = property(fget=get_billing_hierarchy)

    def can_access_billing_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_billing_ids(self):
        """Gets the root billing ``Ids`` in this hierarchy.

        :return: the root billing ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_billing_ids = property(fget=get_root_billing_ids)

    def get_root_billings(self):
        """Gets the root billings in the billing hierarchy.
        A node with no parents is an orphan. While all billing ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root billings
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_billings = property(fget=get_root_billings)

    def has_parent_billings(self, billing_id):
        """Tests if the ``Billing`` has any parents.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if the billing has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_billing(self, id_, billing_id):
        """Tests if an ``Id`` is a direct parent of billing.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``billing_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_billing_ids(self, billing_id):
        """Gets the parent ``Ids`` of the given billing.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the billing
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_billings(self, billing_id):
        """Gets the parent billings of the given ``id``.

        :param billing_id: the ``Id`` of the ``Billing`` to query
        :type billing_id: ``osid.id.Id``
        :return: the parent billings of the ``id``
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NotFound`` -- a ``Billing`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_billing(self, id_, billing_id):
        """Tests if an ``Id`` is an ancestor of a billing.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``billing_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_billings(self, billing_id):
        """Tests if a billing has any children.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if the ``billing_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``bobilling_id is null ok_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_billing(self, id_, billing_id):
        """Tests if a billing is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``billing_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_billing_ids(self, billing_id):
        """Gets the child ``Ids`` of the given billing.

        :param billing_id: the ``Id`` to query
        :type billing_id: ``osid.id.Id``
        :return: the children of the billing
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_billings(self, billing_id):
        """Gets the child billings of the given ``id``.

        :param billing_id: the ``Id`` of the ``Billing`` to query
        :type billing_id: ``osid.id.Id``
        :return: the child billings of the ``id``
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NotFound`` -- a ``Billing`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_billing(self, id_, billing_id):
        """Tests if an ``Id`` is a descendant of a billing.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``billing_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billing_node_ids(self, billing_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given billing.

        :param billing_id: the ``Id`` to query
        :type billing_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a billing node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billing_nodes(self, billing_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given billing.

        :param billing_id: the ``Id`` to query
        :type billing_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a billing node
        :rtype: ``osid.acknowledgement.BillingNode``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingHierarchyDesignSession

    def can_modify_billing_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_billing(self, billing_id):
        """Adds a root billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``billing_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_billing(self, billing_id):
        """Removes a root billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_billing(self, billing_id, child_id):
        """Adds a child to a billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``billing_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``billing_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_billing(self, billing_id, child_id):
        """Removes a child from a billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``billing_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``billing_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_billings(self, billing_id):
        """Removes all children from a billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class AcknowledgementProxyManager(osid_managers.OsidProxyManager, AcknowledgementProfile):

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()

    def get_acknowledgement_batch_proxy_manager(self):
        """Gets an ``AcknowledgementBatchProxyManager``.

        :return: an ``AcknowledgementBatchProxyManager``
        :rtype: ``osid.acknowledgement.batch.AcknowledgementBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_acknowledgement_bach()`` is ``false``

        """
        raise UNIMPLEMENTED()

    acknowledgement_batch_proxy_manager = property(fget=get_acknowledgement_batch_proxy_manager)


##
# The following methods are from osid.acknowledgement.BillingLookupSession

    def can_lookup_billings(self):
        """Tests if this user can perform ``Billing`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_billing_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_billing_view(self):
        """A complete view of the ``Billing`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_billing(self, billing_id):
        """Gets the ``Billing`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Billing`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Billing`` and retained for
        compatibility.


        :param billing_id: ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: the billing
        :rtype: ``osid.acknowledgement.Billing``
        :raise: ``NotFound`` -- ``billing_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_ids(self, billing_ids):
        """Gets a ``BillingList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the billings
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Billings`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.


        :param billing_ids: the list of ``Ids`` to retrieve
        :type billing_ids: ``osid.id.IdList``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``billing_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_genus_type(self, billing_genus_type):
        """Gets a ``BillingList`` corresponding to the given billing genus ``Type`` which does not include billings of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.


        :param billing_genus_type: a billing genus type
        :type billing_genus_type: ``osid.type.Type``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``billing_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_parent_genus_type(self, billing_genus_type):
        """Gets a ``BillingList`` corresponding to the given billing genus ``Type`` and include any additional billings with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.


        :param billing_genus_type: a billing genus type
        :type billing_genus_type: ``osid.type.Type``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``billing_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_record_type(self, billing_record_type):
        """Gets a ``BillingList`` containing the given billing record ``Type``.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.


        :param billing_record_type: a billing record type
        :type billing_record_type: ``osid.type.Type``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``billing_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_provider(self, provider_id):
        """Gets a ``BillingList`` from the given Provider.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.


        :param provider_id: a provider ``Id``
        :type provider_id: ``osid.id.Id``
        :return: the returned ``Billing`` list
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``provider_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings(self):
        """Gets all ``Billings``.
        In plenary mode, the returned list contains all known billings
        or an error results. Otherwise, the returned list may contain
        only those billings that are accessible through this session.


        :return: a list of ``Billings``
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    billings = property(fget=get_billings)


##
# The following methods are from osid.acknowledgement.BillingQuerySession

    def can_search_billings(self):
        """Tests if this user can perform ``Billing`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_billing_query(self):
        """Gets a billing query.

        :return: the billing query
        :rtype: ``osid.acknowledgement.BillingQuery``

        """
        raise UNIMPLEMENTED()

    billing_query = property(fget=get_billing_query)

    def get_billings_by_query(self, billing_query):
        """Gets a list of ``Billings`` matching the given search.

        :param billing_query: the billing query
        :type billing_query: ``osid.acknowledgement.BillingQuery``
        :return: the returned ``BillingList``
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NullArgument`` -- ``billing_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``billing_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingSearchSession

    def get_billing_search(self):
        """Gets a billing search.

        :return: the billing search
        :rtype: ``osid.acknowledgement.BillingSearch``

        """
        raise UNIMPLEMENTED()

    billing_search = property(fget=get_billing_search)

    def get_billing_search_order(self):
        """Gets a billing search order.
        The ``BillingSearchOrder`` is supplied to a ``BillingSearch`` to
        specify the ordering of results.


        :return: the billing search order
        :rtype: ``osid.acknowledgement.BillingSearchOrder``

        """
        raise UNIMPLEMENTED()

    billing_search_order = property(fget=get_billing_search_order)

    def get_billings_by_search(self, billing_query, billing_search):
        """Gets the search results matching the given search.

        :param billing_query: the billing query
        :type billing_query: ``osid.acknowledgement.BillingQuery``
        :param billing_search: the billing search
        :type billing_search: ``osid.acknowledgement.BillingSearch``
        :return: the search results
        :rtype: ``osid.acknowledgement.BillingSearchResults``
        :raise: ``NullArgument`` -- ``billing_query`` or ``billing_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``billing_query`` or ``billing_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_billing_query_from_inspector(self, billing_query_inspector):
        """Gets a billing query from an inspector.
        The inspector is available from a ``BillingSearchResults``.


        :param billing_query_inspector: a billing query inspector
        :type billing_query_inspector: ``osid.acknowledgement.BillingQueryInspector``
        :return: the billing query
        :rtype: ``osid.acknowledgement.BillingQuery``
        :raise: ``NullArgument`` -- ``billing_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``ibilling_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingAdminSession

    def can_create_billings(self):
        """Tests if this user can create ``Billings``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Billing`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Billing`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_billing_with_record_types(self, billing_record_types):
        """Tests if this user can create a single ``Billing`` using the desired record types.
        While ``AcknowledgementManager.getBillingRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Billing``. Providing an empty array tests if a ``Billing`` can
        be created with no records.


        :param billing_record_types: array of types
        :type billing_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Billing`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``billing_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_billing_form_for_create(self, billing_record_types):
        """Gets the billing form for creating new billings.
        A new form should be requested for each create transaction.


        :param billing_record_types: array of types
        :type billing_record_types: ``osid.type.Type[]``
        :return: the billing form
        :rtype: ``osid.acknowledgement.BillingForm``
        :raise: ``NullArgument`` -- ``billing_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- cannot get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_billing(self, billing_form):
        """Creates a new ``Billing``.

        :param billing_form: the form for this ``Billing``
        :type billing_form: ``osid.acknowledgement.BillingForm``
        :return: the new ``Billing``
        :rtype: ``osid.acknowledgement.Billing``
        :raise: ``IllegalState`` -- ``billing_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``billing_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``billing_form`` did not originate from ``get_billing_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_billings(self):
        """Tests if this user can update ``Billings``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Billing`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Billing`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_billing_form_for_update(self, billing_id):
        """Gets the billing form for updating an existing billing.
        A new billing form should be requested for each update
        transaction.


        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: the billing form
        :rtype: ``osid.acknowledgement.BillingForm``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_billing(self, billing_form):
        """Updates an existing billing.

        :param billing_form: the form containing the elements to be updated
        :type billing_form: ``osid.acknowledgement.BillingForm``
        :raise: ``IllegalState`` -- ``billing_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``billing_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``billing_form did not originate from get_billing_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_billings(self):
        """Tests if this user can delete ``Billings`` A return of true does not guarantee successful authorization.
        A return of false indicates that it is known deleting a
        ``Billing`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Billing`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_billing(self, billing_id):
        """Deletes a ``Billing``.

        :param billing_id: the ``Id`` of the ``Billing`` to remove
        :type billing_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``billing_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_billing_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Billings``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Billing`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_billing(self, billing_id, alias_id):
        """Adds an ``Id`` to a ``Billing`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Item`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another billing, it is reassigned to
        the given billing ``Id``.


        :param billing_id: the ``Id`` of a ``Billing``
        :type billing_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``billing_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingNotificationSession

    def can_register_for_billing_notifications(self):
        """Tests if this user can register for ``Billing`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_billing_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_billing_notification()`` .




        """
        raise UNIMPLEMENTED()

    def unreliable_billing_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.




        """
        raise UNIMPLEMENTED()

    def acknowledge_billing_notification(self, notification_id):
        """Acknowledge a billing notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_billings(self):
        """Register for notifications of new billings.
        ``BillingReceiver.newBillings()`` is invoked when a new
        ``Billing`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billings(self):
        """Registers for notification of updated billings.
        ``BillingReceiver.changedBillings()`` is invoked when a billing
        is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billing(self, billing_id):
        """Registers for notification of an updated billing.
        ``BillingReceiver.changedBillings()`` is invoked when the
        specified billing is changed.


        :param billing_id: the ``Id`` of the ``Billing`` to monitor
        :type billing_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_billings(self):
        """Registers for notification of deleted billings.
        ``BillingReceiver.deletedBillings()`` is invoked when a billing
        is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_billing(self, billing_id):
        """Registers for notification of a deleted billing.
        ``BillingReceiver.deletedBillings()`` is invoked when the
        specified billing is deleted.


        :param billing_id: the ``Id`` of the ``Billing`` to monitor
        :type billing_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billing_hierarchy(self):
        """Registers for notification of an updated billing hierarchy structure.
        ``BillingReceiver.changedChildOfBillings()`` is invoked when a
        node experiences a change in its children.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billing_hierarchy_for_ancestors(self, billing_id):
        """Registers for notification of an updated billing hierarchy structure.
        ``BillingReceiver.changedChildOfBillings()`` is invoked when the
        specified node or any of its ancestors experiences a change in
        its children.


        :param billing_id: the ``Id`` of the ``Billing`` node to monitor
        :type billing_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_billing_hierarchy_for_descendants(self, billing_id):
        """Registers for notification of an updated billing hierarchy structure.
        ``BillingReceiver.changedChildOfBillings()`` is invoked when the
        specified node or any of its descendants experiences a change in
        its children.


        :param billing_id: the ``Id`` of the ``Billing`` node to monitor
        :type billing_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingHierarchySession

    def get_billing_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    billing_hierarchy_id = property(fget=get_billing_hierarchy_id)

    def get_billing_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    billing_hierarchy = property(fget=get_billing_hierarchy)

    def can_access_billing_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_billing_ids(self):
        """Gets the root billing ``Ids`` in this hierarchy.

        :return: the root billing ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_billing_ids = property(fget=get_root_billing_ids)

    def get_root_billings(self):
        """Gets the root billings in the billing hierarchy.
        A node with no parents is an orphan. While all billing ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.


        :return: the root billings
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_billings = property(fget=get_root_billings)

    def has_parent_billings(self, billing_id):
        """Tests if the ``Billing`` has any parents.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if the billing has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_billing(self, id_, billing_id):
        """Tests if an ``Id`` is a direct parent of billing.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``billing_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_billing_ids(self, billing_id):
        """Gets the parent ``Ids`` of the given billing.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the billing
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_billings(self, billing_id):
        """Gets the parent billings of the given ``id``.

        :param billing_id: the ``Id`` of the ``Billing`` to query
        :type billing_id: ``osid.id.Id``
        :return: the parent billings of the ``id``
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NotFound`` -- a ``Billing`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_billing(self, id_, billing_id):
        """Tests if an ``Id`` is an ancestor of a billing.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``billing_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_billings(self, billing_id):
        """Tests if a billing has any children.

        :param billing_id: a billing ``Id``
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if the ``billing_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``bobilling_id is null ok_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_billing(self, id_, billing_id):
        """Tests if a billing is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``billing_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_billing_ids(self, billing_id):
        """Gets the child ``Ids`` of the given billing.

        :param billing_id: the ``Id`` to query
        :type billing_id: ``osid.id.Id``
        :return: the children of the billing
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_billings(self, billing_id):
        """Gets the child billings of the given ``id``.

        :param billing_id: the ``Id`` of the ``Billing`` to query
        :type billing_id: ``osid.id.Id``
        :return: the child billings of the ``id``
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NotFound`` -- a ``Billing`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_billing(self, id_, billing_id):
        """Tests if an ``Id`` is a descendant of a billing.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``billing_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billing_node_ids(self, billing_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given billing.

        :param billing_id: the ``Id`` to query
        :type billing_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a billing node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billing_nodes(self, billing_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given billing.

        :param billing_id: the ``Id`` to query
        :type billing_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a billing node
        :rtype: ``osid.acknowledgement.BillingNode``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.BillingHierarchyDesignSession

    def can_modify_billing_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.


        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_billing(self, billing_id):
        """Adds a root billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``billing_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_billing(self, billing_id):
        """Removes a root billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_billing(self, billing_id, child_id):
        """Adds a child to a billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``billing_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``billing_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``billing_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_billing(self, billing_id, child_id):
        """Removes a child from a billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``billing_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``billing_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_billings(self, billing_id):
        """Removes all children from a billing.

        :param billing_id: the ``Id`` of a billing
        :type billing_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Billing(osid_objects.OsidCatalog, osid_sessions.OsidSession):

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
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.CreditLookupSession

    def get_billing_id(self):
        """Gets the ``Billing``  ``Id`` associated with this session.

        :return: the ``Billing Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    billing_id = property(fget=get_billing_id)

    def get_billing(self):
        """Gets the ``Billing`` associated with this session.

        :return: the billing
        :rtype: ``osid.acknowledgement.Billing``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    billing = property(fget=get_billing)

    def can_lookup_credits(self):
        """Tests if this user can examine this billing.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if billing reading methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_credit_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_credit_view(self):
        """A complete view of the ``Credit`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_billing_view(self):
        """Federates the view for methods in this session.
        A federated view will include credits in billings which are
        children of this billing in the billing hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_billing_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this billing only.



        """
        raise UNIMPLEMENTED()

    def use_effective_credit_view(self):
        """Only credits whose effective dates are current are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_effective_credit_view(self):
        """All credits of any effective dates are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_credit(self, credit_id):
        """Gets the ``Credit`` specified by its ``Id``.

        :param credit_id: the ``Id`` of the ``Credit`` to retrieve
        :type credit_id: ``osid.id.Id``
        :return: the returned ``Credit``
        :rtype: ``osid.acknowledgement.Credit``
        :raise: ``NotFound`` -- no ``Credit`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_ids(self, credit_ids):
        """Gets a ``CreditList`` corresponding to the given ``IdList``.

        :param credit_ids: the list of ``Ids`` to retrieve
        :type credit_ids: ``osid.id.IdList``
        :return: the returned ``Credit list``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``credit_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_genus_type(self, credit_genus_type):
        """Gets a ``CreditList`` corresponding to the given credit genus ``Type`` which does not include credits of types derived from the specified ``Type``.

        :param credit_genus_type: a credits genus type
        :type credit_genus_type: ``osid.type.Type``
        :return: the returned ``Credit list``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``credit_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_parent_genus_type(self, credit_genus_type):
        """Gets a ``CreditList`` corresponding to the given credit genus ``Type`` and include any additional credits with genus types derived from the specified ``Type``.

        :param credit_genus_type: a credit genus type
        :type credit_genus_type: ``osid.type.Type``
        :return: the returned ``Credit list``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``credit_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_record_type(self, credit_record_type):
        """Gets a ``CreditList`` containing the given credit record ``Type``.

        :param credit_record_type: a credit record type
        :type credit_record_type: ``osid.type.Type``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``credit_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_on_date(self, from_, to):
        """Gets a ``CreditList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from or to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_genus_type_on_date(self, credit_genus_type, from_, to):
        """Gets a list of credits of the given genus type and effective entire given date range inclusive but not confined to the date range.

        :param credit_genus_type: a credit genus ``Type``
        :type credit_genus_type: ``osid.type.Type``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``credit_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_for_resource(self, resource_id):
        """Gets a ``CreditList`` for the given resource ``Id``.

        :param resource_id: the ``Id`` of the resource
        :type resource_id: ``osid.id.Id``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_for_resource_on_date(self, resource_id, from_, to):
        """Gets a list of credits for a resource and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_genus_type_for_resource(self, resource_id, credit_genus_type):
        """Gets a list of credits by a genus type for a resource.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param credit_genus_type: a credit genus ``Type``
        :type credit_genus_type: ``osid.type.Type``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``credit_genus_type`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_genus_type_for_resource_on_date(self, resource_id, credit_genus_type, from_, to):
        """Gets a list of credits by genus type for a resource and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param credit_genus_type: a credit genus ``Type``
        :type credit_genus_type: ``osid.type.Type``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, credit_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_for_reference(self, reference_id):
        """Gets a ``CreditList`` for the given reference ``Id``.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_for_reference_on_date(self, reference_id, from_, to):
        """Gets a list of credits for a reference and effective entire given date range inclusive but not confined to the date range.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``reference_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_genus_type_for_reference(self, reference_id, credit_genus_type):
        """Gets a list of credits by a genus type for a reference.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param credit_genus_type: a credit genus ``Type``
        :type credit_genus_type: ``osid.type.Type``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``reference_id`` or ``credit_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_genus_type_for_reference_on_date(self, reference_id, credit_genus_type, from_, to):
        """Gets a list of credits of the given genus type for a reference and effective entire given date range inclusive but not confined to the date range.

        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param credit_genus_type: a credit genus ``Type``
        :type credit_genus_type: ``osid.type.Type``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``reference_id, credit_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_for_resource_and_reference(self, resource_id, reference_id):
        """Gets a ``CreditList`` for the given resource and reference.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_for_resource_and_reference_on_date(self, resource_id, reference_id, from_, to):
        """Gets a ``CreditList`` corresponding to the given resource and reference and effective entire given date range inclusive but not confined to the date range.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_genus_type_for_resource_and_reference(self, resource_id, reference_id, credit_genus_type):
        """Gets a ``CreditList`` of the given genus type for the given resource and reference.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param credit_genus_type: a credit genus ``Type``
        :type credit_genus_type: ``osid.type.Type``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``resource_id,``  ``reference_id,`` or ``credit_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_genus_type_for_resource_and_reference_on_date(self, resource_id, reference_id, credit_genus_type, from_, to):
        """Gets a ``CreditList`` of the given genus type corresponding to the given resource and reference and effective entire given date range inclusive but not confined to the date range.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param reference_id: a reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param credit_genus_type: a credit genus ``Type``
        :type credit_genus_type: ``osid.type.Type``
        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, reference_id,``  ``credit_genus_type,``  ``from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits(self):
        """Gets all credits.

        :return: a list of credits
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    credits = property(fget=get_credits)


##
# The following methods are from osid.acknowledgement.CreditQuerySession

    def can_search_credits(self):
        """Tests if this user can perform ``Credit`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may wish not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_credit_query(self):
        """Gets a credit query.

        :return: the credit query
        :rtype: ``osid.acknowledgement.CreditQuery``

        """
        raise UNIMPLEMENTED()

    credit_query = property(fget=get_credit_query)

    def get_credits_by_query(self, credit_query):
        """Gets a list of credits matching the given credit query.

        :param credit_query: the credit query
        :type credit_query: ``osid.acknowledgement.CreditQuery``
        :return: the returned ``CreditList``
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``credit_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``credit_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.CreditSearchSession

    def get_credit_search(self):
        """Gets a credit search.

        :return: the credit search
        :rtype: ``osid.acknowledgement.CreditSearch``

        """
        raise UNIMPLEMENTED()

    credit_search = property(fget=get_credit_search)

    def get_credit_search_order(self):
        """Gets a credit search order.
        The ``CreditSearchOrder`` is supplied to a ``CreditSearch`` to
        specify the ordering of results.

        :return: the credit search order
        :rtype: ``osid.acknowledgement.CreditSearchOrder``

        """
        raise UNIMPLEMENTED()

    credit_search_order = property(fget=get_credit_search_order)

    def get_credits_by_search(self, credit_query, credit_search):
        """Gets the search results matching the given search.

        :param credit_query: the credit query
        :type credit_query: ``osid.acknowledgement.CreditQuery``
        :param credit_search: the credit search
        :type credit_search: ``osid.acknowledgement.CreditSearch``
        :return: the search results
        :rtype: ``osid.acknowledgement.CreditSearchResults``
        :raise: ``NullArgument`` -- ``credit_query`` or ``credit_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``credit_query`` or ``credit_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_credit_query_from_inspector(self, credit_query_inspector):
        """Gets a credit query from an inspector.
        The inspector is available from a ``CreditSearchResults``.

        :param credit_query_inspector: a credit query inspector
        :type credit_query_inspector: ``osid.acknowledgement.CreditQueryInspector``
        :return: the credit query
        :rtype: ``osid.acknowledgement.CreditQuery``
        :raise: ``NullArgument`` -- ``credit_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``credit_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.CreditAdminSession

    def can_create_credits(self):
        """Tests if this user can create credits.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Credit``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Credit`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_credit_with_record_types(self, credit_record_types):
        """Tests if this user can create a single ``Credit`` using the desired record types.
        While ``AcknowledgementManager.getCreditRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific ``Credit``.
        Providing an empty array tests if a ``Credit`` can be created
        with no records.

        :param credit_record_types: array of credit record types
        :type credit_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Credit`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``credit_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_credit_form_for_create(self, reference_id, resource_id, credit_record_types):
        """Gets the credit form for creating new credits.
        A new form should be requested for each create transaction.

        :param reference_id: the reference ``Id``
        :type reference_id: ``osid.id.Id``
        :param resource_id: the resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param credit_record_types: array of credit record types to be included in the create operation or an empty list if none
        :type credit_record_types: ``osid.type.Type[]``
        :return: the credit form
        :rtype: ``osid.acknowledgement.CreditForm``
        :raise: ``NotFound`` -- ``reference_id`` or ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``reference_id, resource_id`` or ``credit_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- cannot get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_credit(self, credit_form):
        """Creates a new ``Credit``.

        :param credit_form: the form for this ``Credit``
        :type credit_form: ``osid.acknowledgement.CreditForm``
        :return: the new ``Credit``
        :rtype: ``osid.acknowledgement.Credit``
        :raise: ``IllegalState`` -- ``credit_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``credit_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``credit_form`` did not originate from ``get_credit_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_credits(self):
        """Tests if this user can update credits.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Credit``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Credit`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_credit_form_for_update(self, credit_id):
        """Gets the credit form for updating an existing credit.
        A new credit form should be requested for each update
        transaction.

        :param credit_id: the ``Id`` of the ``Credit``
        :type credit_id: ``osid.id.Id``
        :return: the credit form
        :rtype: ``osid.acknowledgement.CreditForm``
        :raise: ``NotFound`` -- ``credit_id`` is not found
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_credit(self, credit_form):
        """Updates an existing credit.

        :param credit_form: the form containing the elements to be updated
        :type credit_form: ``osid.acknowledgement.CreditForm``
        :raise: ``IllegalState`` -- ``credit_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``credit_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``credit_form`` did not originate from ``get_credit_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_credits(self):
        """Tests if this user can delete credits.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Credit`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Credit`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_credit(self, credit_id):
        """Deletes a ``Credit``.

        :param credit_id: the ``Id`` of the ``Credit`` to remove
        :type credit_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``credit_id`` not found
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_credit_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Credits``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Credit`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_credit(self, credit_id, alias_id):
        """Adds an ``Id`` to a ``Credit`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Credit`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another credit, it is reassigned to
        the given credit ``Id``.

        :param credit_id: the ``Id`` of a ``Credit``
        :type credit_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``credit_id`` not found
        :raise: ``NullArgument`` -- ``credit_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.CreditNotificationSession

    def can_register_for_credit_notifications(self):
        """Tests if this user can register for ``Credit`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def reliable_credit_notifications(self):
        """Reliable notifications are desired.
        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_credit_notification()`` .



        """
        raise UNIMPLEMENTED()

    def unreliable_credit_notifications(self):
        """Unreliable notifications are desired.
        In unreliable mode, notifications do not need to be
        acknowledged.



        """
        raise UNIMPLEMENTED()

    def acknowledge_credit_notification(self, notification_id):
        """Acknowledge a credit notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_credits(self):
        """Register for notifications of new credits.
        ``CreditReceiver.newCredits()`` is invoked when a new ``Credit``
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_credits_by_genus_type(self, credit_genus_type):
        """Register for notifications of new credits by the given credit genus ``Type``.
        ``CreditReceiver.newCredits()`` is invoked when a new ``Credit``
        appears in this billing.

        :param credit_genus_type: the ``Id`` of the reference to monitor
        :type credit_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``credit_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_credits_for_reference(self, reference_id):
        """Register for notifications of new credits for the given reference ``Id``.
        ``CreditReceiver.newCredits()`` is invoked when a new ``Credit``
        appears in this billing.

        :param reference_id: the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_credits_for_resource(self, resource_id):
        """Register for notifications of new credits for the given resource ``Id``.
        ``CreditReceiver.newCredits()`` is invoked when a new ``Credit``
        appears in this billing.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_credits(self):
        """Registers for notification of updated credits.
        ``CreditReceiver.changedCredits()`` is invoked when a credit in
        this billing is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_credits_by_genus_type(self, credit_genus_type):
        """Register for notifications of changed credits by the given credit gfenus ``Type``.
        ``CreditReceiver.changedCredits()`` is invoked when a ``Credit``
        for the reference in this billing is changed.

        :param credit_genus_type: the genus type of the credit to monitor
        :type credit_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``credit_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_credits_for_reference(self, reference_id):
        """Register for notifications of changed credits for the given reference ``Id``.
        ``CreditReceiver.changedCredits()`` is invoked when a ``Credit``
        for the reference in this billing is changed.

        :param reference_id: the ``Id`` of the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_credits_for_resource(self, resource_id):
        """Register for notifications of changed credits for the given resource ``Id``.
        ``CreditReceiver.changedCredits()`` is invoked when a ``Credit``
        for the resource is changed in this billing.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_credit(self, credit_id):
        """Registers for notification of an updated credit.
        ``CreditReceiver.changedCredits()`` is invoked when the
        specified credit in this billing is changed.

        :param credit_id: the ``Id`` of the ``Credit`` to monitor
        :type credit_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a credit was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_credits(self):
        """Registers for notification of deleted credits.
        ``CreditReceiver.deletedCredit()`` is invoked when a credit is
        removed from this billing.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_credits_by_genus_type(self, credit_genus_type):
        """Register for notifications of deleted credits by the credit genus ``Type``.
        ``CreditReceiver.deletedCredit()`` is invoked when a ``Credit``
        for the reference is removed from this billing.

        :param credit_genus_type: the genus type of the credit to monitor
        :type credit_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``credit_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_credits_for_reference(self, reference_id):
        """Register for notifications of deleted credits for the given reference ``Id``.
        ``CreditReceiver.deletedCredit()`` is invoked when a ``Credit``
        for the reference is removed from this billing.

        :param reference_id: the ``Id`` of the reference to monitor
        :type reference_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_credits_for_resource(self, resource_id):
        """Register for notifications of deleted credits for the given resource ``Id``.
        ``CreditReceiver.deletedCredit()`` is invoked when a ``Credit``
        for the resource is removed from this billing.

        :param resource_id: the ``Id`` of the resource to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_credit(self, credit_id):
        """Registers for notification of a deleted credit.
        ``CreditReceiver.deletedCredit()`` is invoked when the specified
        credit is removed from this billing.

        :param credit_id: the ``Id`` of the ``Credit`` to monitor
        :type credit_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a credit was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.CreditBillingSession

    def can_lookup_credit_billing_mappings(self):
        """Tests if this user can perform lookups of credit/billing mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intendedas a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_billing_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_billing_view(self):
        """A complete view of the ``Credit`` and ``Billing`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_credit_ids_by_billing(self, billing_id):
        """Gets the list of Credit Ids associated with a ``Billing``.

        :param billing_id: ``Id`` of a ``Billings``.
        :type billing_id: ``osid.id.Id``
        :return: list of related credit ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_billing(self, billing_id):
        """Gets the list of ``Credits`` associated with a ``Billing``.

        :param billing_id: ``Id`` of a ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: list of related credits
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NotFound`` -- ``billing_id`` is not found
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credit_ids_by_billings(self, billing_ids):
        """Gets the list of ``Credit Ids`` corresponding to a list of ``Billing`` objects.

        :param billing_ids: list of billing ``Ids``
        :type billing_ids: ``osid.id.IdList``
        :return: list of credit ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``billing_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_credits_by_billings(self, billing_ids):
        """Gets the list of ``Credits`` corresponding to a list of ``Billings``.

        :param billing_ids: list of billing ``Ids``
        :type billing_ids: ``osid.id.IdList``
        :return: list of credits
        :rtype: ``osid.acknowledgement.CreditList``
        :raise: ``NullArgument`` -- ``billing_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billing_ids_by_credit(self, credit_id):
        """Gets the list of ``Billing``  ``Ids`` mapped to a ``Credit``.

        :param credit_id: ``Id`` of a ``Credit``
        :type credit_id: ``osid.id.Id``
        :return: list of billing ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``credit_id`` is not found
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_billings_by_credit(self, credit_id):
        """Gets the list of ``Billing`` objects mapped to a ``Credit``.

        :param credit_id: ``Id`` of a ``Credit``
        :type credit_id: ``osid.id.Id``
        :return: list of billings
        :rtype: ``osid.acknowledgement.BillingList``
        :raise: ``NotFound`` -- ``credit_id`` is not found
        :raise: ``NullArgument`` -- ``credit_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.CreditBillingAssignmentSession

    def can_assign_credits(self):
        """Tests if this user can alter credit/billing mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_credits_to_billing(self, billing_id):
        """Tests if this user can alter credit/billing mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_billing_ids(self, billing_id):
        """Gets a list of billings including and under the given billing node in which any credit can be assigned.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :return: list of assignable billing ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_billing_ids_for_credit(self, billing_id, credit_id):
        """Gets a list of billings including and under the given billing node in which a specific credit can be assigned.

        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :param credit_id: the ``Id`` of the ``Credit``
        :type credit_id: ``osid.id.Id``
        :return: list of assignable billing ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``billing_id`` or ``credit_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_credit_to_billing(self, credit_id, billing_id):
        """Adds an existing ``Credit`` to a ``Billing``.

        :param credit_id: the ``Id`` of the ``Credit``
        :type credit_id: ``osid.id.Id``
        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``credit_id`` already assigned to ``billing_id``
        :raise: ``NotFound`` -- ``credit_id`` or ``billing_id`` not found
        :raise: ``NullArgument`` -- ``credit_id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_credit_from_billing(self, credit_id, billing_id):
        """Removes a ``Credit`` from a ``Billing``.

        :param credit_id: the ``Id`` of the ``Credit``
        :type credit_id: ``osid.id.Id``
        :param billing_id: the ``Id`` of the ``Billing``
        :type billing_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``credit_id`` or ``billing_id`` not found or ``credit_id`` not mapped to ``billing_id``
        :raise: ``NullArgument`` -- ``credit_id`` or ``billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def reassign_credit_to_billing(self, credit_id, from_billing_id, to_biilling_id):
        """Moves a ``Credit`` from one ``Billing`` to another.
        Mappings to other ``Billings`` are unaffected.

        :param credit_id: the ``Id`` of the ``Credit``
        :type credit_id: ``osid.id.Id``
        :param from_billing_id: the ``Id`` of the current ``Billing``
        :type from_billing_id: ``osid.id.Id``
        :param to_biilling_id: the ``Id`` of the destination ``Billing``
        :type to_biilling_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``credit_id, from_billing_id,`` or ``to_billing_id`` not found or ``credit_id`` not mapped to ``from_billing_id``
        :raise: ``NullArgument`` -- ``credit_id, billing_id,`` or ``to_billing_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.acknowledgement.CreditSmartBillingSession

    def can_manage_smart_billings(self):
        """Tests if this user can manage smart billings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart billing management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_credit_query(self, credit_query):
        """Applies a credit query to this billing.

        :param credit_query: the credit query
        :type credit_query: ``osid.acknowledgement.CreditQuery``
        :raise: ``NullArgument`` -- ``credit_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``credit_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_credit_query(self):
        """Gets a credit query inspector for this billing.

        :return: the credit query inspector
        :rtype: ``osid.acknowledgement.CreditQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_credit_sequencing(self, credit_search_order):
        """Applies a credit search order to this billing.

        :param credit_search_order: the credit search order
        :type credit_search_order: ``osid.acknowledgement.CreditSearchOrder``
        :raise: ``NullArgument`` -- ``credit_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``credit_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class BillingList(osid_objects.OsidList):

    def get_next_billing(self):
        """Gets the next ``Billing`` in this list.

        :return: the next ``Billing`` in this list. The ``has_next()`` method should be used to test that a next ``Billing`` is available before calling this method.
        :rtype: ``osid.acknowledgement.Billing``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

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
        raise UNIMPLEMENTED()



class Billings(AcknowledgementManager):
    pass


