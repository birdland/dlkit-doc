.. currentmodule:: dlkit.calendaring.receivers
.. automodule:: dlkit.calendaring.receivers

Receivers
=========


Event Receiver
--------------

.. autoclass:: EventReceiver
   :show-inheritance:

   .. automethod:: EventReceiver.new_event

   .. automethod:: EventReceiver.changed_event

   .. automethod:: EventReceiver.deleted_event



Recurring Event Receiver
------------------------

.. autoclass:: RecurringEventReceiver
   :show-inheritance:

   .. automethod:: RecurringEventReceiver.new_recurring_event

   .. automethod:: RecurringEventReceiver.changed_recurring_event

   .. automethod:: RecurringEventReceiver.deleted_recurring_event



Superseding Event Receiver
--------------------------

.. autoclass:: SupersedingEventReceiver
   :show-inheritance:

   .. automethod:: SupersedingEventReceiver.new_superseding_event

   .. automethod:: SupersedingEventReceiver.changed_superseding_event

   .. automethod:: SupersedingEventReceiver.deleted_superseding_event



Offset Event Receiver
---------------------

.. autoclass:: OffsetEventReceiver
   :show-inheritance:

   .. automethod:: OffsetEventReceiver.new_offset_event

   .. automethod:: OffsetEventReceiver.changed_offset_event

   .. automethod:: OffsetEventReceiver.deleted_offset_event



Schedule Receiver
-----------------

.. autoclass:: ScheduleReceiver
   :show-inheritance:

   .. automethod:: ScheduleReceiver.new_schedule

   .. automethod:: ScheduleReceiver.changed_schedule

   .. automethod:: ScheduleReceiver.deleted_schedule



Schedule Slot Receiver
----------------------

.. autoclass:: ScheduleSlotReceiver
   :show-inheritance:

   .. automethod:: ScheduleSlotReceiver.new_schedule_slot

   .. automethod:: ScheduleSlotReceiver.new_schedule_slot_ancestor

   .. automethod:: ScheduleSlotReceiver.new_schedule_slot_descendant

   .. automethod:: ScheduleSlotReceiver.changed_schedule_slot

   .. automethod:: ScheduleSlotReceiver.deleted_schedule_slot

   .. automethod:: ScheduleSlotReceiver.deleted_schedule_slot_descendant

   .. automethod:: ScheduleSlotReceiver.deleted_schedule_slot_ancestor



Time Period Receiver
--------------------

.. autoclass:: TimePeriodReceiver
   :show-inheritance:

   .. automethod:: TimePeriodReceiver.new_time_period

   .. automethod:: TimePeriodReceiver.changed_time_period

   .. automethod:: TimePeriodReceiver.deleted_time_period



Commitment Receiver
-------------------

.. autoclass:: CommitmentReceiver
   :show-inheritance:

   .. automethod:: CommitmentReceiver.new_commitment

   .. automethod:: CommitmentReceiver.new_commitment_for_event

   .. automethod:: CommitmentReceiver.new_commitment_for_resource

   .. automethod:: CommitmentReceiver.changed_commitment

   .. automethod:: CommitmentReceiver.changed_commitment_for_event

   .. automethod:: CommitmentReceiver.changed_commitment_for_resource

   .. automethod:: CommitmentReceiver.changed_commitment_state

   .. automethod:: CommitmentReceiver.deleted_commitment

   .. automethod:: CommitmentReceiver.deleted_commitment_for_event

   .. automethod:: CommitmentReceiver.deleted_commitment_for_resource



Calendar Receiver
-----------------

.. autoclass:: CalendarReceiver
   :show-inheritance:

   .. automethod:: CalendarReceiver.new_calendar

   .. automethod:: CalendarReceiver.new_ancestor_calendar

   .. automethod:: CalendarReceiver.new_descendant_calendar

   .. automethod:: CalendarReceiver.changed_calendar

   .. automethod:: CalendarReceiver.deleted_calendar

   .. automethod:: CalendarReceiver.deleted_ancestor_calendar

   .. automethod:: CalendarReceiver.deleted_descendant_calendar



