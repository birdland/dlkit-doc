

Searches
========


Item Search
-----------

.. py:class:: ItemSearch(abc_assessment_searches.ItemSearch, osid_searches.OsidSearch)
    ``ItemSearch`` defines the interface for specifying item search options.

    .. py:method:: search_among_items(item_ids):
        :noindex:


    .. py:method:: order_item_results(item_search_order):
        :noindex:


    .. py:method:: get_item_search_record(item_search_record_type):
        :noindex:


Item Search Results
-------------------

.. py:class:: ItemSearchResults(abc_assessment_searches.ItemSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_items():
        :noindex:


    .. py:attribute:: items
        :noindex:


    .. py:method:: get_item_query_inspector():
        :noindex:


    .. py:attribute:: item_query_inspector
        :noindex:


    .. py:method:: get_item_search_results_record(item_search_record_type):
        :noindex:


Assessment Search
-----------------

.. py:class:: AssessmentSearch(abc_assessment_searches.AssessmentSearch, osid_searches.OsidSearch)
    ``AssessmentSearch`` defines the interface for specifying assessment search options.

    .. py:method:: search_among_assessments(assessment_ids):
        :noindex:


    .. py:method:: order_assessment_results(assessment_search_order):
        :noindex:


    .. py:method:: get_assessment_search_record(assessment_search_record_type):
        :noindex:


Assessment Search Results
-------------------------

.. py:class:: AssessmentSearchResults(abc_assessment_searches.AssessmentSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_assessments():
        :noindex:


    .. py:attribute:: assessments
        :noindex:


    .. py:method:: get_assessment_query_inspector():
        :noindex:


    .. py:attribute:: assessment_query_inspector
        :noindex:


    .. py:method:: get_assessment_search_results_record(assessment_search_record_type):
        :noindex:


Assessment Offered Search
-------------------------

.. py:class:: AssessmentOfferedSearch(abc_assessment_searches.AssessmentOfferedSearch, osid_searches.OsidSearch)
    ``AssessmentOfferedSearch`` defines the interface for specifying assessment search options.

    .. py:method:: search_among_assessments_offered(assessment_offrered_ids):
        :noindex:


    .. py:method:: order_assessment_offered_results(assessment_offered_search_order):
        :noindex:


    .. py:method:: get_assessment_offered_search_record(assessment_offered_search_record_type):
        :noindex:


Assessment Offered Search Results
---------------------------------

.. py:class:: AssessmentOfferedSearchResults(abc_assessment_searches.AssessmentOfferedSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_assessments_offered():
        :noindex:


    .. py:attribute:: assessments_offered
        :noindex:


    .. py:method:: get_assessment_offered_query_inspector():
        :noindex:


    .. py:attribute:: assessment_offered_query_inspector
        :noindex:


    .. py:method:: get_assessment_offered_search_results_record(assessment_offered_search_record_type):
        :noindex:


Assessment Taken Search
-----------------------

.. py:class:: AssessmentTakenSearch(abc_assessment_searches.AssessmentTakenSearch, osid_searches.OsidSearch)
    ``AssessmentTakenSearch`` defines the interface for specifying assessment search options.

    .. py:method:: search_among_assessments_taken(assessment_taken_ids):
        :noindex:


    .. py:method:: order_assessment_taken_results(assessment_taken_search_order):
        :noindex:


    .. py:method:: get_assessment_taken_search_record(assessment_taken_search_record_type):
        :noindex:


Assessment Taken Search Results
-------------------------------

.. py:class:: AssessmentTakenSearchResults(abc_assessment_searches.AssessmentTakenSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_assessments_taken():
        :noindex:


    .. py:attribute:: assessments_taken
        :noindex:


    .. py:method:: get_assessment_taken_query_inspector():
        :noindex:


    .. py:attribute:: assessment_taken_query_inspector
        :noindex:


    .. py:method:: get_assessment_taken_search_results_record(assessment_taken_search_record_type):
        :noindex:


Bank Search
-----------

.. py:class:: BankSearch(abc_assessment_searches.BankSearch, osid_searches.OsidSearch)
    The interface for governing bank searches.

    .. py:method:: search_among_banks(bank_ids):
        :noindex:


    .. py:method:: order_bank_results(bank_search_order):
        :noindex:


    .. py:method:: get_bank_search_record(bank_search_record_type):
        :noindex:


Bank Search Results
-------------------

.. py:class:: BankSearchResults(abc_assessment_searches.BankSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_banks():
        :noindex:


    .. py:attribute:: banks
        :noindex:


    .. py:method:: get_bank_query_inspector():
        :noindex:


    .. py:attribute:: bank_query_inspector
        :noindex:


    .. py:method:: get_bank_search_results_record(bank_search_record_type):
        :noindex:


