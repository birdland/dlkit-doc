
.. currentmodule:: dlkit.logging_.queries
.. automodule:: dlkit.logging_.queries

Queries
=======


Log Entry Query
---------------

.. autoclass:: LogEntryQuery
   :show-inheritance:

   .. automethod:: LogEntryQuery.match_priority

   .. automethod:: LogEntryQuery.match_any_priority

   .. autoattribute:: LogEntryQuery.priority_terms

   .. automethod:: LogEntryQuery.match_minimum_priority

   .. autoattribute:: LogEntryQuery.minimum_priority_terms

   .. automethod:: LogEntryQuery.match_timestamp

   .. autoattribute:: LogEntryQuery.timestamp_terms

   .. automethod:: LogEntryQuery.match_resource_id

   .. autoattribute:: LogEntryQuery.resource_id_terms

   .. automethod:: LogEntryQuery.supports_resource_query

   .. autoattribute:: LogEntryQuery.resource_query

   .. autoattribute:: LogEntryQuery.resource_terms

   .. automethod:: LogEntryQuery.match_agent_id

   .. autoattribute:: LogEntryQuery.agent_id_terms

   .. automethod:: LogEntryQuery.supports_agent_query

   .. autoattribute:: LogEntryQuery.agent_query

   .. autoattribute:: LogEntryQuery.agent_terms

   .. automethod:: LogEntryQuery.match_log_id

   .. autoattribute:: LogEntryQuery.log_id_terms

   .. automethod:: LogEntryQuery.supports_log_query

   .. autoattribute:: LogEntryQuery.log_query

   .. autoattribute:: LogEntryQuery.log_terms

   .. automethod:: LogEntryQuery.get_log_entry_query_record

Log Query
---------

.. autoclass:: LogQuery
   :show-inheritance:

   .. automethod:: LogQuery.match_log_entry_id

   .. autoattribute:: LogQuery.log_entry_id_terms

   .. automethod:: LogQuery.supports_log_entry_query

   .. autoattribute:: LogQuery.log_entry_query

   .. automethod:: LogQuery.match_any_log_entry

   .. autoattribute:: LogQuery.log_entry_terms

   .. automethod:: LogQuery.match_ancestor_log_id

   .. autoattribute:: LogQuery.ancestor_log_id_terms

   .. automethod:: LogQuery.supports_ancestor_log_query

   .. autoattribute:: LogQuery.ancestor_log_query

   .. automethod:: LogQuery.match_any_ancestor_log

   .. autoattribute:: LogQuery.ancestor_log_terms

   .. automethod:: LogQuery.match_descendant_log_id

   .. autoattribute:: LogQuery.descendant_log_id_terms

   .. automethod:: LogQuery.supports_descendant_log_query

   .. autoattribute:: LogQuery.descendant_log_query

   .. automethod:: LogQuery.match_any_descendant_log

   .. autoattribute:: LogQuery.descendant_log_terms

   .. automethod:: LogQuery.get_log_query_record

