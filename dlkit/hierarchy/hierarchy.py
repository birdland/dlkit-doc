
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects
from ..osid import records as osid_records
from ..osid import queries as osid_queries
from ..osid import searches as osid_searches


class HierarchyProfile(osid_managers.OsidProfile):
    """The hierarchy profile describes the interoperability among hierarchy services."""


    def __init__(self):
        self._provider_manager = None
    def supports_hierarchy_traversal(self):
        """Tests if hierarchy traversal is supported.


        :return: ``true`` if hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_hierarchy_design(self):
        """Tests if hierarchy design is supported.


        :return: ``true`` if hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_hierarchy_lookup(self):
        """Tests if a hierarchy lookup is supported.


        :return: ``true`` if hierarchy lookup is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def supports_hierarchy_admin(self):
        """Tests if a hierarchy administration is supported.


        :return: ``true`` if hierarchy administration is supported, ``false`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_hierarchy_record_types(self):
        """Gets the supported ``Hierarchy`` types.


        :return: a list containing the supported ``Hierarchy`` record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    hierarchy_record_types = property(fget=get_hierarchy_record_types)

    def get_hierarchy_search_record_types(self):
        """Gets the supported ``Hierarchy`` search record types.


        :return: a list containing the supported ``Hierarchy`` search record types
        :rtype: ``osid.type.TypeList``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.type.TypeList

    hierarchy_search_record_types = property(fget=get_hierarchy_search_record_types)
##
# The following methods are from osid.hierarchy.HierarchyTraversalSession

    def get_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.


        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.


        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    hierarchy = property(fget=get_hierarchy)

    def can_access_hierarchy(self):
        """Tests if this user can perform hierarchy queries.


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

    def get_roots(self):
        """Gets the root nodes of this hierarchy.


        :return: the root nodes
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    roots = property(fget=get_roots)

    def has_parents(self, id_):
        """Tests if this ``Id`` contains any parents.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` contains parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def is_parent(self, id_, parent_id):
        """Tests if an ``Id`` is a direct parent of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param parent_id: the ``Id`` of a parent
        :type parent_id: ``osid.id.Id``
        :return: ``true`` if this ``parent_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``parent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``parent_id`` not found return
        ``false``.


        """
        return # boolean

    def get_parents(self, id_):
        """Gets the parents of the given ``id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the parents of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def is_ancestor(self, id_, ancestor_id):
        """Tests if an ``Id`` is an ancestor of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of an ancestor
        :type ancestor_id: ``osid.id.Id``
        :return: ``true`` if this ``ancestor_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ancestor_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``ancestor_id`` not found return
        ``false``.


        """
        return # boolean

    def has_children(self, id_):
        """Tests if this ``Id`` has any children.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def is_child(self, id_, child_id):
        """Tests if a node is a direct child of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of a child
        :type child_id: ``osid.id.Id``
        :return: ``true`` if this ``child_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``child_id`` not found return
        ``false``.


        """
        return # boolean

    def get_children(self, id_):
        """Gets the children of the given ``Id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the children of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def is_descendant(self, id_, descendant_id):
        """Tests if a node is a descendant of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of a descendant
        :type descendant_id: ``osid.id.Id``
        :return: ``true`` if this ``descendant_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``descendant`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If not found return ``false``.


        """
        return # boolean

    def get_nodes(self, id_, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given ``Id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Node


##
# The following methods are from osid.hierarchy.HierarchyDesignSession

    def get_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.


        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.


        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    hierarchy = property(fget=get_hierarchy)

    def can_modify_hierarchy(self):
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

    def add_root(self, id_):
        """Adds a root node.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``id`` is already in hierarchy
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def add_child(self, id_, child_id):
        """Adds a child to a ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``child_id`` is already a child of ``id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_root(self, id_):
        """Removes a root node.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` was not found or not in hierarchy
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_child(self, id_, child_id):
        """Removes a childfrom an ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child to remove
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` was not found or ``child_id`` is not a child of ``id``
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_children(self, id_):
        """Removes all childrenfrom an ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- an node identified by the given ``Id`` was not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


##
# The following methods are from osid.hierarchy.HierarchyLookupSession

    def can_lookup_hierarchies(self):
        """Tests if this user can perform ``Hierarchy`` lookups.


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

    def use_comparative_hierarchy_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_hierarchy_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_hierarchy(self, hierarchy_id):
        """Gets the ``Hierarchy`` specified by its ``Id``.


        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Hierarchy`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Hierarchy`` and retained
        for compati


        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to retrieve
        :type hierarchy_id: ``osid.id.Id``
        :return: the returned ``Hierarchy``
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``NotFound`` -- no ``Hierarchy`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    def get_hierarchies_by_ids(self, hierarchy_ids):
        """Gets a ``Hierarchy`` corresponding to the given ``IdList``.


        In plenary mode, the returned list contains all of the
        hierarchies specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Hierarchy`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.


        :param hierarchy_ids: the list of ``Ids`` to retrieve
        :type hierarchy_ids: ``osid.id.IdList``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``hierarchy_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given genus ``Type`` which does not include hierarchies of
            types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_parent_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy genus ``Type`` and include any additional
            hierarchies with types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_record_type(self, hierarchy_record_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy record ``Type``.


        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_provider(self, resource_id):
        """Gets a ``HierarchyList`` for the given provider ````.


        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies(self):
        """Gets all hierarchies.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :return: a list of ``Hierarchies``
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    hierarchies = property(fget=get_hierarchies)


##
# The following methods are from osid.hierarchy.HierarchyAdminSession

    def can_create_hierarchies(self):
        """Tests if this user can create ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_create_hierarchy_with_record_types(self, hierarchy_record_types):
        """Tests if this user can create a single ``Hierarchy`` using the desired record types.


        While ``HierarchyManager.getHierarchyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Hierarchy``.
        Providing an empty array tests if a ``Hierarchy`` can be created
        with no records.


        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Hierarchy`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_hierarchy_form_for_create(self, hierarchy_record_types):
        """Gets the hierarchy form for creating new hierarchies.


        A new form should be requested for each create transaction. This
        method is used for creating new hierarchies, where only the
        ``Hierarchy`` ``Type`` is known.


        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyForm

    def create_hierarchy(self, hierarchy_form):
        """Creates a new ``Hierarchy``.


        :param hierarchy_form: the form for this ``Hierarchy``
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :return: the new ``Hierarchy``
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_create()``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    def can_update_hierarchies(self):
        """Tests if this user can update ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_hierarchy_form_for_update(self, hierarchy_id):
        """Gets the hierarchy form for updating an existing hierarchy.


        A new hierarchy form should be requested for each update
        transaction.


        :param hierarchy_id: the ``Id`` of the ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyForm

    def update_hierarchy(self, hierarchy_form):
        """Updates an existing hierarchy.


        :param hierarchy_form: the form containing the elements to be updated
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_update()``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_delete_hierarchies(self):
        """Tests if this user can delete ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def delete_hierarchy(self, hierarchy_id):
        """Deletes a ``Hierarchy``.


        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to remove
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_manage_hierarchy_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Hierarchy`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def alias_hierarchy(self, hierarchy_id, alias_id):
        """Adds an ``Id`` to a ``Hierarchy`` for the purpose of creating compatibility.


        The primary ``Id`` of the ``Hierarchy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.


        :param hierarchy_id: the ``Id`` of an ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass




class HierarchyManager(osid_managers.OsidManager, osid_sessions.OsidSession, HierarchyProfile):
    """The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.


    The sessions included in this manager are:




      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies


    """


    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._hierarchy_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)


    # def _get_view(self, view):
    #     """Gets the currently set view"""
    #     if view in self._views:
    #         return self._views[view]
    #     else:
    #         self._views[view] = DEFAULT
    #         return DEFAULT


    def _set_hierarchy_view(self, session):
        """Sets the underlying hierarchy view to match current view"""
        if self._hierarchy_view == COMPARATIVE:
            try:
                session.use_comparative_hierarchy_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_hierarchy_view()
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
            self._set_hierarchy_view(session)
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
        parameter_id = Id('parameter:hierarchyProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('HIERARCHY', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('HIERARCHY', provider_impl)


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

##
# The following methods are from osid.hierarchy.HierarchyTraversalSession

    def get_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.


        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.


        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    hierarchy = property(fget=get_hierarchy)

    def can_access_hierarchy(self):
        """Tests if this user can perform hierarchy queries.


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

    def get_roots(self):
        """Gets the root nodes of this hierarchy.


        :return: the root nodes
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    roots = property(fget=get_roots)

    def has_parents(self, id_):
        """Tests if this ``Id`` contains any parents.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` contains parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def is_parent(self, id_, parent_id):
        """Tests if an ``Id`` is a direct parent of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param parent_id: the ``Id`` of a parent
        :type parent_id: ``osid.id.Id``
        :return: ``true`` if this ``parent_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``parent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``parent_id`` not found return
        ``false``.


        """
        return # boolean

    def get_parents(self, id_):
        """Gets the parents of the given ``id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the parents of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def is_ancestor(self, id_, ancestor_id):
        """Tests if an ``Id`` is an ancestor of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of an ancestor
        :type ancestor_id: ``osid.id.Id``
        :return: ``true`` if this ``ancestor_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ancestor_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``ancestor_id`` not found return
        ``false``.


        """
        return # boolean

    def has_children(self, id_):
        """Tests if this ``Id`` has any children.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def is_child(self, id_, child_id):
        """Tests if a node is a direct child of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of a child
        :type child_id: ``osid.id.Id``
        :return: ``true`` if this ``child_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``child_id`` not found return
        ``false``.


        """
        return # boolean

    def get_children(self, id_):
        """Gets the children of the given ``Id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the children of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def is_descendant(self, id_, descendant_id):
        """Tests if a node is a descendant of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of a descendant
        :type descendant_id: ``osid.id.Id``
        :return: ``true`` if this ``descendant_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``descendant`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If not found return ``false``.


        """
        return # boolean

    def get_nodes(self, id_, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given ``Id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Node


##
# The following methods are from osid.hierarchy.HierarchyDesignSession

    def get_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.


        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.


        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    hierarchy = property(fget=get_hierarchy)

    def can_modify_hierarchy(self):
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

    def add_root(self, id_):
        """Adds a root node.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``id`` is already in hierarchy
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def add_child(self, id_, child_id):
        """Adds a child to a ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``child_id`` is already a child of ``id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_root(self, id_):
        """Removes a root node.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` was not found or not in hierarchy
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_child(self, id_, child_id):
        """Removes a childfrom an ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child to remove
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` was not found or ``child_id`` is not a child of ``id``
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_children(self, id_):
        """Removes all childrenfrom an ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- an node identified by the given ``Id`` was not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


##
# The following methods are from osid.hierarchy.HierarchyLookupSession

    def can_lookup_hierarchies(self):
        """Tests if this user can perform ``Hierarchy`` lookups.


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

    def use_comparative_hierarchy_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_hierarchy_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_hierarchy(self, hierarchy_id):
        """Gets the ``Hierarchy`` specified by its ``Id``.


        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Hierarchy`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Hierarchy`` and retained
        for compati


        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to retrieve
        :type hierarchy_id: ``osid.id.Id``
        :return: the returned ``Hierarchy``
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``NotFound`` -- no ``Hierarchy`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    def get_hierarchies_by_ids(self, hierarchy_ids):
        """Gets a ``Hierarchy`` corresponding to the given ``IdList``.


        In plenary mode, the returned list contains all of the
        hierarchies specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Hierarchy`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.


        :param hierarchy_ids: the list of ``Ids`` to retrieve
        :type hierarchy_ids: ``osid.id.IdList``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``hierarchy_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given genus ``Type`` which does not include hierarchies of
            types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_parent_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy genus ``Type`` and include any additional
            hierarchies with types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_record_type(self, hierarchy_record_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy record ``Type``.


        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_provider(self, resource_id):
        """Gets a ``HierarchyList`` for the given provider ````.


        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies(self):
        """Gets all hierarchies.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :return: a list of ``Hierarchies``
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    hierarchies = property(fget=get_hierarchies)


##
# The following methods are from osid.hierarchy.HierarchyAdminSession

    def can_create_hierarchies(self):
        """Tests if this user can create ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_create_hierarchy_with_record_types(self, hierarchy_record_types):
        """Tests if this user can create a single ``Hierarchy`` using the desired record types.


        While ``HierarchyManager.getHierarchyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Hierarchy``.
        Providing an empty array tests if a ``Hierarchy`` can be created
        with no records.


        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Hierarchy`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_hierarchy_form_for_create(self, hierarchy_record_types):
        """Gets the hierarchy form for creating new hierarchies.


        A new form should be requested for each create transaction. This
        method is used for creating new hierarchies, where only the
        ``Hierarchy`` ``Type`` is known.


        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyForm

    def create_hierarchy(self, hierarchy_form):
        """Creates a new ``Hierarchy``.


        :param hierarchy_form: the form for this ``Hierarchy``
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :return: the new ``Hierarchy``
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_create()``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    def can_update_hierarchies(self):
        """Tests if this user can update ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_hierarchy_form_for_update(self, hierarchy_id):
        """Gets the hierarchy form for updating an existing hierarchy.


        A new hierarchy form should be requested for each update
        transaction.


        :param hierarchy_id: the ``Id`` of the ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyForm

    def update_hierarchy(self, hierarchy_form):
        """Updates an existing hierarchy.


        :param hierarchy_form: the form containing the elements to be updated
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_update()``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_delete_hierarchies(self):
        """Tests if this user can delete ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def delete_hierarchy(self, hierarchy_id):
        """Deletes a ``Hierarchy``.


        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to remove
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_manage_hierarchy_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Hierarchy`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def alias_hierarchy(self, hierarchy_id, alias_id):
        """Adds an ``Id`` to a ``Hierarchy`` for the purpose of creating compatibility.


        The primary ``Id`` of the ``Hierarchy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.


        :param hierarchy_id: the ``Id`` of an ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass




class HierarchyProxyManager(osid_managers.OsidProxyManager, HierarchyProfile):
    """The hierarchy manager provides access sessions to traverse and manage hierrachies of ``Ids``.


    Methods in this manager accept a ``Proxy`` to pass information from
    server environments. The sessions included in this manager are:




      * ``HierarchyTraversalSession:`` a basic session traversing a
        hierarchy
      * ``HierarchyDesignSession:`` a session to design a hierarchy
      * ``HierarchySequencingSession:`` a session to sequence nodes in a
        hierarchy
      * ``HierarchyStructureNotificationSession:`` a session for
        notififcations within a hierarchy structure
      * ``HierarchyLookupSession:`` a session looking up hiererachies
      * ``HierarchyQuerySession:`` a session querying hiererachies
      * ``HierarchySearchSession:`` a session for searching for
        hierarchies
      * ``HierarchyAdminSession:`` a session for creating and deleting
        hierarchies
      * ``HierarchyNotificationSession:`` a session for subscribing to
        changes in hierarchies


    """


##
# The following methods are from osid.hierarchy.HierarchyTraversalSession

    def get_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.


        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.


        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    hierarchy = property(fget=get_hierarchy)

    def can_access_hierarchy(self):
        """Tests if this user can perform hierarchy queries.


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

    def get_roots(self):
        """Gets the root nodes of this hierarchy.


        :return: the root nodes
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    roots = property(fget=get_roots)

    def has_parents(self, id_):
        """Tests if this ``Id`` contains any parents.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` contains parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def is_parent(self, id_, parent_id):
        """Tests if an ``Id`` is a direct parent of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param parent_id: the ``Id`` of a parent
        :type parent_id: ``osid.id.Id``
        :return: ``true`` if this ``parent_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``parent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``parent_id`` not found return
        ``false``.


        """
        return # boolean

    def get_parents(self, id_):
        """Gets the parents of the given ``id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the parents of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def is_ancestor(self, id_, ancestor_id):
        """Tests if an ``Id`` is an ancestor of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of an ancestor
        :type ancestor_id: ``osid.id.Id``
        :return: ``true`` if this ``ancestor_id`` is a parent of ``id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``ancestor_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``ancestor_id`` not found return
        ``false``.


        """
        return # boolean

    def has_children(self, id_):
        """Tests if this ``Id`` has any children.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: ``true`` if this ``Id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def is_child(self, id_, child_id):
        """Tests if a node is a direct child of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of a child
        :type child_id: ``osid.id.Id``
        :return: ``true`` if this ``child_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``child_id`` not found return
        ``false``.


        """
        return # boolean

    def get_children(self, id_):
        """Gets the children of the given ``Id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :return: the children of the ``id``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.IdList

    def is_descendant(self, id_, descendant_id):
        """Tests if a node is a descendant of another.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of a descendant
        :type descendant_id: ``osid.id.Id``
        :return: ``true`` if this ``descendant_id`` is a child of the ``Id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``descendant`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If not found return ``false``.


        """
        return # boolean

    def get_nodes(self, id_, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given ``Id``.


        :param id: the ``Id`` to query
        :type id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the
            node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children
            in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``id`` is not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Node


##
# The following methods are from osid.hierarchy.HierarchyDesignSession

    def get_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.


        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.id.Id

    hierarchy_id = property(fget=get_hierarchy_id)

    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.


        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    hierarchy = property(fget=get_hierarchy)

    def can_modify_hierarchy(self):
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

    def add_root(self, id_):
        """Adds a root node.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``id`` is already in hierarchy
        :raise: ``NotFound`` -- ``id`` not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def add_child(self, id_, child_id):
        """Adds a child to a ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``child_id`` is already a child of ``id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_root(self, id_):
        """Removes a root node.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` was not found or not in hierarchy
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_child(self, id_, child_id):
        """Removes a childfrom an ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :param child_id: the ``Id`` of the child to remove
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``id`` or ``child_id`` was not found or ``child_id`` is not a child of ``id``
        :raise: ``NullArgument`` -- ``id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def remove_children(self, id_):
        """Removes all childrenfrom an ``Id``.


        :param id: the ``Id`` of the node
        :type id: ``osid.id.Id``
        :raise: ``NotFound`` -- an node identified by the given ``Id`` was not found
        :raise: ``NullArgument`` -- ``id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass


##
# The following methods are from osid.hierarchy.HierarchyLookupSession

    def can_lookup_hierarchies(self):
        """Tests if this user can perform ``Hierarchy`` lookups.


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

    def use_comparative_hierarchy_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as
            authorization, and not result in an error.


        This view is used when greater interoperability is desired at
        the expense of precision.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def use_plenary_hierarchy_view(self):
        """A complete view of the ``Hierarchy`` returns is desired.


        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.






        *compliance: mandatory -- This method is must be implemented.*


        """
        pass

    def get_hierarchy(self, hierarchy_id):
        """Gets the ``Hierarchy`` specified by its ``Id``.


        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Hierarchy`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Hierarchy`` and retained
        for compati


        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to retrieve
        :type hierarchy_id: ``osid.id.Id``
        :return: the returned ``Hierarchy``
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``NotFound`` -- no ``Hierarchy`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    def get_hierarchies_by_ids(self, hierarchy_ids):
        """Gets a ``Hierarchy`` corresponding to the given ``IdList``.


        In plenary mode, the returned list contains all of the
        hierarchies specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Hierarchy`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.


        :param hierarchy_ids: the list of ``Ids`` to retrieve
        :type hierarchy_ids: ``osid.id.IdList``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``hierarchy_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given genus ``Type`` which does not include hierarchies of
            types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_parent_genus_type(self, hierarchy_genus_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy genus ``Type`` and include any additional
            hierarchies with types derived from the specified ``Type``.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_genus_type: a hierarchy genus type
        :type hierarchy_genus_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_record_type(self, hierarchy_record_type):
        """Gets a ``HierarchyList`` corresponding to the given hierarchy record ``Type``.


        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param hierarchy_record_type: a hierarchy record type
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies_by_provider(self, resource_id):
        """Gets a ``HierarchyList`` for the given provider ````.


        The set of hierarchies implementing the given record type are
        returned.In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Hierarchy`` list
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    def get_hierarchies(self):
        """Gets all hierarchies.


        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.


        :return: a list of ``Hierarchies``
        :rtype: ``osid.hierarchy.HierarchyList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyList

    hierarchies = property(fget=get_hierarchies)


