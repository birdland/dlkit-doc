.. currentmodule:: dlkit.acknowledgement.searches
.. automodule:: dlkit.acknowledgement.searches

Searches
========


Credit Search
-------------

.. autoclass:: CreditSearch
   :show-inheritance:

   .. automethod:: CreditSearch.search_among_credits

   .. automethod:: CreditSearch.order_credit_results

   .. automethod:: CreditSearch.get_credit_search_record



Credit Search Results
---------------------

.. autoclass:: CreditSearchResults
   :show-inheritance:

   .. autoattribute:: CreditSearchResults.credits

   .. autoattribute:: CreditSearchResults.credit_query_inspector

   .. automethod:: CreditSearchResults.get_credit_search_results_record



Billing Search
--------------

.. autoclass:: BillingSearch
   :show-inheritance:

   .. automethod:: BillingSearch.search_among_billings

   .. automethod:: BillingSearch.order_billing_results

   .. automethod:: BillingSearch.get_billing_search_record



Billing Search Results
----------------------

.. autoclass:: BillingSearchResults
   :show-inheritance:

   .. autoattribute:: BillingSearchResults.billings

   .. autoattribute:: BillingSearchResults.billing_query_inspector

   .. automethod:: BillingSearchResults.get_billing_search_results_record



