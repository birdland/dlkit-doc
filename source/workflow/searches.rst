.. currentmodule:: dlkit.abstract_osid.workflow.searches
.. automodule:: dlkit.abstract_osid.workflow.searches

Searches
========


Process Search
--------------

.. autoclass:: ProcessSearch
   :show-inheritance:

.. automethod:: ProcessSearch.search_among_processes

.. automethod:: ProcessSearch.order_process_results

.. automethod:: ProcessSearch.get_process_search_record



Process Search Results
----------------------

.. autoclass:: ProcessSearchResults
   :show-inheritance:

.. autoattribute:: ProcessSearchResults.processes

.. autoattribute:: ProcessSearchResults.process_query_inspector

.. automethod:: ProcessSearchResults.get_process_search_results_record



Step Search
-----------

.. autoclass:: StepSearch
   :show-inheritance:

.. automethod:: StepSearch.search_among_steps

.. automethod:: StepSearch.order_step_results

.. automethod:: StepSearch.get_step_search_record



Step Search Results
-------------------

.. autoclass:: StepSearchResults
   :show-inheritance:

.. autoattribute:: StepSearchResults.steps

.. autoattribute:: StepSearchResults.step_query_inspector

.. automethod:: StepSearchResults.get_step_search_results_record



Work Search
-----------

.. autoclass:: WorkSearch
   :show-inheritance:

.. automethod:: WorkSearch.search_among_works

.. automethod:: WorkSearch.order_work_results

.. automethod:: WorkSearch.get_work_search_record



Work Search Results
-------------------

.. autoclass:: WorkSearchResults
   :show-inheritance:

.. autoattribute:: WorkSearchResults.works

.. autoattribute:: WorkSearchResults.work_query_inspector

.. automethod:: WorkSearchResults.get_work_search_results_record



Office Search
-------------

.. autoclass:: OfficeSearch
   :show-inheritance:

.. automethod:: OfficeSearch.search_among_offices

.. automethod:: OfficeSearch.order_office_results

.. automethod:: OfficeSearch.get_office_search_record



Office Search Results
---------------------

.. autoclass:: OfficeSearchResults
   :show-inheritance:

.. autoattribute:: OfficeSearchResults.offices

.. autoattribute:: OfficeSearchResults.office_query_inspector

.. automethod:: OfficeSearchResults.get_office_search_results_record



