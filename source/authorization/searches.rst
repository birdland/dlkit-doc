.. currentmodule:: dlkit.authorization.searches
.. automodule:: dlkit.authorization.searches

Searches
========


Authorization Search
--------------------

.. autoclass:: AuthorizationSearch
   :show-inheritance:

.. automethod:: AuthorizationSearch.search_among_authorizations

.. automethod:: AuthorizationSearch.order_authorization_results

.. automethod:: AuthorizationSearch.get_authorization_search_record



Authorization Search Results
----------------------------

.. autoclass:: AuthorizationSearchResults
   :show-inheritance:

.. autoattribute:: AuthorizationSearchResults.authorizations

.. autoattribute:: AuthorizationSearchResults.authorization_query_inspector

.. automethod:: AuthorizationSearchResults.get_authorization_search_results_record



Function Search
---------------

.. autoclass:: FunctionSearch
   :show-inheritance:

.. automethod:: FunctionSearch.search_among_functions

.. automethod:: FunctionSearch.order_function_results

.. automethod:: FunctionSearch.get_function_search_record



Function Search Results
-----------------------

.. autoclass:: FunctionSearchResults
   :show-inheritance:

.. autoattribute:: FunctionSearchResults.functions

.. autoattribute:: FunctionSearchResults.function_query_inspector

.. automethod:: FunctionSearchResults.get_function_search_results_record



Qualifier Search
----------------

.. autoclass:: QualifierSearch
   :show-inheritance:

.. automethod:: QualifierSearch.search_among_qualifiers

.. automethod:: QualifierSearch.order_qualifier_results

.. automethod:: QualifierSearch.get_qualifier_search_record



Qualifier Search Results
------------------------

.. autoclass:: QualifierSearchResults
   :show-inheritance:

.. autoattribute:: QualifierSearchResults.qualifiers

.. autoattribute:: QualifierSearchResults.qualifier_query_inspector

.. automethod:: QualifierSearchResults.get_qualifier_search_results_record



Vault Search
------------

.. autoclass:: VaultSearch
   :show-inheritance:

.. automethod:: VaultSearch.search_among_vaults

.. automethod:: VaultSearch.order_vault_results

.. automethod:: VaultSearch.get_vault_search_record



Vault Search Results
--------------------

.. autoclass:: VaultSearchResults
   :show-inheritance:

.. autoattribute:: VaultSearchResults.vaults

.. autoattribute:: VaultSearchResults.vault_query_inspector

.. automethod:: VaultSearchResults.get_vault_search_results_record



