.. currentmodule:: dlkit.acknowledgement.objects
.. automodule:: dlkit.acknowledgement.objects

Objects
=======


Credit
------

.. autoclass:: Credit
   :show-inheritance:

   .. autoattribute:: Credit.reference_id

   .. autoattribute:: Credit.resource_id

   .. autoattribute:: Credit.resource

   .. automethod:: Credit.get_credit_record



Credit Form
-----------

.. autoclass:: CreditForm
   :show-inheritance:

   .. automethod:: CreditForm.get_credit_form_record



Credit List
-----------

.. autoclass:: CreditList
   :show-inheritance:

   .. autoattribute:: CreditList.next_credit

   .. automethod:: CreditList.get_next_credits



Billing Form
------------

.. autoclass:: BillingForm
   :show-inheritance:

   .. automethod:: BillingForm.get_billing_form_record



Billing List
------------

.. autoclass:: BillingList
   :show-inheritance:

   .. autoattribute:: BillingList.next_billing

   .. automethod:: BillingList.get_next_billings



Billing Node
------------

.. autoclass:: BillingNode
   :show-inheritance:

   .. autoattribute:: BillingNode.billing

   .. autoattribute:: BillingNode.parent_billing_nodes

   .. autoattribute:: BillingNode.child_billing_nodes



Billing Node List
-----------------

.. autoclass:: BillingNodeList
   :show-inheritance:

   .. autoattribute:: BillingNodeList.next_billing_node

   .. automethod:: BillingNodeList.get_next_billing_nodes



