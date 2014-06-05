.. currentmodule:: dlkit.services.rules


Engine
======


Engine
------

.. autoclass:: Engine
   :show-inheritance:

   .. automethod:: Engine.get_engine_record



Rules Methods
-------------

   .. autoattribute:: Engine.engine_id

   .. autoattribute:: Engine.engine

   .. automethod:: Engine.can_evaluate_rules

   .. automethod:: Engine.get_condition_for_rule

   .. automethod:: Engine.evaluate_rule

   .. automethod:: Engine.execute_rule



Rule Lookup Methods
-------------------

   .. autoattribute:: Engine.engine_id

   .. autoattribute:: Engine.engine

   .. automethod:: Engine.can_lookup_rules

   .. automethod:: Engine.use_comparative_rule_view

   .. automethod:: Engine.use_plenary_rule_view

   .. automethod:: Engine.use_federated_engine_view

   .. automethod:: Engine.use_isolated_engine_view

   .. automethod:: Engine.use_active_rule_view

   .. automethod:: Engine.use_any_status_rule_view

   .. automethod:: Engine.get_rule

   .. automethod:: Engine.get_rules_by_ids

   .. automethod:: Engine.get_rules_by_genus_type

   .. automethod:: Engine.get_rules_by_parent_genus_type

   .. automethod:: Engine.get_rules_by_record_type

   .. autoattribute:: Engine.rules



Rule Query Methods
------------------

   .. autoattribute:: Engine.engine_id

   .. autoattribute:: Engine.engine

   .. automethod:: Engine.use_federated_engine_view

   .. automethod:: Engine.use_isolated_engine_view

   .. automethod:: Engine.can_search_rules

   .. autoattribute:: Engine.rule_query

   .. automethod:: Engine.get_rules_by_query



Rule Search Methods
-------------------

   .. autoattribute:: Engine.rule_search

   .. autoattribute:: Engine.rule_search_order

   .. automethod:: Engine.get_rules_by_search

   .. automethod:: Engine.get_rule_query_from_inspector



Rule Admin Methods
------------------

   .. autoattribute:: Engine.engine_id

   .. autoattribute:: Engine.engine

   .. automethod:: Engine.can_create_rules

   .. automethod:: Engine.can_create_rule_with_record_types

   .. automethod:: Engine.get_rule_form_for_create

   .. automethod:: Engine.create_rule

   .. automethod:: Engine.can_update_rules

   .. automethod:: Engine.get_rule_form_for_update

   .. automethod:: Engine.update_rule

   .. automethod:: Engine.can_delete_rules

   .. automethod:: Engine.delete_rule

   .. automethod:: Engine.can_manage_rule_aliases

   .. automethod:: Engine.alias_rule



Rule Notification Methods
-------------------------

   .. autoattribute:: Engine.engine_id

   .. autoattribute:: Engine.engine

   .. automethod:: Engine.can_register_for_rule_notifications

   .. automethod:: Engine.use_federated_engine_view

   .. automethod:: Engine.use_isolated_engine_view

   .. automethod:: Engine.register_for_new_rules

   .. automethod:: Engine.register_for_changed_rules

   .. automethod:: Engine.register_for_changed_rule

   .. automethod:: Engine.register_for_deleted_rules

   .. automethod:: Engine.register_for_deleted_rule



Rule Engine Methods
-------------------

   .. automethod:: Engine.can_lookup_rule_engine_mappings

   .. automethod:: Engine.use_comparative_rule_view

   .. automethod:: Engine.use_plenary_rule_view

   .. automethod:: Engine.get_rule_ids_by_engine

   .. automethod:: Engine.get_rules_by_engine

   .. automethod:: Engine.get_rule_ids_by_engines

   .. automethod:: Engine.get_rules_by_engines

   .. automethod:: Engine.get_engine_ids_by_rule

   .. automethod:: Engine.get_engines_by_rule



Rule Engine Assignment Methods
------------------------------

   .. automethod:: Engine.can_assign_rules

   .. automethod:: Engine.can_assign_rules_to_engine

   .. automethod:: Engine.get_assignable_engine_ids

   .. automethod:: Engine.get_assignable_engine_ids_for_rule

   .. automethod:: Engine.assign_rule_to_engine

   .. automethod:: Engine.unassign_rule_from_engine



Rule Smart Engine Methods
-------------------------

   .. autoattribute:: Engine.engine_id

   .. autoattribute:: Engine.engine

   .. automethod:: Engine.can_manage_smart_engines

   .. autoattribute:: Engine.rule_query

   .. autoattribute:: Engine.rule_search_order

   .. automethod:: Engine.apply_rule_query

   .. automethod:: Engine.inspect_rule_query

   .. automethod:: Engine.apply_rule_sequencing

   .. automethod:: Engine.get_rule_query_from_inspector



