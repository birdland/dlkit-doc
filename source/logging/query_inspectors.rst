.. currentmodule:: dlkit.logging.query_inspectors
.. automodule:: dlkit.logging.query_inspectors

Query_Inspectors
================


Log Entry Query Inspector
-------------------------

.. autoclass:: LogEntryQueryInspector
   :show-inheritance:

   .. autoattribute:: LogEntryQueryInspector.priority_terms

   .. autoattribute:: LogEntryQueryInspector.minimum_priority_terms

   .. autoattribute:: LogEntryQueryInspector.timestamp_terms

   .. autoattribute:: LogEntryQueryInspector.resource_id_terms

   .. autoattribute:: LogEntryQueryInspector.resource_terms

   .. autoattribute:: LogEntryQueryInspector.agent_id_terms

   .. autoattribute:: LogEntryQueryInspector.agent_terms

   .. autoattribute:: LogEntryQueryInspector.log_id_terms

   .. autoattribute:: LogEntryQueryInspector.log_terms

   .. automethod:: LogEntryQueryInspector.get_log_entry_query_inspector_record



Log Query Inspector
-------------------

.. autoclass:: LogQueryInspector
   :show-inheritance:

   .. autoattribute:: LogQueryInspector.log_entry_id_terms

   .. autoattribute:: LogQueryInspector.log_entry_terms

   .. autoattribute:: LogQueryInspector.ancestor_log_id_terms

   .. autoattribute:: LogQueryInspector.ancestor_log_terms

   .. autoattribute:: LogQueryInspector.descendant_log_id_terms

   .. autoattribute:: LogQueryInspector.descendant_log_terms

   .. automethod:: LogQueryInspector.get_log_query_inspector_record