##
# The following methods are from osid.hierarchy.HierarchyAdminSession

    def can_create_hierarchies(self):
        """Tests if this user can create ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def can_create_hierarchy_with_record_types(self, hierarchy_record_types):
        """Tests if this user can create a single ``Hierarchy`` using the desired record types.


        While ``HierarchyManager.getHierarchyRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Hierarchy``.
        Providing an empty array tests if a ``Hierarchy`` can be created
        with no records.


        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Hierarchy`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_hierarchy_form_for_create(self, hierarchy_record_types):
        """Gets the hierarchy form for creating new hierarchies.


        A new form should be requested for each create transaction. This
        method is used for creating new hierarchies, where only the
        ``Hierarchy`` ``Type`` is known.


        :param hierarchy_record_types: array of hierarchy record types
        :type hierarchy_record_types: ``osid.type.Type[]``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NullArgument`` -- ``hierarchy_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyForm

    def create_hierarchy(self, hierarchy_form):
        """Creates a new ``Hierarchy``.


        :param hierarchy_form: the form for this ``Hierarchy``
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :return: the new ``Hierarchy``
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_create()``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    def can_update_hierarchies(self):
        """Tests if this user can update ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def get_hierarchy_form_for_update(self, hierarchy_id):
        """Gets the hierarchy form for updating an existing hierarchy.


        A new hierarchy form should be requested for each update
        transaction.


        :param hierarchy_id: the ``Id`` of the ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :return: the hierarchy form
        :rtype: ``osid.hierarchy.HierarchyForm``
        :raise: ``NotFound`` -- ``hierarchy_id`` is not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.HierarchyForm

    def update_hierarchy(self, hierarchy_form):
        """Updates an existing hierarchy.


        :param hierarchy_form: the form containing the elements to be updated
        :type hierarchy_form: ``osid.hierarchy.HierarchyForm``
        :raise: ``IllegalState`` -- ``hierarchy_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``hierarchy_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``hierarchy_form`` did not originate from ``get_hierarchy_form_for_update()``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_delete_hierarchies(self):
        """Tests if this user can delete ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Hierarchy`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Hierarchy`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def delete_hierarchy(self, hierarchy_id):
        """Deletes a ``Hierarchy``.


        :param hierarchy_id: the ``Id`` of the ``Hierarchy`` to remove
        :type hierarchy_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def can_manage_hierarchy_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Hierarchy`` objects.


        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Hierarchy`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # boolean

    def alias_hierarchy(self, hierarchy_id, alias_id):
        """Adds an ``Id`` to a ``Hierarchy`` for the purpose of creating compatibility.


        The primary ``Id`` of the ``Hierarchy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.


        :param hierarchy_id: the ``Id`` of an ``Hierarchy``
        :type hierarchy_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``hierarchy_id`` not found
        :raise: ``NullArgument`` -- ``hierarchy_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure


        *compliance: mandatory -- This method must be implemented.*


        """
        pass




