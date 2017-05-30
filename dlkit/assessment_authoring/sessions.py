
from ..osid import sessions as osid_sessions


class AssessmentPartLookupSession(osid_sessions.OsidSession):
    """This session defines methods for retrieving assessment parts."""

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    bank = property(fget=get_bank)

    def can_lookup_assessment_parts(self):
        """Tests if this user can perform ``AssessmentPart`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_assessment_part_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_assessment_part_view(self):
        """A complete view of the ``AssessmentPart`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment parts in catalogs which
        are children of this catalog in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_active_assessment_part_view(self):
        """Only active assessment parts are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_any_status_assessment_part_view(self):
        """All active and inactive assessment parts are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_sequestered_assessment_part_view(self):
        """The methods in this session omit sequestered assessment parts.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_unsequestered_assessment_part_view(self):
        """The methods in this session return all assessment parts, including sequestered assessment parts.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_assessment_part(self, assessment_part_id):
        """Gets the ``AssessmentPart`` specified by its ``Id``.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart`` to retrieve
        :type assessment_part_id: ``osid.id.Id``
        :return: the returned ``AssessmentPart``
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``NotFound`` -- no ``AssessmentPart`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPart

    def get_assessment_parts_by_ids(self, assessment_part_ids):
        """Gets an ``AssessmentPartList`` corresponding to the given ``IdList``.

        :param assessment_part_ids: the list of ``Ids`` to retrieve
        :type assessment_part_ids: ``osid.id.IdList``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``assessment_part_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartList

    def get_assessment_parts_by_genus_type(self, assessment_part_genus_type):
        """Gets an ``AssessmentPartList`` corresponding to the given assessment part genus ``Type`` which does not include assessment parts of types derived from the specified ``Type``.

        :param assessment_part_genus_type: an assessment part genus type
        :type assessment_part_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_part_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartList

    def get_assessment_parts_by_parent_genus_type(self, assessment_genus_type):
        """Gets an ``AssessmentPartList`` corresponding to the given assessment part genus ``Type`` and include any additional assessment parts with genus types derived from the specified ``Type``.

        :param assessment_genus_type: an assessment part genus type
        :type assessment_genus_type: ``osid.type.Type``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_part_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartList

    def get_assessment_parts_by_record_type(self, assessment_part_record_type):
        """Gets an ``AssessmentPart`` containing the given assessment part record ``Type``.

        :param assessment_part_record_type: an assessment part record type
        :type assessment_part_record_type: ``osid.type.Type``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_part_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartList

    def get_assessment_parts_for_assessment(self, assessment_id):
        """Gets an ``AssessmentPart`` for the given assessment.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``AssessmentPart`` list
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartList

    def get_assessment_parts(self):
        """Gets all ``AssessmentParts``.

        :return: a list of ``AssessmentParts``
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartList

    assessment_parts = property(fget=get_assessment_parts)


class AssessmentPartQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``AssessmentPart`` objects.

    The search query is constructed using the ``AssessmentPartQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bank view: searches include assessment parts in bank
        of which this bank is an ancestor in the bank hierarchy
      * isolated bank view: searches are restricted to assessment parts
        in this bank
      * sequestered assessment part viiew: All assessment part methods
        suppress sequestered assessment parts.
      * unsequestered assessment part view: All assessment part methods
        return all assessment parts.


    Assessment parts may have a query record indicated by their
    respective record types. The query record is accessed via the
    ``AssessmentPartQuery``.

    """

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    bank = property(fget=get_bank)

    def can_search_assessment_parts(self):
        """Tests if this user can perform ``AssessmentPart`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment part in banks which are
        children of this step in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_sequestered_assessment_part_view(self):
        """The methods in this session omit sequestered assessment parts.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_unsequestered_assessment_part_view(self):
        """The methods in this session return all assessment parts, including sequestered assessment parts.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_assessment_part_query(self):
        """Gets an assessment part query.

        :return: the assessment part query
        :rtype: ``osid.assessment.authoring.AssessmentPartQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartQuery

    assessment_part_query = property(fget=get_assessment_part_query)

    def get_assessment_parts_by_query(self, assessment_part_query):
        """Gets a list of ``AssessmentParts`` matching the given assessment part query.

        :param assessment_part_query: the assessment part query
        :type assessment_part_query: ``osid.assessment.authoring.AssessmentPartQuery``
        :return: the returned ``AssessmentPartList``
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NullArgument`` -- ``assessment_part_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``assessment_part_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartList


class AssessmentPartAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``AssessmentParts``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``AssessmentPart,`` an ``AssessmentPartForm`` is requested using
    ``get_assessment_part_form_for_create()`` specifying the desired
    record ``Types`` or none if no record ``Types`` are needed. The
    returned ``AssessmentPartForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``AssessmentPartForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``AssessmentPartForm`` corresponds to an attempted transaction.

    For updates, ``AssessmentPartForms`` are requested to the
    ``AssessmentPart``  ``Id`` that is to be updated using
    ``getAssessmentPartFormForUpdate()``. Similarly, the
    ``AssessmentPartForm`` has metadata about the data that can be
    updated and it can perform validation before submitting the update.
    The ``AssessmentPartForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``AssessmentParts``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    bank = property(fget=get_bank)

    def can_create_assessment_parts(self):
        """Tests if this user can create assessment parts.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to unauthorized users.

        :return: ``false`` if ``AssessmentPart`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_assessment_part_with_record_types(self, assessment_part_record_types):
        """Tests if this user can create a single ``AssessmentPart`` using the desired record types.

        While
        ``AssessmentAuthoringManager.getAssessmentPartRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``AssessmentPart``. Providing an empty array tests if an
        ``AssessmentPart`` can be created with no records.

        :param assessment_part_record_types: array of assessment part record types
        :type assessment_part_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssessmentPart`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``assessment_part_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assessment_part_form_for_create_for_assessment(self, assessment_id, assessment_part_record_types):
        """Gets the assessment part form for creating new assessment parts for an assessment.

        A new form should be requested for each create transaction.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :param assessment_part_record_types: array of assessment part record types to be included in the create operation or an empty list if none
        :type assessment_part_record_types: ``osid.type.Type[]``
        :return: the assessment part form
        :rtype: ``osid.assessment.authoring.AssessmentPartForm``
        :raise: ``NotFound`` -- ``assessment_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_id`` or ``assessment_part_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartForm

    def create_assessment_part_for_assessment(self, assessment_part_form):
        """Creates a new assessment part.

        :param assessment_part_form: assessment part form
        :type assessment_part_form: ``osid.assessment.authoring.AssessmentPartForm``
        :return: the new part
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``IllegalState`` -- ``assessment_part_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- ``assessment_part_form`` is invalid
        :raise: ``NullArgument`` -- ``assessment_part_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_part_form`` did not originate from ``get_assessment_part_form_for_create_for_assessment()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPart

    def get_assessment_part_form_for_create_for_assessment_part(self, assessment_part_id, assessment_part_record_types):
        """Gets the assessment part form for creating new assessment parts under another assessment part.

        A new form should be requested for each create transaction.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param assessment_part_record_types: array of assessment part record types to be included in the create operation or an empty list if none
        :type assessment_part_record_types: ``osid.type.Type[]``
        :return: the assessment part form
        :rtype: ``osid.assessment.authoring.AssessmentPartForm``
        :raise: ``NotFound`` -- ``assessment_part_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` or ``assessment_part_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartForm

    def create_assessment_part_for_assessment_part(self, assessment_part_form):
        """Creates a new assessment part.

        :param assessment_part_form: assessment part form
        :type assessment_part_form: ``osid.assessment.authoring.AssessmentPartForm``
        :return: the new part
        :rtype: ``osid.assessment.authoring.AssessmentPart``
        :raise: ``IllegalState`` -- ``assessment_part_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- ``assessment_part_form`` is invalid
        :raise: ``NullArgument`` -- ``assessment_part_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_part_form`` did not originate from ``get_assessment_part_form_for_create_for_assessment_part()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPart

    def can_update_assessment_parts(self):
        """Tests if this user can update ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssessmentPart`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if assessment part modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assessment_part_form_for_update(self, assessment_part_id):
        """Gets the assessment part form for updating an existing assessment part.

        A new assessment part form should be requested for each update
        transaction.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :return: the assessment part form
        :rtype: ``osid.assessment.authoring.AssessmentPartForm``
        :raise: ``NotFound`` -- ``assessment_part_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartForm

    def update_assessment_part(self, assessment_part_id, assessment_part_form):
        """Updates an existing assessment part.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param assessment_part_form: part form
        :type assessment_part_form: ``osid.assessment.authoring.AssessmentPartForm``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``assessment_part_form`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_assessment_parts(self):
        """Tests if this user can delete ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssessmentPart`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``AssessmentPart`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_assessment_part(self, assessment_part_id):
        """Removes an asessment part and all mapped items.

        :param assessment_part_id: the ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_assessment_part_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``AssessmentPart`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_assessment_part(self, assessment_part_id, alias_id):
        """Adds an ``Id`` to an ``AssessmentPart`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``AssessmentPart`` is determined by
        the provider. The new ``Id`` is an alias to the primary ``Id``.
        If the alias is a pointer to another assessment part, it is
        reassigned to the given assessment part ``Id``.

        :param assessment_part_id: the ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class AssessmentPartItemSession(osid_sessions.OsidSession):
    """This session defines methods for looking up ``Item`` to ``AssessmentPart`` mappings."""

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    bank = property(fget=get_bank)

    def can_access_assessment_part_items(self):
        """Tests if this user can perform assessment part lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_asseessment_part_item_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_assessment_part_item_view(self):
        """A complete view of the returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include assessment parts in catalogs which
        are children of this catalog in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_assessment_part_items(self, assessment_part_id):
        """Gets the list of items mapped to the given ``AssessmentPart``.

        In plenary mode, the returned list contains all known items or
        an error results. Otherwise, the returned list may contain only
        those items that are accessible through this session.

        :param assessment_part_id: ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :return: list of items
        :rtype: ``osid.assessment.ItemList``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.assessment.ItemList

    def get_assessment_parts_by_item(self, item_id):
        """Gets the assessment parts containing the given item.

        In plenary mode, the returned list contains all known assessment
        parts or an error results. Otherwise, the returned list may
        contain only those assessment parts that are accessible through
        this session.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :return: the returned ``AssessmentPart list``
        :rtype: ``osid.assessment.authoring.AssessmentPartList``
        :raise: ``NotFound`` -- ``item_id`` is not found
        :raise: ``NullArgument`` -- ``item_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.AssessmentPartList


class AssessmentPartItemDesignSession(osid_sessions.OsidSession):
    """This session provides the means for adding items to an assessment part.

    The item is identified inside an assesment part using its own Id. To
    add the same item to the assessment part, multiple assessment parts
    should be used and placed at the same level in the
    ``AssessmentPart`` hierarchy.

    """

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the ``Bank`` associated with this session
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    bank = property(fget=get_bank)

    def can_design_assessment_parts(self):
        """Tests if this user can manage mapping of ``Items`` to ``AssessmentParts``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as an application hint that may opt not to offer composition
        operations.

        :return: ``false`` if assessment part composition is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def add_item(self, item_id, assessment_part_id):
        """Appends an item to an assessment part.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param assessment_part_id: ``Id`` of the ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``item_id`` already part of ``assessment_part_id``
        :raise: ``NotFound`` -- ``item_id`` or ``assessment_part_id`` not found
        :raise: ``NullArgument`` -- ``item_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def move_item_ahead(self, item_id, assessment_part_id, reference_id):
        """Reorders items in an assessment part by moving the specified item in front of a reference item.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param assessment_part_id: ``Id`` of the ``AssessmentPartId``
        :type assessment_part_id: ``osid.id.Id``
        :param reference_id: ``Id`` of the reference ``Item``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id`` or ``reference_id``  ``not found in assessment_part_id``
        :raise: ``NullArgument`` -- ``item_id, reference_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def move_item_behind(self, item_id, assessment_part_id, reference_id):
        """Reorders items in an assessment part by moving the specified item behind of a reference item.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param assessment_part_id: ``Id of the AssessmentPartId``
        :type assessment_part_id: ``osid.id.Id``
        :param reference_id: ``Id`` of the reference ``Item``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id`` or ``reference_id``  ``not found in assessment_part_id``
        :raise: ``NullArgument`` -- ``item_id, reference_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_items(self, item_ids, assessment_part_id):
        """Reorders a set of items in an assessment part.

        :param item_ids: ``Ids`` for a set of ``Items``
        :type item_ids: ``osid.id.Id[]``
        :param assessment_part_id: ``Id`` of the ``AssessmentPartId``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found or, an ``item_id`` not related to ``assessment_part_id``
        :raise: ``NullArgument`` -- ``item_ids`` or ``agenda_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_item(self, item_id, assessment_part_id):
        """Removes an ``Item`` from an ``AssessmentPartId``.

        :param item_id: ``Id`` of the ``Item``
        :type item_id: ``osid.id.Id``
        :param assessment_part_id: ``Id`` of the ``AssessmentPartId``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``item_id``  ``not found in assessment_part_id``
        :raise: ``NullArgument`` -- ``item_id`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class SequenceRuleLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``SequenceRules``."""

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    bank = property(fget=get_bank)

    def can_lookup_sequence_rules(self):
        """Tests if this user can perform ``SequenceRules`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_sequence_rule_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_sequence_rule_view(self):
        """A complete view of the ``SequenceRule`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_bank_view(self):
        """Federates the view for methods in this session.

        A federated view will include sequence rule in banks which are
        children of this bank in the bank hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_bank_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bank only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_active_sequence_rule_view(self):
        """Only active sequence rules are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_any_status_sequence_rule_view(self):
        """All active and inactive sequence rules are returned by methods in this session.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_sequence_rule(self, sequence_rule_id):
        """Gets the ``SequenceRule`` specified by its ``Id``.

        :param sequence_rule_id: ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :return: the sequence rule
        :rtype: ``osid.assessment.authoring.SequenceRule``
        :raise: ``NotFound`` -- ``sequence_rule_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRule

    def get_sequence_rules_by_ids(self, sequence_rule_ids):
        """Gets a ``SequenceRuleList`` corresponding to the given ``IdList``.

        :param sequence_rule_ids: the list of ``Ids`` to retrieve
        :type sequence_rule_ids: ``osid.id.IdList``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NotFound`` -- a ``Id was`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    def get_sequence_rules_by_genus_type(self, sequence_rule_genus_type):
        """Gets a ``SequenceRuleList`` corresponding to the given sequence rule genus ``Type`` which does not include sequence rule of genus types derived from the specified ``Type``.

        :param sequence_rule_genus_type: a sequence rule genus type
        :type sequence_rule_genus_type: ``osid.type.Type``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``sequence_rule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    def get_sequence_rules_by_parent_genus_type(self, sequence_rule_genus_type):
        """Gets a ``SequenceRuleList`` corresponding to the given sequence rule genus ``Type`` and include any additional sequence rule with genus types derived from the specified ``Type``.

        :param sequence_rule_genus_type: a sequence rule genus type
        :type sequence_rule_genus_type: ``osid.type.Type``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``sequence_rule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    def get_sequence_rules_by_record_type(self, sequence_rule_record_type):
        """Gets a ``SequenceRuleList`` containing the given sequence rule record ``Type``.

        :param sequence_rule_record_type: a sequence rule record type
        :type sequence_rule_record_type: ``osid.type.Type``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``sequence_rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    def get_sequence_rules_for_assessment_part(self, assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given source assessment part.

        :param assessment_part_id: an assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    def get_sequence_rules_for_next_assessment_part(self, next_assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given target assessment part.

        :param next_assessment_part_id: an assessment part ``Id``
        :type next_assessment_part_id: ``osid.id.Id``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``next_assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    def get_sequence_rules_for_assessment_parts(self, assessment_part_id, next_assessment_part_id):
        """Gets a ``SequenceRuleList`` for the given source and target assessment parts.

        :param assessment_part_id: source assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param next_assessment_part_id: target assessment part ``Id``
        :type next_assessment_part_id: ``osid.id.Id``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``assessment_part_id`` or ``next_assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    def get_sequence_rules_for_assessment(self, assessment_id):
        """Gets a ``SequenceRuleList`` for an entire assessment.

        :param assessment_id: an assessment ``Id``
        :type assessment_id: ``osid.id.Id``
        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``NullArgument`` -- ``assessment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    def get_sequence_rules(self):
        """Gets all ``SequenceRules``.

        :return: the returned ``SequenceRule`` list
        :rtype: ``osid.assessment.authoring.SequenceRuleList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleList

    sequence_rules = property(fget=get_sequence_rules)


