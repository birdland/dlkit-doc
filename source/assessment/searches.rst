
.. currentmodule:: dlkit.assessment.searches
.. automodule:: dlkit.assessment.searches

Searches
========


Item Search
-----------

.. autoclass:: ItemSearch
   :show-inheritance:

   .. automethod:: ItemSearch.search_among_items

   .. automethod:: ItemSearch.order_item_results

   .. automethod:: ItemSearch.get_item_search_record

Item Search Results
-------------------

.. autoclass:: ItemSearchResults
   :show-inheritance:

   .. autoattribute:: ItemSearchResults.items

   .. autoattribute:: ItemSearchResults.item_query_inspector

   .. automethod:: ItemSearchResults.get_item_search_results_record

Assessment Search
-----------------

.. autoclass:: AssessmentSearch
   :show-inheritance:

   .. automethod:: AssessmentSearch.search_among_assessments

   .. automethod:: AssessmentSearch.order_assessment_results

   .. automethod:: AssessmentSearch.get_assessment_search_record

Assessment Search Results
-------------------------

.. autoclass:: AssessmentSearchResults
   :show-inheritance:

   .. autoattribute:: AssessmentSearchResults.assessments

   .. autoattribute:: AssessmentSearchResults.assessment_query_inspector

   .. automethod:: AssessmentSearchResults.get_assessment_search_results_record

Assessment Offered Search
-------------------------

.. autoclass:: AssessmentOfferedSearch
   :show-inheritance:

   .. automethod:: AssessmentOfferedSearch.search_among_assessments_offered

   .. automethod:: AssessmentOfferedSearch.order_assessment_offered_results

   .. automethod:: AssessmentOfferedSearch.get_assessment_offered_search_record

Assessment Offered Search Results
---------------------------------

.. autoclass:: AssessmentOfferedSearchResults
   :show-inheritance:

   .. autoattribute:: AssessmentOfferedSearchResults.assessments_offered

   .. autoattribute:: AssessmentOfferedSearchResults.assessment_offered_query_inspector

   .. automethod:: AssessmentOfferedSearchResults.get_assessment_offered_search_results_record

Assessment Taken Search
-----------------------

.. autoclass:: AssessmentTakenSearch
   :show-inheritance:

   .. automethod:: AssessmentTakenSearch.search_among_assessments_taken

   .. automethod:: AssessmentTakenSearch.order_assessment_taken_results

   .. automethod:: AssessmentTakenSearch.get_assessment_taken_search_record

Assessment Taken Search Results
-------------------------------

.. autoclass:: AssessmentTakenSearchResults
   :show-inheritance:

   .. autoattribute:: AssessmentTakenSearchResults.assessments_taken

   .. autoattribute:: AssessmentTakenSearchResults.assessment_taken_query_inspector

   .. automethod:: AssessmentTakenSearchResults.get_assessment_taken_search_results_record

Bank Search
-----------

.. autoclass:: BankSearch
   :show-inheritance:

   .. automethod:: BankSearch.search_among_banks

   .. automethod:: BankSearch.order_bank_results

   .. automethod:: BankSearch.get_bank_search_record

Bank Search Results
-------------------

.. autoclass:: BankSearchResults
   :show-inheritance:

   .. autoattribute:: BankSearchResults.banks

   .. autoattribute:: BankSearchResults.bank_query_inspector

   .. automethod:: BankSearchResults.get_bank_search_results_record