class Hierarchy(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A ``Hierarchy`` represents an authenticatable identity.


    Like all OSID objects, a ``Hierarchy`` is identified by its Id and
    any persisted references should use the Id.


    """


    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        osid.OsidObject.__init__(self, self._catalog) # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._hierarchy_view = DEFAULT
        self._object_views = dict()


    def _set_hierarchy_view(self, session):
        """Sets the underlying hierarchy view to match current view"""
        if self._hierarchy_view == FEDERATED:
            try:
                session.use_federated_hierarchy_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_hierarchy_view()
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
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_hierarchy')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_hierarchy_view(session)
            self._set_object_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session


    def get_hierarchy_id(self):
        """Gets the Id of this hierarchy."""
        return self._catalog_id


    def get_hierarchy(self):
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
    def get_hierarchy_record(self, hierarchy_record_type):
        """Gets the hierarchy record corresponding to the given ``Hierarchy`` record ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``hierarchy_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(hierarchy_record_type)`` is ``true`` .


        :param hierarchy_record_type: the type of the record to retrieve
        :type hierarchy_record_type: ``osid.type.Type``
        :return: the hierarchy record
        :rtype: ``osid.hierarchy.records.HierarchyRecord``
        :raise: ``NullArgument`` -- ``hierarchy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(hierarchyrecord_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.records.HierarchyRecord


class HierarchyList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``HierarchyList`` provides a means for accessing ``Id`` elements sequentially either one
        at a
    time or many at a time.


    Examples: while (hl.hasNext()) { Hierarchy hierarchy =
    hl.getNextHierarchy(); }




    or
      while (hl.hasNext()) {
           Hierarchy[] hierarchies = hl.getNextHierarchies(hl.available());
      }






    """

    def get_next_hierarchy(self):
        """Gets the next ``Hierarchy`` in this list.


        :return: the next ``Hierarchy`` in this list. The ``has_next()`` method should be used to test that a next
            ``Hierarchy`` is available before calling this method.
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy

    next_hierarchy = property(fget=get_next_hierarchy)

    def get_next_hierarchies(self, n):
        """Gets the next set of ``Hierarchy`` objects in this list.


        The specified amount must be less than or equal to the return
        from ``available()``.


        :param n: the number of ``Hierarchy`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Hierarchy`` elements.The length of the array is less than or equal to the number
            specified.
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.hierarchy.Hierarchy


