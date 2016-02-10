
from ..osid import sessions as osid_sessions


class HierarchyTraversalSession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy.


    Each node in the hierarchy is a unique OSID ``Id``. The hierarchy
    may be traversed recursively to establish the tree structure through
    ``get_parents()`` and ``getChildren()``. To relate these ``Ids`` to
    another OSID, ``get_nodes()`` can be used for retrievals that can be
    used for bulk lookups in other OSIDs.




    Any Id available in an associated OSID is known to this hierarchy. A
    lookup up a particular ``Id`` in this hierarchy for the purposes of
    establishing a starting point for traversal or determining
    relationships should use the ``Id`` returned from the corresponding
    OSID object, not an Id that has been stored, to avoid problems with
    ``Id`` translation or aliasing.




    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parents()`` or ``get_children()`` in lieu of a
    ``PermissionDenied`` error that may disrupt the traversal through
    authorized pathways.


    """

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


class HierarchyDesignSession(osid_sessions.OsidSession):
    """This session provides methods to manage a hierarchy.


    Each node is expressed as an OSID ``Id`` that represents an external
    object. The hierarchy only expresses relationships among these Ids.
    However, changing the hierarchy may have implications, such as
    inherited data, in the associated OSID.


    """

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


class HierarchyLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Hierarchy`` objects.


    The ``Hierarchy`` represents a structure of OSID ``Ids``.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition








    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Hierarchies`` objects it can access, without breaking
    execution. However, an assessment may only be useful if all
    ``Hierarchy`` objects referenced by it are available, and a test-
    taking applicationmay sacrifice some interoperability for the sake
    of precision.


    """

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


class HierarchyAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Hierarchies``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Hierarchy,`` a ``HierarchyForm`` is requested using
    ``get_hierarchy_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``HierarchyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``HierarchyForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``HierarchyForm``
    corresponds to an attempted transaction.




    For updates, ``HierarchyForms`` are requested to the ``Hierarchy``
    ``Id`` that is to be updated using ``getHierarchyFormForUpdate()``.
    Similarly, the ``HierarchyForm`` has metadata about the data that
    can be updated and it can perform validation before submitting the
    update. The ``HierarchyForm`` can only be used once for a successful
    update and cannot be reused.




    The delete operations delete ``Hierarchies``.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.


    """

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


