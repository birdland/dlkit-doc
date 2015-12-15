

Sessions
========


Relationship Lookup Session
---------------------------

.. py:class:: RelationshipLookupSession(abc_relationship_sessions.RelationshipLookupSession, osid_sessions.OsidSession)
    This session defines methods for retrieving relationships.


    A ``Relationship`` is mapped to two OSID ``Ids``.




    This lookup session defines several views:




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition
      * federated family view: includes relationships in families which
        are children of this family in the family hierarchy
      * isolated family view: restricts lookups to this family only
      * effective relationship view: Relationship methods return only
        relationships currently in effect.
      * any effective relationship view: Relationship methods return
        both effective and ineffective relationships.








    Relationships may have an additional records indicated by their
    respective record types. The record may not be accessed through a
    cast of the ``Relationship``.





    .. py:method:: get_family_id():
        :noindex:


    .. py:attribute:: family_id
        :noindex:


    .. py:method:: get_family():
        :noindex:


    .. py:attribute:: family
        :noindex:


    .. py:method:: can_lookup_relationships():
        :noindex:


    .. py:method:: use_comparative_relationship_view():
        :noindex:


    .. py:method:: use_plenary_relationship_view():
        :noindex:


    .. py:method:: use_federated_family_view():
        :noindex:


    .. py:method:: use_isolated_family_view():
        :noindex:


    .. py:method:: use_effective_relationship_view():
        :noindex:


    .. py:method:: use_any_effective_relationship_view():
        :noindex:


    .. py:method:: get_relationship(relationship_id):
        :noindex:


    .. py:method:: get_relationships_by_ids(relationship_ids):
        :noindex:


    .. py:method:: get_relationships_by_genus_type(relationship_genus_type):
        :noindex:


    .. py:method:: get_relationships_by_parent_genus_type(relationship_genus_type):
        :noindex:


    .. py:method:: get_relationships_by_record_type(relationship_record_type):
        :noindex:


    .. py:method:: get_relationships_on_date(from_, to):
        :noindex:


    .. py:method:: get_relationships_for_source(source_id):
        :noindex:


    .. py:method:: get_relationships_for_source_on_date(source_id, from_, to):
        :noindex:


    .. py:method:: get_relationships_by_genus_type_for_source(source_id, relationship_genus_type):
        :noindex:


    .. py:method:: get_relationships_by_genus_type_for_source_on_date(source_id, relationship_genus_type, from_, to):
        :noindex:


    .. py:method:: get_relationships_for_destination(destination_id):
        :noindex:


    .. py:method:: get_relationships_for_destination_on_date(destination_id, from_, to):
        :noindex:


    .. py:method:: get_relationships_by_genus_type_for_destination(destination_id, relationship_genus_type):
        :noindex:


    .. py:method:: get_relationships_by_genus_type_for_destination_on_date(destination_id, relationship_genus_type, from_, to):
        :noindex:


    .. py:method:: get_relationships_for_peers(source_id, destination_id):
        :noindex:


    .. py:method:: get_relationships_for_peers_on_date(source_id, destination_id, from_, to):
        :noindex:


    .. py:method:: get_relationships_by_genus_type_for_peers(source_id, destination_id, relationship_genus_type):
        :noindex:


    .. py:method:: get_relationships_by_genus_type_for_peers_on_date(source_id, destination_id, relationship_genus_type, from_, to):
        :noindex:


    .. py:method:: get_relationships():
        :noindex:


    .. py:attribute:: relationships
        :noindex:


Relationship Query Session
--------------------------

.. py:class:: RelationshipQuerySession(abc_relationship_sessions.RelationshipQuerySession, osid_sessions.OsidSession)
    This session provides methods for searching among ``Relationship`` objects.


    The search query is constructed using the ``Relationship``.




    Relationships may have a query record indicated by their respective
    record types. The query record is accessed via the
    ``RelationshipQuery``.





    .. py:method:: get_family_id():
        :noindex:


    .. py:attribute:: family_id
        :noindex:


    .. py:method:: get_family():
        :noindex:


    .. py:attribute:: family
        :noindex:


    .. py:method:: use_federated_family_view():
        :noindex:


    .. py:method:: use_isolated_family_view():
        :noindex:


    .. py:method:: can_search_relationships():
        :noindex:


    .. py:method:: get_relationship_query():
        :noindex:


    .. py:attribute:: relationship_query
        :noindex:


    .. py:method:: get_relationships_by_query(relationship_query):
        :noindex:


Relationship Admin Session
--------------------------

.. py:class:: RelationshipAdminSession(abc_relationship_sessions.RelationshipAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Relationships``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Relationship,`` a ``RelationshipForm`` is requested using
    ``get_relationship_form_for_create()`` specifying the desired peers
    and record ``Types`` or none if no record ``Types`` are needed. The
    returned ``RelationshipForm`` will indicate that it is to be used
    with a create operation and can be used to examine metdata or
    validate data prior to creation. Once the ``RelationshipForm`` is
    submiited to a create operation, it cannot be reused with another
    create operation unless the first operation was unsuccessful. Each
    ``RelationshipForm`` corresponds to an attempted transaction.




    For updates, ``RelationshipForms`` are requested to the
    ``Relationship``  ``Id`` that is to be updated using
    ``getRelationshipFormForUpdate()``. Similarly, the
    ``RelationshipForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``RelationshipForm`` can only be used once for a successful update
    and cannot be reused.




    The delete operations delete ``Relationships``. To unmap a
    ``Relationship`` from the current ``Family,`` the
    ``RelationshipFamilyAssignmentSession`` should be used. These delete
    operations attempt to remove the ``Relationship`` itself thus
    removing it from all known ``Family`` catalogs.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: get_family_id():
        :noindex:


    .. py:attribute:: family_id
        :noindex:


    .. py:method:: get_family():
        :noindex:


    .. py:attribute:: family
        :noindex:


    .. py:method:: can_create_relationships():
        :noindex:


    .. py:method:: can_create_relationship_with_record_types(relationship_record_types):
        :noindex:


    .. py:method:: get_relationship_form_for_create(source_id, destination_id, relationship_record_types):
        :noindex:


    .. py:method:: create_relationship(relationship_form):
        :noindex:


    .. py:method:: can_update_relationships():
        :noindex:


    .. py:method:: get_relationship_form_for_update(relationship_id):
        :noindex:


    .. py:method:: update_relationship(relationship_form):
        :noindex:


    .. py:method:: can_delete_relationships():
        :noindex:


    .. py:method:: delete_relationship(relationship_id):
        :noindex:


    .. py:method:: can_manage_relationship_aliases():
        :noindex:


    .. py:method:: alias_relationship(relationship_id, alias_id):
        :noindex:


Family Lookup Session
---------------------

.. py:class:: FamilyLookupSession(abc_relationship_sessions.FamilyLookupSession, osid_sessions.OsidSession)
    This session provides methods for retrieving ``Family`` objects.


    The ``Family`` represents a collection of relationships.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition








    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Families`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Families``
    referenced by it are available, and a test-taking applicationmay
    sacrifice some interoperability for the sake of precision.





    .. py:method:: can_lookup_families():
        :noindex:


    .. py:method:: use_comparative_family_view():
        :noindex:


    .. py:method:: use_plenary_family_view():
        :noindex:


    .. py:method:: get_family(family_id):
        :noindex:


    .. py:method:: get_families_by_ids(family_ids):
        :noindex:


    .. py:method:: get_families_by_genus_type(family_genus_type):
        :noindex:


    .. py:method:: get_families_by_parent_genus_type(family_genus_type):
        :noindex:


    .. py:method:: get_families_by_record_type(family_record_type):
        :noindex:


    .. py:method:: get_families_by_provider(resource_id):
        :noindex:


    .. py:method:: get_families():
        :noindex:


    .. py:attribute:: families
        :noindex:


Family Admin Session
--------------------

.. py:class:: FamilyAdminSession(abc_relationship_sessions.FamilyAdminSession, osid_sessions.OsidSession)
    This session creates, updates, and deletes ``Families``.


    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.




    Create and update operations differ in their usage. To create a
    ``Family,`` a ``FamilyForm`` is requested using
    ``get_family_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``FamilyForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``FamilyForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``FamilyForm``
    corresponds to an attempted transaction.




    For updates, ``FamilyForms`` are requested to the ``Family``  ``Id``
    that is to be updated using ``getFamilyFormForUpdate()``. Similarly,
    the ``FamilyForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``FamilyForm`` can only be used once for a successful update and
    cannot be reused.




    The delete operations delete ``Families``.




    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.





    .. py:method:: can_create_families():
        :noindex:


    .. py:method:: can_create_family_with_record_types(family_record_types):
        :noindex:


    .. py:method:: get_family_form_for_create(family_record_types):
        :noindex:


    .. py:method:: create_family(family_form):
        :noindex:


    .. py:method:: can_update_families():
        :noindex:


    .. py:method:: get_family_form_for_update(family_id):
        :noindex:


    .. py:method:: update_family(family_form):
        :noindex:


    .. py:method:: can_delete_families():
        :noindex:


    .. py:method:: delete_family(family_id):
        :noindex:


    .. py:method:: can_manage_family_aliases():
        :noindex:


    .. py:method:: alias_family(family_id, alias_id):
        :noindex:


Family Hierarchy Session
------------------------

.. py:class:: FamilyHierarchySession(abc_relationship_sessions.FamilyHierarchySession, osid_sessions.OsidSession)
    This session defines methods for traversing a hierarchy of ``Family`` objects.


    Each node in the hierarchy is a unique ``Family``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_families()`` and ``getChildFamilies()``. To relate
    these ``Ids`` to another OSID, ``get_family_nodes()`` can be used
    for retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Family`` available in the Relationship OSID is known to this
    hierarchy but does not appear in the hierarchy traversal until added
    as a root node or a child of another node.




    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_families()`` or ``get_child_families()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.




    This session defines views that offer differing behaviors when
    retrieving multiple objects.




      * comparative view: family elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition





    .. py:method:: get_family_hierarchy_id():
        :noindex:


    .. py:attribute:: family_hierarchy_id
        :noindex:


    .. py:method:: get_family_hierarchy():
        :noindex:


    .. py:attribute:: family_hierarchy
        :noindex:


    .. py:method:: can_access_family_hierarchy():
        :noindex:


    .. py:method:: use_comparative_family_view():
        :noindex:


    .. py:method:: use_plenary_family_view():
        :noindex:


    .. py:method:: get_root_family_ids():
        :noindex:


    .. py:attribute:: root_family_ids
        :noindex:


    .. py:method:: get_root_families():
        :noindex:


    .. py:attribute:: root_families
        :noindex:


    .. py:method:: has_parent_families(family_id):
        :noindex:


    .. py:method:: is_parent_of_family(id_, family_id):
        :noindex:


    .. py:method:: get_parent_family_ids(family_id):
        :noindex:


    .. py:method:: get_parent_families(family_id):
        :noindex:


    .. py:method:: is_ancestor_of_family(id_, family_id):
        :noindex:


    .. py:method:: has_child_families(family_id):
        :noindex:


    .. py:method:: is_child_of_family(id_, family_id):
        :noindex:


    .. py:method:: get_child_family_ids(family_id):
        :noindex:


    .. py:method:: get_child_families(family_id):
        :noindex:


    .. py:method:: is_descendant_of_family(id_, family_id):
        :noindex:


    .. py:method:: get_family_node_ids(family_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


    .. py:method:: get_family_nodes(family_id, ancestor_levels, descendant_levels, include_siblings):
        :noindex:


Family Hierarchy Design Session
-------------------------------

.. py:class:: FamilyHierarchyDesignSession(abc_relationship_sessions.FamilyHierarchyDesignSession, osid_sessions.OsidSession)
    This session manages a hierarchy of families may be organized into a hierarchy for organizing or
    federating.


    A parent ``Family`` includes all of the relationships of its
    children such that a single root node contains all of the
    relationships of the federation.





    .. py:method:: get_family_hierarchy_id():
        :noindex:


    .. py:attribute:: family_hierarchy_id
        :noindex:


    .. py:method:: get_family_hierarchy():
        :noindex:


    .. py:attribute:: family_hierarchy
        :noindex:


    .. py:method:: can_modify_family_hierarchy():
        :noindex:


    .. py:method:: add_root_family(family_id):
        :noindex:


    .. py:method:: remove_root_family(family_id):
        :noindex:


    .. py:method:: add_child_family(family_id, child_id):
        :noindex:


    .. py:method:: remove_child_family(family_id, child_id):
        :noindex:


    .. py:method:: remove_child_families(family_id):
        :noindex:


