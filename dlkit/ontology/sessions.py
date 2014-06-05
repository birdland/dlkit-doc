from ..osid import sessions as osid_sessions


class SubjectLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Subject`` s."""
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

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
        return # boolean

    def use_comparative_subject_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_subject_view(self):
        """A complete view of the ``Subject`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_ontology_view(self):
        """Federates the view for methods in this session.

        A federated view will include subjects in ontologies which are
        children of this ontology in the ontology hierarchy.



        """
        pass

    def use_isolated_ontology_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this ontology only.



        """
        pass

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
        return # osid.ontology.Subject

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
        return # osid.ontology.SubjectList

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
        return # osid.ontology.SubjectList

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
        return # osid.ontology.SubjectList

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
        return # osid.ontology.SubjectList

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
        return # osid.ontology.SubjectList

    subjects = property(fget=get_subjects)


class SubjectQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching ``Subject`` objects.

    The search query is constructed using the ``SubjectQuery``. The
    subject record ``Type`` also specifies the record for the subject
    query.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated ontology view: searches include subjects in ontologies
        of which this ontology is a ancestor in the ontology hierarchy
      * isolated ontology view: searches are restricted to subjects in
        this ontology

    
    Subjects may have a query record indicated by their respective
    record types. The query record is accessed via the ``SubjectQuery``.

    """
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

    def use_federated_ontology_view(self):
        """Federates the view for methods in this session.

        A federated view will include subjects in ontologies which are
        children of this ontology in the ontology hierarchy.



        """
        pass

    def use_isolated_ontology_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this ontology only.



        """
        pass

    def get_subject_query(self):
        """Gets a subject query.

        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``

        """
        return # osid.ontology.SubjectQuery

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
        return # osid.ontology.SubjectList


class SubjectSearchSession(SubjectQuerySession):
    """This session provides methods for searching ``Subject`` objects.

    The search query is constructed using the ``SubjectQuery``. The
    subject record ``Type`` also specifies the record for the subject
    query.

    ``get_subjects_by_query()`` is the basic search method and returns a
    list of ``Subjects``. A more advanced search may be performed with
    ``getSubjectsBySearch()``. It accepts a ``SubjectSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_subjects_by_search()`` returns a ``SubjectSearchResults`` that
    can be used to access the resulting ``SubjectList`` or be used to
    perform a search within the result set through ``SubjectSearch``.
    
    This session defines views that offer differing behaviors for
    searching.
    
      * federated ontology view: searches include subjects in ontologies
        of which this ontology is a ancestor in the ontology hierarchy
      * isolated ontology view: searches are restricted to subjects in
        this ontology

    
    Subjects may have a query record indicated by their respective
    record types. The query record is accessed via the ``SubjectQuery``.

    """
    def get_subject_search(self):
        """Gets a subject search.

        :return: the subject search
        :rtype: ``osid.ontology.SubjectSearch``

        """
        return # osid.ontology.SubjectSearch

    subject_search = property(fget=get_subject_search)

    def get_subject_search_order(self):
        """Gets a subject search order.

        The ``SubjectSearchOrder`` is supplied to a ``SubjectSearch`` to
        specify the ordering of results.

        :return: the subject search order
        :rtype: ``osid.ontology.SubjectSearchOrder``

        """
        return # osid.ontology.SubjectSearchOrder

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
        return # osid.ontology.SubjectSearchResults

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
        return # osid.ontology.SubjectQuery


class SubjectAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Subjects``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Subject,`` a ``SubjectForm`` is requested using
    ``get_subject_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``SubjectForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``SubjectForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``SubjectForm``
    corresponds to an attempted transaction.
    
    For updates, ``SubjectForms`` are requested to the ``Subject``
    ``Id`` that is to be updated using ``getSubjectFormForUpdate()``.
    Similarly, the ``SubjectForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``SubjectForm`` can only be used once for a successful
    update and cannot be reused.
    
    The delete operations delete ``Subjects``. To unmap a ``Subject``
    from the current ``Ontology,`` the
    ``SubjectOntologyAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Subject`` itself thus removing it
    from all known ``Ontology`` catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

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
        return # boolean

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
        return # osid.ontology.SubjectForm

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
        return # osid.ontology.Subject

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
        return # boolean

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
        return # osid.ontology.SubjectForm

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
        pass

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
        return # boolean

    def delete_subject(self, subject_id):
        """Deletes the ``Subject`` identified by the given ``Id``.

        :param subject_id: the ``Id`` of the ``Subject`` to delete
        :type subject_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Subject`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        return # boolean

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
        pass


class SubjectNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive asynchronous notifications on adds/changes to ``Subject`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The views defined in this session correspond to the views in the
    ``SubjectLookupSession``.

    """
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

    def use_federated_ontology_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for subjects in
        ontologies which are children of this ontology in the ontology
        hierarchy.



        """
        pass

    def use_isolated_ontology_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this ontology only.



        """
        pass

    def register_for_new_subjects(self):
        """Register for notifications of new subjects.

        ``SubjectReceiver.newSubject()`` is invoked when a new subject
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

    def register_for_changed_subjects(self):
        """Registers for notification of updated subjects.

        ``SubjectReceiver.changedSubject()`` is invoked when a subject
        is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

    def register_for_deleted_subjects(self):
        """Registers for notification of deleted subjects.

        ``SubjectReceiver.deletedSubject()`` is invoked when a subject
        is removed from this ontology.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

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
        pass


class SubjectHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Subject`` objects.

    Each node in the hierarchy is a unique ``Subject``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``getSubjectNodes()``. To relate these ``Ids`` to another OSID,
    ``get_ancestor_subjects()`` and ``get_descendant_subjects()`` can be
    used for retrievals that can be used for bulk lookups in other
    OSIDs. Any ``Subject`` available in the Ontology OSID is known to
    this hierarchy but does not appear in the hierarchy traversal until
    added as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_subjects()`` or ``get_child_subjects()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.
    
    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: subject elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition


    """
    def get_subject_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    subject_hierarchy_id = property(fget=get_subject_hierarchy_id)

    def get_subject_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

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
        return # boolean

    def use_comparative_subject_view(self):
        """The returns from the subject methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_subject_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_root_subject_ids(self):
        """Gets the root subject ``Ids`` in this hierarchy.

        :return: the root subject ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    root_subject_ids = property(fget=get_root_subject_ids)

    def get_root_subjects(self):
        """Gets the root subjects in this subject hierarchy.

        :return: the root subjects
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.SubjectList

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.ontology.SubjectList

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
        return # boolean

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.ontology.SubjectList

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
        return # boolean

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
        return # osid.hierarchy.Node

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
        return # osid.ontology.SubjectNode


class SubjectHierarchyDesignSession(osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Subject`` objects.

    Each node in the hierarchy is a unique ``Subject``.

    """
    def get_subject_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    subject_hierarchy_id = property(fget=get_subject_hierarchy_id)

    def get_subject_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    subject_hierarchy = property(fget=get_subject_hierarchy)

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
        return # boolean

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
        pass

    def remove_root_subject(self, subject_id):
        """Removes a root subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``subject_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- the root subjects
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

    def remove_child_subjects(self, subject_id):
        """Removes all children from a subject.

        :param subject_id: the ``Id`` of a subject
        :type subject_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``subject_id`` not found
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class SubjectOntologySession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Subject`` to ``Ontology`` mappings.

    A ``Subject`` may appear in multiple ``Ontologies``. Each
    ``Ontology`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
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
        return # boolean

    def use_comparative_ontology_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_ontology_view(self):
        """A complete view of the ``Subject`` and ``Ontology`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

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
        return # osid.id.IdList

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
        return # osid.ontology.SubjectList

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
        return # osid.id.IdList

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
        return # osid.ontology.SubjectList

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
        return # osid.id.IdList

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
        return # osid.ontology.OntologyList


class SubjectOntologyAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Subjects`` to ``Ontologies``.

    A ``Subject`` may map to multiple ``Ontologies`` and removing the
    last reference to a ``Subject`` is the equivalent of deleting it.
    Each ``Ontology`` may have its own authorizations governing who is
    allowed to operate on it.

    Adding a reference of a ``Subject`` to another ``Ontology`` is not a
    copy operation (eg: does not change its ``Id`` ).

    """
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
        return # boolean

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
        return # boolean

    def get_assignable_ontology_ids(self, ontology_id):
        """Gets a list of ontologies including and under the given ontology node in which any subject can be assigned.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: list of assignable ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

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
        return # osid.id.IdList

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
        pass

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
        pass


class SubjectSmartOntologySession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``SubjectQuery`` can be retrieved from this session and mapped to
    this ``Ontology`` to create a virtual collection of ``Subjects``.
    The entries may be sequenced using the ``SubjectSearchOrder`` from
    this session.

    This ``Ontology`` has a default query that matches any subject and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``SubjectQueryInspector``. The query may be
    modified by converting the inspector back to a ``SubjectQuery``.

    """
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

    def get_subject_query(self):
        """Gets a subject query.

        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``

        """
        return # osid.ontology.SubjectQuery

    subject_query = property(fget=get_subject_query)

    def get_subject_search_order(self):
        """Gets a subject search order.

        :return: the subject search order
        :rtype: ``osid.ontology.SubjectSearchOrder``

        """
        return # osid.ontology.SubjectSearchOrder

    subject_search_order = property(fget=get_subject_search_order)

    def apply_subject_query(self, subject_query):
        """Applies a subject query to this ontology.

        :param subject_query: the subject query
        :type subject_query: ``osid.ontology.SubjectQuery``
        :raise: ``NullArgument`` -- ``subject_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``subject_query`` not of this service

        """
        pass

    def inspect_subject_query(self):
        """Gets a subject query inspector for this ontology.

        :return: the subject query inspector
        :rtype: ``osid.ontology.SubjectQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.ontology.SubjectQueryInspector

    def apply_subject_sequencing(self, subject_search_order):
        """Applies a subject search order to this ontology.

        :param subject_search_order: the subject search order
        :type subject_search_order: ``osid.ontology.SubjectSearchOrder``
        :raise: ``NullArgument`` -- ``subject_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``subject_search_order`` not of this service

        """
        pass

    def get_subject_query_from_inspector(self, subject_query_inspector):
        """Gets a subject query from an inspector.

        :param subject_query_inspector: a subject query inspector
        :type subject_query_inspector: ``osid.ontology.SubjectQueryInspector``
        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``
        :raise: ``NullArgument`` -- ``subject_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``subject_query_inspector`` is not of this service

        """
        return # osid.ontology.SubjectQuery


class RelevancyLookupSession(osid_sessions.OsidSession):
    """This session provides methods for examining subject relevancy."""
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

    def use_comparative_relevancy_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_relevancy_view(self):
        """A complete view of the ``Relevancy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_ontology_view(self):
        """Federates the view for methods in this session.

        A federated view will include relevancies in ontologies which
        are children of this ontology in the ontology hierarchy.



        """
        pass

    def use_isolated_ontology_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this ontology only.



        """
        pass

    def use_effective_relevancy_view(self):
        """The returns from the lookup methods return only effetive relevancies."""
        pass

    def use_any_effective_relevancy_view(self):
        """Both effective and ineffective relavcnies are returned."""
        pass

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
        return # osid.ontology.Relevancy

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
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

    def get_relevancies_by_genus_type_on_date(self, relevancy_genus_type, from_, to):
        """Gets a ``RelevancyList`` of the given genus type and effective during the entire given date range inclusive but not confined to the date range.

        :param relevancy_genus_type: relevancy genus type
        :type relevancy_genus_type: ``osid.type.Type``
        :param from: a starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: an ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``relevancy_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        :raise: ``NullArgument`` -- ``subject_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        :raise: ``NullArgument`` -- ``subject_id, relevancy_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        :raise: ``NullArgument`` -- ``id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        :raise: ``NullArgument`` -- ``id, relevancy_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        :raise: ``NullArgument`` -- ``subject_id, id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.RelevancyList

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
        return # osid.ontology.RelevancyList

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
        :raise: ``NullArgument`` -- ``subject_id, id, relevancy_genus_t_ype, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.RelevancyList

    def get_relevancies(self):
        """Gets all relevancies.

        :return: list of relevancies
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.RelevancyList

    relevancies = property(fget=get_relevancies)


class RelevancyQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching ``Relevancy`` objects.

    The search query is constructed using the ``RelevancyQuery``. The
    relevancy record ``Type`` also specifies the record for the
    relevancy query.

    This session defines views that offer differing behaviors for
    searching.
    
      * federated ontology view: searches include relevancies in
        ontologies of which this ontology is a ancestor in the ontology
        hierarchy
      * isolated ontology view: searches are restricted

    
    Relevancies may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RelevancyQuery``.

    """
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

    def use_federated_ontology_view(self):
        """Federates the view for methods in this session.

        A federated view will include relevancies in ontologies which
        are children of this ontology in the ontology hierarchy.



        """
        pass

    def use_isolated_ontology_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts searches to this ontology only.



        """
        pass

    def get_relevancy_query(self):
        """Gets a relevancy query.

        :return: the relevancy query
        :rtype: ``osid.ontology.RelevancyQuery``

        """
        return # osid.ontology.RelevancyQuery

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
        return # osid.ontology.RelevancyList


class RelevancySearchSession(RelevancyQuerySession):
    """This session provides methods for searching ``Relevancy`` objects.

    The search query is constructed using the ``RelevancyQuery``. The
    relevancy record ``Type`` also specifies the record for the
    relevancy query.

    ``get_relevancies_by_query()`` is the basic search method and
    returns a list of relevancies. A more advanced search may be
    performed with ``getRelevanciesBySearch()``. It accepts a
    ``RelevancySearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_relevancies_by_search()`` returns a
    ``RelevancySearchResults`` that can be used to access the resulting
    ``RelevancyList`` or be used to perform a search within the result
    set through ``RelevancySearch``.
    
    This session defines views that offer differing behaviors for
    searching.
    
      * federated ontology view: searches include relevancies in
        ontologies of which this ontology is a ancestor in the ontology
        hierarchy
      * isolated ontology view: searches are restricted

    
    Relevancies may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RelevancyQuery``.

    """
    def get_relevancy_search(self):
        """Gets a relevancy search.

        :return: the relevancy search
        :rtype: ``osid.ontology.RelevancySearch``

        """
        return # osid.ontology.RelevancySearch

    relevancy_search = property(fget=get_relevancy_search)

    def get_relevancy_search_order(self):
        """Gets a relevancy search order.

        The ``RelevancySearchOrder`` is supplied to a
        ``RelevancySearch`` to specify the ordering of results.

        :return: the relevancy search order
        :rtype: ``osid.ontology.RelevancySearchOrder``

        """
        return # osid.ontology.RelevancySearchOrder

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
        return # osid.ontology.RelevancySearchResults

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
        return # osid.ontology.RelevancyQuery


class RelevancyAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Relevancies``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Relevancy,`` a ``RelevancyForm`` is requested using
    ``get_relevancy_form_for_create()`` specifying the desired peers and
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``RelevancyForm`` will indicate that it is to be used with
    a create operation and can be used to examine metdata or validate
    data prior to creation. Once the ``RelevancyForm`` is submiited to a
    create operation, it cannot be reused with another create operation
    unless the first operation was unsuccessful. Each ``RelevancyForm``
    corresponds to an attempted transaction.
    
    For updates, ``RelevancyForms`` are requested to the ``Relevancy``
    ``Id`` that is to be updated using ``getRelevancyFormForUpdate()``.
    Similarly, the ``RelevancyForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``RelevancyForm`` can only be used once for a successful
    update and cannot be reused.
    
    The delete operations delete ``Relevancies``. To unmap a
    ``Relevancy`` from the current ``Ontology,`` the
    ``RelevancyOntologyAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Relevancy`` itself thus removing
    it from all known ``Ontology`` catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

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
        return # boolean

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
        return # osid.ontology.RelevancyForm

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
        return # osid.ontology.Relevancy

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
        return # boolean

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
        return # osid.ontology.RelevancyForm

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
        pass

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
        return # boolean

    def delete_relevancy(self, relevancy_id):
        """Deletes the ``Relevancy`` identified by the given ``Id``.

        :param relevancy_id: the ``Id`` of the ``Relevancy`` to delete
        :type relevancy_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Relevancy`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``relevancy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        return # boolean

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
        pass


class RelevancyNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive asynchronous notifications on adds/changes to subject relevancies.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    The views defined in this session correspond to the views in the
    ``RelevancyLookupSession``.

    """
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

    def use_federated_ontology_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for relevancies in
        ontologies which are children of this ontology in the ontology
        hierarchy.



        """
        pass

    def use_isolated_ontology_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this ontology only.



        """
        pass

    def register_for_new_relevancies(self):
        """Register for notifications of new relevancies.

        ``RelevancyReceiver.newRelevancy()`` is invoked when a new
        relevancy is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

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
        pass

    def register_for_changed_relevancies(self):
        """Registers for notification of updated relevancies.

        ``RelevancyReceiver.changedRelevancy()`` is invoked when a
        relevancy is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

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
        pass

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
        pass

    def register_for_deleted_relevancies(self):
        """Registers for notification of deleted relevancies.

        ``RelevancyReceiver.deletedRelevancy()`` is invoked when a
        relevancy is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

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
        pass

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
        pass


class RelevancyOntologySession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Relevancy`` to ``Ontology`` mappings.

    A ``Relevancy`` may appear in multiple ``Ontologies``. Each
    ``Ontology`` may have its own authorizations governing who is
    allowed to look at it.

    This lookup session defines two views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
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
        return # boolean

    def use_comparative_ontology_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_ontology_view(self):
        """A complete view of the ``Relevancy`` and ``Ontology`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

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
        return # osid.id.IdList

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
        return # osid.ontology.RelevancyList

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
        return # osid.id.IdList

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
        return # osid.ontology.RelevancyList

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
        return # osid.id.IdList

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
        return # osid.ontology.OntologyList


class RelevancyOntologyAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Relevancies`` to ``Ontologies``.

    A ``Relevancy`` may map to multiple ``Ontologies`` and removing the
    last reference to a ``Relevancy`` is the equivalent of deleting it.
    Each ``Ontology`` may have its own authorizations governing who is
    allowed to operate on it.

    Adding a reference of a ``Relevancy`` to another ``Ontology`` is not
    a copy operation (eg: does not change its ``Id`` ).

    """
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
        return # boolean

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
        return # boolean

    def get_assignable_ontology_ids(self, ontology_id):
        """Gets a list of ontologies including and under the given ontology node in which any relevancy can be assigned.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :return: list of assignable ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

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
        return # osid.id.IdList

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
        pass

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
        pass


class RelevancySmartOntologySession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``RelevancyQuery`` can be retrieved from this session and mapped
    to this ``Ontology`` to create a virtual collection of
    ``Relevancies``. The entries may be sequenced using the
    ``RelevancySearchOrder`` from this session.

    This ``Ontology`` has a default query that matches any relevancy and
    a default search order that specifies no sequencing. The queries may
    be examined using a ``RelevancyQueryInspector``. The query may be
    modified by converting the inspector back to a ``RelevancyQuery``.

    """
    def get_ontology_id(self):
        """Gets the ``Ontology``  ``Id`` associated with this session.

        :return: the ``Ontology Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_id = property(fget=get_ontology_id)

    def get_ontology(self):
        """Gets the ``Ontology`` associated with this session.

        :return: the ``Ontology`` associated with this session
        :rtype: ``osid.ontology.Ontology``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

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
        return # boolean

    def get_relevancy_query(self):
        """Gets a relevancy query.

        :return: the relevancy query
        :rtype: ``osid.ontology.RelevancyQuery``

        """
        return # osid.ontology.RelevancyQuery

    relevancy_query = property(fget=get_relevancy_query)

    def get_relevancy_search_order(self):
        """Gets a relevancy search order.

        :return: the relevancy search order
        :rtype: ``osid.ontology.RelevancySearchOrder``

        """
        return # osid.ontology.RelevancySearchOrder

    relevancy_search_order = property(fget=get_relevancy_search_order)

    def apply_relevancy_query(self, relevancy_query):
        """Applies a relevancy query to this ontology.

        :param relevancy_query: the relevancy query
        :type relevancy_query: ``osid.ontology.RelevancyQuery``
        :raise: ``NullArgument`` -- ``relevancy_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``relevancy_query`` not of this service

        """
        pass

    def inspect_relevancy_query(self):
        """Gets a relevancy query inspector for this ontology.

        :return: the relevancy query inspector
        :rtype: ``osid.ontology.RelevancyQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.ontology.RelevancyQueryInspector

    def apply_relevancy_sequencing(self, relevancy_search_order):
        """Applies a relevancy search order to this ontology.

        :param relevancy_search_order: the relevancy search order
        :type relevancy_search_order: ``osid.ontology.RelevancySearchOrder``
        :raise: ``NullArgument`` -- ``relevancy_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``relevancy_search_order`` not of this service

        """
        pass

    def get_relevancy_query_from_inspector(self, relevancy_query_inspector):
        """Gets a relevancy query from an inspector.

        :param relevancy_query_inspector: a relevancy query inspector
        :type relevancy_query_inspector: ``osid.ontology.RelevancyQueryInspector``
        :return: the relevancy query
        :rtype: ``osid.ontology.RelevancyQuery``
        :raise: ``NullArgument`` -- ``relevancy_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``relevancy_query_inspector`` is not of this service

        """
        return # osid.ontology.RelevancyQuery


class OntologyLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Ontology`` objects.

    The ``Ontology`` represents a collection of ``Subjects``.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Ontologies`` it can access, without breaking
    execution. However, an administrative application may require all
    ``Ontology`` elements to be available.
    
    Ontologies may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Ontology``.

    """
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
        return # boolean

    def use_comparative_ontology_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_ontology_view(self):
        """A complete view of the ``Ontology`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

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
        return # osid.ontology.Ontology

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
        return # osid.ontology.OntologyList

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
        return # osid.ontology.OntologyList

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
        return # osid.ontology.OntologyList

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
        return # osid.ontology.OntologyList

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
        return # osid.ontology.OntologyList

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
        return # osid.ontology.OntologyList

    ontologies = property(fget=get_ontologies)


class OntologyQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Ontology`` objects.

    The search query is constructed using the ``OntologyQuery``.

    Ontologies may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``OntologyQuery``.

    """
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
        return # boolean

    def get_ontology_query(self):
        """Gets an ontology query.

        :return: an ontology query
        :rtype: ``osid.ontology.OntologyQuery``

        """
        return # osid.ontology.OntologyQuery

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
        return # osid.ontology.OntologyList


class OntologySearchSession(OntologyQuerySession):
    """This session provides methods for searching among ``Ontology`` objects.

    The search query is constructed using the ``OntologyQuery``.

    ``get_ontologies_by_query()`` is the basic search method and returns
    a list of ``Ontology`` objects.A more advanced search may be
    performed with ``getOntologiesBySearch()``. It accepts an
    ``OntologySearch`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_ontologies_by_search()`` returns an
    ``OntologySearchResults`` that can be used to access the resulting
    ``OntologyList`` or be used to perform a search within the result
    set through ``OntologySearch``.
    
    Ontologies may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``OntologyQuery``.

    """
    def get_ontology_search(self):
        """Gets an ontology search.

        :return: an ontology search
        :rtype: ``osid.ontology.OntologySearch``

        """
        return # osid.ontology.OntologySearch

    ontology_search = property(fget=get_ontology_search)

    def get_ontology_search_order(self):
        """Gets an ontology search order.

        The ``OntologySearchOrder`` is supplied to an ``OntologySearch``
        to specify the ordering of results.

        :return: the ontology search order
        :rtype: ``osid.ontology.OntologySearchOrder``

        """
        return # osid.ontology.OntologySearchOrder

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
        return # osid.ontology.OntologySearchResults

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
        return # osid.ontology.OntologyQuery


class OntologyAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Ontologies``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Ontology,`` an ``OntologyForm`` is requested using
    ``get_ontology_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``OntologyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``OntologyForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``OntologyForm``
    corresponds to an attempted transaction.
    
    For updates, ``OntologyForms`` are requested to the ``Ontology``
    ``Id`` that is to be updated using ``getOntologyFormForUpdate()``.
    Similarly, the ``OntologyForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``OntologyForm`` can only be used once for a successful
    update and cannot be reused.
    
    The delete operations delete ``Ontologies``.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
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
        return # boolean

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
        return # boolean

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
        return # osid.ontology.OntologyForm

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
        return # osid.ontology.OntologyForm

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
        return # boolean

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
        return # osid.ontology.OntologyForm

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
        pass

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
        return # boolean

    def delete_ontology(self, ontology_id):
        """Deletes an ``Ontology``.

        :param ontology_id: the ``Id`` of the ``Ontology`` to remove
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        return # boolean

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
        pass


class OntologyNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Ontology`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session i

    """
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
        return # boolean

    def register_for_new_ontologies(self):
        """Register for notifications of new ontologies.

        ``OntologyReceiver.newOntology()`` is invoked when a new
        ``Ontology`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

    def register_for_changed_ontologies(self):
        """Registers for notification of updated ontologies.

        ``OntologyReceiver.changedOntology()`` is invoked when an
        ontology is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

    def register_for_deleted_ontologies(self):
        """Registers for notification of deleted ontologies.

        ``OntologyReceiver.deletedOntology()`` is invoked when a
        calenedar is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

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
        pass


class OntologyHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Ontology`` objects.

    Each node in the hierarchy is a unique ``Ontology``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parent_ontologies()`` and ``getChildOntologies()``. To relate
    these ``Ids`` to another OSID, ``get_ontology_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Ontology`` available in the Ontology OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_ontologies()`` or ``get_child_ontologies()``
    in lieu of a ``PermissionDenied`` error that may disrupt the
    traversal through authorized pathways.
    
    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: ontology elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition


    """
    def get_ontology_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_hierarchy_id = property(fget=get_ontology_hierarchy_id)

    def get_ontology_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

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
        return # boolean

    def use_comparative_ontology_view(self):
        """The returns from the ontology methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_ontology_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_root_ontology_ids(self):
        """Gets the root ontology ``Ids`` in this hierarchy.

        :return: the root ontology ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    root_ontology_ids = property(fget=get_root_ontology_ids)

    def get_root_ontologies(self):
        """Gets the root ontologies in this ontology hierarchy.

        :return: the root ontologies
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.ontology.OntologyList

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.ontology.OntologyList

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
        return # boolean

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.ontology.OntologyList

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
        return # boolean

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
        return # osid.hierarchy.Node

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
        return # osid.ontology.OntologyNode


class OntologyHierarchyDesignSession(osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Ontology`` objects.

    Each node in the hierarchy is a unique ``Ontology``.

    """
    def get_ontology_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    ontology_hierarchy_id = property(fget=get_ontology_hierarchy_id)

    def get_ontology_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    ontology_hierarchy = property(fget=get_ontology_hierarchy)

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
        return # boolean

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
        pass

    def remove_root_ontology(self, ontology_id):
        """Removes a root ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` is not a root
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

    def remove_child_ontologies(self, ontology_id):
        """Removes all children from an ontology.

        :param ontology_id: the ``Id`` of an ontology
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class OntologyAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to manage ``Id`` to ``Ontology`` mappings.

    Arbitrary ``Ids`` may be used to offer a restricted ontology to
    allow an arbitrary ``Id`` to be used in the ``SubjectLookupSession``
    or the ``SubjectHierarchySession``. Only one ontology can be
    assigned to an ``Id``.

    """
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
        return # boolean

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
        pass

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
        pass

    def get_ontology(self, id_):
        """Gets the ontology to which the ``Id`` is assigned.

        :param id: ``an _id``
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def get_ids(self, ontology_id):
        """Gets a list of the ``Ids`` assigned to an ontology.

        :param ontology_id: ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``ontology_id`` not found
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


