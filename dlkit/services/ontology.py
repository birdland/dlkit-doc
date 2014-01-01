# -*- coding: utf-8 -*-
"""Ontology Open Service Interface Definitions
ontology version 3.0.0

The Ontology OSID is an auxiliary service used to define subject matter
that can be related to ``OsidObjects``. Ontologies are an alternative to
tagging where structure, restricted vocabulary, or localization of topic
names are desired.

Subjects

``Subjects`` are used to represent a topic and can be organized in a
hierarchy to form an ontology.

Relevancies

``Subjects`` are related to OSID ``Ids`` with a ``Relevancy``. A
``Relevancy`` is an ``OsidRelationship``.

Ontology Cataloging

``Subjects`` and ``Relevancies`` are organized into ``Ontology``
catalogs.

An external ``Id`` may be mapped to an ``Ontology``. This mapping allows
``OsidCatalogs`` to relate to a specific and sharable ``Ontology`` to
constrain a set of ``Subjects`` that may be relevant to a collection of
external ``OsidObjects``.

Sub Packages

The Ontology OSID includes a rules subpackage for managing rules to
enable subject relevancies and an Ontology Batch OSID for managing
``Subjects,``  ``Relevancies,`` and ``Ontologies`` in bulk.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class OntologyProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_lookup(self):
        """Tests if a subject lookup service is supported.
        a subject lookup service defines methods to access subjects.

        :return: true if subject lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_query(self):
        """Tests if a subject query service is supported.

        :return: ``true`` if subject query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_search(self):
        """Tests if a subject search service is supported.

        :return: ``true`` if subject search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_admin(self):
        """Tests if a subject administrative service is supported.

        :return: ``true`` if subject admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_notification(self):
        """Tests if subject notification is supported.
        Messages may be sent when subjects are created, modified, or
        deleted.

        :return: ``true`` if subject notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_hierarchy(self):
        """Tests if a subject hierarchy traversal is supported.

        :return: ``true`` if a subject hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_hierarchy_design(self):
        """Tests if subject hierarchy design is supported.

        :return: ``true`` if a subject hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_ontology(self):
        """Tests if a subject to ontology lookup session is available.

        :return: ``true`` if subject ontology lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_ontology_assignment(self):
        """Tests if a subject to ontology assignment session is available.

        :return: ``true`` if subject ontology assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_subject_smart_ontology(self):
        """Tests if a subject smart ontology session is available.

        :return: ``true`` if subject smart ontology session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relevancy_lookup(self):
        """Tests if a subject relevancy lookup service is supported.

        :return: ``true`` if relevancy lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relevancy_query(self):
        """Tests if a relevancy query service is supported.

        :return: ``true`` if relevancy query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relevancy_search(self):
        """Tests if a relevancy search service is supported.

        :return: ``true`` if relevancy search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relevancy_admin(self):
        """Tests if a relevancy administrative service is supported.

        :return: ``true`` if relevancy admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relevancy_notification(self):
        """Tests if relevancy notification is supported.
        Messages may be sent when subject relevancies are created,
        modified, or deleted.

        :return: ``true`` if relevancy notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_lookup(self):
        """Tests if an ontology lookup service is supported.

        :return: ``true`` if ontology lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relevancy_ontology(self):
        """Tests if a relevancy to ontology lookup session is available.

        :return: ``true`` if relevancy ontology lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relevancy_ontology_assignment(self):
        """Tests if a relevancy to ontology assignment session is available.

        :return: ``true`` if relevancy ontology assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_relevancy_smart_ontology(self):
        """Tests if a relevancy smart ontology session is available.

        :return: ``true`` if relevancy smart ontology session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_query(self):
        """Tests if an ontology query service is supported.

        :return: ``true`` if ontology query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_search(self):
        """Tests if an ontology search service is supported.

        :return: ``true`` if ontology search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_admin(self):
        """Tests if an ontology administrative service is supported.

        :return: ``true`` if ontology admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_notification(self):
        """Tests if ontology notification is supported.
        Messages may be sent when ontologies are created, modified, or
        deleted.

        :return: ``true`` if ontology notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_hierarchy(self):
        """Tests if an ontology hierarchy traversal is supported.

        :return: ``true`` if an ontology hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_hierarchy_design(self):
        """Tests if ontology hierarchy design is supported.

        :return: ``true`` if an ontology hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_assignment(self):
        """Tests if ``Ids`` can be asssigned to ontologies.

        :return: ``true`` if an ontology hassignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_batch(self):
        """Tests if an ontology batch service is supported.

        :return: ``true`` if ontology batch is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_ontology_rules(self):
        """Tests if an ontology rules service is supported.

        :return: ``true`` if ontology rules is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_subject_record_types(self):
        """Gets the supported ``Subject`` record types.

        :return: a list containing the supported ``Subject`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    subject_record_types = property(fget=get_subject_record_types)

    def supports_subject_record_type(self, subject_record_type):
        """Tests if the given ``Subject`` record type is supported.

        :param subject_record_type: a ``Type`` indicating a ``Subject`` record type
        :type subject_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``subject_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_subject_search_record_types(self):
        """Gets the supported ``Subject`` search record types.

        :return: a list containing the supported ``Subject`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    subject_search_record_types = property(fget=get_subject_search_record_types)

    def supports_subject_search_record_type(self, subject_search_record_type):
        """Tests if the given ``Subject`` search record type is supported.

        :param subject_search_record_type: a ``Type`` indicating a ``Subject`` search record type
        :type subject_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``subject_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_record_types(self):
        """Gets the supported ``Relevancy`` record types.

        :return: a list containing the supported ``Relevancy`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    relevancy_record_types = property(fget=get_relevancy_record_types)

    def supports_relevancy_record_type(self, relevancy_record_type):
        """Tests if the given ``Relevancy`` record type is supported.

        :param relevancy_record_type: a ``Type`` indicating a ``Relevnacy`` record type
        :type relevancy_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relevancy_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_search_record_types(self):
        """Gets the supported ``Relevancy`` search record types.

        :return: a list containing the supported ``Relevancy`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    relevancy_search_record_types = property(fget=get_relevancy_search_record_types)

    def supports_relevancy_search_record_type(self, relevancy_search_record_type):
        """Tests if the given ``Relevancy`` search record type is supported.

        :param relevancy_search_record_type: a ``Type`` indicating a ``Relevancy`` search record type
        :type relevancy_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relevancy_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_ontology_record_types(self):
        """Gets the supported ``Ontology`` record types.

        :return: a list containing the supported ``Ontology`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    ontology_record_types = property(fget=get_ontology_record_types)

    def supports_ontology_record_type(self, ontology_record_type):
        """Tests if the given ``Ontology`` record type is supported.

        :param ontology_record_type: a ``Type`` indicating an ``Ontology`` type
        :type ontology_record_type: ``osid.type.Type``
        :return: ``true`` if the given ontology record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_ontology_search_record_types(self):
        """Gets the supported ontology search record types.

        :return: a list containing the supported ``Ontology`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    ontology_search_record_types = property(fget=get_ontology_search_record_types)

    def supports_ontology_search_record_type(self, ontology_search_record_type):
        """Tests if the given ontology search record type is supported.

        :param ontology_search_record_type: a ``Type`` indicating an ``Ontology`` search record type
        :type ontology_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class OntologyManager(osid_managers.OsidManager, osid_sessions.OsidSession, OntologyProfile):

    def get_subject_lookup_session(self):
        """Gets the ``OsidSession`` associated with the subject lookup service.

        :return: a ``SubjectLookupSession``
        :rtype: ``osid.ontology.SubjectLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    subject_lookup_session = property(fget=get_subject_lookup_session)

    def get_subject_lookup_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the subject lookup service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a SubjectLookupSession``
        :rtype: ``osid.ontology.SubjectLookupSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_lookup_session_for_id(self, id_):
        """Gets the ``OsidSession`` associated with the subject lookup service for the given ``Id`` assigned using the ``OntologyAssignmentSession``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: ``a SubjectLookupSession``
        :rtype: ``osid.ontology.SubjectLookupSession``
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_query_session(self):
        """Gets the ``OsidSession`` associated with the subject query service.

        :return: a ``SubjectQuerySession``
        :rtype: ``osid.ontology.SubjectQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    subject_query_session = property(fget=get_subject_query_session)

    def get_subject_query_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the subject query service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: a ``SubjectQuerySession``
        :rtype: ``osid.ontology.SubjectQuerySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_search_session(self):
        """Gets the ``OsidSession`` associated with the subject search service.

        :return: a ``SubjectSearchSession``
        :rtype: ``osid.ontology.SubjectSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    subject_search_session = property(fget=get_subject_search_session)

    def get_subject_search_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the subject search service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a SubjectSearchSession``
        :rtype: ``osid.ontology.SubjectSearchSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_admin_session(self):
        """Gets the ``OsidSession`` associated with the subject administration service.

        :return: a ``SubjectAdminSession``
        :rtype: ``osid.ontology.SubjectAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    subject_admin_session = property(fget=get_subject_admin_session)

    def get_subject_admin_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the subject admin service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a SubjectAdminSession``
        :rtype: ``osid.ontology.SubjectAdminSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_notification_session(self, subject_receiver):
        """Gets the notification session for notifications pertaining to subject changes.

        :param subject_receiver: the subject receiver
        :type subject_receiver: ``osid.ontology.SubjectReceiver``
        :return: a ``SubjectNotificationSession``
        :rtype: ``osid.ontology.SubjectNotificationSession``
        :raise: ``NullArgument`` -- ``subject_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_notification_session_for_ontology(self, subject_receiver, ontology_id):
        """Gets the ``OsidSession`` associated with the subject notification service for the given ontology.

        :param subject_receiver: the subject receiver
        :type subject_receiver: ``osid.ontology.SubjectReceiver``
        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a SubjectNotificationSession``
        :rtype: ``osid.ontology.SubjectNotificationSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``subject_receiver`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_hierarchy_session(self):
        """Gets the session traversing subject hierarchies.

        :return: a ``SubjectHierarchySession``
        :rtype: ``osid.ontology.SubjectHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    subject_hierarchy_session = property(fget=get_subject_hierarchy_session)

    def get_subject_hierarchy_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the subject heirarchy traversal service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: a ``SubjectHierarchySession``
        :rtype: ``osid.ontology.SubjectHierarchySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_hierarchy_session_for_id(self, id_):
        """Gets the hierarchy session for the given ``Id`` assigned using the ``OntologyAssignmentSession``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: a ``SubjectHierarchySession``
        :rtype: ``osid.ontology.SubjectHierarchySession``
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_hierarchy_design_session(self):
        """Gets the session designing subject hierarchies.

        :return: a ``SubjectHierarchyDesignSession``
        :rtype: ``osid.ontology.SubjectHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    subject_hierarchy_design_session = property(fget=get_subject_hierarchy_design_session)

    def get_subject_hierarchy_design_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the subject heirarchy design service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: a ``SubjectHierarchyDesignSession``
        :rtype: ``osid.ontology.SubjectHierarchyDesignSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_ontology_session(self):
        """Gets the session retrieving subject ontology mappings.

        :return: a ``SubjectOntologySession``
        :rtype: ``osid.ontology.SubjectOntologySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_ontology() is false``

        """
        raise UNIMPLEMENTED()

    subject_ontology_session = property(fget=get_subject_ontology_session)

    def get_subject_ontology_assignment_session(self):
        """Gets the session managing subject ontology mappings.

        :return: a ``SubjectOntologyAssignmentSession``
        :rtype: ``osid.ontology.SubjectOntologyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_ontology_assignment() is false``

        """
        raise UNIMPLEMENTED()

    subject_ontology_assignment_session = property(fget=get_subject_ontology_assignment_session)

    def get_subject_smart_ontology_session(self, ontology_id):
        """Gets the session managing subject smart ontologies.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: a ``SubjectSmartOntologySession``
        :rtype: ``osid.ontology.SubjectSmartOntologySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_smart_ontology() is false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_lookup_session(self):
        """Gets the ``OsidSession`` associated with the relevancy lookup service.

        :return: a ``RelevancyLookupSession``
        :rtype: ``osid.ontology.RelevancyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relevancy_lookup_session = property(fget=get_relevancy_lookup_session)

    def get_relevancy_lookup_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the relevancy lookup service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a RelevancyLookupSession``
        :rtype: ``osid.ontology.RelevancyLookupSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_query_session(self):
        """Gets the ``OsidSession`` associated with the relevancy query service.

        :return: a ``RelevancyQuerySession``
        :rtype: ``osid.ontology.RelevancyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relevancy_query_session = property(fget=get_relevancy_query_session)

    def get_relevancy_query_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the relevancy query service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a RelevancyQuerySession``
        :rtype: ``osid.ontology.RelevancyQuerySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_search_session(self):
        """Gets the ``OsidSession`` associated with the relevancy search service.

        :return: a ``RelevancySearchSession``
        :rtype: ``osid.ontology.RelevancySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relevancy_search_session = property(fget=get_relevancy_search_session)

    def get_relevancy_search_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the relevancy search service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a RelevancySearchSession``
        :rtype: ``osid.ontology.RelevancySearchSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_admin_session(self):
        """Gets the ``OsidSession`` associated with the relevancy administration service.

        :return: a ``RelvancyAdminSession``
        :rtype: ``osid.ontology.RelevancyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    relevancy_admin_session = property(fget=get_relevancy_admin_session)

    def get_relevancy_admin_session_for_ontology(self, ontology_id):
        """Gets the ``OsidSession`` associated with the relevancy admin service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a RelevancyAdminSession``
        :rtype: ``osid.ontology.RelevancyAdminSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_notification_session(self, relevancy_receiver):
        """Gets the notification session for notifications pertaining to relevancy changes.

        :param relevancy_receiver: the relevancy receiver
        :type relevancy_receiver: ``osid.ontology.RelevancyReceiver``
        :return: ``a _relevancy_notification_session``
        :rtype: ``osid.ontology.RelevancyNotificationSession``
        :raise: ``NullArgument`` -- ``relevancy_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_notification_session_for_ontology(self, relevancy_receiver, ontology_id):
        """Gets the ``OsidSession`` associated with the relevancy notification service for the given ontology.

        :param relevancy_receiver: the subject receiver
        :type relevancy_receiver: ``osid.ontology.RelevancyReceiver``
        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``a _relevancy_notification_session``
        :rtype: ``osid.ontology.RelevancyNotificationSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``relevancy_receiver`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_ontology_session(self):
        """Gets the session retrieving relevancy ontology mappings.

        :return: a ``RelevancyOntologySession``
        :rtype: ``osid.ontology.RelevancyOntologySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_ontology() is false``

        """
        raise UNIMPLEMENTED()

    relevancy_ontology_session = property(fget=get_relevancy_ontology_session)

    def get_relevancy_ontology_assignment_session(self):
        """Gets the session managing relevancy ontology mappings.

        :return: a ``RelevancyOntologyAssignmentSession``
        :rtype: ``osid.ontology.RelevancyOntologyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_ontology_assignment() is false``

        """
        raise UNIMPLEMENTED()

    relevancy_ontology_assignment_session = property(fget=get_relevancy_ontology_assignment_session)

    def get_relevancy_smart_ontology_session(self, ontology_id):
        """Gets the session managing relevancy smart ontologies.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :return: a ``RelevancySmartOntologySession``
        :rtype: ``osid.ontology.RelevancySmartOntologySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_smart_ontology() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_lookup_session(self):
        """Gets the OsidSession associated with the ontology lookup service.

        :return: an ``OntologyLookupSession``
        :rtype: ``osid.ontology.OntologyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_lookup() is false``

        """
        raise UNIMPLEMENTED()

    ontology_lookup_session = property(fget=get_ontology_lookup_session)

    def get_ontology_query_session(self):
        """Gets the OsidSession associated with the ontology query service.

        :return: an ``OntologyQuerySession``
        :rtype: ``osid.ontology.OntologyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_query() is false``

        """
        raise UNIMPLEMENTED()

    ontology_query_session = property(fget=get_ontology_query_session)

    def get_ontology_search_session(self):
        """Gets the OsidSession associated with the ontology search service.

        :return: an ``OntologySearchSession``
        :rtype: ``osid.ontology.OntologySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_search() is false``

        """
        raise UNIMPLEMENTED()

    ontology_search_session = property(fget=get_ontology_search_session)

    def get_ontology_admin_session(self):
        """Gets the OsidSession associated with the ontology administration service.

        :return: an ``OntologyAdminSession``
        :rtype: ``osid.ontology.OntologyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_admin() is false``

        """
        raise UNIMPLEMENTED()

    ontology_admin_session = property(fget=get_ontology_admin_session)

    def get_ontology_notification_session(self, ontology_receiver):
        """Gets the notification session for notifications pertaining to ontology service changes.

        :param ontology_receiver: the ontology receiver
        :type ontology_receiver: ``osid.ontology.OntologyReceiver``
        :return: an ``OntologyNotificationSession``
        :rtype: ``osid.ontology.OntologyNotificationSession``
        :raise: ``NullArgument`` -- ``ontology_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_hierarchy_session(self):
        """Gets the session traversing ontology hierarchies.

        :return: an ``OntologyHierarchySession``
        :rtype: ``osid.ontology.OntologyHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    ontology_hierarchy_session = property(fget=get_ontology_hierarchy_session)

    def get_ontology_hierarchy_design_session(self):
        """Gets the session designing ontology hierarchies.

        :return: an ``OntologyHierarchyDesignSession``
        :rtype: ``osid.ontology.OntologyHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    ontology_hierarchy_design_session = property(fget=get_ontology_hierarchy_design_session)

    def get_ontology_assignment_session(self):
        """Gets the session to assign ``Ids`` to ontologies.

        :return: an ``OntologyAssignmentSession``
        :rtype: ``osid.ontology.OntologyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_assignment() is false``

        """
        raise UNIMPLEMENTED()

    ontology_assignment_session = property(fget=get_ontology_assignment_session)

    def get_ontology_batch_manager(self):
        """Gets the ontology batch service.

        :return: an ``OntologyBatchManager``
        :rtype: ``osid.ontology.batch.OntologyBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_batch() is false``

        """
        raise UNIMPLEMENTED()

    ontology_batch_manager = property(fget=get_ontology_batch_manager)

    def get_ontology_rules_manager(self):
        """Gets the ontology rules service.

        :return: an ``OntologyRulesManager``
        :rtype: ``osid.ontology.rules.OntologyRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_rules() is false``

        """
        raise UNIMPLEMENTED()

    ontology_rules_manager = property(fget=get_ontology_rules_manager)


