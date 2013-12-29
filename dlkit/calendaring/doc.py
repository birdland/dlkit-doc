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