class SequenceRuleAdminSession(osid_sessions.OsidSession):
    """This session creates and removes sequence rules.

    The data for create and update is provided via the
    ``SequenceRuleForm``.

    """

    def get_bank_id(self):
        """Gets the ``Bank``  ``Id`` associated with this session.

        :return: the ``Bank Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bank_id = property(fget=get_bank_id)

    def get_bank(self):
        """Gets the ``Bank`` associated with this session.

        :return: the bank
        :rtype: ``osid.assessment.Bank``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.Bank

    bank = property(fget=get_bank)

    def can_create_sequence_rule(self):
        """Tests if this user can create sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_sequence_rule_with_record_types(self, sequence_rule_record_types):
        """Tests if this user can create a single ``SequenceRule`` using the desired record types.

        While
        ``AssessmentAuthoringManager.getSequenceRuleRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``SequenceRule``. Providing an empty array tests if a
        ``SequenceRule`` can be created with no records.

        :param sequence_rule_record_types: array of sequence rule record types
        :type sequence_rule_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``SequenceRule`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``sequence_rule_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_sequence_rule_form_for_create(self, assessment_part_id, next_assessment_part_id, sequence_rule_record_types):
        """Gets the sequence rule form for creating new sequence rules between two assessment parts.

        A new form should be requested for each create transaction.

        :param assessment_part_id: the source assessment part ``Id``
        :type assessment_part_id: ``osid.id.Id``
        :param next_assessment_part_id: the target assessment part ``Id``
        :type next_assessment_part_id: ``osid.id.Id``
        :param sequence_rule_record_types: array of sequence rule record types
        :type sequence_rule_record_types: ``osid.type.Type[]``
        :return: the sequence rule form
        :rtype: ``osid.assessment.authoring.SequenceRuleForm``
        :raise: ``InvalidArgument`` -- ``assessment_part_id`` and ``next_assessment_part_id`` not on the same assessment
        :raise: ``NotFound`` -- ``assessment_part_id`` or ``next_assessment_part_id`` is not found
        :raise: ``NullArgument`` -- ``assessment_part_id, next_assessment_part_id`` , or ``sequence_rule_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleForm

    def create_sequence_rule(self, sequence_rule_form):
        """Creates a new ``SequenceRule``.

        :param sequence_rule_form: the form for this ``SequenceRule``
        :type sequence_rule_form: ``osid.assessment.authoring.SequenceRuleForm``
        :return: the new ``SequenceRule``
        :rtype: ``osid.assessment.authoring.SequenceRule``
        :raise: ``IllegalState`` -- ``sequence_rule_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``sequence_rule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_form`` did not originate from ``get_sequence_rule_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRule

    def can_update_sequence_rules(self):
        """Tests if this user can update sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_sequence_rule_form_for_update(self, sequence_rule_id):
        """Gets the sequence rule form for updating an existing sequence rule.

        A new sequence rule form should be requested for each update
        transaction.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :return: the sequence rule form
        :rtype: ``osid.assessment.authoring.SequenceRuleForm``
        :raise: ``NotFound`` -- ``sequence_rule_id`` is not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.assessment.authoring.SequenceRuleForm

    def update_sequence_rule(self, sequence_rule_form):
        """Updates an existing sequence rule.

        :param sequence_rule_form: the form containing the elements to be updated
        :type sequence_rule_form: ``osid.assessment.authoring.SequenceRuleForm``
        :raise: ``IllegalState`` -- ``sequence_rule_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``sequence_rule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``sequence_rule_form`` did not originate from ``get_sequence_rule_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_sequence_rules(self):
        """Tests if this user can delete sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``SequenceRule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_sequence_rule(self, sequence_rule_id):
        """Deletes a ``SequenceRule``.

        :param sequence_rule_id: the ``Id`` of the ``SequenceRule`` to remove
        :type sequence_rule_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_sequence_rule_aliases(self):
        """Tests if this user can manage ``Id`` aliases for sequence rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_sequence_rule(self, sequence_rule_id, alias_id):
        """Adds a ``Id`` to a ``SequenceRule`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``SequenceRule`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id`` . If the alias is a pointer to another sequence rule. it
        is reassigned to the given sequence rule ``Id``.

        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``sequence_rule_id`` not found
        :raise: ``NullArgument`` -- ``sequence_rule_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_sequence_sequence_rules(self):
        """Tests if this user can order ``SequenceRules``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known sequencing operations
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer sequencing
        operations to an unauthorized user.

        :return: ``false`` if ``SequenceRule`` ordering is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def move_sequence_rule_ahead(self, sequence_rule_id, assessment_part_id, reference_id):
        """Reorders sequence rule for a source assessment part by moving the specified sequence rule in front of a reference sequence rule.

        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param assessment_part_id: the ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param reference_id: the reference sequence rule ``Id``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id, assessment_part_id,`` or ``reference_id`` not found or, ``sequence_rule_id`` or ``reference_id`` not related to ``assessment_part_id``
        :raise: ``NullArgument`` -- ``sequence_rule_id, assessment_part_id,`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def move_sequence_rule_behind(self, sequence_rule_id, assessment_part_id, reference_id):
        """Reorders sequence rule for a source assessment part by moving the specified sequence rule behind a reference sequence rule.

        :param sequence_rule_id: the ``Id`` of a ``SequenceRule``
        :type sequence_rule_id: ``osid.id.Id``
        :param assessment_part_id: the ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :param reference_id: the reference sequence rule ``Id``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``sequence_rule_id, assessment_part_id,`` or ``reference_id`` not found or, ``sequence_rule_id`` or ``reference_id`` not related to ``assessment_part_id``
        :raise: ``NullArgument`` -- ``sequence_rule_id, assessment_part_id,`` or ``reference_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_sequence_rules(self, sequence_rule_ids, assessment_part_id):
        """Reorders a set of sequence rules for an assessment part.

        :param sequence_rule_ids: the ``Ids`` for a set of ``SequenceRules``
        :type sequence_rule_ids: ``osid.id.Id[]``
        :param assessment_part_id: the ``Id`` of an ``AssessmentPart``
        :type assessment_part_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``assessment_part_id`` not found or, a ``sequence_rule_id`` not related to ``assessment_part_id``
        :raise: ``NullArgument`` -- ``sequence_rule_ids`` or ``assessment_part_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


