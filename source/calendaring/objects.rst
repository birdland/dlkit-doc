.. currentmodule:: dlkit.calendaring.objects
.. automodule:: dlkit.calendaring.objects

Objects
=======


Event
-----

.. autoclass:: Event
   :show-inheritance:

.. automethod:: Event.is_implicit

.. automethod:: Event.is_in_recurring_series

.. automethod:: Event.is_superseding_event

.. automethod:: Event.is_offset_event

.. automethod:: Event.get_duration

.. autoattribute:: Event.location_description

.. automethod:: Event.has_location

.. autoattribute:: Event.location_id

.. autoattribute:: Event.location

.. automethod:: Event.has_sponsors

.. autoattribute:: Event.sponsor_ids

.. autoattribute:: Event.sponsors

.. automethod:: Event.get_event_record



Event Form
----------

.. autoclass:: EventForm
   :show-inheritance:

.. autoattribute:: EventForm.location_description_metadata

.. autoattribute:: EventForm.location_description

.. autoattribute:: EventForm.location_metadata

.. autoattribute:: EventForm.location

.. autoattribute:: EventForm.sponsor_metadata

.. autoattribute:: EventForm.sponsors

.. automethod:: EventForm.get_event_form_record



Event List
----------

.. autoclass:: EventList
   :show-inheritance:

.. autoattribute:: EventList.next_event

.. automethod:: EventList.get_next_events



Recurring Event
---------------

.. autoclass:: RecurringEvent
   :show-inheritance:

.. autoattribute:: RecurringEvent.schedule_ids

.. autoattribute:: RecurringEvent.schedules

.. autoattribute:: RecurringEvent.superseding_event_ids

.. autoattribute:: RecurringEvent.superseding_events

.. autoattribute:: RecurringEvent.specific_meeting_times

.. autoattribute:: RecurringEvent.event_ids

.. autoattribute:: RecurringEvent.events

.. autoattribute:: RecurringEvent.blackouts

.. automethod:: RecurringEvent.has_sponsors

.. autoattribute:: RecurringEvent.sponsor_ids

.. autoattribute:: RecurringEvent.sponsors

.. automethod:: RecurringEvent.get_recurring_event_record



Recurring Event Form
--------------------

.. autoclass:: RecurringEventForm
   :show-inheritance:

.. autoattribute:: RecurringEventForm.sponsor_metadata

.. autoattribute:: RecurringEventForm.sponsors

.. automethod:: RecurringEventForm.get_recurring_event_form_record



Recurring Event List
--------------------

.. autoclass:: RecurringEventList
   :show-inheritance:

.. autoattribute:: RecurringEventList.next_recurring_event

.. automethod:: RecurringEventList.get_next_recurring_events



Superseding Event
-----------------

.. autoclass:: SupersedingEvent
   :show-inheritance:

.. autoattribute:: SupersedingEvent.superseded_event_id

.. autoattribute:: SupersedingEvent.superseded_event

.. autoattribute:: SupersedingEvent.superseding_event_id

.. autoattribute:: SupersedingEvent.superseding_event

.. automethod:: SupersedingEvent.supersedes_by_date

.. autoattribute:: SupersedingEvent.superseded_date

.. automethod:: SupersedingEvent.supersedes_by_position

.. autoattribute:: SupersedingEvent.superseded_event_position

.. automethod:: SupersedingEvent.get_superseding_event_record



Superseding Event Form
----------------------

.. autoclass:: SupersedingEventForm
   :show-inheritance:

.. autoattribute:: SupersedingEventForm.superseded_date_metadata

.. autoattribute:: SupersedingEventForm.superseded_date

.. autoattribute:: SupersedingEventForm.superseded_position_metadata

.. autoattribute:: SupersedingEventForm.superseded_position

.. automethod:: SupersedingEventForm.get_superseding_event_form_record



Superseding Event List
----------------------

.. autoclass:: SupersedingEventList
   :show-inheritance:

.. autoattribute:: SupersedingEventList.next_superseding_event

.. automethod:: SupersedingEventList.get_next_superseding_events



Offset Event
------------

.. autoclass:: OffsetEvent
   :show-inheritance:

.. automethod:: OffsetEvent.has_fixed_start_time

.. autoattribute:: OffsetEvent.fixed_start_time

.. autoattribute:: OffsetEvent.start_reference_event_id

.. autoattribute:: OffsetEvent.start_reference_event

.. automethod:: OffsetEvent.has_fixed_start_offset

.. autoattribute:: OffsetEvent.fixed_start_offset

.. automethod:: OffsetEvent.has_relative_weekday_start_offset

.. autoattribute:: OffsetEvent.relative_weekday_start_offset

.. autoattribute:: OffsetEvent.relative_start_weekday

.. automethod:: OffsetEvent.has_fixed_duration

.. automethod:: OffsetEvent.get_duration

.. autoattribute:: OffsetEvent.end_reference_event_id

.. autoattribute:: OffsetEvent.end_reference_event

.. automethod:: OffsetEvent.has_fixed_end_offset

.. autoattribute:: OffsetEvent.fixed_end_offset

.. automethod:: OffsetEvent.has_relative_weekday_end_offset

.. autoattribute:: OffsetEvent.relative_weekday_end_offset

.. autoattribute:: OffsetEvent.relative_end_weekday

.. autoattribute:: OffsetEvent.location_description

.. automethod:: OffsetEvent.has_location

.. autoattribute:: OffsetEvent.location_id

.. autoattribute:: OffsetEvent.location

.. automethod:: OffsetEvent.has_sponsors

.. autoattribute:: OffsetEvent.sponsor_ids

.. autoattribute:: OffsetEvent.sponsors

.. automethod:: OffsetEvent.get_offset_event_record



Offset Event Form
-----------------

.. autoclass:: OffsetEventForm
   :show-inheritance:

.. autoattribute:: OffsetEventForm.fixed_start_time_metadata

.. autoattribute:: OffsetEventForm.fixed_start_time

.. autoattribute:: OffsetEventForm.start_reference_event_metadata

.. autoattribute:: OffsetEventForm.start_reference_event

.. autoattribute:: OffsetEventForm.fixed_start_offset_metadata

.. autoattribute:: OffsetEventForm.fixed_start_offset

.. autoattribute:: OffsetEventForm.relative_weekday_start_offset_metadata

.. autoattribute:: OffsetEventForm.relative_weekday_start_offset

.. autoattribute:: OffsetEventForm.relative_start_weekday_metadata

.. autoattribute:: OffsetEventForm.relative_start_weekday

.. autoattribute:: OffsetEventForm.fixed_duration_metadata

.. autoattribute:: OffsetEventForm.fixed_duration

.. autoattribute:: OffsetEventForm.end_reference_event_metadata

.. autoattribute:: OffsetEventForm.end_reference_event

.. autoattribute:: OffsetEventForm.fixed_end_offset_metadata

.. autoattribute:: OffsetEventForm.fixed_end_offset

.. autoattribute:: OffsetEventForm.relative_weekday_end_offset_metadata

.. autoattribute:: OffsetEventForm.relative_weekday_end_offset

.. autoattribute:: OffsetEventForm.relative_end_weekday_metadata

.. autoattribute:: OffsetEventForm.relative_end_weekday

.. autoattribute:: OffsetEventForm.location_description_metadata

.. autoattribute:: OffsetEventForm.location_description

.. autoattribute:: OffsetEventForm.location_metadata

.. autoattribute:: OffsetEventForm.location

.. autoattribute:: OffsetEventForm.sponsor_metadata

.. autoattribute:: OffsetEventForm.sponsors

.. automethod:: OffsetEventForm.get_offset_event_form_record



Offset Event List
-----------------

.. autoclass:: OffsetEventList
   :show-inheritance:

.. autoattribute:: OffsetEventList.next_offset_event

.. automethod:: OffsetEventList.get_next_offset_events



Schedule
--------

.. autoclass:: Schedule
   :show-inheritance:

.. autoattribute:: Schedule.schedule_slot_id

.. autoattribute:: Schedule.schedule_slot

.. automethod:: Schedule.has_time_period

.. autoattribute:: Schedule.time_period_id

.. autoattribute:: Schedule.time_period

.. autoattribute:: Schedule.schedule_start

.. autoattribute:: Schedule.schedule_end

.. automethod:: Schedule.has_limit

.. autoattribute:: Schedule.limit

.. autoattribute:: Schedule.location_description

.. automethod:: Schedule.has_location

.. autoattribute:: Schedule.location_id

.. autoattribute:: Schedule.location

.. autoattribute:: Schedule.total_duration

.. automethod:: Schedule.get_schedule_record



Schedule Form
-------------

.. autoclass:: ScheduleForm
   :show-inheritance:

.. autoattribute:: ScheduleForm.limit_metadata

.. autoattribute:: ScheduleForm.limit

.. autoattribute:: ScheduleForm.location_description

.. autoattribute:: ScheduleForm.location_metadata

.. autoattribute:: ScheduleForm.location

.. automethod:: ScheduleForm.get_schedule_slot_form_record



Schedule List
-------------

.. autoclass:: ScheduleList
   :show-inheritance:

.. autoattribute:: ScheduleList.next_schedule

.. automethod:: ScheduleList.get_next_schedules



Schedule Slot
-------------

.. autoclass:: ScheduleSlot
   :show-inheritance:

.. autoattribute:: ScheduleSlot.schedule_slot_ids

.. autoattribute:: ScheduleSlot.schedule_slots

.. automethod:: ScheduleSlot.has_weekly_interval

.. autoattribute:: ScheduleSlot.weekdays

.. automethod:: ScheduleSlot.has_week_of_month_interval

.. autoattribute:: ScheduleSlot.weekly_interval

.. autoattribute:: ScheduleSlot.week_of_month

.. autoattribute:: ScheduleSlot.weekday_time

.. automethod:: ScheduleSlot.has_fixed_interval

.. autoattribute:: ScheduleSlot.fixed_interval

.. autoattribute:: ScheduleSlot.duration

.. automethod:: ScheduleSlot.get_schedule_slot_record



Schedule Slot Form
------------------

.. autoclass:: ScheduleSlotForm
   :show-inheritance:

.. autoattribute:: ScheduleSlotForm.weekday_metadata

.. autoattribute:: ScheduleSlotForm.weekdays

.. autoattribute:: ScheduleSlotForm.weekly_interval_metadata

.. autoattribute:: ScheduleSlotForm.weekly_interval

.. autoattribute:: ScheduleSlotForm.week_of_month_metadata

.. autoattribute:: ScheduleSlotForm.week_of_the_month

.. autoattribute:: ScheduleSlotForm.weekday_time_metadata

.. autoattribute:: ScheduleSlotForm.weekday_time

.. autoattribute:: ScheduleSlotForm.weekday_schedule

.. autoattribute:: ScheduleSlotForm.fixed_interval_metadata

.. autoattribute:: ScheduleSlotForm.fixed_interval

.. automethod:: ScheduleSlotForm.ge_duration_metadata

.. autoattribute:: ScheduleSlotForm.duration

.. automethod:: ScheduleSlotForm.get_schedule_slot_form_record



Schedule Slot List
------------------

.. autoclass:: ScheduleSlotList
   :show-inheritance:

.. autoattribute:: ScheduleSlotList.next_schedule_slot

.. automethod:: ScheduleSlotList.get_next_schedule_slots



Time Period
-----------

.. autoclass:: TimePeriod
   :show-inheritance:

.. autoattribute:: TimePeriod.start

.. autoattribute:: TimePeriod.end

.. autoattribute:: TimePeriod.exception_ids

.. autoattribute:: TimePeriod.exceptions

.. automethod:: TimePeriod.get_time_period_record



Time Period Form
----------------

.. autoclass:: TimePeriodForm
   :show-inheritance:

.. autoattribute:: TimePeriodForm.start_metadata

.. autoattribute:: TimePeriodForm.start

.. autoattribute:: TimePeriodForm.end_metadata

.. autoattribute:: TimePeriodForm.end

.. automethod:: TimePeriodForm.get_time_period_form_record



Time Period List
----------------

.. autoclass:: TimePeriodList
   :show-inheritance:

.. autoattribute:: TimePeriodList.next_time_period

.. automethod:: TimePeriodList.get_next_time_periods



Commitment
----------

.. autoclass:: Commitment
   :show-inheritance:

.. autoattribute:: Commitment.event_id

.. autoattribute:: Commitment.event

.. autoattribute:: Commitment.resource_id

.. autoattribute:: Commitment.resource

.. automethod:: Commitment.get_commitment_record



Commitment Form
---------------

.. autoclass:: CommitmentForm
   :show-inheritance:

.. automethod:: CommitmentForm.get_commitment_form_record



Commitment List
---------------

.. autoclass:: CommitmentList
   :show-inheritance:

.. autoattribute:: CommitmentList.next_commitment

.. automethod:: CommitmentList.get_next_commitments



Calendar Form
-------------

.. autoclass:: CalendarForm
   :show-inheritance:

.. automethod:: CalendarForm.get_calendar_form_record



Calendar List
-------------

.. autoclass:: CalendarList
   :show-inheritance:

.. autoattribute:: CalendarList.next_calendar

.. automethod:: CalendarList.get_next_calendars



Calendar Node
-------------

.. autoclass:: CalendarNode
   :show-inheritance:

.. autoattribute:: CalendarNode.calendar

.. autoattribute:: CalendarNode.parent_calendar_nodes

.. autoattribute:: CalendarNode.child_calendar_nodes



Calendar Node List
------------------

.. autoclass:: CalendarNodeList
   :show-inheritance:

.. autoattribute:: CalendarNodeList.next_calendar_node

.. automethod:: CalendarNodeList.get_next_calendar_nodes



Meeting Time
------------

.. autoclass:: MeetingTime
   :show-inheritance:

.. autoattribute:: MeetingTime.date

.. autoattribute:: MeetingTime.location_description

.. automethod:: MeetingTime.has_location

.. autoattribute:: MeetingTime.location_id

.. autoattribute:: MeetingTime.location



Meeting Time List
-----------------

.. autoclass:: MeetingTimeList
   :show-inheritance:

.. autoattribute:: MeetingTimeList.next_meeting_time

.. automethod:: MeetingTimeList.get_next_meeting_times



Time List
---------

.. autoclass:: TimeList
   :show-inheritance:

.. autoattribute:: TimeList.next_time

.. automethod:: TimeList.get_next_times



Date Time List
--------------

.. autoclass:: DateTimeList
   :show-inheritance:

.. autoattribute:: DateTimeList.next_date_time

.. automethod:: DateTimeList.get_next_date_times



Duration List
-------------

.. autoclass:: DurationList
   :show-inheritance:

.. autoattribute:: DurationList.next_duration

.. automethod:: DurationList.get_next_durations



Date Time Interval
------------------

.. autoclass:: DateTimeInterval
   :show-inheritance:

.. autoattribute:: DateTimeInterval.start

.. autoattribute:: DateTimeInterval.end



Date Time Interval List
-----------------------

.. autoclass:: DateTimeIntervalList
   :show-inheritance:

.. autoattribute:: DateTimeIntervalList.next_date_time_interval

.. automethod:: DateTimeIntervalList.get_next_date_time_intervals



