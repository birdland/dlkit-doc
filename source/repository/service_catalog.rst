

Service Catalog
===============


Repository
----------

.. py:class:: Repository(abc_repository_objects.Repository, osid_objects.OsidCatalog)
    A repository defines a collection of assets.

    .. py:method:: get_repository_record(repository_record_type):
        :noindex:




Asset Lookup Methods
--------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_lookup_assets():
        Tests if this user can perform ``Asset`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_asset_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_asset_view():
        A complete view of the ``Asset`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_repository_view():
        Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_repository_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_asset(asset_id):
        Gets the ``Asset`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Asset`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Asset`` and retained for compatibility.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset`` to
                retrieve
        :return: (osid.repository.Asset) - the returned ``Asset``
        :raises:  NotFound - no ``Asset`` found with the given ``Id``
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_ids(asset_ids):
        Gets an ``AssetList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the assets
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assets`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :arg:    asset_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.repository.AssetList) - the returned ``Asset
                list``
        :raises:  NotFound - an ``Id`` was not found
        :raises:  NullArgument - ``asset_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_genus_type(asset_genus_type):
        Gets an ``AssetList`` corresponding to the given asset genus ``Type`` which does not include
            assets of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :arg:    asset_genus_type (osid.type.Type): an asset genus type
        :return: (osid.repository.AssetList) - the returned ``Asset
                list``
        :raises:  NullArgument - ``asset_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_parent_genus_type(asset_genus_type):
        Gets an ``AssetList`` corresponding to the given asset genus ``Type`` and include any
            additional assets with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :arg:    asset_genus_type (osid.type.Type): an asset genus type
        :return: (osid.repository.AssetList) - the returned ``Asset
                list``
        :raises:  NullArgument - ``asset_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_record_type(asset_record_type):
        Gets an ``AssetList`` containing the given asset record ``Type``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :arg:    asset_record_type (osid.type.Type): an asset record type
        :return: (osid.repository.AssetList) - the returned ``Asset
                list``
        :raises:  NullArgument - ``asset_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets_by_provider(resource_id):
        Gets an ``AssetList`` from the given provider.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.repository.AssetList) - the returned ``Asset
                list``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_assets():
        Gets all ``Assets``.

        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.

        :return: (osid.repository.AssetList) - a list of ``Assets``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: assets




Asset Query Methods
-------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_search_assets():
        Tests if this user can perform ``Asset`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_repository_view():
        Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_repository_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_asset_query():
        Gets an asset query.

        :return: (osid.repository.AssetQuery) - the asset query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: asset_query


    .. py:method:: get_assets_by_query(asset_query):
        Gets a list of ``Assets`` matching the given asset query.

        :arg:    asset_query (osid.repository.AssetQuery): the asset
                query
        :return: (osid.repository.AssetList) - the returned ``AssetList``
        :raises:  NullArgument - ``asset_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - the ``asset_query`` is not of this service
        *compliance: mandatory -- This method must be implemented.*






Asset Search Methods
--------------------

    .. py:method:: get_asset_search():
        Gets an asset search.

        :return: (osid.repository.AssetSearch) - the asset search
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: asset_search


    .. py:method:: get_asset_search_order():
        Gets an asset search order.

        The ``AssetSearchOrder`` is supplied to an ``AssetSearch`` to
        specify the ordering of results.

        :return: (osid.repository.AssetSearchOrder) - the asset search
                order
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: asset_search_order


    .. py:method:: get_assets_by_search(asset_query, asset_search):
        Gets the search results matching the given search query using the given search.

        :arg:    asset_query (osid.repository.AssetQuery): the asset
                query
        :arg:    asset_search (osid.repository.AssetSearch): the asset
                search
        :return: (osid.repository.AssetSearchResults) - the asset search
                results
        :raises:  NullArgument - ``asset_query`` or ``asset_search`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``asset_query`` or ``asset_search`` is not
                of this service
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_asset_query_from_inspector(asset_query_inspector):
        Gets an asset query from an inspector.

        The inspector is available from a ``AssetSearchResults``.

        :arg:    asset_query_inspector
                (osid.repository.AssetQueryInspector): an asset query
                inspector
        :return: (osid.repository.AssetQuery) - the asset query
        :raises:  NullArgument - ``asset_query_inspector`` is ``null``
        :raises:  Unsupported - ``asset_query_inspector`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Asset Admin Methods
-------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_create_assets():
        Tests if this user can create ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Asset`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_asset_with_record_types(asset_record_types):
        Tests if this user can create a single ``Asset`` using the desired record types.

        While ``RepositoryManager.getAssetRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Asset``.
        Providing an empty array tests if an ``Asset`` can be created
        with no records.

        :arg:    asset_record_types (osid.type.Type[]): array of asset
                record types
        :return: (boolean) - ``true`` if ``Asset`` creation using the
                specified record ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``asset_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_asset_form_for_create(asset_record_types):
        Gets the asset form for creating new assets.

        A new form should be requested for each create transaction.

        :arg:    asset_record_types (osid.type.Type[]): array of asset
                record types
        :return: (osid.repository.AssetForm) - the asset form
        :raises:  NullArgument - ``asset_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_asset(asset_form):
        Creates a new ``Asset``.

        :arg:    asset_form (osid.repository.AssetForm): the form for
                this ``Asset``
        :return: (osid.repository.Asset) - the new ``Asset``
        :raises:  IllegalState - ``asset_form`` already used in a create
                transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``asset_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``asset_form`` did not originate from
                ``get_asset_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_assets():
        Tests if this user can update ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Asset`` modification is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_asset_form_for_update(asset_id):
        Gets the asset form for updating an existing asset.

        A new asset form should be requested for each update
        transaction.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset``
        :return: (osid.repository.AssetForm) - the asset form
        :raises:  NotFound - ``asset_id`` is not found
        :raises:  NullArgument - ``asset_id`` is null
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_asset(asset_form):
        Updates an existing asset.

        :arg:    asset_form (osid.repository.AssetForm): the form
                containing the elements to be updated
        :raises:  IllegalState - ``asset_form`` already used in anupdate
                transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``asset_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``asset_form`` did not originate from
                ``get_asset_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_assets():
        Tests if this user can delete ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Asset`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_asset(asset_id):
        Deletes an ``Asset``.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset`` to
                remove
        :raises:  NotFound - ``asset_id`` not found
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_asset_aliases():
        Tests if this user can manage ``Id`` aliases for ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Asset`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_asset(asset_id, alias_id):
        Adds an ``Id`` to an ``Asset`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Asset`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another asset, it is
        reassigned to the given asset ``Id``.

        :arg:    asset_id (osid.id.Id): the ``Id`` of an ``Asset``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is already assigned
        :raises:  NotFound - ``asset_id`` not found
        :raises:  NullArgument - ``asset_id`` or ``alias_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_asset_content():
        Tests if this user can create content for ``Assets``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Asset`` content creation is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_asset_content_with_record_types(asset_content_record_types):
        Tests if this user can create an ``AssetContent`` using the desired record types.

        While ``RepositoryManager.getAssetContentRecordTypes()`` can be
        used to test which records are supported, this method tests
        which records are required for creating a specific
        ``AssetContent``. Providing an empty array tests if an
        ``AssetContent`` can be created with no records.

        :arg:    asset_content_record_types (osid.type.Type[]): array of
                asset content record types
        :return: (boolean) - ``true`` if ``AssetContent`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``asset_content_record_types`` is
                ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_asset_content_form_for_create(asset_id, asset_content_record_types):
        Gets an asset content form for creating new assets.

        :arg:    asset_id (osid.id.Id): the ``Id`` of an ``Asset``
        :arg:    asset_content_record_types (osid.type.Type[]): array of
                asset content record types
        :return: (osid.repository.AssetContentForm) - the asset content
                form
        :raises:  NotFound - ``asset_id`` is not found
        :raises:  NullArgument - ``asset_id`` or
                ``asset_content_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_asset_content(asset_content_form):
        Creates new ``AssetContent`` for a given asset.

        :arg:    asset_content_form (osid.repository.AssetContentForm):
                the form for this ``AssetContent``
        :return: (osid.repository.AssetContent) - the new
                ``AssetContent``
        :raises:  IllegalState - ``asset_content_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``asset_content_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``asset_content_form`` did not originate
                from ``get_asset_content_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_asset_contents():
        Tests if this user can update ``AssetContent``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``AssetContent`` modification
                is not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_asset_content_form_for_update(asset_content_id):
        Gets the asset content form for updating an existing asset content.

        A new asset content form should be requested for each update
        transaction.

        :arg:    asset_content_id (osid.id.Id): the ``Id`` of the
                ``AssetContent``
        :return: (osid.repository.AssetContentForm) - the asset content
                form
        :raises:  NotFound - ``asset_content_id`` is not found
        :raises:  NullArgument - ``asset_content_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_asset_content(asset_content_form):
        Updates an existing asset content.

        :arg:    asset_content_form (osid.repository.AssetContentForm):
                the form containing the elements to be updated
        :raises:  IllegalState - ``asset_content_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``asset_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``asset_content_form`` did not originate
                from ``get_asset_content_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_asset_contents():
        Tests if this user can delete ``AssetsContents``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``AssetContent`` deletion is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_asset_content(asset_content_id):
        Deletes content from an ``Asset``.

        :arg:    asset_content_id (osid.id.Id): the ``Id`` of the
                ``AssetContent``
        :raises:  NotFound - ``asset_content_id`` is not found
        :raises:  NullArgument - ``asset_content_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Asset Notification Methods
