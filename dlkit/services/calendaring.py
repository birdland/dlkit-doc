# -*- coding: utf-8 -*-
"""Calendaring Open Service Interface Definitions
calendaring version 3.0.0

The Calendaring OSID manages events, commitments and calendars. The
Calendaring OSID offers a rich set of event management services.

Event

An ``Event`` is range of time associated with a ``Location`` and event
sponsors. ``Events`` may be managed singularly, or be generated of of
one of the typs of events listed below.

Offset Events

An ``OffSetEvent`` is an ``OsidRule`` for generating an ``Event`` off of
another Event. An ``OffsetEvent`` may be offset by a fixed period of
time, a weekday, or include an external ``Rule`` to determine the
offset. Example ``OffsetEvents`` are "the first Tuesday after Labor Day"
or "24 hours before a due date."

Superseding Events

A ``SupersedingEvent`` is an ``OsidRule`` for replacing another
``Event``. Typically, ``SupersedingEvents`` are used for replacing a
generated ``Event`` from a recurring event series. ``Events`` may be
superseded by date or position in a recruring even seriest. Examples are
"replace the event on 12/25 with an event scheduled for 12/26" or
"replace the 10th event in a course schedule with an exam."

Recurring Events

A ``RecurringEvent`` generates a series of ``Events`` from a Schedule. A
``Schedule`` is a series of times and locations.

A RecurringEvent may include ``SupersedingEvents`` to replace specific
events in the series with another ``Event`` which may, in turn, be
another RecurringEvent. ``RecurringEvents`` may also have a set of
blackout dates in which ``Event`` generation is suuppressed.

Schedules

A ``Schedule`` describes a repeating time and Location. ``Schedules``
may be bounded by dates or by using a ``TimePeriod``. A ``TimePeriod``
is a reusable date range and may include a set of exception ``Events``
to define a set of time ranges that any ``RecurringEvent`` mapped to the
``TimePeriod`` may not occur.

``Schedules`` are composed of ``ScheduleSlots``.  ``ScheduleSlots`` are
normalized weekly time slots. A ``ScheduleSlot`` may be composed of
other ``ScheduleSlots``.

To make a ``RecurringEvent`` for MWF 3pm in room 26-100 during the
summer except July 4th:

  * A ``ScheduleSlot`` for MWF 3pm is created.
  * A ``Schedule`` is created using the ScheduleSlot for room 10-250 in
    the summer ``TimePeriod.``
  * A ``RecurringEvent`` is created using the Schedule.
  * A blackout date for Independence Day is added to the
    ``RecurringEvent.``


Commitments

``Commitments`` are ``OsidRelationships`` between ``Resources`` and
Events. ``Commitments`` may include any data specific to the
relationship.

Calendaring Catalogging

``Events`` and ``Schedules`` are cataloged into ``Calendars``. The
``Calendar`` is simply an ``OsidCatalog`` representing a collection of
``Events`` that may be federated using the OSID hierarchy pattern to
create virtual calendars.

Calendaring Rules

The Calendaring OSID includes a rules package for managing the behavior
of ``Commitments`` and ``Events. It also includes`` a Calendaring Cycle
OSID for managing canonical events and time periods as well as a
Calendaring Mason OSID for defining rules for building events and time
periods. The Calendaring Batch OSID manages ``Events,``
``Commitments,`` and ``TimePeriods`` in bulk.

"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class CalendaringProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible.

        :return: ``true`` if visible federation is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_event_lookup(self):
        """Tests if an event lookup service is supported.
        An event lookup service defines methods to access events.

        :return: true if event lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_event_query(self):
        """Tests if an event query service is supported.

        :return: ``true`` if event query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_event_search(self):
        """Tests if an event search service is supported.

        :return: ``true`` if event search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_event_admin(self):
        """Tests if an event administrative service is supported.

        :return: ``true`` if event admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_event_notification(self):
        """Tests if event notification is supported.
        Messages may be sent when events are created, modified, or
        deleted.

        :return: ``true`` if event notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_event_calendar(self):
        """Tests if an event to calendar lookup session is available.

        :return: ``true`` if event calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_event_calendar_assignment(self):
        """Tests if an event to calendar assignment session is available.

        :return: ``true`` if event calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_event_smart_calendar(self):
        """Tests if event smart calendaring is available.

        :return: ``true`` if event smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_lookup(self):
        """Tests if a recurring event lookup service is supported.

        :return: true if recurring event lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_unravelling(self):
        """Tests if a recurring event unravelling service is supported.

        :return: true if recurring event unravelling is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_query(self):
        """Tests if a recurring event query service is supported.

        :return: ``true`` if recurring event query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_search(self):
        """Tests if a recurring event search service is supported.

        :return: ``true`` if recurring event search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_admin(self):
        """Tests if a recurring event administrative service is supported.

        :return: ``true`` if recurring event admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_notification(self):
        """Tests if recurring event notification is supported.
        Messages may be sent when recurring events are created,
        modified, or deleted.

        :return: ``true`` if recurring event notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_calendar(self):
        """Tests if a recurring event to calendar lookup session is available.

        :return: ``true`` if recurring event calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_calendar_assignment(self):
        """Tests if a recurring event to calendar assignment session is available.

        :return: ``true`` if recurring event calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_recurring_event_smart_calendar(self):
        """Tests if recurring event smart calendaring is available.

        :return: ``true`` if recurring event smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_superseding_event_lookup(self):
        """Tests if a superseding event lookup service is supported.
        A superseding event lookup service defines methods to access
        superseding events.

        :return: true if superseding event lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_superseding_event_query(self):
        """Tests if a superseding event query service is supported.

        :return: ``true`` if superseding event query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_superseding_event_search(self):
        """Tests if a superseding event search service is supported.

        :return: ``true`` if superseding event search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_superseding_event_admin(self):
        """Tests if a superseding event administrative service is supported.

        :return: ``true`` if superseding event admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_superseding_event_notification(self):
        """Tests if superseding event notification is supported.
        Messages may be sent when supsreding events are created,
        modified, or deleted.

        :return: ``true`` if superseding event notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_superseding_event_calendar(self):
        """Tests if superseding event to calendar lookup session is available.

        :return: ``true`` if superseding event calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_superseding_event_calendar_assignment(self):
        """Tests if a superseding event to calendar assignment session is available.

        :return: ``true`` if superseding event calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_superseding_event_smart_calendar(self):
        """Tests if supsreding event smart calendaring is available.

        :return: ``true`` if superseding smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_offset_event_lookup(self):
        """Tests if an offset event lookup service is supported.
        An offset event lookup service defines methods to access events.

        :return: true if offset event lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_offset_event_query(self):
        """Tests if an offset event query service is supported.

        :return: ``true`` if offset event query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_offset_event_search(self):
        """Tests if an offset event search service is supported.

        :return: ``true`` if offset event search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_offset_event_admin(self):
        """Tests if an offset event administrative service is supported.

        :return: ``true`` if offset event admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_offset_event_notification(self):
        """Tests if offset event notification is supported.
        Messages may be sent when events are created, modified, or
        deleted.

        :return: ``true`` if offset event notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_offset_event_calendar(self):
        """Tests if an offset event to calendar lookup session is available.

        :return: ``true`` if event calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_offset_event_calendar_assignment(self):
        """Tests if an offset event to calendar assignment session is available.

        :return: ``true`` if offset event calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_offset_event_smart_calendar(self):
        """Tests if offset event smart calendaring is available.

        :return: ``true`` if offset event smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_lookup(self):
        """Tests if a schedule lookup service is supported.
        A schedule lookup service defines methods to access schedules.

        :return: true if schedule lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_query(self):
        """Tests if a schedule query service is supported.

        :return: ``true`` if schedule query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_search(self):
        """Tests if a schedule search service is supported.

        :return: ``true`` if schedule search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_admin(self):
        """Tests if a schedule administrative service is supported.

        :return: ``true`` if schedule admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_notification(self):
        """Tests if schedule notification is supported.
        Messages may be sent when schedules are created, modified, or
        deleted.

        :return: ``true`` if schedule notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_calendar(self):
        """Tests if a schedule to calendar lookup session is available.

        :return: ``true`` if schedule calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_calendar_assignment(self):
        """Tests if a schedule to calendar assignment session is available.

        :return: ``true`` if schedule calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_smart_calendar(self):
        """Tests if schedule smart calendaring is available.

        :return: ``true`` if schedule smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_slot_lookup(self):
        """Tests if a schedule slot lookup service is supported.
        A schedule sot lookup service defines methods to access schedule
        slots.

        :return: true if schedule slot lookup is supported, false otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_slot_query(self):
        """Tests if a schedule slot query service is supported.

        :return: ``true`` if schedule slot query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_slot_search(self):
        """Tests if a schedule slot search service is supported.

        :return: ``true`` if schedule slots search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_slot_admin(self):
        """Tests if a schedule slot administrative service is supported.

        :return: ``true`` if schedule slot admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_slot_notification(self):
        """Tests if schedule slot notification is supported.
        Messages may be sent when schedule slots are created, modified,
        or deleted.

        :return: ``true`` if schedule slot notification is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_slot_calendar(self):
        """Tests if a schedule slot to calendar lookup session is available.

        :return: ``true`` if schedule slot calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_slot_calendar_assignment(self):
        """Tests if a schedule slot to calendar assignment session is available.

        :return: ``true`` if schedule slot calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_schedule_slot_smart_calendar(self):
        """Tests if schedule slot smart calendaring is available.

        :return: ``true`` if schedule slot smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commitment_lookup(self):
        """Tests if an event commitment lookup service is supported.

        :return: ``true`` if commitment lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commitment_query(self):
        """Tests if a commitment query service is supported.

        :return: ``true`` if commitment query is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commitment_search(self):
        """Tests if a commitment search service is supported.

        :return: ``true`` if commitment search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commitment_admin(self):
        """Tests if a commitment administrative service is supported.

        :return: ``true`` if commitment admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commitment_notification(self):
        """Tests if commitment notification is supported.
        Messages may be sent when commitments are created, modified, or
        deleted.

        :return: ``true`` if commitment notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commitment_calendar(self):
        """Tests if a commitment to calendar lookup session is available.

        :return: ``true`` if commitment calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commitment_calendar_assignment(self):
        """Tests if a commitment to calendar assignment session is available.

        :return: ``true`` if commitment calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_commitment_smart_calendar(self):
        """Tests if commitment smart calendaring is available.

        :return: ``true`` if commitment smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_time_period_lookup(self):
        """Tests if a time period lookup service is supported.

        :return: ``true`` if time period lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_time_period_search(self):
        """Tests if a time period search service is supported.

        :return: ``true`` if time period search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_time_period_admin(self):
        """Tests if a time period administrative service is supported.

        :return: ``true`` if time period admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_time_period_notification(self):
        """Tests if time period notification is supported.
        Messages may be sent when time periods are created, modified, or
        deleted.

        :return: ``true`` if time period notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_time_period_calendar(self):
        """Tests if a time period to calendar lookup session is available.

        :return: ``true`` if time period calendar lookup session is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_time_period_calendar_assignment(self):
        """Tests if a time period to calendar assignment session is available.

        :return: ``true`` if time period calendar assignment is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_time_period_smart_calendar(self):
        """Tests if time period smart calendaring is available.

        :return: ``true`` if time period smart calendaring is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_lookup(self):
        """Tests if a calendar lookup service is supported.

        :return: ``true`` if calendar lookup is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_search(self):
        """Tests if a calendar search service is supported.

        :return: ``true`` if calendar search is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_admin(self):
        """Tests if a calendar administrative service is supported.

        :return: ``true`` if calendar admin is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_notification(self):
        """Tests if calendar notification is supported.
        Messages may be sent when calendars are created, modified, or
        deleted.

        :return: ``true`` if calendar notification is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_hierarchy(self):
        """Tests if a calendar hierarchy traversal is supported.

        :return: ``true`` if a calendar hierarchy traversal is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_hierarchy_design(self):
        """Tests if calendar hierarchy design is supported.

        :return: ``true`` if a calendar hierarchy design is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendaring_batch(self):
        """Tests if a calendaring batch subpackage is supported.

        :return: ``true`` if a calendar batch package is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendaring_cycle(self):
        """Tests if a calendaring cycle subpackage is supported.

        :return: ``true`` if a calendar cycle package is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendaring_rules(self):
        """Tests if a calendaring rules subpackage is supported.

        :return: ``true`` if a calendar rules package is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_event_record_types(self):
        """Gets the supported ``Event`` record types.

        :return: a list containing the supported ``Event`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    event_record_types = property(fget=get_event_record_types)

    def supports_event_record_type(self, event_record_type):
        """Tests if the given ``Event`` record type is supported.

        :param event_record_type: a ``Type`` indicating an ``Event`` record type
        :type event_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_event_search_record_types(self):
        """Gets the supported ``Event`` search record types.

        :return: a list containing the supported ``Event`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    event_search_record_types = property(fget=get_event_search_record_types)

    def supports_event_search_record_type(self, event_search_record_type):
        """Tests if the given ``Event`` search record type is supported.

        :param event_search_record_type: a ``Type`` indicating an ``Event`` search record type
        :type event_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``event_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_record_types(self):
        """Gets the supported ``RecurringEvent`` record types.

        :return: a list containing the supported ``RecurringEvent`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    recurring_event_record_types = property(fget=get_recurring_event_record_types)

    def supports_recurring_event_record_type(self, recurring_event_record_type):
        """Tests if the given ``RecurringEvent`` record type is supported.

        :param recurring_event_record_type: a ``Type`` indicating a ``RecurringEvent`` record type
        :type recurring_event_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``recurring_event_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_search_record_types(self):
        """Gets the supported ``RecurringEvent`` search record types.

        :return: a list containing the supported ``RecurringEvent`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    recurring_event_search_record_types = property(fget=get_recurring_event_search_record_types)

    def supports_recurring_event_search_record_type(self, recurring_event_search_record_type):
        """Tests if the given ``RecurringEvent`` search record type is supported.

        :param recurring_event_search_record_type: a ``Type`` indicating a ``RecurringEvent`` search record type
        :type recurring_event_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``recurring_event_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_record_types(self):
        """Gets the supported ``Superseding`` record types.

        :return: a list containing the supported ``SupersedingEvent`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    superseding_event_record_types = property(fget=get_superseding_event_record_types)

    def supports_superseding_event_record_type(self, superseding_event_record_type):
        """Tests if the given ``SupersedingEvent`` record type is supported.

        :param superseding_event_record_type: a ``Type`` indicating a ``SupersedingEvent`` record type
        :type superseding_event_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``superseding_event_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_search_record_types(self):
        """Gets the supported ``SupersedingEvent`` search record types.

        :return: a list containing the supported ``SupersedingEvent`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    superseding_event_search_record_types = property(fget=get_superseding_event_search_record_types)

    def supports_superseding_event_search_record_type(self, superseding_event_search_record_type):
        """Tests if the given ``SupersedingEvent`` search record type is supported.

        :param superseding_event_search_record_type: a ``Type`` indicating a ``SupersedingEvent`` search record type
        :type superseding_event_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``superseding_event_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_record_types(self):
        """Gets the supported ``OffsetEvent`` record types.

        :return: a list containing the supported ``OffsetEvent`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    offset_event_record_types = property(fget=get_offset_event_record_types)

    def supports_offset_event_record_type(self, offset_event_record_type):
        """Tests if the given ``OffsetEvent`` record type is supported.

        :param offset_event_record_type: a ``Type`` indicating a ``OffsetEvent`` record type
        :type offset_event_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``offset_event_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_search_record_types(self):
        """Gets the supported ``OffsetEvent`` search record types.

        :return: a list containing the supported ``OffsetEvent`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    offset_event_search_record_types = property(fget=get_offset_event_search_record_types)

    def supports_offset_event_search_record_type(self, offset_event_search_record_type):
        """Tests if the given ``OffsetEvent`` search record type is supported.

        :param offset_event_search_record_type: a ``Type`` indicating a ``OffsetEvent`` search record type
        :type offset_event_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``offset_event_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_schedule_record_types(self):
        """Gets the supported ``Schedule`` record types.

        :return: a list containing the supported ``Schedule`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    schedule_record_types = property(fget=get_schedule_record_types)

    def supports_schedule_record_type(self, schedule_record_type):
        """Tests if the given ``Schedule`` record type is supported.

        :param schedule_record_type: a ``Type`` indicating a ``Schedule`` record type
        :type schedule_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_schedule_search_record_types(self):
        """Gets the supported ``Schedule`` search record types.

        :return: a list containing the supported ``Schedule`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    schedule_search_record_types = property(fget=get_schedule_search_record_types)

    def supports_schedule_search_record_type(self, schedule_search_record_type):
        """Tests if the given ``Schedule`` search record type is supported.

        :param schedule_search_record_type: a ``Type`` indicating a ``Schedule`` search record type
        :type schedule_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_record_types(self):
        """Gets the supported ``ScheduleSlot`` record types.

        :return: a list containing the supported ``ScheduleSlot`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    schedule_slot_record_types = property(fget=get_schedule_slot_record_types)

    def supports_schedule_slot_record_type(self, schedule_slot_record_type):
        """Tests if the given ``ScheduleSlot`` record type is supported.

        :param schedule_slot_record_type: a ``Type`` indicating a ``ScheduleSlot`` record type
        :type schedule_slot_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_slot_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_search_record_types(self):
        """Gets the supported ``ScheduleSlot`` search record types.

        :return: a list containing the supported ``ScheduleSlot`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    schedule_slot_search_record_types = property(fget=get_schedule_slot_search_record_types)

    def supports_schedule_slot_search_record_type(self, schedule_slot_search_record_type):
        """Tests if the given ``ScheduleSlot`` search record type is supported.

        :param schedule_slot_search_record_type: a ``Type`` indicating a ``ScheduleSlot`` search record type
        :type schedule_slot_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_slot_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_time_period_record_types(self):
        """Gets the supported ``TimePeriod`` record types.

        :return: a list containing the supported ``TimePeriod`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    time_period_record_types = property(fget=get_time_period_record_types)

    def supports_time_period_record_type(self, time_period_record_type):
        """Tests if the given ``TimePeriod`` record type is supported.

        :param time_period_record_type: a ``Type`` indicating a ``TimePeriod`` record type
        :type time_period_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``time_period_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_time_period_search_record_types(self):
        """Gets the supported ``TimePeriod`` search record types.

        :return: a list containing the supported ``TimePeriod`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    time_period_search_record_types = property(fget=get_time_period_search_record_types)

    def supports_time_period_search_record_type(self, time_period_search_record_type):
        """Tests if the given ``TimePeriod`` search record type is supported.

        :param time_period_search_record_type: a ``Type`` indicating a ``TimePeriod`` search record type
        :type time_period_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given Type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``time_period_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_commitment_record_types(self):
        """Gets the supported ``Commitment`` record types.

        :return: a list containing the supported ``Commitment`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    commitment_record_types = property(fget=get_commitment_record_types)

    def supports_commitment_record_type(self, commitment_record_type):
        """Tests if the given ``Commitment`` record type is supported.

        :param commitment_record_type: a ``Type`` indicating a ``Commitment`` type
        :type commitment_record_type: ``osid.type.Type``
        :return: ``true`` if the given commitment record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``commitment_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_commitment_search_record_types(self):
        """Gets the supported commitment search record types.

        :return: a list containing the supported ``Commitment`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    commitment_search_record_types = property(fget=get_commitment_search_record_types)

    def supports_commitment_search_record_type(self, commitment_search_record_type):
        """Tests if the given commitment search record type is supported.

        :param commitment_search_record_type: a ``Type`` indicating a ``Commitment`` search record type
        :type commitment_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``commitment_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_calendar_record_types(self):
        """Gets the supported ``Calendar`` record types.

        :return: a list containing the supported ``Calendar`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    calendar_record_types = property(fget=get_calendar_record_types)

    def supports_calendar_record_type(self, calendar_record_type):
        """Tests if the given ``Calendar`` record type is supported.

        :param calendar_record_type: a ``Type`` indicating a ``Calendar`` type
        :type calendar_record_type: ``osid.type.Type``
        :return: ``true`` if the given calendar record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_calendar_search_record_types(self):
        """Gets the supported calendar search record types.

        :return: a list containing the supported ``Calendar`` search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    calendar_search_record_types = property(fget=get_calendar_search_record_types)

    def supports_calendar_search_record_type(self, calendar_search_record_type):
        """Tests if the given calendar search record type is supported.

        :param calendar_search_record_type: a ``Type`` indicating a ``Calendar`` search record type
        :type calendar_search_record_type: ``osid.type.Type``
        :return: ``true`` if the given search record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_spatial_unit_record_types(self):
        """Gets all the spatial unit record types supported.

        :return: the list of supported spatial unit record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    spatial_unit_record_types = property(fget=get_spatial_unit_record_types)

    def supports_spatial_unit_record_type(self, spatial_unit_record_type):
        """Tests if a given spatial unit record type is supported.

        :param spatial_unit_record_type: the spatial unit record type
        :type spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the spatial unit record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_record_types(self):
        """Gets all the coordinate record types supported.

        :return: the list of supported coordinate record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    coordinate_record_types = property(fget=get_coordinate_record_types)

    def supports_coordinate_record_type(self, coordinate_record_type):
        """Tests if a given coordinate record type is supported.

        :param coordinate_record_type: the coordinate domain type
        :type coordinate_record_type: ``osid.type.Type``
        :return: ``true`` if the coordinate record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class CalendaringManager(osid_managers.OsidManager, osid_sessions.OsidSession, CalendaringProfile):

    def get_event_lookup_session(self):
        """Gets the ``OsidSession`` associated with the event lookup service.

        :return: an ``EventLookupSession``
        :rtype: ``osid.calendaring.EventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    event_lookup_session = property(fget=get_event_lookup_session)

    def get_event_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventLookupSession``
        :rtype: ``osid.calendaring.EventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_query_session(self):
        """Gets the ``OsidSession`` associated with the event query service.

        :return: an ``EventQuerySession``
        :rtype: ``osid.calendaring.EventQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    event_query_session = property(fget=get_event_query_session)

    def get_event_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventQuerySession``
        :rtype: ``osid.calendaring.EventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_search_session(self):
        """Gets the ``OsidSession`` associated with the event search service.

        :return: an ``EventSearchSession``
        :rtype: ``osid.calendaring.EventSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    event_search_session = property(fget=get_event_search_session)

    def get_event_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventSearchSession``
        :rtype: ``osid.calendaring.EventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_admin_session(self):
        """Gets the ``OsidSession`` associated with the event administration service.

        :return: an ``EventAdminSession``
        :rtype: ``osid.calendaring.EventAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    event_admin_session = property(fget=get_event_admin_session)

    def get_event_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventAdminSession``
        :rtype: ``osid.calendaring.EventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_notification_session(self, event_receiver):
        """Gets the notification session for notifications pertaining to event changes.

        :param event_receiver: the event receiver
        :type event_receiver: ``osid.calendaring.EventReceiver``
        :return: an ``EventNotificationSession``
        :rtype: ``osid.calendaring.EventNotificationSession``
        :raise: ``NullArgument`` -- ``event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_notification_session_for_calendar(self, event_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the event notification service for the given calendar.

        :param event_receiver: the event receiver
        :type event_receiver: ``osid.calendaring.EventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventNotificationSession``
        :rtype: ``osid.calendaring.EventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``event_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_calendar_session(self):
        """Gets the session for retrieving event to calendar mappings.

        :return: an ``EventCalendarSession``
        :rtype: ``osid.calendaring.EventCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    event_calendar_session = property(fget=get_event_calendar_session)

    def get_event_calendar_assignment_session(self):
        """Gets the session for assigning event to calendar mappings.

        :return: an ``EventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.EventCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    event_calendar_assignment_session = property(fget=get_event_calendar_assignment_session)

    def get_event_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``EventSmartCalendarSession``
        :rtype: ``osid.calendaring.EventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_lookup_session(self):
        """Gets the ``OsidSession`` associated with the recurring event lookup service.

        :return: a ``RecurringEventLookupSession``
        :rtype: ``osid.calendaring.RecurringEventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    recurring_event_lookup_session = property(fget=get_recurring_event_lookup_session)

    def get_recurring_event_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventLookupSession``
        :rtype: ``osid.calendaring.RecurringEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_query_session(self):
        """Gets the ``OsidSession`` associated with the recurring event query service.

        :return: a ``RecurringEventQuerySession``
        :rtype: ``osid.calendaring.RecurringEventQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    recurring_event_query_session = property(fget=get_recurring_event_query_session)

    def get_recurring_event_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventQuerySession``
        :rtype: ``osid.calendaring.RecurringEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_search_session(self):
        """Gets the ``OsidSession`` associated with the recurring event search service.

        :return: a ``RecurringEventSearchSession``
        :rtype: ``osid.calendaring.RecurringEventSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    recurring_event_search_session = property(fget=get_recurring_event_search_session)

    def get_recurring_event_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventSearchSession``
        :rtype: ``osid.calendaring.RecurringEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_admin_session(self):
        """Gets the ``OsidSession`` associated with the recurring event administration service.

        :return: a ``RecurringEventAdminSession``
        :rtype: ``osid.calendaring.RecurringEventAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    recurring_event_admin_session = property(fget=get_recurring_event_admin_session)

    def get_recurring_event_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventAdminSession``
        :rtype: ``osid.calendaring.RecurringEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_notification_session(self, recurring_event_receiver):
        """Gets the notification session for notifications pertaining to recurring event changes.

        :param recurring_event_receiver: the recurring event receiver
        :type recurring_event_receiver: ``osid.calendaring.RecurringEventReceiver``
        :return: a ``RecurringEventNotificationSession``
        :rtype: ``osid.calendaring.RecurringEventNotificationSession``
        :raise: ``NullArgument`` -- ``recurring_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_notification_session_for_calendar(self, recurring_event_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the recurring event notification service for the given calendar.

        :param recurring_event_receiver: the recurring event receiver
        :type recurring_event_receiver: ``osid.calendaring.RecurringEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventNotificationSession``
        :rtype: ``osid.calendaring.RecurringEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``recurring_event_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_calendar_session(self):
        """Gets the session for retrieving recurring event to calendar mappings.

        :return: A ``RecurringEventCalendarSession``
        :rtype: ``osid.calendaring.RecurringEventCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    recurring_event_calendar_session = property(fget=get_recurring_event_calendar_session)

    def get_recurring_event_calendar_assignment_session(self):
        """Gets the session for assigning recurring event to calendar mappings.

        :return: a ``RecurringEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.RecurringEventCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    recurring_event_calendar_assignment_session = property(fget=get_recurring_event_calendar_assignment_session)

    def get_recurring_event_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the recurring event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``RecurringEventSmartCalendarSession``
        :rtype: ``osid.calendaring.RecurringEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_lookup_session(self):
        """Gets the ``OsidSession`` associated with the superseding event lookup service.

        :return: a ``SupersedingEventLookupSession``
        :rtype: ``osid.calendaring.SupersedingEventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    superseding_event_lookup_session = property(fget=get_superseding_event_lookup_session)

    def get_superseding_event_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventLookupSession``
        :rtype: ``osid.calendaring.SupersedingEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_query_session(self):
        """Gets the ``OsidSession`` associated with the superseding event query service.

        :return: a ``SupersedingEventQuerySession``
        :rtype: ``osid.calendaring.SupersedingEventQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    superseding_event_query_session = property(fget=get_superseding_event_query_session)

    def get_superseding_event_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventQuerySession``
        :rtype: ``osid.calendaring.SupersedingEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_search_session(self):
        """Gets the ``OsidSession`` associated with the superseding event search service.

        :return: a ``SupersedingEventSearchSession``
        :rtype: ``osid.calendaring.SupersedingEventSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    superseding_event_search_session = property(fget=get_superseding_event_search_session)

    def get_superseding_event_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventSearchSession``
        :rtype: ``osid.calendaring.SupersedingEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_admin_session(self):
        """Gets the ``OsidSession`` associated with the superseding event administration service.

        :return: a ``SupersedingEventAdminSession``
        :rtype: ``osid.calendaring.SupersedingEventAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    superseding_event_admin_session = property(fget=get_superseding_event_admin_session)

    def get_superseding_event_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventAdminSession``
        :rtype: ``osid.calendaring.SupersedingEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_notification_session(self, superseding_event_receiver):
        """Gets the notification session for notifications pertaining to superseding event changes.

        :param superseding_event_receiver: the superseding event receiver
        :type superseding_event_receiver: ``osid.calendaring.SupersedingEventReceiver``
        :return: a ``SupersedingEventNotificationSession``
        :rtype: ``osid.calendaring.SupersedingEventNotificationSession``
        :raise: ``NullArgument`` -- ``superseding_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_notification_session_for_calendar(self, superseding_event_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the superseding event notification service for the given calendar.

        :param superseding_event_receiver: the superseding event receiver
        :type superseding_event_receiver: ``osid.calendaring.SupersedingEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventNotificationSession``
        :rtype: ``osid.calendaring.SupersedingEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``superseding_event_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_calendar_session(self):
        """Gets the session for retrieving superseding event to calendar mappings.

        :return: a ``SupersedingEventCalendarSession``
        :rtype: ``osid.calendaring.SupersedingEventCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    superseding_event_calendar_session = property(fget=get_superseding_event_calendar_session)

    def get_superseding_event_calendar_assignment_session(self):
        """Gets the session for assigning superseding event to calendar mappings.

        :return: a ``SupersedingEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.SupersedingEventCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    superseding_event_calendar_assignment_session = property(fget=get_superseding_event_calendar_assignment_session)

    def get_superseding_event_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the superseding event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``SupersedingEventSmartCalendarSession``
        :rtype: ``osid.calendaring.SupersedingEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_lookup_session(self):
        """Gets the ``OsidSession`` associated with the offset event lookup service.

        :return: an ``OffsetEventLookupSession``
        :rtype: ``osid.calendaring.OffsetEventLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    offset_event_lookup_session = property(fget=get_offset_event_lookup_session)

    def get_offset_event_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventLookupSession``
        :rtype: ``osid.calendaring.OffsetEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_query_session(self):
        """Gets the ``OsidSession`` associated with the offset event query service.

        :return: an ``OffsetEventQuerySession``
        :rtype: ``osid.calendaring.OffsetEventQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    offset_event_query_session = property(fget=get_offset_event_query_session)

    def get_offset_event_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventQuerySession``
        :rtype: ``osid.calendaring.OffsetEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_search_session(self):
        """Gets the ``OsidSession`` associated with the offset event search service.

        :return: an ``OffsetEventSearchSession``
        :rtype: ``osid.calendaring.OffsetEventSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    offset_event_search_session = property(fget=get_offset_event_search_session)

    def get_offset_event_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventSearchSession``
        :rtype: ``osid.calendaring.OffsetEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_admin_session(self):
        """Gets the ``OsidSession`` associated with the offset event administration service.

        :return: an ``OffsetEventAdminSession``
        :rtype: ``osid.calendaring.OffsetEventAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    offset_event_admin_session = property(fget=get_offset_event_admin_session)

    def get_offset_event_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventAdminSession``
        :rtype: ``osid.calendaring.OffsetEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_notification_session(self, offset_event_receiver):
        """Gets the notification session for notifications pertaining to offset event changes.

        :param offset_event_receiver: the offset event receiver
        :type offset_event_receiver: ``osid.calendaring.OffsetEventReceiver``
        :return: an ``OffsetEventNotificationSession``
        :rtype: ``osid.calendaring.OffsetEventNotificationSession``
        :raise: ``NullArgument`` -- ``offset_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_notification_session_for_calendar(self, offset_event_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the offset event notification service for the given calendar.

        :param offset_event_receiver: the offset event receiver
        :type offset_event_receiver: ``osid.calendaring.OffsetEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventNotificationSession``
        :rtype: ``osid.calendaring.OffsetEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``offset_event_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_calendar_session(self):
        """Gets the session for retrieving offset event to calendar mappings.

        :return: an ``OffsetEventCalendarSession``
        :rtype: ``osid.calendaring.OffsetEventCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    offset_event_calendar_session = property(fget=get_offset_event_calendar_session)

    def get_offset_event_calendar_assignment_session(self):
        """Gets the session for assigning offset event to calendar mappings.

        :return: an ``OffsetEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.OffsetEventCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    offset_event_calendar_assignment_session = property(fget=get_offset_event_calendar_assignment_session)

    def get_offset_event_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the offset event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: an ``OffsetEventSmartCalendarSession``
        :rtype: ``osid.calendaring.OffsetEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_lookup_session(self):
        """Gets the ``OsidSession`` associated with the schedule lookup service.

        :return: a ``ScheduleLookupSession``
        :rtype: ``osid.calendaring.ScheduleLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_lookup_session = property(fget=get_schedule_lookup_session)

    def get_schedule_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleLookupSession``
        :rtype: ``osid.calendaring.ScheduleLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_query_session(self):
        """Gets the ``OsidSession`` associated with the schedule query service.

        :return: a ``ScheduleQuerySession``
        :rtype: ``osid.calendaring.ScheduleQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_query_session = property(fget=get_schedule_query_session)

    def get_schedule_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleQuerySession``
        :rtype: ``osid.calendaring.ScheduleQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_search_session(self):
        """Gets the ``OsidSession`` associated with the schedule search service.

        :return: a ``ScheduleSearchSession``
        :rtype: ``osid.calendaring.ScheduleSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_search_session = property(fget=get_schedule_search_session)

    def get_schedule_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSearchSession``
        :rtype: ``osid.calendaring.ScheduleSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_admin_session(self):
        """Gets the ``OsidSession`` associated with the schedule administration service.

        :return: a ``ScheduleAdminSession``
        :rtype: ``osid.calendaring.ScheduleAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_admin_session = property(fget=get_schedule_admin_session)

    def get_schedule_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleAdminSession``
        :rtype: ``osid.calendaring.ScheduleAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_notification_session(self, schedule_receiver):
        """Gets the notification session for notifications pertaining to schedule changes.

        :param schedule_receiver: the schedule receiver
        :type schedule_receiver: ``osid.calendaring.ScheduleReceiver``
        :return: a ``ScheduleNotificationSession``
        :rtype: ``osid.calendaring.ScheduleNotificationSession``
        :raise: ``NullArgument`` -- ``schedule_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_notification_session_for_calendar(self, schedule_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule notification service for the given calendar.

        :param schedule_receiver: the schedule receiver
        :type schedule_receiver: ``osid.calendaring.ScheduleReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleNotificationSession``
        :rtype: ``osid.calendaring.ScheduleNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_calendar_session(self):
        """Gets the session for retrieving schedule to calendar mappings.

        :return: a ``ScheduleCalendarSession``
        :rtype: ``osid.calendaring.ScheduleCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_calendar_session = property(fget=get_schedule_calendar_session)

    def get_schedule_calendar_assignment_session(self):
        """Gets the session for assigning schedule to calendar mappings.

        :return: a ``ScheduleCalendarAssignmentSession``
        :rtype: ``osid.calendaring.ScheduleCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_calendar_assignment_session = property(fget=get_schedule_calendar_assignment_session)

    def get_schedule_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the schedule smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSmartCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_lookup_session(self):
        """Gets the ``OsidSession`` associated with the schedule slot lookup service.

        :return: a ``ScheduleSlotLookupSession``
        :rtype: ``osid.calendaring.ScheduleSlotLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_slot_lookup_session = property(fget=get_schedule_slot_lookup_session)

    def get_schedule_slot_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotLookupSession``
        :rtype: ``osid.calendaring.ScheduleSlotLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_query_session(self):
        """Gets the ``OsidSession`` associated with the schedule slot query service.

        :return: a ``ScheduleSlotQuerySession``
        :rtype: ``osid.calendaring.ScheduleSlotQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_slot_query_session = property(fget=get_schedule_slot_query_session)

    def get_schedule_slot_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotQuerySession``
        :rtype: ``osid.calendaring.ScheduleSlotQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_search_session(self):
        """Gets the ``OsidSession`` associated with the schedule slot search service.

        :return: a ``ScheduleSlotSearchSession``
        :rtype: ``osid.calendaring.ScheduleSlotSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_slot_search_session = property(fget=get_schedule_slot_search_session)

    def get_schedule_slot_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotSearchSession``
        :rtype: ``osid.calendaring.ScheduleSlotSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_admin_session(self):
        """Gets the ``OsidSession`` associated with the schedule slot administration service.

        :return: a ``ScheduleSlotAdminSession``
        :rtype: ``osid.calendaring.ScheduleSlotAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_slot_admin_session = property(fget=get_schedule_slot_admin_session)

    def get_schedule_slot_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotAdminSession``
        :rtype: ``osid.calendaring.ScheduleSlotAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_notification_session(self, schedule_slot_receiver):
        """Gets the notification session for notifications pertaining to schedule slot changes.

        :param schedule_slot_receiver: the schedule slot receiver
        :type schedule_slot_receiver: ``osid.calendaring.ScheduleSlotReceiver``
        :return: a ``ScheduleSlotNotificationSession``
        :rtype: ``osid.calendaring.ScheduleSlotNotificationSession``
        :raise: ``NullArgument`` -- ``schedule_slot_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_notification_session_for_calendar(self, schedule_slot_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the schedule slot notification service for the given calendar.

        :param schedule_slot_receiver: the schedule slot receiver
        :type schedule_slot_receiver: ``osid.calendaring.ScheduleSlotReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotNotificationSession``
        :rtype: ``osid.calendaring.ScheduleSlotNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_slot_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_calendar_session(self):
        """Gets the session for retrieving schedule slot to calendar mappings.

        :return: a ``ScheduleSlotCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSlotCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_slot_calendar_session = property(fget=get_schedule_slot_calendar_session)

    def get_schedule_slot_calendar_assignment_session(self):
        """Gets the session for assigning schedule slot to calendar mappings.

        :return: a ``ScheduleSlotCalendarAssignmentSession``
        :rtype: ``osid.calendaring.ScheduleSlotCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    schedule_slot_calendar_assignment_session = property(fget=get_schedule_slot_calendar_assignment_session)

    def get_schedule_slot_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the schedule slot smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``ScheduleSlotSmartCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSlotSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_lookup_session(self):
        """Gets the ``OsidSession`` associated with the commitment lookup service.

        :return: a ``CommitmentLookupSession``
        :rtype: ``osid.calendaring.CommitmentLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    commitment_lookup_session = property(fget=get_commitment_lookup_session)

    def get_commitment_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentLookupSession``
        :rtype: ``osid.calendaring.CommitmentLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_query_session(self):
        """Gets the ``OsidSession`` associated with the commitment query service.

        :return: a ``CommitmentQuerySession``
        :rtype: ``osid.calendaring.CommitmentQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    commitment_query_session = property(fget=get_commitment_query_session)

    def get_commitment_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentQuerySession``
        :rtype: ``osid.calendaring.CommitmentQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_search_session(self):
        """Gets the ``OsidSession`` associated with the commitment search service.

        :return: a ``CommitmentSearchSession``
        :rtype: ``osid.calendaring.CommitmentSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    commitment_search_session = property(fget=get_commitment_search_session)

    def get_commitment_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentSearchSession``
        :rtype: ``osid.calendaring.CommitmentSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_admin_session(self):
        """Gets the ``OsidSession`` associated with the commitment administration service.

        :return: a ``CommitmentAdminSession``
        :rtype: ``osid.calendaring.CommitmentAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    commitment_admin_session = property(fget=get_commitment_admin_session)

    def get_commitment_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmenttAdminSession``
        :rtype: ``osid.calendaring.CommitmentAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_notification_session(self, commitment_receiver):
        """Gets the notification session for notifications pertaining to commitment changes.

        :param commitment_receiver: the commitment receiver
        :type commitment_receiver: ``osid.calendaring.CommitmentReceiver``
        :return: a ``CommitmentNotificationSession``
        :rtype: ``osid.calendaring.CommitmentNotificationSession``
        :raise: ``NullArgument`` -- ``commitment_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_notification_session_for_calendar(self, commitment_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the commitment notification service for the given calendar.

        :param commitment_receiver: the commitment receiver
        :type commitment_receiver: ``osid.calendaring.CommitmentReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentNotificationSession``
        :rtype: ``osid.calendaring.CommitmentNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``commitment_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_calendar_session(self):
        """Gets the session for retrieving commitment to calendar mappings.

        :return: a ``CommitmentCalendarSession``
        :rtype: ``osid.calendaring.CommitmentCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    commitment_calendar_session = property(fget=get_commitment_calendar_session)

    def get_commitment_calendar_assignment_session(self):
        """Gets the session for assigning commitment to calendar mappings.

        :return: a ``CommitmentCalendarAssignmentSession``
        :rtype: ``osid.calendaring.CommitmentCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    commitment_calendar_assignment_session = property(fget=get_commitment_calendar_assignment_session)

    def get_commitment_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the commitment smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``CommitmentSmartCalendarSession``
        :rtype: ``osid.calendaring.CommitmentSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_lookup_session(self):
        """Gets the ``OsidSession`` associated with the time period lookup service.

        :return: a ``TimePeriodLookupSession``
        :rtype: ``osid.calendaring.TimePeriodLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    time_period_lookup_session = property(fget=get_time_period_lookup_session)

    def get_time_period_lookup_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the time period lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodLookupSession``
        :rtype: ``osid.calendaring.TimePeriodLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_query_session(self):
        """Gets the ``OsidSession`` associated with the time period query service.

        :return: a ``TimePeriodQuerySession``
        :rtype: ``osid.calendaring.TimePeriodQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    time_period_query_session = property(fget=get_time_period_query_session)

    def get_time_period_query_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the time period query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodQuerySession``
        :rtype: ``osid.calendaring.TimePeriodQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_search_session(self):
        """Gets the ``OsidSession`` associated with the time period search service.

        :return: a ``TimePeriodSearchSession``
        :rtype: ``osid.calendaring.TimePeriodSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    time_period_search_session = property(fget=get_time_period_search_session)

    def get_time_period_search_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the time period search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodSearchSession``
        :rtype: ``osid.calendaring.TimePeriodSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_admin_session(self):
        """Gets the ``OsidSession`` associated with the time period administration service.

        :return: a ``TimePeriodAdminSession``
        :rtype: ``osid.calendaring.TimePeriodAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    time_period_admin_session = property(fget=get_time_period_admin_session)

    def get_time_period_admin_session_for_calendar(self, calendar_id):
        """Gets the ``OsidSession`` associated with the time period admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodAdminSession``
        :rtype: ``osid.calendaring.TimePeriodAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_notification_session(self, time_period_receiver):
        """Gets the notification session for notifications pertaining to time period changes.

        :param time_period_receiver: the time period receiver
        :type time_period_receiver: ``osid.calendaring.TimePeriodReceiver``
        :return: a ``TimePeriodNotificationSession``
        :rtype: ``osid.calendaring.TimePeriodNotificationSession``
        :raise: ``NullArgument`` -- ``time_period_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_notification_session_for_calendar(self, time_period_receiver, calendar_id):
        """Gets the ``OsidSession`` associated with the time period notification service for the given calendar.

        :param time_period_receiver: the time period receiver
        :type time_period_receiver: ``osid.calendaring.TimePeriodReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``a _time_period_notification_session``
        :rtype: ``osid.calendaring.TimePeriodNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``time_period_receiver`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_calendar_session(self):
        """Gets the session for retrieving time period to calendar mappings.

        :return: a ``TimePeriodCalendarSession``
        :rtype: ``osid.calendaring.TimePeriodCalendarSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    time_period_calendar_session = property(fget=get_time_period_calendar_session)

    def get_time_period_calendar_assignment_session(self):
        """Gets the session for assigning time period to calendar mappings.

        :return: a ``TimePeriodCalendarAssignmentSession``
        :rtype: ``osid.calendaring.TimePeriodCalendarAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    time_period_calendar_assignment_session = property(fget=get_time_period_calendar_assignment_session)

    def get_time_period_smart_calendar_session(self, calendar_id):
        """Gets the session associated with the time period smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :return: a ``TimePeriodSmartCalendarSession``
        :rtype: ``osid.calendaring.TimePeriodSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_lookup_session(self):
        """Gets the OsidSession associated with the calendar lookup service.

        :return: a ``CalendarLookupSession``
        :rtype: ``osid.calendaring.CalendarLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_lookup() is false``

        """
        raise UNIMPLEMENTED()

    calendar_lookup_session = property(fget=get_calendar_lookup_session)

    def get_calendar_search_session(self):
        """Gets the OsidSession associated with the calendar search service.

        :return: a ``CalendarSearchSession``
        :rtype: ``osid.calendaring.CalendarSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_search() is false``

        """
        raise UNIMPLEMENTED()

    calendar_search_session = property(fget=get_calendar_search_session)

    def get_calendar_admin_session(self):
        """Gets the OsidSession associated with the calendar administration service.

        :return: a ``CalendarAdminSession``
        :rtype: ``osid.calendaring.CalendarAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_admin() is false``

        """
        raise UNIMPLEMENTED()

    calendar_admin_session = property(fget=get_calendar_admin_session)

    def get_calendar_notification_session(self, calendar_receiver):
        """Gets the notification session for notifications pertaining to calendar service changes.

        :param calendar_receiver: the calendar receiver
        :type calendar_receiver: ``osid.calendaring.CalendarReceiver``
        :return: a ``CalendarNotificationSession``
        :rtype: ``osid.calendaring.CalendarNotificationSession``
        :raise: ``NullArgument`` -- ``calendar_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_hierarchy_session(self):
        """Gets the session traversing calendar hierarchies.

        :return: a ``CalendarHierarchySession``
        :rtype: ``osid.calendaring.CalendarHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    calendar_hierarchy_session = property(fget=get_calendar_hierarchy_session)

    def get_calendar_hierarchy_design_session(self):
        """Gets the session designing calendar hierarchies.

        :return: a ``CalendarHierarchyDesignSession``
        :rtype: ``osid.calendaring.CalendarHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    calendar_hierarchy_design_session = property(fget=get_calendar_hierarchy_design_session)

    def get_calandaring_batch_manager(self):
        """Gets the calendaring batch manager.

        :return: a ``CalendaringBatchManager``
        :rtype: ``osid.calendaring.batch.CalendaringBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calandaring_batch_manager = property(fget=get_calandaring_batch_manager)

    def get_calandaring_cycle_manager(self):
        """Gets the calendaring cycle manager.

        :return: a ``CalendaringCycleManager``
        :rtype: ``osid.calendaring.cycle.CalendaringCycleManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_cycle()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calandaring_cycle_manager = property(fget=get_calandaring_cycle_manager)

    def get_calandaring_rules_manager(self):
        """Gets the calendaring rules manager.

        :return: a ``CalendaringRulesManager``
        :rtype: ``osid.calendaring.rules.CalendaringRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calandaring_rules_manager = property(fget=get_calandaring_rules_manager)


##
# The following methods are from osid.calendaring.CalendarLookupSession

    def can_lookup_calendars(self):
        """Tests if this user can perform ``Calendar`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_calendar_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_calendar_view(self):
        """A complete view of the ``Calendar`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_calendar(self, calendar_id):
        """Gets the ``Calendar`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Calendar`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Calendar`` and retained for
        compatility.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: the calendar
        :rtype: ``osid.calendaring.Calendar``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_ids(self, calendar_ids):
        """Gets a ``CalendarList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the calendars
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Calendar`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :param calendar_ids: the list of ``Ids`` to retrieve
        :type calendar_ids: ``osid.id.IdList``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_genus_type(self, calendar_genus_type):
        """Gets a ``CalendarList`` corresponding to the given calendar genus ``Type`` which does not include calendars of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.

        :param calendar_genus_type: a calendar genus type
        :type calendar_genus_type: ``osid.type.Type``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``calendar_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_parent_genus_type(self, calendar_genus_type):
        """Gets a ``CalendarList`` corresponding to the given calendar genus ``Type`` and include any additional calendars with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.

        :param calendar_genus_type: a calendar genus type
        :type calendar_genus_type: ``osid.type.Type``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``calendar_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_record_type(self, calendar_record_type):
        """Gets a ``CalendarList`` containing the given calendar record ``Type``.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.

        :param calendar_record_type: a calendar record type
        :type calendar_record_type: ``osid.type.Type``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_provider(self, resource_id):
        """Gets a ``CalendarList`` for the given provider.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars(self):
        """Gets all ``Calendars``.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.

        :return: a ``CalendarList``
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    calendars = property(fget=get_calendars)


##
# The following methods are from osid.calendaring.CalendarQuerySession

    def can_search_calendars(self):
        """Tests if this user can perform ``Calendar`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_calendar_query(self):
        """Gets a calendar query.

        :return: a calendar query
        :rtype: ``osid.calendaring.CalendarQuery``

        """
        raise UNIMPLEMENTED()

    calendar_query = property(fget=get_calendar_query)

    def get_calendars_by_query(self, calendar_query):
        """Gets a list of ``Calendar`` objects matching the given calendar query.

        :param calendar_query: the calendar query
        :type calendar_query: ``osid.calendaring.CalendarQuery``
        :return: the returned ``CalendarList``
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``calendar_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``calendar_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarSearchSession

    def get_calendar_search(self):
        """Gets a calendar search.

        :return: a calendar search
        :rtype: ``osid.calendaring.CalendarSearch``

        """
        raise UNIMPLEMENTED()

    calendar_search = property(fget=get_calendar_search)

    def get_calendar_search_order(self):
        """Gets a calendar search order.
        The ``CalendarSearchOrder`` is supplied to a ``CalendarSearch``
        to specify the ordering of results.

        :return: the calendar search order
        :rtype: ``osid.calendaring.CalendarSearchOrder``

        """
        raise UNIMPLEMENTED()

    calendar_search_order = property(fget=get_calendar_search_order)

    def get_calendars_by_search(self, calendar_query, calendar_search):
        """Gets the search results matching the given search query using the given search.

        :param calendar_query: the calendar query
        :type calendar_query: ``osid.calendaring.CalendarQuery``
        :param calendar_search: the calendar search
        :type calendar_search: ``osid.calendaring.CalendarSearch``
        :return: the calendar search results
        :rtype: ``osid.calendaring.CalendarSearchResults``
        :raise: ``NullArgument`` -- ``calendar_query`` or ``calendar_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``calendar_query`` or ``calendar_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_calendar_query_from_inspector(self, calendar_query_inspector):
        """Gets a calendar query from an inspector.
        The inspector is available from an ``CalendarSearchResults``.

        :param calendar_query_inspector: a calendar query inspector
        :type calendar_query_inspector: ``osid.calendaring.CalendarQueryInspector``
        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``NullArgument`` -- ``calendar_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``calendar_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarAdminSession

    def can_create_calendars(self):
        """Tests if this user can create ``Calendars``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Calendar`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Calendar`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_calendar_with_record_types(self, calendar_record_types):
        """Tests if this user can create a single ``Calendar`` using the desired record types.
        While ``CalendaringManager.getCalendarRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Calendar``. Providing an empty array tests if a ``Calendar``
        can be created with no records.

        :param calendar_record_types: array of calendar record types
        :type calendar_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Calendar`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_calendar_form_for_create(self, calendar_record_types):
        """Gets the calendar form for creating new calendars.
        A new form should be requested for each create transaction.

        :param calendar_record_types: array of calendar record types
        :type calendar_record_types: ``osid.type.Type[]``
        :return: the calendar form
        :rtype: ``osid.calendaring.CalendarForm``
        :raise: ``NullArgument`` -- ``calendar_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_calendar(self, calendar_form):
        """Creates a new ``Calendar``.

        :param calendar_form: the form for this ``Calendar``
        :type calendar_form: ``osid.calendaring.CalendarForm``
        :return: the new ``Calendar``
        :rtype: ``osid.calendaring.CalendarForm``
        :raise: ``IllegalState`` -- ``calendar_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``calendar_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``calendar_form`` did not originate from ``get_calendar_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_calendars(self):
        """Tests if this user can update ``Calendars``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Calendar`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Calendar`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_calendar_form_for_update(self, calendar_id):
        """Gets the calendar form for updating an existing calendar.
        A new calendar form should be requested for each update
        transaction.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: the calendar form
        :rtype: ``osid.calendaring.CalendarForm``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_calendar(self, calendar_form):
        """Updates an existing calendar.

        :param calendar_form: the form containing the elements to be updated
        :type calendar_form: ``osid.calendaring.CalendarForm``
        :raise: ``IllegalState`` -- ``calendar_form`` already used for an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``calendar_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``calendar_form`` did not originate from ``get_calendar_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_calendars(self):
        """Tests if this user can delete calendars.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Calendar`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Calendar`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_calendar(self, calendar_id):
        """Deletes a ``Calendar``.

        :param calendar_id: the ``Id`` of the ``Calendar`` to remove
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_calendar_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Calendars``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Calendar`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_calendar(self, calendar_id, alias_id):
        """Adds an ``Id`` to a ``Calendar`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Calendar`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another calendar, it is
        reassigned to the given calendar ``Id``.

        :param calendar_id: the ``Id`` of a ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarNotificationSession

    def can_register_for_calendar_notifications(self):
        """Tests if this user can register for ``Calendar`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_calendars(self):
        """Register for notifications of new calendars.
        ``CalendarReceiver.newCalendar()`` is invoked when a new
        ``Calendar`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_calendar_ancestors(self, calendar_id):
        """Registers for notification if an ancestor is added to the specified calendar in the calendar hierarchy.
        ``CalendarReceiver.newCalendarAncestor()`` is invoked when the
        specified calendar experiences an addition in ancestry.

        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_calendar_descendants(self, calendar_id):
        """Registers for notification if a descendant is added to the specified calendar in the calendar hierarchy.
        ``CalendarReceiver.newCalendarDescendant()`` is invoked when the
        specified calendar experiences an addition in descendants.

        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_calendars(self):
        """Registers for notification of updated calendars.
        ``CalendarReceiver.changedCalendar()`` is invoked when a
        calendar is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_calendar(self, calendar_id):
        """Registers for notification of an updated calendar.
        ``CalendarReceiver.changedCalendar()`` is invoked when the
        specified calendar is changed.

        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_calendars(self):
        """Registers for notification of deleted calendars.
        ``CalendarReceiver.deletedCalendar()`` is invoked when a
        calenedar is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_calendar(self, calendar_id):
        """Registers for notification of a deleted calendar.
        ``CalendarReceiver.deletedCalendar()`` is invoked when the
        specified calendar is deleted.

        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_calendar_ancestors(self, calendar_id):
        """Registers for notification if an ancestor is removed from the specified calendar in the calendar hierarchy.
        ``CalendarReceiver.deletedCalendarAncestor()`` is invoked when
        the specified calendar experiences a removal of an ancestor.

        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_calendar_descendants(self, calendar_id):
        """Registers for notification if a descendant is removed from fthe specified calendar in the calendar hierarchy.
        ``CalendarReceiver.deletedCalendarDescednant()`` is invoked when
        the specified calendar experiences a removal of one of its
        descendants.

        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarHierarchySession

    def get_calendar_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    calendar_hierarchy_id = property(fget=get_calendar_hierarchy_id)

    def get_calendar_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    calendar_hierarchy = property(fget=get_calendar_hierarchy)

    def can_access_calendar_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_calendar_ids(self):
        """Gets the root calendar ``Ids`` in this hierarchy.

        :return: the root calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_calendar_ids = property(fget=get_root_calendar_ids)

    def get_root_calendars(self):
        """Gets the root calendars in this calendar hierarchy.

        :return: the root calendars
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_calendars = property(fget=get_root_calendars)

    def has_parent_calendars(self, calendar_id):
        """Tests if the ``Calendar`` has any parents.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if the calendar has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_calendar(self, id_, calendar_id):
        """Tests if an ``Id`` is a direct parent of a calendar.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``calendar_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_calendar_ids(self, calendar_id):
        """Gets the parent ``Ids`` of the given calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the calendar
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_calendars(self, calendar_id):
        """Gets the parents of the given calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: the parents of the calendar
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_calendar(self, id_, calendar_id):
        """Tests if an ``Id`` is an ancestor of a calendar.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``calendar_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_calendars(self, calendar_id):
        """Tests if a calendar has any children.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if the ``calendar_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_calendar(self, id_, calendar_id):
        """Tests if a calendar is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``calendar_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_calendar_ids(self, calendar_id):
        """Gets the child ``Ids`` of the given calendar.

        :param calendar_id: the ``Id`` to query
        :type calendar_id: ``osid.id.Id``
        :return: the children of the calendar
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_calendars(self, calendar_id):
        """Gets the children of the given calendar.

        :param calendar_id: the ``Id`` to query
        :type calendar_id: ``osid.id.Id``
        :return: the children of the calendar
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_calendar(self, id_, calendar_id):
        """Tests if an ``Id`` is a descendant of a calendar.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``calendar_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_node_ids(self, calendar_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given calendar.

        :param calendar_id: the ``Id`` to query
        :type calendar_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_nodes(self, calendar_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given calendar.

        :param calendar_id: the ``Id`` to query
        :type calendar_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a calendar node
        :rtype: ``osid.calendaring.CalendarNode``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarHierarchyDesignSession

    def can_modify_calendar_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_calendar(self, calendar_id):
        """Adds a root calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` not a root
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_calendar(self, calendar_id):
        """Removes a root calendar from this hierarchy.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_calendar(self, calendar_id, child_id):
        """Adds a child to a calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``calendar_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``calendar_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_calendar(self, calendar_id, child_id):
        """Removes a child from a calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_calendars(self, calendar_id):
        """Removes all children from a calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` is in hierarchy
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class CalendaringProxyManager(osid_managers.OsidProxyManager, CalendaringProfile):

    def get_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventLookupSession``
        :rtype: ``osid.calendaring.EventLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventLookupSession``
        :rtype: ``osid.calendaring.EventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the event query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventQuerySession``
        :rtype: ``osid.calendaring.EventQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventQuerySession``
        :rtype: ``osid.calendaring.EventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the event search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventSearchSession``
        :rtype: ``osid.calendaring.EventSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventSearchSession``
        :rtype: ``osid.calendaring.EventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the event administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventAdminSession``
        :rtype: ``osid.calendaring.EventAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventAdminSession``
        :rtype: ``osid.calendaring.EventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_notification_session(self, event_receiver, proxy):
        """Gets the notification session for notifications pertaining to event changes.

        :param event_receiver: the event receiver
        :type event_receiver: ``osid.calendaring.EventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventNotificationSession``
        :rtype: ``osid.calendaring.EventNotificationSession``
        :raise: ``NullArgument`` -- ``event_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_notification_session_for_calendar(self, event_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the event notification service for the given calendar.

        :param event_receiver: the event receiver
        :type event_receiver: ``osid.calendaring.EventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``an _event_notification_session``
        :rtype: ``osid.calendaring.EventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``event_receiver,`` None ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_calendar_session(self, proxy):
        """Gets the session for retrieving event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventCalendarSession``
        :rtype: ``osid.calendaring.EventCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_calendar_assignment_session(self, proxy):
        """Gets the session for assigning event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.EventCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_event_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``EventSmartCalendarSession``
        :rtype: ``osid.calendaring.EventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the recurring event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventLookupSession``
        :rtype: ``osid.calendaring.RecurringEventLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventLookupSession``
        :rtype: ``osid.calendaring.RecurringEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the recurring event query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventQuerySession``
        :rtype: ``osid.calendaring.RecurringEventQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventQuerySession``
        :rtype: ``osid.calendaring.RecurringEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the recurring event search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventSearchSession``
        :rtype: ``osid.calendaring.RecurringEventSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventSearchSession``
        :rtype: ``osid.calendaring.RecurringEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the recurring event administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventAdminSession``
        :rtype: ``osid.calendaring.RecurringEventAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventAdminSession``
        :rtype: ``osid.calendaring.RecurringEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_notification_session(self, recurring_event_receiver, proxy):
        """Gets the notification session for notifications pertaining to recurring event changes.

        :param recurring_event_receiver: the recurring event receiver
        :type recurring_event_receiver: ``osid.calendaring.RecurringEventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventNotificationSession``
        :rtype: ``osid.calendaring.RecurringEventNotificationSession``
        :raise: ``NullArgument`` -- ``recurring_event_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_notification_session_for_calendar(self, recurring_event_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the recurring event notification service for the given calendar.

        :param recurring_event_receiver: the recurring event receiver
        :type recurring_event_receiver: ``osid.calendaring.RecurringEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventNotificationSession``
        :rtype: ``osid.calendaring.RecurringEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``recurring_event_receiver,``  ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_calendar_session(self, proxy):
        """Gets the session for retrieving recurring event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventCalendarSession``
        :rtype: ``osid.calendaring.RecurringEventCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_calendar_assignment_session(self, proxy):
        """Gets the session for assigning recurring event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.RecurringEventCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the recurring event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``RecurringEventSmartCalendarSession``
        :rtype: ``osid.calendaring.RecurringEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_recurring_event_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the superseding event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventLookupSession``
        :rtype: ``osid.calendaring.SupersedingEventLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventLookupSession``
        :rtype: ``osid.calendaring.SupersedingEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the superseding event query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventQuerySession``
        :rtype: ``osid.calendaring.SupersedingEventQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventQuerySession``
        :rtype: ``osid.calendaring.SupersedingEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the superseding event search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventSearchSession``
        :rtype: ``osid.calendaring.SupersedingEventSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventSearchSession``
        :rtype: ``osid.calendaring.SupersedingEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the superseding event administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventAdminSession``
        :rtype: ``osid.calendaring.SupersedingEventAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_event_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventAdminSession``
        :rtype: ``osid.calendaring.SupersedingEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_notification_session(self, superseding_event_receiver, proxy):
        """Gets the notification session for notifications pertaining to superseding event changes.

        :param superseding_event_receiver: the superseding event receiver
        :type superseding_event_receiver: ``osid.calendaring.SupersedingEventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventNotificationSession``
        :rtype: ``osid.calendaring.SupersedingEventNotificationSession``
        :raise: ``NullArgument`` -- ``superseding_event_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_notification_session_for_calendar(self, superseding_event_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the superseding event notification service for the given calendar.

        :param superseding_event_receiver: the superseding event receiver
        :type superseding_event_receiver: ``osid.calendaring.SupersedingEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventNotificationSession``
        :rtype: ``osid.calendaring.SupersedingEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``superseding_event_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_calendar_session(self, proxy):
        """Gets the session for retrieving superseding event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventCalendarSession``
        :rtype: ``osid.calendaring.SupersedingEventCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_calendar_assignment_session(self, proxy):
        """Gets the session for assigning superseding event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.SupersedingEventCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the superseding event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SupersedingEventSmartCalendarSession``
        :rtype: ``osid.calendaring.SupersedingEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_superseding_event_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the offset event lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventLookupSession``
        :rtype: ``osid.calendaring.OffsetEventLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventLookupSession``
        :rtype: ``osid.calendaring.OffsetEventLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the offset event query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventQuerySession``
        :rtype: ``osid.calendaring.OffsetEventQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventQuerySession``
        :rtype: ``osid.calendaring.OffsetEventQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the offset event search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventSearchSession``
        :rtype: ``osid.calendaring.OffsetEventSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventSearchSession``
        :rtype: ``osid.calendaring.OffsetEventSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the offset event administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventAdminSession``
        :rtype: ``osid.calendaring.OffsetEventAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventAdminSession``
        :rtype: ``osid.calendaring.OffsetEventAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_notification_session(self, offset_event_receiver, proxy):
        """Gets the notification session for notifications pertaining to offset event changes.

        :param offset_event_receiver: the offset event receiver
        :type offset_event_receiver: ``osid.calendaring.OffsetEventReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventNotificationSession``
        :rtype: ``osid.calendaring.OffsetEventNotificationSession``
        :raise: ``NullArgument`` -- ``offset_event_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_notification_session_for_calendar(self, offset_event_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the offset event notification service for the given calendar.

        :param offset_event_receiver: the offset event receiver
        :type offset_event_receiver: ``osid.calendaring.OffsetEventReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventNotificationSession``
        :rtype: ``osid.calendaring.OffsetEventNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``offset_event_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_offset_event_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_calendar_session(self, proxy):
        """Gets the session for retrieving offset event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventCalendarSession``
        :rtype: ``osid.calendaring.OffsetEventCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_calendar_assignment_session(self, proxy):
        """Gets the session for assigning offset event to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventCalendarAssignmentSession``
        :rtype: ``osid.calendaring.OffsetEventCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the offset event smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: an ``OffsetEventSmartCalendarSession``
        :rtype: ``osid.calendaring.OffsetEventSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_offset_event_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleLookupSession``
        :rtype: ``osid.calendaring.ScheduleLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleLookupSession``
        :rtype: ``osid.calendaring.ScheduleLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleQuerySession``
        :rtype: ``osid.calendaring.ScheduleQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleQuerySession``
        :rtype: ``osid.calendaring.ScheduleQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSearchSession``
        :rtype: ``osid.calendaring.ScheduleSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSearchSession``
        :rtype: ``osid.calendaring.ScheduleSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleAdminSession``
        :rtype: ``osid.calendaring.ScheduleAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleAdminSession``
        :rtype: ``osid.calendaring.ScheduleAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_notification_session(self, schedule_receiver, proxy):
        """Gets the notification session for notifications pertaining to schedule changes.

        :param schedule_receiver: the schedule receiver
        :type schedule_receiver: ``osid.calendaring.ScheduleReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleNotificationSession``
        :rtype: ``osid.calendaring.ScheduleNotificationSession``
        :raise: ``NullArgument`` -- ``schedule_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_notification_session_for_calendar(self, schedule_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule notification service for the given calendar.

        :param schedule_receiver: the schedule receiver
        :type schedule_receiver: ``osid.calendaring.ScheduleReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleNotificationSession``
        :rtype: ``osid.calendaring.ScheduleNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_calendar_session(self, proxy):
        """Gets the session for retrieving schedule to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleCalendarSession``
        :rtype: ``osid.calendaring.ScheduleCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_calendar_assignment_session(self, proxy):
        """Gets the session for assigning schedule to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleCalendarAssignmentSession``
        :rtype: ``osid.calendaring.ScheduleCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the schedule smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSmartCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotLookupSession``
        :rtype: ``osid.calendaring.ScheduleSlotLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotLookupSession``
        :rtype: ``osid.calendaring.ScheduleSlotLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotQuerySession``
        :rtype: ``osid.calendaring.ScheduleSlotQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotQuerySession``
        :rtype: ``osid.calendaring.ScheduleSlotQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotSearchSession``
        :rtype: ``osid.calendaring.ScheduleSlotSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotSearchSession``
        :rtype: ``osid.calendaring.ScheduleSlotSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotAdminSession``
        :rtype: ``osid.calendaring.ScheduleSlotAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotAdminSession``
        :rtype: ``osid.calendaring.ScheduleSlotAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_notification_session(self, schedule_slot_receiver, proxy):
        """Gets the notification session for notifications pertaining to schedule slot changes.

        :param schedule_slot_receiver: the schedule slot receiver
        :type schedule_slot_receiver: ``osid.calendaring.ScheduleSlotReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotNotificationSession``
        :rtype: ``osid.calendaring.ScheduleSlotNotificationSession``
        :raise: ``NullArgument`` -- ``schedule_slot_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_notification_session_for_calendar(self, schedule_slot_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the schedule slot notification service for the given calendar.

        :param schedule_slot_receiver: the schedule slot receiver
        :type schedule_slot_receiver: ``osid.calendaring.ScheduleSlotReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotNotificationSession``
        :rtype: ``osid.calendaring.ScheduleSlotNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_slot_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_calendar_session(self, proxy):
        """Gets the session for retrieving schedule slot to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSlotCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_calendar_assignment_session(self, proxy):
        """Gets the session for assigning schedule slot to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotCalendarAssignmentSession``
        :rtype: ``osid.calendaring.ScheduleSlotCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the schedule slot smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ScheduleSlotSmartCalendarSession``
        :rtype: ``osid.calendaring.ScheduleSlotSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the commitment lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentLookupSession``
        :rtype: ``osid.calendaring.CommitmentLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a CommitmentLookupSession``
        :rtype: ``osid.calendaring.CommitmentLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the commitment query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentQuerySession``
        :rtype: ``osid.calendaring.CommitmentQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentQuerySession``
        :rtype: ``osid.calendaring.CommitmentQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the commitment search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentSearchSession``
        :rtype: ``osid.calendaring.CommitmentSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentSearchSession``
        :rtype: ``osid.calendaring.CommitmentSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the commitment administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentAdminSession``
        :rtype: ``osid.calendaring.CommitmentAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmenttAdminSession``
        :rtype: ``osid.calendaring.CommitmentAdminSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_notification_session(self, commitment_receiver, proxy):
        """Gets the notification session for notifications pertaining to commitment changes.

        :param commitment_receiver: the commitment receiver
        :type commitment_receiver: ``osid.calendaring.CommitmentReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentNotificationSession``
        :rtype: ``osid.calendaring.CommitmentNotificationSession``
        :raise: ``NullArgument`` -- ``commitment_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_notification_session_for_calendar(self, commitment_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the commitment notification service for the given calendar.

        :param commitment_receiver: the commitment receiver
        :type commitment_receiver: ``osid.calendaring.CommitmentReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentNotificationSession``
        :rtype: ``osid.calendaring.CommitmentNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``commitment_receiver, calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_commitment_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_calendar_session(self, proxy):
        """Gets the session for retrieving commitment to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentCalendarSession``
        :rtype: ``osid.calendaring.CommitmentCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_calendar_assignment_session(self, proxy):
        """Gets the session for assigning commitment to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentCalendarAssignmentSession``
        :rtype: ``osid.calendaring.CommitmentCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_commitment_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the commitment smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CommitmentSmartCalendarSession``
        :rtype: ``osid.calendaring.CommitmentSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_commitment_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_lookup_session(self, proxy):
        """Gets the ``OsidSession`` associated with the time period lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodLookupSession``
        :rtype: ``osid.calendaring.TimePeriodLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_lookup_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period lookup service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodLookupSession``
        :rtype: ``osid.calendaring.TimePeriodLookupSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_query_session(self, proxy):
        """Gets the ``OsidSession`` associated with the time period query service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodQuerySession``
        :rtype: ``osid.calendaring.TimePeriodQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_query_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period query service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodQuerySession``
        :rtype: ``osid.calendaring.TimePeriodQuerySession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_search_session(self, proxy):
        """Gets the ``OsidSession`` associated with the time period search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodSearchSession``
        :rtype: ``osid.calendaring.TimePeriodSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_search_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period search service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodSearchSession``
        :rtype: ``osid.calendaring.TimePeriodSearchSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_admin_session(self, proxy):
        """Gets the ``OsidSession`` associated with the time period administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodAdminSession``
        :rtype: ``osid.calendaring.TimePeriodAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_admin_session_for_calendar(self, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period admin service for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``calendar_id`` not found
        :rtype: ``osid.calendaring.TimePeriodAdminSession``
        :raise: ``NotFound`` -- a ``TimePeriodAdminSession``
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_notification_session(self, time_period_receiver, proxy):
        """Gets the notification session for notifications pertaining to time period changes.

        :param time_period_receiver: the time period receiver
        :type time_period_receiver: ``osid.calendaring.TimePeriodReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodNotificationSession``
        :rtype: ``osid.calendaring.TimePeriodNotificationSession``
        :raise: ``NullArgument`` -- ``time_period_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_notification_session_for_calendar(self, time_period_receiver, calendar_id, proxy):
        """Gets the ``OsidSession`` associated with the time period notification service for the given calendar.

        :param time_period_receiver: the time period receiver
        :type time_period_receiver: ``osid.calendaring.TimePeriodReceiver``
        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: ``a _time_period_notification_session``
        :rtype: ``osid.calendaring.TimePeriodNotificationSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``time_period_receiver`` or ``calendar_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- ``unable to complete request``
        :raise: ``Unimplemented`` -- ``supports_time_period_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_calendar_session(self, proxy):
        """Gets the session for retrieving time period to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodCalendarSession``
        :rtype: ``osid.calendaring.TimePeriodCalendarSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_calendar_assignment_session(self, proxy):
        """Gets the session for assigning time period to calendar mappings.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodCalendarAssignmentSession``
        :rtype: ``osid.calendaring.TimePeriodCalendarAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_calendar_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_time_period_smart_calendar_session(self, calendar_id, proxy):
        """Gets the session associated with the time period smart calendar for the given calendar.

        :param calendar_id: the ``Id`` of the calendar
        :type calendar_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TimePeriodSmartCalendarSession``
        :rtype: ``osid.calendaring.TimePeriodSmartCalendarSession``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id or proxy is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_time_period_smart_calendar()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_lookup_session(self, proxy):
        """Gets the OsidSession associated with the calendar lookup service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarLookupSession``
        :rtype: ``osid.calendaring.CalendarLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_lookup() is false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_search_session(self, proxy):
        """Gets the OsidSession associated with the calendar search service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarSearchSession``
        :rtype: ``osid.calendaring.CalendarSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_search() is false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_admin_session(self, proxy):
        """Gets the OsidSession associated with the calendar administration service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarAdminSession``
        :rtype: ``osid.calendaring.CalendarAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_admin() is false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_notification_session(self, calendar_receiver, proxy):
        """Gets the notification session for notifications pertaining to calendar service changes.

        :param calendar_receiver: the calendar receiver
        :type calendar_receiver: ``osid.calendaring.CalendarReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarNotificationSession``
        :rtype: ``osid.calendaring.CalendarNotificationSession``
        :raise: ``NullArgument`` -- ``calendar_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_notification() is false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_hierarchy_session(self, proxy):
        """Gets the session traversing calendar hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarHierarchySession``
        :rtype: ``osid.calendaring.CalendarHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_hierarchy() is false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_hierarchy_design_session(self, proxy):
        """Gets the session designing calendar hierarchies.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarHierarchyDesignSession``
        :rtype: ``osid.calendaring.CalendarHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_hierarchy_design() is false``

        """
        raise UNIMPLEMENTED()

    def get_calandaring_batch_proxy_manager(self):
        """Gets the calendaring batch proxy manager.

        :return: a ``CalendaringBatchProxyManager``
        :rtype: ``osid.calendaring.batch.CalendaringBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calandaring_batch_proxy_manager = property(fget=get_calandaring_batch_proxy_manager)

    def get_calandaring_cycle_proxy_manager(self):
        """Gets the calendaring cycle proxy manager.

        :return: a ``CalendaringCycleProxyManager``
        :rtype: ``osid.calendaring.cycle.CalendaringCycleProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_cycle()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calandaring_cycle_proxy_manager = property(fget=get_calandaring_cycle_proxy_manager)

    def get_calandaring_rules_proxy_manager(self):
        """Gets the calendaring rules proxy manager.

        :return: a ``CalendaringRulesProxyManager``
        :rtype: ``osid.calendaring.rules.CalendaringRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendaring_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calandaring_rules_proxy_manager = property(fget=get_calandaring_rules_proxy_manager)


##
# The following methods are from osid.calendaring.CalendarLookupSession

    def can_lookup_calendars(self):
        """Tests if this user can perform ``Calendar`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_calendar_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_calendar_view(self):
        """A complete view of the ``Calendar`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_calendar(self, calendar_id):
        """Gets the ``Calendar`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Calendar`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Calendar`` and retained for
        compatility.


        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: the calendar
        :rtype: ``osid.calendaring.Calendar``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_ids(self, calendar_ids):
        """Gets a ``CalendarList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the calendars
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Calendar`` objects may be omitted from the list
        and may present the elements in any order including returning a
        unique set.


        :param calendar_ids: the list of ``Ids`` to retrieve
        :type calendar_ids: ``osid.id.IdList``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_genus_type(self, calendar_genus_type):
        """Gets a ``CalendarList`` corresponding to the given calendar genus ``Type`` which does not include calendars of types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.


        :param calendar_genus_type: a calendar genus type
        :type calendar_genus_type: ``osid.type.Type``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``calendar_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_parent_genus_type(self, calendar_genus_type):
        """Gets a ``CalendarList`` corresponding to the given calendar genus ``Type`` and include any additional calendars with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.


        :param calendar_genus_type: a calendar genus type
        :type calendar_genus_type: ``osid.type.Type``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``calendar_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_record_type(self, calendar_record_type):
        """Gets a ``CalendarList`` containing the given calendar record ``Type``.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.


        :param calendar_record_type: a calendar record type
        :type calendar_record_type: ``osid.type.Type``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_provider(self, resource_id):
        """Gets a ``CalendarList`` for the given provider.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Calendar`` list
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars(self):
        """Gets all ``Calendars``.
        In plenary mode, the returned list contains all known calendars
        or an error results. Otherwise, the returned list may contain
        only those calendars that are accessible through this session.


        :return: a ``CalendarList``
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    calendars = property(fget=get_calendars)


##
# The following methods are from osid.calendaring.CalendarQuerySession

    def can_search_calendars(self):
        """Tests if this user can perform ``Calendar`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_calendar_query(self):
        """Gets a calendar query.

        :return: a calendar query
        :rtype: ``osid.calendaring.CalendarQuery``

        """
        raise UNIMPLEMENTED()

    calendar_query = property(fget=get_calendar_query)

    def get_calendars_by_query(self, calendar_query):
        """Gets a list of ``Calendar`` objects matching the given calendar query.

        :param calendar_query: the calendar query
        :type calendar_query: ``osid.calendaring.CalendarQuery``
        :return: the returned ``CalendarList``
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NullArgument`` -- ``calendar_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``calendar_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarSearchSession

    def get_calendar_search(self):
        """Gets a calendar search.

        :return: a calendar search
        :rtype: ``osid.calendaring.CalendarSearch``

        """
        raise UNIMPLEMENTED()

    calendar_search = property(fget=get_calendar_search)

    def get_calendar_search_order(self):
        """Gets a calendar search order.
        The ``CalendarSearchOrder`` is supplied to a ``CalendarSearch``
        to specify the ordering of results.


        :return: the calendar search order
        :rtype: ``osid.calendaring.CalendarSearchOrder``

        """
        raise UNIMPLEMENTED()

    calendar_search_order = property(fget=get_calendar_search_order)

    def get_calendars_by_search(self, calendar_query, calendar_search):
        """Gets the search results matching the given search query using the given search.

        :param calendar_query: the calendar query
        :type calendar_query: ``osid.calendaring.CalendarQuery``
        :param calendar_search: the calendar search
        :type calendar_search: ``osid.calendaring.CalendarSearch``
        :return: the calendar search results
        :rtype: ``osid.calendaring.CalendarSearchResults``
        :raise: ``NullArgument`` -- ``calendar_query`` or ``calendar_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``calendar_query`` or ``calendar_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_calendar_query_from_inspector(self, calendar_query_inspector):
        """Gets a calendar query from an inspector.
        The inspector is available from an ``CalendarSearchResults``.


        :param calendar_query_inspector: a calendar query inspector
        :type calendar_query_inspector: ``osid.calendaring.CalendarQueryInspector``
        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``NullArgument`` -- ``calendar_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``calendar_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarAdminSession

    def can_create_calendars(self):
        """Tests if this user can create ``Calendars``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Calendar`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.


        :return: ``false`` if ``Calendar`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_calendar_with_record_types(self, calendar_record_types):
        """Tests if this user can create a single ``Calendar`` using the desired record types.
        While ``CalendaringManager.getCalendarRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Calendar``. Providing an empty array tests if a ``Calendar``
        can be created with no records.


        :param calendar_record_types: array of calendar record types
        :type calendar_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Calendar`` creation using the specified ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_calendar_form_for_create(self, calendar_record_types):
        """Gets the calendar form for creating new calendars.
        A new form should be requested for each create transaction.


        :param calendar_record_types: array of calendar record types
        :type calendar_record_types: ``osid.type.Type[]``
        :return: the calendar form
        :rtype: ``osid.calendaring.CalendarForm``
        :raise: ``NullArgument`` -- ``calendar_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_calendar(self, calendar_form):
        """Creates a new ``Calendar``.

        :param calendar_form: the form for this ``Calendar``
        :type calendar_form: ``osid.calendaring.CalendarForm``
        :return: the new ``Calendar``
        :rtype: ``osid.calendaring.CalendarForm``
        :raise: ``IllegalState`` -- ``calendar_form`` already used for a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``calendar_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``calendar_form`` did not originate from ``get_calendar_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_calendars(self):
        """Tests if this user can update ``Calendars``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Calendar`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.


        :return: ``false`` if ``Calendar`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_calendar_form_for_update(self, calendar_id):
        """Gets the calendar form for updating an existing calendar.
        A new calendar form should be requested for each update
        transaction.


        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: the calendar form
        :rtype: ``osid.calendaring.CalendarForm``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_calendar(self, calendar_form):
        """Updates an existing calendar.

        :param calendar_form: the form containing the elements to be updated
        :type calendar_form: ``osid.calendaring.CalendarForm``
        :raise: ``IllegalState`` -- ``calendar_form`` already used for an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``calendar_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``calendar_form`` did not originate from ``get_calendar_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_calendars(self):
        """Tests if this user can delete calendars.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Calendar`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.


        :return: ``false`` if ``Calendar`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_calendar(self, calendar_id):
        """Deletes a ``Calendar``.

        :param calendar_id: the ``Id`` of the ``Calendar`` to remove
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_calendar_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Calendars``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Calendar`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_calendar(self, calendar_id, alias_id):
        """Adds an ``Id`` to a ``Calendar`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Calendar`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another calendar, it is
        reassigned to the given calendar ``Id``.


        :param calendar_id: the ``Id`` of a ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarNotificationSession

    def can_register_for_calendar_notifications(self):
        """Tests if this user can register for ``Calendar`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_calendars(self):
        """Register for notifications of new calendars.
        ``CalendarReceiver.newCalendar()`` is invoked when a new
        ``Calendar`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_calendar_ancestors(self, calendar_id):
        """Registers for notification if an ancestor is added to the specified calendar in the calendar hierarchy.
        ``CalendarReceiver.newCalendarAncestor()`` is invoked when the
        specified calendar experiences an addition in ancestry.


        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_calendar_descendants(self, calendar_id):
        """Registers for notification if a descendant is added to the specified calendar in the calendar hierarchy.
        ``CalendarReceiver.newCalendarDescendant()`` is invoked when the
        specified calendar experiences an addition in descendants.


        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_calendars(self):
        """Registers for notification of updated calendars.
        ``CalendarReceiver.changedCalendar()`` is invoked when a
        calendar is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_calendar(self, calendar_id):
        """Registers for notification of an updated calendar.
        ``CalendarReceiver.changedCalendar()`` is invoked when the
        specified calendar is changed.


        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_calendars(self):
        """Registers for notification of deleted calendars.
        ``CalendarReceiver.deletedCalendar()`` is invoked when a
        calenedar is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_calendar(self, calendar_id):
        """Registers for notification of a deleted calendar.
        ``CalendarReceiver.deletedCalendar()`` is invoked when the
        specified calendar is deleted.


        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_calendar_ancestors(self, calendar_id):
        """Registers for notification if an ancestor is removed from the specified calendar in the calendar hierarchy.
        ``CalendarReceiver.deletedCalendarAncestor()`` is invoked when
        the specified calendar experiences a removal of an ancestor.


        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_calendar_descendants(self, calendar_id):
        """Registers for notification if a descendant is removed from fthe specified calendar in the calendar hierarchy.
        ``CalendarReceiver.deletedCalendarDescednant()`` is invoked when
        the specified calendar experiences a removal of one of its
        descendants.


        :param calendar_id: the ``Id`` of the calendar to monitor
        :type calendar_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``calendar_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarHierarchySession

    def get_calendar_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    calendar_hierarchy_id = property(fget=get_calendar_hierarchy_id)

    def get_calendar_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    calendar_hierarchy = property(fget=get_calendar_hierarchy)

    def can_access_calendar_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may not offer traversal
        functions to unauthorized users.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_calendar_ids(self):
        """Gets the root calendar ``Ids`` in this hierarchy.

        :return: the root calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_calendar_ids = property(fget=get_root_calendar_ids)

    def get_root_calendars(self):
        """Gets the root calendars in this calendar hierarchy.

        :return: the root calendars
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_calendars = property(fget=get_root_calendars)

    def has_parent_calendars(self, calendar_id):
        """Tests if the ``Calendar`` has any parents.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if the calendar has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_calendar(self, id_, calendar_id):
        """Tests if an ``Id`` is a direct parent of a calendar.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``calendar_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_calendar_ids(self, calendar_id):
        """Gets the parent ``Ids`` of the given calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the calendar
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_calendars(self, calendar_id):
        """Gets the parents of the given calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: the parents of the calendar
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_calendar(self, id_, calendar_id):
        """Tests if an ``Id`` is an ancestor of a calendar.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``calendar_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_calendars(self, calendar_id):
        """Tests if a calendar has any children.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if the ``calendar_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_calendar(self, id_, calendar_id):
        """Tests if a calendar is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``calendar_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_calendar_ids(self, calendar_id):
        """Gets the child ``Ids`` of the given calendar.

        :param calendar_id: the ``Id`` to query
        :type calendar_id: ``osid.id.Id``
        :return: the children of the calendar
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_calendars(self, calendar_id):
        """Gets the children of the given calendar.

        :param calendar_id: the ``Id`` to query
        :type calendar_id: ``osid.id.Id``
        :return: the children of the calendar
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_calendar(self, id_, calendar_id):
        """Tests if an ``Id`` is a descendant of a calendar.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``calendar_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_node_ids(self, calendar_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given calendar.

        :param calendar_id: the ``Id`` to query
        :type calendar_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a catalog node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_nodes(self, calendar_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given calendar.

        :param calendar_id: the ``Id`` to query
        :type calendar_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a calendar node
        :rtype: ``osid.calendaring.CalendarNode``
        :raise: ``NotFound`` -- ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CalendarHierarchyDesignSession

    def can_modify_calendar_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.


        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_calendar(self, calendar_id):
        """Adds a root calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` not a root
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_calendar(self, calendar_id):
        """Removes a root calendar from this hierarchy.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_calendar(self, calendar_id, child_id):
        """Adds a child to a calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``calendar_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``calendar_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``calendar_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_calendar(self, calendar_id, child_id):
        """Removes a child from a calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_calendars(self, calendar_id):
        """Removes all children from a calendar.

        :param calendar_id: the ``Id`` of a calendar
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``calendar_id`` is in hierarchy
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Calendar(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def get_calendar_record(self, calendar_record_type):
        """Gets the record corresponding to the given ``Calendar`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``calendar_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(calendar_record_type)`` is ``true`` .

        :param calendar_record_type: a calendar record type
        :type calendar_record_type: ``osid.type.Type``
        :return: the calendar record
        :rtype: ``osid.calendaring.records.CalendarRecord``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(calendar_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.EventLookupSession

    def get_calendar_id(self):
        """Gets the ``Calendar``  ``Id`` associated with this session.

        :return: the ``Calendar Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    calendar_id = property(fget=get_calendar_id)

    def get_calendar(self):
        """Gets the ``Calendar`` associated with this session.

        :return: the ``Calendar`` associated with this session
        :rtype: ``osid.calendaring.Calendar``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    calendar = property(fget=get_calendar)

    def can_lookup_events(self):
        """Tests if this user can perform ``Event`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_event_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_event_view(self):
        """A complete view of the ``Event`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_calendar_view(self):
        """Federates the view for methods in this session.
        A federated view will include events in calendars which are
        children of this calendar in the calendar hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_calendar_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this calendar only.



        """
        raise UNIMPLEMENTED()

    def use_effective_event_view(self):
        """Only events whose effective dates are current are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_effective_event_view(self):
        """All events of any effective dates are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_normalized_event_view(self):
        """A normalized view uses a single ``Event`` to represent a set of recurring events."""
        raise UNIMPLEMENTED()

    def use_denormalized_event_view(self):
        """A denormalized view expands recurring events into a series of ``Events``."""
        raise UNIMPLEMENTED()

    def use_sequestered_event_view(self):
        """The returns from the lookup methods omit sequestered events."""
        raise UNIMPLEMENTED()

    def use_unsequestered_event_view(self):
        """All events are returned including sequestered events."""
        raise UNIMPLEMENTED()

    def get_event(self, event_id):
        """Gets the ``Event`` specified by its ``Id``.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :return: the event
        :rtype: ``osid.calendaring.Event``
        :raise: ``NotFound`` -- ``event_id`` not found
        :raise: ``NullArgument`` -- ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_ids(self, event_ids):
        """Gets an ``EventList`` corresponding to the given ``IdList``.

        :param event_ids: the list of ``Ids`` to retrieve
        :type event_ids: ``osid.id.IdList``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``event_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_genus_type(self, event_genus_type):
        """Gets an ``EventList`` corresponding to the given event genus ``Type`` which does not include events of genus types derived from the specified ``Type``.

        :param event_genus_type: an event genus type
        :type event_genus_type: ``osid.type.Type``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NullArgument`` -- ``event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_parent_genus_type(self, event_genus_type):
        """Gets an ``EventList`` corresponding to the given event genus ``Type`` and include any additional event with genus types derived from the specified ``Type``.

        :param event_genus_type: an event genus type
        :type event_genus_type: ``osid.type.Type``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NullArgument`` -- ``event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_record_type(self, event_record_type):
        """Gets an ``EventList`` containing the given event record ``Type``.

        :param event_record_type: an event record type
        :type event_record_type: ``osid.type.Type``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_on_date(self, from_, to):
        """Gets a list of events where the given date range falls within an event inclusive.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_in_date_range(self, from_, to):
        """Gets an ``EventList`` that fall within the given range inclusive ````.

        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_upcoming_events(self, number):
        """Gets the next upcoming events on this calendar.

        :param number: the number of events
        :type number: ``cardinal``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_location(self, location_id):
        """Gets a list of events with the given location.

        :param location_id: a location
        :type location_id: ``osid.id.Id``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_location_on_date(self, location_id, from_, to):
        """Gets an ``EventList`` at the given location where the given date range falls within the event dates inclusive.

        :param location_id: a location
        :type location_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``location_id, from`` , or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_location_in_date_range(self, location_id, from_, to):
        """Gets an ``EventList`` that fall within the given range inclusive at the given location ````.

        :param location_id: a location
        :type location_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``location_id, from`` , or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_sponsor(self, resource_id):
        """Gets a list of events with the given sponsor.

        :param resource_id: a sponsor
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_sponsor_on_date(self, resource_id, from_, to):
        """Gets an ``EventList`` with the given sponsor where the given date range falls within the event dates inclusive.

        :param resource_id: a sponsor
        :type resource_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_sponsor_in_date_range(self, resource_id, from_, to):
        """Gets an ``EventList`` that fall within the given range inclusive at the given location ````.

        :param resource_id: a sponsor
        :type resource_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Event`` list
        :rtype: ``osid.calendaring.EventList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``resource_id, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events(self):
        """Gets all ``Events``.

        :return: an ``EventList``
        :rtype: ``osid.calendaring.EventList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    events = property(fget=get_events)


##
# The following methods are from osid.calendaring.EventQuerySession

    def can_search_events(self):
        """Tests if this user can perform ``Events`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_event_query(self):
        """Gets an event query.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``

        """
        raise UNIMPLEMENTED()

    event_query = property(fget=get_event_query)

    def get_events_by_query(self, event_query):
        """Gets a list of ``Events`` matching the given event query.

        :param event_query: the event query
        :type event_query: ``osid.calendaring.EventQuery``
        :return: the returned ``EventList``
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NullArgument`` -- ``event_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``event_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.EventSearchSession

    def get_event_search(self):
        """Gets an event search.

        :return: the event search
        :rtype: ``osid.calendaring.EventSearch``

        """
        raise UNIMPLEMENTED()

    event_search = property(fget=get_event_search)

    def get_event_search_order(self):
        """Gets an event search order.
        The ``EventSearchOrder`` is supplied to an ``EventSearch`` to
        specify the ordering of results.

        :return: the event search order
        :rtype: ``osid.calendaring.EventSearchOrder``

        """
        raise UNIMPLEMENTED()

    event_search_order = property(fget=get_event_search_order)

    def get_events_by_search(self, event_query, event_search):
        """Gets the search results matching the given search query using the given search.

        :param event_query: the event search query
        :type event_query: ``osid.calendaring.EventQuery``
        :param event_search: the event search
        :type event_search: ``osid.calendaring.EventSearch``
        :return: the event search results
        :rtype: ``osid.calendaring.EventSearchResults``
        :raise: ``NullArgument`` -- ``event_query`` or ``event_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``event_search`` or ``event_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_event_query_from_inspector(self, event_query_inspector):
        """Gets an event query from an inspector.
        The inspector is available from an ``EventSearchResults``.

        :param event_query_inspector: an event query inspector
        :type event_query_inspector: ``osid.calendaring.EventQueryInspector``
        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``NullArgument`` -- ``event_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``event_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.EventAdminSession

    def can_create_events(self):
        """Tests if this user can create ``Events``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an ``Event``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Event`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_event_with_record_types(self, event_record_types):
        """Tests if this user can create a single ``Event`` using the desired record types.
        While ``CalendaringManager.getEventRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Event``.
        Providing an empty array tests if an ``Event`` can be created
        with no records.

        :param event_record_types: array of event record types
        :type event_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Event`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``event_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_event_form_for_create(self, event_record_types):
        """Gets the event form for creating new events.
        A new form should be requested for each create transaction.

        :param event_record_types: array of event record types
        :type event_record_types: ``osid.type.Type[]``
        :return: the event form
        :rtype: ``osid.calendaring.EventForm``
        :raise: ``NullArgument`` -- ``event_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_event(self, event_form):
        """Creates a new ``Event``.

        :param event_form: the form for this ``Event``
        :type event_form: ``osid.calendaring.EventForm``
        :return: the new ``Event``
        :rtype: ``osid.calendaring.Event``
        :raise: ``IllegalState`` -- ``event_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``event_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``event_form`` did not originate from ``get_event_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_events(self):
        """Tests if this user can update ``Events``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an ``Event``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if event modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_event_form_for_update(self, event_id):
        """Gets the event form for updating an existing event.
        A new event form should be requested for each update
        transaction.

        :param event_id: the ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :return: the event form
        :rtype: ``osid.calendaring.EventForm``
        :raise: ``NotFound`` -- ``event_id`` is not found
        :raise: ``NullArgument`` -- ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_event(self, event_form):
        """Updates an existing event.

        :param event_form: the form containing the elements to be updated
        :type event_form: ``osid.calendaring.EventForm``
        :raise: ``IllegalState`` -- ``event_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``event_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``event_form`` did not originate from ``get_event_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_events(self):
        """Tests if this user can delete ``Events``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an ``Event``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Event`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_event(self, event_id):
        """Deletes the ``Event`` identified by the given ``Id``.

        :param event_id: the ``Id`` of the ``Event`` to delete
        :type event_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``Event`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_event_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Events``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Event`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_event(self, event_id, alias_id):
        """Adds an ``Id`` to an ``Event`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Event`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another event, it is
        reassigned to the given event ``Id``.

        :param event_id: the ``Id`` of an ``Event``
        :type event_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``event_id`` not found
        :raise: ``NullArgument`` -- ``event_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.EventNotificationSession

    def can_register_for_event_notifications(self):
        """Tests if this user can register for ``Event`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_normalized_view(self):
        """A normalized view sends a single notification for recurring events."""
        raise UNIMPLEMENTED()

    def use_denormalized_view(self):
        """A denormalized view sends a separate notification for each non- recurring event within a recurring set."""
        raise UNIMPLEMENTED()

    def register_for_new_events(self):
        """Register for notifications of new events.
        ``EventReceiver.newEvent()`` is invoked when a new event is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_events(self):
        """Registers for notification of updated events.
        ``EventReceiver.changedEvent()`` is invoked when an event is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_event(self, event_id):
        """Registers for notification of an updated event.
        ``EventReceiver.changedEvent()`` is invoked when the specified
        event is changed.

        :param event_id: the ``Id`` of the ``Event`` to monitor
        :type event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_events(self):
        """Registers for notification of deleted events.
        ``EventReceiver.deletedEvent()`` is invoked when an event is
        removed from this calendar.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_event(self, event_id):
        """Registers for notification of a deleted event.
        ``EventReceiver.changedEvent()`` is invoked when the specified
        event is removed from this calendar.

        :param event_id: the ``Id`` of the ``Event`` to monitor
        :type event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.EventCalendarSession

    def can_lookup_event_calendar_mappings(self):
        """Tests if this user can perform lookups of event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_calendar_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_calendar_view(self):
        """A complete view of the ``Event`` and ``Calendar`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_event_ids_by_calendar(self, calendar_id):
        """Gets the list of ``Event``  ``Ids`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related event ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_calendar(self, calendar_id):
        """Gets the list of ``Events`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related events
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_event_ids_by_calendars(self, calendar_ids):
        """Gets the list of ``Event Ids`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of event ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_events_by_calendars(self, calendar_ids):
        """Gets the list of ``Events`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of events
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_ids_by_event(self, event_id):
        """Gets the list of ``Calendar``  ``Ids`` mapped to an ``Event``.

        :param event_id: ``Id`` of an ``Event``
        :type event_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``event_id`` is not found
        :raise: ``NullArgument`` -- ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_event(self, event_id):
        """Gets the list of ``Calendars`` mapped to an ``Event``.

        :param event_id: ``Id`` of an ``Event``
        :type event_id: ``osid.id.Id``
        :return: list of calendars
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``event_id`` is not found
        :raise: ``NullArgument`` -- ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.EventCalendarAssignmentSession

    def can_assign_events(self):
        """Tests if this user can alter event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_events_to_calendar(self, calendar_id):
        """Tests if this user can alter event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a PERMISSION_DENIED. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids(self, calendar_id):
        """Gets a list of calendars including and under the given calendar node in which any event can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids_for_event(self, calendar_id, event_id):
        """Gets a list of calendars including and under the given calendar node in which a specific event can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param event_id: the ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_event_to_calendar(self, event_id, calendar_id):
        """Adds an existing ``Event`` to a ``Calendar``.

        :param event_id: the ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``event_id`` is already assigned to ``calendar_id``
        :raise: ``NotFound`` -- ``event_id`` or ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``event_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_event_from_calendar(self, event_id, calendar_id):
        """Removes an ``Event`` from a ``Calendar``.

        :param event_id: the ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``event_id or calendar_id not found or event_id not assigned to calendar_id``
        :raise: ``NullArgument`` -- ``event_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.EventSmartCalendarSession

    def can_manage_smart_calendars(self):
        """Tests if this user can manage smart calendars.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer smart
        operations.

        :return: ``false`` if smart calendar methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_event_query(self, event_query):
        """Applies an event query to this calendar.

        :param event_query: the event query
        :type event_query: ``osid.calendaring.EventQuery``
        :raise: ``NullArgument`` -- ``event_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``event_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_event_query(self):
        """Gets an event query inspector for this calendar.

        :return: the event query inspector
        :rtype: ``osid.calendaring.EventQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_event_sequencing(self, event_search_order):
        """Applies an event search order to this calendar.

        :param event_search_order: the event search order
        :type event_search_order: ``osid.calendaring.EventSearchOrder``
        :raise: ``NullArgument`` -- ``event_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``event_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.RecurringEventLookupSession

    def can_lookup_recurring_events(self):
        """Tests if this user can perform ``RecurringEvent`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_recurring_event_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_recurring_event_view(self):
        """A complete view of the ``Event`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_active_recurring_event_view(self):
        """Only active recurring events are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_status_recurring_event_view(self):
        """All active and inactive recurring events are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_sequestered_recurring_event_view(self):
        """The returns from the lookup methods omit sequestered recurring events."""
        raise UNIMPLEMENTED()

    def use_unsequestered_recurring_event_view(self):
        """All recurring events are returned including sequestered recurring events."""
        raise UNIMPLEMENTED()

    def get_recurring_event(self, recurring_event_id):
        """Gets the ``RecurringEvent`` specified by its ``Id``.

        :param recurring_event_id: ``Id`` of the ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``
        :return: the recurring event
        :rtype: ``osid.calendaring.RecurringEvent``
        :raise: ``NotFound`` -- ``recurring_event_id`` not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_ids(self, recurring_event_ids):
        """Gets a ``RecurringEventList`` corresponding to the given ``IdList``.

        :param recurring_event_ids: the list of ``Ids`` to retrieve
        :type recurring_event_ids: ``osid.id.IdList``
        :return: the returned ``RecurringEvent`` list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``recurring_event_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_genus_type(self, recurring_event_genus_type):
        """Gets a ``RecurringEventList`` corresponding to the given recurring event genus ``Type`` which does not include recurring events of genus types derived from the specified ``Type``.

        :param recurring_event_genus_type: a recurring event genus type
        :type recurring_event_genus_type: ``osid.type.Type``
        :return: the returned ``RecurringEvent`` list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NullArgument`` -- ``recurring_event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_parent_genus_type(self, recurring_event_genus_type):
        """Gets a ``RecurringEventList`` corresponding to the given recurring event genus ``Type`` and include any additional recurring event with genus types derived from the specified ``Type``.

        :param recurring_event_genus_type: a recurring event genus type
        :type recurring_event_genus_type: ``osid.type.Type``
        :return: the returned ``RecurringEvent`` list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NullArgument`` -- ``recurring_event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_record_type(self, recurring_event_record_type):
        """Gets a ``RecurringEventList`` containing the given recurring event record ``Type``.

        :param recurring_event_record_type: a recurring event record type
        :type recurring_event_record_type: ``osid.type.Type``
        :return: the returned ``RecurringEvent`` list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NullArgument`` -- ``recurring_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_schedule_slot(self, schedule_slot_id):
        """Gets the ``RecurringEvents`` containing the given schedule slot.

        :param schedule_slot_id: a schedule slot ``Id``
        :type schedule_slot_id: ``osid.id.Id``
        :return: the returned ``RecurringEvent`` list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events(self):
        """Gets all ``RecurringEvents``.

        :return: a ``RecurringEventList``
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    recurring_events = property(fget=get_recurring_events)


##
# The following methods are from osid.calendaring.RecurringEventUnravellingSession

    def can_unravel_recurring_events(self):
        """Tests if this user can perform ``RecurringEvent`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_by_event(self, event_id):
        """Gets the recurring event where the given event ``Id`` was issued as part of the recurring series.

        :param event_id: ``an event _id``
        :type event_id: ``osid.id.Id``
        :return: the returned ``RecurringEvent``
        :rtype: ``osid.calendaring.RecurringEvent``
        :raise: ``NotFound`` -- ``event_id`` is not found
        :raise: ``NullArgument`` -- ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_events(self, event_ids):
        """Gets a ``RecurringEventList`` corresponding to the given event ``IdList`` where the events were implcitly created from the recurring series.
        In plenary mode, the returned list contains all of the recurring
        events corresponding to the events in the ``Id`` list, in the
        order of the list, including duplicates, or an error results if
        an ``Id`` in the supplied list is not found or inaccessible.
        Otherwise, inaccessible ``Events`` may be omitted from the list
        and may present the elements in any order including returning a
        unique set.

        :param event_ids: the list of ``Ids`` to retrieve
        :type event_ids: ``osid.id.IdList``
        :return: the returned ``RecurringEvent`` list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``event_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def expand_recurring_event(self, recurring_event_id):
        """Expands the given recurring event into a series of non-recurring events.
        In plenary mode, the returned list contains all of the events in
        the series, including duplicates, or an error results. In
        comparative mode, events may be omitted from the list and may
        present the elements in any order, including providing a unique
        set.

        :param recurring_event_id: ``Id`` of the recurring ``Event``
        :type recurring_event_id: ``osid.id.Id``
        :return: the returned ``Event list``
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NotFound`` -- ``recurring_event_id was`` not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def expand_recurring_event_in_date_range(self, recurring_event_id, from_, to):
        """Expands the given recurring event into a series of non-recurring events that fall within the given date range inclusive.
        In plenary mode, the returned list contains all of the events in
        the series, including duplicates, or an error results. In
        comparative mode, events may be omitted from the list and may
        present the elements in any order, including providing a unique
        set.

        :param recurring_event_id: ``Id`` of the recurring ``Event``
        :type recurring_event_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Event list``
        :rtype: ``osid.calendaring.EventList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NotFound`` -- ``recurring_event_id was`` not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def expand_recurring_events(self, recurring_event_ids):
        """Expands the given recurring events into a series of non- recurring events.
        In plenary mode, the returned list contains all of the events in
        the series, including duplicates, or an error results. In
        comparative mode, events may be omitted from the list and may
        present the elements in any order, including providing a unique
        set.

        :param recurring_event_ids: the list of ``Ids`` to expand
        :type recurring_event_ids: ``osid.id.IdList``
        :return: the returned ``Event list``
        :rtype: ``osid.calendaring.EventList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``recurring_event_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def expand_recurring_events_in_date_range(self, recurring_event_ids, from_, to):
        """Expands the given recurring events into a series of non- recurring events that fall within the given date range inclusive.
        In plenary mode, the returned list contains all of the events in
        the series, including duplicates, or an error results. In
        comparative mode, events may be omitted from the list and may
        present the elements in any order, including providing a unique
        set.

        :param recurring_event_ids: the list of ``Ids`` to expand
        :type recurring_event_ids: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Event list``
        :rtype: ``osid.calendaring.EventList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``recurring_event_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_date(self, datetime):
        """Gets a list of recurring events where the given date falls within the span of a recurring event.
        In plenary mode, the returned list contains all known events or
        an error results. Otherwise, the returned list may contain only
        those events that are accessible through this session. In both
        cases, the order of the set is not specified.

        :param datetime: a date
        :type datetime: ``osid.calendaring.DateTime``
        :return: the returned ``RecurringEvent`` list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NullArgument`` -- ``datetime`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_in_date_range(self, from_, to):
        """Gets a ``RecurringEventList`` whose series falls entirely within the given range inclusive ````.
        In plenary mode, the returned list contains all known recurring
        events or an error results. Otherwise, the returned list may
        contain only those recurring events that are accessible through
        this session. In both cases, the order of the set is not
        specified.

        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``RecurringEvent`` list
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_number_of_events(self, recurring_event_id):
        """Gets the number of events in the recurring series.

        :param recurring_event_id: ``Id`` of the recurring ``Event``
        :type recurring_event_id: ``osid.id.Id``
        :return: the number of meeting times
        :rtype: ``cardinal``
        :raise: ``NotFound`` -- ``recurring_event_id was`` not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_number_of_events_in_date_range(self, recurring_event_id, from_, to):
        """Gets the number of events in the recurring series between the given dates inclusive.

        :param recurring_event_id: ``Id`` of the recurring ``Event``
        :type recurring_event_id: ``osid.id.Id``
        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :return: the number of meeting times
        :rtype: ``cardinal``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NotFound`` -- ``recurring_event_id was`` not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.RecurringEventQuerySession

    def can_search_recurring_events(self):
        """Tests if this user can perform ``RecurringEvents`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_query(self):
        """Gets a recurring event query.

        :return: the recurring event query
        :rtype: ``osid.calendaring.RecurringEventQuery``

        """
        raise UNIMPLEMENTED()

    recurring_event_query = property(fget=get_recurring_event_query)

    def get_recurring_events_by_query(self, recurring_event_query):
        """Gets a list of ``RecurringEvents`` matching the given recurring event query.

        :param recurring_event_query: the recurring event query
        :type recurring_event_query: ``osid.calendaring.RecurringEventQuery``
        :return: the returned ``RecurringEventList``
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NullArgument`` -- ``recurring_event_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``recurring_event_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.RecurringEventSearchSession

    def get_recurring_event_search(self):
        """Gets a recurring event search.

        :return: the recurring event search
        :rtype: ``osid.calendaring.RecurringEventSearch``

        """
        raise UNIMPLEMENTED()

    recurring_event_search = property(fget=get_recurring_event_search)

    def get_recurring_event_search_order(self):
        """Gets a recurring event search order.
        The ``RecurringEventSearchOrder`` is supplied to a
        ``RecurringEventSearch`` to specify the ordering of results.

        :return: the recurring event search order
        :rtype: ``osid.calendaring.RecurringEventSearchOrder``

        """
        raise UNIMPLEMENTED()

    recurring_event_search_order = property(fget=get_recurring_event_search_order)

    def get_recurring_events_by_search(self, recurring_event_query, recurring_event_search):
        """Gets the search results matching the given search query using the given search.

        :param recurring_event_query: the recurring event search query
        :type recurring_event_query: ``osid.calendaring.RecurringEventQuery``
        :param recurring_event_search: the recurring event search
        :type recurring_event_search: ``osid.calendaring.RecurringEventSearch``
        :return: the recurring event search results
        :rtype: ``osid.calendaring.RecurringEventSearchResults``
        :raise: ``NullArgument`` -- ``recurring_event_query`` or ``recurring_event_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``recurring_event_search`` or ``recurring_event_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_query_from_inspector(self, recurring_event_query_inspector):
        """Gets a recurring event query from an inspector.
        The inspector is available from a
        ``RecurringEventSearchResults``.

        :param recurring_event_query_inspector: a recurring event query inspector
        :type recurring_event_query_inspector: ``osid.calendaring.RecurringEventQueryInspector``
        :return: the recurring event query
        :rtype: ``osid.calendaring.RecurringEventQuery``
        :raise: ``NullArgument`` -- ``recurring_event_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``recurring_event_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.RecurringEventAdminSession

    def can_create_recurring_events(self):
        """Tests if this user can create ``RecurringEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``RecurringEvent`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if ``RecurringEvent`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_recurring_event_with_record_types(self, recurring_event_record_types):
        """Tests if this user can create a single ``RecurringEvent`` using the desired record types.
        While ``CalendaringManager.getRecurringEventRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``RecurringEvent``. Providing an empty array tests if a
        ``RecurringEvent`` can be created with no records.

        :param recurring_event_record_types: array of recurring event types
        :type recurring_event_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``RecurringEvent`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``recurring_event_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_form_for_create(self, recurring_event_record_types):
        """Gets the recurring event form for creating new recurring events.
        A new form should be requested for each create transaction.

        :param recurring_event_record_types: array of recurring event types
        :type recurring_event_record_types: ``osid.type.Type[]``
        :return: the recurring event form
        :rtype: ``osid.calendaring.RecurringEventForm``
        :raise: ``NullArgument`` -- ``recurring_event_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_recurring_event(self, recurring_event_form):
        """Creates a new ``RecurringEvent``.

        :param recurring_event_form: the form for this ``RecurringEvent``
        :type recurring_event_form: ``osid.calendaring.RecurringEventForm``
        :return: the new ``RecurringEvent``
        :rtype: ``osid.calendaring.RecurringEvent``
        :raise: ``IllegalState`` -- ``recurring_event_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``recurring_event_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``recurring_event_form`` did not originate in a create transaction

        """
        raise UNIMPLEMENTED()

    def can_update_recurring_events(self):
        """Tests if this user can update ``RecurringEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``RecurringEvent`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if recurring event modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_form_for_update(self, recurring_event_id):
        """Gets the recurring event form for updating an existing recurring event.
        A new recurring event form should be requested for each update
        transaction.

        :param recurring_event_id: the ``Id`` of the ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``
        :return: the recurring event form
        :rtype: ``osid.calendaring.RecurringEventForm``
        :raise: ``NotFound`` -- ``recurring_event_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_recurring_event(self, recurring_event_form):
        """Updates an existing recurring event.

        :param recurring_event_form: the form containing the elements to be updated
        :type recurring_event_form: ``osid.calendaring.RecurringEventForm``
        :raise: ``IllegalState`` -- ``recurring_event_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``recurring_event_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``recurring_event_form`` did not originate in an update transaction

        """
        raise UNIMPLEMENTED()

    def can_delete_recurring_events(self):
        """Tests if this user can delete ``RecurringEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``RecurringEvent`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``RecurringEvent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_recurring_event(self, recurring_event_id):
        """Deletes the ``RecurringEvent`` identified by the given ``Id``.

        :param recurring_event_id: the ``Id`` of the ``RecurringEvent`` to delete
        :type recurring_event_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``RecurringEvent`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_recurring_event_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``RecurringEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``RecurringEvent`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_recurring_event(self, recurring_event_id, alias_id):
        """Adds an ``Id`` to a ``RecurringEvent`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``RecurringEvent`` is determined by
        the provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another recurring event, it
        is reassigned to the given recurring event ``Id``.

        :param recurring_event_id: the ``Id`` of a ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``recurring_event_id`` not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_schedule_recurring_events(self):
        """Tests if this user can schedule recurring events.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known recurring event
        methods in this session will result in a ``PermissionDenied``.
        This is intended as a hint to an application that may opt not to
        offer create operations to an unauthorized user.

        :return: ``false`` if recurring event scheduling is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_schedule(self, recurring_event_id, schedule_id):
        """Adds a schedule to the given recurring event.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param schedule_id: a schedule ``Id``
        :type schedule_id: ``osid.id.Id``
        :return: the ``Id`` of the schedule
        :rtype: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- schedule is already part of recurring event
        :raise: ``NotFound`` -- ``recurring_event_id`` or ``schedule_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` or ``schedule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_schedule(self, recurring_event_id, schedule_id):
        """Removes a schedule from a given recurring event.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param schedule_id: the schedule ``Id``
        :type schedule_id: ``osid.id.Id``
        :raise: ``NotFound`` -- schedule not part of recurring event
        :raise: ``NullArgument`` -- ``recurring_event_id`` or ``schedule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_specific_date(self, recurring_event_id, date, location_description):
        """Adds a specific date to the given recurring event.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param date: a date
        :type date: ``osid.calendaring.DateTime``
        :param location_description: location description
        :type location_description: ``osid.locale.DisplayText``
        :raise: ``NotFound`` -- ``recurring_event_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id, date`` , or ``location_description`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_specific_date_with_location(self, recurring_event_id, date, location_id):
        """Adds a specific date to the given recurring event.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param date: a date
        :type date: ``osid.calendaring.DateTime``
        :param location_id: a location
        :type location_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``recurring_event_id`` or ``location_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id, date`` , or ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def clear_specific_dates(self, recurring_event_id, from_, to):
        """Clears any specific dates between the given dates inclusive.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param from: start date inclusive
        :type from: ``osid.calendaring.DateTime``
        :param to: end date inclusive
        :type to: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NotFound`` -- ``recurring_event_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_event(self, recurring_event_id, event_id):
        """Adds another event as part of this recurring event.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``recurring_event_id`` or ``event_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` or ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_event(self, recurring_event_id, event_id):
        """Removes an event as part of this recurring event.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``recurring_event_id`` or ``event_id`` is not found or ``event_id`` not part of ``recurring_event_id``
        :raise: ``NullArgument`` -- ``recurring_event_id`` or ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_blackout(self, recurring_event_id, from_, to):
        """Adds a blackout to the given recurring event that blocks events in the series.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param from: start date inclusive
        :type from: ``osid.calendaring.DateTime``
        :param to: end date inclusive
        :type to: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NotFound`` -- ``recurring_event_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def clear_blackout(self, recurring_event_id, from_, to):
        """Clears any blackouts between the given dates inclusive.

        :param recurring_event_id: a recurring event ``Id``
        :type recurring_event_id: ``osid.id.Id``
        :param from: start date inclusive
        :type from: ``osid.calendaring.DateTime``
        :param to: end date inclusive
        :type to: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NotFound`` -- ``recurring_event_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.RecurringEventNotificationSession

    def can_register_for_recurring_event_notifications(self):
        """Tests if this user can register for ``RecurringEvent`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_recurring_events(self):
        """Register for notifications of new recurring events.
        ``RecurringEventReceiver.newRecurringEvent()`` is invoked when a
        new recurring event is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_recurring_events(self):
        """Registers for notification of updated recurring events.
        ``RecurringEventReceiver.changedRecurringEvent()`` is invoked
        when a recurring event is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_recurring_event(self, recurring_event_id):
        """Registers for notification of an updated recurring event.
        ``RecurringEventReceiver.changedRecurringEvent()`` is invoked
        when the specified recurring event is changed.

        :param recurring_event_id: the ``Id`` of the ``RecurringEvent`` to monitor
        :type recurring_event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``recurring_event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_recurring_events(self):
        """Registers for notification of deleted recurring events.
        ``RecurringEventReceiver.deletedRecurringEvent()`` is invoked
        when a recurring event is removed from this calendar.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_recurring_event(self, recurring_event_id):
        """Registers for notification of a deleted recurring event.
        ``RecurringEventReceiver.changedRecurringEvent()`` is invoked
        when the specified recurring event is removed from this
        calendar.

        :param recurring_event_id: the ``Id`` of the ``RecurringEvent`` to monitor
        :type recurring_event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``recurring_event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.RecurringEventCalendarSession

    def can_lookup_recurring_event_calendar_mappings(self):
        """Tests if this user can perform lookups of recurring event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_ids_by_calendar(self, calendar_id):
        """Gets the list of ``RecurringEvent``  ``Ids`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related recurring event ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_calendar(self, calendar_id):
        """Gets the list of ``RecurringEvents`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related recurring events
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_event_ids_by_calendars(self, calendar_ids):
        """Gets the list of ``RecurringEvent Ids`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of recurring event ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_recurring_events_by_calendars(self, calendar_ids):
        """Gets the list of ``RecurringEvents`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of recurring events
        :rtype: ``osid.calendaring.RecurringEventList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_ids_by_recurring_event(self, recurring_event_id):
        """Gets the list of ``Calendar``  ``Ids`` mapped to a ``RecurringEvent``.

        :param recurring_event_id: ``Id`` of a ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``recurring_event_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_recurring_event(self, recurring_event_id):
        """Gets the list of ``Calendars`` mapped to a ``RecurringEvent``.

        :param recurring_event_id: ``Id`` of a ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``
        :return: list of calendar
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``recurring_event_id`` is not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.RecurringEventCalendarAssignmentSession

    def can_assign_recurring_events(self):
        """Tests if this user can alter recurring event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_recurring_events_to_calendar(self, calendar_id):
        """Tests if this user can alter recurring event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids_for_recurring_event(self, calendar_id, recurring_event_id):
        """Gets a list of calendars including and under the given calendar node in which a specific recurring event can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param recurring_event_id: the ``Id`` of the ``recurring_event_id``
        :type recurring_event_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``recurring_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_recurring_event_to_calendar(self, recurring_event_id, calendar_id):
        """Adds an existing ``RecurringEvent`` to a ``Calendar``.

        :param recurring_event_id: the ``Id`` of the ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``recurring_event_id`` is already assigned to ``calendar_id``
        :raise: ``NotFound`` -- ``recurring_event_id`` or ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``recurring_event_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_recurring_event_from_calendar(self, recurring_event_id, calendar_id):
        """Removes a ``RecurringEvent`` from a ``Calendar``.

        :param recurring_event_id: the ``Id`` of the ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``recurring_event_id`` or ``calendar_id`` not found or ``recurring_event_id`` not assigned to ``calendar_id``
        :raise: ``NullArgument`` -- ``recurring_event_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.RecurringEventSmartCalendarSession

    def apply_recurring_event_query(self, recurring_event_query):
        """Applies a recurring event query to this calendar.

        :param recurring_event_query: the recurring event query
        :type recurring_event_query: ``osid.calendaring.RecurringEventQuery``
        :raise: ``NullArgument`` -- ``recurring_event_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``recurring_event_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_recurring_event_query(self):
        """Gets a recurring event query inspector for this calendar.

        :return: the recruring event query inspector
        :rtype: ``osid.calendaring.RecurringEventQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_recurring_event_sequencing(self, recurring_event_search_order):
        """Applies a recurring event search order to this calendar.

        :param recurring_event_search_order: the recurring event search order
        :type recurring_event_search_order: ``osid.calendaring.RecurringEventSearchOrder``
        :raise: ``NullArgument`` -- ``recurring_event_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``recurring_event_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.SupersedingEventLookupSession

    def can_lookup_superseding_events(self):
        """Tests if this user can perform ``SupersedingEvent`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_superseding_event_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_superseding_event_view(self):
        """A complete view of the ``SupersedingEvent`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_active_superseding_event_view(self):
        """Only active superseding events are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_status_superseding_event_view(self):
        """All active and inactive superseding events are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_superseding_event(self, superseding_event_id):
        """Gets the ``Superseding`` specified by its ``Id``.

        :param superseding_event_id: ``Id`` of the ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``
        :return: the superseding event
        :rtype: ``osid.calendaring.SupersedingEvent``
        :raise: ``NotFound`` -- ``supersedng_event_id`` not found
        :raise: ``NullArgument`` -- ``superseding_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_events_by_ids(self, superseding_event_ids):
        """Gets a ``SupersedingEventList`` corresponding to the given ``IdList``.

        :param superseding_event_ids: the list of ``Ids`` to retrieve
        :type superseding_event_ids: ``osid.id.IdList``
        :return: the returned ``SupersedingEvent`` list
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``superseding_event_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_events_by_genus_type(self, superseding_event_genus_type):
        """Gets a ``SupersedingEventList`` corresponding to the given superseding event genus ``Type`` which does not include superseding events of genus types derived from the specified ``Type``.

        :param superseding_event_genus_type: a superseding event genus type
        :type superseding_event_genus_type: ``osid.type.Type``
        :return: the returned ``SupersedingEvent`` list
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``NullArgument`` -- ``superseding_event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_events_by_parent_genus_type(self, superseding_event_genus_type):
        """Gets a ``SupersedingEventList`` corresponding to the given superseding event genus ``Type`` and include any additional superseding event with genus types derived from the specified ``Type``.

        :param superseding_event_genus_type: a superseding event genus type
        :type superseding_event_genus_type: ``osid.type.Type``
        :return: the returned ``SupersedingEvent`` list
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``NullArgument`` -- ``superseding_event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_events_by_record_type(self, superseding_event_record_type):
        """Gets a ``SupersedingEventList`` containing the given superseding event record ``Type``.

        :param superseding_event_record_type: a superseding event record type
        :type superseding_event_record_type: ``osid.type.Type``
        :return: the returned ``SupersedingEvent`` list
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``NullArgument`` -- ``superseding_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_events_by_superseded_event(self, superseded_event_id):
        """Gets the ``SupersedingEvents`` related to the relative event ``Id``.

        :param superseded_event_id: ``Id`` of the related event
        :type superseded_event_id: ``osid.id.Id``
        :return: the superseding events
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``NotFound`` -- ``superseded_event_id`` not found
        :raise: ``NullArgument`` -- ``superseded_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_events(self):
        """Gets all ``SupersedingEvents``.

        :return: a ``SupersedingEventList``
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    superseding_events = property(fget=get_superseding_events)


##
# The following methods are from osid.calendaring.SupersedingEventQuerySession

    def can_search_superseding_events(self):
        """Tests if this user can perform ``SupersedingEvents`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_query(self):
        """Gets a superseding event query.

        :return: the superseding event query
        :rtype: ``osid.calendaring.SupersedingEventQuery``

        """
        raise UNIMPLEMENTED()

    superseding_event_query = property(fget=get_superseding_event_query)

    def get_superseding_events_by_query(self, superseding_event_query):
        """Gets a list of ``SupersedingEvents`` matching the given superseding event query.

        :param superseding_event_query: the superseding event query
        :type superseding_event_query: ``osid.calendaring.SupersedingEventQuery``
        :return: the returned ``SupersedingEventList``
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``NullArgument`` -- ``superseding_event_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``superseding_event_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.SupersedingEventSearchSession

    def get_superseding_event_search(self):
        """Gets a superseding event search.

        :return: the superseding event search
        :rtype: ``osid.calendaring.SupersedingEventSearch``

        """
        raise UNIMPLEMENTED()

    superseding_event_search = property(fget=get_superseding_event_search)

    def get_superseding_event_search_order(self):
        """Gets a superseding event search order.
        The ``SupersedingEventSearchOrder`` is supplied to a
        ``SupersedingEventSearch`` to specify the ordering of results.

        :return: the superseding event search order
        :rtype: ``osid.calendaring.SupersedingEventSearchOrder``

        """
        raise UNIMPLEMENTED()

    superseding_event_search_order = property(fget=get_superseding_event_search_order)

    def get_superseding_events_by_search(self, superseding_event_query, superseding_event_search):
        """Gets the search results matching the given search query using the given search.

        :param superseding_event_query: the superseding search query
        :type superseding_event_query: ``osid.calendaring.SupersedingEventQuery``
        :param superseding_event_search: the superseding search
        :type superseding_event_search: ``osid.calendaring.SupersedingEventSearch``
        :return: the returned search results
        :rtype: ``osid.calendaring.SupersedingEventSearchResults``
        :raise: ``NullArgument`` -- ``superseding_event_query`` or ``superseding_event_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``superseding_event_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_query_from_inspector(self, superseding_event_query_inspector):
        """Gets a superseding event query from an inspector.
        The inspector is available from a
        ``SupersedingEventSearchResults``.

        :param superseding_event_query_inspector: a superseding event query inspector
        :type superseding_event_query_inspector: ``osid.calendaring.SupersedingEventQueryInspector``
        :return: the superseding event query
        :rtype: ``osid.calendaring.SupersedingEventQuery``
        :raise: ``NullArgument`` -- ``superseding_event_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``superseding_event_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.SupersedingEventAdminSession

    def can_create_superseding_events(self):
        """Tests if this user can create ``SupersedingEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an Event
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Event`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_superseding_event_with_record_types(self, supersdeing_event_record_types):
        """Tests if this user can create a single ``SupersedingEvent`` using the desired record types.
        While ``CalendaringManager.getSupersedingEventRecordTypes()``
        can be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``SupersedingEvent``. Providing an empty array tests if a
        ``RecurringEvent`` can be created with no records.

        :param supersdeing_event_record_types: array of superseding evnt record types
        :type supersdeing_event_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``SupersedingEvent`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``superseding_event_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_form_for_create(self, superseded_event_id, superseding_event_id, supersdeing_event_record_types):
        """Gets the superseding event form for creating new events.
        A new form should be requested for each create transaction.

        :param superseded_event_id: the ``Id`` of the superseded event
        :type superseded_event_id: ``osid.id.Id``
        :param superseding_event_id: the ``Id`` of the superseding event
        :type superseding_event_id: ``osid.id.Id``
        :param supersdeing_event_record_types: array of superseding evnt record types
        :type supersdeing_event_record_types: ``osid.type.Type[]``
        :return: the superseding event form
        :rtype: ``osid.calendaring.SupersedingEventForm``
        :raise: ``NotFound`` -- ``superseded_event_id`` or ``superseding_event_id`` not found
        :raise: ``NullArgument`` -- ``superseded_event_id, superseding_event_id,`` or ``supersdeing_event_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_superseding_event(self, superseding_event_form):
        """Creates a new ``SupersedingEvent``.

        :param superseding_event_form: the form for this ``SupersedingEvent``
        :type superseding_event_form: ``osid.calendaring.SupersedingEventForm``
        :return: the new ``SupersedingEvent``
        :rtype: ``osid.calendaring.SupersedingEvent``
        :raise: ``IllegalState`` -- ``supersdeing_event_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``supersdeing_event_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``superseding_event_form`` did not originate from ``get_superseding_event_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_superseding_events(self):
        """Tests if this user can update ``SupersedingEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``SupersedingEvent`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer update operations to an unauthorized user.

        :return: ``false`` if superseding event modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_form_for_update(self, superseding_event_id):
        """Gets the superseding event form for updating an existing superseding event.
        A new superseding event form should be requested for each update
        transaction.

        :param superseding_event_id: the ``Id`` of the ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``
        :return: the superseding event form
        :rtype: ``osid.calendaring.SupersedingEventForm``
        :raise: ``NotFound`` -- ``superseding_event_id`` is not found
        :raise: ``NullArgument`` -- ``superseding_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_superseding_event(self, superseding_event_form):
        """Updates an existing superseding event.

        :param superseding_event_form: the form containing the elements to be updated
        :type superseding_event_form: ``osid.calendaring.SupersedingEventForm``
        :raise: ``IllegalState`` -- ``supersdeing_event_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``superseding_event_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``superseding_event_form`` did not originate from ``get_superseding_event_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_superseding_events(self):
        """Tests if this user can delete ``SupersedingEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``SupersedingEvent`` will result in a ``PermissionDenied``. This
        is intended as a hint to an application that may opt not to
        offer delete operations to an unauthorized user.

        :return: ``false`` if ``SupersedingEvent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_superseding_event(self, superseding_event_id):
        """Deletes the ``SupersedingEvent`` identified by the given ``Id``.

        :param superseding_event_id: the ``Id`` of the ``SupersedingEvent`` to delete
        :type superseding_event_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``SupersedingEvent`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``superseding_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_superseding_event_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``SupersedingEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``SupersedingEvent`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_superseding_event(self, superseding_event_id, alias_id):
        """Adds an ``Id`` to a ``SupersedingEvent`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``SupersedingEvent`` is determined by
        the provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another superseding event,
        it is reassigned to the given superseding event ``Id``.

        :param superseding_event_id: the ``Id`` of a ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``superseding_event_id`` not found
        :raise: ``NullArgument`` -- ``superseding_event_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.SupersedingEventNotificationSession

    def can_register_for_superseding_event_notifications(self):
        """Tests if this user can register for ``SupersedingEvent`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_superseding_events(self):
        """Register for notifications of new superseding events.
        ``SupersedingEventReceiver.newSupersedingEvent()`` is invoked
        when a new superseding event is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_superseding_events(self):
        """Registers for notification of updated superseding events.
        ``SupersedingEventReceiver.changedSupersedingEvent()`` is
        invoked when a superseding event is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_superseding_event(self, superseding_event_id):
        """Registers for notification of an updated superseding event.
        ``SupersedingEventReceiver.changedSupersedingEvent()`` is
        invoked when the specified superseding event is changed.

        :param superseding_event_id: the ``Id`` of the ``Superseding`` to monitor
        :type superseding_event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``superseding_event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_superseding_events(self):
        """Registers for notification of deleted superseding events.
        ``SupersedingEventReceiver.deletedSupersedingEvent()`` is
        invoked when a superseding event is removed from this calendar.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_superseding_event(self, superseding_event_id):
        """Registers for notification of a deleted superseding event.
        ``SupersedingEventReceiver.changedSupersedingEvent()`` is
        invoked when the specified superseding event is removed from
        this calendar.

        :param superseding_event_id: the ``Id`` of the ``Superseding`` to monitor
        :type superseding_event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``superseding_event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.SupersedingEventCalendarSession

    def can_lookup_superseding_event_calendar_mappings(self):
        """Tests if this user can perform lookups of superseding event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_ids_by_calendar(self, calendar_id):
        """Gets the list of ``SupersedingEvent``  ``Ids`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related superseding event ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_events_by_calendar(self, calendar_id):
        """Gets the list of ``SupersedingEvents`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related superseding events
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_event_ids_by_calendars(self, calendar_ids):
        """Gets the list of ``SupersedingEvent Ids`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of superseding event ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_events_by_calendars(self, calendar_ids):
        """Gets the list of ``SupersedingEvents`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of superseding events
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_superseding_ids_by_recurring_event(self, superseding_event_id):
        """Gets the list of ``Calendar``  ``Ids`` mapped to a ``SupersedingEvent``.

        :param superseding_event_id: ``Id`` of a ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``superseding_event_id`` is not found
        :raise: ``NullArgument`` -- ``supesreding_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_superseding_event(self, superseding_event_id):
        """Gets the list of ``Calendars`` mapped to a ``SupersedingEvent``.

        :param superseding_event_id: ``Id`` of a ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``
        :return: list of calendar
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``superseding_event_id`` is not found
        :raise: ``NullArgument`` -- ``supesreding_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.SupersedingEventCalendarAssignmentSession

    def can_assign_superseding_events(self):
        """Tests if this user can alter superseding event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_superseding_events_to_calendar(self, calendar_id):
        """Tests if this user can alter superseding event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids_for_superseding_event(self, calendar_id, superseding_event_id):
        """Gets a list of calendars including and under the given calendar node in which a specific superseding event can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param superseding_event_id: the ``Id`` of the ``superseding_event_id``
        :type superseding_event_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``superseding_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_superseding_event_to_calendar(self, superseding_event_id, calendar_id):
        """Adds an existing ``SupersedingEvent`` to a ``Calendar``.

        :param superseding_event_id: the ``Id`` of the ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``superseding_event_id`` is already assigned to ``calendar_id``
        :raise: ``NotFound`` -- ``superseding_event_id`` or ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``superseding_event_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_superseding_event_from_calendar(self, superseding_event_id, calendar_id):
        """Removes a ``SupersedingEvent`` from a ``Calendar``.

        :param superseding_event_id: the ``Id`` of the ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``superseding_event_id`` or ``calendar_id`` not found or ``superseding_event_id`` not assigned to ``calendar_id``
        :raise: ``NullArgument`` -- ``superseding_event_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.SupersedingEventSmartCalendarSession

    def apply_superseding_event_query(self, superseding_event_query):
        """Applies a superseding event query to this calendar.

        :param superseding_event_query: the superseding event query
        :type superseding_event_query: ``osid.calendaring.SupersedingEventQuery``
        :raise: ``NullArgument`` -- ``superseding_event_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``superseding_event_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_superseding_event_query(self):
        """Gets a superseding event query inspector for this calendar.

        :return: the superseding event query inspector
        :rtype: ``osid.calendaring.SupersedingEventQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_superseding_event_sequencing(self, superseding_event_search_order):
        """Applies a superseding event search order to this calendar.

        :param superseding_event_search_order: the superseding event search order
        :type superseding_event_search_order: ``osid.calendaring.SupersedingEventSearchOrder``
        :raise: ``NullArgument`` -- ``superseding_event_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``superseding_event_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.OffsetEventLookupSession

    def can_lookup_offset_events(self):
        """Tests if this user can perform ``OffsetEvent`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_offset_event_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_offset_event_view(self):
        """A complete view of the ``OffsetEvent`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_active_offset_event_view(self):
        """Only active offset events are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_status_offset_event_view(self):
        """All active and inactive offset events are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_offset_event(self, offset_event_id):
        """Gets the ``OffsetEvent`` specified by its ``Id``.

        :param offset_event_id: ``Id`` of the ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``
        :return: the offset event
        :rtype: ``osid.calendaring.OffsetEvent``
        :raise: ``NotFound`` -- ``offset_event_id`` not found
        :raise: ``NullArgument`` -- ``offset_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_events_by_ids(self, offset_event_ids):
        """Gets an ``OffsetEventList`` corresponding to the given ``IdList``.

        :param offset_event_ids: the list of ``Ids`` to retrieve
        :type offset_event_ids: ``osid.id.IdList``
        :return: the returned ``OffsetEvent`` list
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``offset_event_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_events_by_genus_type(self, offset_event_genus_type):
        """Gets an ``OffsetEventList`` corresponding to the given offset event genus ``Type`` which does not include offset events of genus types derived from the specified ``Type``.

        :param offset_event_genus_type: an offset event genus type
        :type offset_event_genus_type: ``osid.type.Type``
        :return: the returned ``OffsetEvent`` list
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``NullArgument`` -- ``offset_event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_events_by_parent_genus_type(self, offset_event_genus_type):
        """Gets an ``OffsetEventList`` corresponding to the given offset event genus ``Type`` and include any additional offset event with genus types derived from the specified ``Type``.

        :param offset_event_genus_type: an offset event genus type
        :type offset_event_genus_type: ``osid.type.Type``
        :return: the returned ``OffsetEvent`` list
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``NullArgument`` -- ``offset_event_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_events_by_record_type(self, offset_eventrecord_type):
        """Gets an ``OffsetEventList`` containing the given offset event record ``Type``.

        :param offset_eventrecord_type: an offset event record type
        :type offset_eventrecord_type: ``osid.type.Type``
        :return: the returned ``OffsetEvent`` list
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``NullArgument`` -- ``offset_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_events_by_event(self, event_id):
        """Gets the ``OffsetEvents`` using the given event as a start or ending offset.

        :param event_id: ``Id`` of the related event
        :type event_id: ``osid.id.Id``
        :return: the offset events
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_events(self):
        """Gets all ``OffsetEvents``.

        :return: an ``OffsetEventList``
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    offset_events = property(fget=get_offset_events)


##
# The following methods are from osid.calendaring.OffsetEventQuerySession

    def can_search_offset_events(self):
        """Tests if this user can perform ``OffsetEvents`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_query(self):
        """Gets an offset event query.

        :return: the offset event query
        :rtype: ``osid.calendaring.OffsetEventQuery``

        """
        raise UNIMPLEMENTED()

    offset_event_query = property(fget=get_offset_event_query)

    def get_offset_events_by_query(self, offset_event_query):
        """Gets a list of ``OffsetEvents`` matching the given offset event query.

        :param offset_event_query: the offset event query
        :type offset_event_query: ``osid.calendaring.OffsetEventQuery``
        :return: the returned ``OffsetEventList``
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``NullArgument`` -- ``offset_event_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``offset_event_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.OffsetEventSearchSession

    def get_offset_event_search(self):
        """Gets an offset event search.

        :return: the offset event search
        :rtype: ``osid.calendaring.OffsetEventSearch``

        """
        raise UNIMPLEMENTED()

    offset_event_search = property(fget=get_offset_event_search)

    def get_offset_event_search_order(self):
        """Gets an offset event search order.
        The ``OffsetEventSearchOrder`` is supplied to an
        ``OffsetEventSearch`` to specify the ordering of results.

        :return: the offset event search order
        :rtype: ``osid.calendaring.OffsetEventSearchOrder``

        """
        raise UNIMPLEMENTED()

    offset_event_search_order = property(fget=get_offset_event_search_order)

    def get_offset_events_by_search(self, offset_event_query, offset_event_search):
        """Gets the search results matching the given search query using the given search.

        :param offset_event_query: the offset event search query
        :type offset_event_query: ``osid.calendaring.OffsetEventQuery``
        :param offset_event_search: the offset event search
        :type offset_event_search: ``osid.calendaring.OffsetEventSearch``
        :return: the returned search results
        :rtype: ``osid.calendaring.OffsetEventSearchResults``
        :raise: ``NullArgument`` -- ``offset_event_query`` or ``offset_event_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``offset_event_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_offset_event_query_from_inspector(self, offset_event_query_inspector):
        """Gets an offset event query from an inspector.
        The inspector is available from an ``OffsetEventSearchResults``.

        :param offset_event_query_inspector: an offset event query inspector
        :type offset_event_query_inspector: ``osid.calendaring.OffsetEventQueryInspector``
        :return: the offset event query
        :rtype: ``osid.calendaring.OffsetEventQuery``
        :raise: ``NullArgument`` -- ``offset_event_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``offset_event_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.OffsetEventAdminSession

    def can_create_offset_events(self):
        """Tests if this user can create ``OffsetEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``OffsetEvent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``OffsetEvent`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_offset_event_with_record_types(self, offset_event_record_types):
        """Tests if this user can create a single ``OffsetEvent`` using the desired record types.
        While ``CalendaringManager.getOffsetEventRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``OffsetEvent``. Providing an empty array tests if an
        ``OffsetEvent`` can be created with no records.

        :param offset_event_record_types: array of offset event record types
        :type offset_event_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``OffsetEvent`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``offset_event_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_form_for_create(self, offset_event_record_types):
        """Gets the offset event form for creating new offset events.
        A new form should be requested for each create transaction.

        :param offset_event_record_types: array of offset event record types
        :type offset_event_record_types: ``osid.type.Type[]``
        :return: the offset event form
        :rtype: ``osid.calendaring.OffsetEventForm``
        :raise: ``NullArgument`` -- ``offset_event_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested recod types

        """
        raise UNIMPLEMENTED()

    def create_offset_event(self, offset_event_form):
        """Creates a new ``OffsetEvent``.

        :param offset_event_form: the form for this ``OffsetEvent``
        :type offset_event_form: ``osid.calendaring.OffsetEventForm``
        :return: the new ``OffsetEvent``
        :rtype: ``osid.calendaring.OffsetEvent``
        :raise: ``IllegalState`` -- ``offset_event_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``offset_event_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``offset_event_form`` did not originate from ``get_offset_event_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_offset_events(self):
        """Tests if this user can update ``OffsetEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``OffsetEvent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if offset event modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_offset_event_form_for_update(self, offset_event_id):
        """Gets the offset event form for updating an existing offset event.
        A new offset event form should be requested for each update
        transaction.

        :param offset_event_id: the ``Id`` of the ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``
        :return: the offset event form
        :rtype: ``osid.calendaring.OffsetEventForm``
        :raise: ``NotFound`` -- ``offset_event_id`` is not found
        :raise: ``NullArgument`` -- ``offset_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_offset_event(self, offset_event_form):
        """Updates an existing offset event.

        :param offset_event_form: the form containing the elements to be updated
        :type offset_event_form: ``osid.calendaring.OffsetEventForm``
        :raise: ``IllegalState`` -- ``offset_event_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``offset_event_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``offset_event_form`` did not originate from ``get_offset_event_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_offset_events(self):
        """Tests if this user can delete ``OffsetEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``OffsetEvent`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``OffsetEvent`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_offset_event(self, offset_event_id):
        """Deletes the ``OffsetEvent`` identified by the given ``Id``.

        :param offset_event_id: the ``Id`` of the ``OffsetEvent`` to delete
        :type offset_event_id: ``osid.id.Id``
        :raise: ``NotFound`` -- an ``OffsetEvent`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``offset_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_offset_event_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``OffsetEvents``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``OffsetEvent`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_offset_event(self, offset_event_id, alias_id):
        """Adds an ``Id`` to an ``OffsetEvent`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``OffsetEvent`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another offset event, it is
        reassigned to the given offset event ``Id``.

        :param offset_event_id: the ``Id`` of an ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``offset_event_id`` not found
        :raise: ``NullArgument`` -- ``offset_event_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.OffsetEventNotificationSession

    def can_register_for_offset_event_notifications(self):
        """Tests if this user can register for ``OffsetEvent`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_offset_events(self):
        """Register for notifications of new offset events.
        ``OffsetEventReceiver.newOffsetEvent()`` is invoked when a new
        offset event is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_offset_events(self):
        """Registers for notification of updated offset events.
        ``OffsetEventReceiver.changedOffsetEvent()`` is invoked when an
        offset event is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_offset_event(self, offset_event_id):
        """Registers for notification of an updated offset event.
        ``OffsetEventReceiver.changedOffsetEvent()`` is invoked when the
        specified offset event is changed.

        :param offset_event_id: the ``Id`` of the ``OffsetEventId`` to monitor
        :type offset_event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``offset_event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_offset_events(self):
        """Registers for notification of deleted offset events.
        ``OffsetEventReceiver.deletedOffsetEvent()`` is invoked when an
        offset event is removed from this calendar.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_offset_event(self, offset_event_id):
        """Registers for notification of a deleted offset event.
        ``OffsetEventReceiver.changedOffsetEvent()`` is invoked when the
        specified offset event is removed from this calendar.

        :param offset_event_id: the ``Id`` of the ``OffsetEvent`` to monitor
        :type offset_event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``offset_eventid is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.OffsetEventCalendarSession

    def get_offset_event_ids_by_calendar(self, calendar_id):
        """Gets the list of ``OffsetEvent``  ``Ids`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related offset event ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_events_by_calendar(self, calendar_id):
        """Gets the list of ``OffsetEvents`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related offset events
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_event_ids_by_calendars(self, calendar_ids):
        """Gets the list of ``OffsetEvent Ids`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of offset event ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_offset_events_by_calendars(self, calendar_ids):
        """Gets the list of ``OffsetEvents`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of offset events
        :rtype: ``osid.calendaring.OffsetEventList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_ids_by_offset_event(self, offset_event_id):
        """Gets the list of ``Calendar``  ``Ids`` mapped to an ``OffsetEvent``.

        :param offset_event_id: ``Id`` of an ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``offset_event_id`` is not found
        :raise: ``NullArgument`` -- ``offset_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_offset_event(self, offset_e_vent_id):
        """Gets the list of ``Calendars`` mapped to an ``OffsetEvent``.

        :param offset_e_vent_id: ``Id`` of an ``OffsetEvent``
        :type offset_e_vent_id: ``osid.id.Id``
        :return: list of calendars
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``offset_event_id`` is not found
        :raise: ``NullArgument`` -- ``offset_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.OffsetEventCalendarAssignmentSession

    def can_assign_offset_events(self):
        """Tests if this user can alter offset event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_offset_events_to_calendar(self, calendar_id):
        """Tests if this user can alter offset event/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids_for_offset_event(self, calendar_id, offset_event_id):
        """Gets a list of calendars including and under the given calendar node in which a specific offset event can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param offset_event_id: the ``Id`` of the ``offset_event_id``
        :type offset_event_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``offset_event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_offset_event_to_calendar(self, offset_event_id, calendar_id):
        """Adds an existing ``OffsetEvent`` to a ``Calendar``.

        :param offset_event_id: the ``Id`` of the ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``offset_event_id`` is already assigned to ``calendar_id``
        :raise: ``NotFound`` -- ``offset_event_id`` or ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``offset_event_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_offset_event_from_calendar(self, offset_event_id, calendar_id):
        """Removes an ``OffsetEvent`` from a ``Calendar``.

        :param offset_event_id: the ``Id`` of the ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``offset_event_id`` or ``calendar_id`` not found or ``offset_event_id`` not assigned to ``calendar_id``
        :raise: ``NullArgument`` -- ``offset_event_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.OffsetEventSmartCalendarSession

    def apply_offset_event_query(self, offset_event_query):
        """Applies an offset event query to this calendar.

        :param offset_event_query: the offset event query
        :type offset_event_query: ``osid.calendaring.OffsetEventQuery``
        :raise: ``NullArgument`` -- ``offset_event_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``offset_event_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_offset_event_query(self):
        """Gets an offset event query inspector for this calendar.

        :return: the offset event query inspector
        :rtype: ``osid.calendaring.OffsetEventQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_offset_event_sequencing(self, offset_event_search_order):
        """Applies an offset event search order to this calendar.

        :param offset_event_search_order: the offset event search order
        :type offset_event_search_order: ``osid.calendaring.OffsetEventSearchOrder``
        :raise: ``NullArgument`` -- ``offset_event_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``offset_event_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleLookupSession

    def can_lookup_schedules(self):
        """Tests if this user can perform ``Schedule`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_schedule_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_schedule_view(self):
        """A complete view of the ``Schedule`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_schedule(self, schedule_id):
        """Gets the ``Schedule`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Schedule`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Schedule`` and retained for
        compatibility.

        :param schedule_id: ``Id`` of the ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :return: the schedule
        :rtype: ``osid.calendaring.Schedule``
        :raise: ``NotFound`` -- ``schedule_id`` not found
        :raise: ``NullArgument`` -- ``schedule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_by_ids(self, schedule_ids):
        """Gets a ``ScheduleList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the schedule
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Schedules`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param schedule_ids: the list of ``Ids`` to retrieve
        :type schedule_ids: ``osid.id.IdList``
        :return: the returned ``Schedule`` list
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``schedule_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_by_genus_type(self, schedule_genus_type):
        """Gets a ``ScheduleList`` corresponding to the given schedule genus ``Type`` which does not include schedule of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known schedule
        or an error results. Otherwise, the returned list may contain
        only those schedule that are accessible through this session.

        :param schedule_genus_type: a schedule genus type
        :type schedule_genus_type: ``osid.type.Type``
        :return: the returned ``Schedule`` list
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NullArgument`` -- ``schedule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_by_parent_genus_type(self, schedule_genus_type):
        """Gets a ``ScheduleList`` corresponding to the given schedule genus ``Type`` and include any additional schedule with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known schedule
        or an error results. Otherwise, the returned list may contain
        only those schedule that are accessible through this session.

        :param schedule_genus_type: a schedule genus type
        :type schedule_genus_type: ``osid.type.Type``
        :return: the returned ``Schedule`` list
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NullArgument`` -- ``schedule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_by_record_type(self, schedule_record_type):
        """Gets a ``ScheduleList`` containing the given schedule record ``Type``.
        In plenary mode, the returned list contains all known schedule
        or an error results. Otherwise, the returned list may contain
        only those schedule that are accessible through this session.

        :param schedule_record_type: a schedule record type
        :type schedule_record_type: ``osid.type.Type``
        :return: the returned ``Schedule`` list
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NullArgument`` -- ``schedule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_for_location(self, location_id):
        """Gets a ``ScheduleList`` containing the given location.
        In plenary mode, the returned list contains all known schedule
        or an error results. Otherwise, the returned list may contain
        only those schedule that are accessible through this session.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :return: the returned ``Schedule`` list
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_by_date(self, date):
        """Gets a ``ScheduleList`` containing the given date.
        In plenary mode, the returned list contains all known schedule
        or an error results. Otherwise, the returned list may contain
        only those schedule that are accessible through this session.

        :param date: a date
        :type date: ``osid.calendaring.DateTime``
        :return: the returned ``Schedule`` list
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NullArgument`` -- ``date`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_by_date_range(self, from_, to):
        """Gets a ``ScheduleList`` contained by the given date range inclusive.
        In plenary mode, the returned list contains all known schedule
        or an error results. Otherwise, the returned list may contain
        only those schedule that are accessible through this session.

        :param from: start of date range
        :type from: ``osid.calendaring.DateTime``
        :param to: end of date range
        :type to: ``osid.calendaring.DateTime``
        :return: the returned ``Schedule`` list
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules(self):
        """Gets all ``Schedules``.
        In plenary mode, the returned list contains all known schedule
        or an error results. Otherwise, the returned list may contain
        only those schedule that are accessible through this session.

        :return: a ``ScheduleList``
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    schedules = property(fget=get_schedules)


##
# The following methods are from osid.calendaring.ScheduleQuerySession

    def can_search_schedules(self):
        """Tests if this user can perform ``Schedules`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_schedule_query(self):
        """Gets a schedule query.

        :return: the schedule query
        :rtype: ``osid.calendaring.ScheduleQuery``

        """
        raise UNIMPLEMENTED()

    schedule_query = property(fget=get_schedule_query)

    def get_schedules_by_query(self, schedule_query):
        """Gets a list of ``Schedules`` matching the given schedle query.

        :param schedule_query: the schedule query
        :type schedule_query: ``osid.calendaring.ScheduleQuery``
        :return: the returned ``ScheduleList``
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NullArgument`` -- ``schedule_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSearchSession

    def get_schedule_search(self):
        """Gets a schedule search.

        :return: the schedule search
        :rtype: ``osid.calendaring.ScheduleSearch``

        """
        raise UNIMPLEMENTED()

    schedule_search = property(fget=get_schedule_search)

    def get_schedule_search_order(self):
        """Gets a schedule search order.
        The ``ScheduleSearchOrder`` is supplied to a ``ScheduleSearch``
        to specify the ordering of results.

        :return: the schedule search order
        :rtype: ``osid.calendaring.ScheduleSearchOrder``

        """
        raise UNIMPLEMENTED()

    schedule_search_order = property(fget=get_schedule_search_order)

    def get_schedules_by_search(self, schedule_query, schedule_search):
        """Gets the search results matching the given search query using the given search.

        :param schedule_query: the schedule query
        :type schedule_query: ``osid.calendaring.ScheduleQuery``
        :param schedule_search: the schedule search
        :type schedule_search: ``osid.calendaring.ScheduleSearch``
        :return: the schedule search results
        :rtype: ``osid.calendaring.ScheduleSearchResults``
        :raise: ``NullArgument`` -- ``schedule_query`` or ``schedule_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_search`` or ``schedule_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_schedule_query_from_inspector(self, schedule_query_inspector):
        """Gets a schedule query from an inspector.
        The inspector is available from an ``ScheduleSearchResults``.

        :param schedule_query_inspector: a schedule query inspector
        :type schedule_query_inspector: ``osid.calendaring.ScheduleQueryInspector``
        :return: the schedule query
        :rtype: ``osid.calendaring.ScheduleQuery``
        :raise: ``NullArgument`` -- ``schedule_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``schedule_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleAdminSession

    def can_create_schedules(self):
        """Tests if this user can create ``Schedules``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Schedule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Schedule`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_schedule_with_record_types(self, schedule_record_types):
        """Tests if this user can create a single ``Schedule`` using the desired record types.
        While ``CalendaringManager.getScheduleRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Schedule``. Providing an empty array tests if a ``Schedule``
        can be created with no records.

        :param schedule_record_types: array of schedule record types
        :type schedule_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Schedule`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_schedule_form_for_create(self, schedule_slot_id, time_period_id, schedule_record_types):
        """Gets the schedule form for creating new schedules.
        A new form should be requested for each create transaction.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param time_period_id: the ``Id`` of the ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :param schedule_record_types: array of schedule record types
        :type schedule_record_types: ``osid.type.Type[]``
        :return: the schedule form
        :rtype: ``osid.calendaring.ScheduleForm``
        :raise: ``NotFound`` -- ``schedule_slot_id`` or ``time_period_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_slot_id`` or ``time_period_id`` or ``schedule_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_schedule(self, schedule_form):
        """Creates a new ``Schedule``.

        :param schedule_form: the form for this ``Schedule``
        :type schedule_form: ``osid.calendaring.ScheduleForm``
        :return: the new ``Schedule``
        :rtype: ``osid.calendaring.Schedule``
        :raise: ``IllegalState`` -- ``schedule_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``schedule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_form`` did not originate from ``get_schedule_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def create_adhoc_schedule(self, schedule_slot_id, start, end, schedule_form):
        """Creates a new ``Schedule``.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param start: the start date
        :type start: ``osid.calendaring.DateTime``
        :param end: the end date
        :type end: ``osid.calendaring.DateTime``
        :param schedule_form: the form for this ``Schedule``
        :type schedule_form: ``osid.calendaring.ScheduleForm``
        :return: the new ``Schedule``
        :rtype: ``osid.calendaring.Schedule``
        :raise: ``AlreadyExists`` -- attempt at duplicating a property the underlying system is enforcing to be unique
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NotFound`` -- ``schedule_slot_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_slot_id, start, end`` or ``schedule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_form`` is not of this service

        """
        raise UNIMPLEMENTED()

    def can_update_schedules(self):
        """Tests if this user can update ``Schedules``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Schedule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if schedule modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_schedule_form_for_update(self, schedule_id):
        """Gets the schedule form for updating an existing schedules.
        A new schedule form should be requested for each update
        transaction.

        :param schedule_id: the ``Id`` of the ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :return: the schedule form
        :rtype: ``osid.calendaring.ScheduleForm``
        :raise: ``NotFound`` -- ``schedule_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_schedule(self, schedule_form):
        """Updates an existing schedule.

        :param schedule_form: the form containing the elements to be updated
        :type schedule_form: ``osid.calendaring.ScheduleForm``
        :raise: ``IllegalState`` -- ``schedule_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``schedule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_form`` did not originate from ``get_schedule_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def update_adhoc_schedule(self, schedule_id, start, end, schedule_form):
        """Updates an existing schedule.

        :param schedule_id: the ``Id`` of the ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :param start: the start date
        :type start: ``osid.calendaring.DateTime``
        :param end: the end date
        :type end: ``osid.calendaring.DateTime``
        :param schedule_form: the form containing the elements to be updated
        :type schedule_form: ``osid.calendaring.ScheduleForm``
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NotFound`` -- ``schedule_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_id, start, end`` or ``schedule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_form`` is not supported

        """
        raise UNIMPLEMENTED()

    def can_delete_schedules(self):
        """Tests if this user can delete ``Schedules``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Schedule`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Schedule`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_schedule(self, schedule_id):
        """Deletes the ``Schedule`` identified by the given ``Id``.

        :param schedule_id: the ``Id`` of the ``Schedule`` to delete
        :type schedule_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Schedule`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``schedule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_schedule_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Schedules``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Schedule`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_schedule(self, schedule_id, alias_id):
        """Adds an ``Id`` to a ``Schedule`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Schedule`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another schedule, it is
        reassigned to the given schedule ``Id``.

        :param schedule_id: the ``Id`` of a ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``schedule_id`` not found
        :raise: ``NullArgument`` -- ``schedule_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleNotificationSession

    def can_register_for_schedule_notifications(self):
        """Tests if this user can register for ``Schedule`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_schedules(self):
        """Register for notifications of new schedules.
        ``ScheduleReceiver.newSchedule()`` is invoked when a new
        schedule is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_schedules(self):
        """Registers for notification of updated schedule schedules.
        ``ScheduleReceiver.changedSchedule()`` is invoked when a
        schedule is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_schedule(self, schedule_id):
        """Registers for notification of an updated schedule.
        ``ScheduleReceiver.changedSchedule()`` is invoked when the
        specified schedule is changed.

        :param schedule_id: the ``Id`` of the ``Schedule`` to monitor
        :type schedule_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``schedule_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_schedules(self):
        """Registers for notification of deleted schedules.
        ``ScheduleReceiver.deletedSchedule()`` is invoked when a
        schedule is removed from this calendar.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_schedule(self, schedule_id):
        """Registers for notification of a deleted schedule.
        ``ScheduleReceiver.changedSchedule()`` is invoked when the
        specified schedule is removed from this calendar.

        :param schedule_id: the ``Id`` of the ``Schedule`` to monitor
        :type schedule_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``schedule_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleCalendarSession

    def can_lookup_schedule_calendar_mappings(self):
        """Tests if this user can perform lookups of schedule/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_schedule_ids_by_calendar(self, calendar_id):
        """Gets the list of ``Schedule``  ``Ids`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related schedule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_by_calendar(self, calendar_id):
        """Gets the list of ``Schedules`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related schedules
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_ids_by_calendars(self, calendar_ids):
        """Gets the list of ``Schedule Ids`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of schedule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedules_by_calendars(self, calendar_ids):
        """Gets the list of ``Schedules`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of schedules
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_ids_by_schedule(self, schedule_id):
        """Gets the list of ``Calendar``  ``Ids`` mapped to a ``Schedule``.

        :param schedule_id: ``Id`` of a ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``schedule_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_schedule(self, schedule_id):
        """Gets the list of ``Calendars`` mapped to a ``Schedule``.

        :param schedule_id: ``Id`` of a ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :return: list of calendars
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``schedule_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleCalendarAssignmentSession

    def can_assign_schedules(self):
        """Tests if this user can alter schedule/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_schedules_to_calendar(self, calendar_id):
        """Tests if this user can alter schedule/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids_for_schedule(self, calendar_id, schedule_id):
        """Gets a list of calendars including and under the given calendar node in which a specific schedule can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param schedule_id: the ``Id`` of the ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``schedule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_schedule_to_calendar(self, schedule_id, calendar_id):
        """Adds an existing ``Schedule`` to a ``Calendar``.

        :param schedule_id: the ``Id`` of the ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``schedule_id`` is already assigned to ``calendar_id``
        :raise: ``NotFound`` -- ``schedule_id`` or ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_schedule_from_calendar(self, schedule_id, calendar_id):
        """Removes a ``Schedule`` from a ``Calendar``.

        :param schedule_id: the ``Id`` of the ``Schedule``
        :type schedule_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``schedule_id`` or ``calendar_id`` not found or ``schedule_id`` not assigned to ``calendar_id``
        :raise: ``NullArgument`` -- ``schedule_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSmartCalendarSession

    def apply_schedule_query(self, schedule_query):
        """Applies a schedule query to this calendar.

        :param schedule_query: the schedule query
        :type schedule_query: ``osid.calendaring.ScheduleQuery``
        :raise: ``NullArgument`` -- ``schedule_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``schedule_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_schedule_query(self):
        """Gets a schedule query inspector for this calendar.

        :return: the schedule query inspector
        :rtype: ``osid.calendaring.ScheduleQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_schedule_sequencing(self, schedule_search_order):
        """Applies a schedule search order to this calendar.

        :param schedule_search_order: the schedule search order
        :type schedule_search_order: ``osid.calendaring.ScheduleSearchOrder``
        :raise: ``NullArgument`` -- ``schedule_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``schedule_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSlotLookupSession

    def can_lookup_schedule_slots(self):
        """Tests if this user can perform ``ScheduleSlot`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_schedule_slot_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_schedule_slot_view(self):
        """A complete view of the ``ScheduleSlot`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_sequestered_schedule_slot_view(self):
        """The returns from the lookup methods omit sequestered schedule slots."""
        raise UNIMPLEMENTED()

    def use_unsequestered_schedule_slot_view(self):
        """All schedule slots are returned including sequestered schedule slots."""
        raise UNIMPLEMENTED()

    def get_schedule_slot(self, schedule_slot_id):
        """Gets the ``ScheduleSlot`` specified by its ``Id``.

        :param schedule_slot_id: ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :return: the schedule slot
        :rtype: ``osid.calendaring.ScheduleSlot``
        :raise: ``NotFound`` -- ``schedule_slot_id`` not found
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots_by_ids(self, schedule_slot_ids):
        """Gets a ``ScheduleSlotList`` corresponding to the given ``IdList``.

        :param schedule_slot_ids: the list of ``Ids`` to retrieve
        :type schedule_slot_ids: ``osid.id.IdList``
        :return: the returned ``ScheduleSlot`` list
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``schedule_slot_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots_by_genus_type(self, schedule_slot_genus_type):
        """Gets a ``ScheduleSlotList`` corresponding to the given schedule slot genus ``Type`` which does not include schedule slots of genus types derived from the specified ``Type``.

        :param schedule_slot_genus_type: a schedule slot genus type
        :type schedule_slot_genus_type: ``osid.type.Type``
        :return: the returned ``ScheduleSlot`` list
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``NullArgument`` -- ``schedule_slot_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots_by_parent_genus_type(self, schedule_slot_genus_type):
        """Gets a ``ScheduleSlotList`` corresponding to the given schedule slot genus ``Type`` and include any additional schedule slots with genus types derived from the specified ``Type``.

        :param schedule_slot_genus_type: a schedule slot genus type
        :type schedule_slot_genus_type: ``osid.type.Type``
        :return: the returned ``ScheduleSlot`` list
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``NullArgument`` -- ``schedule_slot_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots_by_record_type(self, schedule_slot_record_type):
        """Gets a ``ScheduleSlotList`` containing the given schedule record ``Type``.

        :param schedule_slot_record_type: a schedule slot record type
        :type schedule_slot_record_type: ``osid.type.Type``
        :return: the returned ``ScheduleSlot`` list
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``NullArgument`` -- ``schedule_slot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots_by_weekdays(self, weekdays):
        """Gets a ``ScheduleSlotList`` containing the given set of weekdays.

        :param weekdays: a set of weekdays
        :type weekdays: ``cardinal[]``
        :return: the returned ``ScheduleSlot`` list
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``InvalidArgument`` -- a ``weekday`` is negative
        :raise: ``NullArgument`` -- ``weekdays`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots_by_time(self, time):
        """Gets a ``ScheduleSlotList`` matching the given time.

        :param time: a time
        :type time: ``osid.calendaring.Time``
        :return: the returned ``ScheduleSlot`` list
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``NullArgument`` -- ``time`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots(self):
        """Gets all ``ScheduleSlots``.

        :return: a ``ScheduleSlotList``
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    schedule_slots = property(fget=get_schedule_slots)


##
# The following methods are from osid.calendaring.ScheduleSlotQuerySession

    def can_search_schedule_slots(self):
        """Tests if this user can perform ``ScheduleSlots`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_query(self):
        """Gets a schedule slot query.

        :return: the schedule slot query
        :rtype: ``osid.calendaring.ScheduleSlotQuery``

        """
        raise UNIMPLEMENTED()

    schedule_slot_query = property(fget=get_schedule_slot_query)

    def get_schedule_slots_by_query(self, schedule_slot_query):
        """Gets a list of ``ScheduleSlots`` matching the given schedule slot query.

        :param schedule_slot_query: the schedule slot query
        :type schedule_slot_query: ``osid.calendaring.ScheduleSlotQuery``
        :return: the returned ``ScheduleSlotList``
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``NullArgument`` -- ``schedule_slot_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_slot_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSlotSearchSession

    def get_schedule_slot_search(self):
        """Gets a schedule slot search.

        :return: the schedule slot search
        :rtype: ``osid.calendaring.ScheduleSlotSearch``

        """
        raise UNIMPLEMENTED()

    schedule_slot_search = property(fget=get_schedule_slot_search)

    def get_schedule_slot_search_order(self):
        """Gets a schedule slot search order.
        The ``ScheduleSlotSearchOrder`` is supplied to a
        ``ScheduleSlotSearch`` to specify the ordering of results.

        :return: the schedule slot search order
        :rtype: ``osid.calendaring.ScheduleSlotSearchOrder``

        """
        raise UNIMPLEMENTED()

    schedule_slot_search_order = property(fget=get_schedule_slot_search_order)

    def get_schedule_slots_by_search(self, schedule_slot_query, schedule_slot_search):
        """Gets the search results matching the given search query using the given search.

        :param schedule_slot_query: the schedule slot query
        :type schedule_slot_query: ``osid.calendaring.ScheduleSlotQuery``
        :param schedule_slot_search: the schedule slot search
        :type schedule_slot_search: ``osid.calendaring.ScheduleSlotSearch``
        :return: the schedule slot search results
        :rtype: ``osid.calendaring.ScheduleSearchResults``
        :raise: ``NullArgument`` -- ``schedule_slot_query`` or ``schedule_slot_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_slot_search`` or ``schedule_slot_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_query_from_inspector(self, schedule_slot_query_inspector):
        """Gets a schedule slot query from an inspector.
        The inspector is available from an
        ``ScheduleSlotSearchResults``.

        :param schedule_slot_query_inspector: a schedule slot query inspector
        :type schedule_slot_query_inspector: ``osid.calendaring.ScheduleSlotQueryInspector``
        :return: the schedule query
        :rtype: ``osid.calendaring.ScheduleSlotQuery``
        :raise: ``NullArgument`` -- ``schedule_slot_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``schedule_slot_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSlotAdminSession

    def can_create_schedule_slots(self):
        """Tests if this user can create ``ScheduleSlots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``ScheduleSlot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``ScheduleSlot`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_schedule_slot_with_record_types(self, schedule_slot_record_types):
        """Tests if this user can create a single ``ScheduleSlot`` using the desired record types.
        While ``CalendaringManager.getScheduleSlotRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``ScheduleSlot``. Providing an empty array tests if a
        ``ScheduleSlot`` can be created with no records.

        :param schedule_slot_record_types: array of schedule slot record types
        :type schedule_slot_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``ScheduleSlot`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_slot_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_form_for_create(self, schedule_slot_record_types):
        """Gets the schedule slot form for creating new schedule slots.
        A new form should be requested for each create transaction.

        :param schedule_slot_record_types: array of schedule slot record types
        :type schedule_slot_record_types: ``osid.type.Type[]``
        :return: the schedule slot form
        :rtype: ``osid.calendaring.ScheduleSlotForm``
        :raise: ``NullArgument`` -- ``schedule_slot_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_schedule_slot(self, schedule_slot_form):
        """Creates a new ``ScheduleSlot``.

        :param schedule_slot_form: the form for this ``ScheduleSlot``
        :type schedule_slot_form: ``osid.calendaring.ScheduleSlotForm``
        :return: the new ``ScheduleSlot``
        :rtype: ``osid.calendaring.ScheduleSlot``
        :raise: ``IllegalState`` -- ``schedule_slot_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``schedule_slot_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_slot_form`` did not originate from ``get_schedule_slot_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_schedule_slots(self):
        """Tests if this user can update ``ScheduleSlots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``ScheduleSlot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if schedule slot modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_form_for_update(self, schedule_slot_id):
        """Gets the schedule slot form for updating an existing schedule slot.
        A new schedule slot form should be requested for each update
        transaction.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :return: the schedule slot form
        :rtype: ``osid.calendaring.ScheduleSlotForm``
        :raise: ``NotFound`` -- ``schedule_slot_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_schedule_slot(self, schedule_slot_form):
        """Updates an existing schedule slot.

        :param schedule_slot_form: the form containing the elements to be updated
        :type schedule_slot_form: ``osid.calendaring.ScheduleSlotForm``
        :raise: ``IllegalState`` -- ``schedule_slot_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``schedule_slot_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``schedule_slot_form`` did not originate from ``get_schedule_slot_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_schedule_slots(self):
        """Tests if this user can delete ``ScheduleSlots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``ScheduleSlot`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``ScheduleSlot`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_schedule_slot(self, schedule_slot_id):
        """Deletes the ``ScheduleSlot`` identified by the given ``Id``.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot`` to delete
        :type schedule_slot_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``ScheduleSlot`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_schedule_slot_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``ScheduleSlots``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``ScheduleSlot`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_schedule_slot(self, schedule_slot_id, alias_id):
        """Adds an ``Id`` to a ``ScheduleSlot`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``ScheduleSlot`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another schedule slot, it
        is reassigned to the given schedule slot ``Id``.

        :param schedule_slot_id: the ``Id`` of a ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``schedule_slot_id`` not found
        :raise: ``NullArgument`` -- ``schedule_slot_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSlotNotificationSession

    def can_register_for_schedule_slot_notifications(self):
        """Tests if this user can register for ``ScheduleSlot`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_schedule_slots(self):
        """Register for notifications of new schedule slots.
        ``ScheduleSlotReceiver.newScheduleSlot()`` is invoked when a new
        schedule slot is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_schedule_slot_ancestors(self, schedule_slot_id):
        """Registers for notification if an ancestor is added to the specified schedule slot in the scheduls slot composition.
        ``SchedulesSlotReceiver.newScheduleSlotAncestor()`` is invoked
        when the specified scheduls slot experiences an addition in
        ancestors.

        :param schedule_slot_id: the ``Id`` of the schedule slot to monitor
        :type schedule_slot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_schedule_slot_descendants(self, schedule_slot_id):
        """Registers for notification if a descendant is added to the specified schedule slot in the scheduls slot composition.
        ``SchedulesSlotReceiver.newScheduleSlotDescendant()`` is invoked
        when the specified scheduls slot experiences an addition in
        descendants.

        :param schedule_slot_id: the ``Id`` of the schedule slot to monitor
        :type schedule_slot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_schedule_slots(self):
        """Registers for notification of updated schedule schedule slots.
        ``ScheduleSlotReceiver.changedScheduleSlot()`` is invoked when a
        schedule slot is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_schedule_slot(self, schedule_slot_id):
        """Registers for notification of an updated schedule slot.
        ``ScheduleSlotReceiver.changedSchedulSlote()`` is invoked when
        the specified schedule slot is changed.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot`` to monitor
        :type schedule_slot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``schedule_slot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_schedule_slots(self):
        """Registers for notification of deleted schedule slots.
        ``ScheduleSlotReceiver.deletedScheduleSlot()`` is invoked when a
        schedule slot is removed from this calendar.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_schedule_slot(self, schedule_slot_id):
        """Registers for notification of a deleted schedule slot.
        ``ScheduleSlotReceiver.changedScheduleSlot()`` is invoked when
        the specified schedule slot is removed from this calendar.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot`` to monitor
        :type schedule_slot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``schedule_slot_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_schedule_slot_ancestors(self, schedule_slot_id):
        """Registers for notification if an ancestor removed from to the specified schedule slot in the schedule slot composition.
        ``ScheduleSlotReceiver.deletedScheduleSlotAncestor()`` is
        invoked when the specified scheduls slot experiences a removal
        of an ancestor.

        :param schedule_slot_id: the ``Id`` of the schedule slot to monitor
        :type schedule_slot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_schedule_slot_descendants(self, schedule_slot_id):
        """Registers for notification if a descendant removed from to the specified schedule slot in the schedule slot composition.
        ``ScheduleSlotReceiver.deletedScheduleSlotDescendant()`` is
        invoked when the specified scheduls slot experiences a removal
        of a descendant.

        :param schedule_slot_id: the ``Id`` of the schedule slot to monitor
        :type schedule_slot_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSlotCalendarSession

    def can_lookup_schedule_slot_calendar_mappings(self):
        """Tests if this user can perform lookups of schedule slot/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_ids_by_calendar(self, calendar_id):
        """Gets the list of ``ScheduleSlot``  ``Ids`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related schedule slot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots_by_calendar(self, calendar_id):
        """Gets the list of ``ScheduleSlots`` associated with a ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related schedule slot
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slot_ids_by_calendars(self, calendar_ids):
        """Gets the list of ``ScheduleSlot Ids`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of schedule slot ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_schedule_slots_by_calendars(self, calendar_ids):
        """Gets the list of ``ScheduleSlots`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of schedule slots
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_ids_by_schedule_slot(self, schedule_slot_id):
        """Gets the list of ``Calendar``  ``Ids`` mapped to a ``ScheduleSlot``.

        :param schedule_slot_id: ``Id`` of a ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``schedule_slot_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_schedule_slot(self, schedule_slot_id):
        """Gets the list of ``Calendars`` mapped to a ``ScheduleSlot``.

        :param schedule_slot_id: ``Id`` of a ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :return: list of calendars
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``schedule_slot_id`` is not found
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSlotCalendarAssignmentSession

    def can_assign_schedule_slots(self):
        """Tests if this user can alter schedule slot/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_schedule_slots_to_calendar(self, calendar_id):
        """Tests if this user can alter schedule slot/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a PERMISSION_DENIED. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids_for_schedule_slot(self, calendar_id, schedule_slot_id):
        """Gets a list of calendars including and under the given calendar node in which a specific schedule slot can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``schedule_slot_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_schedule_slot_to_calendar(self, schedule_slot_id, calendar_id):
        """Adds an existing ``ScheduleSlot`` to a ``Calendar``.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``schedule_slot_id`` is already assigned to ``calendar_id``
        :raise: ``NotFound`` -- ``schedule_slot_id`` or ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``schedule_slot_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_schedule_slot_from_calendar(self, schedule_slot_id, calendar_id):
        """Removes a ``ScheduleSlot`` from a ``Calendar``.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``schedule_slot_id`` or ``calendar_id`` not found or ``schedule_slot_id`` not assigned to ``calendar_id``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.ScheduleSlotSmartCalendarSession

    def apply_schedule_slot_query(self, schedule_slot_query):
        """Applies a schedule slot query to this calendar.

        :param schedule_slot_query: the schedule slot query
        :type schedule_slot_query: ``osid.calendaring.ScheduleSlotQuery``
        :raise: ``NullArgument`` -- ``schedule_slot_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``schedule_slot_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_schedule_slot_query(self):
        """Gets a schedule slot query inspector for this calendar.

        :return: the schedule slot query inspector
        :rtype: ``osid.calendaring.ScheduleSlotQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_schedule_slot_sequencing(self, schedule_slot_search_order):
        """Applies a schedule slot search order to this calendar.

        :param schedule_slot_search_order: the schedule slot search order
        :type schedule_slot_search_order: ``osid.calendaring.ScheduleSlotSearchOrder``
        :raise: ``NullArgument`` -- ``schedule_slot_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``schedule_slot_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CommitmentLookupSession

    def can_lookup_commitments(self):
        """Tests if this user can lookup event commitments.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_commitment_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_commitment_view(self):
        """A complete view of the ``Commitment`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_effective_commitment_view(self):
        """The commitments in this lookup session return only commitments currently in effect."""
        raise UNIMPLEMENTED()

    def use_any_effective_commitment_view(self):
        """The commitments in this lookup session return both effective and ineffective commitments."""
        raise UNIMPLEMENTED()

    def get_commitment(self, commitment_id):
        """Gets the ``Commitment`` specified by its ``Id``.

        :param commitment_id: ``Id`` of the ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :return: the commitment
        :rtype: ``osid.calendaring.Commitment``
        :raise: ``NotFound`` -- ``commitment_id`` not found
        :raise: ``NullArgument`` -- ``commitment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_ids(self, commitment_ids):
        """Gets a ``CommitmentList`` corresponding to the given ``IdList``.

        :param commitment_ids: the list of ``Ids`` to retrieve
        :type commitment_ids: ``osid.id.IdList``
        :return: the returned ``Commitment`` list
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``commitment_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_genus_type(self, commitment_genus_type):
        """Gets the commitments for the given event genus type.

        :param commitment_genus_type: commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``commitment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_parent_genus_type(self, commitment_genus_type):
        """Gets the commitments for the given event genus type and include any commitments with a genus type derived from the specified genus type.

        :param commitment_genus_type: commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``commitment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_record_type(self, commitment_record_type):
        """Gets a ``CommitmentList`` containing the given event commitment record ``Type``.

        :param commitment_record_type: a commitment record type
        :type commitment_record_type: ``osid.type.Type``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_on_date(self, from_, to):
        """Gets a ``CommitmentList`` effective during the entire given date range inclusive but not confined to the date range.

        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_genus_type_on_date(self, commitment_genus_type, from_, to):
        """Gets a ``CommitmentList`` of the given genus type and effective during the entire given date range inclusive but not confined to the date range.

        :param commitment_genus_type: a commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``commitment_genus_type, from,`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_for_event(self, event_id):
        """Gets the commitments for the given event.
        If the event is a recurring event, the commitments are returned
        for the recurring event only.

        In plenary mode, the returned list contains all of the
        commitments mapped to the event ``Id`` or an error results if an
        Id in the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Commitments`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.
        
        In effective mode, commitments are returned that are currently
        effective. In any effective mode, effective commitments and
        those currently expired are returned.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_for_event_on_date(self, event_id, from_, to):
        """Gets a ``CommitmentList`` for the given event and effective during the entire given date range inclusive but not confined to the date range.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``event_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_genus_type_for_event(self, event_id, commitment_genus_type):
        """Gets the commitments for the given event and commitment genus type including any genus types derived from the given genus type.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param commitment_genus_type: commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``event_id`` or ``commitment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_genus_type_for_event_on_date(self, event_id, commitment_genus_type, from_, to):
        """Gets a ``CommitmentList`` for the given event and commitment genus type effective during the entire given date range inclusive but not confined to the date range.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param commitment_genus_type: commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``event_id, commitment_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_for_resource(self, resource_id):
        """Gets the commitments for the given resource.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_for_resource_on_date(self, resource_id, from_, to):
        """Gets a ``CommitmentList`` for the given resource and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: ``Id`` of the ``Event``
        :type resource_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_genus_type_for_resource(self, resource_id, commitment_genus_type):
        """Gets the commitments for the given resource and commitment genus type including any genus types derived from the given genus type.

        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param commitment_genus_type: commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``resource_id`` or ``commitment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_genus_type_for_resource_on_date(self, resource_id, commitment_genus_type, from_, to):
        """Gets a ``CommitmentList`` for the given resource, commitment genus type, and effective during the entire given date range inclusive but not confined to the date range.

        :param resource_id: ``Id`` of the ``Event``
        :type resource_id: ``osid.id.Id``
        :param commitment_genus_type: commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``resource_id, commitment_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_for_event_and_resource(self, event_id, resource_id):
        """Gets the commitments for the given event and resource.
        If the event is a recurring event, the commitments are returned
        for the recurring event only.

        In plenary mode, the returned list contains all of the
        commitments mapped to the event ``Id`` or an error results if an
        Id in the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Commitments`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.
        
        In effective mode, commitments are returned that are currently
        effective. In any effective mode, effective commitments and
        those currently expired are returned.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``event_id`` or ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_for_event_and_resource_on_date(self, event_id, resource_id, from_, to):
        """Gets a ``CommitmentList`` for the given event and resource and effective during the entire given date range inclusive but not confined to the date range.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``event_id, resource_id, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_genus_type_for_event_and_resource(self, event_id, resource_id, commitment_genus_type):
        """Gets the commitmentsof the given genus type for the given event, resource, and commitment genus type including any genus types derived from the given genus type.
        . If the event is a recurring event, the commitments are
        returned for the recurring event only.

        In plenary mode, the returned list contains all of the
        commitments mapped to the event ``Id`` or an error results if an
        Id in the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Commitments`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.
        
        In effective mode, commitments are returned that are currently
        effective. In any effective mode, effective commitments and
        those currently expired are returned.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param commitment_genus_type: commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``event_id, resource_id`` or ``commitment_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_genus_type_for_event_and_resource_on_date(self, event_id, resource_id, commitment_genus_type, from_, to):
        """Gets a ``CommitmentList`` of the given genus type for the given event, resource, commitment genus type and effective during the entire given date range inclusive but not confined to the date range.

        :param event_id: ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param resource_id: ``Id`` of a ``Resource``
        :type resource_id: ``osid.id.Id``
        :param commitment_genus_type: commitment genus type
        :type commitment_genus_type: ``osid.type.Type``
        :param from: starting date
        :type from: ``osid.calendaring.DateTime``
        :param to: ending date
        :type to: ``osid.calendaring.DateTime``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``event_id, resource_id, commitment_genus_type, from`` or ``to`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments(self):
        """Gets all commitments.

        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    commitments = property(fget=get_commitments)


##
# The following methods are from osid.calendaring.CommitmentQuerySession

    def can_search_commitments(self):
        """Tests if this user can perform ``Commitment`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_commitment_query(self):
        """Gets a commitment query.

        :return: the commitment query
        :rtype: ``osid.calendaring.CommitmentQuery``

        """
        raise UNIMPLEMENTED()

    commitment_query = property(fget=get_commitment_query)

    def get_commitments_by_query(self, commitment_query):
        """Gets a list of ``Commitments`` matching the given commitment query.

        :param commitment_query: the commitment query
        :type commitment_query: ``osid.calendaring.CommitmentQuery``
        :return: the returned ``CommitmentList``
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``commitment_query is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``commitment_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CommitmentSearchSession

    def get_commitment_search(self):
        """Gets a commitment search.

        :return: the commitment search
        :rtype: ``osid.calendaring.CommitmentSearch``

        """
        raise UNIMPLEMENTED()

    commitment_search = property(fget=get_commitment_search)

    def get_commitment_search_order(self):
        """Gets a commitment search order.
        The ``CommitmentSearchOrder`` is supplied to a
        ``CommitmentSearch`` to specify the ordering of results.

        :return: the commitment search order
        :rtype: ``osid.calendaring.CommitmentSearchOrder``

        """
        raise UNIMPLEMENTED()

    commitment_search_order = property(fget=get_commitment_search_order)

    def get_commitments_by_search(self, commitment_query, commitment_search):
        """Gets the search results matching the given search query using the given search.

        :param commitment_query: the commitment search query
        :type commitment_query: ``osid.calendaring.CommitmentQuery``
        :param commitment_search: the commitment search
        :type commitment_search: ``osid.calendaring.CommitmentSearch``
        :return: the commitment search results
        :rtype: ``osid.calendaring.CommitmentSearchResults``
        :raise: ``NullArgument`` -- ``commitment_query`` or ``commitment_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``commitment_search`` or ``commitment_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_commitment_query_from_inspector(self, commitment_query_inspector):
        """Gets a commitment query from an inspector.
        The inspector is available from an ``CommitmentSearchResults``.

        :param commitment_query_inspector: a commitment query inspector
        :type commitment_query_inspector: ``osid.calendaring.CommitmentQueryInspector``
        :return: the commitment query
        :rtype: ``osid.calendaring.CommitmentQuery``
        :raise: ``NullArgument`` -- ``commitment_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``commitment_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CommitmentAdminSession

    def can_create_commitments(self):
        """Tests if this user can create ``Commitments``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Commitment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Commitment`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_commitment_with_record_types(self, commitment_record_types):
        """Tests if this user can create a single ``Commitment`` using the desired record types.
        While ``CalendaringManager.getCommitmentRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Commitment``. Providing an empty array tests if a
        ``Commitment`` can be created with no records.

        :param commitment_record_types: array of comitment record types
        :type commitment_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Commitment`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``commitment_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_commitment_form_for_create(self, event_id, resource_id, commitment_record_types):
        """Gets the commitment form for creating new commitments.
        A new form should be requested for each create transaction.

        :param event_id: the ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``
        :param commitment_record_types: array of comitment record types
        :type commitment_record_types: ``osid.type.Type[]``
        :return: the commitment form
        :rtype: ``osid.calendaring.CommitmentForm``
        :raise: ``NotFound`` -- ``event_id`` or ``resource_id`` is not found
        :raise: ``NullArgument`` -- ``event_id`` or ``resource_id`` or ``commitment_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested recod types

        """
        raise UNIMPLEMENTED()

    def create_commitment(self, commitment_form):
        """Creates a new ``Commitment``.

        :param commitment_form: the forms for this ``Commitment``
        :type commitment_form: ``osid.calendaring.CommitmentForm``
        :return: the new ``Commitment``
        :rtype: ``osid.calendaring.Commitment``
        :raise: ``IllegalState`` -- ``commitment_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``commitment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``commitment_form`` did not originate from ``get_commitment_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_commitments(self):
        """Tests if this user can update ``Commitments``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Commitment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if commitment modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_commitment_form_for_update(self, commitment_id):
        """Gets the commitment form for updating an existing commitment.
        A new commitment form should be requested for each update
        transaction.

        :param commitment_id: the ``Id`` of the ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :return: the commitment form
        :rtype: ``osid.calendaring.CommitmentForm``
        :raise: ``NotFound`` -- ``commitment_id`` is not found
        :raise: ``NullArgument`` -- ``commitmentid`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_commitment(self, commitment_form):
        """Updates an existing commitment.

        :param commitment_form: the form containing the elements to be updated
        :type commitment_form: ``osid.calendaring.CommitmentForm``
        :raise: ``IllegalState`` -- ``commitment_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``commitment_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``commitment_form`` did not originate from ``get_commitment_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_commitments(self):
        """Tests if this user can delete ``Commitments``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Commitment`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Commitment`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_commitment(self, commitment_id):
        """Deletes the ``Commitment`` identified by the given ``Id``.

        :param commitment_id: the ``Id`` of the ``Commitment`` to delete
        :type commitment_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Commitment`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``commitment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_commitment_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Commitments``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Commitment`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_commitment(self, commitment_id, alias_id):
        """Adds an ``Id`` to a ``Commitment`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Commitment`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another commitment, it is
        reassigned to the given commitment ``Id``.

        :param commitment_id: the ``Id`` of a ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``commitment_id`` not found
        :raise: ``NullArgument`` -- ``commitment_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CommitmentNotificationSession

    def can_register_for_commitment_notifications(self):
        """Tests if this user can register for ``Commitment`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_commitments(self):
        """Register for notifications of new commitments.
        ``CommitmentReceiver.newCommitment()`` is invoked when a new
        commitment is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_commitments_by_genus_type(self, commitment_genus_type):
        """Register for notifications of new commitments by commitment genus type.
        ``CommitmentReceiver.newCommitment()`` is invoked when a new
        commitment is created.

        :param commitment_genus_type: the commitment genus type to monitor
        :type commitment_genus_type: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``commitment_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_commitments_for_event(self, event_id):
        """Register for notifications of new commitments for the given event.
        ``CommitmentReceiver.newCommitment()`` is invoked when a new
        commitment is created.

        :param event_id: the ``Id`` of the ``Event`` to monitor
        :type event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_commitments_for_resource(self, resource_id):
        """Register for notifications of new commitments for the given resource.
        ``CommitmentReceiver.newCommitment()`` is invoked when a new
        commitment is created.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_commitments(self):
        """Registers for notification of updated commitments.
        ``CommitmentReceiver.changedCommitment()`` is invoked when a
        commitment is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_commitments_by_genus_type(self, commitment_genus_type):
        """Register for notifications of changed commitments by commitment genus type.
        ``CommitmentReceiver.changedCommitment()`` is invoked when a
        commitment is changed.

        :param commitment_genus_type: the commitment genus type to monitor
        :type commitment_genus_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``commitment_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_commitments_for_event(self, event_id):
        """Register for notifications of changed commitments for the given event.
        ``CommitmentReceiver.changedCommitment()`` is invoked when a
        commitment is changed.

        :param event_id: the ``Id`` of the ``Event`` to monitor
        :type event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_commitments_for_resource(self, resource_id):
        """Register for notifications of changed commitments for the given rsource.
        ``CommitmentReceiver.changedCommitment()`` is invoked when a
        commitment is changed.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_commitment(self, commitment_id):
        """Registers for notification of an updated commitment.
        ``CommitmentReceiver.changedCommitment()`` is invoked when the
        specified commitment is changed.

        :param commitment_id: the ``Id`` of the ``Commitment`` to monitor
        :type commitment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``commitment_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_commitments(self):
        """Registers for notification of deleted commitments.
        ``CommitmentReceiver.deletedCommitment()`` is invoked when a
        commitment is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_commitments_by_genus_type(self, commitment_genus_type):
        """Register for notifications of deleted commitments by commitment genus type.
        ``CommitmentReceiver.deletedCommitment()`` is invoked when a
        commitment is deleted.

        :param commitment_genus_type: the commitment genus type to monitor
        :type commitment_genus_type: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``commitment_genus_type is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_commitments_for_event(self, event_id):
        """Register for notifications of deleted commitments for the given event.
        ``CommitmentReceiver.deletedCommitment()`` is invoked when a
        commitment is deleted.

        :param event_id: the ``Id`` of the ``Event`` to monitor
        :type event_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``event_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_commitments_for_resource(self, resource_id):
        """Register for notifications of deleted commitments for the given rsource.
        ``CommitmentReceiver.deletedCommitment()`` is invoked when a
        commitment is deleted.

        :param resource_id: the ``Id`` of the ``Resource`` to monitor
        :type resource_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``resource_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_commitment(self, commitment_id):
        """Registers for notification of a deleted commitment.
        ``CommitmentReceiver.changedCommitment()`` is invoked when the
        specified commitment is deleted.

        :param commitment_id: the ``Id`` of the ``Commitment`` to monitor
        :type commitment_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``commitment_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CommitmentCalendarSession

    def can_lookup_commitment_calendar_mappings(self):
        """Tests if this user can perform lookups of commitment/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_commitment_ids_by_calendar(self, calendar_id):
        """Gets the list of ``Commitment``  ``Ids`` associated with an ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related commitment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_calendar(self, calendar_id):
        """Gets the list of ``Commitments`` associated with an ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitment_ids_by_calendars(self, calendar_ids):
        """Gets the list of ``Commitment Ids`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of commitment ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_commitments_by_calendars(self, calendar_ids):
        """Gets the list of ``Commitments`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of commitments
        :rtype: ``osid.calendaring.CommitmentList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_ids_by_commitment(self, commitment_id):
        """Gets the list of ``Calendar Ids`` mapped to a ``Commitment``.

        :param commitment_id: ``Id`` of a ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``commitment_id`` is not found
        :raise: ``NullArgument`` -- ``commitment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_commitment(self, commitment_id):
        """Gets the list of ``Calendars`` mapped to a ``Commitment``.

        :param commitment_id: ``Id`` of a ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``commitment_id`` is not found
        :raise: ``NullArgument`` -- ``commitment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CommitmentCalendarAssignmentSession

    def can_assign_commitments(self):
        """Tests if this user can alter commitment/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_commitments_to_calendar(self, calendar_id):
        """Tests if this user can alter commitment/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids_for_commitment(self, calendar_id, commitment_id):
        """Gets a list of calendars including and under the given calendar node in which a specific commitment can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param commitment_id: the ``Id`` of the ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``commitment_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_commitment_to_calendar(self, commitment_id, calendar_id):
        """Adds an existing ``Commitment`` to a ``Calendar``.

        :param commitment_id: the ``Id`` of the ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``commitment_id`` is already assigned to ``calendar_id``
        :raise: ``NotFound`` -- ``commitment_id`` or ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``commitment_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_commitment_from_calendar(self, commitment_id, calendar_id):
        """Removes a ``Commitment`` from a ``Calendar``.

        :param commitment_id: the ``Id`` of the ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``commitment_id`` or ``calendar_id`` not found or ``commitment_id`` not assigned to ``calendar_id``
        :raise: ``NullArgument`` -- ``commitment_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.CommitmentSmartCalendarSession

    def apply_commitment_query(self, commitment_query):
        """Applies a commitment query to this calendar.

        :param commitment_query: the commitment query
        :type commitment_query: ``osid.calendaring.CommitmentQuery``
        :raise: ``NullArgument`` -- ``commitment_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``commitment_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_commitment_query(self):
        """Gets a commitment query inspector for this calendar.

        :return: the commitment query inspector
        :rtype: ``osid.calendaring.CommitmentQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_commitment_sequencing(self, commitment_search_order):
        """Applies a commitment search order to this calendar.

        :param commitment_search_order: the commitment search order
        :type commitment_search_order: ``osid.calendaring.CommitmentSearchOrder``
        :raise: ``NullArgument`` -- ``commitment_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``commitment_search_order`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.TimePeriodLookupSession

    def can_lookup_time_periods(self):
        """Tests if this user can perform ``TimePeriod`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_time_period_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_time_period_view(self):
        """A complete view of the ``TimePeriod`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_time_period(self, time_period_id):
        """Gets the ``TimePeriod`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``TimePeriod`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``TimePeriod`` and retained
        for compatibility.

        :param time_period_id: ``Id`` of the ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :return: the time period
        :rtype: ``osid.calendaring.TimePeriod``
        :raise: ``NotFound`` -- ``time_period_id`` not found
        :raise: ``NullArgument`` -- ``time_period_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods_by_ids(self, time_period_ids):
        """Gets a ``TimePeriodList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the time
        periods specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``TimePeriods`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param time_period_ids: the list of ``Ids`` to retrieve
        :type time_period_ids: ``osid.id.IdList``
        :return: the returned ``TimePeriod`` list
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``rime_period_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods_by_genus_type(self, time_period_genus_type):
        """Gets a ``TimePeriodList`` corresponding to the given time period genus ``Type`` which does not include time periods of genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known time
        periods or an error results. Otherwise, the returned list may
        contain only those time periods that are accessible through this
        session.

        :param time_period_genus_type: a time period genus type
        :type time_period_genus_type: ``osid.type.Type``
        :return: the returned ``TimePeriod`` list
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``NullArgument`` -- ``time_period_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods_by_parent_genus_type(self, time_period_genus_type):
        """Gets a ``TimePeriodList`` corresponding to the given time period genus ``Type`` and include any additional time periods with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known time
        periods or an error results. Otherwise, the returned list may
        contain only those time periods that are accessible through this
        session.

        :param time_period_genus_type: a time period genus type
        :type time_period_genus_type: ``osid.type.Type``
        :return: the returned ``TimePeriod`` list
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``NullArgument`` -- ``time_period_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods_by_record_type(self, time_period_record_type):
        """Gets a ``TimePeriodList`` containing the given time period record ``Type``.
        In plenary mode, the returned list contains all known time
        periods or an error results. Otherwise, the returned list may
        contain only those time periods that are accessible through this
        session.

        :param time_period_record_type: a time period record type
        :type time_period_record_type: ``osid.type.Type``
        :return: the returned ``TimePeriod`` list
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``NullArgument`` -- ``time_period_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods_by_date(self, datetime):
        """Gets a ``TimePeriodList`` containing the given ``DateTime``.
        Time periods containing the given date are matched. In plenary
        mode, the returned list contains all of the time periods
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``TimePeriods`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param datetime: a date
        :type datetime: ``osid.calendaring.DateTime``
        :return: the returned ``TimePeriod`` list
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``NullArgument`` -- ``datetime`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods_in_date_range(self, start, end):
        """Gets a ``TimePeriodList`` corresponding to the given ``DateTime``.
        Time periods whose start end end times are included in the given
        date range are matched.In plenary mode, the returned list
        contains all of the time periods specified in the ``Id`` list,
        in the order of the list, including duplicates, or an error
        results if an ``Id`` in the supplied list is not found or
        inaccessible. Otherwise, inaccessible ``TimePeriods`` may be
        omitted from the list and may present the elements in any order
        including returning a unique set.

        :param start: start of daterange
        :type start: ``osid.calendaring.DateTime``
        :param end: end of date range
        :type end: ``osid.calendaring.DateTime``
        :return: the returned ``TimePeriod`` list
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods(self):
        """Gets all ``TimePeriods``.
        In plenary mode, the returned list contains all known time
        periods or an error results. Otherwise, the returned list may
        contain only those time periods that are accessible through this
        session.

        :return: a ``TimePeriodList``
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    time_periods = property(fget=get_time_periods)


##
# The following methods are from osid.calendaring.TimePeriodQuerySession

    def can_search_time_periods(self):
        """Tests if this user can perform ``TimePeriod`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_time_period_query(self):
        """Gets a time period query.

        :return: the time period query
        :rtype: ``osid.calendaring.TimePeriodQuery``

        """
        raise UNIMPLEMENTED()

    time_period_query = property(fget=get_time_period_query)

    def get_time_periods_by_query(self, time_period_query):
        """Gets a list of ``TimePeriods`` matching the given query.

        :param time_period_query: the time period query
        :type time_period_query: ``osid.calendaring.TimePeriodQuery``
        :return: the returned ``TimePeriodList``
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``NullArgument`` -- ``time_period_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``time_period_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.TimePeriodSearchSession

    def get_time_period_search(self):
        """Gets a time period search.

        :return: the time period search
        :rtype: ``osid.calendaring.TimePeriodSearch``

        """
        raise UNIMPLEMENTED()

    time_period_search = property(fget=get_time_period_search)

    def get_time_period_search_order(self):
        """Gets a time period search order.
        The ``TimePeriodSearchOrder`` is supplied to a
        ``TimePeriodSearch`` to specify the ordering of results.

        :return: the time period search order
        :rtype: ``osid.calendaring.TimePeriodSearchOrder``

        """
        raise UNIMPLEMENTED()

    time_period_search_order = property(fget=get_time_period_search_order)

    def get_time_periods_by_search(self, time_period_query, time_period_search):
        """Gets the search results matching the given search query using the given search.

        :param time_period_query: the time period query
        :type time_period_query: ``osid.calendaring.TimePeriodQuery``
        :param time_period_search: the time period search
        :type time_period_search: ``osid.calendaring.TimePeriodSearch``
        :return: the time period search results
        :rtype: ``osid.calendaring.TimePeriodSearchResults``
        :raise: ``NullArgument`` -- ``time_period_query`` or ``time_period_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``time_period_search`` or t ``ime_period_query`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_time_period_query_from_inspector(self, time_period_query_inspector):
        """Gets a time period query from an inspector.
        The inspector is available from a ``TimePeriodSearchResults``.

        :param time_period_query_inspector: a time period query inspector
        :type time_period_query_inspector: ``osid.calendaring.TimePeriodQueryInspector``
        :return: the time period query
        :rtype: ``osid.calendaring.TimePeriodQuery``
        :raise: ``NullArgument`` -- ``time_period_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``time_period_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.TimePeriodAdminSession

    def can_create_time_periods(self):
        """Tests if this user can create ``TimePeriods``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a TimePeriod
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``TimePeriod`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_time_period_with_record_types(self, time_period_record_types):
        """Tests if this user can create a single ``TimePeriod`` using the desired record types.
        While ``CalendaringManager.getTimePeriodRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``TimePeriod``. Providing an empty array tests if a
        ``TimePeriod`` can be created with no records.

        :param time_period_record_types: array of time period record types
        :type time_period_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``TimePeriod`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``time_period_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_time_period_form_for_create(self, time_period_record_types):
        """Gets the time period form for creating new time periods.
        A new form should be requested for each create transaction.

        :param time_period_record_types: array of time period record types
        :type time_period_record_types: ``osid.type.Type[]``
        :return: the time period form
        :rtype: ``osid.calendaring.TimePeriodForm``
        :raise: ``NullArgument`` -- ``time_period_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_time_period(self, time_period_form):
        """Creates a new ``TimePeriod``.

        :param time_period_form: the forms for this ``TimePeriod``
        :type time_period_form: ``osid.calendaring.TimePeriodForm``
        :return: the new ``TimePeriod``
        :rtype: ``osid.calendaring.TimePeriod``
        :raise: ``IllegalState`` -- ``time_period_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``time_period_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``time_period_form`` did not originate from ``get_time_period_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_time_periods(self):
        """Tests if this user can update ``TimePeriods``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``TimePeriod`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if time period modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_time_period_form_for_update(self, time_period_id):
        """Gets the time period form for updating an existing time period.
        A new time period form should be requested for each update
        transaction.

        :param time_period_id: the ``Id`` of the ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :return: the time period form
        :rtype: ``osid.calendaring.TimePeriodForm``
        :raise: ``NotFound`` -- ``time_period_id`` is not found
        :raise: ``NullArgument`` -- ``time_periodid`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_time_period(self, time_period_form):
        """Updates an existing tiem period.

        :param time_period_form: the form containing the elements to be updated
        :type time_period_form: ``osid.calendaring.TimePeriodForm``
        :raise: ``IllegalState`` -- ``time_period_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``time_period_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``time_period_form`` did not originate from ``get_time_period_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_time_periods(self):
        """Tests if this user can delete ``TimePeriods``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``TimePeriod`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``TimePeriod`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_time_period(self, time_period_id):
        """Deletes the ``TimePeriod`` identified by the given ``Id``.

        :param time_period_id: the ``Id`` of the ``TimePeriod`` to delete
        :type time_period_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``TimePeriod`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``time_period_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_time_period_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``TimePeriods``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``TimePeriod`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_time_period(self, time_period_id, alias_id):
        """Adds an ``Id`` to a ``TimePeriod`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``TimePeriod`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another time period, it is
        reassigned to the given time period ``Id``.

        :param time_period_id: the ``Id`` of a ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``time_period_id`` not found
        :raise: ``NullArgument`` -- ``time_period_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_exception_event(self, time_period_id, event_id):
        """Adds an exception event to a time period.
        Time period exception events govern exceptions to recurring
        events mapped to a time period.

        :param time_period_id: the ``Id`` of a ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :param event_id: an exception event ``Id``
        :type event_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- event is already part of the time period
        :raise: ``NotFound`` -- ``time_period_id`` or ``event_id`` is not found
        :raise: ``NullArgument`` -- ``time_period_id`` or ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_exception_event(self, time_period_id, event_id):
        """Removes an exception event from a time period.

        :param time_period_id: the ``Id`` of a ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :param event_id: an exception event ``Id``
        :type event_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``event_id`` not an exception in ``time_period_id``
        :raise: ``NullArgument`` -- ``time_period_id`` or ``event_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.TimePeriodNotificationSession

    def can_register_for_time_period_notifications(self):
        """Tests if this user can register for ``TimePeriod`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_time_periods(self):
        """Register for notifications of new time periods.
        ``TimePeriodReceiver.newTimePeriod()`` is invoked when a new
        time period is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_time_periods(self):
        """Registers for notification of updated time periods.
        ``TimePeriodReceiver.changedTimePeriod()`` is invoked when a
        time period is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_time_period(self, time_period_id):
        """Registers for notification of an updated time period.
        ``TimePeriodReceiver.changedTimePeriod()`` is invoked when the
        specified time period is changed.

        :param time_period_id: the ``Id`` of the ``TimePeriod`` to monitor
        :type time_period_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``time_period_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_time_periods(self):
        """Registers for notification of deleted time periods.
        ``TimePeriodReceiver.deletedTimePeriod()`` is invoked when a
        time period is removed from this calendar.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_time_period(self, time_period_id):
        """Registers for notification of a deleted time period.
        ``TimePeriodReceiver.changedTimePeriod()`` is invoked when the
        specified time period is removed from this calendar.

        :param time_period_id: the ``Id`` of the ``TimePeriod`` to monitor
        :type time_period_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``time_period_id is null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.TimePeriodCalendarSession

    def can_lookup_time_period_calendar_mappings(self):
        """Tests if this user can perform lookups of time period/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_time_period_ids_by_calendar(self, calendar_id):
        """Gets the list of ``TimePeriod``  ``Ids`` associated with an ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related time period ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods_by_calendar(self, calendar_id):
        """Gets the list of ``TimePeriods`` associated with an ``Calendar``.

        :param calendar_id: ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: list of related time periods
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``NotFound`` -- ``calendar_id`` is not found
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_period_ids_by_calendars(self, calendar_ids):
        """Gets the list of ``TimePeriod Ids`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of time period ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_time_periods_by_calendars(self, calendar_ids):
        """Gets the list of ``TimePeriods`` corresponding to a list of ``Calendars``.

        :param calendar_ids: list of calendar ``Ids``
        :type calendar_ids: ``osid.id.IdList``
        :return: list of time periods
        :rtype: ``osid.calendaring.TimePeriodList``
        :raise: ``NullArgument`` -- ``calendar_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendar_ids_by_time_period(self, time_period_id):
        """Gets the list of ``Calendar Ids`` mapped to a ``TimePeriod``.

        :param time_period_id: ``Id`` of a ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``time_period_id`` is not found
        :raise: ``NullArgument`` -- ``time_period_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_calendars_by_time_period(self, time_period_id):
        """Gets the list of ``Calendars`` mapped to a ``TimePeriod``.

        :param time_period_id: ``Id`` of a ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :return: list of calendar ``Ids``
        :rtype: ``osid.calendaring.CalendarList``
        :raise: ``NotFound`` -- ``time_period_id`` is not found
        :raise: ``NullArgument`` -- ``time_period_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.TimePeriodCalendarAssignmentSession

    def can_assign_time_periods(self):
        """Tests if this user can alter time period/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_time_periods_to_calendar(self, calendar_id):
        """Tests if this user can alter time period/calendar mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_calendar_ids_for_time_period(self, calendar_id, time_period_id):
        """Gets a list of calendars including and under the given calendar node in which a specific time period can be assigned.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param time_period_id: the ``Id`` of the ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :return: list of assignable calendar ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``calendar_id`` or ``time_period_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_time_period_to_calendar(self, time_period_id, calendar_id):
        """Adds an existing ``TimePeriod`` to a ``Calendar``.

        :param time_period_id: the ``Id`` of the ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``time_period_id`` is already assigned to ``calendar_id``
        :raise: ``NotFound`` -- ``time_period_id`` or ``calendar_id`` not found
        :raise: ``NullArgument`` -- ``time_period_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_time_period_from_calendar(self, time_period_id, calendar_id):
        """Removes a ``TimePeriod`` from a ``Calendar``.

        :param time_period_id: the ``Id`` of the ``TimePeriod``
        :type time_period_id: ``osid.id.Id``
        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``time_period_id`` or ``calendar_id`` not found or ``time_period_id`` not assigned to ``calendar_id``
        :raise: ``NullArgument`` -- ``time_period_id`` or ``calendar_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.calendaring.TimePeriodSmartCalendarSession

    def apply_time_period_query(self, time_period_query):
        """Applies a time period query to this calendar.

        :param time_period_query: the time period query
        :type time_period_query: ``osid.calendaring.TimePeriodQuery``
        :raise: ``NullArgument`` -- ``time_period_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``time_period_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspect_time_period_query(self):
        """Gets a time period query inspector for this calendar.

        :return: the time period query inspector
        :rtype: ``osid.calendaring.TimePeriodQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_time_period_sequencing(self, time_period_search_order):
        """Applies a time period search order to this calendar.

        :param time_period_search_order: the time period search order
        :type time_period_search_order: ``osid.calendaring.TimePeriodSearchOrder``
        :raise: ``NullArgument`` -- ``time_period_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``time_period_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class CalendarList(osid_objects.OsidList):

    def get_next_calendar(self):
        """Gets the next ``Calendar`` in this list.

        :return: the next ``Calendar`` in this list. The ``has_next()`` method should be used to test that a next ``Calendar`` is available before calling this method.
        :rtype: ``osid.calendaring.Calendar``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_calendar = property(fget=get_next_calendar)

    def get_next_calendars(self, n):
        """Gets the next set of ``Calendar`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Calendar`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Calendar`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.Calendar``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Calendars(CalendaringManager):
    pass


