
.. currentmodule:: dlkit.hierarchy.objects
.. automodule:: dlkit.hierarchy.objects

Objects
=======


Hierarchy
---------

.. py:class:: Hierarchy(abc_hierarchy_objects.Hierarchy, osid_objects.OsidCatalog)
        :noindex:

   .. automethod:: Hierarchy.get_hierarchy_record

Hierarchy Form
--------------

.. autoclass:: HierarchyForm
   :show-inheritance:

   .. automethod:: HierarchyForm.get_hierarchy_form_record

Hierarchy List
--------------

.. autoclass:: HierarchyList
   :show-inheritance:

   .. autoattribute:: HierarchyList.next_hierarchy

   .. automethod:: HierarchyList.get_next_hierarchies

Node
----

.. autoclass:: Node
   :show-inheritance:

   .. autoattribute:: Node.parents

   .. autoattribute:: Node.children

Node List
---------

.. autoclass:: NodeList
   :show-inheritance:

   .. autoattribute:: NodeList.next_node

   .. automethod:: NodeList.get_next_nodes

