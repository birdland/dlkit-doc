.. currentmodule:: dlkit.configuration.searches
.. automodule:: dlkit.configuration.searches

Searches
========


Parameter Search
----------------

.. autoclass:: ParameterSearch
   :show-inheritance:

   .. automethod:: ParameterSearch.search_among_parameters

   .. automethod:: ParameterSearch.order_parameter_results

   .. automethod:: ParameterSearch.get_parameter_search_record



Parameter Search Results
------------------------

.. autoclass:: ParameterSearchResults
   :show-inheritance:

   .. autoattribute:: ParameterSearchResults.parameters

   .. autoattribute:: ParameterSearchResults.parameter_query_inspector

   .. automethod:: ParameterSearchResults.get_parameter_search_results_record



Value Search
------------

.. autoclass:: ValueSearch
   :show-inheritance:

   .. automethod:: ValueSearch.search_among_values

   .. automethod:: ValueSearch.order_value_results

   .. automethod:: ValueSearch.get_value_search_record



Value Search Results
--------------------

.. autoclass:: ValueSearchResults
   :show-inheritance:

   .. autoattribute:: ValueSearchResults.values

   .. autoattribute:: ValueSearchResults.value_query_inspector

   .. automethod:: ValueSearchResults.get_value_search_results_record



Configuration Search
--------------------

.. autoclass:: ConfigurationSearch
   :show-inheritance:

   .. automethod:: ConfigurationSearch.search_among_configurations

   .. automethod:: ConfigurationSearch.order_configuration_results

   .. automethod:: ConfigurationSearch.get_configuration_search_record



Configuration Search Results
----------------------------

.. autoclass:: ConfigurationSearchResults
   :show-inheritance:

   .. autoattribute:: ConfigurationSearchResults.configurations

   .. autoattribute:: ConfigurationSearchResults.configuration_query_inspector

   .. automethod:: ConfigurationSearchResults.get_configuration_search_results_record



