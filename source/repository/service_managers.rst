

Service Managers
================


Repository Manager
------------------

.. py:class:: RepositoryManager(osid_managers.OsidManager, RepositoryProfile, repository_managers.RepositoryManager)
    The repository manager provides access to asset lookup and creation session and provides
    interoperability tests for various aspects of this service.


    The sessions included in this manager are:




      * ``AssetLookupSession:`` a session to retrieve assets
      * ``AssetQuerySession:`` a session to query assets
      * ``AssetSearchSession:`` a session to search for assets
      * ``AssetAdminSession:`` a session to create and delete assets
      * ``AssetNotificationSession:`` a session to receive notifications
        pertaining to asset changes
      * ``AssetRepositorySession:`` a session to look up asset to
        repository mappings
      * ``AssetRepositoryAssignmentSession:`` a session to manage asset
        to repository mappings
      * ``AssetSmartRepositorySession:`` a session to manage dynamic
        repositories of assets
      * ``AssetTemporalSession:`` a session to access the temporal
        coverage of an asset
      * ``AssetTemporalAssignmentSession:`` a session to manage the
        temporal coverage of an asset
      * ``AssetSpatialSession:`` a session to access the spatial
        coverage of an asset
      * ``AssetSpatialAssignmentSession:`` a session to manage the
        spatial coverage of an asset
      * ``AssetCompositionSession:`` a session to look up asset
        composition mappings
      * ``AssetCompositionDesignSession:`` a session to map assets to
        compositions




      * ``CompositionLookupSession: a`` session to retrieve compositions
      * ``CompositionQuerySession:`` a session to query compositions
      * ``CompositionSearchSession:`` a session to search for
        compositions
      * ``CompositionAdminSession:`` a session to create, update and
        delete compositions
      * ``CompositionNotificationSession:`` a session to receive
        notifications pertaining to changes in compositions
      * ``CompositionRepositorySession:`` a session to retrieve
        composition repository mappings
      * ``CompositionRepositoryAssignmentSession:`` a session to manage
        composition repository mappings
      * ``CompositionSmartRepositorySession:`` a session to manage
        dynamic repositories of compositions




      * ``RepositoryLookupSession: a`` session to retrieve repositories
      * ``RepositoryQuerySession:`` a session to query repositories
      * ``RepositorySearchSession:`` a session to search for
        repositories
      * ``RepositoryAdminSession:`` a session to create, update and
        delete repositories
      * ``RepositoryNotificationSession:`` a session to receive
        notifications pertaining to changes in repositories
      * ``RepositoryHierarchySession:`` a session to traverse repository
        hierarchies
      * ``RepositoryHierarchyDesignSession:`` a session to manage
        repository hierarchies





    .. py:method:: get_asset_lookup_session():
        :noindex:


    .. py:attribute:: asset_lookup_session
        :noindex:


    .. py:method:: get_asset_lookup_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_query_session():
        :noindex:


    .. py:attribute:: asset_query_session
        :noindex:


    .. py:method:: get_asset_query_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_search_session():
        :noindex:


    .. py:attribute:: asset_search_session
        :noindex:


    .. py:method:: get_asset_search_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_admin_session():
        :noindex:


    .. py:attribute:: asset_admin_session
        :noindex:


    .. py:method:: get_asset_admin_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_notification_session(asset_receiver):
        :noindex:


    .. py:method:: get_asset_notification_session_for_repository(asset_receiver, repository_id):
        :noindex:


    .. py:method:: get_asset_repository_session():
        :noindex:


    .. py:attribute:: asset_repository_session
        :noindex:


    .. py:method:: get_asset_repository_assignment_session():
        :noindex:


    .. py:attribute:: asset_repository_assignment_session
        :noindex:


    .. py:method:: get_asset_smart_repository_session(repository_id):
        :noindex:


    .. py:method:: get_asset_temporal_session():
        :noindex:


    .. py:attribute:: asset_temporal_session
        :noindex:


    .. py:method:: get_asset_temporal_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_temporal_assignment_session():
        :noindex:


    .. py:attribute:: asset_temporal_assignment_session
        :noindex:


    .. py:method:: get_asset_temporal_assignment_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_spatial_session():
        :noindex:


    .. py:attribute:: asset_spatial_session
        :noindex:


    .. py:method:: get_asset_spatial_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_spatial_assignment_session():
        :noindex:


    .. py:attribute:: asset_spatial_assignment_session
        :noindex:


    .. py:method:: get_asset_spatial_assignment_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_composition_session():
        :noindex:


    .. py:attribute:: asset_composition_session
        :noindex:


    .. py:method:: get_asset_composition_design_session():
        :noindex:


    .. py:attribute:: asset_composition_design_session
        :noindex:


    .. py:method:: get_composition_lookup_session():
        :noindex:


    .. py:attribute:: composition_lookup_session
        :noindex:


    .. py:method:: get_composition_lookup_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_query_session():
        :noindex:


    .. py:attribute:: composition_query_session
        :noindex:


    .. py:method:: get_composition_query_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_search_session():
        :noindex:


    .. py:attribute:: composition_search_session
        :noindex:


    .. py:method:: get_composition_search_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_admin_session():
        :noindex:


    .. py:attribute:: composition_admin_session
        :noindex:


    .. py:method:: get_composition_admin_session_for_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_notification_session(composition_receiver):
        :noindex:


    .. py:method:: get_composition_notification_session_for_repository(composition_receiver, repository_id):
        :noindex:


    .. py:method:: get_composition_repository_session():
        :noindex:


    .. py:attribute:: composition_repository_session
        :noindex:


    .. py:method:: get_composition_repository_assignment_session():
        :noindex:


    .. py:attribute:: composition_repository_assignment_session
        :noindex:


    .. py:method:: get_composition_smart_repository_session(repository_id):
        :noindex:


    .. py:method:: get_repository_lookup_session():
        :noindex:


    .. py:attribute:: repository_lookup_session
        :noindex:


    .. py:method:: get_repository_query_session():
        :noindex:


    .. py:attribute:: repository_query_session
        :noindex:


    .. py:method:: get_repository_search_session():
        :noindex:


    .. py:attribute:: repository_search_session
        :noindex:


    .. py:method:: get_repository_admin_session():
        :noindex:


    .. py:attribute:: repository_admin_session
        :noindex:


    .. py:method:: get_repository_notification_session(repository_receiver):
        :noindex:


    .. py:method:: get_repository_hierarchy_session():
        :noindex:


    .. py:attribute:: repository_hierarchy_session
        :noindex:


    .. py:method:: get_repository_hierarchy_design_session():
        :noindex:


    .. py:attribute:: repository_hierarchy_design_session
        :noindex:


    .. py:method:: get_repository_batch_manager():
        :noindex:


    .. py:attribute:: repository_batch_manager
        :noindex:


    .. py:method:: get_repository_rules_manager():
        :noindex:


    .. py:attribute:: repository_rules_manager
        :noindex:




Asset Repository Methods
------------------------

    .. py:method:: can_lookup_asset_repository_mappings():
        Tests if this user can perform lookups of asset/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_repository_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_repository_view():
        A complete view of the ``Asset`` and ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_asset_ids_by_repository(repository_id):
        Gets the list of ``Asset``  ``Ids`` associated with a ``Repository``.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.id.IdList) - list of related asset ``Ids``
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_repository(repository_id):
        Gets the list of ``Assets`` associated with a ``Repository``.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.repository.AssetList) - list of related assets
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_asset_ids_by_repositories(repository_ids):
        Gets the list of ``Asset Ids`` corresponding to a list of ``Repository`` objects.

        :arg:    repository_ids (osid.id.IdList): list of repository
                ``Ids``
        :return: (osid.id.IdList) - list of asset ``Ids``
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_repositories(repository_ids):
        Gets the list of ``Assets`` corresponding to a list of ``Repository`` objects.

        :arg:    repository_ids (osid.id.IdList): list of repository
                ``Ids``
        :return: (osid.repository.AssetList) - list of assets
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_ids_by_asset(asset_id):
        Gets the list of ``Repository``  ``Ids`` mapped to an ``Asset``.

        :arg:    asset_id (osid.id.Id): ``Id`` of an ``Asset``
        :return: (osid.id.IdList) - list of repository ``Ids``
        :raises:  NotFound - ``asset_id`` is not found
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_asset(asset_id):
        Gets the list of ``Repository`` objects mapped to an ``Asset``.

        :arg:    asset_id (osid.id.Id): ``Id`` of an ``Asset``
        :return: (osid.repository.RepositoryList) - list of repositories
        :raises:  NotFound - ``asset_id`` is not found
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Asset Repository Assignment Methods
-----------------------------------

    .. py:method:: can_assign_assets():
        Tests if this user can alter asset/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_assets_to_repository(repository_id):
        Tests if this user can alter asset/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``repository_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_repository_ids(repository_id):
        Gets a list of repositories including and under the given repository node in which any asset
            can be assigned.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (osid.id.IdList) - list of assignable repository ``Ids``
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_repository_ids_for_asset(repository_id, asset_id):
        Gets a list of repositories including and under the given repository node in which a
            specific asset can be assigned.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset``
        :return: (osid.id.IdList) - list of assignable repository ``Ids``
        :raises:  NullArgument - ``repository_id`` or ``asset_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_asset_to_repository(asset_id, repository_id):
        Adds an existing ``Asset`` to a ``Repository``.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset``
        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :raises:  AlreadyExists - ``asset_id`` already assigned to
                ``repository_id``
        :raises:  NotFound - ``asset_id`` or ``repository_id`` not found
        :raises:  NullArgument - ``asset_id`` or ``repository_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_asset_from_repository(asset_id, repository_id):
        Removes an ``Asset`` from a ``Repository``.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset``
        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :raises:  NotFound - ``asset_id`` or ``repository_id`` not found
                or ``asset_id`` not assigned to ``repository_id``
        :raises:  NullArgument - ``asset_id`` or ``repository_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Composition Repository Methods
------------------------------

    .. py:method:: use_comparative_composition_repository_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_composition_repository_view():
        A complete view of the ``Composition`` and ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: can_lookup_composition_repository_mappings():
        Tests if this user can perform lookups of composition/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_composition_ids_by_repository(repository_id):
        Gets the list of ``Composition``  ``Ids`` associated with a ``Repository``.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.id.IdList) - list of related composition ``Ids``
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compositions_by_repository(repository_id):
        Gets the list of ``Compositions`` associated with a ``Repository``.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.repository.CompositionList) - list of related
                compositions
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_composition_ids_by_repositories(repository_ids):
        Gets the list of ``Composition``  ``Ids`` corresponding to a list of ``Repository`` objects.

        :arg:    repository_ids (osid.id.IdList): list of repository
                ``Ids``
        :return: (osid.id.IdList) - list of composition ``Ids``
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compoitions_by_repositories(repository_ids):
        Gets the list of ``Compositions`` corresponding to a list of ``Repository`` objects.

        :arg:    repository_ids (osid.id.IdList): list of repository
                ``Ids``
        :return: (osid.repository.CompositionList) - list of Compositions
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_ids_by_composition(composition_id):
        Gets the ``Repository``  ``Ids`` mapped to a ``Composition``.

        :arg:    composition_id (osid.id.Id): ``Id`` of a ``Composition``
        :return: (osid.id.IdList) - list of repository ``Ids``
        :raises:  NotFound - ``composition_id`` is not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_composition(composition_id):
        Gets the ``Repository`` objects mapped to a ``Composition``.

        :arg:    composition_id (osid.id.Id): ``Id`` of a ``Composition``
        :return: (osid.repository.RepositoryList) - list of repositories
        :raises:  NotFound - ``composition_id`` is not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Composition Repository Assignment Methods
-----------------------------------------

    .. py:method:: can_assign_compositions():
        Tests if this user can alter composition/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_compositions_to_repository(repository_id):
        Tests if this user can alter composition/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``repository_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_repository_ids(repository_id):
        Gets a list of repositories including and under the given repository node in which any
            composition can be assigned.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (osid.id.IdList) - list of assignable repository ``Ids``
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_repository_ids_for_composition(repository_id, composition_id):
        Gets a list of repositories including and under the given repository node in which a
            specific composition can be assigned.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition``
        :return: (osid.id.IdList) - list of assignable repository ``Ids``
        :raises:  NullArgument - ``repository_id`` or ``composition_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_composition_to_repository(composition_id, repository_id):
        Adds an existing ``Composition`` to a ``Repository``.

        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition``
        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :raises:  AlreadyExists - ``composition_id`` already assigned to
                ``repository_id``
        :raises:  NotFound - ``composition_id`` or ``repository_id`` not
                found
        :raises:  NullArgument - ``composition_id`` or ``repository_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_composition_from_repository(composition_id, repository_id):
        Removes ``Composition`` from a ``Repository``.

        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition``
        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :raises:  NotFound - ``composition_id`` or ``repository_id`` not
                found or ``composition_id`` not assigned to
                ``repository_id``
        :raises:  NullArgument - ``composition_id`` or ``repository_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Repository Lookup Methods
-------------------------

    .. py:method:: can_lookup_repositories():
        Tests if this user can perform ``Repository`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_repository_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_repository_view():
        A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_repository(repository_id):
        Gets the ``Repository`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Repository`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Repository`` and retained
        for compatibility.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.repository.Repository) - the repository
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_repositories_by_ids(repository_ids):
        Gets a ``RepositoryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        repositories specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Repositories`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :arg:    repository_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NotFound - an ``Id`` was not found
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_genus_type(repository_genus_type):
        Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` which does
            not include repositories of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :arg:    repository_genus_type (osid.type.Type): a repository
                genus type
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NullArgument - ``repository_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_parent_genus_type(repository_genus_type):
        Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` and include
            any additional repositories with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :arg:    repository_genus_type (osid.type.Type): a repository
                genus type
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NullArgument - ``repository_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_record_type(repository_record_type):
        Gets a ``RepositoryList`` containing the given repository record ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :arg:    repository_record_type (osid.type.Type): a repository
                record type
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NullArgument - ``repository_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_provider(resource_id):
        Gets a ``RepositoryList`` from the given provider ````.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories():
        Gets all ``Repositories``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :return: (osid.repository.RepositoryList) - a list of
                ``Repositories``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repositories




Repository Query Methods
------------------------

    .. py:method:: can_search_repositories():
        Tests if this user can perform ``Repository`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_query():
        Gets a repository query.

        :return: (osid.repository.RepositoryQuery) - the repository query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_query


    .. py:method:: get_repositories_by_query(repository_query):
        Gets a list of ``Repositories`` matching the given repository query.

        :arg:    repository_query (osid.repository.RepositoryQuery): the
                repository query
        :return: (osid.repository.RepositoryList) - the returned
                ``RepositoryList``
        :raises:  NullArgument - ``repository_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``repository_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Repository Admin Methods
------------------------

    .. py:method:: can_create_repositories():
        Tests if this user can create ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Repository`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_repository_with_record_types(repository_record_types):
        Tests if this user can create a single ``Repository`` using the desired record types.

        While ``RepositoryManager.getRepositoryRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Repository``. Providing an empty array tests if a
        ``Repository`` can be created with no records.

        :arg:    repository_record_types (osid.type.Type[]): array of
                repository record types
        :return: (boolean) - ``true`` if ``Repository`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``repository_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_form_for_create(repository_record_types):
        Gets the repository form for creating new repositories.

        A new form should be requested for each create transaction.

        :arg:    repository_record_types (osid.type.Type[]): array of
                repository record types
        :return: (osid.repository.RepositoryForm) - the repository form
        :raises:  NullArgument - ``repository_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_repository(repository_form):
        Creates a new ``Repository``.

        :arg:    repository_form (osid.repository.RepositoryForm): the
                form for this ``Repository``
        :return: (osid.repository.Repository) - the new ``Repository``
        :raises:  IllegalState - ``repository_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``repository_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``repository_form`` did not originate from
                ``get_repository_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_repositories():
        Tests if this user can update ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Repository`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_form_for_update(repository_id):
        Gets the repository form for updating an existing repository.

        A new repository form should be requested for each update
        transaction.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (osid.repository.RepositoryForm) - the repository form
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_repository(repository_form):
        Updates an existing repository.

        :arg:    repository_form (osid.repository.RepositoryForm): the
                form containing the elements to be updated
        :raises:  IllegalState - ``repository_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``repository_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``repository_form`` did not originate from
                ``get_repository_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_repositories():
        Tests if this user can delete ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Repository`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_repository(repository_id):
        Deletes a ``Repository``.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository`` to remove
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_repository_aliases():
        Tests if this user can manage ``Id`` aliases for repositories.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Repository`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_repository(repository_id, alias_id):
        Adds an ``Id`` to a ``Repository`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Repository`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another repository, it is reassigned
        to the given repository ``Id``.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a
                ``Repository``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Repository Hierarchy Methods
----------------------------

    .. py:method:: get_repository_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_hierarchy_id


    .. py:method:: get_repository_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_hierarchy


    .. py:method:: can_access_repository_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_repository_view():
        The returns from the repository methods may omit or translate elements based on this
            session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_repository_view():
        A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_repository_ids():
        Gets the root repository ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root repository ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_repository_ids


    .. py:method:: get_root_repositories():
        Gets the root repositories in the repository hierarchy.

        A node with no parents is an orphan. While all repository
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.

        :return: (osid.repository.RepositoryList) - the root repositories
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_repositories


    .. py:method:: has_parent_repositories(repository_id):
        Tests if the ``Repository`` has any parents.

        :arg:    repository_id (osid.id.Id): a repository ``Id``
        :return: (boolean) - ``true`` if the repository has parents,
                ``false`` otherwise
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_repository(id_, repository_id):
        Tests if an ``Id`` is a direct parent of a repository.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``repository_id,``  ``false`` otherwise
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``id`` or ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_repository_ids(repository_id):
        Gets the parent ``Ids`` of the given repository.

        :arg:    repository_id (osid.id.Id): a repository ``Id``
        :return: (osid.id.IdList) - the parent ``Ids`` of the repository
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_repositories(repository_id):
        Gets the parents of the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :return: (osid.repository.RepositoryList) - the parents of the
                repository
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_repository(id_, repository_id):
        Tests if an ``Id`` is an ancestor of a repository.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    repository_id (osid.id.Id): the Id of a repository
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``repository_id,``  ``false`` otherwise
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_repositories(repository_id):
        Tests if a repository has any children.

        :arg:    repository_id (osid.id.Id): a repository ``Id``
        :return: (boolean) - ``true`` if the ``repository_id`` has
                children, ``false`` otherwise
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_repository(id_, repository_id):
        Tests if a node is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``repository_id,``  ``false`` otherwise
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_repository_ids(repository_id):
        Gets the ``Ids`` of the children of the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the repository
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_repositories(repository_id):
        Gets the children of the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :return: (osid.repository.RepositoryList) - the children of the
                repository
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_repository(id_, repository_id):
        Tests if an ``Id`` is a descendant of a repository.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``repository_id,`` ``false`` otherwise
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` or ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_repository_node_ids(repository_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - the specified repository node
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_nodes(repository_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.repository.RepositoryNode) - the specified
                repository node
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Repository Hierarchy Design Methods
-----------------------------------

    .. py:method:: get_repository_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_hierarchy_id


    .. py:method:: get_repository_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_hierarchy


    .. py:method:: can_modify_repository_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_repository(repository_id):
        Adds a root repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :raises:  AlreadyExists - ``repository_id`` is already in
                hierarchy
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_repository(repository_id):
        Removes a root repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :raises:  NotFound - ``repository_id`` not a root
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_repository(repository_id, child_id):
        Adds a child to a repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``repository_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``repository_id`` or ``child_id`` not found
        :raises:  NullArgument - ``repository_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_repository(repository_id, child_id):
        Removes a child from a repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``repository_id`` not a parent of
                ``child_id``
        :raises:  NullArgument - ``repository_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_repositories(repository_id):
        Removes all children from a repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :raises:  NotFound - ``repository_id`` not in hierarchy
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Repository Proxy Manager
------------------------

.. py:class:: RepositoryProxyManager(osid_managers.OsidProxyManager, RepositoryProfile, repository_managers.RepositoryProxyManager)
    The repository manager provides access to asset lookup and creation session and provides
    interoperability tests for various aspects of this service.


    Methods in this manager support the passing of a ``Proxy`` for the
    purposes of passing information from a server environment. The
    sessions included in this manager are:




      * ``AssetLookupSession:`` a session to retrieve assets
      * ``AssetQuerySession:`` a session to query assets
      * ``AssetSearchSession:`` a session to search for assets
      * ``AssetAdminSession:`` a session to create and delete assets
      * ``AssetNotificationSession:`` a session to receive notifications
        pertaining to asset changes
      * ``AssetRepositorySession:`` a session to look up asset to
        repository mappings
      * ``AssetRepositoryAssignmentSession:`` a session to manage asset
        to repository mappings
      * ``AssetSmartRepositorySession:`` a session to manage dynamic
        repositories of assets
      * ``AssetTemporalSession:`` a session to access the temporal
        coverage of an asset
      * ``AssetTemporalAssignmentSession:`` a session to manage the
        temporal coverage of an asset
      * ``AssetSpatialSession:`` a session to access the spatial
        coverage of an asset
      * ``AssetSpatialAssignmentSession:`` a session to manage the
        spatial coverage of an asset
      * ``AssetCompositionSession:`` a session to look up asset
        composition mappings
      * ``AssetCompositionDesignSession:`` a session to map assets to
        compositions




      * ``CompositionLookupSession: a`` session to retrieve compositions
      * ``CompositionQuerySession:`` a session to query compositions
      * ``CompositionSearchSession:`` a session to search for
        compositions
      * ``CompositionAdminSession:`` a session to create, update and
        delete compositions
      * ``CompositionNotificationSession:`` a session to receive
        notifications pertaining to changes in compositions
      * ``CompositionRepositorySession:`` a session to retrieve
        composition repository mappings
      * ``CompositionRepositoryAssignmentSession:`` a session to manage
        composition repository mappings
      * ``CompositionSmartRepositorySession:`` a session to manage
        dynamic repositories of compositions




      * ``RepositoryLookupSession: a`` session to retrieve repositories
      * ``RepositoryQuerySession:`` a session to query repositories
      * ``RepositorySearchSession:`` a session to search for
        repositories
      * ``RepositoryAdminSession:`` a session to create, update and
        delete repositories
      * ``RepositoryNotificationSession:`` a session to receive
        notifications pertaining to changes in repositories
      * ``RepositoryHierarchySession:`` a session to traverse repository
        hierarchies
      * ``RepositoryHierarchyDesignSession:`` a session to manage
        repository hierarchies





    .. py:method:: get_asset_lookup_session(proxy):
        :noindex:


    .. py:method:: get_asset_lookup_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_query_session(proxy):
        :noindex:


    .. py:method:: get_asset_query_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_search_session(proxy):
        :noindex:


    .. py:method:: get_asset_search_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_admin_session(proxy):
        :noindex:


    .. py:method:: get_asset_admin_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_notification_session(asset_receiver, proxy):
        :noindex:


    .. py:method:: get_asset_notification_session_for_repository(asset_receiver, repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_repository_session(proxy):
        :noindex:


    .. py:method:: get_asset_repository_assignment_session(proxy):
        :noindex:


    .. py:method:: get_asset_smart_repository_session(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_temporal_session(proxy):
        :noindex:


    .. py:method:: get_asset_temporal_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_temporal_assignment_session(proxy):
        :noindex:


    .. py:method:: get_asset_temporal_assignment_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_spatial_session(proxy):
        :noindex:


    .. py:method:: get_asset_spatial_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_spatial_assignment_session(proxy):
        :noindex:


    .. py:method:: get_asset_spatial_assignment_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_asset_composition_session(proxy):
        :noindex:


    .. py:method:: get_asset_composition_design_session(proxy):
        :noindex:


    .. py:method:: get_composition_lookup_session(proxy):
        :noindex:


    .. py:method:: get_composition_lookup_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_query_session(proxy):
        :noindex:


    .. py:method:: get_composition_query_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_search_session(proxy):
        :noindex:


    .. py:method:: get_composition_search_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_admin_session(proxy):
        :noindex:


    .. py:method:: get_composition_admin_session_for_repository(repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_notification_session(composition_receiver, proxy):
        :noindex:


    .. py:method:: get_composition_notification_session_for_repository(composition_receiver, repository_id, proxy):
        :noindex:


    .. py:method:: get_composition_repository_session(proxy):
        :noindex:


    .. py:method:: get_composition_repository_assignment_session(proxy):
        :noindex:


    .. py:method:: get_composition_smart_repository_session(repository_id, proxy):
        :noindex:


    .. py:method:: get_repository_lookup_session(proxy):
        :noindex:


    .. py:method:: get_repository_query_session(proxy):
        :noindex:


    .. py:method:: get_repository_search_session(proxy):
        :noindex:


    .. py:method:: get_repository_admin_session(proxy):
        :noindex:


    .. py:method:: get_repository_notification_session(repository_receiver, proxy):
        :noindex:


    .. py:method:: get_repository_hierarchy_session(proxy):
        :noindex:


    .. py:method:: get_repository_hierarchy_design_session(proxy):
        :noindex:


    .. py:method:: get_repository_batch_proxy_manager():
        :noindex:


    .. py:attribute:: repository_batch_proxy_manager
        :noindex:


    .. py:method:: get_repository_rules_proxy_manager():
        :noindex:


    .. py:attribute:: repository_rules_proxy_manager
        :noindex:




Asset Repository Methods
------------------------

    .. py:method:: can_lookup_asset_repository_mappings():
        Tests if this user can perform lookups of asset/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_repository_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_repository_view():
        A complete view of the ``Asset`` and ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_asset_ids_by_repository(repository_id):
        Gets the list of ``Asset``  ``Ids`` associated with a ``Repository``.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.id.IdList) - list of related asset ``Ids``
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_repository(repository_id):
        Gets the list of ``Assets`` associated with a ``Repository``.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.repository.AssetList) - list of related assets
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_asset_ids_by_repositories(repository_ids):
        Gets the list of ``Asset Ids`` corresponding to a list of ``Repository`` objects.

        :arg:    repository_ids (osid.id.IdList): list of repository
                ``Ids``
        :return: (osid.id.IdList) - list of asset ``Ids``
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_repositories(repository_ids):
        Gets the list of ``Assets`` corresponding to a list of ``Repository`` objects.

        :arg:    repository_ids (osid.id.IdList): list of repository
                ``Ids``
        :return: (osid.repository.AssetList) - list of assets
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_ids_by_asset(asset_id):
        Gets the list of ``Repository``  ``Ids`` mapped to an ``Asset``.

        :arg:    asset_id (osid.id.Id): ``Id`` of an ``Asset``
        :return: (osid.id.IdList) - list of repository ``Ids``
        :raises:  NotFound - ``asset_id`` is not found
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_asset(asset_id):
        Gets the list of ``Repository`` objects mapped to an ``Asset``.

        :arg:    asset_id (osid.id.Id): ``Id`` of an ``Asset``
        :return: (osid.repository.RepositoryList) - list of repositories
        :raises:  NotFound - ``asset_id`` is not found
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Asset Repository Assignment Methods
-----------------------------------

    .. py:method:: can_assign_assets():
        Tests if this user can alter asset/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_assets_to_repository(repository_id):
        Tests if this user can alter asset/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``repository_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_repository_ids(repository_id):
        Gets a list of repositories including and under the given repository node in which any asset
            can be assigned.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (osid.id.IdList) - list of assignable repository ``Ids``
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_repository_ids_for_asset(repository_id, asset_id):
        Gets a list of repositories including and under the given repository node in which a
            specific asset can be assigned.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset``
        :return: (osid.id.IdList) - list of assignable repository ``Ids``
        :raises:  NullArgument - ``repository_id`` or ``asset_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_asset_to_repository(asset_id, repository_id):
        Adds an existing ``Asset`` to a ``Repository``.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset``
        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :raises:  AlreadyExists - ``asset_id`` already assigned to
                ``repository_id``
        :raises:  NotFound - ``asset_id`` or ``repository_id`` not found
        :raises:  NullArgument - ``asset_id`` or ``repository_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_asset_from_repository(asset_id, repository_id):
        Removes an ``Asset`` from a ``Repository``.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset``
        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :raises:  NotFound - ``asset_id`` or ``repository_id`` not found
                or ``asset_id`` not assigned to ``repository_id``
        :raises:  NullArgument - ``asset_id`` or ``repository_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Composition Repository Methods
------------------------------

    .. py:method:: use_comparative_composition_repository_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_composition_repository_view():
        A complete view of the ``Composition`` and ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: can_lookup_composition_repository_mappings():
        Tests if this user can perform lookups of composition/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: (boolean) - ``false`` if looking up mappings is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_composition_ids_by_repository(repository_id):
        Gets the list of ``Composition``  ``Ids`` associated with a ``Repository``.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.id.IdList) - list of related composition ``Ids``
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compositions_by_repository(repository_id):
        Gets the list of ``Compositions`` associated with a ``Repository``.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.repository.CompositionList) - list of related
                compositions
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_composition_ids_by_repositories(repository_ids):
        Gets the list of ``Composition``  ``Ids`` corresponding to a list of ``Repository`` objects.

        :arg:    repository_ids (osid.id.IdList): list of repository
                ``Ids``
        :return: (osid.id.IdList) - list of composition ``Ids``
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compoitions_by_repositories(repository_ids):
        Gets the list of ``Compositions`` corresponding to a list of ``Repository`` objects.

        :arg:    repository_ids (osid.id.IdList): list of repository
                ``Ids``
        :return: (osid.repository.CompositionList) - list of Compositions
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_ids_by_composition(composition_id):
        Gets the ``Repository``  ``Ids`` mapped to a ``Composition``.

        :arg:    composition_id (osid.id.Id): ``Id`` of a ``Composition``
        :return: (osid.id.IdList) - list of repository ``Ids``
        :raises:  NotFound - ``composition_id`` is not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_composition(composition_id):
        Gets the ``Repository`` objects mapped to a ``Composition``.

        :arg:    composition_id (osid.id.Id): ``Id`` of a ``Composition``
        :return: (osid.repository.RepositoryList) - list of repositories
        :raises:  NotFound - ``composition_id`` is not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Composition Repository Assignment Methods
-----------------------------------------

    .. py:method:: can_assign_compositions():
        Tests if this user can alter composition/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_assign_compositions_to_repository(repository_id):
        Tests if this user can alter composition/repository mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (boolean) - ``false`` if mapping is not authorized,
                ``true`` otherwise
        :raises:  NullArgument - ``repository_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_repository_ids(repository_id):
        Gets a list of repositories including and under the given repository node in which any
            composition can be assigned.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (osid.id.IdList) - list of assignable repository ``Ids``
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assignable_repository_ids_for_composition(repository_id, composition_id):
        Gets a list of repositories including and under the given repository node in which a
            specific composition can be assigned.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition``
        :return: (osid.id.IdList) - list of assignable repository ``Ids``
        :raises:  NullArgument - ``repository_id`` or ``composition_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: assign_composition_to_repository(composition_id, repository_id):
        Adds an existing ``Composition`` to a ``Repository``.

        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition``
        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :raises:  AlreadyExists - ``composition_id`` already assigned to
                ``repository_id``
        :raises:  NotFound - ``composition_id`` or ``repository_id`` not
                found
        :raises:  NullArgument - ``composition_id`` or ``repository_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: unassign_composition_from_repository(composition_id, repository_id):
        Removes ``Composition`` from a ``Repository``.

        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition``
        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :raises:  NotFound - ``composition_id`` or ``repository_id`` not
                found or ``composition_id`` not assigned to
                ``repository_id``
        :raises:  NullArgument - ``composition_id`` or ``repository_id``
                is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Repository Lookup Methods
-------------------------

    .. py:method:: can_lookup_repositories():
        Tests if this user can perform ``Repository`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_repository_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_repository_view():
        A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_repository(repository_id):
        Gets the ``Repository`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Repository`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Repository`` and retained
        for compatibility.

        :arg:    repository_id (osid.id.Id): ``Id`` of the ``Repository``
        :return: (osid.repository.Repository) - the repository
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_repositories_by_ids(repository_ids):
        Gets a ``RepositoryList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the
        repositories specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Repositories`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :arg:    repository_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NotFound - an ``Id`` was not found
        :raises:  NullArgument - ``repository_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_genus_type(repository_genus_type):
        Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` which does
            not include repositories of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :arg:    repository_genus_type (osid.type.Type): a repository
                genus type
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NullArgument - ``repository_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_parent_genus_type(repository_genus_type):
        Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` and include
            any additional repositories with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :arg:    repository_genus_type (osid.type.Type): a repository
                genus type
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NullArgument - ``repository_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_record_type(repository_record_type):
        Gets a ``RepositoryList`` containing the given repository record ``Type``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :arg:    repository_record_type (osid.type.Type): a repository
                record type
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NullArgument - ``repository_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories_by_provider(resource_id):
        Gets a ``RepositoryList`` from the given provider ````.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.repository.RepositoryList) - the returned
                ``Repository list``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repositories():
        Gets all ``Repositories``.

        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.

        :return: (osid.repository.RepositoryList) - a list of
                ``Repositories``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repositories




Repository Query Methods
------------------------

    .. py:method:: can_search_repositories():
        Tests if this user can perform ``Repository`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_query():
        Gets a repository query.

        :return: (osid.repository.RepositoryQuery) - the repository query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_query


    .. py:method:: get_repositories_by_query(repository_query):
        Gets a list of ``Repositories`` matching the given repository query.

        :arg:    repository_query (osid.repository.RepositoryQuery): the
                repository query
        :return: (osid.repository.RepositoryList) - the returned
                ``RepositoryList``
        :raises:  NullArgument - ``repository_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``repository_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Repository Admin Methods
------------------------

    .. py:method:: can_create_repositories():
        Tests if this user can create ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Repository`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_repository_with_record_types(repository_record_types):
        Tests if this user can create a single ``Repository`` using the desired record types.

        While ``RepositoryManager.getRepositoryRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Repository``. Providing an empty array tests if a
        ``Repository`` can be created with no records.

        :arg:    repository_record_types (osid.type.Type[]): array of
                repository record types
        :return: (boolean) - ``true`` if ``Repository`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``repository_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_form_for_create(repository_record_types):
        Gets the repository form for creating new repositories.

        A new form should be requested for each create transaction.

        :arg:    repository_record_types (osid.type.Type[]): array of
                repository record types
        :return: (osid.repository.RepositoryForm) - the repository form
        :raises:  NullArgument - ``repository_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_repository(repository_form):
        Creates a new ``Repository``.

        :arg:    repository_form (osid.repository.RepositoryForm): the
                form for this ``Repository``
        :return: (osid.repository.Repository) - the new ``Repository``
        :raises:  IllegalState - ``repository_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``repository_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``repository_form`` did not originate from
                ``get_repository_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_repositories():
        Tests if this user can update ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Repository`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_form_for_update(repository_id):
        Gets the repository form for updating an existing repository.

        A new repository form should be requested for each update
        transaction.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository``
        :return: (osid.repository.RepositoryForm) - the repository form
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_repository(repository_form):
        Updates an existing repository.

        :arg:    repository_form (osid.repository.RepositoryForm): the
                form containing the elements to be updated
        :raises:  IllegalState - ``repository_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``repository_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``repository_form`` did not originate from
                ``get_repository_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_repositories():
        Tests if this user can delete ``Repositories``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Repository`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_repository(repository_id):
        Deletes a ``Repository``.

        :arg:    repository_id (osid.id.Id): the ``Id`` of the
                ``Repository`` to remove
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_repository_aliases():
        Tests if this user can manage ``Id`` aliases for repositories.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Repository`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_repository(repository_id, alias_id):
        Adds an ``Id`` to a ``Repository`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Repository`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another repository, it is reassigned
        to the given repository ``Id``.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a
                ``Repository``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Repository Hierarchy Methods
----------------------------

    .. py:method:: get_repository_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_hierarchy_id


    .. py:method:: get_repository_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_hierarchy


    .. py:method:: can_access_repository_hierarchy():
        Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if hierarchy traversal methods are
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_repository_view():
        The returns from the repository methods may omit or translate elements based on this
            session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_repository_view():
        A complete view of the ``Repository`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_root_repository_ids():
        Gets the root repository ``Ids`` in this hierarchy.

        :return: (osid.id.IdList) - the root repository ``Ids``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: root_repository_ids


    .. py:method:: get_root_repositories():
        Gets the root repositories in the repository hierarchy.

        A node with no parents is an orphan. While all repository
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.

        :return: (osid.repository.RepositoryList) - the root repositories
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:attribute:: root_repositories


    .. py:method:: has_parent_repositories(repository_id):
        Tests if the ``Repository`` has any parents.

        :arg:    repository_id (osid.id.Id): a repository ``Id``
        :return: (boolean) - ``true`` if the repository has parents,
                ``false`` otherwise
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_parent_of_repository(id_, repository_id):
        Tests if an ``Id`` is a direct parent of a repository.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :return: (boolean) - ``true`` if this ``id`` is a parent of
                ``repository_id,``  ``false`` otherwise
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``id`` or ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_parent_repository_ids(repository_id):
        Gets the parent ``Ids`` of the given repository.

        :arg:    repository_id (osid.id.Id): a repository ``Id``
        :return: (osid.id.IdList) - the parent ``Ids`` of the repository
        :raises:  NotFound - ``repository_id`` is not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_parent_repositories(repository_id):
        Gets the parents of the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :return: (osid.repository.RepositoryList) - the parents of the
                repository
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_ancestor_of_repository(id_, repository_id):
        Tests if an ``Id`` is an ancestor of a repository.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    repository_id (osid.id.Id): the Id of a repository
        :return: (boolean) - ``true`` if this ``id`` is an ancestor of
                ``repository_id,``  ``false`` otherwise
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: has_child_repositories(repository_id):
        Tests if a repository has any children.

        :arg:    repository_id (osid.id.Id): a repository ``Id``
        :return: (boolean) - ``true`` if the ``repository_id`` has
                children, ``false`` otherwise
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_child_of_repository(id_, repository_id):
        Tests if a node is a direct child of another.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :return: (boolean) - ``true`` if the ``id`` is a child of
                ``repository_id,``  ``false`` otherwise
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.




    .. py:method:: get_child_repository_ids(repository_id):
        Gets the ``Ids`` of the children of the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :return: (osid.id.IdList) - the children of the repository
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_child_repositories(repository_id):
        Gets the children of the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :return: (osid.repository.RepositoryList) - the children of the
                repository
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: is_descendant_of_repository(id_, repository_id):
        Tests if an ``Id`` is a descendant of a repository.

        :arg:    id (osid.id.Id): an ``Id``
        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :return: (boolean) - ``true`` if the ``id`` is a descendant of
                the ``repository_id,`` ``false`` otherwise
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` or ``id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.




    .. py:method:: get_repository_node_ids(repository_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.hierarchy.Node) - the specified repository node
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_repository_nodes(repository_id, ancestor_levels, descendant_levels, include_siblings):
        Gets a portion of the hierarchy for the given repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` to query
        :arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        :arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        :arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        :return: (osid.repository.RepositoryNode) - the specified
                repository node
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Repository Hierarchy Design Methods
-----------------------------------

    .. py:method:: get_repository_hierarchy_id():
        Gets the hierarchy ``Id`` associated with this session.

        :return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_hierarchy_id


    .. py:method:: get_repository_hierarchy():
        Gets the hierarchy associated with this session.

        :return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_hierarchy


    .. py:method:: can_modify_repository_hierarchy():
        Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_root_repository(repository_id):
        Adds a root repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :raises:  AlreadyExists - ``repository_id`` is already in
                hierarchy
        :raises:  NotFound - ``repository_id`` not found
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_root_repository(repository_id):
        Removes a root repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :raises:  NotFound - ``repository_id`` not a root
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_child_repository(repository_id, child_id):
        Adds a child to a repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  AlreadyExists - ``repository_id`` is already a parent of
                ``child_id``
        :raises:  NotFound - ``repository_id`` or ``child_id`` not found
        :raises:  NullArgument - ``repository_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_repository(repository_id, child_id):
        Removes a child from a repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :arg:    child_id (osid.id.Id): the ``Id`` of the new child
        :raises:  NotFound - ``repository_id`` not a parent of
                ``child_id``
        :raises:  NullArgument - ``repository_id`` or ``child_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_child_repositories(repository_id):
        Removes all children from a repository.

        :arg:    repository_id (osid.id.Id): the ``Id`` of a repository
        :raises:  NotFound - ``repository_id`` not in hierarchy
        :raises:  NullArgument - ``repository_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