--------------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_register_for_asset_notifications():
        Tests if this user can register for ``Asset`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: (boolean) - ``false`` if notification methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_repository_view():
        Federates the view for methods in this session.

        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_repository_view():
        Isolates the view for methods in this session.

        An isolated view restricts notifications to this repository
        only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: register_for_new_assets():
        Register for notifications of new assets.

        ``AssetReceiver.newAssets()`` is invoked when a new ``Asset``
        appears in this repository.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_new_assets_by_genus_type(asset_genus_type):
        Registers for notification of new assets of the given asset genus type.

        ``AssetReceiver.newAssets()`` is invoked when an asset is
        appears in this repository.

        :arg:    asset_genus_type (osid.type.Type): the genus type of the
                ``Asset`` to monitor
        :raises:  NullArgument - ``asset_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_assets():
        Registers for notification of updated assets.

        ``AssetReceiver.changedAssets()`` is invoked when an asset in
        this repository is changed.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_assets_by_genus_type(asset_genus_type):
        Registers for notification of updated assets of the given asset genus type.

        ``AssetReceiver.changedAssets()`` is invoked when an asset in
        this repository is changed.

        :arg:    asset_genus_type (osid.type.Type): the genus type of the
                ``Asset`` to monitor
        :raises:  NullArgument - ``asset_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_changed_asset(asset_id):
        Registers for notification of an updated asset.

        ``AssetReceiver.changedAssets()`` is invoked when the specified
        asset in this repository is changed.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset`` to
                monitor
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_assets():
        Registers for notification of deleted assets.

        ``AssetReceiver.deletedAssets()`` is invoked when an asset is
        deleted or removed from this repository.

        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_assets_by_genus_type(asset_genus_type):
        Registers for notification of deleted assets of the given asset genus type.

        ``AssetReceiver.deletedAssets()`` is invoked when an asset is
        deleted or removed from this repository.

        :arg:    asset_genus_type (osid.type.Type): the genus type of the
                ``Asset`` to monitor
        :raises:  NullArgument - ``asset_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: register_for_deleted_asset(asset_id):
        Registers for notification of a deleted asset.

        ``AssetReceiver.deletedAssets()`` is invoked when the specified
        asset is deleted or removed from this repository.

        :arg:    asset_id (osid.id.Id): the ``Id`` of the ``Asset`` to
                monitor
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: reliable_asset_notifications():
        Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: unreliable_asset_notifications():
        Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: acknowledge_asset_notification(notification_id):
        Acknowledge an asset notification.

        :arg:    notification_id (osid.id.Id): the ``Id`` of the
                notification
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Asset Composition Methods
-------------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_access_asset_compositions():
        Tests if this user can perform composition lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_asset_composition_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_asset_composition_view():
        A complete view of the returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_repository_view():
        Federates the view for methods in this session.

        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_repository_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_composition_assets(composition_id):
        Gets the list of assets mapped to the given ``Composition``.

        :arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        :return: (osid.repository.AssetList) - list of assets
        :raises:  NotFound - ``composition_id`` not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_compositions_by_asset(asset_id):
        Gets a list of compositions including the given asset.

        :arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        :return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        :raises:  NotFound - ``asset_id`` is not found
        :raises:  NullArgument - ``asset_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






Asset Composition Design Methods
--------------------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_compose_assets():
        Tests if this user can manage mapping of ``Assets`` to ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as an application hint that may opt not to offer composition
        operations.

        :return: (boolean) - ``false`` if asset composiion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_asset(asset_id, composition_id):
        Appends an asset to a composition.

        :arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        :arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        :raises:  AlreadyExists - ``asset_id`` already part
                ``composition_id``
        :raises:  NotFound - ``asset_id`` or ``composition_id`` not found
        :raises:  NullArgument - ``asset_id`` or ``composition_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: move_asset_ahead(asset_id, composition_id, reference_id):
        Reorders assets in a composition by moving the specified asset in front of a reference
            asset.

        :arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        :arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        :arg:    reference_id (osid.id.Id): ``Id`` of the reference
                ``Asset``
        :raises:  NotFound - ``asset_id`` or ``reference_id``  ``not found
                in composition_id``
        :raises:  NullArgument - ``asset_id, reference_id`` or
                ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: move_asset_behind(asset_id, composition_id, reference_id):
        Reorders assets in a composition by moving the specified asset behind of a reference asset.

        :arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        :arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        :arg:    reference_id (osid.id.Id): ``Id`` of the reference
                ``Asset``
        :raises:  NotFound - ``asset_id`` or ``reference_id``  ``not found
                in composition_id``
        :raises:  NullArgument - ``asset_id, reference_id`` or
                ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: order_assets(asset_ids, composition_id):
        Reorders a set of assets in a composition.

        :arg:    asset_ids (osid.id.Id[]): ``Ids`` for a set of
                ``Assets``
        :arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        :raises:  NotFound - ``composition_id`` not found or, an
                ``asset_id`` not related to ``composition_id``
        :raises:  NullArgument - ``instruction_ids`` or ``agenda_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_asset(asset_id, composition_id):
        Removes an ``Asset`` from a ``Composition``.

        :arg:    asset_id (osid.id.Id): ``Id`` of the ``Asset``
        :arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composition``
        :raises:  NotFound - ``asset_id``  ``not found in composition_id``
        :raises:  NullArgument - ``asset_id`` or ``composition_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization fauilure
        *compliance: mandatory -- This method must be implemented.*






Composition Lookup Methods
--------------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_lookup_compositions():
        Tests if this user can perform ``Composition`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_comparative_composition_view():
        The returns from the lookup methods may omit or translate elements based on this session,
            such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_plenary_composition_view():
        A complete view of the ``Composition`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_federated_repository_view():
        Federates the view for methods in this session.

        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_repository_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_active_composition_view():
        Only active compositions are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_any_status_composition_view():
        All active and inactive compositions are returned by methods in this session.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_sequestered_composition_view():
        The methods in this session omit sequestered compositions.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_unsequestered_composition_view():
        The methods in this session return all compositions, including sequestered compositions.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_composition(composition_id):
        Gets the ``Composition`` specified by its ``Id``.

        :arg:    composition_id (osid.id.Id): ``Id`` of the
                ``Composiiton``
        :return: (osid.repository.Composition) - the composition
        :raises:  NotFound - ``composition_id`` not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_compositions_by_ids(composition_ids):
        Gets a ``CompositionList`` corresponding to the given ``IdList``.

        :arg:    composition_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        :return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        :raises:  NotFound - an ``Id`` was not found
        :raises:  NullArgument - ``composition_ids`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compositions_by_genus_type(composition_genus_type):
        Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` which does
            not include compositions of types derived from the specified ``Type``.

        :arg:    composition_genus_type (osid.type.Type): a composition
                genus type
        :return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        :raises:  NullArgument - ``composition_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compositions_by_parent_genus_type(composition_genus_type):
        Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` and include
            any additional compositions with genus types derived from the specified ``Type``.

        :arg:    composition_genus_type (osid.type.Type): a composition
                genus type
        :return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        :raises:  NullArgument - ``composition_genus_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compositions_by_record_type(composition_record_type):
        Gets a ``CompositionList`` containing the given composition record ``Type``.

        :arg:    composition_record_type (osid.type.Type): a composition
                record type
        :return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        :raises:  NullArgument - ``composition_record_type`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compositions_by_provider(resource_id):
        Gets a ``CompositionList`` from the given provider ````.

        In plenary mode, the returned list contains all known
        compositions or an error results. Otherwise, the returned list
        may contain only those compositions that are accessible through
        this session.


        In sequestered mode, no sequestered compositions are returned.
        In unsequestered mode, all compositions are returned.

        :arg:    resource_id (osid.id.Id): a resource ``Id``
        :return: (osid.repository.CompositionList) - the returned
                ``Composition list``
        :raises:  NullArgument - ``resource_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_compositions():
        Gets all ``Compositions``.

        :return: (osid.repository.CompositionList) - a list of
                ``Compositions``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: compositions




Composition Query Methods
-------------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_search_compositions():
        Tests if this user can perform ``Composition`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: (boolean) - ``false`` if search methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: use_federated_repository_view():
        Federates the view for methods in this session.

        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_isolated_repository_view():
        Isolates the view for methods in this session.

        An isolated view restricts lookups to this repository only.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_sequestered_composition_view():
        The methods in this session omit sequestered compositions.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: use_unsequestered_composition_view():
        The methods in this session return all compositions, including sequestered compositions.

        *compliance: mandatory -- This method is must be implemented.*




    .. py:method:: get_composition_query():
        Gets a composition query.

        :return: (osid.repository.CompositionQuery) - the composition
                query
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: composition_query


    .. py:method:: get_compositions_by_query(composition_query):
        Gets a list of ``Compositions`` matching the given composition query.

        :arg:    composition_query (osid.repository.CompositionQuery):
                the composition query
        :return: (osid.repository.CompositionList) - the returned
                ``CompositionList``
        :raises:  NullArgument - ``composition_query`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``composition_query`` is not of this
                service
        *compliance: mandatory -- This method must be implemented.*






Composition Search Methods
--------------------------

    .. py:method:: get_composition_search():
        Gets a composition search.

        :return: (osid.repository.CompositionSearch) - the composition
                search
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: composition_search


    .. py:method:: get_composition_search_order():
        Gets a composition search order.

        The ``CompositionSearchOrder`` is supplied to an
        ``CompositionSearch`` to specify the ordering of results.

        :return: (osid.repository.CompositionSearchOrder) - the
                composition search order
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: composition_search_order


    .. py:method:: get_compositions_by_search(composition_query, composition_search):
        Gets the search results matching the given search query using the given search.

        :arg:    composition_query (osid.repository.CompositionQuery):
                the composition query
        :arg:    composition_search (osid.repository.CompositionSearch):
                the composition search
        :return: (osid.repository.CompositionSearchResults) - the
                composition search results
        :raises:  NullArgument - ``composition_query`` or
                ``composition_search`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``composition_query`` or
                ``composition_search`` is not of this service
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_composition_query_from_inspector(composition_query_inspector):
        Gets a composition query from an inspector.

        The inspector is available from a ``CompositionSearchResults``.

        :arg:    composition_query_inspector
                (osid.repository.CompositionQueryInspector): a
                composition query inspector
        :return: (osid.repository.CompositionQuery) - the composition
                query
        :raises:  NullArgument - ``composition_query_inspector`` is
                ``null``
        :raises:  Unsupported - ``composition_query_inspector`` is not of
                this service
        *compliance: mandatory -- This method must be implemented.*






Composition Admin Methods
-------------------------

    .. py:method:: get_repository_id():
        Gets the ``Repository``  ``Id`` associated with this session.

        :return: (osid.id.Id) - the ``Repository Id`` associated with
                this session
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository_id


    .. py:method:: get_repository():
        Gets the ``Repository`` associated with this session.

        :return: (osid.repository.Repository) - the ``Repository``
                associated with this session
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:attribute:: repository


    .. py:method:: can_create_compositions():
        Tests if this user can create ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Composition`` creation is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_create_composition_with_record_types(composition_record_types):
        Tests if this user can create a single ``Composition`` using the desired record types.

        While ``RepositoryManager.getCompositionRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Composition``. Providing an empty array tests if a
        ``Composition`` can be created with no records.

        :arg:    composition_record_types (osid.type.Type[]): array of
                composition record types
        :return: (boolean) - ``true`` if ``Composition`` creation using
                the specified ``Types`` is supported, ``false``
                otherwise
        :raises:  NullArgument - ``composition_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_composition_form_for_create(composition_record_types):
        Gets the composition form for creating new compositions.

        A new form should be requested for each create transaction.

        :arg:    composition_record_types (osid.type.Type[]): array of
                composition record types
        :return: (osid.repository.CompositionForm) - the composition form
        :raises:  NullArgument - ``composition_record_types`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: create_composition(composiiton_form):
        Creates a new ``Composition``.

        :arg:    composiiton_form (osid.repository.CompositionForm): the
                form for this ``Composition``
        :return: (osid.repository.Composition) - the new ``Composition``
        :raises:  IllegalState - ``composition_form`` already used in a
                create transaction
        :raises:  InvalidArgument - one or more of the form elements is
                invalid
        :raises:  NullArgument - ``composition_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``composition_form`` did not originate
                from ``get_composition_form_for_create()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_update_compositions():
        Tests if this user can update ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Composition`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: get_composition_form_for_update(composition_id):
        Gets the composition form for updating an existing composition.

        A new composition form should be requested for each update
        transaction.

        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition``
        :return: (osid.repository.CompositionForm) - the composition form
        :raises:  NotFound - ``composition_id`` is not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: update_composition(composiiton_form):
        Updates an existing composition.

        :arg:    composiiton_form (osid.repository.CompositionForm): the
                form containing the elements to be updated
        :raises:  IllegalState - ``composition_form`` already used in an
                update transaction
        :raises:  InvalidArgument - the form contains an invalid value
        :raises:  NullArgument - ``composition_form`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        :raises:  Unsupported - ``composition_form`` did not originate
                from ``get_composition_form_for_update()``
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_delete_compositions():
        Tests if this user can delete ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: (boolean) - ``false`` if ``Composition`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_composition(composition_id):
        Deletes a ``Composition``.

        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition`` to remove
        :raises:  NotFound - ``composition_id`` not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: delete_composition_node(composition_id):
        Deletes a ``Composition`` and all contained children.

        :arg:    composition_id (osid.id.Id): the ``Id`` of the
                ``Composition`` to remove
        :raises:  NotFound - ``composition_id`` not found
        :raises:  NullArgument - ``composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: add_composition_child(composition_id, child_composition_id):
        Adds a composition to a parent composition.

        :arg:    composition_id (osid.id.Id): the ``Id`` of a parent
                ``Composition``
        :arg:    child_composition_id (osid.id.Id): the ``Id`` of a child
                ``Composition``
        :raises:  AlreadyExists - ``child_composition_id`` is already a
                child of ``composition_id``
        :raises:  NotFound - ``composition_id`` or
                ``child_composition_id`` is not found
        :raises:  NullArgument - ``composition_id`` or
                ``child_composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: remove_composition_child(composition_id, child_composition_id):
        Removes a composition from a parent composition.

        :arg:    composition_id (osid.id.Id): the ``Id`` of a parent
                ``Composition``
        :arg:    child_composition_id (osid.id.Id): the ``Id`` of a child
                ``Composition``
        :raises:  NotFound - ``composition_id`` or
                ``child_composition_id`` is not found or not related
        :raises:  NullArgument - ``composition_id`` or
                ``child_composition_id`` is ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: can_manage_composition_aliases():
        Tests if this user can manage ``Id`` aliases for ``Compositions``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: (boolean) - ``false`` if ``Composition`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*




    .. py:method:: alias_composition(composition_id, alias_id):
        Adds an ``Id`` to a ``Composition`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Composition`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another composition, it is reassigned
        to the given composition ``Id``.

        :arg:    composition_id (osid.id.Id): the ``Id`` of a
                ``Composition``
        :arg:    alias_id (osid.id.Id): the alias ``Id``
        :raises:  AlreadyExists - ``alias_id`` is in use as a primary
                ``Id``
        :raises:  NotFound - ``composition_id`` not found
        :raises:  NullArgument - ``composition_id`` or ``alias_id`` is
                ``null``
        :raises:  OperationFailed - unable to complete request
        :raises:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*






