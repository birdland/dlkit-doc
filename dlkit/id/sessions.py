from ..osid import sessions as osid_sessions


class IdLookupSession(osid_sessions.OsidSession):
    """This session is for retrieving ``Id`` objects.

    ``get_ids()`` retrieves all known ``Ids``. The existence of a single
    identifier can be confirmed through the ``get_id()`` method, or it
    can be used as a means of ``Id`` translation.

    """
    def can_lookup_ids(self):
        """Tests if this user can perform ``Id`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_id(self, id_):
        """Gets an ``Id``.

        This method serves to get the principal ``Id`` if the given
        ``Id`` Is an alias.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: the ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.Id

    ident = property(fget=get_id)

    def get_ids_by_ids(self, ids):
        """Gets a list of ``Ids``.

        This method serves to get the principal ``Ids`` if different
        from the given ``Ids``.

        :param ids: a list of ``Ids``
        :type ids: ``osid.id.IdList``
        :return: a list of ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- an ``id`` is not found
        :raise: ``NullArgument`` -- ``ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_id_aliases(self, id_):
        """Gets a list of ``Id`` aliases of an ``Id``.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :return: a list of alias ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_ids_by_authority(self, authority):
        """Gets ``Ids`` by the given authority.

        :param authority: an authority
        :type authority: ``string``
        :return: a list of ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``authority`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_ids(self):
        """Gets all ``Ids``.

        :return: the list of all ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    ids = property(fget=get_ids)

    def is_equivalent(self, id_, equivalent_id):
        """Tests if the two ``Ids`` are equivalent.

        Two ``Ids`` are equivalent if they identify the same object. If
        one of the ``Ids`` is not known, they are not equivalent.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param equivalent_id: an ``Id``
        :type equivalent_id: ``osid.id.Id``
        :return: ``true`` if the ``Ids`` are equivalent, false otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``null`` argument provided
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean


class IdAdminSession(osid_sessions.OsidSession):
    """This session is used to create a new ``Id``."""
    def can_create_ids(self):
        """Tests if this user can create ``Ids``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known create methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations.

        :return: ``false`` if create methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def create_id(self):
        """Issues a new ``Id``.

        :return: the created ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.Id

    def can_alias_ids(self):
        """Tests if this user can alias ``Ids``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known add methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer alias
        operations.

        :return: ``false`` if alias methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_id(self, primary_id, equivalent_id):
        """Makes two ``Ids`` equivalent.

        The primary ``Id`` is known to this service and the equivalent
        ``Id`` may be already known to this service or an external
        ``Id``. If the external ``Id`` is already mapped to another
        ``Id,`` it is changed to map to the given primary ``Id``. Calls
        to ``IdLookupSession.getId(equivalentId)`` return the
        ``primaryId``.

        :param primary_id: the primary ``Id``
        :type primary_id: ``osid.id.Id``
        :param equivalent_id: an ``Id`` to be made equivalent
        :type equivalent_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``primary_id`` is not found
        :raise: ``NullArgument`` -- ``primary_id`` or ``equivalent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class IdBatchAdminSession(IdAdminSession):
    """This session is used to create a new ``Id``."""
    def create_ids(self, quantity):
        """Issues a set of new ``Ids``.

        :param quantity: the number to create
        :type quantity: ``cardinal``
        :return: the created ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def alias_ids(self, primary_ids):
        """Makes a set of ``Ids`` known to this service equivalent such that for each primary and equivalent ``Id`` in the given array, calls to ``IdLookupSession.

        getId(equivalentId)`` return the ``primaryId``.

        :param primary_ids: the primary ``Ids``
        :type primary_ids: ``osid.transaction.batch.AliasRequestList``
        :return: the created ``Ids``
        :rtype: ``osid.transaction.batch.AliasResponseList``
        :raise: ``InvalidArgument`` -- ``primary_ids`` does not match ``equivalent_ids``
        :raise: ``NotFound`` -- a ``primary_id`` or ``equivalent_id`` is not found
        :raise: ``NullArgument`` -- ``primary_ids`` or ``equivalent_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.transaction.batch.AliasResponseList


