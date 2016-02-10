
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class ResourceProfile(osid_managers.OsidProfile):
    """The resource profile describes interoperability among resource services."""


    def __init__(self):
        self._provider_manager = None
    def supports_resource_lookup(self):
        """Tests if resource lookup is supported.


        :return: ``true`` if resource lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_resource_query(self):
        """Tests if resource query is supported.


        :return: ``true`` if resource query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_resource_search(self):
        """Tests if resource search is supported.


        :return: ``true`` if resource search is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_resource_admin(self):
        """Tests if resource administration is supported.


        :return: ``true`` if resource administration is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_resource_notification(self):
        """Tests if resource notification is supported.


        Messages may be sent when resources are created, modified, or
        deleted.


        :return: ``true`` if resource notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_resource_bin(self):
        """Tests if retrieving mappings of resource and bins is supported.


        :return: ``true`` if resource bin mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_resource_bin_assignment(self):
        """Tests if managing mappings of resource and bins is supported.


        :return: ``true`` if resource bin assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_resource_agent(self):
        """Tests if retrieving mappings of resource and agents is supported.


        :return: ``true`` if resource agent mapping retrieval is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_resource_agent_assignment(self):
        """Tests if managing mappings of resources and agents is supported.


        :return: ``true`` if resource agent assignment is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bin_lookup(self):
        """Tests if bin lookup is supported.


        :return: ``true`` if bin lookup is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bin_query(self):
        """Tests if bin query is supported.


        :return: ``true`` if bin query is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bin_admin(self):
        """Tests if bin administration is supported.


        :return: ``true`` if bin administration is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bin_hierarchy(self):
        """Tests if a bin hierarchy traversal is supported.


        :return: ``true`` if a bin hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_bin_hierarchy_design(self):
        """Tests if a bin hierarchy design is supported.


        :return: ``true`` if a bin hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_resource_record_types(self):
        """Gets all the resource record types supported.


        :return: the list of supported resource record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    resource_record_types = property(fget=get_resource_record_types)

    def get_resource_search_record_types(self):
        """Gets all the resource search record types supported.


        :return: the list of supported resource search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    resource_search_record_types = property(fget=get_resource_search_record_types)

    def get_resource_relationship_record_types(self):
        """Gets the supported ``ResourceRelationship`` record types.


        :return: a list containing the supported ``ResourceRelationship`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)

    def get_resource_relationship_search_record_types(self):
        """Gets the supported ``ResourceRelationship`` search record types.


        :return: a list containing the supported ``ResourceRelationship`` search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)

    def get_bin_record_types(self):
        """Gets all the bin record types supported.


        :return: the list of supported bin record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    bin_record_types = property(fget=get_bin_record_types)

    def get_bin_search_record_types(self):
        """Gets all the bin search record types supported.


        :return: the list of supported bin search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    bin_search_record_types = property(fget=get_bin_search_record_types)
##
# The following methods are from osid.resource.BinLookupSession

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
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


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
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins of types derived
            from the specified ``Type``.


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
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional bins with genus
            types derived from the specified ``Type``.


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


##
# The following methods are from osid.resource.BinQuerySession

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


##
# The following methods are from osid.resource.BinAdminSession

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


##
# The following methods are from osid.resource.BinHierarchySession

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
        """The returns from the bin methods may omit or translate elements based on this session, such as authorization,
            and not result in an error.


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
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
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
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
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


##
# The following methods are from osid.resource.BinHierarchyDesignSession

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




class ResourceManager(osid_managers.OsidManager, osid_sessions.OsidSession, ResourceProfile):
    """The resource manager provides access to resource lookup and creation sessions and provides interoperability tests
        for
    various aspects of this service.


    The sessions included in this manager are:




      * ``ResourceLookupSession:`` a session to retrieve resources
      * ``ResourceQuerySession:`` a session to query resources
      * ``ResourceSearchSession:`` a session to search for resources
      * ``ResourceAdminSession:`` a session to create and delete
        resources
      * ``ResourceNotificationSession:`` a session to receive
        notifications pertaining to resource changes
      * ``ResourceBinSession:`` a session to look up resource to bin
        mappings
      * ``ResourceBinAssignmentSession:`` a session to manage resource
        to bin mappings
      * ``ResourceSmartBinSession:`` a session to manage smart resource
        bins
      * ``MembershipSession:`` a session to query memberships
      * ``GroupSession:`` a session to retrieve group memberships
      * ``GroupAssignmentSession:`` a session to manage groups
      * ``GroupNotificationSession:`` a session to retrieve
        notifications on changes to group membership
      * ``GroupHierarchySession:`` a session to view a group hierarchy
      * ``RsourceAgentSession:`` a session to retrieve ``Resource`` and
        ``Agent`` mappings
      * ``ResourceAgentAssignmentSession:`` a session to manage
        ``Resource`` and ``Agent`` mappings




      * ``ResourceRelationshipLookupSession:`` a session to retrieve
        resource relationships
      * ``ResourceRelationshipQuerySession:`` a session to query for
        resource relationships
      * ``ResourceRelationshipSearchSession:`` a session to search for
        resource relationships
      * ``ResourceRelationshipAdminSession:`` a session to create and
        delete resource relationships
      * ``ResourceRelationshipNotificationSession:`` a session to
        receive notifications pertaining to resource relationshipchanges
      * ``ResourceRelationshipBinSession:`` a session to look up
        resource relationship to bin mappings
      * ``ResourceRelationshipBinAssignmentSession:`` a session to
        manage resource relationship to bin mappings
      * ``ResourceRelationshipSmartBinSession:`` a session to manage
        smart resource relationship bins




      * ``BinLookupSession: a`` session to retrieve bins
      * ``BinQuerySession:`` a session to query bins
      * ``BinSearchSession:`` a session to search for bins
      * ``BinAdminSession:`` a session to create, update and delete bins
      * ``BinNotificationSession:`` a session to receive notifications
        pertaining to changes in bins
      * ``BinHierarchySession:`` a session to traverse bin hierarchies
      * ``BinHierarchyDesignSession:`` a session to manage bin
        hierarchies


    """


    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._bin_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)


    # def _get_view(self, view):
    #     """Gets the currently set view"""
    #     if view in self._views:
    #         return self._views[view]
    #     else:
    #         self._views[view] = DEFAULT
    #         return DEFAULT


    def _set_bin_view(self, session):
        """Sets the underlying bin view to match current view"""
        if self._bin_view == COMPARATIVE:
            try:
                session.use_comparative_bin_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_bin_view()
            except AttributeError:
                pass


    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        if self._proxy is None:
            self._proxy = proxy
        if session_name in self._provider_sessions:
            return self._provider_sessions[session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_bin_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session


    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            return session_class(*args, **kwargs)
        else:
            return session_class(proxy=proxy, *args, **kwargs)


    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:resourceProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('RESOURCE', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('RESOURCE', provider_impl)


    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()


    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC


    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY


    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()
    def get_resource_batch_manager(self):
        """Gets the ``ResourceBatchManager``.


        :return: a ``ResourceBatchManager``
        :rtype: ``osid.resource.batch.ResourceBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_batch()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_resource_batch()`` is ``true``.*


        """
        return # osid.resource.batch.ResourceBatchManager

    resource_batch_manager = property(fget=get_resource_batch_manager)

    def get_resource_demographic_manager(self):
        """Gets the ``ResourceDemographicManager``.


        :return: a ``ResourceDemographicManager``
        :rtype: ``osid.resource.demographic.ResourceDemographicManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_demographic()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_resource_demographic()`` is ``true``.*


        """
        return # osid.resource.demographic.ResourceDemographicManager

    resource_demographic_manager = property(fget=get_resource_demographic_manager)
##
# The following methods are from osid.resource.BinLookupSession

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
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


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
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins of types derived
            from the specified ``Type``.


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
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional bins with genus
            types derived from the specified ``Type``.


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


##
# The following methods are from osid.resource.BinQuerySession

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


##
# The following methods are from osid.resource.BinAdminSession

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


##
# The following methods are from osid.resource.BinHierarchySession

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
        """The returns from the bin methods may omit or translate elements based on this session, such as authorization,
            and not result in an error.


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
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
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
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
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


##
# The following methods are from osid.resource.BinHierarchyDesignSession

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




class ResourceProxyManager(osid_managers.OsidProxyManager, ResourceProfile):
    """The resource manager provides access to resource lookup and creation session and provides interoperability tests
        for
    various aspects of this service.


    Methods in this manager accept a ``Proxy``. The sessions included in
    this manager are:




      * ``ResourceLookupSession:`` a session to retrieve resources
      * ``ResourceQuerySession:`` a session to query resources
      * ``ResourceSearchSession:`` a session to search for resources
      * ``ResourceAdminSession:`` a session to create and delete
        resources
      * ``ResourceNotificationSession:`` a session to receive
        notifications pertaining to resource changes
      * ``ResourceBinSession:`` a session to look up resource to bin
        mappings
      * ``ResourceBinAssignmentSession:`` a session to manage resource
        to bin mappings
      * ``ResourceSmartBinSession:`` a session to manage smart resource
        bins
      * ``MembershipSession:`` a session to query memberships
      * ``GroupSession:`` a session to retrieve group memberships
      * ``GroupAssignmentSession:`` a session to manage groups
      * ``GroupNotificationSession:`` a session to retrieve
        notifications on changes to group membership
      * ``GroupHierarchySession:`` a session to view a group hierarchy
      * ``RsourceAgentSession:`` a session to retrieve ``Resource`` and
        ``Agent`` mappings
      * ``ResourceAgentAssignmentSession:`` a session to manage
        ``Resource`` and ``Agent`` mappings




      * ``ResourceRelationshipLookupSession:`` a session to retrieve
        resource relationships
      * ``ResourceRelationshipQuerySession:`` a session to query for
        resource relationships
      * ``ResourceRelationshipSearchSession:`` a session to search for
        resource relationships
      * ``ResourceRelationshipAdminSession:`` a session to create and
        delete resource relationships
      * ``ResourceRelationshipNotificationSession:`` a session to
        receive notifications pertaining to resource relationshipchanges
      * ``ResourceRelationshipBinSession:`` a session to look up
        resource relationship to bin mappings
      * ``ResourceRelationshipBinAssignmentSession:`` a session to
        manage resource relationship to bin mappings
      * ``ResourceRelationshipSmartBinSession:`` a session to manage
        smart resource relationship bins




      * ``BinLookupSession: a`` session to retrieve bins
      * ``BinQuerySession:`` a session to query bins
      * ``BinSearchSession:`` a session to search for bins
      * ``BinAdminSession:`` a session to create, update and delete bins
      * ``BinNotificationSession:`` a session to receive notifications
        pertaining to changes in bins
      * ``BinHierarchySession:`` a session to traverse bin hierarchies
      * ``BinHierarchyDesignSession:`` a session to manage bin
        hierarchies


    """

    def get_resource_batch_proxy_manager(self):
        """Gets the ``ResourceBatchProxyManager``.


        :return: a ``ResourceBatchProxyManager``
        :rtype: ``osid.resource.batch.ResourceBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_batch()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_resource_batch()`` is ``true``.*


        """
        return # osid.resource.batch.ResourceBatchProxyManager

    resource_batch_proxy_manager = property(fget=get_resource_batch_proxy_manager)

    def get_resource_demographic_proxy_manager(self):
        """Gets the ``ResourceDemographicProxyManager``.


        :return: a ``ResourceDemographicProxyManager``
        :rtype: ``osid.resource.demographic.ResourceDemographicProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_resource_demographic()`` is ``false``


        *compliance: optional -- This method must be implemented if
        ``supports_resource_demographic()`` is ``true``.*


        """
        return # osid.resource.demographic.ResourceDemographicProxyManager

    resource_demographic_proxy_manager = property(fget=get_resource_demographic_proxy_manager)
