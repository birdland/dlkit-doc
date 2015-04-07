.. currentmodule:: dlkit.acknowledgement.query_inspectors
.. automodule:: dlkit.acknowledgement.query_inspectors

Query_Inspectors
================


Credit Query Inspector
----------------------

.. autoclass:: CreditQueryInspector
   :show-inheritance:

   .. autoattribute:: CreditQueryInspector.reference_id_terms

   .. autoattribute:: CreditQueryInspector.resource_id_terms

   .. autoattribute:: CreditQueryInspector.resource_terms

   .. autoattribute:: CreditQueryInspector.billing_id_terms

   .. autoattribute:: CreditQueryInspector.billing_terms

   .. automethod:: CreditQueryInspector.get_credit_query_inspector_record



Billing Query Inspector
-----------------------

.. autoclass:: BillingQueryInspector
   :show-inheritance:

   .. autoattribute:: BillingQueryInspector.credit_id_terms

   .. autoattribute:: BillingQueryInspector.credit_terms

   .. autoattribute:: BillingQueryInspector.ancestor_billing_id_terms

   .. autoattribute:: BillingQueryInspector.ancestor_billing_terms

   .. autoattribute:: BillingQueryInspector.descendant_billing_id_terms

   .. autoattribute:: BillingQueryInspector.descendant_billing_terms

   .. automethod:: BillingQueryInspector.get_billing_query_inspector_record