##
# The following methods are from osid.ontology.OntologyLookupSession

    def can_lookup_ontologies(self):
        """Tests if this user can perform ``Ontology`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_ontology_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_ontology_view(self):
        """A complete view of the ``Ontology`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_ontology(self, ontology_id):
        """Gets the ``Ontology`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Ontology`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to an ``Ontology`` and retained
        for compatility.

        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: the ontology
        :rtype: ``osid.ontology.Ontology``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontologies_by_ids(self, ontology_ids):
        """Gets an ``OntologyList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        ontologies specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Ontology`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :param ontology_ids: the list of ``Ids`` to retrieve
        :type ontology_ids: ``osid.id.IdList``
        :return: the returned ``Ontology`` list
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``ontology_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontologies_by_genus_type(self, ontology_genus_type):
        """Gets an ``OntologyList`` corresponding to the given ontology genus ``Type`` which does not include ontologies of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known ontologies
        or an error results. Otherwise, the returned list may contain
        only those ontologies that are accessible through this session.

        :param ontology_genus_type: an ontology genus type
        :type ontology_genus_type: ``osid.type.Type``
        :return: the returned ``Ontology`` list
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NullArgument`` -- ``ontology_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontologies_by_parent_genus_type(self, ontology_genus_type):
        """Gets an ``OntologyList`` corresponding to the given ontology genus ``Type`` and include any additional ontologies with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known ontologies
        or an error results. Otherwise, the returned list may contain
        only those ontologies that are accessible through this session.

        :param ontology_genus_type: an ontology genus type
        :type ontology_genus_type: ``osid.type.Type``
        :return: the returned ``Ontology`` list
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NullArgument`` -- ``ontology_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontologies_by_record_type(self, ontology_record_type):
        """Gets an ``OntologyList`` containing the given ontology record ``Type``.
        In plenary mode, the returned list contains all known ontologies
        or an error results. Otherwise, the returned list may contain
        only those ontologies that are accessible through this session.

        :param ontology_record_type: an ontology record type
        :type ontology_record_type: ``osid.type.Type``
        :return: the returned ``Ontology`` list
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontologies_by_provider(self, resource_id):
        """Gets an ``OntologyList`` for the given provider.
        In plenary mode, the returned list contains all known ontologies
        or an error results. Otherwise, the returned list may contain
        only those ontologies that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Ontology`` list
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontologies(self):
        """Gets all ``Ontologies``.
        In plenary mode, the returned list contains all known ontologies
        or an error results. Otherwise, the returned list may contain
        only those ontologies that are accessible through this session.

        :return: an ``OntologyList``
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    ontologies = property(fget=get_ontologies)


##
# The following methods are from osid.ontology.OntologyQuerySession

    def can_search_ontologies(self):
        """Tests if this user can perform ``Ontology`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_ontology_query(self):
        """Gets an ontology query.

        :return: an ontology query
        :rtype: ``osid.ontology.OntologyQuery``

        """
        raise UNIMPLEMENTED()

    ontology_query = property(fget=get_ontology_query)

    def get_ontologies_by_query(self, ontology_query):
        """Gets a list of ``Ontology`` objects matching the given ontology query.

        :param ontology_query: the ontology query
        :type ontology_query: ``osid.ontology.OntologyQuery``
        :return: the returned ``OntologyList``
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NullArgument`` -- ``ontology_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``ontology_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.OntologySearchSession

    def get_ontology_search(self):
        """Gets an ontology search.

        :return: an ontology search
        :rtype: ``osid.ontology.OntologySearch``

        """
        raise UNIMPLEMENTED()

    ontology_search = property(fget=get_ontology_search)

    def get_ontology_search_order(self):
        """Gets an ontology search order.
        The ``OntologySearchOrder`` is supplied to an ``OntologySearch``
        to specify the ordering of results.

        :return: the ontology search order
        :rtype: ``osid.ontology.OntologySearchOrder``

        """
        raise UNIMPLEMENTED()

    ontology_search_order = property(fget=get_ontology_search_order)

    def get_ontologies_by_search(self, ontology_query, ontology_search):
        """Gets the search results matching the given search query using the given search.

        :param ontology_query: the ontology query
        :type ontology_query: ``osid.ontology.OntologyQuery``
        :param ontology_search: the ontology search
        :type ontology_search: ``osid.ontology.OntologySearch``
        :return: the ontology search results
        :rtype: ``osid.ontology.OntologySearchResults``
        :raise: ``NullArgument`` -- ``ontology_query`` or ``ontology_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``ontology_query`` or ``ontology_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_ontology_query_from_inspector(self, ontology_query_inspector):
        """Gets an ontology query from an inspector.
        The inspector is available from an ``OntologySearchResults``.

        :param ontology_query_inspector: an ontology query inspector
        :type ontology_query_inspector: ``osid.ontology.OntologyQueryInspector``
        :return: the ontology query
        :rtype: ``osid.ontology.OntologyQuery``
        :raise: ``NullArgument`` -- ``ontology_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``ontology_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.OntologyAdminSession

    def can_create_ontologies(self):
        """Tests if this user can create ``Ontologies``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Ontology`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Ontology`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_ontology_with_record_types(self, ontology_record_types):
        """Tests if this user can create a single ``Ontology`` using the desired record types.
        While ``OntologyManager.getOntologyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Ontology``.
        Providing an empty array tests if an ``Ontology`` can be created
        with no records.

        :param ontology_record_types: array of ontology record types
        :type ontology_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Ontology`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_ontology_form_for_create(self, ontology_record_types):
        """Gets the ontology form for creating new ontologies.
        A new form should be requested for each create transaction.

        :param ontology_record_types: array of ontology record types
        :type ontology_record_types: ``osid.type.Type[]``
        :return: the ontology form
        :rtype: ``osid.ontology.OntologyForm``
        :raise: ``NullArgument`` -- ``ontology_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_ontology(self, ontology_form):
        """Creates a new ``Ontology``.

        :param ontology_form: the form for this ``Ontology``
        :type ontology_form: ``osid.ontology.OntologyForm``
        :return: the new ``Ontology``
        :rtype: ``osid.ontology.OntologyForm``
        :raise: ``IllegalState`` -- ``ontology_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``ontology_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``ontology_form`` did not originate from ``get_ontology_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_ontologies(self):
        """Tests if this user can update ``Ontologies``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Ontology`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Ontology`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_ontology_form_for_update(self, ontology_id):
        """Gets the ontology form for updating an existing ontology.
        A new ontology form should be requested for each update
        transaction.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: the ontology form
        :rtype: ``osid.ontology.OntologyForm``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_ontology(self, ontology_form):
        """Updates an existing ontology.

        :param ontology_form: the form containing the elements to be updated
        :type ontology_form: ``osid.ontology.OntologyForm``
        :raise: ``IllegalState`` -- ``ontology_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``ontology_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``ontology_form`` did not originate from ``get_ontology_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_ontologies(self):
        """Tests if this user can delete ontologies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Ontology`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Ontology`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_ontology(self, ontology_id):
        """Deletes an ``Ontology``.

        :param ontology_id: the ``Id`` of the ``Ontology`` to remove
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_ontology_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ontologies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Ontology`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_ontology(self, ontology_id, alias_id):
        """Adds an ``Id`` to an ``Ontology`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Ontology`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another ontology, it is
        reassigned to the given ontology ``Id``.

        :param ontology_id: the ``Id`` of an ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.OntologyNotificationSession

    def can_register_for_ontology_notifications(self):
        """Tests if this user can register for ``Ontology`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_ontologies(self):
        """Register for notifications of new ontologies.
        ``OntologyReceiver.newOntology()`` is invoked when a new
        ``Ontology`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_ontology_ancestors(self, ontology_id):
        """Registers for notification if an ancestor is added to the specified ontology in the ontology hierarchy.
        ``OntologyReceiver.newOntologyAncestor()`` is invoked when the
        specified ontology experiences an addition in ancestry.

        :param ontology_id: the ``Id`` of the ontology to monitor
        :type ontology_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``ontology_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_ontology_descendants(self, ontology_id):
        """Registers for notification if a descendant is added to the specified ontology in the ontology hierarchy.
        ``OntologyReceiver.newOntologyDescendant()`` is invoked when the
        specified ontology experiences an addition in descendants.

        :param ontology_id: the ``Id`` of the ontology to monitor
        :type ontology_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``ontology_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_ontologies(self):
        """Registers for notification of updated ontologies.
        ``OntologyReceiver.changedOntology()`` is invoked when an
        ontology is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_ontology(self, ontology_id):
        """Registers for notification of an updated ontology.
        ``OntologyReceiver.changedOntology()`` is invoked when the
        specified ontology is changed.

        :param ontology_id: the ``Id`` of the ontology to monitor
        :type ontology_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``ontology_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_ontologies(self):
        """Registers for notification of deleted ontologies.
        ``OntologyReceiver.deletedOntology()`` is invoked when a
        calenedar is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_ontology(self, ontology_id):
        """Registers for notification of a deleted ontology.
        ``OntologyReceiver.deletedOntology()`` is invoked when the
        specified ontology is deleted.

        :param ontology_id: the ``Id`` of the ontology to monitor
        :type ontology_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``ontology_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_ontology_ancestors(self, ontology_id):
        """Registers for notification if an ancestor is removed from the specified ontology in the ontology hierarchy.
        ``OntologyReceiver.deletedOntologyAncestor()`` is invoked when
        the specified ontology experiences a removal of an ancestor.

        :param ontology_id: the ``Id`` of the ontology to monitor
        :type ontology_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``ontology_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_ontology_descendants(self, ontology_id):
        """Registers for notification if a descendant is removed from fthe specified ontology in the calndar hierarchy.
        ``OntologyReceiver.deletedOntologyDescednant()`` is invoked when
        the specified ontology experiences a removal of one of its
        descendants.

        :param ontology_id: the ``Id`` of the ontology to monitor
        :type ontology_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``ontology_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.OntologyHierarchySession

    def get_ontology_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    ontology_hierarchy_id = property(fget=get_ontology_hierarchy_id)

    def get_ontology_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    ontology_hierarchy = property(fget=get_ontology_hierarchy)

    def can_access_ontology_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may wish not to offer
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_ontology_ids(self):
        """Gets the root ontology ``Ids`` in this hierarchy.

        :return: the root ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_ontology_ids = property(fget=get_root_ontology_ids)

    def get_root_ontologies(self):
        """Gets the root ontologies in this ontology hierarchy.

        :return: the root ontologies
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_ontologies = property(fget=get_root_ontologies)

    def has_parent_ontologies(self, ontology_id):
        """Tests if the ``Ontology`` has any parents.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``true`` if the ontology has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_ontology(self, id_, ontology_id):
        """Tests if an ``Id`` is a direct parent of an ontology.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``ontology_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_ontology_ids(self, ontology_id):
        """Gets the parent ``Ids`` of the given ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the ontology
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_ontologies(self, ontology_id):
        """Gets the parents of the given ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :return: the parents of the ontology
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_ontology(self, id_, ontology_id):
        """Tests if an ``Id`` is an ancestor of an ontology.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``ontology_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_ontologies(self, ontology_id):
        """Tests if an ontology has any children.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``true`` if the ``ontology_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_ontology(self, id_, ontology_id):
        """Tests if an ontology is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``ontology_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_ontology_ids(self, ontology_id):
        """Gets the child ``Ids`` of the given ontology.

        :param ontology_id: the ``Id`` to query
        :type ontology_id: ``osid.id.Id``
        :return: the children of the ontology
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_ontologies(self, ontology_id):
        """Gets the children of the given ontology.

        :param ontology_id: the ``Id`` to query
        :type ontology_id: ``osid.id.Id``
        :return: the children of the ontology
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_ontology(self, id_, ontology_id):
        """Tests if an ``Id`` is a descendant of an ontology.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``ontology_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontology_node_ids(self, ontology_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given ontology.

        :param ontology_id: the ``Id`` to query
        :type ontology_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an ontology node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontology_nodes(self, ontology_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given ontology.

        :param ontology_id: the ``Id`` to query
        :type ontology_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an ontology node
        :rtype: ``osid.ontology.OntologyNode``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.OntologyHierarchyDesignSession

    def can_modify_ontology_hierarchy(self):
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

    def add_root_ontology(self, ontology_id):
        """Adds a root ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``ontology_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_ontology(self, ontology_id):
        """Removes a root ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` is not a root
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_ontology(self, ontology_id, child_id):
        """Adds a child to an ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``ontology_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``ontology_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_ontology(self, ontology_id, child_id):
        """Removes a child from an ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``ontology_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_ontologies(self, ontology_id):
        """Removes all children from an ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.OntologyAssignmentSession

    def can_assign_ontologies(self):
        """Tests if this user can manage of id/ontology mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known assignment methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may wish not to offer
        mapping functions to unauthorized users.

        :return: ``false`` if managing mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def assign_ontology(self, id_, ontology_id):
        """Assigns an ``Id`` to an ontology.

        :param id: ``an _id``
        :type id: ``osid.id.Id``
        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_ontology(self, id_, ontology_id):
        """Unassigns an ``Id`` from an ontology.

        :param id: ``an _id``
        :type id: ``osid.id.Id``
        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` not assigned to ``ontology_id``
        :raise: ``NullArgument`` -- ``id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ids(self, ontology_id):
        """Gets a list of the ``Ids`` assigned to an ontology.

        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class OntologyProxyManager(osid_managers.OsidProxyManager, OntologyProfile):

    def get_subject_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the subject lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectLookupSession``
        :rtype: ``osid.ontology.SubjectLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_lookup_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the subject lookup service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a SubjectLookupSession``
        :rtype: ``osid.ontology.SubjectLookupSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_lookup_session_for_id(self, id_, proxy):
        """Gets the ``OsidSession`` associated with the subject lookup service for the given ``Id`` assigned using the ``OntologyAssignmentSession``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a SubjectLookupSession``
        :rtype: ``osid.ontology.SubjectLookupSession``
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the subject query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectQuerySession``
        :rtype: ``osid.ontology.SubjectQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subjec_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_query_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the subject query service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectQuerySession``
        :rtype: ``osid.ontology.SubjectQuerySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the subject search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectSearchSession``
        :rtype: ``osid.ontology.SubjectSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_search_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the subject search service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a SubjectSearchSession``
        :rtype: ``osid.ontology.SubjectSearchSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the subject administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectAdminSession``
        :rtype: ``osid.ontology.SubjectAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_admin_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the subject admin service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a SubjectAdminSession``
        :rtype: ``osid.ontology.SubjectAdminSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_notification_session(self, subject_receiver, proxy):
        """Gets the notification session for notifications pertaining to subject changes.

        :param subject_receiver: the subject receiver
        :type subject_receiver: ``osid.ontology.SubjectReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectNotificationSession``
        :rtype: ``osid.ontology.SubjectNotificationSession``
        :raise: ``NullArgument`` -- ``subject_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_notification_session_for_ontology(self, subject_receiver, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the subject notification service for the given ontology.

        :param subject_receiver: the subject receiver
        :type subject_receiver: ``osid.ontology.SubjectReceiver``
        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a SubjectNotificationSession``
        :rtype: ``osid.ontology.SubjectNotificationSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``subject_receiver, ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_hierarchy_session(self, proxy):
        """Gets the session traversing subject hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectHierarchySession``
        :rtype: ``osid.ontology.SubjectHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    def get_subject_hierarchy_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the subject heirarchy traversal service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectHierarchySession``
        :rtype: ``osid.ontology.SubjectHierarchySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_hierarchy_session_for_id(self, id_, proxy):
        """Gets the hierarchy session for the given ``Id`` assigned using the ``OntologyAssignmentSession``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectHierarchySession``
        :rtype: ``osid.ontology.SubjectHierarchySession``
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_hierarchy_design_session(self, proxy):
        """Gets the session designing subject hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectHierarchyDesignSession``
        :rtype: ``osid.ontology.SubjectHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    def get_subject_hierarchy_design_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the subject heirarchy design service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectHierarchyDesignSession``
        :rtype: ``osid.ontology.SubjectHierarchyDesignSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy_design()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_subject_ontology_session(self, proxy):
        """Gets the session retrieving subject ontology mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectOntologySession``
        :rtype: ``osid.ontology.SubjectOntologySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_ontology() is false``

        """
        raise UNIMPLEMENTED()

    def get_subject_ontology_assignment_session(self, proxy):
        """Gets the session managing subject ontology mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectOntologyAssignmentSession``
        :rtype: ``osid.ontology.SubjectOntologyAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_ontology_assignment() is false``

        """
        raise UNIMPLEMENTED()

    def get_subject_smart_ontology_session(self, ontology_id, proxy):
        """Gets the session managing subject smart ontologies.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SubjectSmartOntologySession``
        :rtype: ``osid.ontology.SubjectOntologySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_smart_ontology() is false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relevancy lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelevancyLookupSession``
        :rtype: ``osid.ontology.RelevancyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_lookup_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the relevancy lookup service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a RelevancyLookupSession``
        :rtype: ``osid.ontology.RelevancyLookupSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relevancy query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelevancyQuerySession``
        :rtype: ``osid.ontology.RelevancyQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_query_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the relevancy query service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a RelevancyQuerySession``
        :rtype: ``osid.ontology.RelevancyQuerySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relevancy search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelevanctSearchSession``
        :rtype: ``osid.ontology.RelevancySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_search_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the relevancy search service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a RelevancySearchSession``
        :rtype: ``osid.ontology.RelevancySearchSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the relevancy administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelvancyAdminSession``
        :rtype: ``osid.ontology.RelevancyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_admin_session_for_ontology(self, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the relevancy admin service for the given ontology.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a RelevancyAdminSession``
        :rtype: ``osid.ontology.RelevancyAdminSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_notification_session(self, relevancy_receiver, proxy):
        """Gets the notification session for notifications pertaining to relevancy changes.

        :param relevancy_receiver: the relevancy receiver
        :type relevancy_receiver: ``osid.ontology.RelevancyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _relevancy_notification_session``
        :rtype: ``osid.ontology.RelevancyNotificationSession``
        :raise: ``NullArgument`` -- ``relevancy_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_notification_session_for_ontology(self, relevancy_receiver, ontology_id, proxy):
        """Gets the ``OsidSession`` associated with the relevancy notification service for the given ontology.

        :param relevancy_receiver: the subject receiver
        :type relevancy_receiver: ``osid.ontology.RelevancyReceiver``
        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _relevancy_notification_session``
        :rtype: ``osid.ontology.RelevancyNotificationSession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``relevancy_receiver, ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_relevancy_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_ontology_session(self, proxy):
        """Gets the session retrieving relevancy ontology mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelevancyOntologySession``
        :rtype: ``osid.ontology.RelevancyOntologySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_ontology() is false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_ontology_assignment_session(self, proxy):
        """Gets the session managing relevancy ontology mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelevancyOntologyAssignmentSession``
        :rtype: ``osid.ontology.RelevancyOntologyAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_ontology_assignment() is false``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_smart_ontology_session(self, ontology_id, proxy):
        """Gets the session managing relevancy smart ontologies.

        :param ontology_id: the ``Id`` of the ontology
        :type ontology_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RelevancySmartOntologySession``
        :rtype: ``osid.ontology.RelevancySmartOntologySession``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_smart_ontology() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_lookup_session(self, proxy):
        """Gets the OsidSession associated with the ontology lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OntologyLookupSession``
        :rtype: ``osid.ontology.OntologyLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_lookup() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_query_session(self, proxy):
        """Gets the OsidSession associated with the ontology query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OntologyQuerySession``
        :rtype: ``osid.ontology.OntologyQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_query() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_search_session(self, proxy):
        """Gets the OsidSession associated with the ontology search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OntologySearchSession``
        :rtype: ``osid.ontology.OntologySearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_search() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_admin_session(self, proxy):
        """Gets the OsidSession associated with the ontology administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OntologyAdminSession``
        :rtype: ``osid.ontology.OntologyAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_admin() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_notification_session(self, ontology_receiver, proxy):
        """Gets the notification session for notifications pertaining to ontology service changes.

        :param ontology_receiver: the ontology receiver
        :type ontology_receiver: ``osid.ontology.OntologyReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OntologyNotificationSession``
        :rtype: ``osid.ontology.OntologyNotificationSession``
        :raise: ``NullArgument`` -- ``ontology_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_hierarchy_session(self, proxy):
        """Gets the session traversing ontology hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OntologyHierarchySession``
        :rtype: ``osid.ontology.OntologyHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_hierarchy_design_session(self, proxy):
        """Gets the session designing ontology hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OntologyHierarchyDesignSession``
        :rtype: ``osid.ontology.OntologyHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_assignment_session(self, proxy):
        """Gets the session to assign ``Ids`` to ontologies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OntologyAssignmentSession``
        :rtype: ``osid.ontology.OntologyAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_assignment() is false``

        """
        raise UNIMPLEMENTED()

    def get_ontology_batch_proxy_manager(self):
        """Gets the ontology batch service.

        :return: an ``OntologyBatchProxyManager``
        :rtype: ``osid.ontology.batch.OntologyBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_batch() is false``

        """
        raise UNIMPLEMENTED()

    ontology_batch_proxy_manager = property(fget=get_ontology_batch_proxy_manager)

    def get_ontology_rules_proxy_manager(self):
        """Gets the ontology rules service.

        :return: an ``OntologyRulesProxyManager``
        :rtype: ``osid.ontology.rules.OntologyRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_rules() is false``

        """
        raise UNIMPLEMENTED()

    ontology_rules_proxy_manager = property(fget=get_ontology_rules_proxy_manager)



class Ontology(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_ontology_record(self, ontology_record_type):
        """Gets the ontology record corresponding to the given ``Ontology`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``ontology_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(ontology_record_type)`` is ``true`` .

        :param ontology_record_type: an ontology record type
        :type ontology_record_type: ``osid.type.Type``
        :return: the ontology record
        :rtype: ``osid.ontology.records.OntologyRecord``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(ontology_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectLookupSession

    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    ontology = property(fget=get_ontology)

    def can_lookup_subjects(self):
        """Tests if this user can perform ``Subject`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_subject_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_subject_view(self):
        """A complete view of the ``Subject`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_ontology_view(self):
        """Federates the view for methods in this session.
        A federated view will include subjects in ontologies which are
        children of this ontology in the ontology hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_ontology_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this ontology only.



        """
        raise UNIMPLEMENTED()

    def get_subject(self, subject_id):
        """Gets the ``Subject`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Subject`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Subject`` and retained for
        compatibility.

        :param subject_id: ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :return: the subject
        :rtype: ``osid.ontology.Subject``
        :raise: ``NotFound`` -- ``subject_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subjects_by_ids(self, subject_ids):
        """Gets a ``SubjectList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the subjects
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Subjects`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param subject_ids: the list of ``Ids`` to retrieve
        :type subject_ids: ``osid.id.IdList``
        :return: the returned ``Subject`` list
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``subject_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subjects_by_genus_type(self, subject_genus_type):
        """Gets a ``SubjectList`` corresponding to the given subject genus ``Type`` which does not include subjects of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known subjects
        or an error results. Otherwise, the returned list may contain
        only those subjects that are accessible through this session.

        :param subject_genus_type: a subject genus type
        :type subject_genus_type: ``osid.type.Type``
        :return: the returned ``Subject`` list
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NullArgument`` -- ``subject_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subjects_by_parent_genus_type(self, subject_genus_type):
        """Gets a ``SubjectList`` corresponding to the given subject genus ``Type`` and include any additional subject with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known terms or
        an error results. Otherwise, the returned list may contain only
        those subjects that are accessible through this session.

        :param subject_genus_type: a subject genus type
        :type subject_genus_type: ``osid.type.Type``
        :return: the returned ``Subject`` list
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NullArgument`` -- ``subject_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subjects_by_record_type(self, subject_record_type):
        """Gets a ``SubjectList`` containing the given term record ``Type``.
        In plenary mode, the returned list contains all known subjects
        or an error results. Otherwise, the returned list may contain
        only those subjects that are accessible through this session.

        :param subject_record_type: a subject record type
        :type subject_record_type: ``osid.type.Type``
        :return: the returned ``Subject`` list
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NullArgument`` -- ``subject_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subjects(self):
        """Gets all ``Subjects``.
        In plenary mode, the returned list contains all known subjects
        or an error results. Otherwise, the returned list may contain
        only those subjects that are accessible through this session.

        :return: a ``SubjectList``
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    subjects = property(fget=get_subjects)


##
# The following methods are from osid.ontology.SubjectQuerySession

    def can_search_subjects(self):
        """Tests if this user can perform ``Subjects`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_subject_query(self):
        """Gets a subject query.

        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``

        """
        raise UNIMPLEMENTED()

    subject_query = property(fget=get_subject_query)

    def get_subjects_by_query(self, subject_query):
        """Gets a list of ``Subjects`` matching the given subject query.

        :param subject_query: the subject query
        :type subject_query: ``osid.ontology.SubjectQuery``
        :return: the returned ``SubjectList``
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NullArgument`` -- ``subject_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``subject_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectSearchSession

    def get_subject_search(self):
        """Gets a subject search.

        :return: the subject search
        :rtype: ``osid.ontology.SubjectSearch``

        """
        raise UNIMPLEMENTED()

    subject_search = property(fget=get_subject_search)

    def get_subject_search_order(self):
        """Gets a subject search order.
        The ``SubjectSearchOrder`` is supplied to a ``SubjectSearch`` to
        specify the ordering of results.

        :return: the subject search order
        :rtype: ``osid.ontology.SubjectSearchOrder``

        """
        raise UNIMPLEMENTED()

    subject_search_order = property(fget=get_subject_search_order)

    def get_subjects_by_search(self, subject_query, subject_search):
        """Gets the search results matching the given search query using the given search.

        :param subject_query: the subject query
        :type subject_query: ``osid.ontology.SubjectQuery``
        :param subject_search: the subject search
        :type subject_search: ``osid.ontology.SubjectSearch``
        :return: the subject search results
        :rtype: ``osid.ontology.SubjectSearchResults``
        :raise: ``NullArgument`` -- ``subject_query`` or ``subject_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``subject_search`` or ``subject_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_subject_query_from_inspector(self, subject_query_inspector):
        """Gets a subject query from an inspector.
        The inspector is available from a ``SubjecttSearchResults``.

        :param subject_query_inspector: a subject query inspector
        :type subject_query_inspector: ``osid.ontology.SubjectQueryInspector``
        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``
        :raise: ``NullArgument`` -- ``subject_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``subject_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectAdminSession

    def can_create_subjects(self):
        """Tests if this user can create ``Subjects``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a subject
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Subject`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_subject_with_record_types(self, subject_record_types):
        """Tests if this user can create a single ``Subject`` using the desired record interface types.
        While ``OntologyManager.getSubjectRecordTypes()`` can be used to
        examine which record interfaces are supported, this method tests
        which record(s) are required for creating a specific
        ``Subject``. Providing an empty array tests if a ``Subject`` can
        be created with no records.

        :param subject_record_types: array of subject record types
        :type subject_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Subject`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``subject_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_subject_form_for_create(self, subject_record_types):
        """Gets the subject form for creating new subjects.
        A new form should be requested for each create transaction.

        :param subject_record_types: array of subject record types
        :type subject_record_types: ``osid.type.Type[]``
        :return: the subject form
        :rtype: ``osid.ontology.SubjectForm``
        :raise: ``NullArgument`` -- ``subject_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_subject(self, subject_form):
        """Creates a new ``Subject``.

        :param subject_form: the form for this ``Subject``
        :type subject_form: ``osid.ontology.SubjectForm``
        :return: the new ``Subject``
        :rtype: ``osid.ontology.Subject``
        :raise: ``IllegalState`` -- ``subject_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``subject_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``subject_form`` did not originate from ``get_subject_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_subjects(self):
        """Tests if this user can update ``Subjects``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Subject`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if subject modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_subject_form_for_update(self, subject_id):
        """Gets the subject form for updating an existing subject.
        A new subject form should be requested for each update
        transaction.

        :param subject_id: the ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :return: the subject form
        :rtype: ``osid.ontology.SubjectForm``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_subject(self, subject_form):
        """Updates an existing subject.

        :param subject_form: the form containing the elements to be updated
        :type subject_form: ``osid.ontology.SubjectForm``
        :raise: ``IllegalState`` -- ``subject_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``subject_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``subject_form`` did not originate from ``get_subject_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_subjects(self):
        """Tests if this user can delete ``Subjects``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Subject`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Subject`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_subject(self, subject_id):
        """Deletes the ``Subject`` identified by the given ``Id``.

        :param subject_id: the ``Id`` of the ``Subject`` to delete
        :type subject_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Subject`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_subject_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Subjects``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Subject`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_subject(self, subject_id, alias_id):
        """Adds an ``Id`` to a ``Subject`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Subject`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another subject, it is
        reassigned to the given subject ``Id``.

        :param subject_id: the ``Id`` of a ``Subject``
        :type subject_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``subject_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectNotificationSession

    def can_register_for_subject_notifications(self):
        """Tests if this user can register for ``Subject`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_subjects(self):
        """Register for notifications of new subjects.
        ``SubjectReceiver.newSubject()`` is invoked when a new subject
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_subject_ancestors(self, subject_id):
        """Registers for notification if an ancestor is added to the specified function in the subject hierarchy.
        ``SubjectReceiver.newSubjectAncestor()`` is invoked when the
        specified subject experiences an addition in ancestry.

        :param subject_id: the ``Id`` of the subject to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_subject_descendants(self, subject_id):
        """Registers for notification if a descendant is added to the specified subject in the subject hierarchy.
        ``SubjectReceiver.newSubjectDescendant()`` is invoked when the
        specified subject experiences an addition in descendants.

        :param subject_id: the ``Id`` of the subject to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_subjects(self):
        """Registers for notification of updated subjects.
        ``SubjectReceiver.changedSubject()`` is invoked when a subject
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_subject(self, subject_id):
        """Registers for notification of an updated subject.
        ``SubjectReceiver.changedSubject()`` is invoked when the
        specified subject is changed.

        :param subject_id: the ``Id`` of the ``Subject`` to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subject_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_subjects(self):
        """Registers for notification of deleted subjects.
        ``SubjectReceiver.deletedSubject()`` is invoked when a subject
        is removed from this ontology.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_subject(self, subject_id):
        """Registers for notification of a deleted subject.
        ``SubjectReceiver.changedSubject()`` is invoked when the
        specified subject is removed from this ontology.

        :param subject_id: the ``Id`` of the ``Subject`` to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subjectid is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_subject_ancestors(self, subject_id):
        """Registers for notification if an ancestor is removed from the specified subject in the subject hierarchy.
        ``SubjectReceiver.deletedSubjectAncestor()`` is invoked when the
        specified subject experiences a removal of an ancestor.

        :param subject_id: the ``Id`` of the subject to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_subject_descendants(self, subject_id):
        """Registers for notification if a descendant is removed from fthe specified subject in the subject hierarchy.
        ``SubjectReceiver.deletedSubjectDescednant()`` is invoked when
        the specified subject experiences a removal of one of its
        descendants.

        :param subject_id: the ``Id`` of the subject to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectHierarchySession

    def get_subject_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    subject_hierarchy_id = property(fget=get_subject_hierarchy_id)

    def get_subject_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    subject_hierarchy = property(fget=get_subject_hierarchy)

    def can_access_subject_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer traversal
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_subject_ids(self):
        """Gets the root subject ``Ids`` in this hierarchy.

        :return: the root subject ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_subject_ids = property(fget=get_root_subject_ids)

    def get_root_subjects(self):
        """Gets the root subjects in this subject hierarchy.

        :return: the root subjects
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_subjects = property(fget=get_root_subjects)

    def has_parent_subjects(self, subject_id):
        """Tests if the ``Subject`` has any parents.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :return: ``true`` if the subject has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_subject(self, id_, subject_id):
        """Tests if an ``Id`` is a direct parent of a subject.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``subject_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_subject_ids(self, subject_id):
        """Gets the parent Ids of the given subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the subject
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_subjects(self, subject_id):
        """Gets the parents of the given subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :return: the parents of the subject
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_subject(self, id_, subject_id):
        """Tests if an ``Id`` is an ancestor of a subject.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``subject_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_subjects(self, subject_id):
        """Tests if a subject has any children.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :return: ``true`` if the ``subject_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_subject(self, id_, subject_id):
        """Tests if a subject is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``subject_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_subject_ids(self, subject_id):
        """Gets the child ``Ids`` of the given subject.

        :param subject_id: the ``Id`` to query
        :type subject_id: ``osid.id.Id``
        :return: the children of the subject
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_subjects(self, subject_id):
        """Gets the children of the given subject.

        :param subject_id: the ``Id`` to query
        :type subject_id: ``osid.id.Id``
        :return: the children of the subject
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_subject(self, id_, subject_id):
        """Tests if an ``Id`` is a descendant of a subject.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``subject_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subject_node_ids(self, subject_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given subject.

        :param subject_id: the ``Id`` to query
        :type subject_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a subject node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subject_nodes(self, subject_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given subject.

        :param subject_id: the ``Id`` to query
        :type subject_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a subject node
        :rtype: ``osid.ontology.SubjectNode``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectHierarchyDesignSession

    def can_modify_subject_hierarchy(self):
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

    def add_root_subject(self, subject_id):
        """Adds a root subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``subject_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``subject_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_subject(self, subject_id):
        """Removes a root subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``subject_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- the root subjects
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_subject(self, subject_id, child_id):
        """Adds a child to a subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``subject_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``subject_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_subject(self, subject_id, child_id):
        """Removes a child from a subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``subject_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``subject_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_subjects(self, subject_id):
        """Removes all children from a subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``subject_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectOntologySession

    def can_lookup_subject_ontology_mappings(self):
        """Tests if this user can perform lookups of subject/ontology mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_ontology_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_ontology_view(self):
        """A complete view of the ``Subject`` and ``Ontology`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_subject_ids_by_ontology(self, ontology_id):
        """Gets the list of ``Subject``  ``Ids`` associated with an ``Ontology``.

        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: list of related subject ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subjects_by_ontology(self, ontology_id):
        """Gets the list of ``Subjects`` associated with an ``Ontology``.

        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: list of related subject ``Ids``
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subject_ids_by_ontologies(self, ontology_ids):
        """Gets the list of ``Subject Ids`` corresponding to a list of ``Ontologies``.

        :param ontology_ids: list of ontology ``Ids``
        :type ontology_ids: ``osid.id.IdList``
        :return: list of subject ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``ontology_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_subjects_by_ontologies(self, ontology_ids):
        """Gets the list of ``Subjects`` corresponding to a list of ``Ontologies``.

        :param ontology_ids: list of ontology ``Ids``
        :type ontology_ids: ``osid.id.IdList``
        :return: list of subjects
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``NullArgument`` -- ``ontology_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontology_ids_by_subject(self, subject_id):
        """Gets the list of ``Ontology``  ``Ids`` mapped to a ``Subject``.

        :param subject_id: ``Id`` of a ``Subject``
        :type subject_id: ``osid.id.Id``
        :return: list of ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontologies_by_subject(self, subject_id):
        """Gets the list of ``Ontologies`` mapped to a ``Subject``.

        :param subject_id: ``Id`` of a ``Subject``
        :type subject_id: ``osid.id.Id``
        :return: list of ontologies
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectOntologyAssignmentSession

    def can_assign_subjects(self):
        """Tests if this user can alter subject/ontology mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_subjects_to_ontology(self, ontology_id):
        """Tests if this user can alter subject/ontology mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_ontology_ids(self, ontology_id):
        """Gets a list of ontologies including and under the given ontology node in which any subject can be assigned.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: list of assignable ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_ontology_ids_for_subject(self, ontology_id, subject_id):
        """Gets a list of ontologies including and under the given ontology node in which a specific subject can be assigned.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :param subject_id: the ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :return: list of assignable ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``ontology_id`` or ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_subject_to_ontology(self, subject_id, ontology_id):
        """Adds an existing ``Subject`` to an ``Ontology``.

        :param subject_id: the ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``subject_id`` is already assigned to ``ontology_id``
        :raise: ``NotFound`` -- ``subject_id`` or ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_subject_from_ontology(self, subject_id, ontology_id):
        """Removes a ``Subject`` from an ``Ontology``.

        :param subject_id: the ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``subject_id`` or ``ontology_id`` not found or ``subject_id`` not assigned to ``ontology_id``
        :raise: ``NullArgument`` -- ``subject_id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.SubjectSmartOntologySession

    def can_manage_smart_ontologies(self):
        """Tests if this user can manage smart ontologies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        :return: ``false`` if smart ontology methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_subject_query(self, subject_query):
        """Applies a subject query to this ontology.

        :param subject_query: the subject query
        :type subject_query: ``osid.ontology.SubjectQuery``
        :raise: ``NullArgument`` -- ``subject_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``subject_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_subject_query(self):
        """Gets a subject query inspector for this ontology.

        :return: the subject query inspector
        :rtype: ``osid.ontology.SubjectQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_subject_sequencing(self, subject_search_order):
        """Applies a subject search order to this ontology.

        :param subject_search_order: the subject search order
        :type subject_search_order: ``osid.ontology.SubjectSearchOrder``
        :raise: ``NullArgument`` -- ``subject_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``subject_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.RelevancyLookupSession

    def can_lookup_relevancies(self):
        """Tests if this user can lookup subject relevancies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_relevancy_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_relevancy_view(self):
        """A complete view of the ``Relevancy`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_effective_relevancy_view(self):
        """The returns from the lookup methods return only effetive relevancies."""
        raise UNIMPLEMENTED()

    def use_any_effective_relevancy_view(self):
        """Both effective and ineffective relavcnies are returned."""
        raise UNIMPLEMENTED()

    def get_relevancy(self, relevancy_id):
        """Gets the ``Relevancy`` specified by its ``Id``.

        :param relevancy_id: ``Id`` of the ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :return: the relevancy
        :rtype: ``osid.ontology.Relevancy``
        :raise: ``NotFound`` -- ``relevancy_id`` not found
        :raise: ``NullArgument`` -- ``relevancy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_ids(self, relevancy_ids):
        """Gets a ``RelevancyList`` corresponding to the given ``IdList``.

        :param relevancy_ids: the list of ``Ids`` to retrieve
        :type relevancy_ids: ``osid.id.IdList``
        :return: the returned ``Relevancy list``
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``relevancy_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_genus_type(self, relevancy_genus_type):
        """Gets the relevancies for the given relevancy and genus type.

        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``relevancy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_parent_genus_type(self, relevancy_genus_type):
        """Gets the relevancies for the given relevancy genus type and include any relevancies with a genus type derived from the specified genus type.

        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``relevancy_genus_t_ype`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_record_type(self, relevancy_record_type):
        """Gets a ``RelevancyList`` containing the given relevancy record ``Type``.

        :param relevancy_record_type: a relevancy record type
        :type relevancy_record_type: ``osid.type.Type``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``relevancy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_on_date(self, from_, to):
        """Gets a ``RelevancyList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: a starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: an ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_for_subject(self, subject_id):
        """Gets the ``Relevancy`` mapped to a subject ``Id``.

        :param subject_id: the subject ``Id``
        :type subject_id: ``osid.id.Id``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_for_subject_on_date(self, subject_id, from_, to):
        """Gets a ``RelevancyList`` for the given subject effective during the entire given date range inclusive but not confined to the date range.

        :param subject_id: the subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param from: a starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: an ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``subject_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_genus_type_for_subject(self, subject_id, relevancy_genus_type):
        """Gets the ``Relevancy`` mapped to a subject ``Id`` and relevancy ``genus Type``.
        Genus ``Types`` derived from the given genus ``Typ`` e are
        included.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Relevancy`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Relevancy`` and retained
        for compatibility.
        
        In effective mode, relevancies are returned that are currently
        effective. In any effective mode, effective relevancies and
        those currently expired are returned.

        :param subject_id: the subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``subject_id`` or ``relevancy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_genus_type_for_subject_on_date(self, subject_id, relevancy_genus_type, from_, to):
        """Gets a ``RelevancyList`` of the given genus type for the given subject effective during the entire given date range inclusive but not confined to the date range.

        :param subject_id: the subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :param from: a starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: an ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``subject_id, relevancy_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_for_subjects(self, subject_ids):
        """Gets the relevancies for the given subject ``Ids``.

        :param subject_ids: list of subject ``Ids``
        :type subject_ids: ``osid.id.IdList``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``subject_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_for_mapped_id(self, id_):
        """Gets the ``Relevancy`` elements mapped to an ``Id``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_for_mapped_id_on_date(self, id_, from_, to):
        """Gets a ``RelevancyList`` for the given mapped ``Id`` effective during the entire given date range inclusive but not confined to the date range.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param from: a starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: an ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_genus_type_for_mapped_id(self, id_, relevancy_genus_type):
        """Gets the ``Relevancy`` elements mapped to an ``Id`` of the given relevancy genus ``Type`` which includes derived genus ``Types``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``id`` or ``relevancy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_genus_type_for_mapped_id_on_date(self, id_, relevancy_genus_type, from_, to):
        """Gets a ``RelevancyList`` of the given genus type for the given mapped ``Id`` effective during the entire given date range inclusive but not confined to the date range.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :param from: a starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: an ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``id, relevancy_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_for_mapped_ids(self, ids):
        """Gets the relevancies for the given mapped ``Ids``.

        :param ids: a list of ``Ids``
        :type ids: ``osid.id.IdList``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_for_subject_and_mapped_id(self, subject_id, id_):
        """Gets the ``Relevancy`` mapped to a subject and mapped ``Id``.

        :param subject_id: the subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param id: the mapped ``Id``
        :type id: ``osid.id.Id``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``subject_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_for_subject_and_mapped_id_on_date(self, subject_id, id_, from_, to):
        """Gets a ``RelevancyList`` for the given subject and mapped ``Id`` effective during the entire given date range inclusive but not confined to the date range.

        :param subject_id: the subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param id: the mapped ``Id``
        :type id: ``osid.id.Id``
        :param from: a starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: an ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``subject_id, id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_genus_type_for_subject_and_mapped_id(self, subject_id, id_, relevancy_genus_type):
        """Gets the ``Relevancy`` of the given genus type and mapped to a subject and mapped ``Id``.

        :param subject_id: the subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param id: the mapped ``Id``
        :type id: ``osid.id.Id``
        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``subject_id, id`` , or ``relevancy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_genus_type_for_subject_and_mapped_id_on_date(self, subject_id, id_, relevancy_genus_type, from_, to):
        """Gets a ``RelevancyList`` of the given genus type and related to the given subject and mapped ``Id`` effective during the entire given date range inclusive but not confined to the date range.

        :param subject_id: the subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param id: the mapped ``Id``
        :type id: ``osid.id.Id``
        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :param from: a starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: an ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``subject_id, id, relevancy_genus_t_ype, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies(self):
        """Gets all relevancies.

        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    relevancies = property(fget=get_relevancies)


##
# The following methods are from osid.ontology.RelevancyQuerySession

    def can_search_relevancies(self):
        """Tests if this user can perform ``Relevancy`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_query(self):
        """Gets a relevancy query.

        :return: the relevancy query
        :rtype: ``osid.ontology.RelevancyQuery``

        """
        raise UNIMPLEMENTED()

    relevancy_query = property(fget=get_relevancy_query)

    def get_relevancies_by_query(self, relevancy_query):
        """Gets a list of relevancies matching the given relevancy query.

        :param relevancy_query: the relevancy query
        :type relevancy_query: ``osid.ontology.RelevancyQuery``
        :return: the returned ``RelevancyList``
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``relevancy_query is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relevancy_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.RelevancySearchSession

    def get_relevancy_search(self):
        """Gets a relevancy search.

        :return: the relevancy search
        :rtype: ``osid.ontology.RelevancySearch``

        """
        raise UNIMPLEMENTED()

    relevancy_search = property(fget=get_relevancy_search)

    def get_relevancy_search_order(self):
        """Gets a relevancy search order.
        The ``RelevancySearchOrder`` is supplied to a
        ``RelevancySearch`` to specify the ordering of results.

        :return: the relevancy search order
        :rtype: ``osid.ontology.RelevancySearchOrder``

        """
        raise UNIMPLEMENTED()

    relevancy_search_order = property(fget=get_relevancy_search_order)

    def get_relevancies_by_search(self, relevancy_query, relevancy_search):
        """Gets the search results matching the given search query using the given search.

        :param relevancy_query: the relevancy query
        :type relevancy_query: ``osid.ontology.RelevancyQuery``
        :param relevancy_search: the relevancy search
        :type relevancy_search: ``osid.ontology.RelevancySearch``
        :return: the relevancy search results
        :rtype: ``osid.ontology.RelevancySearchResults``
        :raise: ``NullArgument`` -- ``relevancy_query`` or ``relevancy_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relevancy_search`` or ``relevancy_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_relevancy_query_from_inspector(self, relevancy_query_inspector):
        """Gets a relevancy query from an inspector.
        The inspector is available from a ``RelevancySearchResults``.

        :param relevancy_query_inspector: a relevancy query inspector
        :type relevancy_query_inspector: ``osid.ontology.RelevancyQueryInspector``
        :return: the relevancy query
        :rtype: ``osid.ontology.RelevancyQuery``
        :raise: ``NullArgument`` -- ``relevancy_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``relevancy_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.RelevancyAdminSession

    def can_create_relevancies(self):
        """Tests if this user can create relevancies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Relevancy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Relevancy`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_relevancy_with_record_types(self, relevancy_record_types):
        """Tests if this user can create a single ``Relevancy`` using the desired record interface types.
        While ``OntologyManager.getRelevancyRecordTypes()`` can be used
        to examine which record interfaces are supported, this method
        tests which record(s) are required for creating a specific
        ``Relevancy``. Providing an empty array tests if a ``Relevancy``
        can be created with no records.

        :param relevancy_record_types: array of relevancy record types
        :type relevancy_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Relevancy`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relevancy_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_form_for_create(self, subject_id, id_, relevancy_record_types):
        """Gets the relevancy form for creating new relevancies.
        A new form should be requested for each create transaction.

        :param subject_id: the ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :param id: a mapped ``Id``
        :type id: ``osid.id.Id``
        :param relevancy_record_types: array of relevancy record types
        :type relevancy_record_types: ``osid.type.Type[]``
        :return: the relevancy form
        :rtype: ``osid.ontology.RelevancyForm``
        :raise: ``NotFound`` -- ``subject_id`` is not found
        :raise: ``NullArgument`` -- ``subject_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_relevancy(self, relevancy_form):
        """Creates a new ``Relevancy``.

        :param relevancy_form: the form for this ``Relevancy``
        :type relevancy_form: ``osid.ontology.RelevancyForm``
        :return: the new ``Relevancy``
        :rtype: ``osid.ontology.Relevancy``
        :raise: ``IllegalState`` -- ``relevancy_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``relevancy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relevancy_form`` did not originate from ``get_relevancy_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_relevancies(self):
        """Tests if this user can update relevancies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Relevancy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if relevancy modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_form_for_update(self, relevancy_id):
        """Gets the relevancy form for updating an existing relevancy.
        A new relevancy form should be requested for each update
        transaction.

        :param relevancy_id: the ``Id`` of the ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :return: the relevancy form
        :rtype: ``osid.ontology.RelevancyForm``
        :raise: ``NotFound`` -- ``relevancy_id`` is not found
        :raise: ``NullArgument`` -- ``relevancy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_relevancy(self, relevancy_form):
        """Updates an existing relevancy.

        :param relevancy_form: the form containing the elements to be updated
        :type relevancy_form: ``osid.ontology.RelevancyForm``
        :raise: ``IllegalState`` -- ``relevancy_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``relevancy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relevancy_form`` did not originate from ``get_relevancy_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_relevancies(self):
        """Tests if this user can delete relevancies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Relevancy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Relevancy`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_relevancy(self, relevancy_id):
        """Deletes the ``Relevancy`` identified by the given ``Id``.

        :param relevancy_id: the ``Id`` of the ``Relevancy`` to delete
        :type relevancy_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Relevancy`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``relevancy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_relevancy_aliases(self):
        """Tests if this user can manage ``Id`` aliases for relevancies.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Relevancy`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_relevancy(self, relevancy_id, alias_id):
        """Adds an ``Id`` to a ``Relevancy`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Relevancy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another relevancy, it is
        reassigned to the given relevancy ``Id``.

        :param relevancy_id: the ``Id`` of a ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``relevancy_id`` not found
        :raise: ``NullArgument`` -- ``relevancy_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.RelevancyNotificationSession

    def can_register_for_relevancy_notifications(self):
        """Tests if this user can register for ``Relevancy`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_relevancies(self):
        """Register for notifications of new relevancies.
        ``RelevancyReceiver.newRelevancy()`` is invoked when a new
        relevancy is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_relevancies_by_genus_type(self, relevancy_genus_type):
        """Register for notifications of new relevancies by the given genus type.
        ``RelevancyReceiver.newRelevancy()`` is invoked when a new
        relevancy is created.

        :param relevancy_genus_type: the relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``relevancy_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_relevancies_for_subject(self, subject_id):
        """Register for notifications of new relevancies for the given subject.
        ``RelevancyReceiver.newRelevancy()`` is invoked when a new
        relevancy is created.

        :param subject_id: the ``Id`` of the ``Subject`` to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subject_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_relevancies_for_id(self, id_):
        """Register for notifications of new relevancies for the given mapped ``Id``.
        ``RelevancyReceiver.newRelevancy()`` is invoked when a new
        relevancy is created.

        :param id: the ``Id`` to monitor
        :type id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relevancies(self):
        """Registers for notification of updated relevancies.
        ``RelevancyReceiver.changedRelevancy()`` is invoked when a
        relevancy is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relevancies_by_genus_type(self, relevancy_genus_type):
        """Register for notifications of changed relevancies of the given genus type.
        ``RelevancyReceiver.changedRelevancy()`` is invoked when a
        relevancy is changed.

        :param relevancy_genus_type: the relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``relevancy_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relevancies_for_subject(self, subject_id):
        """Register for notifications of changed relevancies for the given subject.
        ``RelevancyReceiver.changedRelevancy()`` is invoked when a
        relevancy is changed.

        :param subject_id: the ``Id`` of the ``Subject`` to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subject_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relevancies_for_id(self, id_):
        """Register for notifications of changed relevancies for the given ``Id``.
        ``RelevancyReceiver.changedRelevancy()`` is invoked when a
        relevancy is changed.

        :param id: the ``Id`` to monitor
        :type id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_relevancy(self, relevancy_id):
        """Registers for notification of an updated relevancy.
        ``RelevancyReceiver.changedRelevancy()`` is invoked when the
        specified relevancy is changed.

        :param relevancy_id: the ``Id`` of the ``Relevancy`` to monitor
        :type relevancy_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``relevancy_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relevancies(self):
        """Registers for notification of deleted relevancies.
        ``RelevancyReceiver.deletedRelevancy()`` is invoked when a
        relevancy is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relevancies_by_genus_type(self, relevancy_genus_type):
        """Register for notifications of deleted relevancies of the given genus type.
        ``RelevancyReceiver.deletedRelevancy()`` is invoked when a
        relevancy is deleted.

        :param relevancy_genus_type: the relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``relevancy_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relevancies_for_subject(self, subject_id):
        """Register for notifications of deleted relevancies for the given subject.
        ``RelevancyReceiver.deletedRelevancy()`` is invoked when a
        relevancy is deleted.

        :param subject_id: the ``Id`` of the ``Subject`` to monitor
        :type subject_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``subject_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relevancies_for_id(self, id_):
        """Register for notifications of deleted relevancies for the given ``Id``.
        ``RelevancyReceiver.deletedRelevancy()`` is invoked when a
        relevancy is deleted.

        :param id: the ``Id`` to monitor
        :type id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_relevancy(self, relevancy_id):
        """Registers for notification of a deleted relevancy.
        ``RelevancyReceiver.changedRelevancy()`` is invoked when the
        specified relevancy is deleted.

        :param relevancy_id: the ``Id`` of the ``Relevancy`` to monitor
        :type relevancy_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``relevancy_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.RelevancyOntologySession

    def can_lookup_relevancy_ontology_mappings(self):
        """Tests if this user can perform lookups of relevancy/ontology mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_relevancy_ids_by_ontology(self, ontology_id):
        """Gets the list of ``Relevancy``  ``Ids`` associated with an ``Ontology``.

        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: list of related ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_ontology(self, ontology_id):
        """Gets the list of ``Relevancies`` associated with an ``Ontology``.

        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: list of related relevancy ``Ids``
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NotFound`` -- ``ontology_id`` is not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancy_ids_by_ontologies(self, ontology_ids):
        """Gets the list of ``Relevancy Ids`` corresponding to a list of ``Ontologies``.

        :param ontology_ids: list of ontology ``Ids``
        :type ontology_ids: ``osid.id.IdList``
        :return: list of relevancy ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``ontology_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_relevancies_by_ontologies(self, ontology_ids):
        """Gets the list of ``Relevancies`` corresponding to a list of ``Ontologies``.

        :param ontology_ids: list of ontology ``Ids``
        :type ontology_ids: ``osid.id.IdList``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``NullArgument`` -- ``ontology_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontology_ids_by_relevancy(self, relevancy_id):
        """Gets the list of ``Ontology``  ``Ids`` mapped to a ``Relevancy``.

        :param relevancy_id: ``Id`` of a ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :return: list of ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``relevancy_id`` is not found
        :raise: ``NullArgument`` -- ``relevancy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_ontologies_by_relevancy(self, relevancy_id):
        """Gets the list of ``Ontologies`` mapped to a ``Relevancy``.

        :param relevancy_id: ``Id`` of a ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :return: list of ontologies
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``NotFound`` -- ``relevancy_id`` is not found
        :raise: ``NullArgument`` -- ``relevancy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.RelevancyOntologyAssignmentSession

    def can_assign_relevancies(self):
        """Tests if this user can alter relevancy/ontology mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_relevancies_to_ontology(self, ontology_id):
        """Tests if this user can alter relevancy/ontology mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_ontology_ids_for_relevancy(self, ontology_id, relevancy_id):
        """Gets a list of ontologies including and under the given ontology node in which a specific relevancy can be assigned.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :param relevancy_id: the ``Id`` of the ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :return: list of assignable ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``ontology_id`` or ``relevancy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_relevancy_to_ontology(self, relevancy_id, ontology_id):
        """Adds an existing ``Relevancy`` to an ``Ontology``.

        :param relevancy_id: the ``Id`` of the ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``relevancy_id`` is already assigned to ``ontology_id``
        :raise: ``NotFound`` -- ``relevancy_id`` or ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``relevancy_id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_relevancy_from_ontology(self, relevancy_id, ontology_id):
        """Removes a ``Relevancy`` from an ``Ontology``.

        :param relevancy_id: the ``Id`` of the ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``relevancy_id`` or ``ontology_id`` not found or ``relevancy_id`` not assigned to ``ontology_id``
        :raise: ``NullArgument`` -- ``relevancy_id`` or ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.ontology.RelevancySmartOntologySession

    def apply_relevancy_query(self, relevancy_query):
        """Applies a relevancy query to this ontology.

        :param relevancy_query: the relevancy query
        :type relevancy_query: ``osid.ontology.RelevancyQuery``
        :raise: ``NullArgument`` -- ``relevancy_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``relevancy_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_relevancy_query(self):
        """Gets a relevancy query inspector for this ontology.

        :return: the relevancy query inspector
        :rtype: ``osid.ontology.RelevancyQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_relevancy_sequencing(self, relevancy_search_order):
        """Applies a relevancy search order to this ontology.

        :param relevancy_search_order: the relevancy search order
        :type relevancy_search_order: ``osid.ontology.RelevancySearchOrder``
        :raise: ``NullArgument`` -- ``relevancy_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``relevancy_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class OntologyList(osid_objects.OsidList):

    def get_next_ontology(self):
        """Gets the next ``Ontology`` in this list.

        :return: the next ``Ontology`` in this list. The ``has_next()`` method should be used to test that a next ``Ontology`` is available before calling this method.
        :rtype: ``osid.ontology.Ontology``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_ontology = property(fget=get_next_ontology)

    def get_next_ontologies(self, n):
        """Gets the next set of ``Ontology`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Ontology`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Ontology`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.ontology.Ontology``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Ontologies(OntologyManager):
    pass


