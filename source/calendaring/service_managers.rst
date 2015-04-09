Summary
=======
.. currentmodule:: dlkit.services.calendaring
.. automodule:: dlkit.services.calendaring

Service Managers
================


Calendaring Manager
-------------------

.. autoclass:: CalendaringManager
   :show-inheritance:

   .. autoattribute:: CalendaringManager.calandaring_batch_manager

   .. autoattribute:: CalendaringManager.calandaring_cycle_manager

   .. autoattribute:: CalendaringManager.calandaring_rules_manager



Calendaring Profile Methods
___________________

   .. automethod:: CalendaringManager.supports_visible_federation

   .. automethod:: CalendaringManager.supports_event_lookup

   .. automethod:: CalendaringManager.supports_event_query

   .. automethod:: CalendaringManager.supports_event_search

   .. automethod:: CalendaringManager.supports_event_admin

   .. automethod:: CalendaringManager.supports_event_notification

   .. automethod:: CalendaringManager.supports_event_calendar

   .. automethod:: CalendaringManager.supports_event_calendar_assignment

   .. automethod:: CalendaringManager.supports_event_smart_calendar

   .. automethod:: CalendaringManager.supports_recurring_event_lookup

   .. automethod:: CalendaringManager.supports_recurring_event_unravelling

   .. automethod:: CalendaringManager.supports_recurring_event_query

   .. automethod:: CalendaringManager.supports_recurring_event_search

   .. automethod:: CalendaringManager.supports_recurring_event_admin

   .. automethod:: CalendaringManager.supports_recurring_event_notification

   .. automethod:: CalendaringManager.supports_recurring_event_calendar

   .. automethod:: CalendaringManager.supports_recurring_event_calendar_assignment

   .. automethod:: CalendaringManager.supports_recurring_event_smart_calendar

   .. automethod:: CalendaringManager.supports_superseding_event_lookup

   .. automethod:: CalendaringManager.supports_superseding_event_query

   .. automethod:: CalendaringManager.supports_superseding_event_search

   .. automethod:: CalendaringManager.supports_superseding_event_admin

   .. automethod:: CalendaringManager.supports_superseding_event_notification

   .. automethod:: CalendaringManager.supports_superseding_event_calendar

   .. automethod:: CalendaringManager.supports_superseding_event_calendar_assignment

   .. automethod:: CalendaringManager.supports_superseding_event_smart_calendar

   .. automethod:: CalendaringManager.supports_offset_event_lookup

   .. automethod:: CalendaringManager.supports_offset_event_query

   .. automethod:: CalendaringManager.supports_offset_event_search

   .. automethod:: CalendaringManager.supports_offset_event_admin

   .. automethod:: CalendaringManager.supports_offset_event_notification

   .. automethod:: CalendaringManager.supports_offset_event_calendar

   .. automethod:: CalendaringManager.supports_offset_event_calendar_assignment

   .. automethod:: CalendaringManager.supports_offset_event_smart_calendar

   .. automethod:: CalendaringManager.supports_schedule_lookup

   .. automethod:: CalendaringManager.supports_schedule_query

   .. automethod:: CalendaringManager.supports_schedule_search

   .. automethod:: CalendaringManager.supports_schedule_admin

   .. automethod:: CalendaringManager.supports_schedule_notification

   .. automethod:: CalendaringManager.supports_schedule_calendar

   .. automethod:: CalendaringManager.supports_schedule_calendar_assignment

   .. automethod:: CalendaringManager.supports_schedule_smart_calendar

   .. automethod:: CalendaringManager.supports_schedule_slot_lookup

   .. automethod:: CalendaringManager.supports_schedule_slot_query

   .. automethod:: CalendaringManager.supports_schedule_slot_search

   .. automethod:: CalendaringManager.supports_schedule_slot_admin

   .. automethod:: CalendaringManager.supports_schedule_slot_notification

   .. automethod:: CalendaringManager.supports_schedule_slot_calendar

   .. automethod:: CalendaringManager.supports_schedule_slot_calendar_assignment

   .. automethod:: CalendaringManager.supports_schedule_slot_smart_calendar

   .. automethod:: CalendaringManager.supports_commitment_lookup

   .. automethod:: CalendaringManager.supports_commitment_query

   .. automethod:: CalendaringManager.supports_commitment_search

   .. automethod:: CalendaringManager.supports_commitment_admin

   .. automethod:: CalendaringManager.supports_commitment_notification

   .. automethod:: CalendaringManager.supports_commitment_calendar

   .. automethod:: CalendaringManager.supports_commitment_calendar_assignment

   .. automethod:: CalendaringManager.supports_commitment_smart_calendar

   .. automethod:: CalendaringManager.supports_time_period_lookup

   .. automethod:: CalendaringManager.supports_time_period_search

   .. automethod:: CalendaringManager.supports_time_period_admin

   .. automethod:: CalendaringManager.supports_time_period_notification

   .. automethod:: CalendaringManager.supports_time_period_calendar

   .. automethod:: CalendaringManager.supports_time_period_calendar_assignment

   .. automethod:: CalendaringManager.supports_time_period_smart_calendar

   .. automethod:: CalendaringManager.supports_calendar_lookup

   .. automethod:: CalendaringManager.supports_calendar_search

   .. automethod:: CalendaringManager.supports_calendar_admin

   .. automethod:: CalendaringManager.supports_calendar_notification

   .. automethod:: CalendaringManager.supports_calendar_hierarchy

   .. automethod:: CalendaringManager.supports_calendar_hierarchy_design

   .. automethod:: CalendaringManager.supports_calendaring_batch

   .. automethod:: CalendaringManager.supports_calendaring_cycle

   .. automethod:: CalendaringManager.supports_calendaring_rules

   .. autoattribute:: CalendaringManager.event_record_types

   .. automethod:: CalendaringManager.supports_event_record_type

   .. autoattribute:: CalendaringManager.event_search_record_types

   .. automethod:: CalendaringManager.supports_event_search_record_type

   .. autoattribute:: CalendaringManager.recurring_event_record_types

   .. automethod:: CalendaringManager.supports_recurring_event_record_type

   .. autoattribute:: CalendaringManager.recurring_event_search_record_types

   .. automethod:: CalendaringManager.supports_recurring_event_search_record_type

   .. autoattribute:: CalendaringManager.superseding_event_record_types

   .. automethod:: CalendaringManager.supports_superseding_event_record_type

   .. autoattribute:: CalendaringManager.superseding_event_search_record_types

   .. automethod:: CalendaringManager.supports_superseding_event_search_record_type

   .. autoattribute:: CalendaringManager.offset_event_record_types

   .. automethod:: CalendaringManager.supports_offset_event_record_type

   .. autoattribute:: CalendaringManager.offset_event_search_record_types

   .. automethod:: CalendaringManager.supports_offset_event_search_record_type

   .. autoattribute:: CalendaringManager.schedule_record_types

   .. automethod:: CalendaringManager.supports_schedule_record_type

   .. autoattribute:: CalendaringManager.schedule_search_record_types

   .. automethod:: CalendaringManager.supports_schedule_search_record_type

   .. autoattribute:: CalendaringManager.schedule_slot_record_types

   .. automethod:: CalendaringManager.supports_schedule_slot_record_type

   .. autoattribute:: CalendaringManager.schedule_slot_search_record_types

   .. automethod:: CalendaringManager.supports_schedule_slot_search_record_type

   .. autoattribute:: CalendaringManager.time_period_record_types

   .. automethod:: CalendaringManager.supports_time_period_record_type

   .. autoattribute:: CalendaringManager.time_period_search_record_types

   .. automethod:: CalendaringManager.supports_time_period_search_record_type

   .. autoattribute:: CalendaringManager.commitment_record_types

   .. automethod:: CalendaringManager.supports_commitment_record_type

   .. autoattribute:: CalendaringManager.commitment_search_record_types

   .. automethod:: CalendaringManager.supports_commitment_search_record_type

   .. autoattribute:: CalendaringManager.calendar_record_types

   .. automethod:: CalendaringManager.supports_calendar_record_type

   .. autoattribute:: CalendaringManager.calendar_search_record_types

   .. automethod:: CalendaringManager.supports_calendar_search_record_type

   .. autoattribute:: CalendaringManager.spatial_unit_record_types

   .. automethod:: CalendaringManager.supports_spatial_unit_record_type

   .. autoattribute:: CalendaringManager.coordinate_record_types

   .. automethod:: CalendaringManager.supports_coordinate_record_type



Calendar Lookup
_______________

   .. automethod:: CalendaringManager.can_lookup_calendars

   .. automethod:: CalendaringManager.use_comparative_calendar_view

   .. automethod:: CalendaringManager.use_plenary_calendar_view

   .. automethod:: CalendaringManager.get_calendar

   .. automethod:: CalendaringManager.get_calendars_by_ids

   .. automethod:: CalendaringManager.get_calendars_by_genus_type

   .. automethod:: CalendaringManager.get_calendars_by_parent_genus_type

   .. automethod:: CalendaringManager.get_calendars_by_record_type

   .. automethod:: CalendaringManager.get_calendars_by_provider

   .. autoattribute:: CalendaringManager.calendars



Calendar Query
______________

   .. automethod:: CalendaringManager.can_search_calendars

   .. autoattribute:: CalendaringManager.calendar_query

   .. automethod:: CalendaringManager.get_calendars_by_query



Calendar Search
_______________

   .. automethod:: CalendaringManager.can_search_calendars

   .. autoattribute:: CalendaringManager.calendar_search

   .. autoattribute:: CalendaringManager.calendar_search_order

   .. automethod:: CalendaringManager.get_calendars_by_search

   .. automethod:: CalendaringManager.get_calendar_query_from_inspector



Calendar Admin
______________

   .. automethod:: CalendaringManager.can_create_calendars

   .. automethod:: CalendaringManager.can_create_calendar_with_record_types

   .. automethod:: CalendaringManager.get_calendar_form_for_create

   .. automethod:: CalendaringManager.create_calendar

   .. automethod:: CalendaringManager.can_update_calendars

   .. automethod:: CalendaringManager.get_calendar_form_for_update

   .. automethod:: CalendaringManager.update_calendar

   .. automethod:: CalendaringManager.can_delete_calendars

   .. automethod:: CalendaringManager.delete_calendar

   .. automethod:: CalendaringManager.can_manage_calendar_aliases

   .. automethod:: CalendaringManager.alias_calendar



Calendar Notification
_____________________

   .. automethod:: CalendaringManager.can_register_for_calendar_notifications

   .. automethod:: CalendaringManager.register_for_new_calendars

   .. automethod:: CalendaringManager.register_for_new_calendar_ancestors

   .. automethod:: CalendaringManager.register_for_new_calendar_descendants

   .. automethod:: CalendaringManager.register_for_changed_calendars

   .. automethod:: CalendaringManager.register_for_changed_calendar

   .. automethod:: CalendaringManager.register_for_deleted_calendars

   .. automethod:: CalendaringManager.register_for_deleted_calendar

   .. automethod:: CalendaringManager.register_for_deleted_calendar_ancestors

   .. automethod:: CalendaringManager.register_for_deleted_calendar_descendants



Calendar Hierarchy
__________________

   .. autoattribute:: CalendaringManager.calendar_hierarchy_id

   .. autoattribute:: CalendaringManager.calendar_hierarchy

   .. automethod:: CalendaringManager.can_access_calendar_hierarchy

   .. automethod:: CalendaringManager.use_comparative_calendar_view

   .. automethod:: CalendaringManager.use_plenary_calendar_view

   .. autoattribute:: CalendaringManager.root_calendar_ids

   .. autoattribute:: CalendaringManager.root_calendars

   .. automethod:: CalendaringManager.has_parent_calendars

   .. automethod:: CalendaringManager.is_parent_of_calendar

   .. automethod:: CalendaringManager.get_parent_calendar_ids

   .. automethod:: CalendaringManager.get_parent_calendars

   .. automethod:: CalendaringManager.is_ancestor_of_calendar

   .. automethod:: CalendaringManager.has_child_calendars

   .. automethod:: CalendaringManager.is_child_of_calendar

   .. automethod:: CalendaringManager.get_child_calendar_ids

   .. automethod:: CalendaringManager.get_child_calendars

   .. automethod:: CalendaringManager.is_descendant_of_calendar

   .. automethod:: CalendaringManager.get_calendar_node_ids

   .. automethod:: CalendaringManager.get_calendar_nodes



Calendar Hierarchy Design
_________________________

   .. autoattribute:: CalendaringManager.calendar_hierarchy_id

   .. autoattribute:: CalendaringManager.calendar_hierarchy

   .. automethod:: CalendaringManager.can_modify_calendar_hierarchy

   .. automethod:: CalendaringManager.add_root_calendar

   .. automethod:: CalendaringManager.remove_root_calendar

   .. automethod:: CalendaringManager.add_child_calendar

   .. automethod:: CalendaringManager.remove_child_calendar

   .. automethod:: CalendaringManager.remove_child_calendars



Calendaring Proxy Manager
-------------------------

.. autoclass:: CalendaringProxyManager
   :show-inheritance:

   .. autoattribute:: CalendaringProxyManager.calandaring_batch_proxy_manager

   .. autoattribute:: CalendaringProxyManager.calandaring_cycle_proxy_manager

   .. autoattribute:: CalendaringProxyManager.calandaring_rules_proxy_manager



Calendaring Profile Methods
___________________

   .. automethod:: CalendaringProxyManager.supports_visible_federation

   .. automethod:: CalendaringProxyManager.supports_event_lookup

   .. automethod:: CalendaringProxyManager.supports_event_query

   .. automethod:: CalendaringProxyManager.supports_event_search

   .. automethod:: CalendaringProxyManager.supports_event_admin

   .. automethod:: CalendaringProxyManager.supports_event_notification

   .. automethod:: CalendaringProxyManager.supports_event_calendar

   .. automethod:: CalendaringProxyManager.supports_event_calendar_assignment

   .. automethod:: CalendaringProxyManager.supports_event_smart_calendar

   .. automethod:: CalendaringProxyManager.supports_recurring_event_lookup

   .. automethod:: CalendaringProxyManager.supports_recurring_event_unravelling

   .. automethod:: CalendaringProxyManager.supports_recurring_event_query

   .. automethod:: CalendaringProxyManager.supports_recurring_event_search

   .. automethod:: CalendaringProxyManager.supports_recurring_event_admin

   .. automethod:: CalendaringProxyManager.supports_recurring_event_notification

   .. automethod:: CalendaringProxyManager.supports_recurring_event_calendar

   .. automethod:: CalendaringProxyManager.supports_recurring_event_calendar_assignment

   .. automethod:: CalendaringProxyManager.supports_recurring_event_smart_calendar

   .. automethod:: CalendaringProxyManager.supports_superseding_event_lookup

   .. automethod:: CalendaringProxyManager.supports_superseding_event_query

   .. automethod:: CalendaringProxyManager.supports_superseding_event_search

   .. automethod:: CalendaringProxyManager.supports_superseding_event_admin

   .. automethod:: CalendaringProxyManager.supports_superseding_event_notification

   .. automethod:: CalendaringProxyManager.supports_superseding_event_calendar

   .. automethod:: CalendaringProxyManager.supports_superseding_event_calendar_assignment

   .. automethod:: CalendaringProxyManager.supports_superseding_event_smart_calendar

   .. automethod:: CalendaringProxyManager.supports_offset_event_lookup

   .. automethod:: CalendaringProxyManager.supports_offset_event_query

   .. automethod:: CalendaringProxyManager.supports_offset_event_search

   .. automethod:: CalendaringProxyManager.supports_offset_event_admin

   .. automethod:: CalendaringProxyManager.supports_offset_event_notification

   .. automethod:: CalendaringProxyManager.supports_offset_event_calendar

   .. automethod:: CalendaringProxyManager.supports_offset_event_calendar_assignment

   .. automethod:: CalendaringProxyManager.supports_offset_event_smart_calendar

   .. automethod:: CalendaringProxyManager.supports_schedule_lookup

   .. automethod:: CalendaringProxyManager.supports_schedule_query

   .. automethod:: CalendaringProxyManager.supports_schedule_search

   .. automethod:: CalendaringProxyManager.supports_schedule_admin

   .. automethod:: CalendaringProxyManager.supports_schedule_notification

   .. automethod:: CalendaringProxyManager.supports_schedule_calendar

   .. automethod:: CalendaringProxyManager.supports_schedule_calendar_assignment

   .. automethod:: CalendaringProxyManager.supports_schedule_smart_calendar

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_lookup

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_query

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_search

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_admin

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_notification

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_calendar

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_calendar_assignment

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_smart_calendar

   .. automethod:: CalendaringProxyManager.supports_commitment_lookup

   .. automethod:: CalendaringProxyManager.supports_commitment_query

   .. automethod:: CalendaringProxyManager.supports_commitment_search

   .. automethod:: CalendaringProxyManager.supports_commitment_admin

   .. automethod:: CalendaringProxyManager.supports_commitment_notification

   .. automethod:: CalendaringProxyManager.supports_commitment_calendar

   .. automethod:: CalendaringProxyManager.supports_commitment_calendar_assignment

   .. automethod:: CalendaringProxyManager.supports_commitment_smart_calendar

   .. automethod:: CalendaringProxyManager.supports_time_period_lookup

   .. automethod:: CalendaringProxyManager.supports_time_period_search

   .. automethod:: CalendaringProxyManager.supports_time_period_admin

   .. automethod:: CalendaringProxyManager.supports_time_period_notification

   .. automethod:: CalendaringProxyManager.supports_time_period_calendar

   .. automethod:: CalendaringProxyManager.supports_time_period_calendar_assignment

   .. automethod:: CalendaringProxyManager.supports_time_period_smart_calendar

   .. automethod:: CalendaringProxyManager.supports_calendar_lookup

   .. automethod:: CalendaringProxyManager.supports_calendar_search

   .. automethod:: CalendaringProxyManager.supports_calendar_admin

   .. automethod:: CalendaringProxyManager.supports_calendar_notification

   .. automethod:: CalendaringProxyManager.supports_calendar_hierarchy

   .. automethod:: CalendaringProxyManager.supports_calendar_hierarchy_design

   .. automethod:: CalendaringProxyManager.supports_calendaring_batch

   .. automethod:: CalendaringProxyManager.supports_calendaring_cycle

   .. automethod:: CalendaringProxyManager.supports_calendaring_rules

   .. autoattribute:: CalendaringProxyManager.event_record_types

   .. automethod:: CalendaringProxyManager.supports_event_record_type

   .. autoattribute:: CalendaringProxyManager.event_search_record_types

   .. automethod:: CalendaringProxyManager.supports_event_search_record_type

   .. autoattribute:: CalendaringProxyManager.recurring_event_record_types

   .. automethod:: CalendaringProxyManager.supports_recurring_event_record_type

   .. autoattribute:: CalendaringProxyManager.recurring_event_search_record_types

   .. automethod:: CalendaringProxyManager.supports_recurring_event_search_record_type

   .. autoattribute:: CalendaringProxyManager.superseding_event_record_types

   .. automethod:: CalendaringProxyManager.supports_superseding_event_record_type

   .. autoattribute:: CalendaringProxyManager.superseding_event_search_record_types

   .. automethod:: CalendaringProxyManager.supports_superseding_event_search_record_type

   .. autoattribute:: CalendaringProxyManager.offset_event_record_types

   .. automethod:: CalendaringProxyManager.supports_offset_event_record_type

   .. autoattribute:: CalendaringProxyManager.offset_event_search_record_types

   .. automethod:: CalendaringProxyManager.supports_offset_event_search_record_type

   .. autoattribute:: CalendaringProxyManager.schedule_record_types

   .. automethod:: CalendaringProxyManager.supports_schedule_record_type

   .. autoattribute:: CalendaringProxyManager.schedule_search_record_types

   .. automethod:: CalendaringProxyManager.supports_schedule_search_record_type

   .. autoattribute:: CalendaringProxyManager.schedule_slot_record_types

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_record_type

   .. autoattribute:: CalendaringProxyManager.schedule_slot_search_record_types

   .. automethod:: CalendaringProxyManager.supports_schedule_slot_search_record_type

   .. autoattribute:: CalendaringProxyManager.time_period_record_types

   .. automethod:: CalendaringProxyManager.supports_time_period_record_type

   .. autoattribute:: CalendaringProxyManager.time_period_search_record_types

   .. automethod:: CalendaringProxyManager.supports_time_period_search_record_type

   .. autoattribute:: CalendaringProxyManager.commitment_record_types

   .. automethod:: CalendaringProxyManager.supports_commitment_record_type

   .. autoattribute:: CalendaringProxyManager.commitment_search_record_types

   .. automethod:: CalendaringProxyManager.supports_commitment_search_record_type

   .. autoattribute:: CalendaringProxyManager.calendar_record_types

   .. automethod:: CalendaringProxyManager.supports_calendar_record_type

   .. autoattribute:: CalendaringProxyManager.calendar_search_record_types

   .. automethod:: CalendaringProxyManager.supports_calendar_search_record_type

   .. autoattribute:: CalendaringProxyManager.spatial_unit_record_types

   .. automethod:: CalendaringProxyManager.supports_spatial_unit_record_type

   .. autoattribute:: CalendaringProxyManager.coordinate_record_types

   .. automethod:: CalendaringProxyManager.supports_coordinate_record_type



Calendar Lookup
_______________

   .. automethod:: CalendaringProxyManager.can_lookup_calendars

   .. automethod:: CalendaringProxyManager.use_comparative_calendar_view

   .. automethod:: CalendaringProxyManager.use_plenary_calendar_view

   .. automethod:: CalendaringProxyManager.get_calendar

   .. automethod:: CalendaringProxyManager.get_calendars_by_ids

   .. automethod:: CalendaringProxyManager.get_calendars_by_genus_type

   .. automethod:: CalendaringProxyManager.get_calendars_by_parent_genus_type

   .. automethod:: CalendaringProxyManager.get_calendars_by_record_type

   .. automethod:: CalendaringProxyManager.get_calendars_by_provider

   .. autoattribute:: CalendaringProxyManager.calendars



Calendar Query
______________

   .. automethod:: CalendaringProxyManager.can_search_calendars

   .. autoattribute:: CalendaringProxyManager.calendar_query

   .. automethod:: CalendaringProxyManager.get_calendars_by_query



Calendar Search
_______________

   .. automethod:: CalendaringProxyManager.can_search_calendars

   .. autoattribute:: CalendaringProxyManager.calendar_search

   .. autoattribute:: CalendaringProxyManager.calendar_search_order

   .. automethod:: CalendaringProxyManager.get_calendars_by_search

   .. automethod:: CalendaringProxyManager.get_calendar_query_from_inspector



Calendar Admin
______________

   .. automethod:: CalendaringProxyManager.can_create_calendars

   .. automethod:: CalendaringProxyManager.can_create_calendar_with_record_types

   .. automethod:: CalendaringProxyManager.get_calendar_form_for_create

   .. automethod:: CalendaringProxyManager.create_calendar

   .. automethod:: CalendaringProxyManager.can_update_calendars

   .. automethod:: CalendaringProxyManager.get_calendar_form_for_update

   .. automethod:: CalendaringProxyManager.update_calendar

   .. automethod:: CalendaringProxyManager.can_delete_calendars

   .. automethod:: CalendaringProxyManager.delete_calendar

   .. automethod:: CalendaringProxyManager.can_manage_calendar_aliases

   .. automethod:: CalendaringProxyManager.alias_calendar



Calendar Notification
_____________________

   .. automethod:: CalendaringProxyManager.can_register_for_calendar_notifications

   .. automethod:: CalendaringProxyManager.register_for_new_calendars

   .. automethod:: CalendaringProxyManager.register_for_new_calendar_ancestors

   .. automethod:: CalendaringProxyManager.register_for_new_calendar_descendants

   .. automethod:: CalendaringProxyManager.register_for_changed_calendars

   .. automethod:: CalendaringProxyManager.register_for_changed_calendar

   .. automethod:: CalendaringProxyManager.register_for_deleted_calendars

   .. automethod:: CalendaringProxyManager.register_for_deleted_calendar

   .. automethod:: CalendaringProxyManager.register_for_deleted_calendar_ancestors

   .. automethod:: CalendaringProxyManager.register_for_deleted_calendar_descendants



