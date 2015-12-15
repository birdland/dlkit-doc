

Sessions
========


Asset Lookup Session
--------------------

.. py:class:: AssetLookupSession(abc_repository_sessions.AssetLookupSession, osid_sessions.OsidSession)
    This session defines methods for retrieving assets.


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





    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_lookup_assets():
        :noindex:


    .. py:method:: use_comparative_asset_view():
        :noindex:


    .. py:method:: use_plenary_asset_view():
        :noindex:


    .. py:method:: use_federated_repository_view():
        :noindex:


    .. py:method:: use_isolated_repository_view():
        :noindex:


    .. py:method:: get_asset(asset_id):
        :noindex:


    .. py:method:: get_assets_by_ids(asset_ids):
        :noindex:


    .. py:method:: get_assets_by_genus_type(asset_genus_type):
        :noindex:


    .. py:method:: get_assets_by_parent_genus_type(asset_genus_type):
        :noindex:


    .. py:method:: get_assets_by_record_type(asset_record_type):
        :noindex:


    .. py:method:: get_assets_by_provider(resource_id):
        :noindex:


    .. py:method:: get_assets():
        :noindex:


    .. py:attribute:: assets
        :noindex:


Asset Query Session
-------------------

.. py:class:: AssetQuerySession(abc_repository_sessions.AssetQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``Asset`` objects.


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





    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_search_assets():
        :noindex:


    .. py:method:: use_federated_repository_view():
        :noindex:


    .. py:method:: use_isolated_repository_view():
        :noindex:


    .. py:method:: get_asset_query():
        :noindex:


    .. py:attribute:: asset_query
        :noindex:


    .. py:method:: get_assets_by_query(asset_query):
        :noindex:


Asset Search Session
--------------------

.. py:class:: AssetSearchSession(abc_repository_sessions.AssetSearchSession, AssetQuerySession)
    This session provides methods for searching among ``Asset`` objects.


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





    .. py:method:: get_asset_search():
        :noindex:


    .. py:attribute:: asset_search
        :noindex:


    .. py:method:: get_asset_search_order():
        :noindex:


    .. py:attribute:: asset_search_order
        :noindex:


    .. py:method:: get_assets_by_search(asset_query, asset_search):
        :noindex:


    .. py:method:: get_asset_query_from_inspector(asset_query_inspector):
        :noindex:


Asset Admin Session
-------------------

.. py:class:: AssetAdminSession(abc_repository_sessions.AssetAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Assets``.


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




      PhotographRecordForm photoForm = (PhotographRecordForn)
          form.getRecordForm(assetPhotogaphType);
      Metadata metadata = form.getApertureMetadata();
      if (metadata.isReadOnly()) {
          return ("cannot set aperture");
      }




      photoForm.setAperture("5.6");
      if (!form.isValid()) {
          return form.getValidationMessage();
      }




      Asset newAsset = session.createAsset(form);









    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_create_assets():
        :noindex:


    .. py:method:: can_create_asset_with_record_types(asset_record_types):
        :noindex:


    .. py:method:: get_asset_form_for_create(asset_record_types):
        :noindex:


    .. py:method:: create_asset(asset_form):
        :noindex:


    .. py:method:: can_update_assets():
        :noindex:


    .. py:method:: get_asset_form_for_update(asset_id):
        :noindex:


    .. py:method:: update_asset(asset_form):
        :noindex:


    .. py:method:: can_delete_assets():
        :noindex:


    .. py:method:: delete_asset(asset_id):
        :noindex:


    .. py:method:: can_manage_asset_aliases():
        :noindex:


    .. py:method:: alias_asset(asset_id, alias_id):
        :noindex:


    .. py:method:: can_create_asset_content():
        :noindex:


    .. py:method:: can_create_asset_content_with_record_types(asset_content_record_types):
        :noindex:


    .. py:method:: get_asset_content_form_for_create(asset_id, asset_content_record_types):
        :noindex:


    .. py:method:: create_asset_content(asset_content_form):
        :noindex:


    .. py:method:: can_update_asset_contents():
        :noindex:


    .. py:method:: get_asset_content_form_for_update(asset_content_id):
        :noindex:


    .. py:method:: update_asset_content(asset_content_form):
        :noindex:


    .. py:method:: can_delete_asset_contents():
        :noindex:


    .. py:method:: delete_asset_content(asset_content_id):
        :noindex:


Asset Notification Session
--------------------------

.. py:class:: AssetNotificationSession(abc_repository_sessions.AssetNotificationSession, osid_sessions.OsidSession)
    This session defines methods to receive notifications on adds/changes to ``Asset`` objects in
        this
    ``Repository``.


    This also includes existing assets that may appear or disappear due
    to changes in the ``Repository`` hierarchy, This session is intended
    for consumers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.




    The two views defined in this session correspond to the views in the
    ``AssetLookupSession``.





    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_register_for_asset_notifications():
        :noindex:


    .. py:method:: use_federated_repository_view():
        :noindex:


    .. py:method:: use_isolated_repository_view():
        :noindex:


    .. py:method:: register_for_new_assets():
        :noindex:


    .. py:method:: register_for_new_assets_by_genus_type(asset_genus_type):
        :noindex:


    .. py:method:: register_for_changed_assets():
        :noindex:


    .. py:method:: register_for_changed_assets_by_genus_type(asset_genus_type):
        :noindex:


    .. py:method:: register_for_changed_asset(asset_id):
        :noindex:


    .. py:method:: register_for_deleted_assets():
        :noindex:


    .. py:method:: register_for_deleted_assets_by_genus_type(asset_genus_type):
        :noindex:


    .. py:method:: register_for_deleted_asset(asset_id):
        :noindex:


    .. py:method:: reliable_asset_notifications():
        :noindex:


    .. py:method:: unreliable_asset_notifications():
        :noindex:


    .. py:method:: acknowledge_asset_notification(notification_id):
        :noindex:


Asset Repository Session
------------------------

.. py:class:: AssetRepositorySession(abc_repository_sessions.AssetRepositorySession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``Assets`` to ``Repository`` mappings.


    An ``Asset`` may appear in multiple ``Repository`` objects. Each
    Repository may have its own authorizations governing who is allowed
    to look at it.




    This lookup session defines two views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: can_lookup_asset_repository_mappings():
        :noindex:


    .. py:method:: use_comparative_repository_view():
        :noindex:


    .. py:method:: use_plenary_repository_view():
        :noindex:


    .. py:method:: get_asset_ids_by_repository(repository_id):
        :noindex:


    .. py:method:: get_assets_by_repository(repository_id):
        :noindex:


    .. py:method:: get_asset_ids_by_repositories(repository_ids):
        :noindex:


    .. py:method:: get_assets_by_repositories(repository_ids):
        :noindex:


    .. py:method:: get_repository_ids_by_asset(asset_id):
        :noindex:


    .. py:method:: get_repositories_by_asset(asset_id):
        :noindex:


Asset Repository Assignment Session
-----------------------------------

.. py:class:: AssetRepositoryAssignmentSession(abc_repository_sessions.AssetRepositoryAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``Assets`` to ``Repositories``.


    An ``Asset`` may map to multiple ``Repository`` objects and removing
    the last reference to an ``Asset`` is the equivalent of deleting it.
    Each ``Repository`` may have its own authorizations governing who is
    allowed to operate on it.




    Moving or adding a reference of an ``Asset`` to another
    ``Repository`` is not a copy operation (eg: does not change its
    ``Id`` ).





    .. py:method:: can_assign_assets():
        :noindex:


    .. py:method:: can_assign_assets_to_repository(repository_id):
        :noindex:


    .. py:method:: get_assignable_repository_ids(repository_id):
        :noindex:


    .. py:method:: get_assignable_repository_ids_for_asset(repository_id, asset_id):
        :noindex:


    .. py:method:: assign_asset_to_repository(asset_id, repository_id):
        :noindex:


    .. py:method:: unassign_asset_from_repository(asset_id, repository_id):
        :noindex:


Asset Composition Session
-------------------------

.. py:class:: AssetCompositionSession(abc_repository_sessions.AssetCompositionSession, osid_sessions.OsidSession)
    This session defines methods for looking up ``Asset`` to ``Composition`` mappings.


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





    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_access_asset_compositions():
        :noindex:


    .. py:method:: use_comparative_asset_composition_view():
        :noindex:


    .. py:method:: use_plenary_asset_composition_view():
        :noindex:


    .. py:method:: use_federated_repository_view():
        :noindex:


    .. py:method:: use_isolated_repository_view():
        :noindex:


    .. py:method:: get_composition_assets(composition_id):
        :noindex:


    .. py:method:: get_compositions_by_asset(asset_id):
        :noindex:


Asset Composition Design Session
--------------------------------

.. py:class:: AssetCompositionDesignSession(abc_repository_sessions.AssetCompositionDesignSession, osid_sessions.OsidSession)
    This session provides the means for adding assets to an asset composiiton.


    The asset is identified inside a composition using its own Id. To
    add the same asset to the composition, multiple compositions should
    be used and placed at the same level in the ``Composition``
    hierarchy.





    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_compose_assets():
        :noindex:


    .. py:method:: add_asset(asset_id, composition_id):
        :noindex:


    .. py:method:: move_asset_ahead(asset_id, composition_id, reference_id):
        :noindex:


    .. py:method:: move_asset_behind(asset_id, composition_id, reference_id):
        :noindex:


    .. py:method:: order_assets(asset_ids, composition_id):
        :noindex:


    .. py:method:: remove_asset(asset_id, composition_id):
        :noindex:


Composition Lookup Session
--------------------------

.. py:class:: CompositionLookupSession(abc_repository_sessions.CompositionLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Composition`` objects.


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





    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_lookup_compositions():
        :noindex:


    .. py:method:: use_comparative_composition_view():
        :noindex:


    .. py:method:: use_plenary_composition_view():
        :noindex:


    .. py:method:: use_federated_repository_view():
        :noindex:


    .. py:method:: use_isolated_repository_view():
        :noindex:


    .. py:method:: use_active_composition_view():
        :noindex:


    .. py:method:: use_any_status_composition_view():
        :noindex:


    .. py:method:: use_sequestered_composition_view():
        :noindex:


    .. py:method:: use_unsequestered_composition_view():
        :noindex:


    .. py:method:: get_composition(composition_id):
        :noindex:


    .. py:method:: get_compositions_by_ids(composition_ids):
        :noindex:


    .. py:method:: get_compositions_by_genus_type(composition_genus_type):
        :noindex:


    .. py:method:: get_compositions_by_parent_genus_type(composition_genus_type):
        :noindex:


    .. py:method:: get_compositions_by_record_type(composition_record_type):
        :noindex:


    .. py:method:: get_compositions_by_provider(resource_id):
        :noindex:


    .. py:method:: get_compositions():
        :noindex:


    .. py:attribute:: compositions
        :noindex:


Composition Query Session
-------------------------

.. py:class:: CompositionQuerySession(abc_repository_sessions.CompositionQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``Composition`` objects.


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





    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_search_compositions():
        :noindex:


    .. py:method:: use_federated_repository_view():
        :noindex:


    .. py:method:: use_isolated_repository_view():
        :noindex:


    .. py:method:: use_sequestered_composition_view():
        :noindex:


    .. py:method:: use_unsequestered_composition_view():
        :noindex:


    .. py:method:: get_composition_query():
        :noindex:


    .. py:attribute:: composition_query
        :noindex:


    .. py:method:: get_compositions_by_query(composition_query):
        :noindex:


Composition Search Session
--------------------------

.. py:class:: CompositionSearchSession(abc_repository_sessions.CompositionSearchSession, CompositionQuerySession)
    This session provides methods for searching among ``Composition`` objects.


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





    .. py:method:: get_composition_search():
        :noindex:


    .. py:attribute:: composition_search
        :noindex:


    .. py:method:: get_composition_search_order():
        :noindex:


    .. py:attribute:: composition_search_order
        :noindex:


    .. py:method:: get_compositions_by_search(composition_query, composition_search):
        :noindex:


    .. py:method:: get_composition_query_from_inspector(composition_query_inspector):
        :noindex:


Composition Admin Session
-------------------------

.. py:class:: CompositionAdminSession(abc_repository_sessions.CompositionAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Compositions``.


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





    .. py:method:: get_repository_id():
        :noindex:


    .. py:attribute:: repository_id
        :noindex:


    .. py:method:: get_repository():
        :noindex:


    .. py:attribute:: repository
        :noindex:


    .. py:method:: can_create_compositions():
        :noindex:


    .. py:method:: can_create_composition_with_record_types(composition_record_types):
        :noindex:


    .. py:method:: get_composition_form_for_create(composition_record_types):
        :noindex:


    .. py:method:: create_composition(composiiton_form):
        :noindex:


    .. py:method:: can_update_compositions():
        :noindex:


    .. py:method:: get_composition_form_for_update(composition_id):
        :noindex:


    .. py:method:: update_composition(composiiton_form):
        :noindex:


    .. py:method:: can_delete_compositions():
        :noindex:


    .. py:method:: delete_composition(composition_id):
        :noindex:


    .. py:method:: delete_composition_node(composition_id):
        :noindex:


    .. py:method:: add_composition_child(composition_id, child_composition_id):
        :noindex:


    .. py:method:: remove_composition_child(composition_id, child_composition_id):
        :noindex:


    .. py:method:: can_manage_composition_aliases():
        :noindex:


    .. py:method:: alias_composition(composition_id, alias_id):
        :noindex:


Composition Repository Session
------------------------------

.. py:class:: CompositionRepositorySession(abc_repository_sessions.CompositionRepositorySession, osid_sessions.OsidSession)
    This session provides methods to retrieve ``Composition`` to ``Repository`` mappings.


    A ``Composition`` may appear in multiple ``Repository`` objects.
    Each ``Repository`` may have its own authorizations governing who is
    allowed to look at it.




    This lookup session defines several views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition





    .. py:method:: use_comparative_composition_repository_view():
        :noindex:


    .. py:method:: use_plenary_composition_repository_view():
        :noindex:


    .. py:method:: can_lookup_composition_repository_mappings():
        :noindex:


    .. py:method:: get_composition_ids_by_repository(repository_id):
        :noindex:


    .. py:method:: get_compositions_by_repository(repository_id):
        :noindex:


    .. py:method:: get_composition_ids_by_repositories(repository_ids):
        :noindex:


    .. py:method:: get_compoitions_by_repositories(repository_ids):
        :noindex:


    .. py:method:: get_repository_ids_by_composition(composition_id):
        :noindex:


    .. py:method:: get_repositories_by_composition(composition_id):
        :noindex:


Composition Repository Assignment Session
-----------------------------------------

.. py:class:: CompositionRepositoryAssignmentSession(abc_repository_sessions.CompositionRepositoryAssignmentSession, osid_sessions.OsidSession)
    This session provides methods to re-assign ``Compositions`` to ``Repository`` objects.


    A ``Composition`` may be associated with multiple ``Repository``
    objects. Removing the last reference to a ``Composition`` is the
    equivalent of deleting it. Each ``Repository`` may have its own
    authorizations governing who is allowed to operate on it.




    Moving or adding a reference of a ``Composition`` to another
    ``Repository`` is not a copy operation (eg: does not change its
    ``Id`` ).





    .. py:method:: can_assign_compositions():
        :noindex:


    .. py:method:: can_assign_compositions_to_repository(repository_id):
        :noindex:


    .. py:method:: get_assignable_repository_ids(repository_id):
        :noindex:


    .. py:method:: get_assignable_repository_ids_for_composition(repository_id, composition_id):
        :noindex:


    .. py:method:: assign_composition_to_repository(composition_id, repository_id):
        :noindex:


    .. py:method:: unassign_composition_from_repository(composition_id, repository_id):
        :noindex:


Repository Lookup Session
-------------------------

.. py:class:: RepositoryLookupSession(abc_repository_sessions.RepositoryLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Repository`` objects.


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





    .. py:method:: can_lookup_repositories():
        :noindex:


    .. py:method:: use_comparative_repository_view():
        :noindex:


    .. py:method:: use_plenary_repository_view():
        :noindex:


    .. py:method:: get_repository(repository_id):
        :noindex:


    .. py:method:: get_repositories_by_ids(repository_ids):
        :noindex:


    .. py:method:: get_repositories_by_genus_type(repository_genus_type):
        :noindex:


    .. py:method:: get_repositories_by_parent_genus_type(repository_genus_type):
        :noindex:


    .. py:method:: get_repositories_by_record_type(repository_record_type):
        :noindex:


    .. py:method:: get_repositories_by_provider(resource_id):
        :noindex:


    .. py:method:: get_repositories():
        :noindex:


    .. py:attribute:: repositories
        :noindex:


Repository Query Session
------------------------

.. py:class:: RepositoryQuerySession(abc_repository_sessions.RepositoryQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``Repository`` objects.


    The search query is constructed using the ``RepositoryQuery``.




    Repositories may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RepositoryQuery``.





    .. py:method:: can_search_repositories():
        :noindex:


    .. py:method:: get_repository_query():
        :noindex:


    .. py:attribute:: repository_query
        :noindex:


    .. py:method:: get_repositories_by_query(repository_query):
        :noindex:


Repository Admin Session
------------------------

.. py:class:: RepositoryAdminSession(abc_repository_sessions.RepositoryAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Repositories``.


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





    .. py:method:: can_create_repositories():
        :noindex:


    .. py:method:: can_create_repository_with_record_types(repository_record_types):
        :noindex:


    .. py:method:: get_repository_form_for_create(repository_record_types):
        :noindex:


    .. py:method:: create_repository(repository_form):
        :noindex:


    .. py:method:: can_update_repositories():
        :noindex:


    .. py:method:: get_repository_form_for_update(repository_id):
        :noindex:


    .. py:method:: update_repository(repository_form):
        :noindex:


    .. py:method:: can_delete_repositories():
        :noindex:


    .. py:method:: delete_repository(repository_id):
        :noindex:


    .. py:method:: can_manage_repository_aliases():
        :noindex:


    .. py:method:: alias_repository(repository_id, alias_id):
        :noindex:


Repository Hierarchy Session
----------------------------

.. py:class:: RepositoryHierarchySession(abc_repository_sessions.RepositoryHierarchySession, osid_sessions.OsidSession)
    This session defines methods for traversing a hierarchy of ``Repository`` objects.


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





    .. py:method:: get_repository_hierarchy_id():
        :noindex:


    .. py:attribute:: repository_hierarchy_id
        :noindex:


    .. py:method:: get_repository_hierarchy():
        :noindex:


    .. py:attribute:: repository_hierarchy
        :noindex:


    .. py:method:: can_access_repository_hierarchy():
        :noindex:


    .. py:method:: use_comparative_repository_view():
        :noindex:


    .. py:method:: use_plenary_repository_view():
        :noindex:


    .. py:method:: get_root_repository_ids():
        :noindex:


    .. py:attribute:: root_repository_ids
        :noindex:


    .. py:method:: get_root_repositories():
        :noindex:


    .. py:attribute:: root_repositories
        :noindex:


    .. py:method:: has_parent_repositories(repository_id):
        :noindex:


    .. py:method:: is_parent_of_repository(id_, repository_id):
        :noindex:


    .. py:method:: get_parent_repository_ids(repository_id):
        :noindex:


    .. py:method:: get_parent_repositories(repository_id):
        :noindex:


    .. py:method:: is_ancestor_of_repository(id_, repository_id):
        :noindex:


    .. py:method:: has_child_repositories(repository_id):
        :noindex:


    .. py:method:: is_child_of_repository(id_, repository_id):
        :noindex:


    .. py:method:: get_child_repository_ids(repository_id):
        :noindex:


    .. py:method:: get_child_repositories(repository_id):
        :noindex:


    .. py:method:: is_descendant_of_repository(id_, repository_id):
        :noindex:


    .. py:method:: get_repository_node_ids(repository_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


    .. py:method:: get_repository_nodes(repository_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


Repository Hierarchy Design Session
-----------------------------------

.. py:class:: RepositoryHierarchyDesignSession(abc_repository_sessions.RepositoryHierarchyDesignSession, osid_sessions.OsidSession)
    This session defines methods for managing a hierarchy of ``Repository`` objects.


    Each node in the hierarchy is a unique ``Repository``.





    .. py:method:: get_repository_hierarchy_id():
        :noindex:


    .. py:attribute:: repository_hierarchy_id
        :noindex:


    .. py:method:: get_repository_hierarchy():
        :noindex:


    .. py:attribute:: repository_hierarchy
        :noindex:


    .. py:method:: can_modify_repository_hierarchy():
        :noindex:


    .. py:method:: add_root_repository(repository_id):
        :noindex:


    .. py:method:: remove_root_repository(repository_id):
        :noindex:


    .. py:method:: add_child_repository(repository_id, child_id):
        :noindex:


    .. py:method:: remove_child_repository(repository_id, child_id):
        :noindex:


    .. py:method:: remove_child_repositories(repository_id):
        :noindex:


