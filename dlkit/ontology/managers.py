from ..osid import managers as osid_managers


class OntologyProfile(osid_managers.OsidProfile):
    """The ``OntologyProfile`` describes the interoperability among ontology services."""
    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_lookup(self):
        """Tests if a subject lookup service is supported.

        a subject lookup service defines methods to access subjects.

        :return: true if subject lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_query(self):
        """Tests if a subject query service is supported.

        :return: ``true`` if subject query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_search(self):
        """Tests if a subject search service is supported.

        :return: ``true`` if subject search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_admin(self):
        """Tests if a subject administrative service is supported.

        :return: ``true`` if subject admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_notification(self):
        """Tests if subject notification is supported.

        Messages may be sent when subjects are created, modified, or
        deleted.

        :return: ``true`` if subject notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_hierarchy(self):
        """Tests if a subject hierarchy traversal is supported.

        :return: ``true`` if a subject hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_hierarchy_design(self):
        """Tests if subject hierarchy design is supported.

        :return: ``true`` if a subject hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_ontology(self):
        """Tests if a subject to ontology lookup session is available.

        :return: ``true`` if subject ontology lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_ontology_assignment(self):
        """Tests if a subject to ontology assignment session is available.

        :return: ``true`` if subject ontology assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_subject_smart_ontology(self):
        """Tests if a subject smart ontology session is available.

        :return: ``true`` if subject smart ontology session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relevancy_lookup(self):
        """Tests if a subject relevancy lookup service is supported.

        :return: ``true`` if relevancy lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relevancy_query(self):
        """Tests if a relevancy query service is supported.

        :return: ``true`` if relevancy query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relevancy_search(self):
        """Tests if a relevancy search service is supported.

        :return: ``true`` if relevancy search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relevancy_admin(self):
        """Tests if a relevancy administrative service is supported.

        :return: ``true`` if relevancy admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relevancy_notification(self):
        """Tests if relevancy notification is supported.

        Messages may be sent when subject relevancies are created,
        modified, or deleted.

        :return: ``true`` if relevancy notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_lookup(self):
        """Tests if an ontology lookup service is supported.

        :return: ``true`` if ontology lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relevancy_ontology(self):
        """Tests if a relevancy to ontology lookup session is available.

        :return: ``true`` if relevancy ontology lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relevancy_ontology_assignment(self):
        """Tests if a relevancy to ontology assignment session is available.

        :return: ``true`` if relevancy ontology assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_relevancy_smart_ontology(self):
        """Tests if a relevancy smart ontology session is available.

        :return: ``true`` if relevancy smart ontology session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_query(self):
        """Tests if an ontology query service is supported.

        :return: ``true`` if ontology query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_search(self):
        """Tests if an ontology search service is supported.

        :return: ``true`` if ontology search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_admin(self):
        """Tests if an ontology administrative service is supported.

        :return: ``true`` if ontology admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_notification(self):
        """Tests if ontology notification is supported.

        Messages may be sent when ontologies are created, modified, or
        deleted.

        :return: ``true`` if ontology notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_hierarchy(self):
        """Tests if an ontology hierarchy traversal is supported.

        :return: ``true`` if an ontology hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_hierarchy_design(self):
        """Tests if ontology hierarchy design is supported.

        :return: ``true`` if an ontology hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_assignment(self):
        """Tests if ``Ids`` can be asssigned to ontologies.

        :return: ``true`` if an ontology hassignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_batch(self):
        """Tests if an ontology batch service is supported.

        :return: ``true`` if ontology batch is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def supports_ontology_rules(self):
        """Tests if an ontology rules service is supported.

        :return: ``true`` if ontology rules is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_subject_record_types(self):
        """Gets the supported ``Subject`` record types.

        :return: a list containing the supported ``Subject`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    subject_record_types = property(fget=get_subject_record_types)

    def supports_subject_record_type(self, subject_record_type):
        """Tests if the given ``Subject`` record type is supported.

        :param subject_record_type: a ``Type`` indicating a ``Subject`` record type
        :type subject_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``subject_record_type`` is ``null``

        """
        return # boolean

    def get_subject_search_record_types(self):
        """Gets the supported ``Subject`` search record types.

        :return: a list containing the supported ``Subject`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    subject_search_record_types = property(fget=get_subject_search_record_types)

    def supports_subject_search_record_type(self, subject_search_record_type):
        """Tests if the given ``Subject`` search record type is supported.

        :param subject_search_record_type: a ``Type`` indicating a ``Subject`` search record type
        :type subject_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``subject_search_record_type`` is ``null``

        """
        return # boolean

    def get_relevancy_record_types(self):
        """Gets the supported ``Relevancy`` record types.

        :return: a list containing the supported ``Relevancy`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    relevancy_record_types = property(fget=get_relevancy_record_types)

    def supports_relevancy_record_type(self, relevancy_record_type):
        """Tests if the given ``Relevancy`` record type is supported.

        :param relevancy_record_type: a ``Type`` indicating a ``Relevnacy`` record type
        :type relevancy_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relevancy_record_type`` is ``null``

        """
        return # boolean

    def get_relevancy_search_record_types(self):
        """Gets the supported ``Relevancy`` search record types.

        :return: a list containing the supported ``Relevancy`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    relevancy_search_record_types = property(fget=get_relevancy_search_record_types)

    def supports_relevancy_search_record_type(self, relevancy_search_record_type):
        """Tests if the given ``Relevancy`` search record type is supported.

        :param relevancy_search_record_type: a ``Type`` indicating a ``Relevancy`` search record type
        :type relevancy_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``relevancy_search_record_type`` is ``null``

        """
        return # boolean

    def get_ontology_record_types(self):
        """Gets the supported ``Ontology`` record types.

        :return: a list containing the supported ``Ontology`` record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    ontology_record_types = property(fget=get_ontology_record_types)

    def supports_ontology_record_type(self, ontology_record_type):
        """Tests if the given ``Ontology`` record type is supported.

        :param ontology_record_type: a ``Type`` indicating an ``Ontology`` type
        :type ontology_record_type: ``osid.type.Type``
        :return: ``true`` if the given ontology record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``

        """
        return # boolean

    def get_ontology_search_record_types(self):
        """Gets the supported ontology search record types.

        :return: a list containing the supported ``Ontology`` search record types
        :rtype: ``osid.type.TypeList``

        """
        return # osid.type.TypeList

    ontology_search_record_types = property(fget=get_ontology_search_record_types)

    def supports_ontology_search_record_type(self, ontology_search_record_type):
        """Tests if the given ontology search record type is supported.

        :param ontology_search_record_type: a ``Type`` indicating an ``Ontology`` search record type
        :type ontology_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_search_record_type`` is ``null``

        """
        return # boolean


