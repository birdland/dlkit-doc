
.. currentmodule:: dlkit.resource.objects
.. automodule:: dlkit.resource.objects

Objects
=======


Resource
--------

.. autoclass:: Resource
   :show-inheritance:

   .. automethod:: Resource.is_group

   .. automethod:: Resource.is_demographic

   .. automethod:: Resource.has_avatar

   .. autoattribute:: Resource.avatar_id

   .. autoattribute:: Resource.avatar

   .. automethod:: Resource.get_resource_record

Resource Form
-------------

.. autoclass:: ResourceForm
   :show-inheritance:

   .. autoattribute:: ResourceForm.group_metadata

   .. autoattribute:: ResourceForm.group

   .. autoattribute:: ResourceForm.avatar_metadata

   .. autoattribute:: ResourceForm.avatar

   .. automethod:: ResourceForm.get_resource_form_record

Resource List
-------------

.. autoclass:: ResourceList
   :show-inheritance:

   .. autoattribute:: ResourceList.next_resource

   .. automethod:: ResourceList.get_next_resources

Resource Node
-------------

.. autoclass:: ResourceNode
   :show-inheritance:

   .. autoattribute:: ResourceNode.resource

   .. autoattribute:: ResourceNode.parent_resource_nodes

   .. autoattribute:: ResourceNode.child_resource_nodes

Resource Node List
------------------

.. autoclass:: ResourceNodeList
   :show-inheritance:

   .. autoattribute:: ResourceNodeList.next_resource_node

   .. automethod:: ResourceNodeList.get_next_resource_nodes

Bin
---

.. py:class:: Bin(abc_resource_objects.Bin, osid_objects.OsidCatalog)
        :noindex:

   .. automethod:: Bin.get_bin_record

Bin Form
--------

.. autoclass:: BinForm
   :show-inheritance:

   .. automethod:: BinForm.get_bin_form_record

Bin List
--------

.. autoclass:: BinList
   :show-inheritance:

   .. autoattribute:: BinList.next_bin

   .. automethod:: BinList.get_next_bins

Bin Node
--------

.. autoclass:: BinNode
   :show-inheritance:

   .. autoattribute:: BinNode.bin

   .. autoattribute:: BinNode.parent_bin_nodes

   .. autoattribute:: BinNode.child_bin_nodes

Bin Node List
-------------

.. autoclass:: BinNodeList
   :show-inheritance:

   .. autoattribute:: BinNodeList.next_bin_node

   .. automethod:: BinNodeList.get_next_bin_nodes

