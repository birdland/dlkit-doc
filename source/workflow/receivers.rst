.. currentmodule:: dlkit.abstract_osid.workflow.receivers
.. automodule:: dlkit.abstract_osid.workflow.receivers

Receivers
=========


Process Receiver
----------------

.. autoclass:: ProcessReceiver
   :show-inheritance:

.. automethod:: ProcessReceiver.new_process

.. automethod:: ProcessReceiver.changed_process

.. automethod:: ProcessReceiver.deleted_process



Step Receiver
-------------

.. autoclass:: StepReceiver
   :show-inheritance:

.. automethod:: StepReceiver.new_step

.. automethod:: StepReceiver.changed_step

.. automethod:: StepReceiver.deleted_step



Work Receiver
-------------

.. autoclass:: WorkReceiver
   :show-inheritance:

.. automethod:: WorkReceiver.new_work

.. automethod:: WorkReceiver.changed_work

.. automethod:: WorkReceiver.deleted_work



Workflow Event Receiver
-----------------------

.. autoclass:: WorkflowEventReceiver
   :show-inheritance:

.. automethod:: WorkflowEventReceiver.new_workflow_event



Office Receiver
---------------

.. autoclass:: OfficeReceiver
   :show-inheritance:

.. automethod:: OfficeReceiver.new_office

.. automethod:: OfficeReceiver.new_ancestor_office

.. automethod:: OfficeReceiver.new_descendant_office

.. automethod:: OfficeReceiver.changed_office

.. automethod:: OfficeReceiver.deleted_office

.. automethod:: OfficeReceiver.deleted_ancestor_office

.. automethod:: OfficeReceiver.deleted_descendant_office



