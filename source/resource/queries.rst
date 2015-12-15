

Queries
=======


Resource Query
--------------

.. py:class:: ResourceQuery(abc_resource_queries.ResourceQuery, osid_queries.OsidObjectQuery)
    This is the query for searching resources.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_group(match):
        :noindex:


    .. py:method:: clear_group_terms():
        :noindex:


    .. py:attribute:: group_terms
        :noindex:


    .. py:method:: match_demographic(match):
        :noindex:


    .. py:method:: clear_demographic_terms():
        :noindex:


    .. py:attribute:: demographic_terms
        :noindex:


    .. py:method:: match_containing_group_id(resource_id, match):
        :noindex:


    .. py:method:: clear_containing_group_id_terms():
        :noindex:


    .. py:attribute:: containing_group_id_terms
        :noindex:


    .. py:method:: supports_containing_group_query():
        :noindex:


    .. py:method:: get_containing_group_query():
        :noindex:


    .. py:attribute:: containing_group_query
        :noindex:


    .. py:method:: match_any_containing_group(match):
        :noindex:


    .. py:method:: clear_containing_group_terms():
        :noindex:


    .. py:attribute:: containing_group_terms
        :noindex:


    .. py:method:: match_avatar_id(asset_id, match):
        :noindex:


    .. py:method:: clear_avatar_id_terms():
        :noindex:


    .. py:attribute:: avatar_id_terms
        :noindex:


    .. py:method:: supports_avatar_query():
        :noindex:


    .. py:method:: get_avatar_query():
        :noindex:


    .. py:attribute:: avatar_query
        :noindex:


    .. py:method:: match_any_avatar(match):
        :noindex:


    .. py:method:: clear_avatar_terms():
        :noindex:


    .. py:attribute:: avatar_terms
        :noindex:


    .. py:method:: match_agent_id(agent_id, match):
        :noindex:


    .. py:method:: clear_agent_id_terms():
        :noindex:


    .. py:attribute:: agent_id_terms
        :noindex:


    .. py:method:: supports_agent_query():
        :noindex:


    .. py:method:: get_agent_query():
        :noindex:


    .. py:attribute:: agent_query
        :noindex:


    .. py:method:: match_any_agent(match):
        :noindex:


    .. py:method:: clear_agent_terms():
        :noindex:


    .. py:attribute:: agent_terms
        :noindex:


    .. py:method:: match_resource_relationship_id(resource_relationship_id, match):
        :noindex:


    .. py:method:: clear_resource_relationship_id_terms():
        :noindex:


    .. py:attribute:: resource_relationship_id_terms
        :noindex:


    .. py:method:: supports_resource_relationship_query():
        :noindex:


    .. py:method:: get_resource_relationship_query():
        :noindex:


    .. py:attribute:: resource_relationship_query
        :noindex:


    .. py:method:: match_any_resource_relationship(match):
        :noindex:


    .. py:method:: clear_resource_relationship_terms():
        :noindex:


    .. py:attribute:: resource_relationship_terms
        :noindex:


    .. py:method:: match_bin_id(bin_id, match):
        :noindex:


    .. py:method:: clear_bin_id_terms():
        :noindex:


    .. py:attribute:: bin_id_terms
        :noindex:


    .. py:method:: supports_bin_query():
        :noindex:


    .. py:method:: get_bin_query():
        :noindex:


    .. py:attribute:: bin_query
        :noindex:


    .. py:method:: clear_bin_terms():
        :noindex:


    .. py:attribute:: bin_terms
        :noindex:


    .. py:method:: get_resource_query_record(resource_record_type):
        :noindex:


Bin Query
---------

.. py:class:: BinQuery(abc_resource_queries.BinQuery, osid_queries.OsidCatalogQuery)
    This is the query for searching bins.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_resource_id(resource_id, match):
        :noindex:


    .. py:method:: clear_resource_id_terms():
        :noindex:


    .. py:attribute:: resource_id_terms
        :noindex:


    .. py:method:: supports_resource_query():
        :noindex:


    .. py:method:: get_resource_query():
        :noindex:


    .. py:attribute:: resource_query
        :noindex:


    .. py:method:: match_any_resource(match):
        :noindex:


    .. py:method:: clear_resource_terms():
        :noindex:


    .. py:attribute:: resource_terms
        :noindex:


    .. py:method:: match_ancestor_bin_id(binid, match):
        :noindex:


    .. py:method:: clear_ancestor_bin_id_terms():
        :noindex:


    .. py:attribute:: ancestor_bin_id_terms
        :noindex:


    .. py:method:: supports_ancestor_bin_query():
        :noindex:


    .. py:method:: get_ancestor_bin_query():
        :noindex:


    .. py:attribute:: ancestor_bin_query
        :noindex:


    .. py:method:: match_any_ancestor_bin(match):
        :noindex:


    .. py:method:: clear_ancestor_bin_terms():
        :noindex:


    .. py:attribute:: ancestor_bin_terms
        :noindex:


    .. py:method:: match_descendant_bin_id(binid, match):
        :noindex:


    .. py:method:: clear_descendant_bin_id_terms():
        :noindex:


    .. py:attribute:: descendant_bin_id_terms
        :noindex:


    .. py:method:: supports_descendant_bin_query():
        :noindex:


    .. py:method:: get_descendant_bin_query():
        :noindex:


    .. py:attribute:: descendant_bin_query
        :noindex:


    .. py:method:: match_any_descendant_bin(match):
        :noindex:


    .. py:method:: clear_descendant_bin_terms():
        :noindex:


    .. py:attribute:: descendant_bin_terms
        :noindex:


    .. py:method:: get_bin_query_record(bin_record_type):
        :noindex:


