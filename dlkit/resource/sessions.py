
from ..osid import sessions as osid_sessions


class ResourceLookupSession(osid_sessions.OsidSession):
    """This session defines methods for retrieving resources.

    A ``Resource`` is an arbitrary entity that may represent a person,
    place or thing used to identify an object used in various services.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * isolated bin view: All resource methods in this session operate,
        retrieve and pertain to resources defined explicitly in the
        current bin. Using an isolated view is useful for managing
        ``Resources`` with the ``ResourceAdminSession.``
      * federated bin view: All resource methods in this session
        operate, retrieve and pertain to all resources defined in this
        bin and any other resources implicitly available in this bin
        through bin inheritence.


    The methods ``use_federated_bin_view()`` and
    ``use_isolated_bin_view()`` behave as a radio group and one should
    be selected before invoking any lookup methods.

    Resources may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Resource``.

    """

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        :return: the ``Bin Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        :return: the ``Bin`` associated with this session
        :rtype: ``osid.resource.Bin``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    bin = property(fget=get_bin)

    def can_lookup_resources(self):
        """Tests if this user can perform ``Resource`` lookups.

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

    def use_comparative_resource_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_resource_view(self):
        """A complete view of the ``Resource`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_resource(self, resource_id):
        """Gets the ``Resource`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Resource`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Resource`` and retained for
        compatibility.

        :param resource_id: the ``Id`` of the ``Resource`` to retrieve
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``NotFound`` -- no ``Resource`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    def get_resources_by_ids(self, resource_ids):
        """Gets a ``ResourceList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the resources
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Resources`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param resource_ids: the list of ``Ids`` to retrieve
        :type resource_ids: ``osid.id.IdList``
        :return: the returned ``Resource`` list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``resource_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList

    def get_resources_by_genus_type(self, resource_genus_type):
        """Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` which does not include resources of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :param resource_genus_type: a resource genus type
        :type resource_genus_type: ``osid.type.Type``
        :return: the returned ``Resource`` list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList

    def get_resources_by_parent_genus_type(self, resource_genus_type):
        """Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` and include any additional resources with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :param resource_genus_type: a resource genus type
        :type resource_genus_type: ``osid.type.Type``
        :return: the returned ``Resource`` list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``resource_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList

    def get_resources_by_record_type(self, resource_record_type):
        """Gets a ``ResourceList`` containing the given resource record ``Type``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :param resource_record_type: a resource record type
        :type resource_record_type: ``osid.type.Type``
        :return: the returned ``Resource`` list
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList

    def get_resources(self):
        """Gets all ``Resources``.

        In plenary mode, the returned list contains all known resources
        or an error results. Otherwise, the returned list may contain
        only those resources that are accessible through this session.

        :return: a list of ``Resources``
        :rtype: ``osid.resource.ResourceList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList

    resources = property(fget=get_resources)


class ResourceQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Resource`` objects.

    The search query is constructed using the ``ResourceQuery``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bin view: searches include resources in bins of which
        this bin is a ancestor in the bin hierarchy
      * isolated bin view: searches are restricted to resources in this
        bin


    Resources may have a resource record indicated by their respective
    record types. The resource query record is accessed via the
    ``ResourceQuery``.

    """

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        :return: the ``Bin Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        :return: the ``Bin`` associated with this session
        :rtype: ``osid.resource.Bin``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    bin = property(fget=get_bin)

    def can_search_resources(self):
        """Tests if this user can perform ``Resource`` searches.

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

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_resource_query(self):
        """Gets a resource query.

        The returned query will not have an extension query.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    def get_resources_by_query(self, resource_query):
        """Gets a list of ``Resources`` matching the given resource query.

        :param resource_query: the resource query
        :type resource_query: ``osid.resource.ResourceQuery``
        :return: the returned ``ResourceList``
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``resource_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList


class ResourceSearchSession(ResourceQuerySession):
    """This session provides methods for searching among ``Resource`` objects.

    The search query is constructed using the ``ResourceQuery``.

    ``get_resources_by_query()`` is the basic search method and returns
    a list of ``Resources``. A more advanced search may be performed
    with ``getResourcesBySearch()``. It accepts an ``ResourceSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_resources_by_search()`` returns an ``ResourceSearchResults``
    that can be used to access the resulting ``ResourceList`` or be used
    to perform a search within the result set through ``ResourceList``.

    This session defines views that offer differing behaviors for
    searching.

      * federated bin view: searches include resources in bins of which
        this bin is a ancestor in the bin hierarchy
      * isolated bin view: searches are restricted to resources in this
        bin


    Resources may have a resource query record indicated by their
    respective record types. The resource query record is accessed via
    the ``ResourceQuery``.

    """

    def get_resource_search(self):
        """Gets a resource search.

        :return: the resource search
        :rtype: ``osid.resource.ResourceSearch``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceSearch

    resource_search = property(fget=get_resource_search)

    def get_resource_search_order(self):
        """Gets a resource search order.

        The ``ResourceSearchOrder`` is supplied to a ``ResourceSearch``
        to specify the ordering of results.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceSearchOrder

    resource_search_order = property(fget=get_resource_search_order)

    def get_resources_by_search(self, resource_query, resource_search):
        """Gets the search results matching the given search query using the given search.

        :param resource_query: the resource query
        :type resource_query: ``osid.resource.ResourceQuery``
        :param resource_search: the resource search
        :type resource_search: ``osid.resource.ResourceSearch``
        :return: the resource search results
        :rtype: ``osid.resource.ResourceSearchResults``
        :raise: ``NullArgument`` -- ``resource_query`` or ``resource_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_query`` or ``resource_search`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceSearchResults

    def get_resource_query_from_inspector(self, resource_query_inspector):
        """Gets a resource query from an inspector.

        The inspector is available from a ``ResourceSearchResults``.

        :param resource_query_inspector: a resource query inspector
        :type resource_query_inspector: ``osid.resource.ResourceQueryInspector``
        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``NullArgument`` -- ``resource_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``resource_query_inspector`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceQuery


class ResourceAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Resources``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Resource,`` a ``ResourceForm`` is requested using
    ``get_resource_form_for_create()`` specifying desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``ResourceForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``ResourceForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``ResourceForm``
    corresponds to an attempted transaction.

    For updates, ``ResourceForms`` are requested to the ``Resource``
    ``Id`` that is to be updated using ``getResourceFormForUpdate()``.
    Similarly, the ``ResourceForm`` has metadata about the data that can
    be updated and it can perform validation before submitting the
    update. The ``ResourceForm`` can only be used once for a successful
    update and cannot be reused.

    The delete operations delete ``Resources``. To unmap a ``Resource``
    from the current ``Bin,`` the ``ResourceBinAssignmentSession``
    should be used. These delete operations attempt to remove the
    ``Resource`` itself thus removing it from all known ``Bin``
    catalogs.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        :return: the ``Bin Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        :return: the ``Bin`` associated with this session
        :rtype: ``osid.resource.Bin``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    bin = property(fget=get_bin)

    def can_create_resources(self):
        """Tests if this user can create ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Resource`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_resource_with_record_types(self, resource_record_types):
        """Tests if this user can create a single ``Resource`` using the desired record types.

        While ``ResourceManager.getResourceRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Resource``.
        Providing an empty array tests if a ``Resource`` can be created
        with no records.

        :param resource_record_types: array of resource record types
        :type resource_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Resource`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_resource_form_for_create(self, resource_record_types):
        """Gets the resource form for creating new resources.

        A new form should be requested for each create transaction.

        :param resource_record_types: array of resource record types
        :type resource_record_types: ``osid.type.Type[]``
        :return: the resource form
        :rtype: ``osid.resource.ResourceForm``
        :raise: ``NullArgument`` -- ``resource_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceForm

    def create_resource(self, resource_form):
        """Creates a new ``Resource``.

        :param resource_form: the form for this ``Resource``
        :type resource_form: ``osid.resource.ResourceForm``
        :return: the new ``Resource``
        :rtype: ``osid.resource.Resource``
        :raise: ``IllegalState`` -- ``resource_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``resource_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_form`` did not originate from ``get_resource_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    def can_update_resources(self):
        """Tests if this user can update ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Resource`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_resource_form_for_update(self, resource_id):
        """Gets the resource form for updating an existing resource.

        A new resource form should be requested for each update
        transaction.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: the resource form
        :rtype: ``osid.resource.ResourceForm``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceForm

    def update_resource(self, resource_form):
        """Updates an existing resource.

        :param resource_form: the form containing the elements to be updated
        :type resource_form: ``osid.resource.ResourceForm``
        :raise: ``IllegalState`` -- ``resource_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``resource_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``resource_form`` did not originate from ``get_resource_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_resources(self):
        """Tests if this user can delete ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Resource`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Resource`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_resource(self, resource_id):
        """Deletes a ``Resource``.

        :param resource_id: the ``Id`` of the ``Resource`` to remove
        :type resource_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``resource_id`` not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_resource_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Resources``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Resource`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_resource(self, resource_id, alias_id):
        """Adds an ``Id`` to a ``Resource`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Resource`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another resource it is
        reassigned to the given resource ``Id``.

        :param resource_id: the ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``resource_id`` not found
        :raise: ``NullArgument`` -- ``alias_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ResourceNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Resource`` objects in this ``Bin``.

    This also includes existing resources that may appear or disappear
    due to changes in the ``Bin`` hierarchy, This session is intended
    for consumers needing to synchronize their state with this service
    without the use of polling. Notifications are cancelled when this
    session is closed.

    The two views defined in this session correspond to the views in the
    ``ResourceLookupSession``.

    """

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        :return: the ``Bin Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        :return: the ``Bin`` associated with this session
        :rtype: ``osid.resource.Bin``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    bin = property(fget=get_bin)

    def can_register_for_resource_notifications(self):
        """Tests if this user can register for ``Resource`` notifications.

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

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this bin only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def register_for_new_resources(self):
        """Register for notifications of new resources.

        ``ResourceReceiver.newResources()`` is invoked when a new
        ``Resource`` is appears in this bin.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_resources(self):
        """Registers for notification of updated resources.

        ``ResourceReceiver.changedResources()`` is invoked when a
        resource in this bin is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_changed_resource(self, resource_id):
        """Registers for notification of an updated resource.

        ``ResourceReceiver.changedResources()`` is invoked when the
        specified resource in this bin is changed.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_resources(self):
        """Registers for notification of deleted resources.

        ``ResourceReceiver.deletedResources()`` is invoked when a
        resource is deleted or removed from this bin.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def register_for_deleted_resource(self, resource_id):
        """Registers for notification of a deleted resource.

        ``ResourceReceiver.deletedResources()`` is invoked when the
        specified resource is deleted or removed from this bin.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def reliable_resource_notifications(self):
        """Reliable notifications are desired.

        In reliable mode, notifications are to be acknowledged using
        ``acknowledge_item_notification()`` .



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def unreliable_resource_notifications(self):
        """Unreliable notifications are desired.

        In unreliable mode, notifications do not need to be
        acknowledged.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def acknowledge_resource_notification(self, notification_id):
        """Acknowledge an resource notification.

        :param notification_id: the ``Id`` of the notification
        :type notification_id: ``osid.id.Id``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ResourceBinSession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Resource`` to ``Bin`` mappings.

    A ``Resource`` may appear in multiple ``Bins``. Each ``Bin`` may
    have its own authorizations governing who is allowed to look at it.

    This lookup session defines several views:

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """

    def use_comparative_bin_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_bin_view(self):
        """A complete view of the ``Resource`` and ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def can_lookup_resource_bin_mappings(self):
        """Tests if this user can perform lookups of resource/bin mappings.

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

    def get_resource_ids_by_bin(self, bin_id):
        """Gets the list of ``Resource``  ``Ids`` associated with a ``Bin``.

        :param bin_id: ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: list of related resource ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_resources_by_bin(self, bin_id):
        """Gets the list of ``Resources`` associated with a ``Bin``.

        :param bin_id: ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: list of related resources
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList

    def get_resource_ids_by_bins(self, bin_ids):
        """Gets the list of ``Resource Ids`` corresponding to a list of ``Bin`` objects.

        :param bin_ids: list of bin ``Ids``
        :type bin_ids: ``osid.id.IdList``
        :return: list of resource ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_resources_by_bins(self, bin_ids):
        """Gets the list of ``Resources`` corresponding to a list of ``Bins``.

        :param bin_ids: list of bin ``Ids``
        :type bin_ids: ``osid.id.IdList``
        :return: list of resources
        :rtype: ``osid.resource.ResourceList``
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceList

    def get_bin_ids_by_resource(self, resource_id):
        """Gets the list of ``Bin``  ``Ids`` mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_bins_by_resource(self, resource_id):
        """Gets the list of ``Bin`` objects mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of bins
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList


class ResourceBinAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Resources`` to ``Bins``.

    A ``Resource`` may map to multiple ``Bin`` objects and removing the
    last reference to a ``Resource`` is the equivalent of deleting it.
    Each ``Bin`` may have its own authorizations governing who is
    allowed to operate on it.

    Moving or adding a reference of a ``Resource`` to another ``Bin`` is
    not a copy operation (eg: does not change its ``Id`` ).

    """

    def can_assign_resources(self):
        """Tests if this user can alter resource/bin mappings.

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

    def can_assign_resources_to_bin(self, bin_id):
        """Tests if this user can alter resource/bin mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied`` . This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_assignable_bin_ids(self, bin_id):
        """Gets a list of bins including and under the given bin node in which any resource can be assigned.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: list of assignable bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_assignable_bin_ids_for_resource(self, bin_id, resource_id):
        """Gets a list of bins including and under the given bin node in which a specific resource can be assigned.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of assignable bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``bin_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def assign_resource_to_bin(self, resource_id, bin_id):
        """Adds an existing ``Resource`` to a ``Bin``.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``resource_id`` is already assigned to ``bin_id``
        :raise: ``NotFound`` -- ``resource_id`` or ``bin_id`` not found
        :raise: ``NullArgument`` -- ``resource_id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_resource_from_bin(self, resource_id, bin_id):
        """Removes a ``Resource`` from a ``Bin``.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``resource_id`` or ``bin_id`` not found or ``resource_id`` not assigned to ``bin_id``
        :raise: ``NullArgument`` -- ``resource_id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class ResourceAgentSession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Resource`` to ``Agent`` mappings.

    An ``Agent`` may map to only one ``Resource`` while a ``Resource``
    may map to multiple ``Agents``.

    This lookup session defines several views

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition

    """

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        :return: the ``Bin Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        :return: the ``Bin`` associated with this session
        :rtype: ``osid.resource.Bin``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    bin = property(fget=get_bin)

    def can_lookup_resource_agent_mappings(self):
        """Tests if this user can perform lookups of resource/agent mappings.

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

    def use_comparative_agent_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_agent_view(self):
        """A complete view of the ``Agent`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_bin_view(self):
        """Federates the view for methods in this session.

        A federated view will include resources in bins which are
        children of this bin in the bin hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_bin_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this bin only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_resource_id_by_agent(self, agent_id):
        """Gets the ``Resource``  ``Id`` associated with the given agent.

        :param agent_id: ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: associated resource
        :rtype: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    def get_resource_by_agent(self, agent_id):
        """Gets the ``Resource`` associated with the given agent.

        :param agent_id: ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: associated resource
        :rtype: ``osid.resource.Resource``
        :raise: ``NotFound`` -- ``agent_id`` is not found
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    def get_agent_ids_by_resource(self, resource_id):
        """Gets the list of ``Agent``  ``Ids`` mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of agent ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_agents_by_resource(self, resource_id):
        """Gets the list of ``Agents`` mapped to a ``Resource``.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of agents
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NotFound`` -- ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.AgentList


class ResourceAgentAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``Resource`` to ``Agents``.

    A ``Resource`` may be associated with multiple ``Agents``. An
    ``Agent`` may map to only one ``Resource``.

    """

    def get_bin_id(self):
        """Gets the ``Bin``  ``Id`` associated with this session.

        :return: the ``Bin Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bin_id = property(fget=get_bin_id)

    def get_bin(self):
        """Gets the ``Bin`` associated with this session.

        :return: the ``Bin`` associated with this session
        :rtype: ``osid.resource.Bin``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    bin = property(fget=get_bin)

    def can_assign_agents(self):
        """Tests if this user can alter resource/agent mappings.

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

    def can_assign_agents_to_resource(self, resource_id):
        """Tests if this user can alter resource/agent mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known location methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def assign_agent_to_resource(self, agent_id, resource_id):
        """Adds an existing ``Agent`` to a ``Resource``.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``agent_id`` is already assigned to ``resource_id``
        :raise: ``NotFound`` -- ``agent_id`` or ``resource_id`` not found
        :raise: ``NullArgument`` -- ``agent_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def unassign_agent_from_resource(self, agent_id, resource_id):
        """Removes an ``Agent`` from a ``Resource``.

        :param agent_id: the ``Id`` of the ``Agent``
        :type agent_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``agent_id`` or ``resource_id`` not found or ``agent_id`` not assigned to ``resource_id``
        :raise: ``NullArgument`` -- ``agent_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BinLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Bin`` objects.

    The ``Bin`` represents a collection resources.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition


    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Bins`` it can access, without breaking execution.
    However, an administrative application may require all ``Bin``
    elements to be available.

    Bins may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Bin``.

    """

    def can_lookup_bins(self):
        """Tests if this user can perform ``Bin`` lookups.

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

    def use_comparative_bin_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_bin_view(self):
        """A complete view of the ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_bin(self, bin_id):
        """Gets the ``Bin`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Bin`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Bin`` and retained for compatibility.

        :param bin_id: ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: the bin
        :rtype: ``osid.resource.Bin``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.resource.Bin

    def get_bins_by_ids(self, bin_ids):
        """Gets a ``BinList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the bins
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Bins`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param bin_ids: the list of ``Ids`` to retrieve
        :type bin_ids: ``osid.id.IdList``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``bin_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    def get_bins_by_genus_type(self, bin_genus_type):
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins of types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :param bin_genus_type: a bin genus type
        :type bin_genus_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    def get_bins_by_parent_genus_type(self, bin_genus_type):
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional bins with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :param bin_genus_type: a bin genus type
        :type bin_genus_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    def get_bins_by_record_type(self, bin_record_type):
        """Gets a ``BinList`` containing the given bin record ``Type``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :param bin_record_type: a bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    def get_bins_by_provider(self, resource_id):
        """Gets a ``BinList`` from the given provider.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Bin list``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    def get_bins(self):
        """Gets all ``Bins``.

        In plenary mode, the returned list contains all known bins or an
        error results. Otherwise, the returned list may contain only
        those bins that are accessible through this session.

        :return: a list of ``Bins``
        :rtype: ``osid.resource.BinList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    bins = property(fget=get_bins)


class BinQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching among ``Bin`` objects.

    The search query is constructed using the ``BinQuery``.

    Bins may have a bin query record indicated by their respective
    record types. The bin query record is accessed via the ``BinQuery``.

    """

    def can_search_bins(self):
        """Tests if this user can perform ``Bin`` searches.

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

    def get_bin_query(self):
        """Gets a bin query.

        The returned query will not have an extension query.

        :return: the bin query
        :rtype: ``osid.resource.BinQuery``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinQuery

    bin_query = property(fget=get_bin_query)

    def get_bins_by_query(self, bin_query):
        """Gets a list of ``Bins`` matching the given bin query.

        :param bin_query: the bin query
        :type bin_query: ``osid.resource.BinQuery``
        :return: the returned ``BinList``
        :rtype: ``osid.resource.BinList``
        :raise: ``NullArgument`` -- ``bin_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a ``bin_query`` is not of this service

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList


class BinAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Bins``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Bin,`` a ``BinForm`` is requested using
    ``get_bin_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``BinForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``BinForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``BinForm`` corresponds
    to an attempted transaction.

    For updates, ``BinForms`` are requested to the ``Bin``  ``Id`` that
    is to be updated using ``getBinFormForUpdate()``. Similarly, the
    ``BinForm`` has metadata about the data that can be updated and it
    can perform validation before submitting the update. The ``BinForm``
    can only be used once for a successful update and cannot be reused.

    The delete operations delete ``Bins``.

    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """

    def can_create_bins(self):
        """Tests if this user can create ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer create
        operations to unauthorized users.

        :return: ``false`` if ``Bin`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def can_create_bin_with_record_types(self, bin_record_types):
        """Tests if this user can create a single ``Bin`` using the desired record types.

        While ``ResourceManager.getBinRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Bin``.
        Providing an empty array tests if a ``Bin`` can be created with
        no records.

        :param bin_record_types: array of bin record types
        :type bin_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Bin`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``bin_record_types`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_bin_form_for_create(self, bin_record_types):
        """Gets the bin form for creating new bins.

        :param bin_record_types: array of bin record types
        :type bin_record_types: ``osid.type.Type[]``
        :return: the bin form
        :rtype: ``osid.resource.BinForm``
        :raise: ``NullArgument`` -- ``bin_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinForm

    def create_bin(self, bin_form):
        """Creates a new ``Bin``.

        :param bin_form: the form for this ``Bin``
        :type bin_form: ``osid.resource.BinForm``
        :return: the new ``Bin``
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- ``bin_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``bin_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``bin_form`` did not originate from ``get_bin_form_for_create()``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    def can_update_bins(self):
        """Tests if this user can update ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer update
        operations to unauthorized users.

        :return: ``false`` if ``Bin`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_bin_form_for_update(self, bin_id):
        """Gets the bin form for updating an existing bin.

        A new bin form should be requested for each update transaction.

        :param bin_id: the ``Id`` of the ``Bin``
        :type bin_id: ``osid.id.Id``
        :return: the bin form
        :rtype: ``osid.resource.BinForm``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinForm

    def update_bin(self, bin_form):
        """Updates an existing bin.

        :param bin_form: the form containing the elements to be updated
        :type bin_form: ``osid.resource.BinForm``
        :raise: ``IllegalState`` -- ``bin_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``bin_id`` or ``bin_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``bin_form`` did not originate from ``get_bin_form_for_update()``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_delete_bins(self):
        """Tests if this user can delete ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Bin``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may not wish to offer delete
        operations to unauthorized users.

        :return: ``false`` if ``Bin`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def delete_bin(self, bin_id):
        """Deletes a ``Bin``.

        :param bin_id: the ``Id`` of the ``Bin`` to remove
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def can_manage_bin_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Bins``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Bin`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def alias_bin(self, bin_id, alias_id):
        """Adds an ``Id`` to a ``Bin`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Bin`` is determined by the provider.
        The new ``Id`` performs as an alias to the primary ``Id``. If
        the alias is a pointer to another bin, it is reassigned to the
        given bin ``Id``.

        :param bin_id: the ``Id`` of a ``Bin``
        :type bin_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class BinHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Bin`` objects.

    Each node in the hierarchy is a unique ``Bin``. The hierarchy may be
    traversed recursively to establish the tree structure through
    ``get_parent_bins()`` and ``getChildBins()``. To relate these
    ``Ids`` to another OSID, ``get_bin_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Bin`` available in the Resource OSID is known to this hierarchy
    but does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_bins()`` or ``get_child_bins()`` in lieu of
    a ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.

      * comparative view: bin elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition

    """

    def get_bin_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_access_bin_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_bin_view(self):
        """The returns from the bin methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_bin_view(self):
        """A complete view of the ``Bin`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_root_bin_ids(self):
        """Gets the root bin ``Ids`` in this hierarchy.

        :return: the root bin ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    root_bin_ids = property(fget=get_root_bin_ids)

    def get_root_bins(self):
        """Gets the root bins in the bin hierarchy.

        A node with no parents is an orphan. While all bin ``Ids`` are
        known to the hierarchy, an orphan does not appear in the
        hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root bins
        :rtype: ``osid.resource.BinList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method is must be implemented.*

        """
        return # osid.resource.BinList

    root_bins = property(fget=get_root_bins)

    def has_parent_bins(self, bin_id):
        """Tests if the ``Bin`` has any parents.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the bin has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_parent_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is a direct parent of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_parent_bin_ids(self, bin_id):
        """Gets the parent ``Ids`` of the given bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the bin
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_parent_bins(self, bin_id):
        """Gets the parents of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the parents of the bin
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    def is_ancestor_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is an ancestor of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def has_child_bins(self, bin_id):
        """Tests if a bin has any children.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``bin_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_child_of_bin(self, id_, bin_id):
        """Tests if a bin is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` not found return ``false``.

        """
        return # boolean

    def get_child_bin_ids(self, bin_id):
        """Gets the child ``Ids`` of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the children of the bin
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    def get_child_bins(self, bin_id):
        """Gets the children of the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :return: the children of the bin
        :rtype: ``osid.resource.BinList``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinList

    def is_descendant_of_bin(self, id_, bin_id):
        """Tests if an ``Id`` is a descendant of a bin.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``bin_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``bin_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``id`` is not found return ``false``.

        """
        return # boolean

    def get_bin_node_ids(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bin node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

    def get_bin_nodes(self, bin_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given bin.

        :param bin_id: the ``Id`` to query
        :type bin_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a bin node
        :rtype: ``osid.resource.BinNode``
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinNode


class BinHierarchyDesignSession(osid_sessions.OsidSession):
    """This session defines methods for managing a hierarchy of ``Bin`` objects.

    Each node in the hierarchy is a unique ``Bin``.

    """

    def get_bin_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    bin_hierarchy_id = property(fget=get_bin_hierarchy_id)

    def get_bin_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    bin_hierarchy = property(fget=get_bin_hierarchy)

    def can_modify_bin_hierarchy(self):
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

    def add_root_bin(self, bin_id):
        """Adds a root bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bin_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``bin_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_root_bin(self, bin_id):
        """Removes a root bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not a root
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def add_child_bin(self, bin_id, child_id):
        """Adds a child to a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``bin_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``bin_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``bin_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_bin(self, bin_id, child_id):
        """Removes a child from a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``bin_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def remove_child_bins(self, bin_id):
        """Removes all children from a bin.

        :param bin_id: the ``Id`` of a bin
        :type bin_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``bin_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``bin_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


