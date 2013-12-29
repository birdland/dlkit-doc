.. currentmodule:: dlkit.calendaring.query_inspectors
.. automodule:: dlkit.calendaring.query_inspectors

Query_Inspectors
================


Event Query Inspector
---------------------

.. autoclass:: EventQueryInspector
   :show-inheritance:

.. autoattribute:: EventQueryInspector.implicit_terms

.. autoattribute:: EventQueryInspector.duration_terms

.. autoattribute:: EventQueryInspector.time_terms

.. autoattribute:: EventQueryInspector.recurring_event_id_terms

.. autoattribute:: EventQueryInspector.recurring_event_terms

.. autoattribute:: EventQueryInspector.superseding_event_id_terms

.. autoattribute:: EventQueryInspector.superseding_event_terms

.. autoattribute:: EventQueryInspector.offset_event_id_terms

.. autoattribute:: EventQueryInspector.offset_event_terms

.. autoattribute:: EventQueryInspector.location_description_terms

.. autoattribute:: EventQueryInspector.location_id_terms

.. autoattribute:: EventQueryInspector.location_terms

.. autoattribute:: EventQueryInspector.sponsor_id_terms

.. autoattribute:: EventQueryInspector.sponsor_terms

.. autoattribute:: EventQueryInspector.coordinate_terms

.. autoattribute:: EventQueryInspector.spatial_unit_terms

.. autoattribute:: EventQueryInspector.commitment_id_terms

.. autoattribute:: EventQueryInspector.commitment_terms

.. autoattribute:: EventQueryInspector.containing_event_id_terms

.. autoattribute:: EventQueryInspector.containing_event_terms

.. autoattribute:: EventQueryInspector.calendar_id_terms

.. autoattribute:: EventQueryInspector.calendar_terms

.. automethod:: EventQueryInspector.get_event_query_inspector_record



Recurring Event Query Inspector
-------------------------------

.. autoclass:: RecurringEventQueryInspector
   :show-inheritance:

.. automethod:: RecurringEventQueryInspector.ge_schedule_id_terms

.. autoattribute:: RecurringEventQueryInspector.schedule_terms

.. autoattribute:: RecurringEventQueryInspector.superseding_event_id_terms

.. autoattribute:: RecurringEventQueryInspector.superseding_event_terms

.. autoattribute:: RecurringEventQueryInspector.speific_date_terms

.. autoattribute:: RecurringEventQueryInspector.event_id_terms

.. autoattribute:: RecurringEventQueryInspector.event_terms

.. autoattribute:: RecurringEventQueryInspector.blackout_terms

.. autoattribute:: RecurringEventQueryInspector.blackout_inclusive_terms

.. autoattribute:: RecurringEventQueryInspector.sponsor_id_terms

.. autoattribute:: RecurringEventQueryInspector.sponsor_terms

.. autoattribute:: RecurringEventQueryInspector.specific_meeting_time_terms

.. autoattribute:: RecurringEventQueryInspector.calendar_id_terms

.. autoattribute:: RecurringEventQueryInspector.calendar_terms

.. automethod:: RecurringEventQueryInspector.get_recurring_event_query_inspector_record



Superseding Event Query Inspector
---------------------------------

.. autoclass:: SupersedingEventQueryInspector
   :show-inheritance:

.. autoattribute:: SupersedingEventQueryInspector.event_id_terms

.. autoattribute:: SupersedingEventQueryInspector.event_terms

.. autoattribute:: SupersedingEventQueryInspector.recurring_event_id_terms

.. autoattribute:: SupersedingEventQueryInspector.recurring_event_terms

.. autoattribute:: SupersedingEventQueryInspector.superseded_event_id_terms

.. autoattribute:: SupersedingEventQueryInspector.superseded_event_terms

.. autoattribute:: SupersedingEventQueryInspector.superseded_date_terms

.. autoattribute:: SupersedingEventQueryInspector.superseded_event_position_terms

.. autoattribute:: SupersedingEventQueryInspector.calendar_id_terms

.. autoattribute:: SupersedingEventQueryInspector.calendar_terms

.. automethod:: SupersedingEventQueryInspector.get_superseding_event_query_inspector_record



Offset Event Query Inspector
----------------------------

.. autoclass:: OffsetEventQueryInspector
   :show-inheritance:

.. autoattribute:: OffsetEventQueryInspector.fixed_start_time_terms

.. autoattribute:: OffsetEventQueryInspector.start_reference_event_id_terms

.. autoattribute:: OffsetEventQueryInspector.start_reference_event_terms

.. autoattribute:: OffsetEventQueryInspector.fixed_start_offset_terms

.. autoattribute:: OffsetEventQueryInspector.relative_weekday_start_offset_terms

.. autoattribute:: OffsetEventQueryInspector.relative_start_weekday_terms

.. autoattribute:: OffsetEventQueryInspector.fixed_duration_terms

.. autoattribute:: OffsetEventQueryInspector.end_reference_event_id_terms

.. autoattribute:: OffsetEventQueryInspector.end_reference_event_terms

.. autoattribute:: OffsetEventQueryInspector.fixed_end_offset_terms

.. autoattribute:: OffsetEventQueryInspector.relative_weekday_end_offset_terms

.. autoattribute:: OffsetEventQueryInspector.relative_end_weekday_terms

.. autoattribute:: OffsetEventQueryInspector.event_terms

.. autoattribute:: OffsetEventQueryInspector.calendar_id_terms

.. autoattribute:: OffsetEventQueryInspector.calendar_terms

.. automethod:: OffsetEventQueryInspector.get_offset_event_query_inspector_record



Schedule Query Inspector
------------------------

.. autoclass:: ScheduleQueryInspector
   :show-inheritance:

.. autoattribute:: ScheduleQueryInspector.schedule_slot_id_terms

.. autoattribute:: ScheduleQueryInspector.schedule_slot_terms

.. autoattribute:: ScheduleQueryInspector.time_period_id_terms

.. autoattribute:: ScheduleQueryInspector.time_period_terms

.. autoattribute:: ScheduleQueryInspector.schedule_start_terms

.. autoattribute:: ScheduleQueryInspector.schedule_end_terms

.. autoattribute:: ScheduleQueryInspector.schedule_time_inclusive_terms

.. autoattribute:: ScheduleQueryInspector.limit_terms

.. autoattribute:: ScheduleQueryInspector.location_description_terms

.. autoattribute:: ScheduleQueryInspector.location_id_terms

.. autoattribute:: ScheduleQueryInspector.location_terms

.. autoattribute:: ScheduleQueryInspector.total_duration_terms

.. autoattribute:: ScheduleQueryInspector.calendar_id_terms

.. autoattribute:: ScheduleQueryInspector.calendar_terms

.. automethod:: ScheduleQueryInspector.get_schedule_query_inspector_record



Schedule Slot Query Inspector
-----------------------------

.. autoclass:: ScheduleSlotQueryInspector
   :show-inheritance:

.. autoattribute:: ScheduleSlotQueryInspector.schedule_slot_id_terms

.. autoattribute:: ScheduleSlotQueryInspector.schedule_slot_terms

.. autoattribute:: ScheduleSlotQueryInspector.weekday_terms

.. autoattribute:: ScheduleSlotQueryInspector.weekly_interval_terms

.. autoattribute:: ScheduleSlotQueryInspector.week_of_month_terms

.. autoattribute:: ScheduleSlotQueryInspector.weekday_time_terms

.. autoattribute:: ScheduleSlotQueryInspector.fixed_interval_terms

.. autoattribute:: ScheduleSlotQueryInspector.duration_terms

.. autoattribute:: ScheduleSlotQueryInspector.calendar_id_terms

.. autoattribute:: ScheduleSlotQueryInspector.calendar_terms

.. automethod:: ScheduleSlotQueryInspector.get_schedule_slot_query_inspector_record



Time Period Query Inspector
---------------------------

.. autoclass:: TimePeriodQueryInspector
   :show-inheritance:

.. autoattribute:: TimePeriodQueryInspector.start_terms

.. autoattribute:: TimePeriodQueryInspector.end_terms

.. autoattribute:: TimePeriodQueryInspector.time_terms

.. autoattribute:: TimePeriodQueryInspector.time_inclusive_terms

.. autoattribute:: TimePeriodQueryInspector.duration_terms

.. autoattribute:: TimePeriodQueryInspector.exception_id_terms

.. autoattribute:: TimePeriodQueryInspector.exception_terms

.. autoattribute:: TimePeriodQueryInspector.event_id_terms

.. autoattribute:: TimePeriodQueryInspector.event_terms

.. autoattribute:: TimePeriodQueryInspector.calendar_id_terms

.. autoattribute:: TimePeriodQueryInspector.calendar_terms

.. automethod:: TimePeriodQueryInspector.get_time_period_query_inspector_record



Commitment Query Inspector
--------------------------

.. autoclass:: CommitmentQueryInspector
   :show-inheritance:

.. autoattribute:: CommitmentQueryInspector.event_id_terms

.. autoattribute:: CommitmentQueryInspector.event_terms

.. autoattribute:: CommitmentQueryInspector.resource_id_terms

.. autoattribute:: CommitmentQueryInspector.resource_terms

.. autoattribute:: CommitmentQueryInspector.calendar_id_terms

.. autoattribute:: CommitmentQueryInspector.calendar_terms

.. automethod:: CommitmentQueryInspector.get_commitment_query_inspector_record



Calendar Query Inspector
------------------------

.. autoclass:: CalendarQueryInspector
   :show-inheritance:

.. autoattribute:: CalendarQueryInspector.event_id_terms

.. autoattribute:: CalendarQueryInspector.event_terms

.. autoattribute:: CalendarQueryInspector.time_period_id_terms

.. autoattribute:: CalendarQueryInspector.time_period_terms

.. autoattribute:: CalendarQueryInspector.commitment_id_terms

.. autoattribute:: CalendarQueryInspector.commitment_terms

.. autoattribute:: CalendarQueryInspector.ancestor_calendar_id_terms

.. autoattribute:: CalendarQueryInspector.ancestor_calendar_terms

.. autoattribute:: CalendarQueryInspector.descendant_calendar_id_terms

.. autoattribute:: CalendarQueryInspector.descendant_calendar_terms

.. automethod:: CalendarQueryInspector.get_calendar_query_inspector_record



