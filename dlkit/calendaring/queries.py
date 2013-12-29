from ..osid import queries as osid_queries


class EventQuery(osid_queries.OsidObjectQuery, osid_queries.OsidTemporalQuery, osid_queries.OsidContainableQuery):
    """This is the query for searching events.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_implicit(self, match):
        """Matches an event that is implicitly generated.

        :param match: ``true`` to match events implicitly generated, ``false`` to match events explicitly defined
        :type match: ``boolean``

        """
        pass

    def clear_implicit_terms(self):
        """Clears the implcit terms."""
        pass

    implicit_terms = property(fdel=clear_implicit_terms)

    def match_duration(self, low, high, match):
        """Matches the event duration between the given range inclusive.

        :param low: low duration range
        :type low: ``osid.calendaring.Duration``
        :param high: high duration range
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``null``

        """
        pass

    def match_any_duration(self, match):
        """Matches an event that has any duration.

        :param match: ``true`` to match events with any duration, ``false`` to match events with no start time
        :type match: ``boolean``

        """
        pass

    def clear_duration_terms(self):
        """Clears the duration terms."""
        pass

    duration_terms = property(fdel=clear_duration_terms)

    def match_time(self, time, match):
        """Matches events that include the given time.

        :param time: date
        :type time: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``time`` is ``null``

        """
        pass

    def match_time_inclusive(self, start, end, match):
        """Matches events with start and end times between the given range inclusive.

        :param start: start date
        :type start: ``osid.calendaring.DateTime``
        :param end: end date
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``end`` or ``start`` is ``null``

        """
        pass

    def match_any_time(self, match):
        """Matches events that has any time assigned.

        :param match: ``true`` to match events with any time, ``false`` to match events with no time
        :type match: ``boolean``

        """
        pass

    def clear_time_terms(self):
        """Clears the time terms."""
        pass

    time_terms = property(fdel=clear_time_terms)

    def match_recurring_event_id(self, recurring_event_id, match):
        """Matches events that related to the recurring event.

        :param recurring_event_id: an ``Id`` for a recurring event
        :type recurring_event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``recurring_event_id`` is ``null``

        """
        pass

    def clear_recurring_event_id_terms(self):
        """Clears the recurring event terms."""
        pass

    recurring_event_id_terms = property(fdel=clear_recurring_event_id_terms)

    def supports_recurring_event_query(self):
        """Tests if a ``RecurringEventQuery`` is available for querying recurring events.

        :return: ``true`` if a recurring event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_recurring_event_query(self):
        """Gets the query for a recurring event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the recurring event query
        :rtype: ``osid.calendaring.RecurringEventQuery``
        :raise: ``Unimplemented`` -- ``supports_recurring_event_query()`` is ``false``

        """
        return # osid.calendaring.RecurringEventQuery

    recurring_event_query = property(fget=get_recurring_event_query)

    def match_any_recurring_event(self, match):
        """Matches an event that is part of any recurring event.

        :param match: ``true`` to match events part of any recurring event, ``false`` to match only standalone events
        :type match: ``boolean``

        """
        pass

    def clear_recurring_event_terms(self):
        """Clears the recurring event terms."""
        pass

    recurring_event_terms = property(fdel=clear_recurring_event_terms)

    def match_superseding_event_id(self, superseding_event_id, match):
        """Matches events that relate to the superseding event.

        :param superseding_event_id: an ``Id`` for a superseding event
        :type superseding_event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_superseding_event_id_terms(self):
        """Clears the superseding events type terms."""
        pass

    superseding_event_id_terms = property(fdel=clear_superseding_event_id_terms)

    def supports_superseding_event_query(self):
        """Tests if a ``SupersedingEventQuery`` is available for querying offset events.

        :return: ``true`` if a superseding event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_superseding_event_query(self):
        """Gets the query for a superseding event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the superseding event query
        :rtype: ``osid.calendaring.SupersedingEventQuery``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` is ``false``

        """
        return # osid.calendaring.SupersedingEventQuery

    superseding_event_query = property(fget=get_superseding_event_query)

    def match_any_superseding_event(self, match):
        """Matches any superseding event.

        :param match: ``true`` to match any superseding events, ``false`` otherwise
        :type match: ``boolean``

        """
        pass

    def clear_superseding_event_terms(self):
        """Clears the superseding event terms."""
        pass

    superseding_event_terms = property(fdel=clear_superseding_event_terms)

    def match_offset_event_id(self, offset_event_id, match):
        """Matches events that relates to the offset event.

        :param offset_event_id: an ``Id`` for an offset event
        :type offset_event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_offset_event_id_terms(self):
        """Clears the recurring events type terms."""
        pass

    offset_event_id_terms = property(fdel=clear_offset_event_id_terms)

    def supports_offset_event_query(self):
        """Tests if an ``OffsetEventQuery`` is available for querying offset events.

        :return: ``true`` if an offset event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_offset_event_query(self):
        """Gets the query for an offset event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the offset event query
        :rtype: ``osid.calendaring.OffsetEventQuery``
        :raise: ``Unimplemented`` -- ``supports_offset_event_query()`` is ``false``

        """
        return # osid.calendaring.OffsetEventQuery

    offset_event_query = property(fget=get_offset_event_query)

    def match_any_offset_event(self, match):
        """Matches any offset event.

        :param match: ``true`` to match any offset events, ``false`` otherwise
        :type match: ``boolean``

        """
        pass

    def clear_offset_event_terms(self):
        """Clears the offset event terms."""
        pass

    offset_event_terms = property(fdel=clear_offset_event_terms)

    def match_location_description(self, location, string_match_type, match):
        """Matches the location description string.

        :param location: location string
        :type location: ``string``
        :param string_match_type: string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``location`` is not of ``string_match_type``
        :raise: ``NullArgument`` -- ``location`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def match_any_location_description(self, match):
        """Matches an event that has any location description assigned.

        :param match: ``true`` to match events with any location description, ``false`` to match events with no location description
        :type match: ``boolean``

        """
        pass

    def clear_location_description_terms(self):
        """Clears the location description terms."""
        pass

    location_description_terms = property(fdel=clear_location_description_terms)

    def match_location_id(self, location_id, match):
        """Sets the location ``Id`` for this query.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        """
        pass

    def clear_location_id_terms(self):
        """Clears the location ``Id`` terms."""
        pass

    location_id_terms = property(fdel=clear_location_id_terms)

    def supports_location_query(self):
        """Tests if a ``LocationQuery`` is available for querying locations.

        :return: ``true`` if a location query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_location_query(self):
        """Gets the query for a location.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``Unimplemented`` -- ``supports_location_query()`` is ``false``

        """
        return # osid.mapping.LocationQuery

    location_query = property(fget=get_location_query)

    def match_any_location(self, match):
        """Matches an event that has any location assigned.

        :param match: ``true`` to match events with any location, ``false`` to match events with no location
        :type match: ``boolean``

        """
        pass

    def clear_location_terms(self):
        """Clears the location terms."""
        pass

    location_terms = property(fdel=clear_location_terms)

    def match_sponsor_id(self, sponsor_id, match):
        """Sets the sponsor ``Id`` for this query.

        :param sponsor_id: a sponsor ``Id``
        :type sponsor_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``sponsor_id`` is ``null``

        """
        pass

    def clear_sponsor_id_terms(self):
        """Clears the sponsor ``Id`` terms."""
        pass

    sponsor_id_terms = property(fdel=clear_sponsor_id_terms)

    def supports_sponsor_query(self):
        """Tests if a ``LocationQuery`` is available for querying sponsors.

        :return: ``true`` if a sponsor query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_sponsor_query(self):
        """Gets the query for a sponsor.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the sponsor query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_sponsor_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    sponsor_query = property(fget=get_sponsor_query)

    def clear_sponsor_terms(self):
        """Clears the sponsor terms."""
        pass

    sponsor_terms = property(fdel=clear_sponsor_terms)

    def match_coordinate(self, coordinate, match):
        """Matches events whose locations contain the given coordinate.

        :param coordinate: a coordinate
        :type coordinate: ``osid.mapping.Coordinate``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``coordinate`` is ``null``

        """
        pass

    def clear_coordinate_terms(self):
        """Clears the cooordinate terms."""
        pass

    coordinate_terms = property(fdel=clear_coordinate_terms)

    def match_spatial_unit(self, spatial_unit, match):
        """Matches events whose locations fall within the given spatial unit.

        :param spatial_unit: a spatial unit
        :type spatial_unit: ``osid.mapping.SpatialUnit``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``spatial_unit`` is ``null``

        """
        pass

    def clear_spatial_unit_terms(self):
        """Clears the spatial unit terms."""
        pass

    spatial_unit_terms = property(fdel=clear_spatial_unit_terms)

    def match_commitment_id(self, commitment_id, match):
        """Sets the commitment ``Id`` for this query.

        :param commitment_id: a commitment ``Id``
        :type commitment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``commitment_id`` is ``null``

        """
        pass

    def clear_commitment_id_terms(self):
        """Clears the commitment ``Id`` terms."""
        pass

    commitment_id_terms = property(fdel=clear_commitment_id_terms)

    def supports_commitment_query(self):
        """Tests if a ``CommitmentQuery`` is available for querying recurring event terms.

        :return: ``true`` if a commitment query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_commitment_query(self):
        """Gets the query for a commitment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the commitment query
        :rtype: ``osid.calendaring.CommitmentQuery``
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` is ``false``

        """
        return # osid.calendaring.CommitmentQuery

    commitment_query = property(fget=get_commitment_query)

    def match_any_commitment(self, match):
        """Matches an event that has any commitment.

        :param match: ``true`` to match events with any commitment, ``false`` to match events with no commitments
        :type match: ``boolean``

        """
        pass

    def clear_commitment_terms(self):
        """Clears the commitment terms."""
        pass

    commitment_terms = property(fdel=clear_commitment_terms)

    def match_containing_event_id(self, event_id, match):
        """Sets the event ``Id`` for this query to match events that have the specified event as an ancestor.

        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_containing_event_id_terms(self):
        """Clears the containing event ``Id`` terms."""
        pass

    containing_event_id_terms = property(fdel=clear_containing_event_id_terms)

    def supports_containing_event_query(self):
        """Tests if a containing event query is available.

        :return: ``true`` if a containing event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_containing_event_query(self):
        """Gets the query for a containing event.

        :return: the containing event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_containing_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    containing_event_query = property(fget=get_containing_event_query)

    def match_containing_any_event(self, match):
        """Matches events with any ancestor event.

        :param match: ``true`` to match events with any ancestor event, ``false`` to match events with no ancestor events
        :type match: ``boolean``

        """
        pass

    def clear_containing_event_terms(self):
        """Clears the containing event terms."""
        pass

    containing_event_terms = property(fdel=clear_containing_event_terms)

    def match_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_calendar_id_terms(self):
        """Clears the calendar ``Id`` terms."""
        pass

    calendar_id_terms = property(fdel=clear_calendar_id_terms)

    def supports_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available for querying calendars.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    calendar_query = property(fget=get_calendar_query)

    def clear_calendar_terms(self):
        """Clears the calendar terms."""
        pass

    calendar_terms = property(fdel=clear_calendar_terms)

    def get_event_query_record(self, event_record_type):
        """Gets the event query record corresponding to the given ``Event`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param event_record_type: an event query record type
        :type event_record_type: ``osid.type.Type``
        :return: the event query record
        :rtype: ``osid.calendaring.records.EventQueryRecord``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.EventQueryRecord


class RecurringEventQuery(osid_queries.OsidObjectQuery, osid_queries.OsidContainableQuery):
    """This is the query for searching recurring events.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_schedule_id(self, schedule_id, match):
        """Sets the schedule ``Id`` for this query for matching schedules.

        :param schedule_id: a schedule ``Id``
        :type schedule_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_id`` is ``null``

        """
        pass

    def clear_schedule_id_terms(self):
        """Clears the schedule ``Id`` terms."""
        pass

    schedule_id_terms = property(fdel=clear_schedule_id_terms)

    def supports_schedule_query(self):
        """Tests if a ``ScheduleQuery`` is available for querying schedules.

        :return: ``true`` if a schedule query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_schedule_query(self):
        """Gets the query for a schedule.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the schedule query
        :rtype: ``osid.calendaring.ScheduleQuery``
        :raise: ``Unimplemented`` -- ``supports_schedule_query()`` is ``false``

        """
        return # osid.calendaring.ScheduleQuery

    schedule_query = property(fget=get_schedule_query)

    def match_any_schedule(self, match):
        """Matches a recurring event that has any schedule assigned.

        :param match: ``true`` to match recurring events with any schedules, ``false`` to match recurring events with no schedules
        :type match: ``boolean``

        """
        pass

    def clear_schedule_terms(self):
        """Clears the schedule terms."""
        pass

    schedule_terms = property(fdel=clear_schedule_terms)

    def match_superseding_event_id(self, superseding_event_id, match):
        """Sets the superseding event ``Id`` for this query.

        :param superseding_event_id: a superseding event ``Id``
        :type superseding_event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``superseding_event_id`` is ``null``

        """
        pass

    def clear_superseding_event_id_terms(self):
        """Clears the superseding event ``Id`` terms."""
        pass

    superseding_event_id_terms = property(fdel=clear_superseding_event_id_terms)

    def supports_superseding_event_query(self):
        """Tests if a ``SupersedingEventQuery`` is available for querying superseding events.

        :return: ``true`` if a superseding event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_superseding_event_query(self):
        """Gets the query for a superseding event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the superseding event query
        :rtype: ``osid.calendaring.SupersedingEventQuery``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` is ``false``

        """
        return # osid.calendaring.SupersedingEventQuery

    superseding_event_query = property(fget=get_superseding_event_query)

    def match_any_superseding_event(self, match):
        """Matches a recurring event that has any superseding event assigned.

        :param match: ``true`` to match recurring events with any superseding events, ``false`` to match events with no superseding events
        :type match: ``boolean``

        """
        pass

    def clear_superseding_event_terms(self):
        """Clears the superseding event terms."""
        pass

    superseding_event_terms = property(fdel=clear_superseding_event_terms)

    def match_specific_meeting_time(self, start, end, match):
        """Matches recurring events with specific dates between the given range inclusive.

        :param start: start date
        :type start: ``osid.calendaring.DateTime``
        :param end: end date
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``zero``

        """
        pass

    def match_any_specific_meeting_time(self, match):
        """Matches a recurring event that has any specific date assigned.

        :param match: ``true`` to match recurring events with any specific date, ``false`` to match recurring events with no specific date
        :type match: ``boolean``

        """
        pass

    def clear_specific_meeting_time_terms(self):
        """Clears the blackout terms."""
        pass

    specific_meeting_time_terms = property(fdel=clear_specific_meeting_time_terms)

    def match_event_id(self, event_id, match):
        """Sets the composed event ``Id`` for this query.

        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_event_id_terms(self):
        """Clears the event ``Id`` terms."""
        pass

    event_id_terms = property(fdel=clear_event_id_terms)

    def supports_event_query(self):
        """Tests if an ``EventQuery`` is available for querying composed events.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_event_query(self):
        """Gets the query for an event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    event_query = property(fget=get_event_query)

    def match_any_event(self, match):
        """Matches a recurring event that has any composed event assigned.

        :param match: ``true`` to match recurring events with any composed events, ``false`` to match events with no composed events
        :type match: ``boolean``

        """
        pass

    def clear_event_terms(self):
        """Clears the event terms."""
        pass

    event_terms = property(fdel=clear_event_terms)

    def match_blackout(self, datetime, match):
        """Matches a blackout that contains the given date time.

        :param datetime: a datetime
        :type datetime: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``datetime`` is ``null``

        """
        pass

    def match_blackout_inclusive(self, start, end, match):
        """Matches recurring events with blackouts between the given range inclusive.

        :param start: start date
        :type start: ``osid.calendaring.DateTime``
        :param end: end date
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``zero``

        """
        pass

    def match_any_blackout(self, match):
        """Matches a recurring event that has any blackout assigned.

        :param match: ``true`` to match recurring events with any blackout, ``false`` to match recurring events with no blackout
        :type match: ``boolean``

        """
        pass

    def clear_blackout_terms(self):
        """Clears the blackout terms."""
        pass

    blackout_terms = property(fdel=clear_blackout_terms)

    def match_sponsor_id(self, sponsor_id, match):
        """Sets the sponsor ``Id`` for this query.

        :param sponsor_id: a sponsor ``Id``
        :type sponsor_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``sponsor_id`` is ``null``

        """
        pass

    def clear_sponsor_id_terms(self):
        """Clears the sponsor ``Id`` terms."""
        pass

    sponsor_id_terms = property(fdel=clear_sponsor_id_terms)

    def supports_sponsor_query(self):
        """Tests if a ``LocationQuery`` is available for querying sponsors.

        :return: ``true`` if a sponsor query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_sponsor_query(self):
        """Gets the query for a sponsor.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the sponsor query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_sponsor_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    sponsor_query = property(fget=get_sponsor_query)

    def clear_sponsor_terms(self):
        """Clears the sponsor terms."""
        pass

    sponsor_terms = property(fdel=clear_sponsor_terms)

    def match_date(self, datetime, match):
        """Matches a recurring events where any event overlaps with the given date.

        :param datetime: a datetime
        :type datetime: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``null``

        """
        pass

    def match_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_calendar_id_terms(self):
        """Clears the calendar ``Id`` terms."""
        pass

    calendar_id_terms = property(fdel=clear_calendar_id_terms)

    def supports_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available for querying calendars.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    calendar_query = property(fget=get_calendar_query)

    def clear_calendar_terms(self):
        """Clears the calendar terms."""
        pass

    calendar_terms = property(fdel=clear_calendar_terms)

    def get_recurring_event_query_record(self, recurring_event_record_type):
        """Gets the recurring event query recod corresponding to the given ``RecurringEvent`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param recurring_event_record_type: a recurring event query record type
        :type recurring_event_record_type: ``osid.type.Type``
        :return: the recurring event query record
        :rtype: ``osid.calendaring.records.RecurringEventQueryRecord``
        :raise: ``NullArgument`` -- ``recurring_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(recurring_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.RecurringEventQueryRecord


class SupersedingEventQuery(osid_queries.OsidRuleQuery):
    """This is the query for searching superseding events.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_superseded_event_id(self, event_id, match):
        """Sets the event ``Id`` for this query for matching attached events.

        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_superseded_event_id_terms(self):
        """Clears the event ``Id`` terms."""
        pass

    superseded_event_id_terms = property(fdel=clear_superseded_event_id_terms)

    def supports_superseded_event_query(self):
        """Tests if an ``EventQuery`` is available for querying attached events.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_superseded_event_query(self):
        """Gets the query for an attached event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_superseded_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    superseded_event_query = property(fget=get_superseded_event_query)

    def clear_superseded_event_terms(self):
        """Clears the event terms."""
        pass

    superseded_event_terms = property(fdel=clear_superseded_event_terms)

    def match_superseding_event_id(self, superseding_event_id, match):
        """Sets the superseding event ``Id`` for this query.

        :param superseding_event_id: a superseding event ``Id``
        :type superseding_event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``superseding_event_id`` is ``null``

        """
        pass

    def clear_superseding_event_id_terms(self):
        """Clears the superseding event ``Id`` terms."""
        pass

    superseding_event_id_terms = property(fdel=clear_superseding_event_id_terms)

    def supports_superseding_event_query(self):
        """Tests if a ``SupersedingEventQuery`` is available.

        :return: ``true`` if a superseding event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_superseding_event_query(self):
        """Gets the query for a superseding event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the superseding event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_superseding_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    superseding_event_query = property(fget=get_superseding_event_query)

    def clear_superseding_event_terms(self):
        """Clears the superseding event terms."""
        pass

    superseding_event_terms = property(fdel=clear_superseding_event_terms)

    def match_superseded_date(self, from_, to, match):
        """Matches superseding events that supersede within the given dates inclusive.

        :param from: start date
        :type from: ``osid.calendaring.DateTime``
        :param to: end date
        :type to: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``from`` is greater than ``to``
        :raise: ``NullArgument`` -- ``from`` or ``to`` is ``null``

        """
        pass

    def match_any_superseded_date(self, match):
        """Matches a superseding event that has any superseded date.

        :param match: ``true`` to match superseding events with any superseded date, false to match superseding events with no superseded date
        :type match: ``boolean``

        """
        pass

    def clear_superseded_date_terms(self):
        """Clears the superseded date terms."""
        pass

    superseded_date_terms = property(fdel=clear_superseded_date_terms)

    def match_superseded_event_position(self, from_, to, match):
        """Matches superseding events that supersede within the denormalized event positions inclusive.

        :param from: start position
        :type from: ``integer``
        :param to: end position
        :type to: ``integer``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- the absolute value of ``from`` is greater than ``to``

        """
        pass

    def match_any_superseded_event_position(self, match):
        """Matches a superseding event that has any superseded position.

        :param match: ``true`` to match superseding events with any superseded event position, false to match superseding events with no superseded event position
        :type match: ``boolean``

        """
        pass

    def clear_superseded_position_terms(self):
        """Clears the superseded position terms."""
        pass

    superseded_position_terms = property(fdel=clear_superseded_position_terms)

    def match_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_calendar_id_terms(self):
        """Clears the calendar ``Id`` terms."""
        pass

    calendar_id_terms = property(fdel=clear_calendar_id_terms)

    def supports_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available for querying calendars.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    calendar_query = property(fget=get_calendar_query)

    def clear_calendar_terms(self):
        """Clears the calendar terms."""
        pass

    calendar_terms = property(fdel=clear_calendar_terms)

    def get_superseding_event_query_record(self, superseding_event_record_type):
        """Gets the superseding event query record corresponding to the given ``SupersedingEvent`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param superseding_event_record_type: a superseding event query record type
        :type superseding_event_record_type: ``osid.type.Type``
        :return: the superseding event query record
        :rtype: ``osid.calendaring.records.SupersedingEventQueryRecord``
        :raise: ``NullArgument`` -- ``superseding_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(superseding_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.SupersedingEventQueryRecord


class OffsetEventQuery(osid_queries.OsidRuleQuery):
    """This is the query for searching events.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_fixed_start_time(self, from_, to, match):
        """Matches a fixed start time between the given range inclusive.

        :param from: the start of the range
        :type from: ``osid.calendaring.DateTime``
        :param to: the end of the range
        :type to: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to``  ``null``

        """
        pass

    def match_any_fixed_start_time(self, match):
        """Matches events with fixed start times.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_fixed_start_time_terms(self):
        """Clears the fixed start time terms."""
        pass

    fixed_start_time_terms = property(fdel=clear_fixed_start_time_terms)

    def match_start_reference_event_id(self, event_id, match):
        """Sets the start reference event ``Id`` for this query.

        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_start_reference_event_id_terms(self):
        """Clears the start reference event ``Id`` terms."""
        pass

    start_reference_event_id_terms = property(fdel=clear_start_reference_event_id_terms)

    def supports_start_reference_event_query(self):
        """Tests if an ``EventQuery`` is available for querying start reference event terms.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_start_reference_event_query(self):
        """Gets the query for the start reference event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_start_reference_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    start_reference_event_query = property(fget=get_start_reference_event_query)

    def match_any_start_reference_event(self, match):
        """Matches offset events with any starting reference event.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_start_reference_event_terms(self):
        """Clears the start reference event terms."""
        pass

    start_reference_event_terms = property(fdel=clear_start_reference_event_terms)

    def match_fixed_start_offset(self, from_, to, match):
        """Matches a fixed offset amount between the given range inclusive.

        :param from: the start of the range
        :type from: ``osid.calendaring.Duration``
        :param to: the end of the range
        :type to: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to``  ``null``

        """
        pass

    def match_any_fixed_start_offset(self, match):
        """Matches fixed offset events.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_fixed_start_offset_terms(self):
        """Clears the fixed offset terms."""
        pass

    fixed_start_offset_terms = property(fdel=clear_fixed_start_offset_terms)

    def match_relative_weekday_start_offset(self, low, high, match):
        """Matches a relative weekday offset amount between the given range inclusive.

        :param low: the start of the range
        :type low: ``integer``
        :param high: the end of the range
        :type high: ``integer``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_relative_weekday_start_offset_terms(self):
        """Clears the relative weekday offset terms."""
        pass

    relative_weekday_start_offset_terms = property(fdel=clear_relative_weekday_start_offset_terms)

    def match_relative_start_weekday(self, weekday, match):
        """Matches a relative weekday.

        :param weekday: the weekday
        :type weekday: ``cardinal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def match_any_relative_start_weekdays(self, match):
        """Matches relative weekday offset events.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_relative_start_weekday_terms(self):
        """Clears the relative weekday terms."""
        pass

    relative_start_weekday_terms = property(fdel=clear_relative_start_weekday_terms)

    def match_fixed_duration_offset(self, low, high, match):
        """Matches a fixed duration between the given range inclusive.

        :param low: the start of the range
        :type low: ``osid.calendaring.Duration``
        :param high: the end of the range
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_fixed_duration_terms(self):
        """Clears the fixed duration terms."""
        pass

    fixed_duration_terms = property(fdel=clear_fixed_duration_terms)

    def match_end_reference_event_id(self, event_id, match):
        """Sets the end reference event ``Id`` for this query.

        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_end_reference_event_id_terms(self):
        """Clears the end reference event ``Id`` terms."""
        pass

    end_reference_event_id_terms = property(fdel=clear_end_reference_event_id_terms)

    def supports_end_reference_event_query(self):
        """Tests if an ``EventQuery`` is available for querying end reference event terms.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_end_reference_event_query(self):
        """Gets the query for the end reference event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_event_reference_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    end_reference_event_query = property(fget=get_end_reference_event_query)

    def match_any_end_reference_event(self, match):
        """Matches any end reference event events.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_end_reference_event_terms(self):
        """Clears the end reference event terms."""
        pass

    end_reference_event_terms = property(fdel=clear_end_reference_event_terms)

    def match_fixed_end_offset(self, from_, to, match):
        """Matches a fixed offset amount between the given range inclusive.

        :param from: the start of the range
        :type from: ``osid.calendaring.Duration``
        :param to: the end of the range
        :type to: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to``  ``null``

        """
        pass

    def match_any_fixed_end_offset(self, match):
        """Matches fixed offset events.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_fixed_end_offset_terms(self):
        """Clears the fixed offset terms."""
        pass

    fixed_end_offset_terms = property(fdel=clear_fixed_end_offset_terms)

    def match_relative_weekday_end_offset(self, low, high, match):
        """Matches a relative weekday offset amount between the given range inclusive.

        :param low: the start of the range
        :type low: ``integer``
        :param high: the end of the range
        :type high: ``integer``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_relative_weekday_end_offset_terms(self):
        """Clears the relative weekday offset terms."""
        pass

    relative_weekday_end_offset_terms = property(fdel=clear_relative_weekday_end_offset_terms)

    def match_relative_end_weekday(self, weekday, match):
        """Matches a relative weekday.

        :param weekday: the weekday
        :type weekday: ``cardinal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def match_any_relative_end_weekdays(self, match):
        """Matches relative weekday offset events.

        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def clear_relative_end_weekday_terms(self):
        """Clears the relative weekday terms."""
        pass

    relative_end_weekday_terms = property(fdel=clear_relative_end_weekday_terms)

    def supports_event_query(self):
        """Tests if an ``EventQuery`` is available for querying the resulting event.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_event_query(self):
        """Gets the query for the resulting event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    event_query = property(fget=get_event_query)

    def match_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_calendar_id_terms(self):
        """Clears the calendar ``Id`` terms."""
        pass

    calendar_id_terms = property(fdel=clear_calendar_id_terms)

    def supports_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available for querying calendars.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    calendar_query = property(fget=get_calendar_query)

    def clear_calendar_terms(self):
        """Clears the calendar terms."""
        pass

    calendar_terms = property(fdel=clear_calendar_terms)

    def get_offset_event_query_record(self, offset_event_record_type):
        """Gets the offset event query record corresponding to the given ``OffsetEvent`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param offset_event_record_type: an offset event query record type
        :type offset_event_record_type: ``osid.type.Type``
        :return: the offset event query record
        :rtype: ``osid.calendaring.records.OffsetEventQueryRecord``
        :raise: ``NullArgument`` -- ``offset_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(offset_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.OffsetEventQueryRecord


class ScheduleQuery(osid_queries.OsidObjectQuery):
    """This is the query for searching schedules.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_schedule_slot_id(self, schedule_slot_id, match):
        """Sets the schedule ``Id`` for this query for matching nested schedule slots.

        :param schedule_slot_id: a schedule slot ``Id``
        :type schedule_slot_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``

        """
        pass

    def clear_schedule_slot_id_terms(self):
        """Clears the schedule slot ``Id`` terms."""
        pass

    schedule_slot_id_terms = property(fdel=clear_schedule_slot_id_terms)

    def supports_schedule_slot_query(self):
        """Tests if a ``ScheduleSlotQuery`` is available for querying sechedule slots.

        :return: ``true`` if a schedule slot query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_schedule_slot_query(self):
        """Gets the query for a schedul slot.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the schedule slot query
        :rtype: ``osid.calendaring.ScheduleSlotQuery``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` is ``false``

        """
        return # osid.calendaring.ScheduleSlotQuery

    schedule_slot_query = property(fget=get_schedule_slot_query)

    def match_any_schedule_slot(self, match):
        """Matches a schedule that has any schedule slot assigned.

        :param match: ``true`` to match schedule with any schedule slots, ``false`` to match schedules with no schedule slots
        :type match: ``boolean``

        """
        pass

    def clear_schedule_slot_terms(self):
        """Clears the schedule slot terms."""
        pass

    schedule_slot_terms = property(fdel=clear_schedule_slot_terms)

    def match_time_period_id(self, time_period_id, match):
        """Sets the time period ``Id`` for this query.

        :param time_period_id: a time period ``Id``
        :type time_period_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``time_period_id`` is ``null``

        """
        pass

    def clear_time_period_id_terms(self):
        """Clears the time period ``Id`` terms."""
        pass

    time_period_id_terms = property(fdel=clear_time_period_id_terms)

    def supports_time_period_query(self):
        """Tests if a ``TimePeriodQuery`` is available.

        :return: ``true`` if a time period query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_time_period_query(self):
        """Gets the query for a time period.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the time period query
        :rtype: ``osid.calendaring.TimePeriodQuery``
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` is ``false``

        """
        return # osid.calendaring.TimePeriodQuery

    time_period_query = property(fget=get_time_period_query)

    def match_any_time_period(self, match):
        """Matches a schedule that has any time period assigned.

        :param match: ``true`` to match schedules with any time periods, ``false`` to match schedules with no time periods
        :type match: ``boolean``

        """
        pass

    def clear_time_period_terms(self):
        """Clears the time period terms."""
        pass

    time_period_terms = property(fdel=clear_time_period_terms)

    def match_schedule_start(self, low, high, match):
        """Matches the schedule start time between the given range inclusive.

        :param low: low time range
        :type low: ``osid.calendaring.DateTime``
        :param high: high time range
        :type high: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``null``

        """
        pass

    def match_any_schedule_start(self, match):
        """Matches a schedule that has any start time assigned.

        :param match: ``true`` to match schedules with any start time, ``false`` to match schedules with no start time
        :type match: ``boolean``

        """
        pass

    def clear_schedule_start_terms(self):
        """Clears the schedule start terms."""
        pass

    schedule_start_terms = property(fdel=clear_schedule_start_terms)

    def match_schedule_end(self, low, high, match):
        """Matches the schedule end time between the given range inclusive.

        :param low: low time range
        :type low: ``osid.calendaring.DateTime``
        :param high: high time range
        :type high: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``null``

        """
        pass

    def match_any_schedule_end(self, match):
        """Matches a schedule that has any end time assigned.

        :param match: ``true`` to match schedules with any end time, ``false`` to match schedules with no start time
        :type match: ``boolean``

        """
        pass

    def clear_schedule_end_terms(self):
        """Clears the schedule end terms."""
        pass

    schedule_end_terms = property(fdel=clear_schedule_end_terms)

    def match_schedule_time_inclusive(self, start, end, match):
        """Matches schedules with start and end times between the given range inclusive.

        :param start: start date
        :type start: ``osid.calendaring.DateTime``
        :param end: end date
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``end`` or ``start`` is ``null``

        """
        pass

    def match_any_schedule_time(self, match):
        """Matches schedules that has any time assigned.

        :param match: ``true`` to match schedules with any time, ``false`` to match schedules with no time
        :type match: ``boolean``

        """
        pass

    def clear_schedule_time_terms(self):
        """Clears the schedule time terms."""
        pass

    schedule_time_terms = property(fdel=clear_schedule_time_terms)

    def match_limit(self, from_, to, match):
        """Matches schedules that have the given limit in the given range inclusive.

        :param from: start range
        :type from: ``integer``
        :param to: end range
        :type to: ``integer``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``

        """
        pass

    def match_any_limit(self, match):
        """Matches schedules with any occurrence limit.

        :param match: ``true`` to match schedules with any limit, to match schedules with no limit
        :type match: ``boolean``

        """
        pass

    def clear_limit_terms(self):
        """Clears the limit terms."""
        pass

    limit_terms = property(fdel=clear_limit_terms)

    def match_location_description(self, location, string_match_type, match):
        """Matches the location description string.

        :param location: location string
        :type location: ``string``
        :param string_match_type: string match type
        :type string_match_type: ``osid.type.Type``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``location`` is not of ``string_match_type``
        :raise: ``NullArgument`` -- ``location`` or ``string_match_type`` is ``null``
        :raise: ``Unsupported`` -- ``supports_string_match_type(string_match_type)`` is ``false``

        """
        pass

    def match_any_location_description(self, match):
        """Matches a schedule that has any location description assigned.

        :param match: ``true`` to match schedules with any location description, ``false`` to match schedules with no location description
        :type match: ``boolean``

        """
        pass

    def clear_location_description_terms(self):
        """Clears the location description terms."""
        pass

    location_description_terms = property(fdel=clear_location_description_terms)

    def match_location_id(self, location_id, match):
        """Sets the location ``Id`` for this query.

        :param location_id: a location ``Id``
        :type location_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        """
        pass

    def clear_location_id_terms(self):
        """Clears the location ``Id`` terms."""
        pass

    location_id_terms = property(fdel=clear_location_id_terms)

    def supports_location_query(self):
        """Tests if a ``LocationQuery`` is available for querying locations.

        :return: ``true`` if a location query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_location_query(self):
        """Gets the query for a location.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the location query
        :rtype: ``osid.mapping.LocationQuery``
        :raise: ``Unimplemented`` -- ``supports_location_query()`` is ``false``

        """
        return # osid.mapping.LocationQuery

    location_query = property(fget=get_location_query)

    def match_any_location(self, match):
        """Matches a schedule that has any location assigned.

        :param match: ``true`` to match schedules with any location, ``false`` to match schedules with no location
        :type match: ``boolean``

        """
        pass

    def clear_location_terms(self):
        """Clears the location terms."""
        pass

    location_terms = property(fdel=clear_location_terms)

    def match_total_duration(self, low, high, match):
        """Matches the total duration between the given range inclusive.

        :param low: low duration range
        :type low: ``osid.calendaring.Duration``
        :param high: high duration range
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``null``

        """
        pass

    def clear_total_duration_terms(self):
        """Clears the total duration terms."""
        pass

    total_duration_terms = property(fdel=clear_total_duration_terms)

    def match_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_calendar_id_terms(self):
        """Clears the calendar ``Id`` terms."""
        pass

    calendar_id_terms = property(fdel=clear_calendar_id_terms)

    def supports_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available for querying calendars.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    calendar_query = property(fget=get_calendar_query)

    def clear_calendar_terms(self):
        """Clears the calendar terms."""
        pass

    calendar_terms = property(fdel=clear_calendar_terms)

    def get_schedule_query_record(self, schedule_record_type):
        """Gets the schedule query record corresponding to the given ``Schedule`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param schedule_record_type: a schedule query record type
        :type schedule_record_type: ``osid.type.Type``
        :return: the schedule query record
        :rtype: ``osid.calendaring.records.ScheduleQueryRecord``
        :raise: ``NullArgument`` -- ``schedule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_record_type)`` is ``false``

        """
        return # osid.calendaring.records.ScheduleQueryRecord


class ScheduleSlotQuery(osid_queries.OsidObjectQuery, osid_queries.OsidContainableQuery):
    """This is the query for searching schedule slots.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_schedule_slot_id(self, schedule_slot_id, match):
        """Sets the schedule ``Id`` for this query for matching nested schedule slots.

        :param schedule_slot_id: a schedule slot ``Id``
        :type schedule_slot_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``schedule_slot_id`` is ``null``

        """
        pass

    def clear_schedule_slot_id_terms(self):
        """Clears the schedule slot ``Id`` terms."""
        pass

    schedule_slot_id_terms = property(fdel=clear_schedule_slot_id_terms)

    def supports_schedule_slot_query(self):
        """Tests if a ``ScheduleSlotQuery`` is available for querying sechedule slots.

        :return: ``true`` if a schedule slot query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_schedule_slot_query(self):
        """Gets the query for a schedul slot.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the schedule slot query
        :rtype: ``osid.calendaring.ScheduleSlotQuery``
        :raise: ``Unimplemented`` -- ``supports_schedule_slot_query()`` is ``false``

        """
        return # osid.calendaring.ScheduleSlotQuery

    schedule_slot_query = property(fget=get_schedule_slot_query)

    def match_any_schedule_slot(self, match):
        """Matches a schedule that has any schedule slot assigned.

        :param match: ``true`` to match schedule with any schedule slots, ``false`` to match schedules with no schedule slots
        :type match: ``boolean``

        """
        pass

    def clear_schedule_slot_terms(self):
        """Clears the schedule slot terms."""
        pass

    schedule_slot_terms = property(fdel=clear_schedule_slot_terms)

    def match_weekday(self, weekday, match):
        """Matches schedules that have the given weekday.

        :param weekday: a weekday
        :type weekday: ``cardinal``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def match_any_weekday(self, match):
        """Matches schedules with any weekday set.

        :param match: ``true`` to match schedules with any weekday, ``false`` to match schedules with no weekday
        :type match: ``boolean``

        """
        pass

    def clear_weekday_terms(self):
        """Clears the weekday terms."""
        pass

    weekday_terms = property(fdel=clear_weekday_terms)

    def match_weekly_interval(self, from_, to, match):
        """Matches schedules that have the given weekly interval in the given range inclusive.

        :param from: start range
        :type from: ``integer``
        :param to: end range
        :type to: ``integer``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``

        """
        pass

    def match_any_weekly_interval(self, match):
        """Matches schedules with any weekly interval set.

        :param match: ``true`` to match schedules with any weekly interval, ``false`` to match schedules with no weekly interval
        :type match: ``boolean``

        """
        pass

    def clear_weekly_interval_terms(self):
        """Clears the weekly interval terms."""
        pass

    weekly_interval_terms = property(fdel=clear_weekly_interval_terms)

    def match_week_of_month(self, from_, to, match):
        """Matches schedules that have a week of month in the given range inclusive.

        :param from: start range
        :type from: ``integer``
        :param to: end range
        :type to: ``integer``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``

        """
        pass

    def match_any_week_of_month(self, match):
        """Matches schedules with any month week set.

        :param match: ``true`` to match schedules with any week of month, ``false`` to match schedules with no month week
        :type match: ``boolean``

        """
        pass

    def clear_week_of_month_terms(self):
        """Clears the week of month terms."""
        pass

    week_of_month_terms = property(fdel=clear_week_of_month_terms)

    def match_weekday_time(self, from_, to, match):
        """Matches schedules that have a weekday time in the given range inclusive.

        :param from: start range
        :type from: ``osid.calendaring.Time``
        :param to: end range
        :type to: ``osid.calendaring.Time``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to``  ``null``

        """
        pass

    def match_any_weekday_time(self, match):
        """Matches schedules with any weekday time.

        :param match: ``true`` to match schedules with any weekday time, ``false`` to match schedules with no weekday time
        :type match: ``boolean``

        """
        pass

    def clear_weekday_time_terms(self):
        """Clears the weekday time terms."""
        pass

    weekday_time_terms = property(fdel=clear_weekday_time_terms)

    def match_fixed_interval(self, from_, to, match):
        """Matches schedules that have the given fixed interval in the given range inclusive.

        :param from: start range
        :type from: ``osid.calendaring.Duration``
        :param to: end range
        :type to: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``to`` is less than ``from``
        :raise: ``NullArgument`` -- ``from`` or ``to``  ``null``

        """
        pass

    def match_any_fixed_interval(self, match):
        """Matches schedules with any fixed interval.

        :param match: ``true`` to match schedules with any fixed interval, ``false`` to match schedules with no fixed interval
        :type match: ``boolean``

        """
        pass

    def clear_fixed_interval_terms(self):
        """Clears the fixed interval terms."""
        pass

    fixed_interval_terms = property(fdel=clear_fixed_interval_terms)

    def match_duration(self, low, high, match):
        """Matches the duration between the given range inclusive.

        :param low: low duration range
        :type low: ``osid.calendaring.Duration``
        :param high: high duration range
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``null``

        """
        pass

    def match_any_duration(self, match):
        """Matches a schedule slot that has any duration.

        :param match: ``true`` to match schedules with any duration, ``false`` to match schedules with no start time
        :type match: ``boolean``

        """
        pass

    def clear_duration_terms(self):
        """Clears the duration terms."""
        pass

    duration_terms = property(fdel=clear_duration_terms)

    def match_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_calendar_id_terms(self):
        """Clears the calendar ``Id`` terms."""
        pass

    calendar_id_terms = property(fdel=clear_calendar_id_terms)

    def supports_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available for querying calendars.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    calendar_query = property(fget=get_calendar_query)

    def clear_calendar_terms(self):
        """Clears the calendar terms."""
        pass

    calendar_terms = property(fdel=clear_calendar_terms)

    def get_schedule_slot_query_record(self, schedule_slot_record_type):
        """Gets the schedule slot query record corresponding to the given ``ScheduleSlot`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param schedule_slot_record_type: a schedule slot query record type
        :type schedule_slot_record_type: ``osid.type.Type``
        :return: the schedule slot query record
        :rtype: ``osid.calendaring.records.ScheduleSlotQueryRecord``
        :raise: ``NullArgument`` -- ``schedule_slot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_slot_record_type)`` is ``false``

        """
        return # osid.calendaring.records.ScheduleSlotQueryRecord


class TimePeriodQuery(osid_queries.OsidObjectQuery):
    """This is the query for searching time periods.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_start(self, low, high, match):
        """Matches the time period start time between the given range inclusive.

        :param low: low time range
        :type low: ``osid.calendaring.DateTime``
        :param high: high time range
        :type high: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``zero``

        """
        pass

    def match_any_start(self, match):
        """Matches a time period that has any start time assigned.

        :param match: ``true`` to match time periods with any start time, ``false`` to match time periods with no start time
        :type match: ``boolean``

        """
        pass

    def clear_start_terms(self):
        """Clears the time period start terms."""
        pass

    start_terms = property(fdel=clear_start_terms)

    def match_end(self, low, high, match):
        """Matches the time period end time between the given range inclusive.

        :param low: low time range
        :type low: ``osid.calendaring.DateTime``
        :param high: high time range
        :type high: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``zero``

        """
        pass

    def match_any_end(self, match):
        """Matches a time period that has any end time assigned.

        :param match: ``true`` to match time periods with any end time, ``false`` to match time periods with no end time
        :type match: ``boolean``

        """
        pass

    def clear_end_terms(self):
        """Clears the time period end terms."""
        pass

    end_terms = property(fdel=clear_end_terms)

    def match_time(self, time, match):
        """Matches time periods that include the given time.

        :param time: date
        :type time: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``

        """
        pass

    def match_time_inclusive(self, start, end, match):
        """Matches time periods with start and end times between the given range inclusive.

        :param start: start date
        :type start: ``osid.calendaring.DateTime``
        :param end: end date
        :type end: ``osid.calendaring.DateTime``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``end`` is less than ``start``
        :raise: ``NullArgument`` -- ``start`` or ``end`` is ``zero``

        """
        pass

    def match_any_time(self, match):
        """Matches a time period that has any time assigned.

        :param match: ``true`` to match time periods with any time, ``false`` to match time periods with no time
        :type match: ``boolean``

        """
        pass

    def clear_time_terms(self):
        """Clears the time terms."""
        pass

    time_terms = property(fdel=clear_time_terms)

    def match_duration(self, low, high, match):
        """Matches the time period duration between the given range inclusive.

        :param low: low duration range
        :type low: ``osid.calendaring.Duration``
        :param high: high duration range
        :type high: ``osid.calendaring.Duration``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``InvalidArgument`` -- ``high`` is less than ``low``
        :raise: ``NullArgument`` -- ``high`` or ``low`` is ``null``

        """
        pass

    def clear_duration_terms(self):
        """Clears the duration terms."""
        pass

    duration_terms = property(fdel=clear_duration_terms)

    def match_exception_id(self, event_id, match):
        """Sets the event ``Id`` for this query to match exceptions.

        :param event_id: an exception event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_exception_id_terms(self):
        """Clears the exception event ``Id`` terms."""
        pass

    exception_id_terms = property(fdel=clear_exception_id_terms)

    def supports_exception_query(self):
        """Tests if an ``EventQuery`` is available for querying exception events.

        :return: ``true`` if a exception query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_exception_query(self):
        """Gets the query for an exception event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_exception_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    exception_query = property(fget=get_exception_query)

    def match_any_exception(self, match):
        """Matches a time period that has any exception event assigned.

        :param match: ``true`` to match time periods with any exception, ``false`` to match time periods with no exception
        :type match: ``boolean``

        """
        pass

    def clear_exception_terms(self):
        """Clears the exception event terms."""
        pass

    exception_terms = property(fdel=clear_exception_terms)

    def match_event_id(self, event_id, match):
        """Sets the event ``Id`` for this query.

        :param event_id: an event or recurring event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_event_id_terms(self):
        """Clears the event ``Id`` terms."""
        pass

    event_id_terms = property(fdel=clear_event_id_terms)

    def supports_event_query(self):
        """Tests if an ``EventQuery`` is available for querying events.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_event_query(self):
        """Gets the query for an event or recurring event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    event_query = property(fget=get_event_query)

    def match_any_event(self, match):
        """Matches a time period that has any event assigned.

        :param match: ``true`` to match time periods with any event, ``false`` to match time periods with no events
        :type match: ``boolean``

        """
        pass

    def clear_event_terms(self):
        """Clears the event terms."""
        pass

    event_terms = property(fdel=clear_event_terms)

    def match_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_calendar_id_terms(self):
        """Clears the calendar ``Id`` terms."""
        pass

    calendar_id_terms = property(fdel=clear_calendar_id_terms)

    def supports_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available for querying resources.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    calendar_query = property(fget=get_calendar_query)

    def clear_calendar_terms(self):
        """Clears the calendar terms."""
        pass

    calendar_terms = property(fdel=clear_calendar_terms)

    def get_time_period_query_record(self, time_period_record_type):
        """Gets the time period query record corresponding to the given ``TimePeriod`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param time_period_record_type: a time period query record type
        :type time_period_record_type: ``osid.type.Type``
        :return: the time period query record
        :rtype: ``osid.calendaring.records.TimePeriodQueryRecord``
        :raise: ``NullArgument`` -- ``time_period_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(time_period_record_type)`` is ``false``

        """
        return # osid.calendaring.records.TimePeriodQueryRecord


class CommitmentQuery(osid_queries.OsidRelationshipQuery):
    """This is the query for searching commitments.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_event_id(self, event_id, match):
        """Sets the event ``Id`` for this query.

        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_event_id_terms(self):
        """Clears the event ``Id`` terms."""
        pass

    event_id_terms = property(fdel=clear_event_id_terms)

    def supports_event_query(self):
        """Tests if an ``EventQuery`` is available.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_event_query(self):
        """Gets the query for an event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    event_query = property(fget=get_event_query)

    def clear_event_terms(self):
        """Clears the event terms."""
        pass

    event_terms = property(fdel=clear_event_terms)

    def match_resource_id(self, resource_id, match):
        """Sets the resource ``Id`` for this query.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``

        """
        pass

    def clear_resource_id_terms(self):
        """Clears the resource ``Id`` terms."""
        pass

    resource_id_terms = property(fdel=clear_resource_id_terms)

    def supports_resource_query(self):
        """Tests if a ``ResourceQuery`` is available for querying resources.

        :return: ``true`` if a resource query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_resource_query(self):
        """Gets the query for a resource.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the resource query
        :rtype: ``osid.resource.ResourceQuery``
        :raise: ``Unimplemented`` -- ``supports_resource_query()`` is ``false``

        """
        return # osid.resource.ResourceQuery

    resource_query = property(fget=get_resource_query)

    def clear_resource_terms(self):
        """Clears the resource terms."""
        pass

    resource_terms = property(fdel=clear_resource_terms)

    def match_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_calendar_id_terms(self):
        """Clears the calendar ``Id`` terms."""
        pass

    calendar_id_terms = property(fdel=clear_calendar_id_terms)

    def supports_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available for querying resources.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    calendar_query = property(fget=get_calendar_query)

    def clear_calendar_terms(self):
        """Clears the calendar terms."""
        pass

    calendar_terms = property(fdel=clear_calendar_terms)

    def get_commitment_query_record(self, commitment_record_type):
        """Gets the commitment query record corresponding to the given ``Commitment`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param commitment_record_type: a commitment query record type
        :type commitment_record_type: ``osid.type.Type``
        :return: the commitment query record
        :rtype: ``osid.calendaring.records.CommitmentQueryRecord``
        :raise: ``NullArgument`` -- ``commitment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(commitment_record_type)`` is ``false``

        """
        return # osid.calendaring.records.CommitmentQueryRecord


class CalendarQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching calendars.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_event_id(self, event_id, match):
        """Sets the event ``Id`` for this query.

        :param event_id: an event ``Id``
        :type event_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_event_id_terms(self):
        """Clears the event ``Id`` terms."""
        pass

    event_id_terms = property(fdel=clear_event_id_terms)

    def supports_event_query(self):
        """Tests if an ``EventQuery`` is available.

        :return: ``true`` if an event query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_event_query(self):
        """Gets the query for an event.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the event query
        :rtype: ``osid.calendaring.EventQuery``
        :raise: ``Unimplemented`` -- ``supports_event_query()`` is ``false``

        """
        return # osid.calendaring.EventQuery

    event_query = property(fget=get_event_query)

    def match_any_event(self, match):
        """Matches a calendar that has any event assigned.

        :param match: ``true`` to match calendars with any event, ``false`` to match calendars with no events
        :type match: ``boolean``

        """
        pass

    def clear_event_terms(self):
        """Clears the event terms."""
        pass

    event_terms = property(fdel=clear_event_terms)

    def match_time_period_id(self, time_period_id, match):
        """Sets the time period ``Id`` for this query.

        :param time_period_id: a time period ``Id``
        :type time_period_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``time_period_id`` is ``null``

        """
        pass

    def clear_time_period_id_terms(self):
        """Clears the time period ``Id`` terms."""
        pass

    time_period_id_terms = property(fdel=clear_time_period_id_terms)

    def supports_time_period_query(self):
        """Tests if a ``TimePeriodQuery`` is available.

        :return: ``true`` if a time period query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_time_period_query(self):
        """Gets the query for a time period.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the tiem period query
        :rtype: ``osid.calendaring.TimePeriodQuery``
        :raise: ``Unimplemented`` -- ``supports_time_period_query()`` is ``false``

        """
        return # osid.calendaring.TimePeriodQuery

    time_period_query = property(fget=get_time_period_query)

    def match_any_term(self, match):
        """Matches a calendar that has any term assigned.

        :param match: ``true`` to match calendars with any term, ``false`` to match calendars with no terms
        :type match: ``boolean``

        """
        pass

    def clear_term_terms(self):
        """Clears the term terms."""
        pass

    term_terms = property(fdel=clear_term_terms)

    def match_commitment_id(self, commitment_id, match):
        """Sets the commitment ``Id`` for this query.

        :param commitment_id: a commitment ``Id``
        :type commitment_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``commitment_id`` is ``null``

        """
        pass

    def clear_commitment_id_terms(self):
        """Clears the commitment ``Id`` terms."""
        pass

    commitment_id_terms = property(fdel=clear_commitment_id_terms)

    def supports_commitment_query(self):
        """Tests if a ``CommitmentQuery`` is available.

        :return: ``true`` if a commitment query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_commitment_query(self):
        """Gets the query for a commitment.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the commitment query
        :rtype: ``osid.calendaring.CommitmentQuery``
        :raise: ``Unimplemented`` -- ``supports_commitment_query()`` is ``false``

        """
        return # osid.calendaring.CommitmentQuery

    commitment_query = property(fget=get_commitment_query)

    def match_any_commitment(self, match):
        """Matches a calendar that has any event commitment.

        :param match: ``true`` to match calendars with any commitment, ``false`` to match calendars with no commitments
        :type match: ``boolean``

        """
        pass

    def clear_commitment_terms(self):
        """Clears the commitment terms."""
        pass

    commitment_terms = property(fdel=clear_commitment_terms)

    def match_ancestor_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query to match calendars that have the specified calendar as an ancestor.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_ancestor_calendar_id_terms(self):
        """Clears the ancestor calendar ``Id`` terms."""
        pass

    ancestor_calendar_id_terms = property(fdel=clear_ancestor_calendar_id_terms)

    def supports_ancestor_calendar_query(self):
        """Tests if a ``CalendarQuery`` is available.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    ancestor_calendar_query = property(fget=get_ancestor_calendar_query)

    def match_any_ancestor_calendar(self, match):
        """Matches a calendar that has any ancestor.

        :param match: ``true`` to match calendars with any ancestor, ``false`` to match root calendars
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_calendar_terms(self):
        """Clears the ancestor calendar terms."""
        pass

    ancestor_calendar_terms = property(fdel=clear_ancestor_calendar_terms)

    def match_descendant_calendar_id(self, calendar_id, match):
        """Sets the calendar ``Id`` for this query to match calendars that have the specified calendar as a descendant.

        :param calendar_id: a calendar ``Id``
        :type calendar_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_id`` is ``null``

        """
        pass

    def clear_descendant_calendar_id_terms(self):
        """Clears the descendant calendar ``Id`` terms."""
        pass

    descendant_calendar_id_terms = property(fdel=clear_descendant_calendar_id_terms)

    def supports_descendant_calendar_query(self):
        """Tests if a ``CalendarQuery``.

        :return: ``true`` if a calendar query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_calendar_query(self):
        """Gets the query for a calendar.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the calendar query
        :rtype: ``osid.calendaring.CalendarQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_calendar_query()`` is ``false``

        """
        return # osid.calendaring.CalendarQuery

    descendant_calendar_query = property(fget=get_descendant_calendar_query)

    def match_any_descendant_calendar(self, match):
        """Matches a calendar that has any descendant.

        :param match: ``true`` to match calendars with any descendant, ``false`` to match leaf calendars
        :type match: ``boolean``

        """
        pass

    def clear_descendant_calendar_terms(self):
        """Clears the descendant calendar terms."""
        pass

    descendant_calendar_terms = property(fdel=clear_descendant_calendar_terms)

    def get_calendar_query_record(self, calendar_record_type):
        """Gets the calendar query record corresponding to the given ``Calendar`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param calendar_record_type: a calendar record type
        :type calendar_record_type: ``osid.type.Type``
        :return: the calendar query record
        :rtype: ``osid.calendaring.records.CalendarQueryRecord``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(calendar_record_type)`` is ``false``

        """
        return # osid.calendaring.records.CalendarQueryRecord


