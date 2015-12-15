

Sessions
========


Hierarchy Traversal Session
---------------------------

.. py:class:: HierarchyTraversalSession(abc_hierarchy_sessions.HierarchyTraversalSession, osid_sessions.OsidSession)
    This session defines methods for traversing a hierarchy.


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





    .. py:method:: get_hierarchy_id():
        :noindex:


    .. py:attribute:: hierarchy_id
        :noindex:


    .. py:method:: get_hierarchy():
        :noindex:


    .. py:attribute:: hierarchy
        :noindex:


    .. py:method:: can_access_hierarchy():
        :noindex:


    .. py:method:: get_roots():
        :noindex:


    .. py:attribute:: roots
        :noindex:


    .. py:method:: has_parents(id_):
        :noindex:


    .. py:method:: is_parent(id_, parent_id):
        :noindex:


    .. py:method:: get_parents(id_):
        :noindex:


    .. py:method:: is_ancestor(id_, ancestor_id):
        :noindex:


    .. py:method:: has_children(id_):
        :noindex:


    .. py:method:: is_child(id_, child_id):
        :noindex:


    .. py:method:: get_children(id_):
        :noindex:


    .. py:method:: is_descendant(id_, descendant_id):
        :noindex:


    .. py:method:: get_nodes(id_, ancestor_levels=10, descendant_levels=10, include_siblings=False):
        :noindex:


Hierarchy Design Session
------------------------

.. py:class:: HierarchyDesignSession(abc_hierarchy_sessions.HierarchyDesignSession, osid_sessions.OsidSession)
    This session provides methods to manage a hierarchy.


    Each node is expressed as an OSID ``Id`` that represents an external
    object. The hierarchy only expresses relationships among these Ids.
    However, changing the hierarchy may have implications, such as
    inherited data, in the associated OSID.





    .. py:method:: get_hierarchy_id():
        :noindex:


    .. py:attribute:: hierarchy_id
        :noindex:


    .. py:method:: get_hierarchy():
        :noindex:


    .. py:attribute:: hierarchy
        :noindex:


    .. py:method:: can_modify_hierarchy():
        :noindex:


    .. py:method:: add_root(id_):
        :noindex:


    .. py:method:: add_child(id_, child_id):
        :noindex:


    .. py:method:: remove_root(id_):
        :noindex:


    .. py:method:: remove_child(id_, child_id):
        :noindex:


    .. py:method:: remove_children(id_):
        :noindex:


Hierarchy Lookup Session
------------------------

.. py:class:: HierarchyLookupSession(abc_hierarchy_sessions.HierarchyLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Hierarchy`` objects.


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





    .. py:method:: can_lookup_hierarchies():
        :noindex:


    .. py:method:: use_comparative_hierarchy_view():
        :noindex:


    .. py:method:: use_plenary_hierarchy_view():
        :noindex:


    .. py:method:: get_hierarchy(hierarchy_id):
        :noindex:


    .. py:method:: get_hierarchies_by_ids(hierarchy_ids):
        :noindex:


    .. py:method:: get_hierarchies_by_genus_type(hierarchy_genus_type):
        :noindex:


    .. py:method:: get_hierarchies_by_parent_genus_type(hierarchy_genus_type):
        :noindex:


    .. py:method:: get_hierarchies_by_record_type(hierarchy_record_type):
        :noindex:


    .. py:method:: get_hierarchies_by_provider(resource_id):
        :noindex:


    .. py:method:: get_hierarchies():
        :noindex:


    .. py:attribute:: hierarchies
        :noindex:


Hierarchy Admin Session
-----------------------

.. py:class:: HierarchyAdminSession(abc_hierarchy_sessions.HierarchyAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Hierarchies``.


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





    .. py:method:: can_create_hierarchies():
        :noindex:


    .. py:method:: can_create_hierarchy_with_record_types(hierarchy_record_types):
        :noindex:


    .. py:method:: get_hierarchy_form_for_create(hierarchy_record_types):
        :noindex:


    .. py:method:: create_hierarchy(hierarchy_form):
        :noindex:


    .. py:method:: can_update_hierarchies():
        :noindex:


    .. py:method:: get_hierarchy_form_for_update(hierarchy_id):
        :noindex:


    .. py:method:: update_hierarchy(hierarchy_form):
        :noindex:


    .. py:method:: can_delete_hierarchies():
        :noindex:


    .. py:method:: delete_hierarchy(hierarchy_id):
        :noindex:


    .. py:method:: can_manage_hierarchy_aliases():
        :noindex:


    .. py:method:: alias_hierarchy(hierarchy_id, alias_id):
        :noindex:


