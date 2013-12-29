.. currentmodule:: dlkit_doc.workflow
.. automodule:: dlkit_doc.workflow

Office
======


Office
------

.. autoclass:: Office
   :show-inheritance:

.. automethod:: Office.get_office_record



Process Lookup Methods
----------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_lookup_processes

.. automethod:: Office.use_comparative_process_view

.. automethod:: Office.use_plenary_process_view

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. automethod:: Office.use_active_process_view

.. automethod:: Office.use_any_status_process_view

.. automethod:: Office.get_process

.. automethod:: Office.get_processes_by_ids

.. automethod:: Office.get_processes_by_genus_type

.. automethod:: Office.get_processes_by_parent_genus_type

.. automethod:: Office.get_processes_by_record_type

.. automethod:: Office.get_processes_by_provider

.. autoattribute:: Office.processes



Process Query Methods
---------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_search_processes

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. autoattribute:: Office.process_query

.. automethod:: Office.get_processes_by_query



Process Search Methods
----------------------

.. autoattribute:: Office.process_search

.. autoattribute:: Office.process_search_order

.. automethod:: Office.get_processes_by_search

.. automethod:: Office.get_process_query_from_inspector



Process Admin Methods
---------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_create_processes

.. automethod:: Office.can_create_process_with_record_types

.. automethod:: Office.get_process_form_for_create

.. automethod:: Office.create_process

.. automethod:: Office.can_update_processes

.. automethod:: Office.get_process_form_for_update

.. automethod:: Office.update_process

.. automethod:: Office.can_delete_processes

.. automethod:: Office.delete_process

.. automethod:: Office.can_manage_process_aliases

.. automethod:: Office.alias_process

.. automethod:: Office.can_assign_competencies

.. automethod:: Office.add_competency

.. automethod:: Office.remove_competency

.. automethod:: Office.remove_competencies



Process Notification Methods
----------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_register_for_process_notifications

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. automethod:: Office.register_for_new_processes

.. automethod:: Office.register_for_changed_processes

.. automethod:: Office.register_for_changed_process

.. automethod:: Office.register_for_deleted_processes

.. automethod:: Office.register_for_deleted_process



Process Office Methods
----------------------

.. automethod:: Office.can_lookup_process_office_mappings

.. automethod:: Office.use_comparative_process_office_view

.. automethod:: Office.use_plenary_process_office_view

.. automethod:: Office.get_process_ids_by_office

.. automethod:: Office.get_processes_by_office

.. automethod:: Office.get_process_ids_by_offices

.. automethod:: Office.get_processes_by_offices

.. automethod:: Office.get_office_ids_by_process

.. automethod:: Office.get_offices_by_process



Process Office Assignment Methods
---------------------------------

.. automethod:: Office.can_assign_processes

.. automethod:: Office.can_assign_processes_to_office

.. automethod:: Office.get_assignable_office_ids

.. automethod:: Office.get_assignable_office_ids_for_process

.. automethod:: Office.assign_process_to_office

.. automethod:: Office.unassign_process_from_office



Process Smart Office Methods
----------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_manage_smart_offices

.. autoattribute:: Office.process_query

.. autoattribute:: Office.process_search_order

.. automethod:: Office.apply_process_query

.. automethod:: Office.inspect_process_query

.. automethod:: Office.apply_process_sequencing

.. automethod:: Office.get_process_query_from_inspector



Step Lookup Methods
-------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_lookup_steps

.. automethod:: Office.use_comparative_step_view

.. automethod:: Office.use_plenary_step_view

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. automethod:: Office.use_active_step_view

.. automethod:: Office.use_any_status_step_view

.. automethod:: Office.get_step

.. automethod:: Office.get_steps_by_ids

.. automethod:: Office.get_steps_by_genus_type

.. automethod:: Office.get_steps_by_parent_genus_type

.. automethod:: Office.get_steps_by_record_type

.. automethod:: Office.get_steps_by_provider

.. automethod:: Office.get_steps_for_process

.. automethod:: Office.get_steps_by_state

.. autoattribute:: Office.steps



Step Query Methods
------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_search_steps

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. autoattribute:: Office.step_query

.. automethod:: Office.get_steps_by_query



Step Search Methods
-------------------

.. autoattribute:: Office.step_search

.. autoattribute:: Office.step_search_order

.. automethod:: Office.get_steps_by_search

.. automethod:: Office.get_step_query_from_inspector



Step Admin Methods
------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_create_steps

.. automethod:: Office.can_create_step_with_record_types

.. automethod:: Office.get_step_form_for_create

.. automethod:: Office.create_step

.. automethod:: Office.can_update_steps

.. automethod:: Office.get_step_form_for_update

.. automethod:: Office.update_step

.. automethod:: Office.can_delete_steps

.. automethod:: Office.delete_step

.. automethod:: Office.can_manage_step_aliases

.. automethod:: Office.alias_step



Step Notification Methods
-------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_register_for_step_notifications

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. automethod:: Office.register_for_new_steps

.. automethod:: Office.register_for_new_steps_for_process

.. automethod:: Office.register_for_changed_steps

.. automethod:: Office.register_for_changed_steps_for_process

.. automethod:: Office.register_for_changed_step

.. automethod:: Office.register_for_deleted_steps

.. automethod:: Office.register_for_deleted_steps_for_process

.. automethod:: Office.register_for_deleted_step



Step Office Methods
-------------------

.. automethod:: Office.can_lookup_step_office_mappings

.. automethod:: Office.use_comparative_step_office_view

.. automethod:: Office.use_plenary_step_office_view

.. automethod:: Office.get_step_ids_by_office

.. automethod:: Office.get_stepes_by_office

.. automethod:: Office.get_step_ids_by_offices

.. automethod:: Office.get_steps_by_offices

.. automethod:: Office.get_office_ids_by_step

.. automethod:: Office.get_offices_by_step



Step Office Assignment Methods
------------------------------

.. automethod:: Office.can_assign_stepes

.. automethod:: Office.can_assign_stepes_to_office

.. automethod:: Office.get_assignable_office_ids

.. automethod:: Office.get_assignable_office_ids_for_step

.. automethod:: Office.assign_step_to_office

.. automethod:: Office.unassign_step_from_office



Step Smart Office Methods
-------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_manage_smart_offices

.. autoattribute:: Office.step_query

.. autoattribute:: Office.step_search_order

.. automethod:: Office.apply_step_query

.. automethod:: Office.inspect_step_query

.. automethod:: Office.apply_step_sequencing

.. automethod:: Office.get_step_query_from_inspector



Work Lookup Methods
-------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_lookup_works

.. automethod:: Office.use_comparative_work_view

.. automethod:: Office.use_plenary_work_view

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. automethod:: Office.get_work

.. automethod:: Office.get_works_by_ids

.. automethod:: Office.get_works_by_genus_type

.. automethod:: Office.get_works_by_parent_genus_type

.. automethod:: Office.get_works_by_record_type

.. autoattribute:: Office.works



Work Query Methods
------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_search_works

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. autoattribute:: Office.work_query

.. automethod:: Office.get_works_by_query



Work Search Methods
-------------------

.. autoattribute:: Office.work_search

.. autoattribute:: Office.work_search_order

.. automethod:: Office.get_works_by_search

.. automethod:: Office.get_work_query_from_inspector



Work Admin Methods
------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_create_works

.. automethod:: Office.can_create_work_with_record_types

.. automethod:: Office.get_work_form_for_create

.. automethod:: Office.create_work

.. automethod:: Office.can_update_works

.. automethod:: Office.get_work_form_for_update

.. automethod:: Office.update_work

.. automethod:: Office.can_delete_works

.. automethod:: Office.delete_work

.. automethod:: Office.can_manage_work_aliases

.. automethod:: Office.alias_work

.. automethod:: Office.can_move_work

.. automethod:: Office.move_work

.. automethod:: Office.can_manage_work_status

.. automethod:: Office.complete_work

.. automethod:: Office.reopen_work



Work Notification Methods
-------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_register_for_work_notifications

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. automethod:: Office.register_for_new_works

.. automethod:: Office.register_for_changed_works

.. automethod:: Office.register_for_changed_work

.. automethod:: Office.register_for_deleted_works

.. automethod:: Office.register_for_deleted_work



Work Office Methods
-------------------

.. automethod:: Office.can_lookup_work_office_availabilities

.. automethod:: Office.use_comparative_work_office_view

.. automethod:: Office.use_plenary_work_office_view

.. automethod:: Office.get_work_ids_by_office

.. automethod:: Office.get_works_by_office

.. automethod:: Office.get_work_ids_by_offices

.. automethod:: Office.get_works_by_offices

.. automethod:: Office.get_office_ids_by_work

.. automethod:: Office.get_offices_by_work



Work Office Assignment Methods
------------------------------

.. automethod:: Office.can_assign_works

.. automethod:: Office.can_assign_works_to_office

.. automethod:: Office.get_assignable_office_ids

.. automethod:: Office.get_assignable_office_ids_for_work

.. automethod:: Office.assign_work_to_office

.. automethod:: Office.unassign_work_from_office



Work Smart Office Methods
-------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_manage_smart_offices

.. autoattribute:: Office.work_query

.. autoattribute:: Office.work_search_order

.. automethod:: Office.apply_work_query

.. automethod:: Office.inspect_work_query

.. automethod:: Office.apply_work_sequencing

.. automethod:: Office.get_work_query_from_inspector



Workflow Methods
----------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_access_workflow

.. automethod:: Office.can_access_workflow_for_process

.. automethod:: Office.get_processes_for_work

.. automethod:: Office.get_step_for_work

.. automethod:: Office.get_work_at_step

.. automethod:: Office.get_suspended_work

.. automethod:: Office.get_suspended_work_at_step

.. automethod:: Office.get_canceled_work

.. automethod:: Office.get_canceled_work_by_date

.. automethod:: Office.get_statuses_for_work

.. automethod:: Office.get_status_for_work

.. automethod:: Office.get_statuses_for_works



Workflow Initiation Methods
---------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_initiate_workflow

.. automethod:: Office.can_initiate_workflow_for_process

.. automethod:: Office.get_available_work

.. automethod:: Office.start_workflow



Workflow Management Methods
---------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_manage_workflow

.. automethod:: Office.can_manage_workflow_for_process

.. automethod:: Office.suspend_work

.. automethod:: Office.resume_work

.. automethod:: Office.cancel_work



Manual Workflow Methods
-----------------------

.. automethod:: Office.can_operate_workflow

.. automethod:: Office.can_operate_workflow_for_process

.. automethod:: Office.advance_work

.. automethod:: Office.get_valid_next_steps_for_work

.. automethod:: Office.get_all_valid_steps_for_work

.. automethod:: Office.assign_work_to_step



Workflow Event Lookup Methods
-----------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_lookup_workflow_events

.. automethod:: Office.use_comparative_workflow_event_view

.. automethod:: Office.use_plenary_workflow_event_view

.. automethod:: Office.use_federated_office_view

.. automethod:: Office.use_isolated_office_view

.. automethod:: Office.get_workflow_event

.. automethod:: Office.get_workflow_events_by_ids

.. automethod:: Office.get_workflow_events_by_genus_type

.. automethod:: Office.get_workflow_events_by_parent_genus_type

.. automethod:: Office.get_workflow_events_by_record_type

.. automethod:: Office.get_workflow_events_by_date

.. automethod:: Office.get_workflow_events_for_process

.. automethod:: Office.get_workflow_events_by_date_for_process

.. automethod:: Office.get_workflow_events_for_step

.. automethod:: Office.get_workflow_events_by_date_for_step

.. automethod:: Office.get_workflow_events_for_work

.. automethod:: Office.get_workflow_events_by_date_for_work

.. automethod:: Office.get_workflow_events_for_work_and_process

.. automethod:: Office.get_workflow_events_by_date_for_work_and_process

.. automethod:: Office.get_workflow_events_for_step_and_work

.. automethod:: Office.get_workflow_events_by_date_for_step_and_work

.. automethod:: Office.get_workflow_events_for_worker

.. automethod:: Office.get_workflow_events_by_date_for_worker

.. automethod:: Office.get_workflow_events_for_worker_and_process

.. automethod:: Office.get_workflow_events_by_date_for_worker_and_process

.. autoattribute:: Office.workflow_events



Workflow Event Notification Methods
-----------------------------------

.. autoattribute:: Office.office_id

.. autoattribute:: Office.office

.. automethod:: Office.can_register_for_workflow_event_notifications

.. automethod:: Office.register_for_new_workflow_events

.. automethod:: Office.register_for_new_workflow_events_for_process

.. automethod:: Office.register_for_new_workflow_events_for_step

.. automethod:: Office.register_for_new_workflow_events_for_work

.. automethod:: Office.register_for_new_workflow_events_for_worker