##
# The following methods are from osid.resource.BinLookupSession

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
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


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
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` which does not include bins of types derived
            from the specified ``Type``.


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
        """Gets a ``BinList`` corresponding to the given bin genus ``Type`` and include any additional bins with genus
            types derived from the specified ``Type``.


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


##
# The following methods are from osid.resource.BinQuerySession

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


##
# The following methods are from osid.resource.BinAdminSession

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


##
# The following methods are from osid.resource.BinHierarchySession

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
        """The returns from the bin methods may omit or translate elements based on this session, such as authorization,
            and not result in an error.


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
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
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
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
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


##
# The following methods are from osid.resource.BinHierarchyDesignSession

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




class Bin(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """An inventory defines a collection of resources."""


    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        osid.OsidObject.__init__(self, self._catalog) # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._bin_view = DEFAULT
        self._object_views = dict()


    def _set_bin_view(self, session):
        """Sets the underlying bin view to match current view"""
        if self._bin_view == FEDERATED:
            try:
                session.use_federated_bin_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_bin_view()
            except AttributeError:
                pass


    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass


    def _get_provider_session(self, session_name):
        """Returns the requested provider session."""
        if session_name in self._provider_sessions:
            return self._provider_sessions[session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_bin')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_bin_view(session)
            self._set_object_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session


    def get_bin_id(self):
        """Gets the Id of this bin."""
        return self._catalog_id


    def get_bin(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self


    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id


    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self


    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError


    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        raise IllegalState()


    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC


    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY


    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()
    def get_bin_record(self, bin_record_type):
        """Gets the bin record corresponding to the given ``Bin`` record ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``bin_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(bin_record_type)`` is
        ``true`` .


        :param bin_record_type: the bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the bin record
        :rtype: ``osid.resource.records.BinRecord``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.resource.records.BinRecord
##
# The following methods are from osid.resource.ResourceLookupSession

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
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


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
        """Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` which does not include resources
            of types derived from the specified ``Type``.


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
        """Gets a ``ResourceList`` corresponding to the given resource genus ``Type`` and include any additional
            resources with genus types derived from the specified ``Type``.


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


##
# The following methods are from osid.resource.ResourceQuerySession

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


##
# The following methods are from osid.resource.ResourceSearchSession

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


##
# The following methods are from osid.resource.ResourceAdminSession

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


##
# The following methods are from osid.resource.ResourceNotificationSession

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


##
# The following methods are from osid.resource.ResourceBinSession

    def use_comparative_bin_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


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


##
# The following methods are from osid.resource.ResourceBinAssignmentSession

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


##
# The following methods are from osid.resource.ResourceAgentSession

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
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


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


##
# The following methods are from osid.resource.ResourceAgentAssignmentSession

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
        :raise: ``NotFound`` -- ``agent_id`` or ``resource_id`` not found or ``agent_id`` not assigned to
            ``resource_id``
        :raise: ``NullArgument`` -- ``agent_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass




class BinList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BinList`` provides a means for accessing ``Bin`` elements sequentially either one at a
        time
    or many at a time.


    Examples: while (bl.hasNext()) { Bin bin = bl.getNextBin(); }




    or
      while (bl.hasNext()) {
           Bin[] bins = bl.getNextBins(bl.available());
      }






    """

    def get_next_bin(self):
        """Gets the next ``Bin`` in this list.


        :return: the next ``Bin`` in this list. The ``has_next()`` method should be used to test that a next ``Bin`` is
            available before calling this method.
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.resource.Bin

    next_bin = property(fget=get_next_bin)

    def get_next_bins(self, n):
        """Gets the next set of ``Bin`` elements in this list which must be less than or equal to the return from
            ``available()``.


        :param n: the number of ``Bin`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Bin`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.resource.Bin


