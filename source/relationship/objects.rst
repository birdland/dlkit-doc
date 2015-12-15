

Objects
=======


Relationship
------------

.. py:class:: Relationship(abc_relationship_objects.Relationship, osid_objects.OsidRelationship)
    A ``Relationship`` is an object between two peers.


    The genus type indicates the relationship between the peer and the
    related peer.





    .. py:method:: get_source_id():
        :noindex:


    .. py:attribute:: source_id
        :noindex:


    .. py:method:: get_destination_id():
        :noindex:


    .. py:attribute:: destination_id
        :noindex:


    .. py:method:: get_relationship_record(relationship_record_type):
        :noindex:


Relationship Form
-----------------

.. py:class:: RelationshipForm(abc_relationship_objects.RelationshipForm, osid_objects.OsidRelationshipForm)
    This is the form for creating and updating ``Relationships``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RelationshipAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_relationship_form_record(relationship_record_type):
        :noindex:


Relationship List
-----------------

.. py:class:: RelationshipList(abc_relationship_objects.RelationshipList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``Relationship`` provides a means for accessing ``Relationship``
        elements
    sequentially either one at a time or many at a time.


    Examples: while (rl.hasNext()) { Relationship relationship =
    rl.getNextRelationship(); }




    or
      while (rl.hasNext()) {
           Relationship[] relationships = rl.getNextRelationships(rl.available());
      }









    .. py:method:: get_next_relationship():
        :noindex:


    .. py:attribute:: next_relationship
        :noindex:


    .. py:method:: get_next_relationships(n):
        :noindex:


Family
------

.. py:class:: Family(abc_relationship_objects.Family, osid_objects.OsidCatalog)
        :noindex:

    .. py:method:: get_family_record(family_record_type):
        :noindex:


Family Form
-----------

.. py:class:: FamilyForm(abc_relationship_objects.FamilyForm, osid_objects.OsidCatalogForm)
    This is the form for creating and updating ``Family`` objects.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``FamilyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_family_form_record(family_record_type):
        :noindex:


Family List
-----------

.. py:class:: FamilyList(abc_relationship_objects.FamilyList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``FamilyList`` provides a means for accessing ``Family`` elements
    sequentially either one at a time or many at a time.


    Examples: while (fl.hasNext()) { Family family = fl.getNextFamily();
    }




    or
      while (fl.hasNext()) {
           Family[] families = fl.getNextFamilies(fl.available());
      }









    .. py:method:: get_next_family():
        :noindex:


    .. py:attribute:: next_family
        :noindex:


    .. py:method:: get_next_families(n):
        :noindex:


Family Node
-----------

.. py:class:: FamilyNode(abc_relationship_objects.FamilyNode, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``FamilyHierarchySession``.





    .. py:method:: get_family():
        :noindex:


    .. py:attribute:: family
        :noindex:


    .. py:method:: get_parent_family_nodes():
        :noindex:


    .. py:attribute:: parent_family_nodes
        :noindex:


    .. py:method:: get_child_family_nodes():
        :noindex:


    .. py:attribute:: child_family_nodes
        :noindex:


Family Node List
----------------

.. py:class:: FamilyNodeList(abc_relationship_objects.FamilyNodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``FamilyNodeList`` provides a means for accessing ``FamilyNode``
        elements
    sequentially either one at a time or many at a time.


    Examples: while (fnl.hasNext()) { FamilyNode node =
    fnl.getNextFamilyNode(); }




    or
      while (fnl.hasNext()) {
           FamilyNode[] nodes = fnl.getNextFamilyNodes(fnl.available());
      }









    .. py:method:: get_next_family_node():
        :noindex:


    .. py:attribute:: next_family_node
        :noindex:


    .. py:method:: get_next_family_nodes(n):
        :noindex:


