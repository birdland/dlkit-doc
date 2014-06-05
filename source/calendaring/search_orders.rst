.. currentmodule:: dlkit.calendaring.search_orders
.. automodule:: dlkit.calendaring.search_orders

Search_Orders
=============


Event Search Order
------------------

.. autoclass:: EventSearchOrder
   :show-inheritance:

   .. automethod:: EventSearchOrder.order_by_duration

   .. automethod:: EventSearchOrder.order_by_recurring_event

   .. automethod:: EventSearchOrder.supports_recurring_event_search_order

   .. autoattribute:: EventSearchOrder.recurring_event_search_order

   .. automethod:: EventSearchOrder.order_by_superseding_event

   .. automethod:: EventSearchOrder.supports_superseding_event_search_order

   .. autoattribute:: EventSearchOrder.superseding_event_search_order

   .. automethod:: EventSearchOrder.order_by_offset_event

   .. automethod:: EventSearchOrder.supports_offset_event_search_order

   .. autoattribute:: EventSearchOrder.offset_event_search_order

   .. automethod:: EventSearchOrder.order_by_location_description

   .. automethod:: EventSearchOrder.order_by_location

   .. automethod:: EventSearchOrder.supports_location_search_order

   .. autoattribute:: EventSearchOrder.location_search_order

   .. automethod:: EventSearchOrder.get_event_search_order_record



Recurring Event Search Order
----------------------------

.. autoclass:: RecurringEventSearchOrder
   :show-inheritance:

   .. automethod:: RecurringEventSearchOrder.get_recurring_event_search_order_record



Superseding Event Search Order
------------------------------

.. autoclass:: SupersedingEventSearchOrder
   :show-inheritance:

   .. automethod:: SupersedingEventSearchOrder.order_by_superseded_event

   .. automethod:: SupersedingEventSearchOrder.supports_superseded_event_search_order

   .. autoattribute:: SupersedingEventSearchOrder.superseded_event_search_order

   .. automethod:: SupersedingEventSearchOrder.order_by_superseding_event

   .. automethod:: SupersedingEventSearchOrder.supports_superseding_event_search_order

   .. autoattribute:: SupersedingEventSearchOrder.superseding_event_search_order

   .. automethod:: SupersedingEventSearchOrder.order_by_superseded_date

   .. automethod:: SupersedingEventSearchOrder.order_by_superseded_event_position

   .. automethod:: SupersedingEventSearchOrder.get_superseding_event_search_order_record



Offset Event Search Order
-------------------------

.. autoclass:: OffsetEventSearchOrder
   :show-inheritance:

   .. automethod:: OffsetEventSearchOrder.order_by_fixed_start_time

   .. automethod:: OffsetEventSearchOrder.order_by_start_reference_event

   .. automethod:: OffsetEventSearchOrder.supports_start_reference_event_search_order

   .. autoattribute:: OffsetEventSearchOrder.start_reference_event_search_order

   .. automethod:: OffsetEventSearchOrder.order_by_fixed_start_offset

   .. automethod:: OffsetEventSearchOrder.order_by_relative_weekday_start_offset

   .. automethod:: OffsetEventSearchOrder.order_by_relative_start_weekday

   .. automethod:: OffsetEventSearchOrder.order_by_fixed_duration

   .. automethod:: OffsetEventSearchOrder.order_by_end_reference_event

   .. automethod:: OffsetEventSearchOrder.supports_end_reference_event_search_order

   .. autoattribute:: OffsetEventSearchOrder.end_reference_event_search_order

   .. automethod:: OffsetEventSearchOrder.order_by_fixed_end_offset

   .. automethod:: OffsetEventSearchOrder.order_by_relative_weekday_end_offset

   .. automethod:: OffsetEventSearchOrder.order_by_relative_end_weekday

   .. automethod:: OffsetEventSearchOrder.order_by_location_description

   .. automethod:: OffsetEventSearchOrder.order_by_location

   .. automethod:: OffsetEventSearchOrder.supports_location_search_order

   .. autoattribute:: OffsetEventSearchOrder.location_search_order

   .. automethod:: OffsetEventSearchOrder.get_offset_event_search_order_record



Schedule Search Order
---------------------

.. autoclass:: ScheduleSearchOrder
   :show-inheritance:

   .. automethod:: ScheduleSearchOrder.order_by_schedule_slot

   .. automethod:: ScheduleSearchOrder.supports_schedule_slot_search_order

   .. autoattribute:: ScheduleSearchOrder.schedule_slot_search_order

   .. automethod:: ScheduleSearchOrder.order_by_time_period

   .. automethod:: ScheduleSearchOrder.supports_time_period_search_order

   .. autoattribute:: ScheduleSearchOrder.time_period_search_order

   .. automethod:: ScheduleSearchOrder.order_by_schedule_start

   .. automethod:: ScheduleSearchOrder.order_by_schedule_end

   .. automethod:: ScheduleSearchOrder.order_by_total_duration

   .. automethod:: ScheduleSearchOrder.order_by_limit

   .. automethod:: ScheduleSearchOrder.order_by_location_description

   .. automethod:: ScheduleSearchOrder.order_by_location

   .. automethod:: ScheduleSearchOrder.supports_location_search_order

   .. autoattribute:: ScheduleSearchOrder.location_search_order

   .. automethod:: ScheduleSearchOrder.get_schedule_search_order_record



Schedule Slot Search Order
--------------------------

.. autoclass:: ScheduleSlotSearchOrder
   :show-inheritance:

   .. automethod:: ScheduleSlotSearchOrder.order_by_weekday_start

   .. automethod:: ScheduleSlotSearchOrder.order_by_weekly_interval

   .. automethod:: ScheduleSlotSearchOrder.order_by_week_of_month

   .. automethod:: ScheduleSlotSearchOrder.order_by_weekday_time

   .. automethod:: ScheduleSlotSearchOrder.order_by_fixed_interval

   .. automethod:: ScheduleSlotSearchOrder.order_by_duration

   .. automethod:: ScheduleSlotSearchOrder.get_schedule_slot_search_order_record



Time Period Search Order
------------------------

.. autoclass:: TimePeriodSearchOrder
   :show-inheritance:

   .. automethod:: TimePeriodSearchOrder.order_by_start

   .. automethod:: TimePeriodSearchOrder.order_by_end

   .. automethod:: TimePeriodSearchOrder.order_by_duration

   .. automethod:: TimePeriodSearchOrder.get_time_period_search_order_record



Commitment Search Order
-----------------------

.. autoclass:: CommitmentSearchOrder
   :show-inheritance:

   .. automethod:: CommitmentSearchOrder.order_by_event

   .. automethod:: CommitmentSearchOrder.supports_event_search_order

   .. autoattribute:: CommitmentSearchOrder.event_search_order

   .. automethod:: CommitmentSearchOrder.order_by_resource

   .. automethod:: CommitmentSearchOrder.supports_resource_search_order

   .. autoattribute:: CommitmentSearchOrder.resource_search_order

   .. automethod:: CommitmentSearchOrder.get_commitment_search_order_record



Calendar Search Order
---------------------

.. autoclass:: CalendarSearchOrder
   :show-inheritance:

   .. automethod:: CalendarSearchOrder.get_calendar_search_order_record