class OntologyManager(osid_managers.OsidManager, OntologyProfile):
    """The ontology manager provides access to ontology sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``SubjectLookupSession:`` a session to look up subjects
      * ``SubjectQuerySession:`` a session to query subjects ``None``
      * ``SubjectSearchSession:`` a session to search subjects
      * ``SubjectAdminSession:`` a session to create, modify and delete
        subjects ``None``
      * ``SubjectNotificationSession: a`` session to receive messages
        pertaining to subject ```` changes
      * ``SubjectHierarchySession:`` a session to traverse subject
        hierarchies
      * ``SubjectHierarchyDesignSession:`` a sesion to manage subject
        hierarchies
      * ``SubjectOntologySession:`` a session for retriieving subject
        and ontology mappings
      * ``SubjectOntologyAssignmentSession:`` a session for managing
        subject and ontology mappings
      * ``SubjectSmartOntologySession:`` a session to manage dynamic
        ontologies of subjects
    
      * ``RelevancyLookupSession:`` a session to look up subject
        relevancies
      * ``RelevancyQuerySession:`` a session to query subject
        relevancies ``None``
      * ``RelevancySearchSession:`` a session to search subject
        relevancies
      * ``RelevancyAdminSession:`` a session to create, modify and
        delete subject relevancies ``None``
      * ``RelevancyNotificationSession: a`` session to receive messages
        pertaining to subject relevancy ```` changes
      * ``RelevancyOntologySession:`` a session for retriieving
        relevancy and ontology mappings
      * ``RelevancyOntologyAssignmentSession:`` a session for managing
        relevancy and ontology mappings
      * ``RelevancySmartOntologySession:`` a session to manage dynamic
        ontologies of relevancies
    
      * ``OntologyLookupSession:`` a session to lookup ontologies
      * ``OntologyQuerySession:`` a session to search ontologies
      * ``OntologySearchSession`` : a session to search ontologies
      * ``OntologyAdminSession`` : a session to create, modify and
        delete ontologies
      * ``OntologyNotificationSession`` : a session to receive messages
        pertaining to ontology changes
      * ``OntologyHierarchySession:`` a session to traverse the ontology
        hierarchy
      * ``OntologyHierarchyDesignSession:`` a session to manage the
        ontology hierarchy


    """
    def get_subject_lookup_session(self):
        """Gets the ``OsidSession`` associated with the subject lookup service.

        :return: a ``SubjectLookupSession``
        :rtype: ``osid.ontology.SubjectLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_lookup()`` is ``false``

        """
        return # osid.ontology.SubjectLookupSession

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
        return # osid.ontology.SubjectLookupSession

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
        return # osid.ontology.SubjectLookupSession

    def get_subject_query_session(self):
        """Gets the ``OsidSession`` associated with the subject query service.

        :return: a ``SubjectQuerySession``
        :rtype: ``osid.ontology.SubjectQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_query()`` is ``false``

        """
        return # osid.ontology.SubjectQuerySession

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
        return # osid.ontology.SubjectQuerySession

    def get_subject_search_session(self):
        """Gets the ``OsidSession`` associated with the subject search service.

        :return: a ``SubjectSearchSession``
        :rtype: ``osid.ontology.SubjectSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_search()`` is ``false``

        """
        return # osid.ontology.SubjectSearchSession

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
        return # osid.ontology.SubjectSearchSession

    def get_subject_admin_session(self):
        """Gets the ``OsidSession`` associated with the subject administration service.

        :return: a ``SubjectAdminSession``
        :rtype: ``osid.ontology.SubjectAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_admin()`` is ``false``

        """
        return # osid.ontology.SubjectAdminSession

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
        return # osid.ontology.SubjectAdminSession

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
        return # osid.ontology.SubjectNotificationSession

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
        return # osid.ontology.SubjectNotificationSession

    def get_subject_hierarchy_session(self):
        """Gets the session traversing subject hierarchies.

        :return: a ``SubjectHierarchySession``
        :rtype: ``osid.ontology.SubjectHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy() is false``

        """
        return # osid.ontology.SubjectHierarchySession

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
        return # osid.ontology.SubjectHierarchySession

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
        return # osid.ontology.SubjectHierarchySession

    def get_subject_hierarchy_design_session(self):
        """Gets the session designing subject hierarchies.

        :return: a ``SubjectHierarchyDesignSession``
        :rtype: ``osid.ontology.SubjectHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_hierarchy_design() is false``

        """
        return # osid.ontology.SubjectHierarchyDesignSession

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
        return # osid.ontology.SubjectHierarchyDesignSession

    def get_subject_ontology_session(self):
        """Gets the session retrieving subject ontology mappings.

        :return: a ``SubjectOntologySession``
        :rtype: ``osid.ontology.SubjectOntologySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_ontology() is false``

        """
        return # osid.ontology.SubjectOntologySession

    subject_ontology_session = property(fget=get_subject_ontology_session)

    def get_subject_ontology_assignment_session(self):
        """Gets the session managing subject ontology mappings.

        :return: a ``SubjectOntologyAssignmentSession``
        :rtype: ``osid.ontology.SubjectOntologyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_subject_ontology_assignment() is false``

        """
        return # osid.ontology.SubjectOntologyAssignmentSession

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
        return # osid.ontology.SubjectSmartOntologySession

    def get_relevancy_lookup_session(self):
        """Gets the ``OsidSession`` associated with the relevancy lookup service.

        :return: a ``RelevancyLookupSession``
        :rtype: ``osid.ontology.RelevancyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_lookup()`` is ``false``

        """
        return # osid.ontology.RelevancyLookupSession

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
        return # osid.ontology.RelevancyLookupSession

    def get_relevancy_query_session(self):
        """Gets the ``OsidSession`` associated with the relevancy query service.

        :return: a ``RelevancyQuerySession``
        :rtype: ``osid.ontology.RelevancyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_query()`` is ``false``

        """
        return # osid.ontology.RelevancyQuerySession

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
        return # osid.ontology.RelevancyQuerySession

    def get_relevancy_search_session(self):
        """Gets the ``OsidSession`` associated with the relevancy search service.

        :return: a ``RelevancySearchSession``
        :rtype: ``osid.ontology.RelevancySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_search()`` is ``false``

        """
        return # osid.ontology.RelevancySearchSession

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
        return # osid.ontology.RelevancySearchSession

    def get_relevancy_admin_session(self):
        """Gets the ``OsidSession`` associated with the relevancy administration service.

        :return: a ``RelvancyAdminSession``
        :rtype: ``osid.ontology.RelevancyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_admin()`` is ``false``

        """
        return # osid.ontology.RelevancyAdminSession

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
        return # osid.ontology.RelevancyAdminSession

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
        return # osid.ontology.RelevancyNotificationSession

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
        return # osid.ontology.RelevancyNotificationSession

    def get_relevancy_ontology_session(self):
        """Gets the session retrieving relevancy ontology mappings.

        :return: a ``RelevancyOntologySession``
        :rtype: ``osid.ontology.RelevancyOntologySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_ontology() is false``

        """
        return # osid.ontology.RelevancyOntologySession

    relevancy_ontology_session = property(fget=get_relevancy_ontology_session)

    def get_relevancy_ontology_assignment_session(self):
        """Gets the session managing relevancy ontology mappings.

        :return: a ``RelevancyOntologyAssignmentSession``
        :rtype: ``osid.ontology.RelevancyOntologyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_relevancy_ontology_assignment() is false``

        """
        return # osid.ontology.RelevancyOntologyAssignmentSession

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
        return # osid.ontology.RelevancySmartOntologySession

    def get_ontology_lookup_session(self):
        """Gets the OsidSession associated with the ontology lookup service.

        :return: an ``OntologyLookupSession``
        :rtype: ``osid.ontology.OntologyLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_lookup() is false``

        """
        return # osid.ontology.OntologyLookupSession

    ontology_lookup_session = property(fget=get_ontology_lookup_session)

    def get_ontology_query_session(self):
        """Gets the OsidSession associated with the ontology query service.

        :return: an ``OntologyQuerySession``
        :rtype: ``osid.ontology.OntologyQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_query() is false``

        """
        return # osid.ontology.OntologyQuerySession

    ontology_query_session = property(fget=get_ontology_query_session)

    def get_ontology_search_session(self):
        """Gets the OsidSession associated with the ontology search service.

        :return: an ``OntologySearchSession``
        :rtype: ``osid.ontology.OntologySearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_search() is false``

        """
        return # osid.ontology.OntologySearchSession

    ontology_search_session = property(fget=get_ontology_search_session)

    def get_ontology_admin_session(self):
        """Gets the OsidSession associated with the ontology administration service.

        :return: an ``OntologyAdminSession``
        :rtype: ``osid.ontology.OntologyAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_admin() is false``

        """
        return # osid.ontology.OntologyAdminSession

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
        return # osid.ontology.OntologyNotificationSession

    def get_ontology_hierarchy_session(self):
        """Gets the session traversing ontology hierarchies.

        :return: an ``OntologyHierarchySession``
        :rtype: ``osid.ontology.OntologyHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_hierarchy() is false``

        """
        return # osid.ontology.OntologyHierarchySession

    ontology_hierarchy_session = property(fget=get_ontology_hierarchy_session)

    def get_ontology_hierarchy_design_session(self):
        """Gets the session designing ontology hierarchies.

        :return: an ``OntologyHierarchyDesignSession``
        :rtype: ``osid.ontology.OntologyHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_hierarchy_design() is false``

        """
        return # osid.ontology.OntologyHierarchyDesignSession

    ontology_hierarchy_design_session = property(fget=get_ontology_hierarchy_design_session)

    def get_ontology_assignment_session(self):
        """Gets the session to assign ``Ids`` to ontologies.

        :return: an ``OntologyAssignmentSession``
        :rtype: ``osid.ontology.OntologyAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_assignment() is false``

        """
        return # osid.ontology.OntologyAssignmentSession

    ontology_assignment_session = property(fget=get_ontology_assignment_session)

    def get_ontology_batch_manager(self):
        """Gets the ontology batch service.

        :return: an ``OntologyBatchManager``
        :rtype: ``osid.ontology.batch.OntologyBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_batch() is false``

        """
        return # osid.ontology.batch.OntologyBatchManager

    ontology_batch_manager = property(fget=get_ontology_batch_manager)

    def get_ontology_rules_manager(self):
        """Gets the ontology rules service.

        :return: an ``OntologyRulesManager``
        :rtype: ``osid.ontology.rules.OntologyRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_rules() is false``

        """
        return # osid.ontology.rules.OntologyRulesManager

    ontology_rules_manager = property(fget=get_ontology_rules_manager)


