# -*- coding: utf-8 -*-
"""Relationship Open Service Interface Definitions
relationship version 3.0.0

The Relationship OSID provides the ability to relate and manage data
between ``OsidObjects``.

Relationships

The Relationship OSID defines a ``Relationship`` that can be used to
explicitly identify a relationship between two OSID ``Ids`` and manage
information specific to the relationship.

The Relationship OSID is a building block on which relationships defined
in the context of other OSIDs can be built. Examples of relationships
include the enrollment record of a student in a ``Course`` or the
commitment or a person to an ``Event``.

The Relationship OSID depends on the relationship Type to indicate the
nature of the relationship including its natural ordering between the
source and destination ``Ids``. A relationship of type "friend" may
place the peers in either order and be queryable in either order. A
relationship of type "parent" is between a father peer and a son peer,
but not the other way around. Queries of the son peer based on the
"parent" type is not equiavelent to queries of the father peer based on
the "parent" type.

Such directional relationships may be accompanied by two types. An
additional relationship type of "child" can be used with the son peer to
determine the father peer. The directionality and the inverse among the
types are part of the type definition.

Family Cataloging

``Relationships`` may be cataloged using the ``Family`` interface.

Sub Packages

The Relationship OSID includes a Relationship Rules OSID for controlling
the enable status of ``Relationships``.

"""
from . import osid
from .osid_errors import Unimplemented, IllegalState, OperationFailed


class RelationshipProfile(osid.OsidProfile):

    def supports_visible_federation(self):
        """Tests if any family federation is exposed.
        Federation is exposed when a specific family may be identified,
        selected and used to create a lookup or admin session.
        Federation is not exposed when a set of families appears as a
        single family.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_lookup(self):
        """Tests if looking up relationships is supported.

        :return: ``true`` if relationship lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_query(self):
        """Tests if querying relationships is supported.

        :return: ``true`` if relationship query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_search(self):
        """Tests if searching relationships is supported.

        :return: ``true`` if relationship search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_admin(self):
        """Tests if relationship administrative service is supported.

        :return: ``true`` if relationship administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_notification(self):
        """Tests if a relationship notification service is supported.

        :return: ``true`` if relationship notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_family(self):
        """Tests if a relationship family cataloging service is supported.

        :return: ``true`` if relationship families are supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_family_assignment(self):
        """Tests if a relationship cataloging service is supported.
        A relationship cataloging service maps relationships to
        families.

        :return: ``true`` if relationship families are supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_smart_family(self):
        """Tests if a relationship smart family cataloging service is supported.

        :return: ``true`` if relationship smart families are supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_family_lookup(self):
        """Tests if looking up families is supported.

        :return: ``true`` if family lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_family_query(self):
        """Tests if querying families is supported.

        :return: ``true`` if family query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_family_search(self):
        """Tests if searching families is supported.

        :return: ``true`` if family search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_family_admin(self):
        """Tests if familyadministrative service is supported.

        :return: ``true`` if family administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_family_notification(self):
        """Tests if a family notification service is supported.

        :return: ``true`` if family notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_family_hierarchy(self):
        """Tests for the availability of a family hierarchy traversal service.

        :return: ``true`` if family hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_family_hierarchy_design(self):
        """Tests for the availability of a family hierarchy design service.

        :return: ``true`` if family hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_batch(self):
        """Tests for the availability of a relationship batch service.

        :return: ``true`` if a relationship batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relationship_rules(self):
        """Tests if a relationship rules service is supported.

        :return: ``true`` if relationship rules service is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_relationship_record_types(self):
        """Gets the supported ``Relationship`` record types.

        :return: a list containing the supported ``Relationship`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    relationship_record_types = property(fget=get_relationship_record_types)

    def supports_relationship_record_type(self, relationship_record_type):
        """Tests if the given ``Relationship`` record type is supported.

        :param relationship_record_type: a ``Type`` indicating a ``Relationship`` record type
        :type relationship_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_relationship_search_record_types(self):
        """Gets the supported ``Relationship`` search record types.

        :return: a list containing the supported ``Relationship`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    relationship_search_record_types = property(fget=get_relationship_search_record_types)

    def supports_relationship_search_record_type(self, relationship_search_record_type):
        """Tests if the given ``Relationship`` search record type is supported.

        :param relationship_search_record_type: a ``Type`` indicating a ``Relationship`` search record type
        :type relationship_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relationship_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_family_record_types(self):
        """Gets the supported ``Family`` record types.

        :return: a list containing the supported ``Family`` types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    family_record_types = property(fget=get_family_record_types)

    def supports_family_record_type(self, family_record_type):
        """Tests if the given ``Family`` record type is supported.

        :param family_record_type: a ``Type`` indicating a ``Family`` record type
        :type family_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_family_search_record_types(self):
        """Gets the supported ``Family`` search record types.

        :return: a list containing the supported ``Family`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    family_search_record_types = property(fget=get_family_search_record_types)

    def supports_family_search_record_type(self, family_search_record_type):
        """Tests if the given ``Family`` search record type is supported.

        :param family_search_record_type: a ``Type`` indicating a ``Family`` search record type
        :type family_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``family_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class RelationshipManager(osid.OsidManager, osid.OsidSession, RelationshipProfile):

    def get_relationship_lookup_session(self):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_lookup_session = property(fget=get_relationship_lookup_session)

    def get_relationship_lookup_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_query_session(self):
        """Gets the ``OsidSession`` associated with the relationship query service.

        :return: a ``RelationshipQuerySession``
        :rtype: ``osid.relationship.RelationshipQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_query_session = property(fget=get_relationship_query_session)

    def get_relationship_query_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship query service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipQuerySession``
        :rtype: ``osid.relationship.RelationshipQuerySession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_search_session(self):
        """Gets the ``OsidSession`` associated with the relationship search service.

        :return: a ``RelationshipSearchSession``
        :rtype: ``osid.relationship.RelationshipSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_search_session = property(fget=get_relationship_search_session)

    def get_relationship_search_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship search service for the given family.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipSearchSession``
        :rtype: ``osid.relationship.RelationshipSearchSession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_admin_session(self):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_admin_session = property(fget=get_relationship_admin_session)

    def get_relationship_admin_session_for_family(self, family_id):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_notification_session(self, relationship_receiver):
        """Gets the ``OsidSession`` associated with the relationship notification service.

        :param relationship_receiver: the receiver
        :type relationship_receiver: ``osid.relationship.RelationshipReceiver``
        :return: a ``RelationshipNotificationSession``
        :rtype: ``osid.relationship.RelationshipNotificationSession``
        :raise: ``NullArgument`` -- ``relationship_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_notification_session_for_family(self, relationship_receiver, family_id):
        """Gets the ``OsidSession`` associated with the relationship notification service for the given family.

        :param relationship_receiver: the receiver
        :type relationship_receiver: ``osid.relationship.RelationshipReceiver``
        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipNotificationSession``
        :rtype: ``osid.relationship.RelationshipNotificationSession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``relationship_receiver`` or ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_family_session(self):
        """Gets the ``OsidSession`` to lookup relationship/family mappings.

        :return: a ``RelationshipFamilySession``
        :rtype: ``osid.relationship.RelationshipFamilySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_family()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_family_session = property(fget=get_relationship_family_session)

    def get_relationship_family_assignment_session(self):
        """Gets the ``OsidSession`` associated with assigning relationships to families.

        :return: a ``RelationshipFamilyAssignmentSession``
        :rtype: ``osid.relationship.RelationshipFamilyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_family_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_family_assignment_session = property(fget=get_relationship_family_assignment_session)

    def get_relationship_smart_family_session(self, family_id):
        """Gets the ``OsidSession`` to manage dynamic families of retlationships.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: a ``RelationshipSmartFamilySession``
        :rtype: ``osid.relationship.RelationshipSmartFamilySession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_smart_family()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_lookup_session(self):
        """Gets the ``OsidSession`` associated with the family lookup service.

        :return: a ``FamilyLookupSession``
        :rtype: ``osid.relationship.FamilyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    family_lookup_session = property(fget=get_family_lookup_session)

    def get_family_query_session(self):
        """Gets the ``OsidSession`` associated with the family query service.

        :return: a ``FamilyQuerySession``
        :rtype: ``osid.relationship.FamilyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    family_query_session = property(fget=get_family_query_session)

    def get_family_search_session(self):
        """Gets the ``OsidSession`` associated with the family search service.

        :return: a ``FamilySearchSession``
        :rtype: ``osid.relationship.FamilySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    family_search_session = property(fget=get_family_search_session)

    def get_family_admin_session(self):
        """Gets the ``OsidSession`` associated with the family administrative service.

        :return: a ``FamilyAdminSession``
        :rtype: ``osid.relationship.FamilyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    family_admin_session = property(fget=get_family_admin_session)

    def get_family_notification_session(self, family_receiver):
        """Gets the ``OsidSession`` associated with the family notification service.

        :param family_receiver: the receiver
        :type family_receiver: ``osid.relationship.FamilyReceiver``
        :return: a ``FamilyNotificationSession``
        :rtype: ``osid.relationship.FamilyNotificationSession``
        :raise: ``NullArgument`` -- ``family_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_hierarchy_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        :return: a ``FamilyHierarchySession`` for families
        :rtype: ``osid.relationship.FamilyHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    family_hierarchy_session = property(fget=get_family_hierarchy_session)

    def get_family_hierarchy_design_session(self):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        :return: a ``HierarchyDesignSession`` for families
        :rtype: ``osid.relationship.FamilyHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    family_hierarchy_design_session = property(fget=get_family_hierarchy_design_session)

    def get_relationship_batch_manager(self):
        """Gets the relationship batch manager.

        :return: a ``RelationshipBatchManager``
        :rtype: ``osid.relationship.batch.RelationshipBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_batch_manager = property(fget=get_relationship_batch_manager)

    def get_relationship_rules_manager(self):
        """Gets the relationship rules manager.

        :return: a ``RelationshipRulesManager``
        :rtype: ``osid.relationship.rules.RelationshipRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_rules_manager = property(fget=get_relationship_rules_manager)


