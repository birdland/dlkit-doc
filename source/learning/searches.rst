

Searches
========


Objective Search
----------------

.. py:class:: ObjectiveSearch(abc_learning_searches.ObjectiveSearch, osid_searches.OsidSearch)
    ``ObjectiveSearch`` defines the interface for specifying objective search options.

    .. py:method:: search_among_objectives(objective_ids):
        :noindex:


    .. py:method:: order_objective_results(objective_search_order):
        :noindex:


    .. py:method:: get_objective_search_record(objective_search_record_type):
        :noindex:


Objective Search Results
------------------------

.. py:class:: ObjectiveSearchResults(abc_learning_searches.ObjectiveSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_objectives():
        :noindex:


    .. py:attribute:: objectives
        :noindex:


    .. py:method:: get_objective_query_inspector():
        :noindex:


    .. py:attribute:: objective_query_inspector
        :noindex:


    .. py:method:: get_objective_search_results_record(objective_search_record_type):
        :noindex:


Activity Search
---------------

.. py:class:: ActivitySearch(abc_learning_searches.ActivitySearch, osid_searches.OsidSearch)
    ``ActivitySearch`` defines the interface for specifying activity search options.

    .. py:method:: search_among_activities(activity_ids):
        :noindex:


    .. py:method:: order_activity_results(activitiesearch_order):
        :noindex:


    .. py:method:: get_activity_search_record(activitiesearch_record_type):
        :noindex:


Activity Search Results
-----------------------

.. py:class:: ActivitySearchResults(abc_learning_searches.ActivitySearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_activities():
        :noindex:


    .. py:attribute:: activities
        :noindex:


    .. py:method:: get_activity_query_inspector():
        :noindex:


    .. py:attribute:: activity_query_inspector
        :noindex:


    .. py:method:: get_activity_search_results_record(activitiesearch_record_type):
        :noindex:


Objective Bank Search
---------------------

.. py:class:: ObjectiveBankSearch(abc_learning_searches.ObjectiveBankSearch, osid_searches.OsidSearch)
    The interface for governing objective bank searches.

    .. py:method:: search_among_objective_banks(objective_bank_ids):
        :noindex:


    .. py:method:: order_objective_bank_results(objective_bank_search_order):
        :noindex:


    .. py:method:: get_objective_bank_search_record(objective_bank_search_record_type):
        :noindex:


Objective Bank Search Results
-----------------------------

.. py:class:: ObjectiveBankSearchResults(abc_learning_searches.ObjectiveBankSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_objective_banks():
        :noindex:


    .. py:attribute:: objective_banks
        :noindex:


    .. py:method:: get_objective_bank_query_inspector():
        :noindex:


    .. py:attribute:: objective_bank_query_inspector
        :noindex:


    .. py:method:: get_objective_bank_search_results_record(objective_bank_search_record_type):
        :noindex:


