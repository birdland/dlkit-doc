

Objects
=======


Hierarchy
---------

.. py:class:: Hierarchy(abc_hierarchy_objects.Hierarchy, osid_objects.OsidCatalog)
        :noindex:

    .. py:method:: get_hierarchy_record(hierarchy_record_type):
        :noindex:


Hierarchy Form
--------------

.. py:class:: HierarchyForm(abc_hierarchy_objects.HierarchyForm, osid_objects.OsidCatalogForm)
    This is the form for creating and updating ``Hierarchy`` objects.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``HierarchyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_hierarchy_form_record(hierarchy_record_type):
        :noindex:


Hierarchy List
--------------

.. py:class:: HierarchyList(abc_hierarchy_objects.HierarchyList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``HierarchyList`` provides a means for accessing ``Id`` elements
    sequentially either one at a time or many at a time.


    Examples: while (hl.hasNext()) { Hierarchy hierarchy =
    hl.getNextHierarchy(); }




    or
      while (hl.hasNext()) {
           Hierarchy[] hierarchies = hl.getNextHierarchies(hl.available());
      }









    .. py:method:: get_next_hierarchy():
        :noindex:


    .. py:attribute:: next_hierarchy
        :noindex:


    .. py:method:: get_next_hierarchies(n):
        :noindex:


Node
----

.. py:class:: Node(abc_hierarchy_objects.Node, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the hierarchy traversal
    session.





    .. py:method:: get_parents():
        :noindex:


    .. py:attribute:: parents
        :noindex:


    .. py:method:: get_children():
        :noindex:


    .. py:attribute:: children
        :noindex:


Node List
---------

.. py:class:: NodeList(abc_hierarchy_objects.NodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``NodeList`` provides a means for accessing ``Id`` elements sequentially
    either one at a time or many at a time.


    Examples: while (nl.hasNext()) { Node node = nl.getNextNode(); }




    or
      while (nl.hasNext()) {
           Node[] nodes = nl.getNextNodes(nl.available());
      }









    .. py:method:: get_next_node():
        :noindex:


    .. py:attribute:: next_node
        :noindex:


    .. py:method:: get_next_nodes(n):
        :noindex:


