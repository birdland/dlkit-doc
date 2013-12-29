.. currentmodule:: dlkit_doc.calendaring
.. automodule:: dlkit_doc.calendaring

Calendar
========


Calendar
--------

.. autoclass:: Calendar
   :show-inheritance:

.. automethod:: Calendar.get_calendar_record



Event Lookup Methods
--------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_lookup_events

.. automethod:: Calendar.use_comparative_event_view

.. automethod:: Calendar.use_plenary_event_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_effective_event_view

.. automethod:: Calendar.use_any_effective_event_view

.. automethod:: Calendar.use_normalized_event_view

.. automethod:: Calendar.use_denormalized_event_view

.. automethod:: Calendar.use_sequestered_event_view

.. automethod:: Calendar.use_unsequestered_event_view

.. automethod:: Calendar.get_event

.. automethod:: Calendar.get_events_by_ids

.. automethod:: Calendar.get_events_by_genus_type

.. automethod:: Calendar.get_events_by_parent_genus_type

.. automethod:: Calendar.get_events_by_record_type

.. automethod:: Calendar.get_events_on_date

.. automethod:: Calendar.get_events_in_date_range

.. automethod:: Calendar.get_upcoming_events

.. automethod:: Calendar.get_events_by_location

.. automethod:: Calendar.get_events_by_location_on_date

.. automethod:: Calendar.get_events_by_location_in_date_range

.. automethod:: Calendar.get_events_by_sponsor

.. automethod:: Calendar.get_events_by_sponsor_on_date

.. automethod:: Calendar.get_events_by_sponsor_in_date_range

.. autoattribute:: Calendar.events



Event Query Methods
-------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_search_events

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_normalized_event_view

.. automethod:: Calendar.use_denormalized_event_view

.. automethod:: Calendar.use_sequestered_event_view

.. automethod:: Calendar.use_unsequestered_event_view

.. autoattribute:: Calendar.event_query

.. automethod:: Calendar.get_events_by_query



Event Search Methods
--------------------

.. autoattribute:: Calendar.event_search

.. autoattribute:: Calendar.event_search_order

.. automethod:: Calendar.get_events_by_search

.. automethod:: Calendar.get_event_query_from_inspector



Event Admin Methods
-------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_create_events

.. automethod:: Calendar.can_create_event_with_record_types

.. automethod:: Calendar.get_event_form_for_create

.. automethod:: Calendar.create_event

.. automethod:: Calendar.can_update_events

.. automethod:: Calendar.get_event_form_for_update

.. automethod:: Calendar.update_event

.. automethod:: Calendar.can_delete_events

.. automethod:: Calendar.delete_event

.. automethod:: Calendar.can_manage_event_aliases

.. automethod:: Calendar.alias_event



Event Notification Methods
--------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_register_for_event_notifications

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_normalized_view

.. automethod:: Calendar.use_denormalized_view

.. automethod:: Calendar.register_for_new_events

.. automethod:: Calendar.register_for_changed_events

.. automethod:: Calendar.register_for_changed_event

.. automethod:: Calendar.register_for_deleted_events

.. automethod:: Calendar.register_for_deleted_event



Event Calendar Methods
----------------------

.. automethod:: Calendar.can_lookup_event_calendar_mappings

.. automethod:: Calendar.use_comparative_calendar_view

.. automethod:: Calendar.use_plenary_calendar_view

.. automethod:: Calendar.use_normalized_event_view

.. automethod:: Calendar.use_denormalized_event_view

.. automethod:: Calendar.get_event_ids_by_calendar

.. automethod:: Calendar.get_events_by_calendar

.. automethod:: Calendar.get_event_ids_by_calendars

.. automethod:: Calendar.get_events_by_calendars

.. automethod:: Calendar.get_calendar_ids_by_event

.. automethod:: Calendar.get_calendars_by_event



Event Calendar Assignment Methods
---------------------------------

.. automethod:: Calendar.can_assign_events

.. automethod:: Calendar.can_assign_events_to_calendar

.. automethod:: Calendar.get_assignable_calendar_ids

.. automethod:: Calendar.get_assignable_calendar_ids_for_event

.. automethod:: Calendar.assign_event_to_calendar

.. automethod:: Calendar.unassign_event_from_calendar



Event Smart Calendar Methods
----------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_manage_smart_calendars

.. autoattribute:: Calendar.event_query

.. autoattribute:: Calendar.event_search_order

.. automethod:: Calendar.apply_event_query

.. automethod:: Calendar.inspect_event_query

.. automethod:: Calendar.apply_event_sequencing

.. automethod:: Calendar.get_event_query_from_inspector



Recurring Event Lookup Methods
------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_lookup_recurring_events

.. automethod:: Calendar.use_comparative_recurring_event_view

.. automethod:: Calendar.use_plenary_recurring_event_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_sequestered_recurring_event_view

.. automethod:: Calendar.use_unsequestered_recurring_event_view

.. automethod:: Calendar.get_recurring_event

.. automethod:: Calendar.get_recurring_events_by_ids

.. automethod:: Calendar.get_recurring_events_by_genus_type

.. automethod:: Calendar.get_recurring_events_by_parent_genus_type

.. automethod:: Calendar.get_recurring_events_by_record_type

.. automethod:: Calendar.get_recurring_events_by_schedule_slot

.. autoattribute:: Calendar.recurring_events



Recurring Event Unravelling Methods
-----------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_unravel_recurring_events

.. automethod:: Calendar.use_comparative_recurring_event_view

.. automethod:: Calendar.use_plenary_recurring_event_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.get_recurring_event_by_event

.. automethod:: Calendar.get_recurring_events_by_events

.. automethod:: Calendar.expand_recurring_event

.. automethod:: Calendar.expand_recurring_event_in_date_range

.. automethod:: Calendar.expand_recurring_events

.. automethod:: Calendar.expand_recurring_events_in_date_range

.. automethod:: Calendar.get_recurring_events_by_date

.. automethod:: Calendar.get_recurring_events_in_date_range

.. automethod:: Calendar.get_number_of_events

.. automethod:: Calendar.get_number_of_events_in_date_range



Recurring Event Query Methods
-----------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_search_recurring_events

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. autoattribute:: Calendar.recurring_event_query

.. automethod:: Calendar.get_recurring_events_by_query



Recurring Event Search Methods
------------------------------

.. autoattribute:: Calendar.recurring_event_search

.. autoattribute:: Calendar.recurring_event_search_order

.. automethod:: Calendar.get_recurring_events_by_search

.. automethod:: Calendar.get_recurring_event_query_from_inspector



Recurring Event Admin Methods
-----------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_create_recurring_events

.. automethod:: Calendar.can_create_recurring_event_with_record_types

.. automethod:: Calendar.get_recurring_event_form_for_create

.. automethod:: Calendar.create_recurring_event

.. automethod:: Calendar.can_update_recurring_events

.. automethod:: Calendar.get_recurring_event_form_for_update

.. automethod:: Calendar.update_recurring_event

.. automethod:: Calendar.can_delete_recurring_events

.. automethod:: Calendar.delete_recurring_event

.. automethod:: Calendar.can_manage_recurring_event_aliases

.. automethod:: Calendar.alias_recurring_event

.. automethod:: Calendar.can_schedule_recurring_events

.. automethod:: Calendar.add_schedule

.. automethod:: Calendar.remove_schedule

.. automethod:: Calendar.add_specific_date

.. automethod:: Calendar.add_specific_date_with_location

.. automethod:: Calendar.clear_specific_dates

.. automethod:: Calendar.add_event

.. automethod:: Calendar.remove_event

.. automethod:: Calendar.add_blackout

.. automethod:: Calendar.clear_blackout



Recurring Event Notification Methods
------------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_register_for_recurring_event_notifications

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.register_for_new_recurring_events

.. automethod:: Calendar.register_for_changed_recurring_events

.. automethod:: Calendar.register_for_changed_recurring_event

.. automethod:: Calendar.register_for_deleted_recurring_events

.. automethod:: Calendar.register_for_deleted_recurring_event



Recurring Event Calendar Methods
--------------------------------

.. automethod:: Calendar.can_lookup_recurring_event_calendar_mappings

.. automethod:: Calendar.use_comparative_calendar_view

.. automethod:: Calendar.use_plenary_calendar_view

.. automethod:: Calendar.get_recurring_event_ids_by_calendar

.. automethod:: Calendar.get_recurring_events_by_calendar

.. automethod:: Calendar.get_recurring_event_ids_by_calendars

