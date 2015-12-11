
from ..osid import objects as osid_objects
from ..osid import sessions as osid_sessions


class Hierarchy(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """A ``Hierarchy`` represents an authenticatable identity.

    Like all OSID objects, a ``Hierarchy`` is identified by its Id and
    any persisted references should use the Id.

    """
    



    def get_hierarchy_record(self, hierarchy_record_type):
        """Gets the hierarchy record corresponding to the given ``Hierarchy`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``hierarchy_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(hierarchy_record_type)`` is ``true`` .

        arg:    hierarchy_record_type (osid.type.Type): the type of the
                record to retrieve
        return: (osid.hierarchy.records.HierarchyRecord) - the hierarchy
                record
        raise:  NullArgument - ``hierarchy_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(hierarchyrecord_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.records.HierarchyRecord


class HierarchyForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Hierarchy`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``HierarchyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    



    def get_hierarchy_form_record(self, hierarchy_record_type):
        """Gets the ``HierarchyFormRecord`` corresponding to the given hierarchy record ``Type``.

        arg:    hierarchy_record_type (osid.type.Type): the hierarchy
                record type
        return: (osid.hierarchy.records.HierarchyFormRecord) - the
                hierarchy form record
        raise:  NullArgument - ``hierarchy_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(hierarchy_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.records.HierarchyFormRecord


class HierarchyList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``HierarchyList`` provides a means for accessing ``Id`` elements sequentially either one at a
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

        return: (osid.hierarchy.Hierarchy) - the next ``Hierarchy`` in
                this list. The ``has_next()`` method should be used to
                test that a next ``Hierarchy`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy

    next_hierarchy = property(fget=get_next_hierarchy)


    def get_next_hierarchies(self, n):
        """Gets the next set of ``Hierarchy`` objects in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Hierarchy`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.hierarchy.Hierarchy) - an array of ``Hierarchy``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Hierarchy


class Node(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the hierarchy traversal
    session.

    """
    



    def get_parents(self):
        """Gets the parents of this node.

        return: (osid.hierarchy.NodeList) - the parents of this node
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.NodeList

    parents = property(fget=get_parents)


    def get_children(self):
        """Gets the children of this node.

        return: (osid.hierarchy.NodeList) - the children of this node
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.NodeList

    children = property(fget=get_children)


class NodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``NodeList`` provides a means for accessing ``Id`` elements sequentially either one at a time
        or many at a time.

    Examples: while (nl.hasNext()) { Node node = nl.getNextNode(); }

    or
      while (nl.hasNext()) {
           Node[] nodes = nl.getNextNodes(nl.available());
      }


    """
    



    def get_next_node(self):
        """Gets the next ``Node`` in this list.

        return: (osid.hierarchy.Node) - the next ``Node`` in this list.
                The ``has_next()`` method should be used to test that a
                next ``Node`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node

    next_node = property(fget=get_next_node)


    def get_next_nodes(self, n):
        """Gets the next set of ``Node`` objects in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        arg:    n (cardinal): the number of ``Node`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.hierarchy.Node) - an array of ``Node``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.hierarchy.Node


