.. currentmodule:: dlkit.services.configuration


Configuration
=============


Configuration
-------------

.. autoclass:: Configuration
   :show-inheritance:

   .. automethod:: Configuration.is_registry

   .. automethod:: Configuration.get_configuration_record



Value Retrieval Methods
-----------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.can_lookup_values

   .. automethod:: Configuration.use_comparative_value_view

   .. automethod:: Configuration.use_plenary_value_view

   .. automethod:: Configuration.use_federated_configuration_view

   .. automethod:: Configuration.use_isolated_configuration_view

   .. automethod:: Configuration.use_conditional_view

   .. automethod:: Configuration.use_unconditional_view

   .. automethod:: Configuration.get_value_by_parameter

   .. automethod:: Configuration.get_values_by_parameter

   .. automethod:: Configuration.get_values_by_parameters

   .. automethod:: Configuration.get_value_condition

   .. automethod:: Configuration.get_value_by_parameter_on_condition

   .. automethod:: Configuration.get_values_by_parameter_on_condition

   .. automethod:: Configuration.get_values_by_parameters_on_condition



Value Lookup Methods
--------------------

   .. automethod:: Configuration.use_active_value_view

   .. automethod:: Configuration.use_any_status_value_view

   .. automethod:: Configuration.get_value

   .. automethod:: Configuration.get_values_by_ids

   .. automethod:: Configuration.get_values_by_genus_type

   .. automethod:: Configuration.get_values_by_parent_genus_type

   .. automethod:: Configuration.get_values_by_record_type

   .. autoattribute:: Configuration.values

   .. automethod:: Configuration.get_values_on_condition



Value Query Methods
-------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.can_search_values

   .. automethod:: Configuration.use_federated_configuration_view

   .. automethod:: Configuration.use_isolated_configuration_view

   .. autoattribute:: Configuration.value_query

   .. automethod:: Configuration.get_values_by_query



Value Search Methods
--------------------

   .. autoattribute:: Configuration.value_search

   .. autoattribute:: Configuration.value_search_order

   .. automethod:: Configuration.get_values_by_search

   .. automethod:: Configuration.get_value_query_from_inspector



Value Admin Methods
-------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.support_value_conditions

   .. automethod:: Configuration.can_create_values

   .. automethod:: Configuration.can_create_value_with_record_types

   .. automethod:: Configuration.get_value_form_for_create

   .. automethod:: Configuration.create_value

   .. automethod:: Configuration.can_update_values

   .. automethod:: Configuration.get_value_form_for_update

   .. automethod:: Configuration.update_value

   .. automethod:: Configuration.can_delete_values

   .. automethod:: Configuration.delete_value

   .. automethod:: Configuration.can_manage_value_aliases

   .. automethod:: Configuration.alias_value



Value Notification Methods
--------------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.can_register_for_value_notifications

   .. automethod:: Configuration.use_federated_configuration_view

   .. automethod:: Configuration.use_isolated_configuration_view

   .. automethod:: Configuration.register_for_new_values

   .. automethod:: Configuration.register_for_new_values_for_parameter

   .. automethod:: Configuration.register_for_changed_values

   .. automethod:: Configuration.register_for_changed_values_for_parameter

   .. automethod:: Configuration.register_for_changed_value

   .. automethod:: Configuration.register_for_deleted_values

   .. automethod:: Configuration.register_for_deleted_values_for_parameter

   .. automethod:: Configuration.register_for_deleted_value



Parameter Lookup Methods
------------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.can_lookup_parameters

   .. automethod:: Configuration.use_comparative_parameter_view

   .. automethod:: Configuration.use_plenary_parameter_view

   .. automethod:: Configuration.use_federated_configuration_view

   .. automethod:: Configuration.use_isolated_configuration_view

   .. automethod:: Configuration.use_active_parameter_view

   .. automethod:: Configuration.use_any_status_parameter_view

   .. automethod:: Configuration.get_parameter

   .. automethod:: Configuration.get_parameters_by_ids

   .. automethod:: Configuration.get_parameters_by_genus_type

   .. automethod:: Configuration.get_parameters_by_parent_genus_type

   .. automethod:: Configuration.get_parameters_by_record_type

   .. autoattribute:: Configuration.parameters



Parameter Query Methods
-----------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.can_search_parameters

   .. automethod:: Configuration.use_federated_configuration_view

   .. automethod:: Configuration.use_isolated_configuration_view

   .. autoattribute:: Configuration.parameter_query

   .. automethod:: Configuration.get_parameters_by_query



Parameter Search Methods
------------------------

   .. autoattribute:: Configuration.parameter_search

   .. autoattribute:: Configuration.parameter_search_order

   .. automethod:: Configuration.get_parameters_by_search

   .. automethod:: Configuration.get_parameter_query_from_inspector



Parameter Admin Methods
-----------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.can_create_parameters

   .. automethod:: Configuration.can_create_parameter_with_record_types

   .. automethod:: Configuration.get_parameter_form_for_create

   .. automethod:: Configuration.create_parameter

   .. automethod:: Configuration.can_update_parameters

   .. automethod:: Configuration.get_parameter_form_for_update

   .. automethod:: Configuration.update_parameter

   .. automethod:: Configuration.can_delete_parameters

   .. automethod:: Configuration.delete_parameter

   .. automethod:: Configuration.can_manage_parameter_aliases

   .. automethod:: Configuration.alias_parameter



Parameter Notification Methods
------------------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.can_register_for_parameter_notifications

   .. automethod:: Configuration.use_federated_configuration_view

   .. automethod:: Configuration.use_isolated_configuration_view

   .. automethod:: Configuration.register_for_new_parameters

   .. automethod:: Configuration.register_for_changed_parameters

   .. automethod:: Configuration.register_for_changed_parameter

   .. automethod:: Configuration.register_for_deleted_parameters

   .. automethod:: Configuration.register_for_deleted_parameter



Parameter Configuration Methods
-------------------------------

   .. automethod:: Configuration.can_lookup_parameter_configurations

   .. automethod:: Configuration.use_comparative_parameter_view

   .. automethod:: Configuration.use_plenary_parameter_view

   .. automethod:: Configuration.get_parameter_ids_by_configuration

   .. automethod:: Configuration.get_parameters_by_configuration

   .. automethod:: Configuration.get_parameter_ids_by_configurations

   .. automethod:: Configuration.get_parameters_by_configurations

   .. automethod:: Configuration.get_configuration_ids_by_parameter

   .. automethod:: Configuration.get_configurations_by_parameter



Parameter Configuration Assignment Methods
------------------------------------------

   .. automethod:: Configuration.can_assign_parameter_configurations

   .. automethod:: Configuration.can_assign_parameters_to_configuration

   .. automethod:: Configuration.get_assignable_configuration_ids

   .. automethod:: Configuration.get_assignable_configuration_ids_for_parameter

   .. automethod:: Configuration.assign_parameter_to_configuration

   .. automethod:: Configuration.unassign_parameter_from_configuration



Parameter Smart Configuration Methods
-------------------------------------

   .. autoattribute:: Configuration.configuration_id

   .. autoattribute:: Configuration.configuration

   .. automethod:: Configuration.can_manage_smart_configurations

   .. autoattribute:: Configuration.parameter_query

   .. autoattribute:: Configuration.parameter_search_order

   .. automethod:: Configuration.apply_parameter_query

   .. automethod:: Configuration.inspec_parameter_query

   .. automethod:: Configuration.apply_parameter_sequencing

   .. automethod:: Configuration.get_parameter_query_from_inspector



