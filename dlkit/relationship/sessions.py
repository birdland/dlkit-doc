from ..osid import sessions as osid_sessions


class RelationshipLookupSession(osid_sessions.OsidSession):
    """This session defines methods for retrieving relationships.

    A ``Relationship`` is mapped to two OSID ``Ids``.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * federated family view: includes relationships in families which
        are children of this family in the family hierarchy
      * isolated family view: restricts lookups to this family only
      * effective relationship view: Relationship methods return only
        relationships currently in effect.
      * any effective relationship view: Relationship methods return
        both effective and ineffective relationships.


    Relationships may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Relationship``.

    """
    def get_family_id(self):
        """Gets the ``Family``  ``Id`` associated with this session.

        :return: the ``Family Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    family_id = property(fget=get_family_id)

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        :return: the family
        :rtype: ``osid.relationship.Family``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.relationship.Family

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
        return # boolean

    def use_comparative_relationship_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_relationship_view(self):
        """A complete view of the ``Relationship`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_family_view(self):
        """Federates the view for methods in this session.

        A federated view will include relationships in families which
        are children of this family in the family hierarchy.



        """
        pass

    def use_isolated_family_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this family only.



        """
        pass

    def use_effective_relationship_view(self):
        """Only relationships whose effective dates are current are returned by methods in this session."""
        pass

    def use_any_effective_relationship_view(self):
        """All relationships of any effective dates are returned by all methods in this session."""
        pass

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
        return # osid.relationship.Relationship

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

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
        return # osid.relationship.RelationshipList

    def get_relationships(self):
        """Gets all ``Relationships``.

        :return: a list of ``Relationships``
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.relationship.RelationshipList

    relationships = property(fget=get_relationships)


class RelationshipAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Relationships``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Relationship,`` a ``RelationshipForm`` is requested using
    ``get_relationship_form_for_create()`` specifying the desired peers
    and record ``Types`` or none if no record ``Types`` are needed. The
    returned ``RelationshipForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``RelationshipForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``RelationshipForm`` corresponds to an attempted transaction.

    For updates, ``RelationshipForms`` are requested to the
    ``Relationship``  ``Id`` that is to be updated using
    ``getRelationshipFormForUpdate()``. Similarly, the
    ``RelationshipForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``RelationshipForm`` can only be used once for a successful update
    and cannot be reused.

    The delete operations delete ``Relationships``. To unmap a
    ``Relationship`` from the current ``Family,`` the
    ``RelationshipFamilyAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Relationship`` itself thus
    removing it from all known ``Family`` catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_family_id(self):
        """Gets the ``Familt``  ``Id`` associated with this session.

        :return: the ``Family Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    family_id = property(fget=get_family_id)

    def get_family(self):
        """Gets the ``Family`` associated with this session.

        :return: the family
        :rtype: ``osid.relationship.Family``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.relationship.Family

    family = property(fget=get_family)

    def can_create_relationships(self):
        """Tests if this user can create ``Relationships`` A return of true does not guarantee successful authorization.

        A return of false indicates that it is known creating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Relationship`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

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
        return # boolean

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
        return # osid.relationship.RelationshipForm

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
        return # osid.relationship.Relationship

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
        return # boolean

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
        return # osid.relationship.RelationshipForm

    def update_relationship(self, relationship_form):
        """Updates an existing relationship.

        :param relationship_form: the form containing the elements to be updated
        :type relationship_form: ``osid.relationship.RelationshipForm``
        :raise: ``IllegalState`` -- ``relationship_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``relationship_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``relationship_form`` did not originate from ``get_relationship_form_for_update()``

        """
        pass

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
        return # boolean

    def delete_relationship(self, relationship_id):
        """Deletes a ``Relationship``.

        :param relationship_id: the ``Id`` of the ``Relationship`` to remove
        :type relationship_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``relationship_id`` not found
        :raise: ``NullArgument`` -- ``relationship_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        return # boolean

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
        pass


class FamilyLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Family`` objects.

    The ``Family`` represents a collection of relationships.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Families`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Families``
    referenced by it are available, and a test-taking applicationmay
    sacrifice some interoperability for the sake of precision.

    """
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
        return # boolean

    def use_comparative_family_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_family_view(self):
        """A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

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
        return # osid.relationship.Family

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
        return # osid.relationship.FamilyList

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
        return # osid.relationship.FamilyList

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
        return # osid.relationship.FamilyList

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
        return # osid.relationship.FamilyList

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
        return # osid.relationship.FamilyList

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
        return # osid.relationship.FamilyList

    families = property(fget=get_families)


class FamilyAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Families``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Family,`` a ``FamilyForm`` is requested using
    ``get_family_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``FamilyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``FamilyForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``FamilyForm``
    corresponds to an attempted transaction.

    For updates, ``FamilyForms`` are requested to the ``Family``  ``Id``
    that is to be updated using ``getFamilyFormForUpdate()``. Similarly,
    the ``FamilyForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``FamilyForm`` can only be used once for a successful update and
    cannot be reused.

    The delete operations delete ``Families``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
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
        return # boolean

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
        return # boolean

    def get_family_form_for_create(self, family_record_types):
        """Gets the family form for creating new families.

        A new form should be requested for each create transaction.

        :param family_record_types: array of family record types
        :type family_record_types: ``osid.type.Type[]``
        :return: the family form
        :rtype: ``osid.relationship.FamilyForm``
        :raise: ``NullArgument`` -- ``family_record_types is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        return # osid.relationship.FamilyForm

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
        return # osid.relationship.Family

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
        return # boolean

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
        return # osid.relationship.FamilyForm

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
        pass

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
        return # boolean

    def delete_family(self, family_id):
        """Deletes a ``Family``.

        :param family_id: the ``Id`` of the ``Family`` to remove
        :type family_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``family_id`` not found
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        return # boolean

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
        pass


class FamilyHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Family`` objects.

    Each node in the hierarchy is a unique ``Family``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_families()`` and ``getChildFamilies()``. To relate
    these ``Ids`` to another OSID, ``get_family_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Family`` available in the Relationship OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_families()`` or ``get_child_families()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: family elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition


    """
    def get_family_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

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
        return # boolean

    def use_comparative_family_view(self):
        """The returns from the family methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_family_view(self):
        """A complete view of the ``Family`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_root_family_ids(self):
        """Gets the root family ``Ids`` in this hierarchy.

        :return: the root family ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

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
        return # osid.relationship.FamilyList

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.relationship.FamilyList

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
        return # boolean

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
        return # boolean

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
        return # boolean

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
        return # osid.id.IdList

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
        return # osid.relationship.FamilyList

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
        return # boolean

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
        return # osid.hierarchy.Node

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
        return # osid.relationship.FamilyNode


class FamilyHierarchyDesignSession(osid_sessions.OsidSession):
    """This session manages a hierarchy of families may be organized into a hierarchy for organizing or federating.

    A parent ``Family`` includes all of the relationships of its
    children such that a single root node contains all of the
    relationships of the federation.

    """
    def get_family_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    family_hierarchy_id = property(fget=get_family_hierarchy_id)

    def get_family_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    family_hierarchy = property(fget=get_family_hierarchy)

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
        return # boolean

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
        pass

    def remove_root_family(self, family_id):
        """Removes a root family.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``family_id`` not a root
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

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
        pass

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
        pass

    def remove_child_families(self, family_id):
        """Removes all children from a family.

        :param family_id: the ``Id`` of a family
        :type family_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``family_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``family_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


