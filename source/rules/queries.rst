.. currentmodule:: dlkit.rules.queries
.. automodule:: dlkit.rules.queries

Queries
=======


Rule Query
----------

.. autoclass:: RuleQuery
   :show-inheritance:

   .. automethod:: RuleQuery.match_engine_id

   .. autoattribute:: RuleQuery.engine_id_terms

   .. automethod:: RuleQuery.supports_engine_query

   .. autoattribute:: RuleQuery.engine_query

   .. autoattribute:: RuleQuery.engine_terms

   .. automethod:: RuleQuery.get_rule_query_record



Engine Query
------------

.. autoclass:: EngineQuery
   :show-inheritance:

   .. automethod:: EngineQuery.match_rule_id

   .. autoattribute:: EngineQuery.rule_id_terms

   .. automethod:: EngineQuery.supports_rule_query

   .. autoattribute:: EngineQuery.rule_query

   .. automethod:: EngineQuery.match_any_rule

   .. autoattribute:: EngineQuery.rule_terms

   .. automethod:: EngineQuery.match_ancestor_engine_id

   .. autoattribute:: EngineQuery.ancestor_engine_id_terms

   .. automethod:: EngineQuery.supports_ancestor_engine_query

   .. autoattribute:: EngineQuery.ancestor_engine_query

   .. automethod:: EngineQuery.match_any_ancestor_engine

   .. autoattribute:: EngineQuery.ancestor_engine_terms

   .. automethod:: EngineQuery.match_descendant_engine_id

   .. autoattribute:: EngineQuery.descendant_engine_id_terms

   .. automethod:: EngineQuery.supports_descendant_engine_query

   .. autoattribute:: EngineQuery.descendant_engine_query

   .. automethod:: EngineQuery.match_any_descendant_engine

   .. autoattribute:: EngineQuery.descendant_engine_terms

   .. automethod:: EngineQuery.get_engine_query_record



