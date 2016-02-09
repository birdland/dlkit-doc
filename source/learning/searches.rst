
.. currentmodule:: dlkit.learning.searches
.. automodule:: dlkit.learning.searches

Searches
========


Objective Search
----------------

.. autoclass:: ObjectiveSearch
   :show-inheritance:

   .. automethod:: ObjectiveSearch.search_among_objectives

   .. automethod:: ObjectiveSearch.order_objective_results

   .. automethod:: ObjectiveSearch.get_objective_search_record

Objective Search Results
------------------------

.. autoclass:: ObjectiveSearchResults
   :show-inheritance:

   .. autoattribute:: ObjectiveSearchResults.objectives

   .. autoattribute:: ObjectiveSearchResults.objective_query_inspector

   .. automethod:: ObjectiveSearchResults.get_objective_search_results_record

Activity Search
---------------

.. autoclass:: ActivitySearch
   :show-inheritance:

   .. automethod:: ActivitySearch.search_among_activities

   .. automethod:: ActivitySearch.order_activity_results

   .. automethod:: ActivitySearch.get_activity_search_record

Activity Search Results
-----------------------

.. autoclass:: ActivitySearchResults
   :show-inheritance:

   .. autoattribute:: ActivitySearchResults.activities

   .. autoattribute:: ActivitySearchResults.activity_query_inspector

   .. automethod:: ActivitySearchResults.get_activity_search_results_record

Proficiency Search
------------------

.. autoclass:: ProficiencySearch
   :show-inheritance:

   .. automethod:: ProficiencySearch.search_among_proficiencies

   .. automethod:: ProficiencySearch.order_proficiency_results

   .. automethod:: ProficiencySearch.get_proficiency_search_record

Proficiency Search Results
--------------------------

.. autoclass:: ProficiencySearchResults
   :show-inheritance:

   .. autoattribute:: ProficiencySearchResults.proficiencies

   .. autoattribute:: ProficiencySearchResults.proficiency_query_inspector

   .. automethod:: ProficiencySearchResults.get_proficiency_search_results_record

Objective Bank Search
---------------------

.. autoclass:: ObjectiveBankSearch
   :show-inheritance:

   .. automethod:: ObjectiveBankSearch.search_among_objective_banks

   .. automethod:: ObjectiveBankSearch.order_objective_bank_results

   .. automethod:: ObjectiveBankSearch.get_objective_bank_search_record

Objective Bank Search Results
-----------------------------

.. autoclass:: ObjectiveBankSearchResults
   :show-inheritance:

   .. autoattribute:: ObjectiveBankSearchResults.objective_banks

   .. autoattribute:: ObjectiveBankSearchResults.objective_bank_query_inspector

   .. automethod:: ObjectiveBankSearchResults.get_objective_bank_search_results_record

