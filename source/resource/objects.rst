

Objects
=======


Resource
--------

.. py:class:: Resource(abc_resource_objects.Resource, osid_objects.OsidObject)
    A ``Resource`` represents an arbitrary entity.


    Resources are used to define an object to accompany an OSID ``Id``
    used in other OSIDs. A resource may be used to represent a meeting
    room in the Scheduling OSID, or a student in the Course OSID.




    A ``Resource`` may also represent a group or organization. A
    provider may present such a group in an opaque manner through a
    single resource definition, or the provider may expose the resource
    collection for examination or manipulation. If such a resource
    collection is visible, ``is_group()`` is ``true`` and can be used in
    one of the group sessions available in this OSID.





    .. py:method:: is_group():
        :noindex:


    .. py:method:: is_demographic():
        :noindex:


    .. py:method:: has_avatar():
        :noindex:


    .. py:method:: get_avatar_id():
        :noindex:


    .. py:attribute:: avatar_id
        :noindex:


    .. py:method:: get_avatar():
        :noindex:


    .. py:attribute:: avatar
        :noindex:


    .. py:method:: get_resource_record(resource_record_type):
        :noindex:


Resource Form
-------------

.. py:class:: ResourceForm(abc_resource_objects.ResourceForm, osid_objects.OsidObjectForm)
    This is the form for creating and updating ``Resources``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ResourceAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.




    Resources can be designated as a group. The group metadata indicates
    if it is possible to convert a resource to a group and vice-versa.





    .. py:method:: get_group_metadata():
        :noindex:


    .. py:attribute:: group_metadata
        :noindex:


    .. py:method:: set_group(group):
        :noindex:


    .. py:method:: clear_group():
        :noindex:


    .. py:attribute:: group
        :noindex:


    .. py:method:: get_avatar_metadata():
        :noindex:


    .. py:attribute:: avatar_metadata
        :noindex:


    .. py:method:: set_avatar(asset_id):
        :noindex:


    .. py:method:: clear_avatar():
        :noindex:


    .. py:attribute:: avatar
        :noindex:


    .. py:method:: get_resource_form_record(resource_record_type):
        :noindex:


Resource List
-------------

.. py:class:: ResourceList(abc_resource_objects.ResourceList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ResourceList`` provides a means for accessing ``Resource`` elements
    sequentially either one at a time or many at a time.


    Examples: while (rl.hasNext()) { Resource resource =
    rl.getNextResource(); }




    or
      while (rl.hasNext()) {
           Resource[] resources = rl.getNextResources(rl.available());
      }









    .. py:method:: get_next_resource():
        :noindex:


    .. py:attribute:: next_resource
        :noindex:


    .. py:method:: get_next_resources(n):
        :noindex:


Resource Node
-------------

.. py:class:: ResourceNode(abc_resource_objects.ResourceNode, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BinHierarchySession``.





    .. py:method:: get_resource():
        :noindex:


    .. py:attribute:: resource
        :noindex:


    .. py:method:: get_parent_resource_nodes():
        :noindex:


    .. py:attribute:: parent_resource_nodes
        :noindex:


    .. py:method:: get_child_resource_nodes():
        :noindex:


    .. py:attribute:: child_resource_nodes
        :noindex:


Resource Node List
------------------

.. py:class:: ResourceNodeList(abc_resource_objects.ResourceNodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``ResourceNodeList`` provides a means for accessing ``ResourceNode``
    elements sequentially either one at a time or many at a time.


    Examples: while (rnl.hasNext()) { ResourceNode node =
    rnl.getNextResourceNode(); }




    or
      while rnl.hasNext()) {
           ResourceNode[] nodes = rnl.getNextResourceNodes(rnl.available());
      }









    .. py:method:: get_next_resource_node():
        :noindex:


    .. py:attribute:: next_resource_node
        :noindex:


    .. py:method:: get_next_resource_nodes(n):
        :noindex:


Bin
---

.. py:class:: Bin(abc_resource_objects.Bin, osid_objects.OsidCatalog)
        :noindex:

    .. py:method:: get_bin_record(bin_record_type):
        :noindex:


Bin Form
--------

.. py:class:: BinForm(abc_resource_objects.BinForm, osid_objects.OsidCatalogForm)
    This is the form for creating and updating bins.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the ``BinAdminSession``.
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.





    .. py:method:: get_bin_form_record(bin_record_type):
        :noindex:


Bin List
--------

.. py:class:: BinList(abc_resource_objects.BinList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``BinList`` provides a means for accessing ``Bin`` elements sequentially
    either one at a time or many at a time.


    Examples: while (bl.hasNext()) { Bin bin = bl.getNextBin(); }




    or
      while (bl.hasNext()) {
           Bin[] bins = bl.getNextBins(bl.available());
      }









    .. py:method:: get_next_bin():
        :noindex:


    .. py:attribute:: next_bin
        :noindex:


    .. py:method:: get_next_bins(n):
        :noindex:


Bin Node
--------

.. py:class:: BinNode(abc_resource_objects.BinNode, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BinHierarchySession``.





    .. py:method:: get_bin():
        :noindex:


    .. py:attribute:: bin
        :noindex:


    .. py:method:: get_parent_bin_nodes():
        :noindex:


    .. py:attribute:: parent_bin_nodes
        :noindex:


    .. py:method:: get_child_bin_nodes():
        :noindex:


    .. py:attribute:: child_bin_nodes
        :noindex:


Bin Node List
-------------

.. py:class:: BinNodeList(abc_resource_objects.BinNodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``BinNodeList`` provides a means for accessing ``BinNode`` elements
    sequentially either one at a time or many at a time.


    Examples: while (bnl.hasNext()) { BinNode node =
    bnl.getNextBinNode(); }




    or
      while (bnl.hasNext()) {
           BinNode[] nodes = bnl.getNextBinNodes(bnl.available());
      }









    .. py:method:: get_next_bin_node():
        :noindex:


    .. py:attribute:: next_bin_node
        :noindex:


    .. py:method:: get_next_bin_nodes(n):
        :noindex:


