.. currentmodule:: dlkit.services.authorization


Vault
=====


Vault
-----

.. autoclass:: Vault
   :show-inheritance:

   .. automethod:: Vault.get_vault_record



Authorization Methods
---------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_access_authorizations

   .. automethod:: Vault.is_authorized

   .. automethod:: Vault.get_authorization_condition

   .. automethod:: Vault.is_authorized_on_condition



Authorization Lookup Methods
----------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_lookup_authorizations

   .. automethod:: Vault.use_comparative_authorization_view

   .. automethod:: Vault.use_plenary_authorization_view

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. automethod:: Vault.use_effective_authorization_view

   .. automethod:: Vault.use_any_effective_authorization_view

   .. automethod:: Vault.use_implicit_authorization_view

   .. automethod:: Vault.use_explicit_authorization_view

   .. automethod:: Vault.get_authorization

   .. automethod:: Vault.get_authorizations_by_ids

   .. automethod:: Vault.get_authorizations_by_genus_type

   .. automethod:: Vault.get_authorizations_by_parent_genus_type

   .. automethod:: Vault.get_authorizations_by_record_type

   .. automethod:: Vault.get_authorizations_on_date

   .. automethod:: Vault.get_authorizations_for_resource

   .. automethod:: Vault.get_authorizations_for_resource_on_date

   .. automethod:: Vault.get_authorizations_for_agent

   .. automethod:: Vault.get_authorizations_for_agent_on_date

   .. automethod:: Vault.get_authorizations_for_function

   .. automethod:: Vault.get_authorizations_for_function_on_date

   .. automethod:: Vault.get_authorizations_for_resource_and_function

   .. automethod:: Vault.get_authorizations_for_resource_and_function_on_date

   .. automethod:: Vault.get_authorizations_for_agent_and_function

   .. automethod:: Vault.get_authorizations_for_agent_and_function_on_date

   .. automethod:: Vault.get_authorizations_by_qualifier

   .. automethod:: Vault.get_explicit_authorization

   .. autoattribute:: Vault.authorizations



Authorization Query Methods
---------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_search_authorizations

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. automethod:: Vault.use_implicit_authorization_view

   .. automethod:: Vault.use_explicit_authorization_view

   .. autoattribute:: Vault.authorization_query

   .. automethod:: Vault.get_authorizations_by_query



Authorization Search Methods
----------------------------

   .. autoattribute:: Vault.authorization_search

   .. autoattribute:: Vault.authorization_search_order

   .. automethod:: Vault.get_authorizations_by_search

   .. automethod:: Vault.get_authorization_query_from_inspector



Authorization Admin Methods
---------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_create_authorizations

   .. automethod:: Vault.can_create_authorization_with_record_types

   .. automethod:: Vault.get_authorization_form_for_create_for_agent

   .. automethod:: Vault.get_authorization_form_for_create_for_resource

   .. automethod:: Vault.get_authorization_form_for_create_for_resource_and_trust

   .. automethod:: Vault.create_authorization

   .. automethod:: Vault.can_update_authorizations

   .. automethod:: Vault.get_authorization_form_for_update

   .. automethod:: Vault.update_authorization

   .. automethod:: Vault.can_delete_authorizations

   .. automethod:: Vault.delete_authorization

   .. automethod:: Vault.can_manage_authorization_aliases

   .. automethod:: Vault.alias_authorization



Authorization Notification Methods
----------------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_register_for_authorization_notifications

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. automethod:: Vault.use_implicit_authorization_view

   .. automethod:: Vault.use_explicit_authorization_view

   .. automethod:: Vault.register_for_new_authorizations

   .. automethod:: Vault.register_for_new_authorizations_for_resource

   .. automethod:: Vault.register_for_new_authorizations_for_function

   .. automethod:: Vault.register_for_changed_authorizations

   .. automethod:: Vault.register_for_changed_authorizations_for_resource

   .. automethod:: Vault.register_for_changed_authorizations_for_function

   .. automethod:: Vault.register_for_changed_authorization

   .. automethod:: Vault.register_for_deleted_authorizations

   .. automethod:: Vault.register_for_deleted_authorizations_for_resource

   .. automethod:: Vault.register_for_deleted_authorizations_for_function

   .. automethod:: Vault.register_for_deleted_authorization



Authorization Vault Methods
---------------------------

   .. automethod:: Vault.use_comparative_vault_view

   .. automethod:: Vault.use_plenary_vault_view

   .. automethod:: Vault.can_lookup_authorization_vault_mappings

   .. automethod:: Vault.get_authorization_ids_by_vault

   .. automethod:: Vault.get_authorizations_by_vault

   .. automethod:: Vault.get_authorizations_ids_by_vault

   .. automethod:: Vault.get_vault_ids_by_authorization

   .. automethod:: Vault.get_vault_by_authorization



Authorization Vault Assignment Methods
--------------------------------------

   .. automethod:: Vault.can_assign_authorizations

   .. automethod:: Vault.can_assign_authorizations_to_vault

   .. automethod:: Vault.get_assignable_vault_ids

   .. automethod:: Vault.get_assignable_vault_ids_for_authorization

   .. automethod:: Vault.assign_authorization_to_vault

   .. automethod:: Vault.unassign_authorization_from_vault



Authorization Smart Vault Methods
---------------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_manage_smart_vault

   .. autoattribute:: Vault.authorization_query

   .. autoattribute:: Vault.authorization_search_order

   .. automethod:: Vault.apply_authorization_query

   .. automethod:: Vault.inspect_authorization_query

   .. automethod:: Vault.apply_authorization_sequencing

   .. automethod:: Vault.get_authorization_query_from_inspector



Function Lookup Methods
-----------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_lookup_functions

   .. automethod:: Vault.use_comparative_function_view

   .. automethod:: Vault.use_plenary_function_view

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. automethod:: Vault.use_active_function_view

   .. automethod:: Vault.use_any_status_function_view

   .. automethod:: Vault.get_function

   .. automethod:: Vault.get_functions_by_ids

   .. automethod:: Vault.get_functions_by_genus_type

   .. automethod:: Vault.get_functions_by_parent_genus_type

   .. automethod:: Vault.get_functions_by_record_type

   .. autoattribute:: Vault.functions



Function Query Methods
----------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_search_functions

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. autoattribute:: Vault.function_query

   .. automethod:: Vault.get_functions_by_query



Function Search Methods
-----------------------

   .. autoattribute:: Vault.function_search

   .. autoattribute:: Vault.function_search_order

   .. automethod:: Vault.get_functions_by_search

   .. automethod:: Vault.get_function_query_from_inspector



Function Admin Methods
----------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_create_functions

   .. automethod:: Vault.can_create_function_with_record_types

   .. automethod:: Vault.get_function_form_for_create

   .. automethod:: Vault.create_function

   .. automethod:: Vault.can_update_functions

   .. automethod:: Vault.get_function_form_for_update

   .. automethod:: Vault.update_function

   .. automethod:: Vault.can_delete_functions

   .. automethod:: Vault.delete_function

   .. automethod:: Vault.can_manage_function_aliases

   .. automethod:: Vault.alias_function



Function Notification Methods
-----------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_register_for_function_notifications

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. automethod:: Vault.register_for_new_functions

   .. automethod:: Vault.register_for_changed_functions

   .. automethod:: Vault.register_for_changed_function

   .. automethod:: Vault.register_for_deleted_functions

   .. automethod:: Vault.register_for_deleted_function



Function Vault Methods
----------------------

   .. automethod:: Vault.can_lookup_function_vault_mappings

   .. automethod:: Vault.use_comparative_vault_view

   .. automethod:: Vault.use_plenary_vault_view

   .. automethod:: Vault.get_function_ids_by_vault

   .. automethod:: Vault.get_functions_by_vault

   .. automethod:: Vault.get_function_ids_by_vaults

   .. automethod:: Vault.get_functions_by_vaults

   .. automethod:: Vault.get_vault_ids_by_function

   .. automethod:: Vault.get_vaults_by_function



Function Vault Assignment Methods
---------------------------------

   .. automethod:: Vault.can_assign_functions

   .. automethod:: Vault.can_assign_functions_to_vault

   .. automethod:: Vault.get_assignable_vault_ids

   .. automethod:: Vault.get_assignable_vault_ids_for_function

   .. automethod:: Vault.assign_function_to_vault

   .. automethod:: Vault.unassign_function_from_vault



Function Smart Vault Methods
----------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_manage_smart_vaults

   .. autoattribute:: Vault.function_query

   .. autoattribute:: Vault.function_search_order

   .. automethod:: Vault.apply_function_query

   .. automethod:: Vault.inspect_function_query

   .. automethod:: Vault.apply_function_sequencing

   .. automethod:: Vault.get_function_query_from_inspector



Qualifier Lookup Methods
------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_lookup_qualifiers

   .. automethod:: Vault.use_comparative_qualifier_view

   .. automethod:: Vault.use_plenary_qualifier_view

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. automethod:: Vault.get_qualifier

   .. automethod:: Vault.get_qualifiers_by_ids

   .. automethod:: Vault.get_qualifiers_by_genus_type

   .. automethod:: Vault.get_qualifiers_by_parent_genus_type

   .. automethod:: Vault.get_qualifiers_by_record_type

   .. autoattribute:: Vault.qualifiers



Qualifier Query Methods
-----------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_search_qualifiers

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. autoattribute:: Vault.qualifier_query

   .. automethod:: Vault.get_qualifiers_by_query



Qualifier Search Methods
------------------------

   .. autoattribute:: Vault.qualifier_search

   .. autoattribute:: Vault.qualifier_search_order

   .. automethod:: Vault.get_qualifiers_by_search

   .. automethod:: Vault.get_qualifier_query_from_inspector



Qualifier Admin Methods
-----------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_create_qualifiers

   .. automethod:: Vault.can_create_qualifier_with_record_types

   .. automethod:: Vault.get_qualifier_form_for_create

   .. automethod:: Vault.create_qualifier

   .. automethod:: Vault.can_update_qualifiers

   .. automethod:: Vault.get_qualifier_form_for_update

   .. automethod:: Vault.update_qualifier

   .. automethod:: Vault.can_delete_qualifiers

   .. automethod:: Vault.delete_qualifier

   .. automethod:: Vault.can_manage_qualifier_aliases

   .. automethod:: Vault.alias_qualifier



Qualifier Notification Methods
------------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_register_for_qualifier_notifications

   .. automethod:: Vault.use_federated_vault_view

   .. automethod:: Vault.use_isolated_vault_view

   .. automethod:: Vault.register_for_new_qualifiers

   .. automethod:: Vault.register_for_new_qualifier_ancestors

   .. automethod:: Vault.register_for_new_qualifier_descendants

   .. automethod:: Vault.register_for_changed_qualifiers

   .. automethod:: Vault.register_for_changed_qualifier

   .. automethod:: Vault.register_for_deleted_qualifiers

   .. automethod:: Vault.register_for_deleted_qualifier

   .. automethod:: Vault.register_for_deleted_qualifier_ancestors

   .. automethod:: Vault.register_for_deleted_qualifier_descendants



Qualifier Hierarchy Methods
---------------------------

   .. autoattribute:: Vault.qualifier_hierarchy_id

   .. autoattribute:: Vault.qualifier_hierarchy

   .. automethod:: Vault.can_access_qualifier_hierarchy

   .. automethod:: Vault.use_comparative_qualifier_view

   .. automethod:: Vault.use_plenary_qualifier_view

   .. autoattribute:: Vault.root_qualifier_ids

   .. autoattribute:: Vault.root_qualifiers

   .. automethod:: Vault.has_parent_qualifiers

   .. automethod:: Vault.is_parent_of_qualifier

   .. automethod:: Vault.get_parent_qualifier_ids

   .. automethod:: Vault.get_parent_qualifiers

   .. automethod:: Vault.is_ancestor_of_qualifier

   .. automethod:: Vault.has_child_qualifiers

   .. automethod:: Vault.is_child_of_qualifier

   .. automethod:: Vault.get_child_qualifier_ids

   .. automethod:: Vault.get_child_qualifiers

   .. automethod:: Vault.is_descendant_of_qualifier

   .. automethod:: Vault.get_qualifier_node_ids

   .. automethod:: Vault.get_qualifier_nodes



Qualifier Hierarchy Design Methods
----------------------------------

   .. autoattribute:: Vault.qualifier_hierarchy_id

   .. autoattribute:: Vault.qualifier_hierarchy

   .. automethod:: Vault.can_modify_qualifier_hierarchy

   .. automethod:: Vault.add_root_qualifier

   .. automethod:: Vault.remove_root_qualifier

   .. automethod:: Vault.add_child_qualifier

   .. automethod:: Vault.remove_child_qualifier

   .. automethod:: Vault.remove_child_qualifiers



Qualifier Vault Methods
-----------------------

   .. automethod:: Vault.can_lookup_qualifier_vault_mappings

   .. automethod:: Vault.use_comparative_vault_view

   .. automethod:: Vault.use_plenary_vault_view

   .. automethod:: Vault.get_qualifier_ids_by_vault

   .. automethod:: Vault.get_qualifiers_by_vault

   .. automethod:: Vault.get_qualifier_ids_by_vaults

   .. automethod:: Vault.get_qualifiers_by_vaults

   .. automethod:: Vault.get_vault_ids_by_qualifier

   .. automethod:: Vault.get_vaults_by_qualifier



Qualifier Vault Assignment Methods
----------------------------------

   .. automethod:: Vault.can_assign_qualifiers

   .. automethod:: Vault.can_assign_qualifiers_to_vault

   .. automethod:: Vault.get_assignable_vault_ids

   .. automethod:: Vault.get_assignable_vault_ids_for_qualifier

   .. automethod:: Vault.assign_qualifier_to_vault

   .. automethod:: Vault.unassign_qualifier_from_vault



Qualifier Smart Vault Methods
-----------------------------

   .. autoattribute:: Vault.vault_id

   .. autoattribute:: Vault.vault

   .. automethod:: Vault.can_manage_smart_vaults

   .. autoattribute:: Vault.qualifier_query

   .. autoattribute:: Vault.qualifier_search_order

   .. automethod:: Vault.apply_qualifier_query

   .. automethod:: Vault.inspect_qualifier_query

   .. automethod:: Vault.apply_qualifier_sequencing

   .. automethod:: Vault.get_qualifier_query_from_inspector