class OntologyProxyManager(osid_managers.OsidProxyManager, OntologyProfile):
    """The authentication manager provides access to ontology sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy``. The
    sessions included in this manager are:

      * ``SubjectLookupSession:`` a session to look up subjects
      * ``SubjectQuerySession:`` a session to query subjects ``None``
      * ``SubjectSearchSession:`` a session to search subjects
      * ``SubjectAdminSession:`` a session to create, modify and delete
        subjects ``None``
      * ``SubjectNotificationSession: a`` session to receive messages
        pertaining to subject ```` changes
      * ``SubjectHierarchySession:`` a session to traverse subject
        hierarchies
      * ``SubjectHierarchyDesignSession:`` a sesion to manage subject
        hierarchies
      * ``SubjectOntologySession:`` a session for retriieving subject
        and ontology mappings
      * ``SubjectOntologyAssignmentSession:`` a session for managing
        subject and ontology mappings
      * ``SubjectSmartOntologySession:`` a session to manage dynamic
        ontologies of subjects
    
      * ``RelevancyLookupSession:`` a session to look up subject
        relevancies
      * ``RelevancyQuerySession:`` a session to query subject
        relevancies ``None``
      * ``RelevancySearchSession:`` a session to search subject
        relevancies
      * ``RelevancyAdminSession:`` a session to create, modify and
        delete subject relevancies ``None``
      * ``RelevancyNotificationSession: a`` session to receive messages
        pertaining to subject relevancy ```` changes
      * ``RelevancyOntologySession:`` a session for retriieving
        relevancy and ontology mappings
      * ``RelevancyOntologyAssignmentSession:`` a session for managing
        relevancy and ontology mappings
      * ``RelevancySmartOntologySession:`` a session to manage dynamic
        ontologies of relevancies
    
      * ``OntologyLookupSession:`` a session to lookup ontologies
      * ``OntologyQuerySession:`` a session to search ontologies
      * ``OntologySearchSession`` : a session to search ontologies
      * ``OntologyAdminSession`` : a session to create, modify and
        delete ontologies
      * ``OntologyNotificationSession`` : a session to receive messages
        pertaining to ontology changes
      * ``OntologyHierarchySession:`` a session to traverse the ontology
        hierarchy
      * ``OntologyHierarchyDesignSession:`` a session to manage the
        ontology hierarchy


    """
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
        return # osid.ontology.SubjectLookupSession

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
        return # osid.ontology.SubjectLookupSession

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
        return # osid.ontology.SubjectLookupSession

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
        return # osid.ontology.SubjectQuerySession

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
        return # osid.ontology.SubjectQuerySession

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
        return # osid.ontology.SubjectSearchSession

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
        return # osid.ontology.SubjectSearchSession

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
        return # osid.ontology.SubjectAdminSession

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
        return # osid.ontology.SubjectAdminSession

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
        return # osid.ontology.SubjectNotificationSession

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
        return # osid.ontology.SubjectNotificationSession

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
        return # osid.ontology.SubjectHierarchySession

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
        return # osid.ontology.SubjectHierarchySession

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
        return # osid.ontology.SubjectHierarchySession

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
        return # osid.ontology.SubjectHierarchyDesignSession

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
        return # osid.ontology.SubjectHierarchyDesignSession

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
        return # osid.ontology.SubjectOntologySession

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
        return # osid.ontology.SubjectOntologyAssignmentSession

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
        return # osid.ontology.SubjectOntologySession

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
        return # osid.ontology.RelevancyLookupSession

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
        return # osid.ontology.RelevancyLookupSession

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
        return # osid.ontology.RelevancyQuerySession

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
        return # osid.ontology.RelevancyQuerySession

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
        return # osid.ontology.RelevancySearchSession

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
        return # osid.ontology.RelevancySearchSession

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
        return # osid.ontology.RelevancyAdminSession

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
        return # osid.ontology.RelevancyAdminSession

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
        return # osid.ontology.RelevancyNotificationSession

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
        return # osid.ontology.RelevancyNotificationSession

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
        return # osid.ontology.RelevancyOntologySession

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
        return # osid.ontology.RelevancyOntologyAssignmentSession

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
        return # osid.ontology.RelevancySmartOntologySession

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
        return # osid.ontology.OntologyLookupSession

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
        return # osid.ontology.OntologyQuerySession

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
        return # osid.ontology.OntologySearchSession

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
        return # osid.ontology.OntologyAdminSession

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
        return # osid.ontology.OntologyNotificationSession

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
        return # osid.ontology.OntologyHierarchySession

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
        return # osid.ontology.OntologyHierarchyDesignSession

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
        return # osid.ontology.OntologyAssignmentSession

    def get_ontology_batch_proxy_manager(self):
        """Gets the ontology batch service.

        :return: an ``OntologyBatchProxyManager``
        :rtype: ``osid.ontology.batch.OntologyBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_batch() is false``

        """
        return # osid.ontology.batch.OntologyBatchProxyManager

    ontology_batch_proxy_manager = property(fget=get_ontology_batch_proxy_manager)

    def get_ontology_rules_proxy_manager(self):
        """Gets the ontology rules service.

        :return: an ``OntologyRulesProxyManager``
        :rtype: ``osid.ontology.rules.OntologyRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_ontology_rules() is false``

        """
        return # osid.ontology.rules.OntologyRulesProxyManager

    ontology_rules_proxy_manager = property(fget=get_ontology_rules_proxy_manager)


