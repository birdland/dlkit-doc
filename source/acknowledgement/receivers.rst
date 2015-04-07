.. currentmodule:: dlkit.acknowledgement.receivers
.. automodule:: dlkit.acknowledgement.receivers

Receivers
=========


Credit Receiver
---------------

.. autoclass:: CreditReceiver
   :show-inheritance:

   .. automethod:: CreditReceiver.new_credits

   .. automethod:: CreditReceiver.changed_credits

   .. automethod:: CreditReceiver.deleted_credits



Billing Receiver
----------------

.. autoclass:: BillingReceiver
   :show-inheritance:

   .. automethod:: BillingReceiver.new_billings

   .. automethod:: BillingReceiver.changed_billings

   .. automethod:: BillingReceiver.deleted_billings

   .. automethod:: BillingReceiver.changed_child_of_billings



