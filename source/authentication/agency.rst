.. currentmodule:: dlkit_doc.authentication
.. automodule:: dlkit_doc.authentication

Agency
======


Agency
------

.. autoclass:: Agency
   :show-inheritance:

.. automethod:: Agency.get_agency_record



Agent Lookup Methods
--------------------

.. autoattribute:: Agency.agency_id

.. autoattribute:: Agency.agency

.. automethod:: Agency.can_lookup_agents

.. automethod:: Agency.use_comparative_agent_view

.. automethod:: Agency.use_plenary_agent_view

.. automethod:: Agency.use_federated_agency_view

.. automethod:: Agency.use_isolated_agency_view

.. automethod:: Agency.get_agent

.. automethod:: Agency.get_agents_by_ids

.. automethod:: Agency.get_agents_by_genus_type

.. automethod:: Agency.get_agents_by_parent_genus_type

.. automethod:: Agency.get_agents_by_record_type

.. autoattribute:: Agency.agents



Agent Query Methods
-------------------

.. autoattribute:: Agency.agency_id

.. autoattribute:: Agency.agency

.. automethod:: Agency.can_search_agents

.. automethod:: Agency.use_federated_agency_view

.. automethod:: Agency.use_isolated_agency_view

.. autoattribute:: Agency.agent_query

.. automethod:: Agency.get_agents_by_query



Agent Search Methods
--------------------

.. autoattribute:: Agency.agent_search

.. autoattribute:: Agency.agent_search_order

.. automethod:: Agency.get_agents_by_search

.. automethod:: Agency.get_agent_query_from_inspector



Agent Admin Methods
-------------------

.. autoattribute:: Agency.agency_id

.. autoattribute:: Agency.agency

.. automethod:: Agency.can_create_agents

.. automethod:: Agency.can_create_agent_with_record_types

.. automethod:: Agency.get_agent_form_for_create

.. automethod:: Agency.create_agent

.. automethod:: Agency.can_update_agents

.. automethod:: Agency.can_update_agent

.. automethod:: Agency.get_agent_form_for_update

.. automethod:: Agency.update_agent

.. automethod:: Agency.can_delete_agents

.. automethod:: Agency.can_delete_agent

.. automethod:: Agency.delete_agent

.. automethod:: Agency.can_manage_agent_aliases

.. automethod:: Agency.alias_agent



Agent Notification Methods
--------------------------

.. autoattribute:: Agency.agency_id

.. autoattribute:: Agency.agency

.. automethod:: Agency.can_register_for_agent_notifications

.. automethod:: Agency.use_federated_agency_view

.. automethod:: Agency.use_isolated_agency_view

.. automethod:: Agency.register_for_new_agents

.. automethod:: Agency.register_for_changed_agents

.. automethod:: Agency.register_for_changed_agent

.. automethod:: Agency.register_for_deleted_agents

.. automethod:: Agency.register_for_deleted_agent



Agent Agency Methods
--------------------

.. automethod:: Agency.can_lookup_agent_agency_mappings

.. automethod:: Agency.use_comparative_agency_view

.. automethod:: Agency.use_plenary_agency_view

.. automethod:: Agency.get_agent_ids_by_agency

.. automethod:: Agency.get_agents_by_agency

.. automethod:: Agency.get_agent_ids_by_agencies

.. automethod:: Agency.get_agents_by_agencies

.. automethod:: Agency.get_agency_ids_by_agent

.. automethod:: Agency.get_agencies_by_agent



Agent Agency Assignment Methods
-------------------------------

.. automethod:: Agency.can_assign_agents

.. automethod:: Agency.can_assign_agents_to_agency

.. automethod:: Agency.get_assignable_agency_ids

.. automethod:: Agency.get_assignable_agency_ids_for_agent

.. automethod:: Agency.assign_agent_to_agency

.. automethod:: Agency.unassign_agent_from_agency



Agent Smart Agency Methods
--------------------------

.. autoattribute:: Agency.agency_id

.. autoattribute:: Agency.agency

.. automethod:: Agency.can_manage_smart_agencies

.. autoattribute:: Agency.agent_query

.. autoattribute:: Agency.agent_search_order

.. automethod:: Agency.apply_agent_query

.. automethod:: Agency.inspect_agent_query

.. automethod:: Agency.apply_agent_sequencing

.. automethod:: Agency.get_agent_query_from_inspector



