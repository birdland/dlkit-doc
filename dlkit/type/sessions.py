from ..osid import sessions as osid_sessions


class TypeLookupSession(osid_sessions.OsidSession):
    """This session retrieves Types.

    A single Type can be retrieved using ``get_type()`` and all types
    known to this service can be accessed via ``get_types()`` .

    """
    def can_lookup_types(self):
        """Tests if this user can perform ``Type`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_type(self, namespace, identifier, authority):
        """Gets a ``Type`` by its string representation which is a combination of the authority and identifier.

        This method only returns the ``Type`` if it is known by the
        given identification components.

        :param namespace: the identifier namespace
        :type namespace: ``string``
        :param identifier: the identifier
        :type identifier: ``string``
        :param authority: the authority
        :type authority: ``string``
        :return: the ``Type``
        :rtype: ``osid.type.Type``
        :raise: ``NotFound`` -- the type is not found
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.type.Type

    def has_type(self, type_):
        """Tests if the given ``Type`` is known.

        :param type: the ``Type`` to look for
        :type type: ``osid.type.Type``
        :return: ``true`` if the given ``Type`` is known, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_types_by_domain(self, domain):
        """Gets all the known Types by domain.

        :param domain: the domain
        :type domain: ``string``
        :return: the list of ``Types`` with the given domain
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``domain`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.type.TypeList

    def get_types_by_authority(self, authority):
        """Gets all the known Types by authority.

        :param authority: the authority
        :type authority: ``string``
        :return: the list of ``Types`` with the given authority
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- respect my authoritay

        """
        return # osid.type.TypeList

    def get_types_by_domain_and_authority(self, domain, authority):
        """Gets all the known Types by domain and authority.

        :param domain: the domain
        :type domain: ``string``
        :param authority: the authority
        :type authority: ``string``
        :return: the list of ``Types`` with the given domain and authority
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``domain`` or ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.type.TypeList

    def get_types(self):
        """Gets all the known Types.

        :return: the list of all known ``Types``
        :rtype: ``osid.type.TypeList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.type.TypeList

    types = property(fget=get_types)

    def is_equivalent(self, type_, equivalent_type):
        """Tests if the given types are equivalent.

        :param type: a type
        :type type: ``osid.type.Type``
        :param equivalent_type: another type
        :type equivalent_type: ``osid.type.Type``
        :return: ``true`` if both types are equivalent, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def implies_support(self, type_, base_type):
        """Tests if the given type is implies support of a base type.

        :param type: a type
        :type type: ``osid.type.Type``
        :param base_type: another type
        :type base_type: ``osid.type.Type``
        :return: ``true`` if ``base_type`` if supported by ``type,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def has_base_type(self, type_):
        """Tests if the given type is derived from a base type.

        :param type: a type
        :type type: ``osid.type.Type``
        :return: ``true`` is the given type is derived from a base type, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_base_types(self, type_):
        """Gets the immediate base types of this type.

        :param type: a type
        :type type: ``osid.type.Type``
        :return: the base types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.type.TypeList


class TypeAdminSession(osid_sessions.OsidSession):
    """This session is used to create, update and delete ``Types`` in the registry."""
    def can_create_types(self):
        """Tests if this user can create ``Types``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Type`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_type_form_for_create(self):
        """Gets the type form for creating new types.

        A new form should be requested for each create transaction.

        :return: the type form
        :rtype: ``osid.type.TypeForm``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.type.TypeForm

    type_form_for_create = property(fget=get_type_form_for_create)

    def create_type(self, authority, identifier_ns, identifier, type_form):
        """Creates a new ``Type``.

        :param authority: the authority
        :type authority: ``string``
        :param identifier_ns: the namespace of the identifier
        :type identifier_ns: ``string``
        :param identifier: the identifier
        :type identifier: ``string``
        :param type_form: the type form
        :type type_form: ``osid.type.TypeForm``
        :return: the created ``Type``
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``log_entry_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the arguments is invalid
        :raise: ``NullArgument`` -- one or more of the arguments is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``type_form`` did not originate from ``get_type_form_for_create()``

        """
        return # osid.type.Type

    def can_update_types(self):
        """Tests if this user can update types.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if type modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_update_type(self, type_):
        """Tests if this user can update the specified type.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating the ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :param type: the ``Type`` to be updated
        :type type: ``osid.type.Type``
        :return: ``false`` if type modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``

        """
        return # boolean

    def get_type_form_for_update(self, type_):
        """Gets the type form for creating new types.

        A new form should be requested for each create transaction.

        :param type: the ``Type`` to be updated
        :type type: ``osid.type.Type``
        :return: the type form
        :rtype: ``osid.type.TypeForm``
        :raise: ``IllegalState`` -- ``type_form`` already used in an update transaction
        :raise: ``NotFound`` -- ``type`` not found
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.type.TypeForm

    def update_type(self, type_, type_form):
        """Updates a type.

        :param type: the ``Type`` to be updated
        :type type: ``osid.type.Type``
        :param type_form: the type form
        :type type_form: ``osid.type.TypeForm``
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NotFound`` -- ``type`` is not found
        :raise: ``NullArgument`` -- ``type`` or ``type_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``type_form`` did not originate from ``get_type_form_for_update()``

        """
        pass

    def can_delete_types(self):
        """Tests if this user can delete ``Types`` from this ``ItemBank``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Type``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Item`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_delete_type(self, type_):
        """Tests if this user can delete the specified type.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleteing the
        ``Type`` will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :param type: the ``Type`` to be deleted
        :type type: ``osid.type.Type``
        :return: ``false`` if type deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``type`` is ``null``

        """
        return # boolean

    def delete_type(self, type_):
        """Removes a ``Type``.

        :param type: the ``Type`` to remove
        :type type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` is not found
        :raise: ``NullArgument`` -- ``type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def make_equivalent(self, primary_type, equivalent_type):
        """Makes two ``Types`` equivalent.

        Calls to ``TypeLookupSession.getType(equivalentType)`` return
        the ``primaryType``.

        :param primary_type: the primary ``Type``
        :type primary_type: ``osid.type.Type``
        :param equivalent_type: a ``Type`` to be made equivalent
        :type equivalent_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``primary_type`` or ``equivalent_type`` is not found
        :raise: ``NullArgument`` -- ``primary_type`` or ``equivalent_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def add_base_type(self, type_, base_type):
        """Adds a base type to a type.

        A base type is a parent of the type where the type implies
        support of the base type.

        :param type: a ``Type``
        :type type: ``osid.type.Type``
        :param base_type: a base type
        :type base_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` or ``base_type`` is not found
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_base_type(self, type_, base_type):
        """Removes a base type from a type.

        :param type: a ``Type``
        :type type: ``osid.type.Type``
        :param base_type: a base type
        :type base_type: ``osid.type.Type``
        :raise: ``NotFound`` -- ``type`` or ``base_type`` is not found
        :raise: ``NullArgument`` -- ``type`` or ``base_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