##
# The following methods are from osid.relationship.FamilyLookupSession

    def can_lookup_families(self):
        """Tests if this user can perform ``Family`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_family_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_family_view(self):
        """A complete view of the ``Family`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_family(self, family_id):
        """Gets the ``Family`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Family`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Family`` and retained for compatibil

        :param family_id: ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: the family
        :rtype: ``osid.relationship.Family``
        :raise: ``NotFound`` -- ``family_id`` not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_families_by_ids(self, family_ids):
        """Gets a ``FamilyList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the families
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible families may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param family_ids: the list of ``Ids`` to retrieve
        :type family_ids: ``osid.id.IdList``
        :return: the returned ``Family list``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``family_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_families_by_genus_type(self, family_genus_type):
        """Gets a ``FamilyList`` corresponding to the given family genus ``Type`` which does not include families of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :param family_genus_type: a family genus type
        :type family_genus_type: ``osid.type.Type``
        :return: the returned ``Family list``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NullArgument`` -- ``family_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_families_by_parent_genus_type(self, family_genus_type):
        """Gets a ``FamilyList`` corresponding to the given family genus ``Type`` and include any additional families with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :param family_genus_type: a family genus type
        :type family_genus_type: ``osid.type.Type``
        :return: the returned ``Family list``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NullArgument`` -- ``family_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_families_by_record_type(self, family_record_type):
        """Gets a ``FamilyList`` containing the given family record ``Type``.
        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :param family_record_type: a family record type
        :type family_record_type: ``osid.type.Type``
        :return: the returned ``Family list``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_families_by_provider(self, resource_id):
        """Gets a ``FamilyList`` from the given provider.
        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Family list``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_families(self):
        """Gets all families.
        In plenary mode, the returned list contains all known families
        or an error results. Otherwise, the returned list may contain
        only those families that are accessible through this session.

        :return: a list of families
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    families = property(fget=get_families)


##
# The following methods are from osid.relationship.FamilyQuerySession

    def can_search_families(self):
        """Tests if this user can perform ``Family`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_family_query(self):
        """Gets a family query.

        :return: the family query
        :rtype: ``osid.relationship.FamilyQuery``

        """
        raise UNIMPLEMENTED()

    family_query = property(fget=get_family_query)

    def get_families_by_query(self, family_query):
        """Gets a list of ``Family`` objects matching the given family query.

        :param family_query: the family query
        :type family_query: ``osid.relationship.FamilyQuery``
        :return: the returned ``FamilyList``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NullArgument`` -- ``family_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``family_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.FamilySearchSession

    def get_family_search(self):
        """Gets a family search.

        :return: the family search
        :rtype: ``osid.relationship.FamilySearch``

        """
        raise UNIMPLEMENTED()

    family_search = property(fget=get_family_search)

    def get_family_search_order(self):
        """Gets a family search order.
        The ``FamilySearchOrder`` is supplied to a ``FamilySearch`` to
        specify the ordering of results.

        :return: the family search order
        :rtype: ``osid.relationship.FamilySearchOrder``

        """
        raise UNIMPLEMENTED()

    family_search_order = property(fget=get_family_search_order)

    def get_families_by_search(self, family_query, family_search):
        """Gets the search results matching the given search.

        :param family_query: the family query
        :type family_query: ``osid.relationship.FamilyQuery``
        :param family_search: the family search
        :type family_search: ``osid.relationship.FamilySearch``
        :return: the search results
        :rtype: ``osid.relationship.FamilySearchResults``
        :raise: ``NullArgument`` -- ``family_query`` or ``family_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``family_query`` or ``family_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_family_query_from_inspector(self, family_query_inspector):
        """Gets a family query from an inspector.
        The inspector is available from an ``FamilySearchResults``.

        :param family_query_inspector: a family query inspector
        :type family_query_inspector: ``osid.relationship.FamilyQueryInspector``
        :return: the familyh query
        :rtype: ``osid.relationship.FamilyQuery``
        :raise: ``NullArgument`` -- ``family_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``family_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.FamilyAdminSession

    def can_create_families(self):
        """Tests if this user can create families.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Family`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_family_with_record_types(self, family_record_types):
        """Tests if this user can create a single ``Family`` using the desired record types.
        While ``RelationshipManager.getFamilyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Family``.
        Providing an empty array tests if a ``Family`` can be created
        with no records.

        :param family_record_types: array of family record types
        :type family_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Family`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``family_record_types is null``

        """
        raise UNIMPLEMENTED()

    def get_family_form_for_create(self, family_record_types):
        """Gets the family form for creating new families.
        . A new form should be requested for each create transaction.

        :param family_record_types: array of family record types
        :type family_record_types: ``osid.type.Type[]``
        :return: the family form
        :rtype: ``osid.relationship.FamilyForm``
        :raise: ``NullArgument`` -- ``family_record_types is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_family(self, family_form):
        """Creates a new ``Family``.

        :param family_form: the form for this ``Family``.
        :type family_form: ``osid.relationship.FamilyForm``
        :return: the new ``Family``
        :rtype: ``osid.relationship.Family``
        :raise: ``IllegalState`` -- ``family_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``family_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``family_form`` did not originate from ``get_family_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_families(self):
        """Tests if this user can update families.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Family`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_family_form_for_update(self, family_id):
        """Gets the family form for updating an existing family.
        A new family form should be requested for each update
        transaction.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: the family form
        :rtype: ``osid.relationship.FamilyForm``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_family(self, family_form):
        """Updates an existing family.

        :param family_form: the form containing the elements to be updated
        :type family_form: ``osid.relationship.FamilyForm``
        :raise: ``IllegalState`` -- ``family_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``family_id`` or ``family_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``family_form`` did not originate from ``get_family_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_families(self):
        """Tests if this user can delete families.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Family``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Family`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_family(self, family_id):
        """Deletes a ``Family``.

        :param family_id: the ``Id`` of the ``Family`` to remove
        :type family_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``family_id`` not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_family_aliases(self):
        """Tests if this user can manage ``Id`` aliases for families.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Family`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_family(self, family_id, alias_id):
        """Adds an ``Id`` to a ``Family`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Family`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another family, it is
        reassigned to the given family ``Id``.

        :param family_id: the ``Id`` of a ``Family``
        :type family_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``family_id`` not found
        :raise: ``NullArgument`` -- ``family_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.FamilyNotificationSession

    def can_register_for_family_notifications(self):
        """Tests if this user can register for ``Family`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_families(self):
        """Register for notifications of new families.
        ``FamilyReceiver.newFamily()`` is invoked when a new ``Family``
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_family_ancestors(self, family_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified family.
        ``FamilyReceiver.newAncestorFamily()`` is invoked when the
        specified family node gets a new ancestor.

        :param family_id: the ``Id`` of the ``Family`` node to monitor
        :type family_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_family_descendants(self, family_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified family.
        ``FamilyReceiver.newDescendantFamily()`` is invoked when the
        specified family node gets a new descendant.

        :param family_id: the ``Id`` of the ``Family`` node to monitor
        :type family_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_families(self):
        """Registers for notification of updated families.
        ``FamilyReceiver.changedFamily()`` is invoked when a family is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_family(self, family_id):
        """Registers for notification of an updated family.
        ``FamilyReceiver.changedFamily()`` is invoked when the specified
        family is changed.

        :param family_id: the ``Id`` of the ``Family`` to monitor
        :type family_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_families(self):
        """Registers for notification of deleted families.
        ``FamilyReceiver.deletedFamily()`` is invoked when a family is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_family(self, family_id):
        """Registers for notification of a deleted family.
        ``FamilyReceiver.deletedFamily()`` is invoked when the specified
        family is deleted.

        :param family_id: the ``Id`` of the ``Family`` to monitor
        :type family_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``family_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_family_ancestors(self, family_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified family.
        ``FamilyReceiver.deletedAncestor()`` is invoked when the
        specified family node loses an ancestor.

        :param family_id: the ``Id`` of the ``Family`` to monitor
        :type family_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_family_descendants(self, family_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified family.
        ``FamilyReceiver.deletedDescendant()`` is invoked when the
        specified family node loses a descendant.

        :param family_id: the ``Id`` of the ``Family`` to monitor
        :type family_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.FamilyHierarchySession

    def get_family_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    family_hierarchy = property(fget=get_family_hierarchy)

    def can_access_family_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer hierrachy
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_family_ids(self):
        """Gets the root family ``Ids`` in this hierarchy.

        :return: the root family ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_family_ids = property(fget=get_root_family_ids)

    def get_root_families(self):
        """Gets the root families in the family hierarchy.
        A node with no parents is an orphan. While all family ``Ids``
        are known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root families
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_families = property(fget=get_root_families)

    def has_parent_families(self, family_id):
        """Tests if the ``Family`` has any parents.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :return: ``true`` if the family has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_family(self, id_, family_id):
        """Tests if an ``Id`` is a direct parent of a family.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``family_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_family_ids(self, family_id):
        """Gets the parent ``Ids`` of the given family.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the family
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_families(self, family_id):
        """Gets the parent families of the given ``id``.

        :param family_id: the ``Id`` of the ``Family`` to query
        :type family_id: ``osid.id.Id``
        :return: the parent families of the ``id``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NotFound`` -- a ``Family`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_family(self, id_, family_id):
        """Tests if an ``Id`` is an ancestor of a family.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``family_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_families(self, family_id):
        """Tests if a family has any children.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :return: ``true`` if the ``family_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_family(self, id_, family_id):
        """Tests if a family is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``family_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_family_ids(self, family_id):
        """Gets the child ``Ids`` of the given family.

        :param family_id: the ``Id`` to query
        :type family_id: ``osid.id.Id``
        :return: the children of the family
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_families(self, family_id):
        """Gets the child families of the given ``id``.

        :param family_id: the ``Id`` of the ``Family`` to query
        :type family_id: ``osid.id.Id``
        :return: the child families of the ``id``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NotFound`` -- a ``Family`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_family(self, id_, family_id):
        """Tests if an ``Id`` is a descendant of a family.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``family_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_family_node_ids(self, family_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given family.

        :param family_id: the ``Id`` to query
        :type family_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a family node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_family_nodes(self, family_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given family.

        :param family_id: the ``Id`` to query
        :type family_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a family node
        :rtype: ``osid.relationship.FamilyNode``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.FamilyHierarchyDesignSession

    def can_modify_family_hierarchy(self):
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

    def add_root_family(self, family_id):
        """Adds a root family.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``family_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``family_id`` not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_family(self, family_id):
        """Removes a root family.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``family_id`` not a root
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_family(self, family_id, child_id):
        """Adds a child to a family.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``family_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``family_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``family_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_family(self, family_id, child_id):
        """Removes a child from a family.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``family_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``family_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_families(self, family_id):
        """Removes all children from a family.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``family_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class RelationshipProxyManager(osid.OsidProxyManager, RelationshipProfile):

    def get_relationship_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_lookup_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship lookup service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipLookupSession``
        :rtype: ``osid.relationship.RelationshipLookupSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipQuerySession``
        :rtype: ``osid.relationship.RelationshipQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_query_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship query service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipQuerySession``
        :rtype: ``osid.relationship.RelationshipQuerySession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipSearchSession``
        :rtype: ``osid.relationship.RelationshipSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_search_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship search service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipSearchSession``
        :rtype: ``osid.relationship.RelationshipSearchSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relationship administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_admin_session_for_family(self, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship administration service for the given family.

        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipAdminSession``
        :rtype: ``osid.relationship.RelationshipAdminSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_notification_session(self, relationship_receiver, proxy):
        """Gets the ``OsidSession`` associated with the relationship notification service.

        :param relationship_receiver: the receiver
        :type relationship_receiver: ``osid.relationship.RelationshipReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipNotificationSession``
        :rtype: ``osid.relationship.RelationshipNotificationSession``
        :raise: ``NullArgument`` -- ``relationship_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_notification_session_for_family(self, relationship_receiver, family_id, proxy):
        """Gets the ``OsidSession`` associated with the relationship notification service for the given family.

        :param relationship_receiver: the receiver
        :type relationship_receiver: ``osid.relationship.RelationshipReceiver``
        :param family_id: the ``Id`` of the family
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipNotificationSession``
        :rtype: ``osid.relationship.RelationshipNotificationSession``
        :raise: ``NotFound`` -- no ``Family`` found by the given ``Id``
        :raise: ``NullArgument`` -- ``relationship_receiver, family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_family_session(self, proxy):
        """Gets the ``OsidSession`` to lookup relationship/family mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipFamilySession``
        :rtype: ``osid.relationship.RelationshipFamilySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_family()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_family_assignment_session(self, proxy):
        """Gets the ``OsidSession`` associated with assigning relationships to families.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipFamilyAssignmentSession``
        :rtype: ``osid.relationship.RelationshipFamilyAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_family_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_smart_family_session(self, family_id, proxy):
        """Gets the ``OsidSession`` to manage dynamic families of retlationships.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelationshipSmartFamilySession``
        :rtype: ``osid.relationship.RelationshipSmartFamilySession``
        :raise: ``NotFound`` -- no family found by the given ``Id``
        :raise: ``NullArgument`` -- ``family_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_smart_family()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyLookupSession``
        :rtype: ``osid.relationship.FamilyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyQuerySession``
        :rtype: ``osid.relationship.FamilyQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilySearchSession``
        :rtype: ``osid.relationship.FamilySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family administrative service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyAdminSession``
        :rtype: ``osid.relationship.FamilyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_notification_session(self, family_receiver, proxy):
        """Gets the ``OsidSession`` associated with the family notification service.

        :param family_receiver: the receiver
        :type family_receiver: ``osid.relationship.FamilyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyNotificationSession``
        :rtype: ``osid.relationship.FamilyNotificationSession``
        :raise: ``NullArgument`` -- ``family_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_hierarchy_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family hierarchy service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``FamilyHierarchySession`` for families
        :rtype: ``osid.relationship.FamilyHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_family_hierarchy_design_session(self, proxy):
        """Gets the ``OsidSession`` associated with the family hierarchy design service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``HierarchyDesignSession`` for families
        :rtype: ``osid.relationship.FamilyHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_family_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relationship_batch_proxy_manager(self):
        """Gets the relationship batch proxy manager.

        :return: a ``RelationshipBatchProxyManager``
        :rtype: ``osid.relationship.batch.RelationshipBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_batch_proxy_manager = property(fget=get_relationship_batch_proxy_manager)

    def get_relationship_rules_proxy_manager(self):
        """Gets the relationship rules proxy manager.

        :return: a ``RelationshipRulesProxyManager``
        :rtype: ``osid.relationship.rules.RelationshipRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relationship_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relationship_rules_proxy_manager = property(fget=get_relationship_rules_proxy_manager)



class Family(osid.OsidCatalog, osid.OsidSession):

    def get_family_record(self, family_record_type):
        """Gets the famly record corresponding to the given ``Family`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``family_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(family_record_type)``
        is ``true`` .

        :param family_record_type: the type of family record to retrieve
        :type family_record_type: ``osid.type.Type``
        :return: the family record
        :rtype: ``osid.relationship.records.FamilyRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.RelationshipLookupSession

    def get_family_id(self):
        """Gets the ``Family``  ``Id`` associated with this session.

        :return: the ``Family Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    family_id = property(fget=get_family_id)

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        :return: the family
        :rtype: ``osid.relationship.Family``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    family = property(fget=get_family)

    def can_lookup_relationships(self):
        """Tests if this user can perform ``Relationship`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_relationship_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_relationship_view(self):
        """A complete view of the ``Relationship`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_family_view(self):
        """Federates the view for methods in this session.
        A federated view will include relationships in families which
        are children of this family in the family hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_family_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts retrievals to this family only.



        """
        raise UNIMPLEMENTED()

    def use_effective_relationship_view(self):
        """Only relationships whose effective dates are current are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_effective_relationship_view(self):
        """All relationships of any effective dates are returned by all methods in this session."""
        raise UNIMPLEMENTED()

    def get_relationship(self, relationship_id):
        """Gets the ``Relationship`` specified by its ``Id``.

        :param relationship_id: the ``Id`` of the ``Relationship`` to retrieve
        :type relationship_id: ``osid.id.Id``
        :return: the returned ``Relationship``
        :rtype: ``osid.relationship.Relationship``
        :raise: ``NotFound`` -- no ``Relationship`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_ids(self, relationship_ids):
        """Gets a ``RelationshipList`` corresponding to the given ``IdList``.

        :param relationship_ids: the list of ``Ids`` to retrieve
        :type relationship_ids: ``osid.id.IdList``
        :return: the returned ``Relationship list``
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``relationship_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_genus_type(self, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding to the given relationship genus ``Type`` which does not include relationships of types derived from the specified ``Type``.

        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the returned ``Relationship list``
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_parent_genus_type(self, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding to the given relationship genus ``Type`` and include any additional relationships with genus types derived from the specified ``Type``.

        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the returned ``Relationship list``
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_record_type(self, relationship_record_type):
        """Gets a ``RelationshipList`` containing the given relationship record ``Type``.

        :param relationship_record_type: a relationship record type
        :type relationship_record_type: ``osid.type.Type``
        :return: the returned ``RelationshipList``
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_on_date(self, from_, to):
        """Gets a ``RelationshipList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``InvalidArgument`` -- ``from is greater than to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_for_source(self, source_id):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id``.

        :param source_id: a peer ``Id``
        :type source_id: ``osid.id.Id``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``source_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_for_source_on_date(self, source_id, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and effective during the entire given date range inclusive but not confined to the date range.

        :param source_id: a peer ``Id``
        :type source_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``InvalidArgument`` -- ``from is greater than to``
        :raise: ``NullArgument`` -- ``source_id, from`` ,or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_genus_type_for_source(self, source_id, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type.
        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer, including
        duplicates, or an error results if a relationship is
        inaccessible. Otherwise, inaccessible ``Relationships`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.
        
        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        :param source_id: a peer ``Id``
        :type source_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``source_id`` or ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_genus_type_for_source_on_date(self, source_id, relationship_genus_type, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type`` and effective during the entire given date range inclusive but not confined to the date range.

        :param source_id: a peer ``Id``
        :type source_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``InvalidArgument`` -- ``from is greater than to``
        :raise: ``NullArgument`` -- ``source_id, relationship_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_for_destination(self, destination_id):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id``.

        :param destination_id: a peer ``Id``
        :type destination_id: ``osid.id.Id``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``destination_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_for_destination_on_date(self, destination_id, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` with a starting effective date in the given range inclusive.

        :param destination_id: a peer ``Id``
        :type destination_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``InvalidArgument`` -- ``from is greater than to``
        :raise: ``NullArgument`` -- ``destination_id, from`` ,or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_genus_type_for_destination(self, destination_id, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type.
        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer, including
        duplicates, or an error results if a relationship is
        inaccessible. Otherwise, inaccessible ``Relationships`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.
        
        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        :param destination_id: a peer ``Id``
        :type destination_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``destination_id`` or ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_genus_type_for_destination_on_date(self, destination_id, relationship_genus_type, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus ``Type`` and effective during the entire given date range inclusive but not confined to the date range.

        :param destination_id: a peer ``Id``
        :type destination_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``InvalidArgument`` -- ``from is greater than to``
        :raise: ``NullArgument`` -- ``destination_id, relationship_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_for_peers(self, source_id, destination_id):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Ids``.

        :param source_id: a peer ``Id``
        :type source_id: ``osid.id.Id``
        :param destination_id: a related peer ``Id``
        :type destination_id: ``osid.id.Id``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``source_id`` or ``destination_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_for_peers_on_date(self, source_id, destination_id, from_, to):
        """Gets a ``RelationshipList`` corresponding to the given peer ``Ids`` and effective during the entire given date range inclusive but not confined to the date range.

        :param source_id: a peer ``Id``
        :type source_id: ``osid.id.Id``
        :param destination_id: a related peer ``Id``
        :type destination_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``source_id, destination_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_genus_type_for_peers(self, source_id, destination_id, relationship_genus_type):
        """Gets a ``RelationshipList`` corresponding between the given peer ``Ids`` and relationship genus ``Type.
        Relationships`` of any genus derived from the given genus are
        returned.

        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer or an error
        results if a relationship is inaccessible. Otherwise,
        inaccessible ``Relationships`` may be omitted from the list.
        
        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        :param source_id: a peer ``Id``
        :type source_id: ``osid.id.Id``
        :param destination_id: a related peer ``Id``
        :type destination_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``source_id, destination_id,`` or ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_genus_type_for_peers_on_date(self, source_id, destination_id, relationship_genus_type, from_, to):
        """Gets a ``RelationshipList`` effective during the entire given date range inclusive but not confined to the date range.

        :param source_id: a peer ``Id``
        :type source_id: ``osid.id.Id``
        :param destination_id: a related peer ``Id``
        :type destination_id: ``osid.id.Id``
        :param relationship_genus_type: a relationship genus type
        :type relationship_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``InvalidArgument`` -- ``from is greater than to``
        :raise: ``NullArgument`` -- ``source_id, destination_id, relationship_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships(self):
        """Gets all ``Relationships``.

        :return: a list of ``Relationships``
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    relationships = property(fget=get_relationships)


##
# The following methods are from osid.relationship.RelationshipQuerySession

    def can_search_relationships(self):
        """Tests if this user can perform ``Relationship`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_relationship_query(self):
        """Gets a relationship query.

        :return: the relationship query
        :rtype: ``osid.relationship.RelationshipQuery``

        """
        raise UNIMPLEMENTED()

    relationship_query = property(fget=get_relationship_query)

    def get_relationships_by_query(self, relationship_query):
        """Gets a list of ``Relationships`` matching the given relationship query.

        :param relationship_query: the relationship query
        :type relationship_query: ``osid.relationship.RelationshipQuery``
        :return: the returned ``RelationshipList``
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``relationship_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relationship_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.RelationshipSearchSession

    def get_relationship_search(self):
        """Gets a relationship search.

        :return: the relationship search
        :rtype: ``osid.relationship.RelationshipSearch``

        """
        raise UNIMPLEMENTED()

    relationship_search = property(fget=get_relationship_search)

    def get_relationship_search_order(self):
        """Gets a relationship search order.
        The ``RelationshipSearchOrder`` is supplied to a
        ``RelationshipSearch`` to specify the ordering of results.

        :return: the relationship search order
        :rtype: ``osid.relationship.RelationshipSearchOrder``

        """
        raise UNIMPLEMENTED()

    relationship_search_order = property(fget=get_relationship_search_order)

    def get_relationships_by_search(self, relationship_query, relationship_search):
        """Gets the search results matching the given search query using the given search.

        :param relationship_query: the relationship query
        :type relationship_query: ``osid.relationship.RelationshipQuery``
        :param relationship_search: the relationship search
        :type relationship_search: ``osid.relationship.RelationshipSearch``
        :return: the returned search results
        :rtype: ``osid.relationship.RelationshipSearchResults``
        :raise: ``NullArgument`` -- ``relationship_query`` or ``relationship_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relationship_query`` or ``relationship_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_relationship_query_from_inspector(self, relationship_query_inspector):
        """Gets a relationship query from an inspector.
        The inspector is available from a ``RelationshipSearchResults``.

        :param relationship_query_inspector: a relationship query inspector
        :type relationship_query_inspector: ``osid.relationship.RelationshipQueryInspector``
        :return: the relationship query
        :rtype: ``osid.relationship.RelationshipQuery``
        :raise: ``NullArgument`` -- ``relationship_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``relationship_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.RelationshipAdminSession

    def can_create_relationships(self):
        """Tests if this user can create ``Relationships`` A return of true does not guarantee successful authorization.
        A return of false indicates that it is known creating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Relationship`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_relationship_with_record_types(self, relationship_record_types):
        """Tests if this user can create a single ``Relationship`` using the desired record types.
        While ``RelationshipManager.getRelationshipRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Relationship``. Providing an empty array tests if a
        ``Relationship`` can be created with no records.

        :param relationship_record_types: array of relationship record types
        :type relationship_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Relationship`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relationship_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_relationship_form_for_create(self, source_id, destination_id, relationship_record_types):
        """Gets the relationship form for creating new relationships.
        A new form should be requested for each create transaction.

        :param source_id: ``Id`` of a peer
        :type source_id: ``osid.id.Id``
        :param destination_id: ``Id`` of the related peer
        :type destination_id: ``osid.id.Id``
        :param relationship_record_types: array of relationship record types
        :type relationship_record_types: ``osid.type.Type[]``
        :return: the relationship form
        :rtype: ``osid.relationship.RelationshipForm``
        :raise: ``NotFound`` -- ``source_id`` or ``destination_id`` is not found
        :raise: ``NullArgument`` -- ``source_id`` or ``destination_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested recod types

        """
        raise UNIMPLEMENTED()

    def create_relationship(self, relationship_form):
        """Creates a new ``Relationship``.

        :param relationship_form: the form for this ``Relationship``
        :type relationship_form: ``osid.relationship.RelationshipForm``
        :return: the new ``Relationship``
        :rtype: ``osid.relationship.Relationship``
        :raise: ``IllegalState`` -- ``relationship_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``relationship_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relationship_form`` did not originate from ``get_relationship_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_relationships(self):
        """Tests if this user can update ``Relationships``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Relationship`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_relationship_form_for_update(self, relationship_id):
        """Gets the relationship form for updating an existing relationship.
        A new relationship form should be requested for each update
        transaction.

        :param relationship_id: the ``Id`` of the ``Relationship``
        :type relationship_id: ``osid.id.Id``
        :return: the relationship form
        :rtype: ``osid.relationship.RelationshipForm``
        :raise: ``NotFound`` -- ``relationship_id`` is not found
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_relationship(self, relationship_id, relationship_form):
        """Updates an existing relationship.

        :param relationship_id: the ``Id`` of the ``Relationship``
        :type relationship_id: ``osid.id.Id``
        :param relationship_form: the form containing the elements to be updated
        :type relationship_form: ``osid.relationship.RelationshipForm``
        :raise: ``IllegalState`` -- ``relationship_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``relationship_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relationship_form`` did not originate from ``get_relationship_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_relationships(self):
        """Tests if this user can delete ``Relationships``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Relationship`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_relationship(self, relationship_id):
        """Deletes a ``Relationship``.

        :param relationship_id: the ``Id`` of the ``Relationship`` to remove
        :type relationship_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``relationship_id`` not found
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_relationship_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Relationships``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Relationship`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_relationship(self, relationship_id, alias_id):
        """Adds an ``Id`` to a ``Relationship`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Relationship`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another relationship, it is
        reassigned to the given relationship ``Id``.

        :param relationship_id: the ``Id`` of a ``Relationship``
        :type relationship_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``relationship`` not found
        :raise: ``NullArgument`` -- ``relationship_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.RelationshipNotificationSession

    def can_register_for_relationship_notifications(self):
        """Tests if this user can register for ``Relationship`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_relationships(self):
        """Register for notifications of new relationships.
        ``RelationshipReceiver.newRelationship()`` is invoked when a new
        ``Relationship`` appears in this family.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_relationships_for_peer(self, peer_id):
        """Register for notifications of new relationships.
        ``RelationshipReceiver.newRelationship()`` is invoked when a new
        ``Relationship`` appears for the given peer.

        :param peer_id: the ``Id`` of a peer to monitor
        :type peer_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``peer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_relationships_by_genus_type(self, relationship_genus_type):
        """Register for notifications of new relationships.
        ``RelationshipReceiver.newRelationship()`` is invoked when a new
        ``Relationship`` appears for the given peer.

        :param relationship_genus_type: the genus type of the ``Relationship`` to monitor
        :type relationship_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relationships(self):
        """Registers for notification of updated relationships.
        ``RelationshipReceiver.changedRelationship()`` is invoked when a
        relationship in this family is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relationships_for_peer(self, peer_id):
        """Register for notifications of updated relationships.
        ``RelationshipReceiver.changedRelationship()`` is invoked when a
        ``Relationship`` if changed for the given peer.

        :param peer_id: the ``Id`` of a peer to monitor
        :type peer_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``peer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relationships_by_genus_type(self, relationship_genus_type):
        """Register for notifications of updated relationships.
        ``RelationshipReceiver.changedRelationship()`` is invoked when a
        ``Relationship`` if changed for the given peer.

        :param relationship_genus_type: the genus type of the ``Relationship`` to monitor
        :type relationship_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relationship(self, relationship_id):
        """Registers for notification of an updated relationship.
        ``RelationshipReceiver.changedRelationship()`` is invoked when
        the specified relationship in this family is changed.

        :param relationship_id: the ``Id`` of the ``Relationship`` to monitor
        :type relationship_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relationships(self):
        """Registers for notification of deleted relationships.
        ``RelationshipReceiver.deletedRelationship()`` is invoked when a
        relationship is deleted or removed from this family.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relationships_for_peer(self, peer_id):
        """Register for notifications of deleted relationships.
        ``RelationshipReceiver.deletedRelationship()`` is invoked when a
        ``Relationship`` if removed for the given peer.

        :param peer_id: the ``Id`` of a peer to monitor
        :type peer_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``peer_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relationships_by_genus_type(self, relationship_genus_type):
        """Register for notifications of deleted relationships.
        ``RelationshipReceiver.deletedRelationship()`` is invoked when a
        ``Relationship`` if removed for the given peer.

        :param relationship_genus_type: the genus type of the ``Relationship`` to monitor
        :type relationship_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``relationship_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relationship(self, relationship_id):
        """Registers for notification of a deleted relationship.
        ``RelationshipReceiver.deletedRelationship()`` is invoked when
        the specified relationship is deleted or removed from this
        family.

        :param relationship_id: the ``Id`` of the ``Relationship`` to monitor
        :type relationship_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.RelationshipFamilySession

    def can_lookup_relationship_family_mappings(self):
        """Tests if this user can perform lookups of relationship/family mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_family_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_family_view(self):
        """A complete view of the ``Relationship`` and ``Family`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_relationship_ids_by_family(self, family_id):
        """Gets the list of ``Relationship Ids`` associated with a ``Family``.

        :param family_id: ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: list of related relationship ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_family(self, family_id):
        """Gets the list of ``Relationships`` associated with a ``Family``.

        :param family_id: ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: list of related relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NotFound`` -- ``family_id`` is not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationship_ids_by_families(self, family_ids):
        """Gets the list of ``Relationship Ids`` corresponding to a list of ``Family`` objects.

        :param family_ids: list of family ``Ids``
        :type family_ids: ``osid.id.IdList``
        :return: list of relationship ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``family_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relationships_by_families(self, family_ids):
        """Gets the list of ``Relationships`` corresponding to a list of ``Family`` objects.

        :param family_ids: list of family ``Ids``
        :type family_ids: ``osid.id.IdList``
        :return: list of relationships
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``NullArgument`` -- ``family_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_family_ids_by_relationship(self, relationship_id):
        """Gets the ``Family``  ``Ids`` mapped to a ``Relationship``.

        :param relationship_id: ``Id`` of a ``Relationship``
        :type relationship_id: ``osid.id.Id``
        :return: list of family ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``relationship_id`` is not found
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_families_by_relationship(self, relationship_id):
        """Gets the ``Family`` objects mapped to a ``Relationship``.

        :param relationship_id: ``Id`` of a ``Relationship``
        :type relationship_id: ``osid.id.Id``
        :return: list of family ``Ids``
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``NotFound`` -- ``relationship_id`` is not found
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.RelationshipFamilyAssignmentSession

    def can_assign_relationships(self):
        """Tests if this user can alter relationship/family mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_relationships_to_family(self, family_id):
        """Tests if this user can alter relationship/family mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_family_ids(self, family_id):
        """Gets a list of families including and under the given family node in which any relationship can be assigned.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :return: list of assignable family ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_family_ids_for_relationship(self, family_id, relationship_id):
        """Gets a list of families including and under the given family node in which a specific relationship can be assigned.

        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :param relationship_id: the ``Id`` of the ``Relationship``
        :type relationship_id: ``osid.id.Id``
        :return: list of assignable family ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``family_id`` or ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_relationship_to_family(self, relationship_id, family_id):
        """Adds an existing ``Relationship`` to a ``Family``.

        :param relationship_id: the ``Id`` of the ``Relationship``
        :type relationship_id: ``osid.id.Id``
        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``relationship_id`` is already assigned to ``family_id``
        :raise: ``NotFound`` -- ``relationship_id`` or ``family_id`` not found
        :raise: ``NullArgument`` -- ``relationship_id`` or ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_relationship_from_family(self, relationship_id, family_id):
        """Removes a ``Relationship`` from a ``Family``.

        :param relationship_id: the ``Id`` of the ``Relationship``
        :type relationship_id: ``osid.id.Id``
        :param family_id: the ``Id`` of the ``Family``
        :type family_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``relationship_id`` or ``family_id`` not found or ``relationship_id`` not assigned to ``family_id``
        :raise: ``NullArgument`` -- ``relationship_id`` or ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.relationship.RelationshipSmartFamilySession

    def can_manage_smart_families(self):
        """Tests if this user can manage smart families.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        :return: ``false`` if smart family methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_relationship_query(self, relationship_query):
        """Applies a relationship query to this family.

        :param relationship_query: the relationship query
        :type relationship_query: ``osid.relationship.RelationshipQuery``
        :raise: ``NullArgument`` -- ``relationship_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``relationship_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_relationship_query(self):
        """Gets a relationship query inspector for this family.

        :return: the relationship query inspector
        :rtype: ``osid.relationship.RelationshipQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_relationship_sequencing(self, relationship_search_order):
        """Applies a relationship search order to this family.

        :param relationship_search_order: the relationship search order
        :type relationship_search_order: ``osid.relationship.RelationshipSearchOrder``
        :raise: ``NullArgument`` -- ``relationship_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``relationship_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class FamilyList(osid.OsidList):

    def get_next_family(self):
        """Gets the next ``Family`` in this list.

        :return: the next ``Family`` in this list. The ``has_next()`` method should be used to test that a next ``Family`` is available before calling this method.
        :rtype: ``osid.relationship.Family``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_family = property(fget=get_next_family)

    def get_next_families(self, n):
        """Gets the next set of ``Family elements`` in this list.
        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Family`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Family`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.relationship.Family``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Families(RelationshipManager):
    pass


