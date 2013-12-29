.. currentmodule:: dlkit.abstract_osid.workflow.queries
.. automodule:: dlkit.abstract_osid.workflow.queries

Queries
=======


Process Query
-------------

.. autoclass:: ProcessQuery
   :show-inheritance:

.. automethod:: ProcessQuery.match_enabled

.. autoattribute:: ProcessQuery.enabled_terms

.. automethod:: ProcessQuery.match_initial_step_id

.. autoattribute:: ProcessQuery.initial_step_id_terms

.. automethod:: ProcessQuery.supports_initial_step_query

.. autoattribute:: ProcessQuery.initial_step_query

.. autoattribute:: ProcessQuery.initial_step_terms

.. automethod:: ProcessQuery.match_initial_state_id

.. autoattribute:: ProcessQuery.initial_state_id_terms

.. automethod:: ProcessQuery.supports_initial_state_query

.. autoattribute:: ProcessQuery.initial_state_query

.. autoattribute:: ProcessQuery.initial_state_terms

.. automethod:: ProcessQuery.match_step_id

.. autoattribute:: ProcessQuery.step_id_terms

.. automethod:: ProcessQuery.supports_step_query

.. autoattribute:: ProcessQuery.step_query

.. automethod:: ProcessQuery.match_any_step

.. autoattribute:: ProcessQuery.step_terms

.. automethod:: ProcessQuery.match_work_id

.. autoattribute:: ProcessQuery.work_id_terms

.. automethod:: ProcessQuery.supports_work_query

.. autoattribute:: ProcessQuery.work_query

.. automethod:: ProcessQuery.match_any_work

.. autoattribute:: ProcessQuery.work_terms

.. automethod:: ProcessQuery.match_office_id

.. autoattribute:: ProcessQuery.office_id_terms

.. automethod:: ProcessQuery.supports_office_query

.. autoattribute:: ProcessQuery.office_query

.. autoattribute:: ProcessQuery.office_terms

.. automethod:: ProcessQuery.get_process_query_record



Step Query
----------

.. autoclass:: StepQuery
   :show-inheritance:

.. automethod:: StepQuery.match_process_id

.. autoattribute:: StepQuery.process_id_terms

.. automethod:: StepQuery.supports_process_query

.. autoattribute:: StepQuery.process_query

.. autoattribute:: StepQuery.process_terms

.. automethod:: StepQuery.match_resource_id

.. autoattribute:: StepQuery.resource_id_terms

.. automethod:: StepQuery.supports_resource_query

.. autoattribute:: StepQuery.resource_query

.. automethod:: StepQuery.match_any_resource

.. autoattribute:: StepQuery.resource_terms

.. automethod:: StepQuery.match_initial

.. autoattribute:: StepQuery.initial_terms

.. automethod:: StepQuery.match_terminal

.. autoattribute:: StepQuery.terminal_terms

.. automethod:: StepQuery.match_input_state_id

.. autoattribute:: StepQuery.input_state_id_terms

.. automethod:: StepQuery.supports_input_state_query

.. autoattribute:: StepQuery.input_state_query

.. automethod:: StepQuery.match_any_input_state

.. autoattribute:: StepQuery.input_state_terms

.. automethod:: StepQuery.match_next_state_id

.. autoattribute:: StepQuery.next_state_id_terms

.. automethod:: StepQuery.supports_next_state_query

.. autoattribute:: StepQuery.next_state_query

.. automethod:: StepQuery.match_any_next_state

.. autoattribute:: StepQuery.next_state_terms

.. automethod:: StepQuery.match_work_id

.. autoattribute:: StepQuery.work_id_terms

.. automethod:: StepQuery.supports_work_query

.. autoattribute:: StepQuery.work_query

.. automethod:: StepQuery.match_any_work

.. autoattribute:: StepQuery.work_terms

.. automethod:: StepQuery.match_office_id

.. autoattribute:: StepQuery.office_id_terms

.. automethod:: StepQuery.supports_office_query

.. autoattribute:: StepQuery.office_query

.. autoattribute:: StepQuery.office_terms

.. automethod:: StepQuery.get_step_query_record



Work Query
----------

.. autoclass:: WorkQuery
   :show-inheritance:

.. automethod:: WorkQuery.match_suspended

.. autoattribute:: WorkQuery.suspended_terms

.. automethod:: WorkQuery.match_process_id

.. autoattribute:: WorkQuery.process_id_terms

.. automethod:: WorkQuery.supports_process_query

.. autoattribute:: WorkQuery.process_query

.. autoattribute:: WorkQuery.process_terms

.. automethod:: WorkQuery.match_step_id

.. autoattribute:: WorkQuery.step_id_terms

.. automethod:: WorkQuery.supports_step_query

.. autoattribute:: WorkQuery.step_query

.. automethod:: WorkQuery.match_any_step

.. autoattribute:: WorkQuery.step_terms

.. automethod:: WorkQuery.match_office_id

.. autoattribute:: WorkQuery.office_id_terms

.. automethod:: WorkQuery.supports_office_query

.. autoattribute:: WorkQuery.office_query

.. autoattribute:: WorkQuery.office_terms

.. automethod:: WorkQuery.get_work_query_record



Office Query
------------

.. autoclass:: OfficeQuery
   :show-inheritance:

.. automethod:: OfficeQuery.match_process_id

.. autoattribute:: OfficeQuery.process_id_terms

.. automethod:: OfficeQuery.supports_process_query

.. autoattribute:: OfficeQuery.process_query

.. automethod:: OfficeQuery.match_any_process

.. autoattribute:: OfficeQuery.process_terms

.. automethod:: OfficeQuery.match_step_id

.. autoattribute:: OfficeQuery.step_id_terms

.. automethod:: OfficeQuery.supports_step_query

.. autoattribute:: OfficeQuery.step_query

.. automethod:: OfficeQuery.match_any_step

.. autoattribute:: OfficeQuery.step_terms

.. automethod:: OfficeQuery.match_work_id

.. autoattribute:: OfficeQuery.work_id_terms

.. automethod:: OfficeQuery.supports_work_query

.. autoattribute:: OfficeQuery.work_query

.. automethod:: OfficeQuery.match_any_work

.. autoattribute:: OfficeQuery.work_terms

.. automethod:: OfficeQuery.match_ancestor_office_id

.. autoattribute:: OfficeQuery.ancestor_office_id_terms

.. automethod:: OfficeQuery.supports_ancestor_office_query

.. autoattribute:: OfficeQuery.ancestor_office_query

.. automethod:: OfficeQuery.match_any_ancestor_office

.. autoattribute:: OfficeQuery.ancestor_office_terms

.. automethod:: OfficeQuery.match_descendant_office_id

.. autoattribute:: OfficeQuery.descendant_office_id_terms

.. automethod:: OfficeQuery.supports_descendant_office_query

.. autoattribute:: OfficeQuery.descendant_office_query

.. automethod:: OfficeQuery.match_any_descendant_office

.. autoattribute:: OfficeQuery.descendant_office_terms

.. automethod:: OfficeQuery.get_office_query_record



