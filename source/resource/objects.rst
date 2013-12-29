.. currentmodule:: dlkit.abstract_osid.resource.objects
.. automodule:: dlkit.abstract_osid.resource.objects

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

.. autoattribute:: ResourceNode.parent_bin_nodes

.. autoattribute:: ResourceNode.child_bin_nodes



Resource Node List
------------------

.. autoclass:: ResourceNodeList
   :show-inheritance:

.. autoattribute:: ResourceNodeList.next_resource_node

.. automethod:: ResourceNodeList.get_next_resource_nodes



Resource Relationship
---------------------

.. autoclass:: ResourceRelationship
   :show-inheritance:

.. autoattribute:: ResourceRelationship.source_resource_id

.. autoattribute:: ResourceRelationship.source_resource

.. autoattribute:: ResourceRelationship.destination_resource_id

.. autoattribute:: ResourceRelationship.destination_resource

.. automethod:: ResourceRelationship.get_resource_relationship_record



Resource Relationship Form
--------------------------

.. autoclass:: ResourceRelationshipForm
   :show-inheritance:

.. automethod:: ResourceRelationshipForm.get_resource_relationship_form_record



Resource Relationship List
--------------------------

.. autoclass:: ResourceRelationshipList
   :show-inheritance:

.. autoattribute:: ResourceRelationshipList.next_resource_relationship

.. automethod:: ResourceRelationshipList.get_next_resource_relationships



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



