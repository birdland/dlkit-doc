

Service Catalog
===============


Family
------

.. py:class:: Family(abc_relationship_objects.Family, osid_objects.OsidCatalog)
    A ``Family`` represents a collection of relationships.


    Like all OSID objects, a ``Family`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.





    .. py:method:: get_family_record(family_record_type):
        :noindex:




Relationship Lookup Methods
---------------------------

    .. py:method:: get_family_id():
        Gets the ``Family``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_id


    .. py:method:: get_family():
        Gets the ``Family`` associated with this session.

        :return: (osid.relationship.Family) - the family
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family


    .. py:method:: can_lookup_relationships():
        Tests if this user can perform ``Relationship`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_relationship_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_relationship_view():
        A complete view of the ``Relationship`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_family_view():
        Federates the view for methods in this session.

        A federated view will include relationships in families which
        are children of this family in the family hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_family_view():
        Isolates the view for methods in this session.

        An isolated view restricts retrievals to this family only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_effective_relationship_view():
        Only relationships whose effective dates are current are returned by methods in this
            session.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_any_effective_relationship_view():
        All relationships of any effective dates are returned by all methods in this session.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_relationship(relationship_id):
        Gets the ``Relationship`` specified by its ``Id``.

        :arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship`` to retrieve
        :return: (osid.relationship.Relationship) - the returned
                ``Relationship``
        :raises:  NotFound - no ``Relationship`` found with the given
                ``Id``
        :raises:  NullArgument - ``relationship_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_ids(relationship_ids):
        Gets a ``RelationshipList`` corresponding to the given ``IdList``.

        :arg:    relationship_ids (osid.id.IdList): the list of ``Ids``
                to retrieve
        :return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        :raises:  NotFound - an ``Id`` was not found
        :raises:  NullArgument - ``relationship_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_genus_type(relationship_genus_type):
        Gets a ``RelationshipList`` corresponding to the given relationship genus ``Type`` which
            does not include relationships of types derived from the specified ``Type``.

        :arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        :return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        :raises:  NullArgument - ``relationship_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_parent_genus_type(relationship_genus_type):
        Gets a ``RelationshipList`` corresponding to the given relationship genus ``Type`` and
            include any additional relationships with genus types derived from the specified
            ``Type``.

        :arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        :return: (osid.relationship.RelationshipList) - the returned
                ``Relationship list``
        :raises:  NullArgument - ``relationship_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_record_type(relationship_record_type):
        Gets a ``RelationshipList`` containing the given relationship record ``Type``.

        :arg:    relationship_record_type (osid.type.Type): a
                relationship record type
        :return: (osid.relationship.RelationshipList) - the returned
                ``RelationshipList``
        :raises:  NullArgument - ``relationship_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_on_date(from_, to):
        Gets a ``RelationshipList`` effective during the entire given date range inclusive but not
            confined to the date range.

        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  InvalidArgument - ``from is greater than to``
        :raises:  NullArgument - ``from`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_for_source(source_id):
        Gets a ``RelationshipList`` corresponding to the given peer ``Id``.

        :arg:    source_id (osid.id.Id): a peer ``Id``
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  NullArgument - ``source_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_for_source_on_date(source_id, from_, to):
        Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and effective during the
            entire given date range inclusive but not confined to the date range.

        :arg:    source_id (osid.id.Id): a peer ``Id``
        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  InvalidArgument - ``from is greater than to``
        :raises:  NullArgument - ``source_id, from`` ,or ``to`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_genus_type_for_source(source_id, relationship_genus_type):
        Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus
            ``Type.

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

        :arg:    source_id (osid.id.Id): a peer ``Id``
        :arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  NullArgument - ``source_id`` or
                ``relationship_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_genus_type_for_source_on_date(source_id, relationship_genus_type, from_, to):
        Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus
            ``Type`` and effective during the entire given date range inclusive but not confined to
            the date range.

        :arg:    source_id (osid.id.Id): a peer ``Id``
        :arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  InvalidArgument - ``from is greater than to``
        :raises:  NullArgument - ``source_id, relationship_genus_type,
                from`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_for_destination(destination_id):
        Gets a ``RelationshipList`` corresponding to the given peer ``Id``.

        :arg:    destination_id (osid.id.Id): a peer ``Id``
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  NullArgument - ``destination_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_for_destination_on_date(destination_id, from_, to):
        Gets a ``RelationshipList`` corresponding to the given peer ``Id`` with a starting effective
            date in the given range inclusive.

        :arg:    destination_id (osid.id.Id): a peer ``Id``
        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  InvalidArgument - ``from is greater than to``
        :raises:  NullArgument - ``destination_id, from`` ,or ``to`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_genus_type_for_destination(destination_id, relationship_genus_type):
        Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus
            ``Type.

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

        :arg:    destination_id (osid.id.Id): a peer ``Id``
        :arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  NullArgument - ``destination_id`` or
                ``relationship_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_genus_type_for_destination_on_date(destination_id, relationship_genus_type, from_, to):
        Gets a ``RelationshipList`` corresponding to the given peer ``Id`` and relationship genus
            ``Type`` and effective during the entire given date range inclusive but not confined to
            the date range.

        :arg:    destination_id (osid.id.Id): a peer ``Id``
        :arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  InvalidArgument - ``from is greater than to``
        :raises:  NullArgument - ``destination_id,
                relationship_genus_type, from`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_for_peers(source_id, destination_id):
        Gets a ``RelationshipList`` corresponding to the given peer ``Ids``.

        :arg:    source_id (osid.id.Id): a peer ``Id``
        :arg:    destination_id (osid.id.Id): a related peer ``Id``
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  NullArgument - ``source_id`` or ``destination_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_for_peers_on_date(source_id, destination_id, from_, to):
        Gets a ``RelationshipList`` corresponding to the given peer ``Ids`` and effective during the
            entire given date range inclusive but not confined to the date range.

        :arg:    source_id (osid.id.Id): a peer ``Id``
        :arg:    destination_id (osid.id.Id): a related peer ``Id``
        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  InvalidArgument - ``from`` is greater than ``to``
        :raises:  NullArgument - ``source_id, destination_id, from`` or
                ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_genus_type_for_peers(source_id, destination_id, relationship_genus_type):
        Gets a ``RelationshipList`` corresponding between the given peer ``Ids`` and relationship
            genus ``Type.

        Relationships`` of any genus derived from the given genus are
        returned.


        In plenary mode, the returned list contains all of the
        relationships corresponding to the given peer or an error
        results if a relationship is inaccessible. Otherwise,
        inaccessible ``Relationships`` may be omitted from the list.


        In effective mode, relationships are returned that are currently
        effective. In any effective mode, effective relationships and
        those currently expired are returned.

        :arg:    source_id (osid.id.Id): a peer ``Id``
        :arg:    destination_id (osid.id.Id): a related peer ``Id``
        :arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  NullArgument - ``source_id, destination_id,`` or
                ``relationship_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships_by_genus_type_for_peers_on_date(source_id, destination_id, relationship_genus_type, from_, to):
        Gets a ``RelationshipList`` effective during the entire given date range inclusive but not
            confined to the date range.

        :arg:    source_id (osid.id.Id): a peer ``Id``
        :arg:    destination_id (osid.id.Id): a related peer ``Id``
        :arg:    relationship_genus_type (osid.type.Type): a relationship
                genus type
        :arg:    from (osid.calendaring.DateTime): starting date
        :arg:    to (osid.calendaring.DateTime): ending date
        :return: (osid.relationship.RelationshipList) - the relationships
        :raises:  InvalidArgument - ``from is greater than to``
        :raises:  NullArgument - ``source_id, destination_id,
                relationship_genus_type, from`` or ``to`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationships():
        Gets all ``Relationships``.

        :return: (osid.relationship.RelationshipList) - a list of
                ``Relationships``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: relationships




Relationship Query Methods
--------------------------

    .. py:method:: get_family_id():
        Gets the ``Family``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_id


    .. py:method:: get_family():
        Gets the ``Family`` associated with this session.

        :return: (osid.relationship.Family) - the family
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family


    .. py:method:: use_federated_family_view():
        Federates the view for methods in this session.

        A federated view will include relationships in families which
        are children of this family in the family hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_family_view():
        Isolates the view for methods in this session.

        An isolated view restricts retrievals to this family only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: can_search_relationships():
        Tests if this user can perform ``Relationship`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationship_query():
        Gets a relationship query.

        :return: (osid.relationship.RelationshipQuery) - the relationship
                query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: relationship_query


    .. py:method:: get_relationships_by_query(relationship_query):
        Gets a list of ``Relationships`` matching the given relationship query.

        :arg:    relationship_query
                (osid.relationship.RelationshipQuery): the relationship
                query
        :return: (osid.relationship.RelationshipList) - the returned
                ``RelationshipList``
        :raises:  NullArgument - ``relationship_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``relationship_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Relationship Admin Methods
