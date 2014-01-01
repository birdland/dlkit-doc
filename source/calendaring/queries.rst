.. currentmodule:: dlkit.calendaring.queries
.. automodule:: dlkit.calendaring.queries

Queries
=======


Event Query
-----------

.. autoclass:: EventQuery
   :show-inheritance:

   .. automethod:: EventQuery.match_implicit

   .. autoattribute:: EventQuery.implicit_terms

   .. automethod:: EventQuery.match_duration

   .. automethod:: EventQuery.match_any_duration

   .. autoattribute:: EventQuery.duration_terms

   .. automethod:: EventQuery.match_time

   .. automethod:: EventQuery.match_time_inclusive

   .. automethod:: EventQuery.match_any_time

   .. autoattribute:: EventQuery.time_terms

   .. automethod:: EventQuery.match_recurring_event_id

   .. autoattribute:: EventQuery.recurring_event_id_terms

   .. automethod:: EventQuery.supports_recurring_event_query

   .. autoattribute:: EventQuery.recurring_event_query

   .. automethod:: EventQuery.match_any_recurring_event

   .. autoattribute:: EventQuery.recurring_event_terms

   .. automethod:: EventQuery.match_superseding_event_id

   .. autoattribute:: EventQuery.superseding_event_id_terms

   .. automethod:: EventQuery.supports_superseding_event_query

   .. autoattribute:: EventQuery.superseding_event_query

   .. automethod:: EventQuery.match_any_superseding_event

   .. autoattribute:: EventQuery.superseding_event_terms

   .. automethod:: EventQuery.match_offset_event_id

   .. autoattribute:: EventQuery.offset_event_id_terms

   .. automethod:: EventQuery.supports_offset_event_query

   .. autoattribute:: EventQuery.offset_event_query

   .. automethod:: EventQuery.match_any_offset_event

   .. autoattribute:: EventQuery.offset_event_terms

   .. automethod:: EventQuery.match_location_description

   .. automethod:: EventQuery.match_any_location_description

   .. autoattribute:: EventQuery.location_description_terms

   .. automethod:: EventQuery.match_location_id

   .. autoattribute:: EventQuery.location_id_terms

   .. automethod:: EventQuery.supports_location_query

   .. autoattribute:: EventQuery.location_query

   .. automethod:: EventQuery.match_any_location

   .. autoattribute:: EventQuery.location_terms

   .. automethod:: EventQuery.match_sponsor_id

   .. autoattribute:: EventQuery.sponsor_id_terms

   .. automethod:: EventQuery.supports_sponsor_query

   .. autoattribute:: EventQuery.sponsor_query

   .. autoattribute:: EventQuery.sponsor_terms

   .. automethod:: EventQuery.match_coordinate

   .. autoattribute:: EventQuery.coordinate_terms

   .. automethod:: EventQuery.match_spatial_unit

   .. autoattribute:: EventQuery.spatial_unit_terms

   .. automethod:: EventQuery.match_commitment_id

   .. autoattribute:: EventQuery.commitment_id_terms

   .. automethod:: EventQuery.supports_commitment_query

   .. autoattribute:: EventQuery.commitment_query

   .. automethod:: EventQuery.match_any_commitment

   .. autoattribute:: EventQuery.commitment_terms

   .. automethod:: EventQuery.match_containing_event_id

   .. autoattribute:: EventQuery.containing_event_id_terms

   .. automethod:: EventQuery.supports_containing_event_query

   .. autoattribute:: EventQuery.containing_event_query

   .. automethod:: EventQuery.match_containing_any_event

   .. autoattribute:: EventQuery.containing_event_terms

   .. automethod:: EventQuery.match_calendar_id

   .. autoattribute:: EventQuery.calendar_id_terms

   .. automethod:: EventQuery.supports_calendar_query

   .. autoattribute:: EventQuery.calendar_query

   .. autoattribute:: EventQuery.calendar_terms

   .. automethod:: EventQuery.get_event_query_record



Recurring Event Query
---------------------

.. autoclass:: RecurringEventQuery
   :show-inheritance:

   .. automethod:: RecurringEventQuery.match_schedule_id

   .. autoattribute:: RecurringEventQuery.schedule_id_terms

   .. automethod:: RecurringEventQuery.supports_schedule_query

   .. autoattribute:: RecurringEventQuery.schedule_query

   .. automethod:: RecurringEventQuery.match_any_schedule

   .. autoattribute:: RecurringEventQuery.schedule_terms

   .. automethod:: RecurringEventQuery.match_superseding_event_id

   .. autoattribute:: RecurringEventQuery.superseding_event_id_terms

   .. automethod:: RecurringEventQuery.supports_superseding_event_query

   .. autoattribute:: RecurringEventQuery.superseding_event_query

   .. automethod:: RecurringEventQuery.match_any_superseding_event

   .. autoattribute:: RecurringEventQuery.superseding_event_terms

   .. automethod:: RecurringEventQuery.match_specific_meeting_time

   .. automethod:: RecurringEventQuery.match_any_specific_meeting_time

   .. autoattribute:: RecurringEventQuery.specific_meeting_time_terms

   .. automethod:: RecurringEventQuery.match_event_id

   .. autoattribute:: RecurringEventQuery.event_id_terms

   .. automethod:: RecurringEventQuery.supports_event_query

   .. autoattribute:: RecurringEventQuery.event_query

   .. automethod:: RecurringEventQuery.match_any_event

   .. autoattribute:: RecurringEventQuery.event_terms

   .. automethod:: RecurringEventQuery.match_blackout

   .. automethod:: RecurringEventQuery.match_blackout_inclusive

   .. automethod:: RecurringEventQuery.match_any_blackout

   .. autoattribute:: RecurringEventQuery.blackout_terms

   .. automethod:: RecurringEventQuery.match_sponsor_id

   .. autoattribute:: RecurringEventQuery.sponsor_id_terms

   .. automethod:: RecurringEventQuery.supports_sponsor_query

   .. autoattribute:: RecurringEventQuery.sponsor_query

   .. autoattribute:: RecurringEventQuery.sponsor_terms

   .. automethod:: RecurringEventQuery.match_date

   .. automethod:: RecurringEventQuery.match_calendar_id

   .. autoattribute:: RecurringEventQuery.calendar_id_terms

   .. automethod:: RecurringEventQuery.supports_calendar_query

   .. autoattribute:: RecurringEventQuery.calendar_query

   .. autoattribute:: RecurringEventQuery.calendar_terms

   .. automethod:: RecurringEventQuery.get_recurring_event_query_record



Superseding Event Query
-----------------------

.. autoclass:: SupersedingEventQuery
   :show-inheritance:

   .. automethod:: SupersedingEventQuery.match_superseded_event_id

   .. autoattribute:: SupersedingEventQuery.superseded_event_id_terms

   .. automethod:: SupersedingEventQuery.supports_superseded_event_query

   .. autoattribute:: SupersedingEventQuery.superseded_event_query

   .. autoattribute:: SupersedingEventQuery.superseded_event_terms

   .. automethod:: SupersedingEventQuery.match_superseding_event_id

   .. autoattribute:: SupersedingEventQuery.superseding_event_id_terms

   .. automethod:: SupersedingEventQuery.supports_superseding_event_query

   .. autoattribute:: SupersedingEventQuery.superseding_event_query

   .. autoattribute:: SupersedingEventQuery.superseding_event_terms

   .. automethod:: SupersedingEventQuery.match_superseded_date

   .. automethod:: SupersedingEventQuery.match_any_superseded_date

   .. autoattribute:: SupersedingEventQuery.superseded_date_terms

   .. automethod:: SupersedingEventQuery.match_superseded_event_position

   .. automethod:: SupersedingEventQuery.match_any_superseded_event_position

   .. autoattribute:: SupersedingEventQuery.superseded_position_terms

   .. automethod:: SupersedingEventQuery.match_calendar_id

   .. autoattribute:: SupersedingEventQuery.calendar_id_terms

   .. automethod:: SupersedingEventQuery.supports_calendar_query

   .. autoattribute:: SupersedingEventQuery.calendar_query

   .. autoattribute:: SupersedingEventQuery.calendar_terms

   .. automethod:: SupersedingEventQuery.get_superseding_event_query_record



Offset Event Query
------------------

.. autoclass:: OffsetEventQuery
   :show-inheritance:

   .. automethod:: OffsetEventQuery.match_fixed_start_time

   .. automethod:: OffsetEventQuery.match_any_fixed_start_time

   .. autoattribute:: OffsetEventQuery.fixed_start_time_terms

   .. automethod:: OffsetEventQuery.match_start_reference_event_id

   .. autoattribute:: OffsetEventQuery.start_reference_event_id_terms

   .. automethod:: OffsetEventQuery.supports_start_reference_event_query

   .. autoattribute:: OffsetEventQuery.start_reference_event_query

   .. automethod:: OffsetEventQuery.match_any_start_reference_event

   .. autoattribute:: OffsetEventQuery.start_reference_event_terms

   .. automethod:: OffsetEventQuery.match_fixed_start_offset

   .. automethod:: OffsetEventQuery.match_any_fixed_start_offset

   .. autoattribute:: OffsetEventQuery.fixed_start_offset_terms

   .. automethod:: OffsetEventQuery.match_relative_weekday_start_offset

   .. autoattribute:: OffsetEventQuery.relative_weekday_start_offset_terms

   .. automethod:: OffsetEventQuery.match_relative_start_weekday

   .. automethod:: OffsetEventQuery.match_any_relative_start_weekdays

   .. autoattribute:: OffsetEventQuery.relative_start_weekday_terms

   .. automethod:: OffsetEventQuery.match_fixed_duration_offset

   .. autoattribute:: OffsetEventQuery.fixed_duration_terms

   .. automethod:: OffsetEventQuery.match_end_reference_event_id

   .. autoattribute:: OffsetEventQuery.end_reference_event_id_terms

   .. automethod:: OffsetEventQuery.supports_end_reference_event_query

   .. autoattribute:: OffsetEventQuery.end_reference_event_query

   .. automethod:: OffsetEventQuery.match_any_end_reference_event

   .. autoattribute:: OffsetEventQuery.end_reference_event_terms

   .. automethod:: OffsetEventQuery.match_fixed_end_offset

   .. automethod:: OffsetEventQuery.match_any_fixed_end_offset

   .. autoattribute:: OffsetEventQuery.fixed_end_offset_terms

   .. automethod:: OffsetEventQuery.match_relative_weekday_end_offset

   .. autoattribute:: OffsetEventQuery.relative_weekday_end_offset_terms

   .. automethod:: OffsetEventQuery.match_relative_end_weekday

   .. automethod:: OffsetEventQuery.match_any_relative_end_weekdays

   .. autoattribute:: OffsetEventQuery.relative_end_weekday_terms

   .. automethod:: OffsetEventQuery.supports_event_query

   .. autoattribute:: OffsetEventQuery.event_query

   .. automethod:: OffsetEventQuery.match_calendar_id

   .. autoattribute:: OffsetEventQuery.calendar_id_terms

   .. automethod:: OffsetEventQuery.supports_calendar_query

   .. autoattribute:: OffsetEventQuery.calendar_query

   .. autoattribute:: OffsetEventQuery.calendar_terms

   .. automethod:: OffsetEventQuery.get_offset_event_query_record



Schedule Query
--------------

.. autoclass:: ScheduleQuery
   :show-inheritance:

   .. automethod:: ScheduleQuery.match_schedule_slot_id

   .. autoattribute:: ScheduleQuery.schedule_slot_id_terms

   .. automethod:: ScheduleQuery.supports_schedule_slot_query

   .. autoattribute:: ScheduleQuery.schedule_slot_query

   .. automethod:: ScheduleQuery.match_any_schedule_slot

   .. autoattribute:: ScheduleQuery.schedule_slot_terms

   .. automethod:: ScheduleQuery.match_time_period_id

   .. autoattribute:: ScheduleQuery.time_period_id_terms

   .. automethod:: ScheduleQuery.supports_time_period_query

   .. autoattribute:: ScheduleQuery.time_period_query

   .. automethod:: ScheduleQuery.match_any_time_period

   .. autoattribute:: ScheduleQuery.time_period_terms

   .. automethod:: ScheduleQuery.match_schedule_start

   .. automethod:: ScheduleQuery.match_any_schedule_start

   .. autoattribute:: ScheduleQuery.schedule_start_terms

   .. automethod:: ScheduleQuery.match_schedule_end

   .. automethod:: ScheduleQuery.match_any_schedule_end

   .. autoattribute:: ScheduleQuery.schedule_end_terms

   .. automethod:: ScheduleQuery.match_schedule_time_inclusive

   .. automethod:: ScheduleQuery.match_any_schedule_time

   .. autoattribute:: ScheduleQuery.schedule_time_terms

   .. automethod:: ScheduleQuery.match_limit

   .. automethod:: ScheduleQuery.match_any_limit

   .. autoattribute:: ScheduleQuery.limit_terms

   .. automethod:: ScheduleQuery.match_location_description

   .. automethod:: ScheduleQuery.match_any_location_description

   .. autoattribute:: ScheduleQuery.location_description_terms

   .. automethod:: ScheduleQuery.match_location_id

   .. autoattribute:: ScheduleQuery.location_id_terms

   .. automethod:: ScheduleQuery.supports_location_query

   .. autoattribute:: ScheduleQuery.location_query

   .. automethod:: ScheduleQuery.match_any_location

   .. autoattribute:: ScheduleQuery.location_terms

   .. automethod:: ScheduleQuery.match_total_duration

   .. autoattribute:: ScheduleQuery.total_duration_terms

   .. automethod:: ScheduleQuery.match_calendar_id

   .. autoattribute:: ScheduleQuery.calendar_id_terms

   .. automethod:: ScheduleQuery.supports_calendar_query

   .. autoattribute:: ScheduleQuery.calendar_query

   .. autoattribute:: ScheduleQuery.calendar_terms

   .. automethod:: ScheduleQuery.get_schedule_query_record



Schedule Slot Query
-------------------

.. autoclass:: ScheduleSlotQuery
   :show-inheritance:

   .. automethod:: ScheduleSlotQuery.match_schedule_slot_id

   .. autoattribute:: ScheduleSlotQuery.schedule_slot_id_terms

   .. automethod:: ScheduleSlotQuery.supports_schedule_slot_query

   .. autoattribute:: ScheduleSlotQuery.schedule_slot_query

   .. automethod:: ScheduleSlotQuery.match_any_schedule_slot

   .. autoattribute:: ScheduleSlotQuery.schedule_slot_terms

   .. automethod:: ScheduleSlotQuery.match_weekday

   .. automethod:: ScheduleSlotQuery.match_any_weekday

   .. autoattribute:: ScheduleSlotQuery.weekday_terms

   .. automethod:: ScheduleSlotQuery.match_weekly_interval

   .. automethod:: ScheduleSlotQuery.match_any_weekly_interval

   .. autoattribute:: ScheduleSlotQuery.weekly_interval_terms

   .. automethod:: ScheduleSlotQuery.match_week_of_month

   .. automethod:: ScheduleSlotQuery.match_any_week_of_month

   .. autoattribute:: ScheduleSlotQuery.week_of_month_terms

   .. automethod:: ScheduleSlotQuery.match_weekday_time

   .. automethod:: ScheduleSlotQuery.match_any_weekday_time

   .. autoattribute:: ScheduleSlotQuery.weekday_time_terms

   .. automethod:: ScheduleSlotQuery.match_fixed_interval

   .. automethod:: ScheduleSlotQuery.match_any_fixed_interval

   .. autoattribute:: ScheduleSlotQuery.fixed_interval_terms

   .. automethod:: ScheduleSlotQuery.match_duration

   .. automethod:: ScheduleSlotQuery.match_any_duration

   .. autoattribute:: ScheduleSlotQuery.duration_terms

   .. automethod:: ScheduleSlotQuery.match_calendar_id

   .. autoattribute:: ScheduleSlotQuery.calendar_id_terms

   .. automethod:: ScheduleSlotQuery.supports_calendar_query

   .. autoattribute:: ScheduleSlotQuery.calendar_query

   .. autoattribute:: ScheduleSlotQuery.calendar_terms

   .. automethod:: ScheduleSlotQuery.get_schedule_slot_query_record



Time Period Query
-----------------

.. autoclass:: TimePeriodQuery
   :show-inheritance:

   .. automethod:: TimePeriodQuery.match_start

   .. automethod:: TimePeriodQuery.match_any_start

   .. autoattribute:: TimePeriodQuery.start_terms

   .. automethod:: TimePeriodQuery.match_end

   .. automethod:: TimePeriodQuery.match_any_end

   .. autoattribute:: TimePeriodQuery.end_terms

   .. automethod:: TimePeriodQuery.match_time

   .. automethod:: TimePeriodQuery.match_time_inclusive

   .. automethod:: TimePeriodQuery.match_any_time

   .. autoattribute:: TimePeriodQuery.time_terms

   .. automethod:: TimePeriodQuery.match_duration

   .. autoattribute:: TimePeriodQuery.duration_terms

   .. automethod:: TimePeriodQuery.match_exception_id

   .. autoattribute:: TimePeriodQuery.exception_id_terms

   .. automethod:: TimePeriodQuery.supports_exception_query

   .. autoattribute:: TimePeriodQuery.exception_query

   .. automethod:: TimePeriodQuery.match_any_exception

   .. autoattribute:: TimePeriodQuery.exception_terms

   .. automethod:: TimePeriodQuery.match_event_id

   .. autoattribute:: TimePeriodQuery.event_id_terms

   .. automethod:: TimePeriodQuery.supports_event_query

   .. autoattribute:: TimePeriodQuery.event_query

   .. automethod:: TimePeriodQuery.match_any_event

   .. autoattribute:: TimePeriodQuery.event_terms

   .. automethod:: TimePeriodQuery.match_calendar_id

   .. autoattribute:: TimePeriodQuery.calendar_id_terms

   .. automethod:: TimePeriodQuery.supports_calendar_query

   .. autoattribute:: TimePeriodQuery.calendar_query

   .. autoattribute:: TimePeriodQuery.calendar_terms

   .. automethod:: TimePeriodQuery.get_time_period_query_record



Commitment Query
----------------

.. autoclass:: CommitmentQuery
   :show-inheritance:

   .. automethod:: CommitmentQuery.match_event_id

   .. autoattribute:: CommitmentQuery.event_id_terms

   .. automethod:: CommitmentQuery.supports_event_query

   .. autoattribute:: CommitmentQuery.event_query

   .. autoattribute:: CommitmentQuery.event_terms

   .. automethod:: CommitmentQuery.match_resource_id

   .. autoattribute:: CommitmentQuery.resource_id_terms

   .. automethod:: CommitmentQuery.supports_resource_query

   .. autoattribute:: CommitmentQuery.resource_query

   .. autoattribute:: CommitmentQuery.resource_terms

   .. automethod:: CommitmentQuery.match_calendar_id

   .. autoattribute:: CommitmentQuery.calendar_id_terms

   .. automethod:: CommitmentQuery.supports_calendar_query

   .. autoattribute:: CommitmentQuery.calendar_query

   .. autoattribute:: CommitmentQuery.calendar_terms

   .. automethod:: CommitmentQuery.get_commitment_query_record



Calendar Query
--------------

.. autoclass:: CalendarQuery
   :show-inheritance:

   .. automethod:: CalendarQuery.match_event_id

   .. autoattribute:: CalendarQuery.event_id_terms

   .. automethod:: CalendarQuery.supports_event_query

   .. autoattribute:: CalendarQuery.event_query

   .. automethod:: CalendarQuery.match_any_event

   .. autoattribute:: CalendarQuery.event_terms

   .. automethod:: CalendarQuery.match_time_period_id

   .. autoattribute:: CalendarQuery.time_period_id_terms

   .. automethod:: CalendarQuery.supports_time_period_query

   .. autoattribute:: CalendarQuery.time_period_query

   .. automethod:: CalendarQuery.match_any_term

   .. autoattribute:: CalendarQuery.term_terms

   .. automethod:: CalendarQuery.match_commitment_id

   .. autoattribute:: CalendarQuery.commitment_id_terms

   .. automethod:: CalendarQuery.supports_commitment_query

   .. autoattribute:: CalendarQuery.commitment_query

   .. automethod:: CalendarQuery.match_any_commitment

   .. autoattribute:: CalendarQuery.commitment_terms

   .. automethod:: CalendarQuery.match_ancestor_calendar_id

   .. autoattribute:: CalendarQuery.ancestor_calendar_id_terms

   .. automethod:: CalendarQuery.supports_ancestor_calendar_query

   .. autoattribute:: CalendarQuery.ancestor_calendar_query

   .. automethod:: CalendarQuery.match_any_ancestor_calendar

   .. autoattribute:: CalendarQuery.ancestor_calendar_terms

   .. automethod:: CalendarQuery.match_descendant_calendar_id

   .. autoattribute:: CalendarQuery.descendant_calendar_id_terms

   .. automethod:: CalendarQuery.supports_descendant_calendar_query

   .. autoattribute:: CalendarQuery.descendant_calendar_query

   .. automethod:: CalendarQuery.match_any_descendant_calendar

   .. autoattribute:: CalendarQuery.descendant_calendar_terms

   .. automethod:: CalendarQuery.get_calendar_query_record



