.. currentmodule:: dlkit.rules.searches
.. automodule:: dlkit.rules.searches

Searches
========


Rule Search
-----------

.. autoclass:: RuleSearch
   :show-inheritance:

   .. automethod:: RuleSearch.search_among_rules

   .. automethod:: RuleSearch.order_rule_results

   .. automethod:: RuleSearch.get_rule_search_record



Rule Search Results
-------------------

.. autoclass:: RuleSearchResults
   :show-inheritance:

   .. autoattribute:: RuleSearchResults.rules

   .. autoattribute:: RuleSearchResults.rule_query_inspector

   .. automethod:: RuleSearchResults.get_rule_search_results_record



Engine Search
-------------

.. autoclass:: EngineSearch
   :show-inheritance:

   .. automethod:: EngineSearch.search_among_engines

   .. automethod:: EngineSearch.order_engine_results

   .. automethod:: EngineSearch.get_engine_search_record



Engine Search Results
---------------------

.. autoclass:: EngineSearchResults
   :show-inheritance:

   .. autoattribute:: EngineSearchResults.engines

   .. autoattribute:: EngineSearchResults.engine_query_inspector

   .. automethod:: EngineSearchResults.get_engine_search_results_record