--------------------------

    .. py:method:: get_family_id():
        Gets the ``Familt``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Family Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family_id


    .. py:method:: get_family():
        Gets the ``Family`` associated with this session.

        :return: (osid.relationship.Family) - the family
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: family


    .. py:method:: can_create_relationships():
        Tests if this user can create ``Relationships`` A return of true does not guarantee
            successful authorization.

        A return of false indicates that it is known creating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Relationship`` creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_relationship_with_record_types(relationship_record_types):
        Tests if this user can create a single ``Relationship`` using the desired record types.

        While ``RelationshipManager.getRelationshipRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Relationship``. Providing an empty array tests if a
        ``Relationship`` can be created with no records.

        :arg:    relationship_record_types (osid.type.Type[]): array of
                relationship record types
        :return: (boolean) - ``true`` if ``Relationship`` creation using
                the specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``relationship_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationship_form_for_create(source_id, destination_id, relationship_record_types):
        Gets the relationship form for creating new relationships.

        A new form should be requested for each create transaction.

        :arg:    source_id (osid.id.Id): ``Id`` of a peer
        :arg:    destination_id (osid.id.Id): ``Id`` of the related peer
        :arg:    relationship_record_types (osid.type.Type[]): array of
                relationship record types
        :return: (osid.relationship.RelationshipForm) - the relationship
                form
        :raises:  NotFound - ``source_id`` or ``destination_id`` is not
                found
        :raises:  NullArgument - ``source_id`` or ``destination_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested recod
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_relationship(relationship_form):
        Creates a new ``Relationship``.

        :arg:    relationship_form (osid.relationship.RelationshipForm):
                the form for this ``Relationship``
        :return: (osid.relationship.Relationship) - the new
                ``Relationship``
        :raises:  IllegalState - ``relationship_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``relationship_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``relationship_form`` did not originate
                from ``get_relationship_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_relationships():
        Tests if this user can update ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Relationship`` modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_relationship_form_for_update(relationship_id):
        Gets the relationship form for updating an existing relationship.

        A new relationship form should be requested for each update
        transaction.

        :arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship``
        :return: (osid.relationship.RelationshipForm) - the relationship
                form
        :raises:  NotFound - ``relationship_id`` is not found
        :raises:  NullArgument - ``relationship_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_relationship(relationship_form):
        Updates an existing relationship.

        :arg:    relationship_form (osid.relationship.RelationshipForm):
                the form containing the elements to be updated
        :raises:  IllegalState - ``relationship_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``relationship_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``relationship_form`` did not originate
                from ``get_relationship_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_relationships():
        Tests if this user can delete ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Relationship`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Relationship`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_relationship(relationship_id):
        Deletes a ``Relationship``.

        :arg:    relationship_id (osid.id.Id): the ``Id`` of the
                ``Relationship`` to remove
        :raises:  NotFound - ``relationship_id`` not found
        :raises:  NullArgument - ``relationship_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_relationship_aliases():
        Tests if this user can manage ``Id`` aliases for ``Relationships``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Relationship`` aliasing is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_relationship(relationship_id, alias_id):
        Adds an ``Id`` to a ``Relationship`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Relationship`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another relationship, it is
        reassigned to the given relationship ``Id``.

        :arg:    relationship_id (osid.id.Id): the ``Id`` of a
                ``Relationship``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``relationship`` not found
        :raises:  NullArgument - ``relationship_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