Calendar Hierarchy
__________________

   .. autoattribute:: CalendaringProxyManager.calendar_hierarchy_id

   .. autoattribute:: CalendaringProxyManager.calendar_hierarchy

   .. automethod:: CalendaringProxyManager.can_access_calendar_hierarchy

   .. automethod:: CalendaringProxyManager.use_comparative_calendar_view

   .. automethod:: CalendaringProxyManager.use_plenary_calendar_view

   .. autoattribute:: CalendaringProxyManager.root_calendar_ids

   .. autoattribute:: CalendaringProxyManager.root_calendars

   .. automethod:: CalendaringProxyManager.has_parent_calendars

   .. automethod:: CalendaringProxyManager.is_parent_of_calendar

   .. automethod:: CalendaringProxyManager.get_parent_calendar_ids

   .. automethod:: CalendaringProxyManager.get_parent_calendars

   .. automethod:: CalendaringProxyManager.is_ancestor_of_calendar

   .. automethod:: CalendaringProxyManager.has_child_calendars

   .. automethod:: CalendaringProxyManager.is_child_of_calendar

   .. automethod:: CalendaringProxyManager.get_child_calendar_ids

   .. automethod:: CalendaringProxyManager.get_child_calendars

   .. automethod:: CalendaringProxyManager.is_descendant_of_calendar

   .. automethod:: CalendaringProxyManager.get_calendar_node_ids

   .. automethod:: CalendaringProxyManager.get_calendar_nodes



Calendar Hierarchy Design
_________________________

   .. autoattribute:: CalendaringProxyManager.calendar_hierarchy_id

   .. autoattribute:: CalendaringProxyManager.calendar_hierarchy

   .. automethod:: CalendaringProxyManager.can_modify_calendar_hierarchy

   .. automethod:: CalendaringProxyManager.add_root_calendar

   .. automethod:: CalendaringProxyManager.remove_root_calendar

   .. automethod:: CalendaringProxyManager.add_child_calendar

   .. automethod:: CalendaringProxyManager.remove_child_calendar

   .. automethod:: CalendaringProxyManager.remove_child_calendars



