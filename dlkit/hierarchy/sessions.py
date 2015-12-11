
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

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    hierarchy_id = property(fget=get_hierarchy_id)


    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_roots(self):
        """Gets the root nodes of this hierarchy.

        return: (osid.id.IdList) - the root nodes
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList

    roots = property(fget=get_roots)


    def has_parents(self, id_):
        """Tests if this ``Id`` contains any parents.

        arg:    id (osid.id.Id): the ``Id`` to query
        return: (boolean) - ``true`` if this ``Id`` contains parents,
                ``false`` otherwise
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def is_parent(self, id_, parent_id):
        """Tests if an ``Id`` is a direct parent of another.

        arg:    id (osid.id.Id): the ``Id`` to query
        arg:    parent_id (osid.id.Id): the ``Id`` of a parent
        return: (boolean) - ``true`` if this ``parent_id`` is a parent
                of ``id,``  ``false`` otherwise
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` or ``parent_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``parent_id`` not found return
        ``false``.

        """
        return # boolean


    def get_parents(self, id_):
        """Gets the parents of the given ``id``.

        arg:    id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the parents of the ``id``
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList


    def is_ancestor(self, id_, ancestor_id):
        """Tests if an ``Id`` is an ancestor of another.

        arg:    id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_id (osid.id.Id): the ``Id`` of an ancestor
        return: (boolean) - ``true`` if this ``ancestor_id`` is a parent
                of ``id,``  ``false`` otherwise
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` or ``ancestor_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``ancestor_id`` not found return
        ``false``.

        """
        return # boolean


    def has_children(self, id_):
        """Tests if this ``Id`` has any children.

        arg:    id (osid.id.Id): the ``Id`` to query
        return: (boolean) - ``true`` if this ``Id`` has children,
                ``false`` otherwise
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def is_child(self, id_, child_id):
        """Tests if a node is a direct child of another.

        arg:    id (osid.id.Id): the ``Id`` to query
        arg:    child_id (osid.id.Id): the ``Id`` of a child
        return: (boolean) - ``true`` if this ``child_id`` is a child of
                the ``Id,``  ``false`` otherwise
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If ``child_id`` not found return
        ``false``.

        """
        return # boolean


    def get_children(self, id_):
        """Gets the children of the given ``Id``.

        arg:    id (osid.id.Id): the ``Id`` to query
        return: (osid.id.IdList) - the children of the ``id``
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.IdList


    def is_descendant(self, id_, descendant_id):
        """Tests if a node is a descendant of another.

        arg:    id (osid.id.Id): the ``Id`` to query
        arg:    descendant_id (osid.id.Id): the ``Id`` of a descendant
        return: (boolean) - ``true`` if this ``descendant_id`` is a
                child of the ``Id,``  ``false`` otherwise
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` or ``descendant`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*
        *implementation notes*: If not found return ``false``.

        """
        return # boolean


    def get_nodes(self, id_, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given ``Id``.

        arg:    id (osid.id.Id): the ``Id`` to query
        arg:    ancestor_levels (cardinal): the maximum number of
                ancestor levels to include. A value of 0 returns no
                parents in the node.
        arg:    descendant_levels (cardinal): the maximum number of
                descendant levels to include. A value of 0 returns no
                children in the node.
        arg:    include_siblings (boolean): ``true`` to include the
                siblings of the given node, ``false`` to omit the
                siblings
        return: (osid.hierarchy.Node) - a node
        raise:  NotFound - ``id`` is not found
        raise:  NullArgument - ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        return: (osid.id.Id) - the hierarchy ``Id`` associated with this
                session
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    hierarchy_id = property(fget=get_hierarchy_id)


    def get_hierarchy(self):
        """Gets the hierarchy associated with this session.

        return: (osid.hierarchy.Hierarchy) - the hierarchy associated
                with this session
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        return: (boolean) - ``false`` if changing this hierarchy is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def add_root(self, id_):
        """Adds a root node.

        arg:    id (osid.id.Id): the ``Id`` of the node
        raise:  AlreadyExists - ``id`` is already in hierarchy
        raise:  NotFound - ``id`` not found
        raise:  NullArgument - ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def add_child(self, id_, child_id):
        """Adds a child to a ``Id``.

        arg:    id (osid.id.Id): the ``Id`` of the node
        arg:    child_id (osid.id.Id): the ``Id`` of the new child
        raise:  AlreadyExists - ``child_id`` is already a child of
                ``id``
        raise:  NotFound - ``id`` or ``child_id`` not found
        raise:  NullArgument - ``id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def remove_root(self, id_):
        """Removes a root node.

        arg:    id (osid.id.Id): the ``Id`` of the node
        raise:  NotFound - ``id`` was not found or not in hierarchy
        raise:  NullArgument - ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def remove_child(self, id_, child_id):
        """Removes a childfrom an ``Id``.

        arg:    id (osid.id.Id): the ``Id`` of the node
        arg:    child_id (osid.id.Id): the ``Id`` of the child to remove
        raise:  NotFound - ``id`` or ``child_id`` was not found or
                ``child_id`` is not a child of ``id``
        raise:  NullArgument - ``id`` or ``child_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def remove_children(self, id_):
        """Removes all childrenfrom an ``Id``.

        arg:    id (osid.id.Id): the ``Id`` of the node
        raise:  NotFound - an node identified by the given ``Id`` was
                not found
        raise:  NullArgument - ``id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        return: (boolean) - ``false`` if lookup methods are not
                authorized, ``true`` otherwise
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

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy`` to retrieve
        return: (osid.hierarchy.Hierarchy) - the returned ``Hierarchy``
        raise:  NotFound - no ``Hierarchy`` found with the given ``Id``
        raise:  NullArgument - ``hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        arg:    hierarchy_ids (osid.id.IdList): the list of ``Ids`` to
                retrieve
        return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        raise:  NotFound - an ``Id was`` not found
        raise:  NullArgument - ``hierarchy_ids`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        arg:    hierarchy_genus_type (osid.type.Type): a hierarchy genus
                type
        return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        raise:  NullArgument - ``hierarchy_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        arg:    hierarchy_genus_type (osid.type.Type): a hierarchy genus
                type
        return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        raise:  NullArgument - ``hierarchy_genus_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        arg:    hierarchy_record_type (osid.type.Type): a hierarchy
                record type
        return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        raise:  NullArgument - ``hierarchy_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        arg:    resource_id (osid.id.Id): a resource ``Id``
        return: (osid.hierarchy.HierarchyList) - the returned
                ``Hierarchy`` list
        raise:  NullArgument - ``resource_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.HierarchyList


    def get_hierarchies(self):
        """Gets all hierarchies.

        In plenary mode, the returned list contains all known
        hierarchies or an error results. Otherwise, the returned list
        may contain only those hierarchies that are accessible through
        this session.

        return: (osid.hierarchy.HierarchyList) - a list of
                ``Hierarchies``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        return: (boolean) - ``false`` if ``Hierarchy`` creation is not
                authorized, ``true`` otherwise
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

        arg:    hierarchy_record_types (osid.type.Type[]): array of
                hierarchy record types
        return: (boolean) - ``true`` if ``Hierarchy`` creation using the
                specified ``Types`` is supported, ``false`` otherwise
        raise:  NullArgument - ``hierarchy_record_types`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_hierarchy_form_for_create(self, hierarchy_record_types):
        """Gets the hierarchy form for creating new hierarchies.

        A new form should be requested for each create transaction. This
        method is used for creating new hierarchies, where only the
        ``Hierarchy`` ``Type`` is known.

        arg:    hierarchy_record_types (osid.type.Type[]): array of
                hierarchy record types
        return: (osid.hierarchy.HierarchyForm) - the hierarchy form
        raise:  NullArgument - ``hierarchy_record_types`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - unable to get form for requested record
                types
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.HierarchyForm


    def create_hierarchy(self, hierarchy_form):
        """Creates a new ``Hierarchy``.

        arg:    hierarchy_form (osid.hierarchy.HierarchyForm): the form
                for this ``Hierarchy``
        return: (osid.hierarchy.Hierarchy) - the new ``Hierarchy``
        raise:  IllegalState - ``hierarchy_form`` already used in a
                create transaction
        raise:  InvalidArgument - one or more of the form elements is
                invalid
        raise:  NullArgument - ``hierarchy_form`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``hierarchy_form`` did not originate from
                ``get_hierarchy_form_for_create()``
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

        return: (boolean) - ``false`` if ``Hierarchy`` modification is
                not authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_hierarchy_form_for_update(self, hierarchy_id):
        """Gets the hierarchy form for updating an existing hierarchy.

        A new hierarchy form should be requested for each update
        transaction.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy``
        return: (osid.hierarchy.HierarchyForm) - the hierarchy form
        raise:  NotFound - ``hierarchy_id`` is not found
        raise:  NullArgument - ``hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.HierarchyForm


    def update_hierarchy(self, hierarchy_form):
        """Updates an existing hierarchy.

        arg:    hierarchy_form (osid.hierarchy.HierarchyForm): the form
                containing the elements to be updated
        raise:  IllegalState - ``hierarchy_form`` already used in an
                update transaction
        raise:  InvalidArgument - the form contains an invalid value
        raise:  NullArgument - ``hierarchy_id`` or ``hierarchy_form`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        raise:  Unsupported - ``hierarchy_form`` did not originate from
                ``get_hierarchy_form_for_update()``
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

        return: (boolean) - ``false`` if ``Hierarchy`` deletion is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def delete_hierarchy(self, hierarchy_id):
        """Deletes a ``Hierarchy``.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of the
                ``Hierarchy`` to remove
        raise:  NotFound - ``hierarchy_id`` not found
        raise:  NullArgument - ``hierarchy_id`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
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

        return: (boolean) - ``false`` if ``Hierarchy`` aliasing is not
                authorized, ``true`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def alias_hierarchy(self, hierarchy_id, alias_id):
        """Adds an ``Id`` to a ``Hierarchy`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Hierarchy`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another vault it is
        reassigned to the given vault ``Id``.

        arg:    hierarchy_id (osid.id.Id): the ``Id`` of an
                ``Hierarchy``
        arg:    alias_id (osid.id.Id): the alias ``Id``
        raise:  AlreadyExists - ``alias_id`` is already assigned
        raise:  NotFound - ``hierarchy_id`` not found
        raise:  NullArgument - ``hierarchy_id`` or ``alias_id`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  PermissionDenied - authorization failure
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


