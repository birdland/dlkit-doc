

Queries
=======


Relationship Query
------------------

.. py:class:: RelationshipQuery(abc_relationship_queries.RelationshipQuery, osid_queries.OsidRelationshipQuery)
    This is the query for searching relationships.


    Each method match specifies an ``AND`` term while multiple
    invocations of the same method produce a nested ``OR``.





    .. py:method:: match_source_id(peer, match):
        :noindex:


    .. py:method:: clear_source_id_terms():
        :noindex:


    .. py:attribute:: source_id_terms
        :noindex:


    .. py:method:: match_destination_id(peer, match):
        :noindex:


    .. py:method:: clear_destination_id_terms():
        :noindex:


    .. py:attribute:: destination_id_terms
        :noindex:


    .. py:method:: match_same_peer_id(match):
        :noindex:


    .. py:method:: clear_same_peer_id_terms():
        :noindex:


    .. py:attribute:: same_peer_id_terms
        :noindex:


    .. py:method:: match_family_id(family_id, match):
        :noindex:


    .. py:method:: clear_family_id_terms():
        :noindex:


    .. py:attribute:: family_id_terms
        :noindex:


    .. py:method:: supports_family_query():
        :noindex:


    .. py:method:: get_family_query():
        :noindex:


    .. py:attribute:: family_query
        :noindex:


    .. py:method:: clear_family_terms():
        :noindex:


    .. py:attribute:: family_terms
        :noindex:


    .. py:method:: get_relationship_query_record(relationship_record_type):
        :noindex:


Family Query
------------

.. py:class:: FamilyQuery(abc_relationship_queries.FamilyQuery, osid_queries.OsidCatalogQuery)
    This is the query interface for searching for families.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_relationship_id(relationship_id, match):
        :noindex:


    .. py:method:: clear_relationship_id_terms():
        :noindex:


    .. py:attribute:: relationship_id_terms
        :noindex:


    .. py:method:: supports_relationship_query():
        :noindex:


    .. py:method:: get_relationship_query():
        :noindex:


    .. py:attribute:: relationship_query
        :noindex:


    .. py:method:: match_any_relationship(match):
        :noindex:


    .. py:method:: clear_relationship_terms():
        :noindex:


    .. py:attribute:: relationship_terms
        :noindex:


    .. py:method:: match_ancestor_family_id(family_id, match):
        :noindex:


    .. py:method:: clear_ancestor_family_id_terms():
        :noindex:


    .. py:attribute:: ancestor_family_id_terms
        :noindex:


    .. py:method:: supports_ancestor_family_query():
        :noindex:


    .. py:method:: get_ancestor_family_query():
        :noindex:


    .. py:attribute:: ancestor_family_query
        :noindex:


    .. py:method:: match_any_ancestor_family(match):
        :noindex:


    .. py:method:: clear_ancestor_family_terms():
        :noindex:


    .. py:attribute:: ancestor_family_terms
        :noindex:


    .. py:method:: match_descendant_family_id(family_id, match):
        :noindex:


    .. py:method:: clear_descendant_family_id_terms():
        :noindex:


    .. py:attribute:: descendant_family_id_terms
        :noindex:


    .. py:method:: supports_descendant_family_query():
        :noindex:


    .. py:method:: get_descendant_family_query():
        :noindex:


    .. py:attribute:: descendant_family_query
        :noindex:


    .. py:method:: match_any_descendant_family(match):
        :noindex:


    .. py:method:: clear_descendant_family_terms():
        :noindex:


    .. py:attribute:: descendant_family_terms
        :noindex:


    .. py:method:: get_family_query_record(family_record_type):
        :noindex:


