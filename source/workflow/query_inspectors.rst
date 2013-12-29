.. currentmodule:: dlkit.workflow.query_inspectors
.. automodule:: dlkit.workflow.query_inspectors

Query_Inspectors
================


Process Query Inspector
-----------------------

.. autoclass:: ProcessQueryInspector
   :show-inheritance:

.. autoattribute:: ProcessQueryInspector.enabled_terms

.. autoattribute:: ProcessQueryInspector.initial_step_id_terms

.. autoattribute:: ProcessQueryInspector.initial_step_terms

.. autoattribute:: ProcessQueryInspector.initial_state_id_terms

.. autoattribute:: ProcessQueryInspector.initial_state_terms

.. autoattribute:: ProcessQueryInspector.step_id_terms

.. autoattribute:: ProcessQueryInspector.step_terms

.. autoattribute:: ProcessQueryInspector.work_id_terms

.. autoattribute:: ProcessQueryInspector.work_terms

.. autoattribute:: ProcessQueryInspector.office_id_terms

.. autoattribute:: ProcessQueryInspector.office_terms

.. automethod:: ProcessQueryInspector.get_process_query_inspector_record



Step Query Inspector
--------------------

.. autoclass:: StepQueryInspector
   :show-inheritance:

.. autoattribute:: StepQueryInspector.process_id_terms

.. autoattribute:: StepQueryInspector.process_terms

.. autoattribute:: StepQueryInspector.resource_id_terms

.. autoattribute:: StepQueryInspector.resource_terms

.. autoattribute:: StepQueryInspector.work_id_terms

.. autoattribute:: StepQueryInspector.work_terms

.. autoattribute:: StepQueryInspector.initial_terms

.. autoattribute:: StepQueryInspector.terminal_terms

.. autoattribute:: StepQueryInspector.input_state_id_terms

.. autoattribute:: StepQueryInspector.input_state_terms

.. autoattribute:: StepQueryInspector.next_state_id_terms

.. autoattribute:: StepQueryInspector.next_state_terms

.. autoattribute:: StepQueryInspector.office_id_terms

.. autoattribute:: StepQueryInspector.office_terms

.. automethod:: StepQueryInspector.get_step_query_inspector_record



Work Query Inspector
--------------------

.. autoclass:: WorkQueryInspector
   :show-inheritance:

.. autoattribute:: WorkQueryInspector.suspended_terms

.. autoattribute:: WorkQueryInspector.process_id_terms

.. autoattribute:: WorkQueryInspector.process_terms

.. autoattribute:: WorkQueryInspector.step_id_terms

.. autoattribute:: WorkQueryInspector.step_terms

.. autoattribute:: WorkQueryInspector.office_id_terms

.. autoattribute:: WorkQueryInspector.office_terms

.. automethod:: WorkQueryInspector.get_work_query_inspector_record



Office Query Inspector
----------------------

.. autoclass:: OfficeQueryInspector
   :show-inheritance:

.. autoattribute:: OfficeQueryInspector.process_id_terms

.. autoattribute:: OfficeQueryInspector.process_terms

.. autoattribute:: OfficeQueryInspector.step_id_terms

.. autoattribute:: OfficeQueryInspector.step_terms

.. autoattribute:: OfficeQueryInspector.work_id_terms

.. autoattribute:: OfficeQueryInspector.work_terms

.. autoattribute:: OfficeQueryInspector.ancestor_office_id_terms

.. autoattribute:: OfficeQueryInspector.ancestor_office_terms

.. autoattribute:: OfficeQueryInspector.descendant_office_id_terms

.. autoattribute:: OfficeQueryInspector.descendant_office_terms

.. automethod:: OfficeQueryInspector.get_office_query_inspector_record