.. automethod:: Calendar.get_recurring_events_by_calendars

.. automethod:: Calendar.get_calendar_ids_by_recurring_event

.. automethod:: Calendar.get_calendars_by_recurring_event



Recurring Event Calendar Assignment Methods
-------------------------------------------

.. automethod:: Calendar.can_assign_recurring_events

.. automethod:: Calendar.can_assign_recurring_events_to_calendar

.. automethod:: Calendar.get_assignable_calendar_ids

.. automethod:: Calendar.get_assignable_calendar_ids_for_recurring_event

.. automethod:: Calendar.assign_recurring_event_to_calendar

.. automethod:: Calendar.unassign_recurring_event_from_calendar



Recurring Event Smart Calendar Methods
--------------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_manage_smart_calendars

.. autoattribute:: Calendar.recurring_event_query

.. autoattribute:: Calendar.recurring_event_search_order

.. automethod:: Calendar.apply_recurring_event_query

.. automethod:: Calendar.inspect_recurring_event_query

.. automethod:: Calendar.apply_recurring_event_sequencing

.. automethod:: Calendar.get_recurring_event_query_from_inspector



Superseding Event Lookup Methods
--------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_lookup_superseding_events

.. automethod:: Calendar.use_comparative_superseding_event_view

.. automethod:: Calendar.use_plenary_superseding_event_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_active_superseding_event_view

.. automethod:: Calendar.use_any_status_superseding_event_view

.. automethod:: Calendar.get_superseding_event

.. automethod:: Calendar.get_superseding_events_by_ids

.. automethod:: Calendar.get_superseding_events_by_genus_type

.. automethod:: Calendar.get_superseding_events_by_parent_genus_type

.. automethod:: Calendar.get_superseding_events_by_record_type

.. automethod:: Calendar.get_superseding_events_by_superseded_event

.. autoattribute:: Calendar.superseding_events



Superseding Event Query Methods
-------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_search_superseding_events

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. autoattribute:: Calendar.superseding_event_query

.. automethod:: Calendar.get_superseding_events_by_query



Superseding Event Search Methods
--------------------------------

.. autoattribute:: Calendar.superseding_event_search

.. autoattribute:: Calendar.superseding_event_search_order

.. automethod:: Calendar.get_superseding_events_by_search

.. automethod:: Calendar.get_superseding_event_query_from_inspector



Superseding Event Admin Methods
-------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_create_superseding_events

.. automethod:: Calendar.can_create_superseding_event_with_record_types

.. automethod:: Calendar.get_superseding_event_form_for_create

.. automethod:: Calendar.create_superseding_event

.. automethod:: Calendar.can_update_superseding_events

.. automethod:: Calendar.get_superseding_event_form_for_update

.. automethod:: Calendar.update_superseding_event

.. automethod:: Calendar.can_delete_superseding_events

.. automethod:: Calendar.delete_superseding_event

.. automethod:: Calendar.can_manage_superseding_event_aliases

.. automethod:: Calendar.alias_superseding_event



Superseding Event Notification Methods
--------------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_register_for_superseding_event_notifications

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.register_for_new_superseding_events

.. automethod:: Calendar.register_for_changed_superseding_events

.. automethod:: Calendar.register_for_changed_superseding_event

.. automethod:: Calendar.register_for_deleted_superseding_events

.. automethod:: Calendar.register_for_deleted_superseding_event



Superseding Event Calendar Methods
----------------------------------

.. automethod:: Calendar.can_lookup_superseding_event_calendar_mappings

.. automethod:: Calendar.use_comparative_calendar_view

.. automethod:: Calendar.use_plenary_calendar_view

.. automethod:: Calendar.get_superseding_event_ids_by_calendar

.. automethod:: Calendar.get_superseding_events_by_calendar

.. automethod:: Calendar.get_superseding_event_ids_by_calendars

.. automethod:: Calendar.get_superseding_events_by_calendars

.. automethod:: Calendar.get_superseding_ids_by_recurring_event

.. automethod:: Calendar.get_calendars_by_superseding_event



Superseding Event Calendar Assignment Methods
---------------------------------------------

.. automethod:: Calendar.can_assign_superseding_events

.. automethod:: Calendar.can_assign_superseding_events_to_calendar

.. automethod:: Calendar.get_assignable_calendar_ids

.. automethod:: Calendar.get_assignable_calendar_ids_for_superseding_event

.. automethod:: Calendar.assign_superseding_event_to_calendar

.. automethod:: Calendar.unassign_superseding_event_from_calendar



Superseding Event Smart Calendar Methods
----------------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_manage_smart_calendars

.. autoattribute:: Calendar.superseding_event_query

.. autoattribute:: Calendar.superseding_event_search_order

.. automethod:: Calendar.apply_superseding_event_query

.. automethod:: Calendar.inspect_superseding_event_query

.. automethod:: Calendar.apply_superseding_event_sequencing

.. automethod:: Calendar.get_superseding_event_query_from_inspector



Offset Event Lookup Methods
---------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_lookup_offset_events

.. automethod:: Calendar.use_comparative_offset_event_view

.. automethod:: Calendar.use_plenary_offset_event_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_active_offset_event_view

.. automethod:: Calendar.use_any_status_offset_event_view

.. automethod:: Calendar.get_offset_event

.. automethod:: Calendar.get_offset_events_by_ids

.. automethod:: Calendar.get_offset_events_by_genus_type

.. automethod:: Calendar.get_offset_events_by_parent_genus_type

.. automethod:: Calendar.get_offset_events_by_record_type

.. automethod:: Calendar.get_offset_events_by_event

.. autoattribute:: Calendar.offset_events



Offset Event Query Methods
--------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_search_offset_events

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. autoattribute:: Calendar.offset_event_query

.. automethod:: Calendar.get_offset_events_by_query



Offset Event Search Methods
---------------------------

.. autoattribute:: Calendar.offset_event_search

.. autoattribute:: Calendar.offset_event_search_order

.. automethod:: Calendar.get_offset_events_by_search

.. automethod:: Calendar.get_offset_event_query_from_inspector



Offset Event Admin Methods
--------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_create_offset_events

.. automethod:: Calendar.can_create_offset_event_with_record_types

.. automethod:: Calendar.get_offset_event_form_for_create

.. automethod:: Calendar.create_offset_event

.. automethod:: Calendar.can_update_offset_events

.. automethod:: Calendar.get_offset_event_form_for_update

.. automethod:: Calendar.update_offset_event

.. automethod:: Calendar.can_delete_offset_events

.. automethod:: Calendar.delete_offset_event

.. automethod:: Calendar.can_manage_offset_event_aliases

.. automethod:: Calendar.alias_offset_event



Offset Event Notification Methods
---------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_register_for_offset_event_notifications

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.register_for_new_offset_events

.. automethod:: Calendar.register_for_changed_offset_events

.. automethod:: Calendar.register_for_changed_offset_event

.. automethod:: Calendar.register_for_deleted_offset_events

.. automethod:: Calendar.register_for_deleted_offset_event



Offset Event Calendar Methods
-----------------------------

.. automethod:: Calendar.can_lookup_event_calendar_mappings

.. automethod:: Calendar.use_comparative_calendar_view

.. automethod:: Calendar.use_plenary_calendar_view

.. automethod:: Calendar.get_offset_event_ids_by_calendar

.. automethod:: Calendar.get_offset_events_by_calendar

.. automethod:: Calendar.get_offset_event_ids_by_calendars

.. automethod:: Calendar.get_offset_events_by_calendars

.. automethod:: Calendar.get_calendar_ids_by_offset_event

.. automethod:: Calendar.get_calendars_by_offset_event



Offset Event Calendar Assignment Methods
----------------------------------------

.. automethod:: Calendar.can_assign_offset_events

.. automethod:: Calendar.can_assign_offset_events_to_calendar

.. automethod:: Calendar.get_assignable_calendar_ids

.. automethod:: Calendar.get_assignable_calendar_ids_for_offset_event

.. automethod:: Calendar.assign_offset_event_to_calendar

.. automethod:: Calendar.unassign_offset_event_from_calendar



Offset Event Smart Calendar Methods
-----------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_manage_smart_calendars

.. autoattribute:: Calendar.offset_event_query

.. autoattribute:: Calendar.offset_event_search_order

.. automethod:: Calendar.apply_offset_event_query

.. automethod:: Calendar.inspect_offset_event_query

.. automethod:: Calendar.apply_offset_event_sequencing

.. automethod:: Calendar.get_offset_event_query_from_inspector



Schedule Lookup Methods
-----------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_lookup_schedules

.. automethod:: Calendar.use_comparative_schedule_view

.. automethod:: Calendar.use_plenary_schedule_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.get_schedule

.. automethod:: Calendar.get_schedules_by_ids

.. automethod:: Calendar.get_schedules_by_genus_type

.. automethod:: Calendar.get_schedules_by_parent_genus_type

.. automethod:: Calendar.get_schedules_by_record_type

.. automethod:: Calendar.get_schedules_for_location

.. automethod:: Calendar.get_schedules_by_date

.. automethod:: Calendar.get_schedules_by_date_range

.. autoattribute:: Calendar.schedules



Schedule Query Methods
----------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_search_schedules

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. autoattribute:: Calendar.schedule_query

.. automethod:: Calendar.get_schedules_by_query



Schedule Search Methods
-----------------------

.. autoattribute:: Calendar.schedule_search

.. autoattribute:: Calendar.schedule_search_order

.. automethod:: Calendar.get_schedules_by_search

.. automethod:: Calendar.get_schedule_query_from_inspector



Schedule Admin Methods
----------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_create_schedules

.. automethod:: Calendar.can_create_schedule_with_record_types

.. automethod:: Calendar.get_schedule_form_for_create

.. automethod:: Calendar.create_schedule

.. automethod:: Calendar.create_adhoc_schedule

.. automethod:: Calendar.can_update_schedules

.. automethod:: Calendar.get_schedule_form_for_update

.. automethod:: Calendar.update_schedule

.. automethod:: Calendar.update_adhoc_schedule

.. automethod:: Calendar.can_delete_schedules

.. automethod:: Calendar.delete_schedule

.. automethod:: Calendar.can_manage_schedule_aliases

.. automethod:: Calendar.alias_schedule



Schedule Notification Methods
-----------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_register_for_schedule_notifications

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.register_for_new_schedules

.. automethod:: Calendar.register_for_changed_schedules

.. automethod:: Calendar.register_for_changed_schedule

.. automethod:: Calendar.register_for_deleted_schedules

.. automethod:: Calendar.register_for_deleted_schedule



Schedule Calendar Methods
-------------------------

.. automethod:: Calendar.can_lookup_schedule_calendar_mappings

.. automethod:: Calendar.use_comparative_calendar_view

.. automethod:: Calendar.use_plenary_calendar_view

.. automethod:: Calendar.get_schedule_ids_by_calendar

.. automethod:: Calendar.get_schedules_by_calendar

.. automethod:: Calendar.get_schedule_ids_by_calendars

.. automethod:: Calendar.get_schedules_by_calendars

.. automethod:: Calendar.get_calendar_ids_by_schedule

.. automethod:: Calendar.get_calendars_by_schedule



Schedule Calendar Assignment Methods
------------------------------------

.. automethod:: Calendar.can_assign_schedules

.. automethod:: Calendar.can_assign_schedules_to_calendar

.. automethod:: Calendar.get_assignable_calendar_ids

.. automethod:: Calendar.get_assignable_calendar_ids_for_schedule

.. automethod:: Calendar.assign_schedule_to_calendar

.. automethod:: Calendar.unassign_schedule_from_calendar



Schedule Smart Calendar Methods
-------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_manage_smart_calendars

.. autoattribute:: Calendar.schedule_query

.. autoattribute:: Calendar.schedule_search_order

.. automethod:: Calendar.apply_schedule_query

.. automethod:: Calendar.inspect_schedule_query

.. automethod:: Calendar.apply_schedule_sequencing

.. automethod:: Calendar.get_schedule_query_from_inspector



Schedule Slot Lookup Methods
----------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_lookup_schedule_slots

.. automethod:: Calendar.use_comparative_schedule_slot_view

.. automethod:: Calendar.use_plenary_schedule_slot_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_sequestered_schedule_slot_view

.. automethod:: Calendar.use_unsequestered_schedule_slot_view

.. automethod:: Calendar.get_schedule_slot

.. automethod:: Calendar.get_schedule_slots_by_ids

.. automethod:: Calendar.get_schedule_slots_by_genus_type

.. automethod:: Calendar.get_schedule_slots_by_parent_genus_type

.. automethod:: Calendar.get_schedule_slots_by_record_type

.. automethod:: Calendar.get_schedule_slots_by_weekdays

.. automethod:: Calendar.get_schedule_slots_by_time

.. autoattribute:: Calendar.schedule_slots



Schedule Slot Query Methods
---------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_search_schedule_slots

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_sequestered_schedule_slot_view

.. automethod:: Calendar.use_unsequestered_schedule_slot_view

.. autoattribute:: Calendar.schedule_slot_query

.. automethod:: Calendar.get_schedule_slots_by_query



Schedule Slot Search Methods
----------------------------

.. autoattribute:: Calendar.schedule_slot_search

.. autoattribute:: Calendar.schedule_slot_search_order

.. automethod:: Calendar.get_schedule_slots_by_search

.. automethod:: Calendar.get_schedule_slot_query_from_inspector



Schedule Slot Admin Methods
---------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_create_schedule_slots

.. automethod:: Calendar.can_create_schedule_slot_with_record_types

.. automethod:: Calendar.get_schedule_slot_form_for_create

.. automethod:: Calendar.create_schedule_slot

.. automethod:: Calendar.can_update_schedule_slots

.. automethod:: Calendar.get_schedule_slot_form_for_update

.. automethod:: Calendar.update_schedule_slot

.. automethod:: Calendar.can_delete_schedule_slots

.. automethod:: Calendar.delete_schedule_slot

.. automethod:: Calendar.can_manage_schedule_slot_aliases

.. automethod:: Calendar.alias_schedule_slot



Schedule Slot Notification Methods
----------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_register_for_schedule_slot_notifications

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.register_for_new_schedule_slots

.. automethod:: Calendar.register_for_new_schedule_slot_ancestors

.. automethod:: Calendar.register_for_new_schedule_slot_descendants

.. automethod:: Calendar.register_for_changed_schedule_slots

.. automethod:: Calendar.register_for_changed_schedule_slot

.. automethod:: Calendar.register_for_deleted_schedule_slots

.. automethod:: Calendar.register_for_deleted_schedule_slot

.. automethod:: Calendar.register_for_deleted_schedule_slot_ancestors

.. automethod:: Calendar.register_for_deleted_schedule_slot_descendants



Schedule Slot Calendar Methods
------------------------------

.. automethod:: Calendar.can_lookup_schedule_slot_calendar_mappings

.. automethod:: Calendar.use_comparative_calendar_view

.. automethod:: Calendar.use_plenary_calendar_view

.. automethod:: Calendar.get_schedule_slot_ids_by_calendar

.. automethod:: Calendar.get_schedule_slots_by_calendar

.. automethod:: Calendar.get_schedule_slot_ids_by_calendars

.. automethod:: Calendar.get_schedule_slots_by_calendars

.. automethod:: Calendar.get_calendar_ids_by_schedule_slot

.. automethod:: Calendar.get_calendars_by_schedule_slot



Schedule Slot Calendar Assignment Methods
-----------------------------------------

.. automethod:: Calendar.can_assign_schedule_slots

.. automethod:: Calendar.can_assign_schedule_slots_to_calendar

.. automethod:: Calendar.get_assignable_calendar_ids

.. automethod:: Calendar.get_assignable_calendar_ids_for_schedule_slot

.. automethod:: Calendar.assign_schedule_slot_to_calendar

.. automethod:: Calendar.unassign_schedule_slot_from_calendar



Schedule Slot Smart Calendar Methods
------------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_manage_smart_calendars

.. autoattribute:: Calendar.schedule_slot_query

.. autoattribute:: Calendar.schedule_slot_search_order

.. automethod:: Calendar.apply_schedule_slot_query

.. automethod:: Calendar.inspect_schedule_slot_query

.. automethod:: Calendar.apply_schedule_slot_sequencing

.. automethod:: Calendar.get_schedule_slot_query_from_inspector



Commitment Lookup Methods
-------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_lookup_commitments

.. automethod:: Calendar.use_comparative_commitment_view

.. automethod:: Calendar.use_plenary_commitment_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.use_effective_commitment_view

.. automethod:: Calendar.use_any_effective_commitment_view

.. automethod:: Calendar.get_commitment

.. automethod:: Calendar.get_commitments_by_ids

.. automethod:: Calendar.get_commitments_by_genus_type

.. automethod:: Calendar.get_commitments_by_parent_genus_type

.. automethod:: Calendar.get_commitments_by_record_type

.. automethod:: Calendar.get_commitments_on_date

.. automethod:: Calendar.get_commitments_by_genus_type_on_date

.. automethod:: Calendar.get_commitments_for_event

.. automethod:: Calendar.get_commitments_for_event_on_date

.. automethod:: Calendar.get_commitments_by_genus_type_for_event

.. automethod:: Calendar.get_commitments_by_genus_type_for_event_on_date

.. automethod:: Calendar.get_commitments_for_resource

.. automethod:: Calendar.get_commitments_for_resource_on_date

.. automethod:: Calendar.get_commitments_by_genus_type_for_resource

.. automethod:: Calendar.get_commitments_by_genus_type_for_resource_on_date

.. automethod:: Calendar.get_commitments_for_event_and_resource

.. automethod:: Calendar.get_commitments_for_event_and_resource_on_date

.. automethod:: Calendar.get_commitments_by_genus_type_for_event_and_resource

.. automethod:: Calendar.get_commitments_by_genus_type_for_event_and_resource_on_date

.. autoattribute:: Calendar.commitments



Commitment Query Methods
------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_search_commitments

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. autoattribute:: Calendar.commitment_query

.. automethod:: Calendar.get_commitments_by_query



Commitment Search Methods
-------------------------

.. autoattribute:: Calendar.commitment_search

.. autoattribute:: Calendar.commitment_search_order

.. automethod:: Calendar.get_commitments_by_search

.. automethod:: Calendar.get_commitment_query_from_inspector



Commitment Admin Methods
------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_create_commitments

.. automethod:: Calendar.can_create_commitment_with_record_types

.. automethod:: Calendar.get_commitment_form_for_create

.. automethod:: Calendar.create_commitment

.. automethod:: Calendar.can_update_commitments

.. automethod:: Calendar.get_commitment_form_for_update

.. automethod:: Calendar.update_commitment

.. automethod:: Calendar.can_delete_commitments

.. automethod:: Calendar.delete_commitment

.. automethod:: Calendar.can_manage_commitment_aliases

.. automethod:: Calendar.alias_commitment



Commitment Notification Methods
-------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_register_for_commitment_notifications

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.register_for_new_commitments

.. automethod:: Calendar.register_for_new_commitments_by_genus_type

.. automethod:: Calendar.register_for_new_commitments_for_event

.. automethod:: Calendar.register_for_new_commitments_for_resource

.. automethod:: Calendar.register_for_changed_commitments

.. automethod:: Calendar.register_for_changed_commitments_by_genus_type

.. automethod:: Calendar.register_for_changed_commitments_for_event

.. automethod:: Calendar.register_for_changed_commitments_for_resource

.. automethod:: Calendar.register_for_changed_commitment

.. automethod:: Calendar.register_for_deleted_commitments

.. automethod:: Calendar.register_for_deleted_commitments_by_genus_type

.. automethod:: Calendar.register_for_deleted_commitments_for_event

.. automethod:: Calendar.register_for_deleted_commitments_for_resource

.. automethod:: Calendar.register_for_deleted_commitment



Commitment Calendar Methods
---------------------------

.. automethod:: Calendar.can_lookup_commitment_calendar_mappings

.. automethod:: Calendar.use_comparative_calendar_view

.. automethod:: Calendar.use_plenary_calendar_view

.. automethod:: Calendar.get_commitment_ids_by_calendar

.. automethod:: Calendar.get_commitments_by_calendar

.. automethod:: Calendar.get_commitment_ids_by_calendars

.. automethod:: Calendar.get_commitments_by_calendars

.. automethod:: Calendar.get_calendar_ids_by_commitment

.. automethod:: Calendar.get_calendars_by_commitment



Commitment Calendar Assignment Methods
--------------------------------------

.. automethod:: Calendar.can_assign_commitments

.. automethod:: Calendar.can_assign_commitments_to_calendar

.. automethod:: Calendar.get_assignable_calendar_ids

.. automethod:: Calendar.get_assignable_calendar_ids_for_commitment

.. automethod:: Calendar.assign_commitment_to_calendar

.. automethod:: Calendar.unassign_commitment_from_calendar



