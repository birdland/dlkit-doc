.. currentmodule:: dlkit.workflow.objects
.. automodule:: dlkit.workflow.objects

Objects
=======


Process
-------

.. autoclass:: Process
   :show-inheritance:

   .. automethod:: Process.is_enabled

   .. autoattribute:: Process.initial_step_id

   .. autoattribute:: Process.initial_step

   .. autoattribute:: Process.initial_state_id

   .. autoattribute:: Process.initial_state

   .. automethod:: Process.get_process_record



Process Form
------------

.. autoclass:: ProcessForm
   :show-inheritance:

   .. autoattribute:: ProcessForm.enabled_metadata

   .. autoattribute:: ProcessForm.enabled

   .. autoattribute:: ProcessForm.initial_step_metadata

   .. autoattribute:: ProcessForm.initial_step

   .. autoattribute:: ProcessForm.initial_state_metadata

   .. autoattribute:: ProcessForm.initial_state

   .. automethod:: ProcessForm.get_process_form_record



Process List
------------

.. autoclass:: ProcessList
   :show-inheritance:

   .. autoattribute:: ProcessList.next_process

   .. automethod:: ProcessList.get_next_processes



Step
----

.. autoclass:: Step
   :show-inheritance:

   .. autoattribute:: Step.process_id

   .. autoattribute:: Step.process

   .. autoattribute:: Step.resource_ids

   .. autoattribute:: Step.resources

   .. autoattribute:: Step.input_state_ids

   .. autoattribute:: Step.input_states

   .. autoattribute:: Step.next_state_id

   .. autoattribute:: Step.next_state

   .. automethod:: Step.get_step_record



Step Form
---------

.. autoclass:: StepForm
   :show-inheritance:

   .. autoattribute:: StepForm.input_states_metadata

   .. automethod:: StepForm.se_input_states

   .. autoattribute:: StepForm.input_states

   .. autoattribute:: StepForm.next_state_metadata

   .. autoattribute:: StepForm.next_state

   .. automethod:: StepForm.get_step_form_record



Step List
---------

.. autoclass:: StepList
   :show-inheritance:

   .. autoattribute:: StepList.next_step

   .. automethod:: StepList.get_next_steps



Work
----

.. autoclass:: Work
   :show-inheritance:

   .. automethod:: Work.get_work_record



Work Form
---------

.. autoclass:: WorkForm
   :show-inheritance:

   .. automethod:: WorkForm.get_work_form_record



Work List
---------

.. autoclass:: WorkList
   :show-inheritance:

   .. autoattribute:: WorkList.next_work

   .. automethod:: WorkList.get_next_works



Workflow Event
--------------

.. autoclass:: WorkflowEvent
   :show-inheritance:

   .. autoattribute:: WorkflowEvent.timestamp

   .. autoattribute:: WorkflowEvent.process_id

   .. autoattribute:: WorkflowEvent.process

   .. autoattribute:: WorkflowEvent.worker_id

   .. autoattribute:: WorkflowEvent.worker

   .. autoattribute:: WorkflowEvent.working_agent_id

   .. autoattribute:: WorkflowEvent.working_agent

   .. autoattribute:: WorkflowEvent.work_id

   .. autoattribute:: WorkflowEvent.work

   .. automethod:: WorkflowEvent.did_cancel

   .. autoattribute:: WorkflowEvent.step_id

   .. autoattribute:: WorkflowEvent.step

   .. automethod:: WorkflowEvent.get_workflow_event_record



Workflow Event List
-------------------

.. autoclass:: WorkflowEventList
   :show-inheritance:

   .. autoattribute:: WorkflowEventList.next_workflow_event

   .. automethod:: WorkflowEventList.get_next_workflow_events



Office Form
-----------

.. autoclass:: OfficeForm
   :show-inheritance:

   .. automethod:: OfficeForm.get_office_form_record



Office List
-----------

.. autoclass:: OfficeList
   :show-inheritance:

   .. autoattribute:: OfficeList.next_office

   .. automethod:: OfficeList.get_next_offices



Office Node
-----------

.. autoclass:: OfficeNode
   :show-inheritance:

   .. autoattribute:: OfficeNode.office

   .. autoattribute:: OfficeNode.parent_office_nodes

   .. autoattribute:: OfficeNode.child_office_nodes



Office Node List
----------------

.. autoclass:: OfficeNodeList
   :show-inheritance:

   .. autoattribute:: OfficeNodeList.next_office_node

   .. automethod:: OfficeNodeList.get_next_office_nodes



