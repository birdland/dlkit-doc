.. currentmodule:: dlkit.services.acknowledgement


Billing
=======


Billing
-------

.. autoclass:: Billing
   :show-inheritance:

   .. automethod:: Billing.get_billing_record



Credit Lookup Methods
---------------------

   .. autoattribute:: Billing.billing_id

   .. autoattribute:: Billing.billing

   .. automethod:: Billing.can_lookup_credits

   .. automethod:: Billing.use_comparative_credit_view

   .. automethod:: Billing.use_plenary_credit_view

   .. automethod:: Billing.use_federated_billing_view

   .. automethod:: Billing.use_isolated_billing_view

   .. automethod:: Billing.use_effective_credit_view

   .. automethod:: Billing.use_any_effective_credit_view

   .. automethod:: Billing.get_credit

   .. automethod:: Billing.get_credits_by_ids

   .. automethod:: Billing.get_credits_by_genus_type

   .. automethod:: Billing.get_credits_by_parent_genus_type

   .. automethod:: Billing.get_credits_by_record_type

   .. automethod:: Billing.get_credits_on_date

   .. automethod:: Billing.get_credits_by_genus_type_on_date

   .. automethod:: Billing.get_credits_for_resource

   .. automethod:: Billing.get_credits_for_resource_on_date

   .. automethod:: Billing.get_credits_by_genus_type_for_resource

   .. automethod:: Billing.get_credits_by_genus_type_for_resource_on_date

   .. automethod:: Billing.get_credits_for_reference

   .. automethod:: Billing.get_credits_for_reference_on_date

   .. automethod:: Billing.get_credits_by_genus_type_for_reference

   .. automethod:: Billing.get_credits_by_genus_type_for_reference_on_date

   .. automethod:: Billing.get_credits_for_resource_and_reference

   .. automethod:: Billing.get_credits_for_resource_and_reference_on_date

   .. automethod:: Billing.get_credits_by_genus_type_for_resource_and_reference

   .. automethod:: Billing.get_credits_by_genus_type_for_resource_and_reference_on_date

   .. autoattribute:: Billing.credits



Credit Query Methods
--------------------

   .. autoattribute:: Billing.billing_id

   .. autoattribute:: Billing.billing

   .. automethod:: Billing.can_search_credits

   .. automethod:: Billing.use_federated_billing_view

   .. automethod:: Billing.use_isolated_billing_view

   .. autoattribute:: Billing.credit_query

   .. automethod:: Billing.get_credits_by_query



Credit Search Methods
---------------------

   .. autoattribute:: Billing.credit_search

   .. autoattribute:: Billing.credit_search_order

   .. automethod:: Billing.get_credits_by_search

   .. automethod:: Billing.get_credit_query_from_inspector



Credit Admin Methods
--------------------

   .. autoattribute:: Billing.billing_id

   .. autoattribute:: Billing.billing

   .. automethod:: Billing.can_create_credits

   .. automethod:: Billing.can_create_credit_with_record_types

   .. automethod:: Billing.get_credit_form_for_create

   .. automethod:: Billing.create_credit

   .. automethod:: Billing.can_update_credits

   .. automethod:: Billing.get_credit_form_for_update

   .. automethod:: Billing.update_credit

   .. automethod:: Billing.can_delete_credits

   .. automethod:: Billing.delete_credit

   .. automethod:: Billing.can_manage_credit_aliases

   .. automethod:: Billing.alias_credit



Credit Notification Methods
---------------------------

   .. autoattribute:: Billing.billing_id

   .. autoattribute:: Billing.billing

   .. automethod:: Billing.can_register_for_credit_notifications

   .. automethod:: Billing.use_federated_billing_view

   .. automethod:: Billing.use_isolated_billing_view

   .. automethod:: Billing.reliable_credit_notifications

   .. automethod:: Billing.unreliable_credit_notifications

   .. automethod:: Billing.acknowledge_credit_notification

   .. automethod:: Billing.register_for_new_credits

   .. automethod:: Billing.register_for_new_credits_by_genus_type

   .. automethod:: Billing.register_for_new_credits_for_reference

   .. automethod:: Billing.register_for_new_credits_for_resource

   .. automethod:: Billing.register_for_changed_credits

   .. automethod:: Billing.register_for_changed_credits_by_genus_type

   .. automethod:: Billing.register_for_changed_credits_for_reference

   .. automethod:: Billing.register_for_changed_credits_for_resource

   .. automethod:: Billing.register_for_changed_credit

   .. automethod:: Billing.register_for_deleted_credits

   .. automethod:: Billing.register_for_deleted_credits_by_genus_type

   .. automethod:: Billing.register_for_deleted_credits_for_reference

   .. automethod:: Billing.register_for_deleted_credits_for_resource

   .. automethod:: Billing.register_for_deleted_credit



Credit Billing Methods
----------------------

   .. automethod:: Billing.can_lookup_credit_billing_mappings

   .. automethod:: Billing.use_comparative_billing_view

   .. automethod:: Billing.use_plenary_billing_view

   .. automethod:: Billing.get_credit_ids_by_billing

   .. automethod:: Billing.get_credits_by_billing

   .. automethod:: Billing.get_credit_ids_by_billings

   .. automethod:: Billing.get_credits_by_billings

   .. automethod:: Billing.get_billing_ids_by_credit

   .. automethod:: Billing.get_billings_by_credit



Credit Billing Assignment Methods
---------------------------------

   .. automethod:: Billing.can_assign_credits

   .. automethod:: Billing.can_assign_credits_to_billing

   .. automethod:: Billing.get_assignable_billing_ids

   .. automethod:: Billing.get_assignable_billing_ids_for_credit

   .. automethod:: Billing.assign_credit_to_billing

   .. automethod:: Billing.unassign_credit_from_billing

   .. automethod:: Billing.reassign_credit_to_billing



Credit Smart Billing Methods
----------------------------

   .. autoattribute:: Billing.billing_id

   .. autoattribute:: Billing.billing

   .. automethod:: Billing.can_manage_smart_billings

   .. autoattribute:: Billing.credit_query

   .. autoattribute:: Billing.credit_search_order

   .. automethod:: Billing.apply_credit_query

   .. automethod:: Billing.inspect_credit_query

   .. automethod:: Billing.apply_credit_sequencing

   .. automethod:: Billing.get_credit_query_from_inspector