Commitment Smart Calendar Methods
---------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_manage_smart_calendars

.. autoattribute:: Calendar.commitment_query

.. autoattribute:: Calendar.commitment_search_order

.. automethod:: Calendar.apply_commitment_query

.. automethod:: Calendar.inspect_commitment_query

.. automethod:: Calendar.apply_commitment_sequencing

.. automethod:: Calendar.get_commitment_query_from_inspector



Time Period Lookup Methods
--------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_lookup_time_periods

.. automethod:: Calendar.use_comparative_time_period_view

.. automethod:: Calendar.use_plenary_time_period_view

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.get_time_period

.. automethod:: Calendar.get_time_periods_by_ids

.. automethod:: Calendar.get_time_periods_by_genus_type

.. automethod:: Calendar.get_time_periods_by_parent_genus_type

.. automethod:: Calendar.get_time_periods_by_record_type

.. automethod:: Calendar.get_time_periods_by_date

.. automethod:: Calendar.get_time_periods_in_date_range

.. autoattribute:: Calendar.time_periods



Time Period Query Methods
-------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_search_time_periods

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. autoattribute:: Calendar.time_period_query

.. automethod:: Calendar.get_time_periods_by_query



Time Period Search Methods
--------------------------

.. autoattribute:: Calendar.time_period_search

.. autoattribute:: Calendar.time_period_search_order

.. automethod:: Calendar.get_time_periods_by_search

.. automethod:: Calendar.get_time_period_query_from_inspector



Time Period Admin Methods
-------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_create_time_periods

.. automethod:: Calendar.can_create_time_period_with_record_types

.. automethod:: Calendar.get_time_period_form_for_create

.. automethod:: Calendar.create_time_period

.. automethod:: Calendar.can_update_time_periods

.. automethod:: Calendar.get_time_period_form_for_update

.. automethod:: Calendar.update_time_period

.. automethod:: Calendar.can_delete_time_periods

.. automethod:: Calendar.delete_time_period

.. automethod:: Calendar.can_manage_time_period_aliases

.. automethod:: Calendar.alias_time_period

.. automethod:: Calendar.add_exception_event

.. automethod:: Calendar.remove_exception_event



Time Period Notification Methods
--------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_register_for_time_period_notifications

.. automethod:: Calendar.use_federated_calendar_view

.. automethod:: Calendar.use_isolated_calendar_view

.. automethod:: Calendar.register_for_new_time_periods

.. automethod:: Calendar.register_for_changed_time_periods

.. automethod:: Calendar.register_for_changed_time_period

.. automethod:: Calendar.register_for_deleted_time_periods

.. automethod:: Calendar.register_for_deleted_time_period



Time Period Calendar Methods
----------------------------

.. automethod:: Calendar.can_lookup_time_period_calendar_mappings

.. automethod:: Calendar.use_comparative_calendar_view

.. automethod:: Calendar.use_plenary_calendar_view

.. automethod:: Calendar.get_time_period_ids_by_calendar

.. automethod:: Calendar.get_time_periods_by_calendar

.. automethod:: Calendar.get_time_period_ids_by_calendars

.. automethod:: Calendar.get_time_periods_by_calendars

.. automethod:: Calendar.get_calendar_ids_by_time_period

.. automethod:: Calendar.get_calendars_by_time_period



Time Period Calendar Assignment Methods
---------------------------------------

.. automethod:: Calendar.can_assign_time_periods

.. automethod:: Calendar.can_assign_time_periods_to_calendar

.. automethod:: Calendar.get_assignable_calendar_ids

.. automethod:: Calendar.get_assignable_calendar_ids_for_time_period

.. automethod:: Calendar.assign_time_period_to_calendar

.. automethod:: Calendar.unassign_time_period_from_calendar



Time Period Smart Calendar Methods
----------------------------------

.. autoattribute:: Calendar.calendar_id

.. autoattribute:: Calendar.calendar

.. automethod:: Calendar.can_manage_smart_calendars

.. autoattribute:: Calendar.time_period_query

.. autoattribute:: Calendar.time_period_search_order

.. automethod:: Calendar.apply_time_period_query

.. automethod:: Calendar.inspect_time_period_query

.. automethod:: Calendar.apply_time_period_sequencing

.. automethod:: Calendar.get_time_period_query_from_inspector



