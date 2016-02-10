
from ..osid import sessions as osid_sessions


class AssetLookupSession(osid_sessions.OsidSession):
    """This session defines methods for retrieving assets.


    An ``Asset`` represents an element of content stored in a
    Repository.




    This lookup session defines several views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated repository view: All asset methods in this session
        operate, retrieve and pertain to assets defined explicitly in
        the current repository. Using an isolated view is useful for
        managing ``Assets`` with the ``AssetAdminSession.``
      * federated repository view: All asset methods in this session
        operate, retrieve and pertain to all assets defined in this
        repository and any other assets implicitly available in this
        repository through repository inheritence.








    The methods ``use_federated_repository_view()`` and
    ``use_isolated_repository_view()`` behave as a radio group and one
    should be selected before invoking any lookup methods.




    Assets may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Asset``.


    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_lookup_assets(self):
        """Tests if this user can perform ``Asset`` lookups.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_comparative_asset_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_asset_view(self):
        """A complete view of the ``Asset`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.


        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this repository only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_asset(self, asset_id):
        """Gets the ``Asset`` specified by its ``Id``.


        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Asset`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Asset`` and retained for compatibility.


        :param asset_id: the ``Id`` of the ``Asset`` to retrieve
        :type asset_id: ``osid.id.Id``
        :return: the returned ``Asset``
        :rtype: ``osid.repository.Asset``
        :raise: ``NotFound`` -- no ``Asset`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Asset

    def get_assets_by_ids(self, asset_ids):
        """Gets an ``AssetList`` corresponding to the given ``IdList``.


        In plenary mode, the returned list contains all of the assets
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Assets`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.


        :param asset_ids: the list of ``Ids`` to retrieve
        :type asset_ids: ``osid.id.IdList``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``asset_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    def get_assets_by_genus_type(self, asset_genus_type):
        """Gets an ``AssetList`` corresponding to the given asset genus ``Type`` which does not include assets of types
            derived from the specified ``Type``.


        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.


        :param asset_genus_type: an asset genus type
        :type asset_genus_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    def get_assets_by_parent_genus_type(self, asset_genus_type):
        """Gets an ``AssetList`` corresponding to the given asset genus ``Type`` and include any additional assets with
            genus types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.


        :param asset_genus_type: an asset genus type
        :type asset_genus_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    def get_assets_by_record_type(self, asset_record_type):
        """Gets an ``AssetList`` containing the given asset record ``Type``.


        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.


        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    def get_assets_by_provider(self, resource_id):
        """Gets an ``AssetList`` from the given provider.


        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Asset list``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    def get_assets(self):
        """Gets all ``Assets``.


        In plenary mode, the returned list contains all known assets or
        an error results. Otherwise, the returned list may contain only
        those assets that are accessible through this session.


        :return: a list of ``Assets``
        :rtype: ``osid.repository.AssetList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    assets = property(fget=get_assets)


class AssetQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Asset`` objects.


    The search query is constructed using the ``AssetQuery``.




    This session defines views that offer differing behaviors for
    searching.




      * federated repository view: searches include assets in
        repositories of which this repository is a ancestor in the
        repository hierarchy
      * isolated repository view: searches are restricted to assets in
        this repository








    Assets may have a query record indicated by their respective record
    types. The query record is accessed via the ``AssetQuery``.


    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_search_assets(self):
        """Tests if this user can perform ``Asset`` searches.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.


        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this repository only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_asset_query(self):
        """Gets an asset query.


        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetQuery

    asset_query = property(fget=get_asset_query)

    def get_assets_by_query(self, asset_query):
        """Gets a list of ``Assets`` matching the given asset query.


        :param asset_query: the asset query
        :type asset_query: ``osid.repository.AssetQuery``
        :return: the returned ``AssetList``
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``asset_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- the ``asset_query`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList


class AssetSearchSession(AssetQuerySession):
    """This session provides methods for searching among ``Asset`` objects.


    The search query is constructed using the ``AssetQuery``.




    ``get_assets_by_query()`` is the basic search method and returns a
    list of ``Assets``. A more advanced search may be performed with
    ``getAssetsBySearch()``. It accepts an ``AssetSearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_assets_by_search()`` returns an ``AssetSearchResults`` that
    can be used to access the resulting ``AssetList`` or be used to
    perform a search within the result set through ``AssetList``.




    This session defines views that offer differing behaviors for
    searching.




      * federated repository view: searches include assets in
        repositories of which this repository is a ancestor in the
        repository hierarchy
      * isolated repository view: searches are restricted to assets in
        this repository








    Assets may have a query record indicated by their respective record
    types. The query record is accessed via the ``AssetQuery``.


    """

    def get_asset_search(self):
        """Gets an asset search.


        :return: the asset search
        :rtype: ``osid.repository.AssetSearch``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetSearch

    asset_search = property(fget=get_asset_search)

    def get_asset_search_order(self):
        """Gets an asset search order.


        The ``AssetSearchOrder`` is supplied to an ``AssetSearch`` to
        specify the ordering of results.


        :return: the asset search order
        :rtype: ``osid.repository.AssetSearchOrder``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetSearchOrder

    asset_search_order = property(fget=get_asset_search_order)

    def get_assets_by_search(self, asset_query, asset_search):
        """Gets the search results matching the given search query using the given search.


        :param asset_query: the asset query
        :type asset_query: ``osid.repository.AssetQuery``
        :param asset_search: the asset search
        :type asset_search: ``osid.repository.AssetSearch``
        :return: the asset search results
        :rtype: ``osid.repository.AssetSearchResults``
        :raise: ``NullArgument`` -- ``asset_query`` or ``asset_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_query`` or ``asset_search`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetSearchResults

    def get_asset_query_from_inspector(self, asset_query_inspector):
        """Gets an asset query from an inspector.


        The inspector is available from a ``AssetSearchResults``.


        :param asset_query_inspector: an asset query inspector
        :type asset_query_inspector: ``osid.repository.AssetQueryInspector``
        :return: the asset query
        :rtype: ``osid.repository.AssetQuery``
        :raise: ``NullArgument`` -- ``asset_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``asset_query_inspector`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetQuery


class AssetAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Assets``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create an
    ``Asset,`` an ``AssetForm`` is requested using
    ``get_asset_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``AssetyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``AssetForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``AssetForm`` corresponds
    to an attempted transaction.




    For updates, ``AssetForms`` are requested to the ``Asset``  ``Id``
    that is to be updated using ``getAssetFormForUpdate()``. Similarly,
    the ``AssetForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``AssetForm`` can only be used once for a successful update and
    cannot be reused.




    The delete operations delete ``Assets``. To unmap an ``Asset`` from
    the current ``Repository,`` the ``AssetRepositoryAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Bid`` itself thus removing it from all known ``Repository``
    catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.




    The view of the administrative methods defined in this session is
    determined by the provider. For an instance of this session where no
    repository has been specified, it may not be parallel to the
    ``AssetLookupSession``. For example, a default
    ``AssetLookupSession`` may view the entire repository hierarchy
    while the default ``AssetAdminSession`` uses an isolated
    ``Repository`` to create new ``Assets`` ora specific repository to
    operate on a predetermined set of ``Assets``. Another scenario is a
    federated provider who does not wish to permit administrative
    operations for the federation unaware.




    Example create:
      if (!session.canCreateAssets()) {
          return "asset creation not permitted";
      }




      Type types[1];
      types[0] = assetPhotographType;
      if (!session.canCreateAssetWithRecordTypes(types)) {
          return "creating an asset with a photograph type is not supported";
      }




      AssetForm form = session.getAssetFormForCreate();
      Metadata metadata = form.getDisplayNameMetadata();
      if (metadata.isReadOnly()) {
          return "cannot set display name";
      }




      form.setDisplayName("my photo");




      PhotographRecordForm photoForm = (PhotographRecordForn) form.getRecordForm(assetPhotogaphType);
      Metadata metadata = form.getApertureMetadata();
      if (metadata.isReadOnly()) {
          return ("cannot set aperture");
      }




      photoForm.setAperture("5.6");
      if (!form.isValid()) {
          return form.getValidationMessage();
      }




      Asset newAsset = session.createAsset(form);






    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_create_assets(self):
        """Tests if this user can create ``Assets``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.


        :return: ``false`` if ``Asset`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_create_asset_with_record_types(self, asset_record_types):
        """Tests if this user can create a single ``Asset`` using the desired record types.


        While ``RepositoryManager.getAssetRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Asset``.
        Providing an empty array tests if an ``Asset`` can be created
        with no records.


        :param asset_record_types: array of asset record types
        :type asset_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Asset`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_asset_form_for_create(self, asset_record_types):
        """Gets the asset form for creating new assets.


        A new form should be requested for each create transaction.


        :param asset_record_types: array of asset record types
        :type asset_record_types: ``osid.type.Type[]``
        :return: the asset form
        :rtype: ``osid.repository.AssetForm``
        :raise: ``NullArgument`` -- ``asset_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetForm

    def create_asset(self, asset_form):
        """Creates a new ``Asset``.


        :param asset_form: the form for this ``Asset``
        :type asset_form: ``osid.repository.AssetForm``
        :return: the new ``Asset``
        :rtype: ``osid.repository.Asset``
        :raise: ``IllegalState`` -- ``asset_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_form`` did not originate from ``get_asset_form_for_create()``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Asset

    def can_update_assets(self):
        """Tests if this user can update ``Assets``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.


        :return: ``false`` if ``Asset`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_asset_form_for_update(self, asset_id):
        """Gets the asset form for updating an existing asset.


        A new asset form should be requested for each update
        transaction.


        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: the asset form
        :rtype: ``osid.repository.AssetForm``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is null
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetForm

    def update_asset(self, asset_form):
        """Updates an existing asset.


        :param asset_form: the form containing the elements to be updated
        :type asset_form: ``osid.repository.AssetForm``
        :raise: ``IllegalState`` -- ``asset_form`` already used in anupdate transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_form`` did not originate from ``get_asset_form_for_update()``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_delete_assets(self):
        """Tests if this user can delete ``Assets``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Asset``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.


        :return: ``false`` if ``Asset`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def delete_asset(self, asset_id):
        """Deletes an ``Asset``.


        :param asset_id: the ``Id`` of the ``Asset`` to remove
        :type asset_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_manage_asset_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Assets``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Asset`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def alias_asset(self, asset_id, alias_id):
        """Adds an ``Id`` to an ``Asset`` for the purpose of creating compatibility.


        The primary ``Id`` of the ``Asset`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another asset, it is
        reassigned to the given asset ``Id``.


        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``asset_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_create_asset_content(self):
        """Tests if this user can create content for ``Assets``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.


        :return: ``false`` if ``Asset`` content creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_create_asset_content_with_record_types(self, asset_content_record_types):
        """Tests if this user can create an ``AssetContent`` using the desired record types.


        While ``RepositoryManager.getAssetContentRecordTypes()`` can be
        used to test which records are supported, this method tests
        which records are required for creating a specific
        ``AssetContent``. Providing an empty array tests if an
        ``AssetContent`` can be created with no records.


        :param asset_content_record_types: array of asset content record types
        :type asset_content_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``AssetContent`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``asset_content_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_asset_content_form_for_create(self, asset_id, asset_content_record_types):
        """Gets an asset content form for creating new assets.


        :param asset_id: the ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :param asset_content_record_types: array of asset content record types
        :type asset_content_record_types: ``osid.type.Type[]``
        :return: the asset content form
        :rtype: ``osid.repository.AssetContentForm``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``asset_content_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetContentForm

    def create_asset_content(self, asset_content_form):
        """Creates new ``AssetContent`` for a given asset.


        :param asset_content_form: the form for this ``AssetContent``
        :type asset_content_form: ``osid.repository.AssetContentForm``
        :return: the new ``AssetContent``
        :rtype: ``osid.repository.AssetContent``
        :raise: ``IllegalState`` -- ``asset_content_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``asset_content_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_content_form`` did not originate from ``get_asset_content_form_for_create()``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetContent

    def can_update_asset_contents(self):
        """Tests if this user can update ``AssetContent``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.


        :return: ``false`` if ``AssetContent`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_asset_content_form_for_update(self, asset_content_id):
        """Gets the asset content form for updating an existing asset content.


        A new asset content form should be requested for each update
        transaction.


        :param asset_content_id: the ``Id`` of the ``AssetContent``
        :type asset_content_id: ``osid.id.Id``
        :return: the asset content form
        :rtype: ``osid.repository.AssetContentForm``
        :raise: ``NotFound`` -- ``asset_content_id`` is not found
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetContentForm

    def update_asset_content(self, asset_content_form):
        """Updates an existing asset content.


        :param asset_content_form: the form containing the elements to be updated
        :type asset_content_form: ``osid.repository.AssetContentForm``
        :raise: ``IllegalState`` -- ``asset_content_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``asset_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``asset_content_form`` did not originate from ``get_asset_content_form_for_update()``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_delete_asset_contents(self):
        """Tests if this user can delete ``AssetsContents``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``AssetContent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.


        :return: ``false`` if ``AssetContent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def delete_asset_content(self, asset_content_id):
        """Deletes content from an ``Asset``.


        :param asset_content_id: the ``Id`` of the ``AssetContent``
        :type asset_content_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_content_id`` is not found
        :raise: ``NullArgument`` -- ``asset_content_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class AssetNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Asset`` objects in this
        ``Repository``.


    This also includes existing assets that may appear or disappear due
    to changes in the ``Repository`` hierarchy, This session is intended
    for consumers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.




    The two views defined in this session correspond to the views in the
    ``AssetLookupSession``.


    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_register_for_asset_notifications(self):
        """Tests if this user can register for ``Asset`` notifications.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.


        A federated view will include assets in repositories which are
        children of this repository in the repository hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts notifications to this repository
        only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def register_for_new_assets(self):
        """Register for notifications of new assets.


        ``AssetReceiver.newAssets()`` is invoked when a new ``Asset``
        appears in this repository.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def register_for_new_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of new assets of the given asset genus type.


        ``AssetReceiver.newAssets()`` is invoked when an asset is
        appears in this repository.


        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def register_for_changed_assets(self):
        """Registers for notification of updated assets.


        ``AssetReceiver.changedAssets()`` is invoked when an asset in
        this repository is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def register_for_changed_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of updated assets of the given asset genus type.


        ``AssetReceiver.changedAssets()`` is invoked when an asset in
        this repository is changed.


        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def register_for_changed_asset(self, asset_id):
        """Registers for notification of an updated asset.


        ``AssetReceiver.changedAssets()`` is invoked when the specified
        asset in this repository is changed.


        :param asset_id: the ``Id`` of the ``Asset`` to monitor
        :type asset_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def register_for_deleted_assets(self):
        """Registers for notification of deleted assets.


        ``AssetReceiver.deletedAssets()`` is invoked when an asset is
        deleted or removed from this repository.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def register_for_deleted_assets_by_genus_type(self, asset_genus_type):
        """Registers for notification of deleted assets of the given asset genus type.


        ``AssetReceiver.deletedAssets()`` is invoked when an asset is
        deleted or removed from this repository.


        :param asset_genus_type: the genus type of the ``Asset`` to monitor
        :type asset_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``asset_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def register_for_deleted_asset(self, asset_id):
        """Registers for notification of a deleted asset.


        ``AssetReceiver.deletedAssets()`` is invoked when the specified
        asset is deleted or removed from this repository.


        :param asset_id: the ``Id`` of the ``Asset`` to monitor
        :type asset_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def reliable_asset_notifications(self):
        """Reliable notifications are desired.


        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def unreliable_asset_notifications(self):
        """Unreliable notifications are desired.


        In unreliable mode, notifications do not need to be
        acknowledged.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def acknowledge_asset_notification(self, notification_id):
        """Acknowledge an asset notification.


        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class AssetRepositorySession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Assets`` to ``Repository`` mappings.


    An ``Asset`` may appear in multiple ``Repository`` objects. Each
    Repository may have its own authorizations governing who is allowed
    to look at it.




    This lookup session defines two views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """

    def can_lookup_asset_repository_mappings(self):
        """Tests if this user can perform lookups of asset/repository mappings.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.


        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Asset`` and ``Repository`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_asset_ids_by_repository(self, repository_id):
        """Gets the list of ``Asset``  ``Ids`` associated with a ``Repository``.


        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of related asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_assets_by_repository(self, repository_id):
        """Gets the list of ``Assets`` associated with a ``Repository``.


        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of related assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    def get_asset_ids_by_repositories(self, repository_ids):
        """Gets the list of ``Asset Ids`` corresponding to a list of ``Repository`` objects.


        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of asset ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_assets_by_repositories(self, repository_ids):
        """Gets the list of ``Assets`` corresponding to a list of ``Repository`` objects.


        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.AssetList

    def get_repository_ids_by_asset(self, asset_id):
        """Gets the list of ``Repository``  ``Ids`` mapped to an ``Asset``.


        :param asset_id: ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: list of repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_repositories_by_asset(self, asset_id):
        """Gets the list of ``Repository`` objects mapped to an ``Asset``.


        :param asset_id: ``Id`` of an ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: list of repositories
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList


class AssetRepositoryAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Assets`` to ``Repositories``.


    An ``Asset`` may map to multiple ``Repository`` objects and removing
    the last reference to an ``Asset`` is the equivalent of deleting it.
    Each ``Repository`` may have its own authorizations governing who is
    allowed to operate on it.




    Moving or adding a reference of an ``Asset`` to another
    ``Repository`` is not a copy operation (eg: does not change its
    ``Id`` ).


    """

    def can_assign_assets(self):
        """Tests if this user can alter asset/repository mappings.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.


        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_assign_assets_to_repository(self, repository_id):
        """Tests if this user can alter asset/repository mappings.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.


        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_assignable_repository_ids(self, repository_id):
        """Gets a list of repositories including and under the given repository node in which any asset can be assigned.


        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_assignable_repository_ids_for_asset(self, repository_id, asset_id):
        """Gets a list of repositories including and under the given repository node in which a specific asset can be
            assigned.


        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` or ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def assign_asset_to_repository(self, asset_id, repository_id):
        """Adds an existing ``Asset`` to a ``Repository``.


        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``asset_id`` already assigned to ``repository_id``
        :raise: ``NotFound`` -- ``asset_id`` or ``repository_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def unassign_asset_from_repository(self, asset_id, repository_id):
        """Removes an ``Asset`` from a ``Repository``.


        :param asset_id: the ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` or ``repository_id`` not found or ``asset_id`` not assigned to
            ``repository_id``
        :raise: ``NullArgument`` -- ``asset_id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class AssetCompositionSession(osid_sessions.OsidSession):
    """This session defines methods for looking up ``Asset`` to ``Composition`` mappings.


    A ``Composition`` represents a collection of ``Assets``.




    This lookup session defines several views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated repository view: All lookup methods in this session
        operate, retrieve and pertain to asseta and compositions defined
        explicitly in the current repository. Using an isolated view is
        useful for managing compositions with the
        CompositionAdminSession.
      * federated repository view: All lookup methods in this session
        operate, retrieve and pertain to all compositions and assets
        defined in this repository and any other compositions implicitly
        available in this repository through repository inheritence.








    The methods ``use_federated_asset_composition_view()`` and
    ``use_isolated_asset_compositiont_view()`` behave as a radio group
    and one should be selected before invoking any lookup methods.


    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_access_asset_compositions(self):
        """Tests if this user can perform composition lookups.


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

    def use_comparative_asset_composition_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_asset_composition_view(self):
        """A complete view of the returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.


        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this repository only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_composition_assets(self, composition_id):
        """Gets the list of assets mapped to the given ``Composition``.


        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: list of assets
        :rtype: ``osid.repository.AssetList``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.repository.AssetList

    def get_compositions_by_asset(self, asset_id):
        """Gets a list of compositions including the given asset.


        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NotFound`` -- ``asset_id`` is not found
        :raise: ``NullArgument`` -- ``asset_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList


class AssetCompositionDesignSession(osid_sessions.OsidSession):
    """This session provides the means for adding assets to an asset composiiton.


    The asset is identified inside a composition using its own Id. To
    add the same asset to the composition, multiple compositions should
    be used and placed at the same level in the ``Composition``
    hierarchy.


    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_compose_assets(self):
        """Tests if this user can manage mapping of ``Assets`` to ``Compositions``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as an application hint that may opt not to offer composition
        operations.


        :return: ``false`` if asset composiion is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def add_asset(self, asset_id, composition_id):
        """Appends an asset to a composition.


        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``asset_id`` already part ``composition_id``
        :raise: ``NotFound`` -- ``asset_id`` or ``composition_id`` not found
        :raise: ``NullArgument`` -- ``asset_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def move_asset_ahead(self, asset_id, composition_id, reference_id):
        """Reorders assets in a composition by moving the specified asset in front of a reference asset.


        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param reference_id: ``Id`` of the reference ``Asset``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` or ``reference_id``  ``not found in composition_id``
        :raise: ``NullArgument`` -- ``asset_id, reference_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def move_asset_behind(self, asset_id, composition_id, reference_id):
        """Reorders assets in a composition by moving the specified asset behind of a reference asset.


        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param reference_id: ``Id`` of the reference ``Asset``
        :type reference_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id`` or ``reference_id``  ``not found in composition_id``
        :raise: ``NullArgument`` -- ``asset_id, reference_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def order_assets(self, asset_ids, composition_id):
        """Reorders a set of assets in a composition.


        :param asset_ids: ``Ids`` for a set of ``Assets``
        :type asset_ids: ``osid.id.Id[]``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` not found or, an ``asset_id`` not related to ``composition_id``
        :raise: ``NullArgument`` -- ``instruction_ids`` or ``agenda_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_asset(self, asset_id, composition_id):
        """Removes an ``Asset`` from a ``Composition``.


        :param asset_id: ``Id`` of the ``Asset``
        :type asset_id: ``osid.id.Id``
        :param composition_id: ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``asset_id``  ``not found in composition_id``
        :raise: ``NullArgument`` -- ``asset_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization fauilure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class CompositionLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Composition`` objects.


    The ``Composition`` represents a collection of ``Assets``.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete and ordered result set or is
        an error condition
      * isolated repository view: All lookup methods in this session
        operate, retrieve and pertain to compositions defined explicitly
        in the current repository. Using an isolated view is useful for
        managing compositions with the ``CompositionAdminSession.``
      * federated repository view: All composition methods in this
        session operate, retrieve and pertain to all compositions
        defined in this repository and any other compositions implicitly
        available in this repository through repository inheritence.
      * active composition view: All composition lookup methods return
        active compositions.
      * any status composition view: Compositions of any active or
        inactive status are returned from methods.
      * sequestered composition viiew: All composition methods suppress
        sequestered compositions.
      * unsequestered composition view: All composition methods return
        all compositions.








    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Composition`` it can access, without breaking
    execution. However, an administrative application may require a
    complete set of ``Composition`` objects to be returned.




    Compositions may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Composition``.


    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_lookup_compositions(self):
        """Tests if this user can perform ``Composition`` lookups.


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

    def use_comparative_composition_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_composition_view(self):
        """A complete view of the ``Composition`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.


        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this repository only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_active_composition_view(self):
        """Only active compositions are returned by methods in this session.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_any_status_composition_view(self):
        """All active and inactive compositions are returned by methods in this session.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_sequestered_composition_view(self):
        """The methods in this session omit sequestered compositions.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_unsequestered_composition_view(self):
        """The methods in this session return all compositions, including sequestered compositions.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_composition(self, composition_id):
        """Gets the ``Composition`` specified by its ``Id``.


        :param composition_id: ``Id`` of the ``Composiiton``
        :type composition_id: ``osid.id.Id``
        :return: the composition
        :rtype: ``osid.repository.Composition``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.repository.Composition

    def get_compositions_by_ids(self, composition_ids):
        """Gets a ``CompositionList`` corresponding to the given ``IdList``.


        :param composition_ids: the list of ``Ids`` to retrieve
        :type composition_ids: ``osid.id.IdList``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``composition_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList

    def get_compositions_by_genus_type(self, composition_genus_type):
        """Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` which does not include
            compositions of types derived from the specified ``Type``.


        :param composition_genus_type: a composition genus type
        :type composition_genus_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList

    def get_compositions_by_parent_genus_type(self, composition_genus_type):
        """Gets a ``CompositionList`` corresponding to the given composition genus ``Type`` and include any additional
            compositions with genus types derived from the specified ``Type``.


        :param composition_genus_type: a composition genus type
        :type composition_genus_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList

    def get_compositions_by_record_type(self, composition_record_type):
        """Gets a ``CompositionList`` containing the given composition record ``Type``.


        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList

    def get_compositions_by_provider(self, resource_id):
        """Gets a ``CompositionList`` from the given provider ````.


        In plenary mode, the returned list contains all known
        compositions or an error results. Otherwise, the returned list
        may contain only those compositions that are accessible through
        this session.


        In sequestered mode, no sequestered compositions are returned.
        In unsequestered mode, all compositions are returned.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Composition list``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList

    def get_compositions(self):
        """Gets all ``Compositions``.


        :return: a list of ``Compositions``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList

    compositions = property(fget=get_compositions)


class CompositionQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Composition`` objects.


    The search query is constructed using the ``CompositionQuery``.




    This session defines views that offer differing behaviors when
    searching.




      * federated repository view: searches include compositions in
        repositories of which this repository is an ancestor in the
        repository hierarchy
      * isolated repository view: searches are restricted to subjects in
        this repository
      * sequestered composition viiew: All composition methods suppress
        sequestered compositions.
      * unsequestered composition view: All composition methods return
        all compositions.








    Compositions may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``CompositionQuery``.


    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_search_compositions(self):
        """Tests if this user can perform ``Composition`` searches.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_federated_repository_view(self):
        """Federates the view for methods in this session.


        A federated view will include compositions in repositories which
        are children of this repository in the repository hierarchy.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_isolated_repository_view(self):
        """Isolates the view for methods in this session.


        An isolated view restricts lookups to this repository only.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_sequestered_composition_view(self):
        """The methods in this session omit sequestered compositions.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_unsequestered_composition_view(self):
        """The methods in this session return all compositions, including sequestered compositions.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_composition_query(self):
        """Gets a composition query.


        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionQuery

    composition_query = property(fget=get_composition_query)

    def get_compositions_by_query(self, composition_query):
        """Gets a list of ``Compositions`` matching the given composition query.


        :param composition_query: the composition query
        :type composition_query: ``osid.repository.CompositionQuery``
        :return: the returned ``CompositionList``
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``composition_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``composition_query`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList


class CompositionSearchSession(CompositionQuerySession):
    """This session provides methods for searching among ``Composition`` objects.


    The search query is constructed using the ``CompositionQuery``.




    ``get_compositions_by_query()`` is the basic search method and
    returns a list of ``Compositions``. A more advanced search may be
    performed with ``getCompositionsBySearch()``. It accepts an
    ``Composition`` in addition to the query for the purpose of
    specifying additional options affecting the entire search, such as
    ordering. ``get_compositions_by_search()`` returns an
    ``CompositionSearchResults`` that can be used to access the
    resulting ``Composition`` or be used to perform a search within the
    result set through ``CompositionSearch``.




    This session defines views that offer differing behaviors when
    searching.




      * federated repository view: searches include compositions in
        repositories of which this repository is an ancestor in the
        repository hierarchy
      * isolated repository view: searches are restricted to subjects in
        this repository








    Compositions may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``CompositionQuery``.


    """

    def get_composition_search(self):
        """Gets a composition search.


        :return: the composition search
        :rtype: ``osid.repository.CompositionSearch``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionSearch

    composition_search = property(fget=get_composition_search)

    def get_composition_search_order(self):
        """Gets a composition search order.


        The ``CompositionSearchOrder`` is supplied to an
        ``CompositionSearch`` to specify the ordering of results.


        :return: the composition search order
        :rtype: ``osid.repository.CompositionSearchOrder``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionSearchOrder

    composition_search_order = property(fget=get_composition_search_order)

    def get_compositions_by_search(self, composition_query, composition_search):
        """Gets the search results matching the given search query using the given search.


        :param composition_query: the composition query
        :type composition_query: ``osid.repository.CompositionQuery``
        :param composition_search: the composition search
        :type composition_search: ``osid.repository.CompositionSearch``
        :return: the composition search results
        :rtype: ``osid.repository.CompositionSearchResults``
        :raise: ``NullArgument`` -- ``composition_query`` or ``composition_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``composition_query`` or ``composition_search`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionSearchResults

    def get_composition_query_from_inspector(self, composition_query_inspector):
        """Gets a composition query from an inspector.


        The inspector is available from a ``CompositionSearchResults``.


        :param composition_query_inspector: a composition query inspector
        :type composition_query_inspector: ``osid.repository.CompositionQueryInspector``
        :return: the composition query
        :rtype: ``osid.repository.CompositionQuery``
        :raise: ``NullArgument`` -- ``composition_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``composition_query_inspector`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionQuery


class CompositionAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Compositions``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Composition,`` a ``CompositionForm`` is requested using
    ``get_composition_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``CompositionForm`` will indicate that it is to be used with a
    create operation and can be used to examine metdata or validate data
    prior to creation. Once the ``CompositionForm`` is submiited to a
    create operation, it cannot be reused with another create operation
    unless the first operation was unsuccessful. Each
    ``CompositionForm`` corresponds to an attempted transaction.




    For updates, ``CompositionForms`` are requested to the
    ``Composition``  ``Id`` that is to be updated using
    ``getCompositionFormForUpdate()``. Similarly, the
    ``CompositionForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``CompositionForm`` can only be used once for a successful update
    and cannot be reused.




    The delete operations delete ``Compositions``. To unmap a
    ``Composition`` from the current ``Repository,`` the
    ``CompositionRepositoryAssignmentSession`` should be used. These
    delete operations attempt to remove the ``Bid`` itself thus removing
    it from all known ``Repository`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.


    """

    def get_repository_id(self):
        """Gets the ``Repository``  ``Id`` associated with this session.


        :return: the ``Repository Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_id = property(fget=get_repository_id)

    def get_repository(self):
        """Gets the ``Repository`` associated with this session.


        :return: the ``Repository`` associated with this session
        :rtype: ``osid.repository.Repository``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    repository = property(fget=get_repository)

    def can_create_compositions(self):
        """Tests if this user can create ``Compositions``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Composition`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_create_composition_with_record_types(self, composition_record_types):
        """Tests if this user can create a single ``Composition`` using the desired record types.


        While ``RepositoryManager.getCompositionRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Composition``. Providing an empty array tests if a
        ``Composition`` can be created with no records.


        :param composition_record_types: array of composition record types
        :type composition_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Composition`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``composition_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_composition_form_for_create(self, composition_record_types):
        """Gets the composition form for creating new compositions.


        A new form should be requested for each create transaction.


        :param composition_record_types: array of composition record types
        :type composition_record_types: ``osid.type.Type[]``
        :return: the composition form
        :rtype: ``osid.repository.CompositionForm``
        :raise: ``NullArgument`` -- ``composition_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionForm

    def create_composition(self, composiiton_form):
        """Creates a new ``Composition``.


        :param composiiton_form: the form for this ``Composition``
        :type composiiton_form: ``osid.repository.CompositionForm``
        :return: the new ``Composition``
        :rtype: ``osid.repository.Composition``
        :raise: ``IllegalState`` -- ``composition_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``composition_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``composition_form`` did not originate from ``get_composition_form_for_create()``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Composition

    def can_update_compositions(self):
        """Tests if this user can update ``Compositions``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Composition`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_composition_form_for_update(self, composition_id):
        """Gets the composition form for updating an existing composition.


        A new composition form should be requested for each update
        transaction.


        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: the composition form
        :rtype: ``osid.repository.CompositionForm``
        :raise: ``NotFound`` -- ``composition_id`` is not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionForm

    def update_composition(self, composiiton_form):
        """Updates an existing composition.


        :param composiiton_form: the form containing the elements to be updated
        :type composiiton_form: ``osid.repository.CompositionForm``
        :raise: ``IllegalState`` -- ``composition_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``composition_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``composition_form`` did not originate from ``get_composition_form_for_update()``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_delete_compositions(self):
        """Tests if this user can delete ``Compositions``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Composition`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Composition`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def delete_composition(self, composition_id):
        """Deletes a ``Composition``.


        :param composition_id: the ``Id`` of the ``Composition`` to remove
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def delete_composition_node(self, composition_id):
        """Deletes a ``Composition`` and all contained children.


        :param composition_id: the ``Id`` of the ``Composition`` to remove
        :type composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def add_composition_child(self, composition_id, child_composition_id):
        """Adds a composition to a parent composition.


        :param composition_id: the ``Id`` of a parent ``Composition``
        :type composition_id: ``osid.id.Id``
        :param child_composition_id: the ``Id`` of a child ``Composition``
        :type child_composition_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``child_composition_id`` is already a child of ``composition_id``
        :raise: ``NotFound`` -- ``composition_id`` or ``child_composition_id`` is not found
        :raise: ``NullArgument`` -- ``composition_id`` or ``child_composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_composition_child(self, composition_id, child_composition_id):
        """Removes a composition from a parent composition.


        :param composition_id: the ``Id`` of a parent ``Composition``
        :type composition_id: ``osid.id.Id``
        :param child_composition_id: the ``Id`` of a child ``Composition``
        :type child_composition_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` or ``child_composition_id`` is not found or not related
        :raise: ``NullArgument`` -- ``composition_id`` or ``child_composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_manage_composition_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Compositions``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Composition`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def alias_composition(self, composition_id, alias_id):
        """Adds an ``Id`` to a ``Composition`` for the purpose of creating compatibility.


        The primary ``Id`` of the ``Composition`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another composition, it is reassigned
        to the given composition ``Id``.


        :param composition_id: the ``Id`` of a ``Composition``
        :type composition_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``composition_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class CompositionRepositorySession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Composition`` to ``Repository`` mappings.


    A ``Composition`` may appear in multiple ``Repository`` objects.
    Each ``Repository`` may have its own authorizations governing who is
    allowed to look at it.




    This lookup session defines several views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """

    def use_comparative_composition_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_composition_repository_view(self):
        """A complete view of the ``Composition`` and ``Repository`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def can_lookup_composition_repository_mappings(self):
        """Tests if this user can perform lookups of composition/repository mappings.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.


        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_composition_ids_by_repository(self, repository_id):
        """Gets the list of ``Composition``  ``Ids`` associated with a ``Repository``.


        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of related composition ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_compositions_by_repository(self, repository_id):
        """Gets the list of ``Compositions`` associated with a ``Repository``.


        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of related compositions
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList

    def get_composition_ids_by_repositories(self, repository_ids):
        """Gets the list of ``Composition``  ``Ids`` corresponding to a list of ``Repository`` objects.


        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of composition ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_compoitions_by_repositories(self, repository_ids):
        """Gets the list of ``Compositions`` corresponding to a list of ``Repository`` objects.


        :param repository_ids: list of repository ``Ids``
        :type repository_ids: ``osid.id.IdList``
        :return: list of Compositions
        :rtype: ``osid.repository.CompositionList``
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.CompositionList

    def get_repository_ids_by_composition(self, composition_id):
        """Gets the ``Repository``  ``Ids`` mapped to a ``Composition``.


        :param composition_id: ``Id`` of a ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: list of repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``composition_id`` is not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_repositories_by_composition(self, composition_id):
        """Gets the ``Repository`` objects mapped to a ``Composition``.


        :param composition_id: ``Id`` of a ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: list of repositories
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``composition_id`` is not found
        :raise: ``NullArgument`` -- ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList


class CompositionRepositoryAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Compositions`` to ``Repository`` objects.


    A ``Composition`` may be associated with multiple ``Repository``
    objects. Removing the last reference to a ``Composition`` is the
    equivalent of deleting it. Each ``Repository`` may have its own
    authorizations governing who is allowed to operate on it.




    Moving or adding a reference of a ``Composition`` to another
    ``Repository`` is not a copy operation (eg: does not change its
    ``Id`` ).


    """

    def can_assign_compositions(self):
        """Tests if this user can alter composition/repository mappings.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.


        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_assign_compositions_to_repository(self, repository_id):
        """Tests if this user can alter composition/repository mappings.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.


        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_assignable_repository_ids(self, repository_id):
        """Gets a list of repositories including and under the given repository node in which any composition can be
            assigned.


        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_assignable_repository_ids_for_composition(self, repository_id, composition_id):
        """Gets a list of repositories including and under the given repository node in which a specific composition can
            be assigned.


        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :return: list of assignable repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``repository_id`` or ``composition_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def assign_composition_to_repository(self, composition_id, repository_id):
        """Adds an existing ``Composition`` to a ``Repository``.


        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``composition_id`` already assigned to ``repository_id``
        :raise: ``NotFound`` -- ``composition_id`` or ``repository_id`` not found
        :raise: ``NullArgument`` -- ``composition_id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def unassign_composition_from_repository(self, composition_id, repository_id):
        """Removes ``Composition`` from a ``Repository``.


        :param composition_id: the ``Id`` of the ``Composition``
        :type composition_id: ``osid.id.Id``
        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``composition_id`` or ``repository_id`` not found or ``composition_id`` not assigned to
            ``repository_id``
        :raise: ``NullArgument`` -- ``composition_id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class RepositoryLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Repository`` objects.


    The ``Repository`` represents a collection of ``Assets`` and
    ``Compositions``.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition








    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Repositories`` it can access, without breaking
    execution. However, an administrative application may require all
    ``Repository`` elements to be available.




    Repositories may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Repository``.


    """

    def can_lookup_repositories(self):
        """Tests if this user can perform ``Repository`` lookups.


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

    def use_comparative_repository_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_repository(self, repository_id):
        """Gets the ``Repository`` specified by its ``Id``.


        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Repository`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Repository`` and retained
        for compatibility.


        :param repository_id: ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: the repository
        :rtype: ``osid.repository.Repository``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.repository.Repository

    def get_repositories_by_ids(self, repository_ids):
        """Gets a ``RepositoryList`` corresponding to the given ``IdList``.


        In plenary mode, the returned list contains all of the
        repositories specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Repositories`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.


        :param repository_ids: the list of ``Ids`` to retrieve
        :type repository_ids: ``osid.id.IdList``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``repository_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList

    def get_repositories_by_genus_type(self, repository_genus_type):
        """Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` which does not include
            repositories of types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.


        :param repository_genus_type: a repository genus type
        :type repository_genus_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList

    def get_repositories_by_parent_genus_type(self, repository_genus_type):
        """Gets a ``RepositoryList`` corresponding to the given repository genus ``Type`` and include any additional
            repositories with genus types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.


        :param repository_genus_type: a repository genus type
        :type repository_genus_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList

    def get_repositories_by_record_type(self, repository_record_type):
        """Gets a ``RepositoryList`` containing the given repository record ``Type``.


        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.


        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList

    def get_repositories_by_provider(self, resource_id):
        """Gets a ``RepositoryList`` from the given provider ````.


        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Repository list``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList

    def get_repositories(self):
        """Gets all ``Repositories``.


        In plenary mode, the returned list contains all known
        repositories or an error results. Otherwise, the returned list
        may contain only those repositories that are accessible through
        this session.


        :return: a list of ``Repositories``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList

    repositories = property(fget=get_repositories)


class RepositoryQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Repository`` objects.


    The search query is constructed using the ``RepositoryQuery``.




    Repositories may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RepositoryQuery``.


    """

    def can_search_repositories(self):
        """Tests if this user can perform ``Repository`` searches.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_repository_query(self):
        """Gets a repository query.


        :return: the repository query
        :rtype: ``osid.repository.RepositoryQuery``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryQuery

    repository_query = property(fget=get_repository_query)

    def get_repositories_by_query(self, repository_query):
        """Gets a list of ``Repositories`` matching the given repository query.


        :param repository_query: the repository query
        :type repository_query: ``osid.repository.RepositoryQuery``
        :return: the returned ``RepositoryList``
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NullArgument`` -- ``repository_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_query`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList


class RepositoryAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Repositories``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Repository,`` a ``RepositoryForm`` is requested using
    ``get_repository_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``RepositoryForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``RepositoryForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``RepositoryForm``
    corresponds to an attempted transaction.




    For updates, ``RepositoryForms`` are requested to the ``Repository``
    ``Id`` that is to be updated using ``getRepositoryFormForUpdate()``.
    Similarly, the ``RepositoryForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``RepositoryForm`` can only be used once for a
    successful update and cannot be reused.




    The delete operations delete ``Repositories``. This session includes
    an ``Id`` aliasing mechanism to assign an external ``Id`` to an
    internally assigned Id.


    """

    def can_create_repositories(self):
        """Tests if this user can create ``Repositories``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Repository`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_create_repository_with_record_types(self, repository_record_types):
        """Tests if this user can create a single ``Repository`` using the desired record types.


        While ``RepositoryManager.getRepositoryRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Repository``. Providing an empty array tests if a
        ``Repository`` can be created with no records.


        :param repository_record_types: array of repository record types
        :type repository_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Repository`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``repository_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_repository_form_for_create(self, repository_record_types):
        """Gets the repository form for creating new repositories.


        A new form should be requested for each create transaction.


        :param repository_record_types: array of repository record types
        :type repository_record_types: ``osid.type.Type[]``
        :return: the repository form
        :rtype: ``osid.repository.RepositoryForm``
        :raise: ``NullArgument`` -- ``repository_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryForm

    def create_repository(self, repository_form):
        """Creates a new ``Repository``.


        :param repository_form: the form for this ``Repository``
        :type repository_form: ``osid.repository.RepositoryForm``
        :return: the new ``Repository``
        :rtype: ``osid.repository.Repository``
        :raise: ``IllegalState`` -- ``repository_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``repository_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_form`` did not originate from ``get_repository_form_for_create()``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.Repository

    def can_update_repositories(self):
        """Tests if this user can update ``Repositories``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Repository`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_repository_form_for_update(self, repository_id):
        """Gets the repository form for updating an existing repository.


        A new repository form should be requested for each update
        transaction.


        :param repository_id: the ``Id`` of the ``Repository``
        :type repository_id: ``osid.id.Id``
        :return: the repository form
        :rtype: ``osid.repository.RepositoryForm``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryForm

    def update_repository(self, repository_form):
        """Updates an existing repository.


        :param repository_form: the form containing the elements to be updated
        :type repository_form: ``osid.repository.RepositoryForm``
        :raise: ``IllegalState`` -- ``repository_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``repository_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``repository_form`` did not originate from ``get_repository_form_for_update()``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_delete_repositories(self):
        """Tests if this user can delete ``Repositories``.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Repository`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Repository`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def delete_repository(self, repository_id):
        """Deletes a ``Repository``.


        :param repository_id: the ``Id`` of the ``Repository`` to remove
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_manage_repository_aliases(self):
        """Tests if this user can manage ``Id`` aliases for repositories.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Repository`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def alias_repository(self, repository_id, alias_id):
        """Adds an ``Id`` to a ``Repository`` for the purpose of creating compatibility.


        The primary ``Id`` of the ``Repository`` is determined by the
        provider. The new ``Id`` is an alias to the primary ``Id``. If
        the alias is a pointer to another repository, it is reassigned
        to the given repository ``Id``.


        :param repository_id: the ``Id`` of a ``Repository``
        :type repository_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is in use as a primary ``Id``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


class RepositoryHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Repository`` objects.


    Each node in the hierarchy is a unique ``Repository``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parents()`` and ``getChildren()``. To relate these ``Ids`` to
    another OSID, ``get_ancestors()`` and ``get_descendants()`` can be
    used for retrievals that can be used for bulk lookups in other
    OSIDs. Any ``Repository`` available in the Repository OSID is known
    to this hierarchy but does not appear in the hierarchy traversal
    until added as a root node or a child of another node.




    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parents()`` or ``get_children()`` in lieu of a
    ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: repository elements may be silently omitted or
        re-ordered
      * plenary view: provides a complete set or is an error condition


    """

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.


        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.


        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_access_repository_hierarchy(self):
        """Tests if this user can perform hierarchy queries.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def use_comparative_repository_view(self):
        """The returns from the repository methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_repository_view(self):
        """A complete view of the ``Repository`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_root_repository_ids(self):
        """Gets the root repository ``Ids`` in this hierarchy.


        :return: the root repository ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    root_repository_ids = property(fget=get_root_repository_ids)

    def get_root_repositories(self):
        """Gets the root repositories in the repository hierarchy.


        A node with no parents is an orphan. While all repository
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.


        :return: the root repositories
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method is must be implemented.*


        """
        return # osid.repository.RepositoryList

    root_repositories = property(fget=get_root_repositories)

    def has_parent_repositories(self, repository_id):
        """Tests if the ``Repository`` has any parents.


        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the repository has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def is_parent_of_repository(self, id_, repository_id):
        """Tests if an ``Id`` is a direct parent of a repository.


        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.


        """
        return # boolean

    def get_parent_repository_ids(self, repository_id):
        """Gets the parent ``Ids`` of the given repository.


        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the repository
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` is not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_parent_repositories(self, repository_id):
        """Gets the parents of the given repository.


        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the parents of the repository
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList

    def is_ancestor_of_repository(self, id_, repository_id):
        """Tests if an ``Id`` is an ancestor of a repository.


        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the Id of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.


        """
        return # boolean

    def has_child_repositories(self, repository_id):
        """Tests if a repository has any children.


        :param repository_id: a repository ``Id``
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``repository_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def is_child_of_repository(self, id_, repository_id):
        """Tests if a node is a direct child of another.


        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.


        """
        return # boolean

    def get_child_repository_ids(self, repository_id):
        """Gets the ``Ids`` of the children of the given repository.


        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the children of the repository
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def get_child_repositories(self, repository_id):
        """Gets the children of the given repository.


        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :return: the children of the repository
        :rtype: ``osid.repository.RepositoryList``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryList

    def is_descendant_of_repository(self, id_, repository_id):
        """Tests if an ``Id`` is a descendant of a repository.


        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``repository_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.


        """
        return # boolean

    def get_repository_node_ids(self, repository_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given repository.


        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: the specified repository node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Node

    def get_repository_nodes(self, repository_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given repository.


        :param repository_id: the ``Id`` to query
        :type repository_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: the specified repository node
        :rtype: ``osid.repository.RepositoryNode``
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.repository.RepositoryNode


class RepositoryHierarchyDesignSession(osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Repository`` objects.


    Each node in the hierarchy is a unique ``Repository``.


    """

    def get_repository_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.


        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    repository_hierarchy_id = property(fget=get_repository_hierarchy_id)

    def get_repository_hierarchy(self):
        """Gets the hierarchy associated with this session.


        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    repository_hierarchy = property(fget=get_repository_hierarchy)

    def can_modify_repository_hierarchy(self):
        """Tests if this user can change the hierarchy.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.


        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def add_root_repository(self, repository_id):
        """Adds a root repository.


        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``repository_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_root_repository(self, repository_id):
        """Removes a root repository.


        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a root
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def add_child_repository(self, repository_id, child_id):
        """Adds a child to a repository.


        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``repository_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``repository_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``repository_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_child_repository(self, repository_id, child_id):
        """Removes a child from a repository.


        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``repository_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_child_repositories(self, repository_id):
        """Removes all children from a repository.


        :param repository_id: the ``Id`` of a repository
        :type repository_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``repository_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``repository_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


