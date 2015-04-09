.. currentmodule:: dlkit.rules.query_inspectors
.. automodule:: dlkit.rules.query_inspectors

Query Inspectors
================


Rule Query Inspector
--------------------

.. autoclass:: RuleQueryInspector
   :show-inheritance:

   .. autoattribute:: RuleQueryInspector.engine_id_terms

   .. autoattribute:: RuleQueryInspector.engine_terms

   .. automethod:: RuleQueryInspector.get_rule_query_inspector_record



Engine Query Inspector
----------------------

.. autoclass:: EngineQueryInspector
   :show-inheritance:

   .. autoattribute:: EngineQueryInspector.rule_id_terms

   .. autoattribute:: EngineQueryInspector.rule_terms

   .. autoattribute:: EngineQueryInspector.ancestor_engine_id_terms

   .. autoattribute:: EngineQueryInspector.ancestor_engine_terms

   .. autoattribute:: EngineQueryInspector.descendant_engine_id_terms

   .. autoattribute:: EngineQueryInspector.descendant_engine_terms

   .. automethod:: EngineQueryInspector.get_engine_query_inspector_record



