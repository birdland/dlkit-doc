.. currentmodule:: dlkit.acknowledgement.queries
.. automodule:: dlkit.acknowledgement.queries

Queries
=======


Credit Query
------------

.. autoclass:: CreditQuery
   :show-inheritance:

   .. automethod:: CreditQuery.match_reference_id

   .. autoattribute:: CreditQuery.reference_id_terms

   .. automethod:: CreditQuery.match_resource_id

   .. autoattribute:: CreditQuery.resource_id_terms

   .. automethod:: CreditQuery.supports_resource_query

   .. autoattribute:: CreditQuery.resource_query

   .. autoattribute:: CreditQuery.resource_terms

   .. automethod:: CreditQuery.match_billing_id

   .. autoattribute:: CreditQuery.billing_id_terms

   .. automethod:: CreditQuery.supports_billing_query

   .. autoattribute:: CreditQuery.billing_query

   .. autoattribute:: CreditQuery.billing_terms

   .. automethod:: CreditQuery.get_credit_query_record



Billing Query
-------------

.. autoclass:: BillingQuery
   :show-inheritance:

   .. automethod:: BillingQuery.match_credit_id

   .. autoattribute:: BillingQuery.credit_id_terms

   .. automethod:: BillingQuery.supports_credit_query

   .. autoattribute:: BillingQuery.credit_query

   .. automethod:: BillingQuery.match_any_credit

   .. autoattribute:: BillingQuery.credit_terms

   .. automethod:: BillingQuery.match_ancestor_billing_id

   .. autoattribute:: BillingQuery.ancestor_billing_id_terms

   .. automethod:: BillingQuery.supports_ancestor_billing_query

   .. autoattribute:: BillingQuery.ancestor_billing_query

   .. automethod:: BillingQuery.match_any_ancestor_billing

   .. autoattribute:: BillingQuery.ancestor_billing_terms

   .. automethod:: BillingQuery.match_descendant_billing_id

   .. autoattribute:: BillingQuery.descendant_billing_id_terms

   .. automethod:: BillingQuery.supports_descendant_billing_query

   .. autoattribute:: BillingQuery.descendant_billing_query

   .. automethod:: BillingQuery.match_any_descendant_billing

   .. autoattribute:: BillingQuery.descendant_billing_terms

   .. automethod:: BillingQuery.get_billing_query_record



