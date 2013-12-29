from ..osid import objects as osid_objects
from ..osid import markers as osid_markers


class Event(osid_objects.OsidObject, osid_markers.Temporal, osid_markers.Containable):
    """An ``Event`` represents a span of time and an optional location."""
    def is_implicit(self):
        """Tests if this event is implicit.

        An implicit event is one that is generated from an offset or
        recurring series.

        :return: ``true`` if this event is implicit, ``false`` if explicitly defined
        :rtype: ``boolean``

        """
        return # boolean

    def is_in_recurring_series(self):
        """Tests if this event is an implclit event part of a recurring event.

        If true, ``is_implicit()`` must also be true.

        :return: ``true`` if this event is part of a recurring series, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def is_superseding_event(self):
        """Tests if this event is a superseding event.

        If true, ``is_implicit()`` must also be true.

        :return: ``true`` if this event is superseding event, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def is_offset_event(self):
        """Tests if this event is an event calculated from an offset.

        If true, ``is_implicit()`` must also be true.

        :return: ``true`` if this event is an offset event, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_duration(self, units):
        """Gets the duration of the event.

        :param units: the units of the duration
        :type units: ``osid.calendaring.DateTimeResolution``
        :return: the duration
        :rtype: ``osid.calendaring.Duration``
        :raise: ``NullArgument`` -- ``units`` is ``null``

        """
        return # osid.calendaring.Duration

    def get_location_description(self):
        """Gets a descriptive location.

        :return: the location
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    location_description = property(fget=get_location_description)

    def has_location(self):
        """Tests if a location is associated with this event.

        :return: ``true`` if there is an associated location, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_location_id(self):
        """Gets the location ``Id``.

        :return: a location ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``

        """
        return # osid.id.Id

    location_id = property(fget=get_location_id)

    def get_location(self):
        """Gets the ``Location``.

        :return: a location
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Location

    location = property(fget=get_location)

    def has_sponsors(self):
        """Tests if a sponsor is associated with this event.

        :return: ``true`` if there is an associated sponsor. ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_sponsor_ids(self):
        """Gets the ``Id`` of the event sponsors.

        :return: the sponsor ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``has_sponsors()`` is ``false``

        """
        return # osid.id.IdList

    sponsor_ids = property(fget=get_sponsor_ids)

    def get_sponsors(self):
        """Gets the ``Sponsors``.

        :return: the sponsors
        :rtype: ``osid.resource.ResourceList``
        :raise: ``IllegalState`` -- ``has_sponsors()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.ResourceList

    sponsors = property(fget=get_sponsors)

    def get_event_record(self, event_record_type):
        """Gets the event record corresponding to the given ``Event`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``event_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(event_record_type)``
        is ``true`` .

        :param event_record_type: the type of the record to retrieve
        :type event_record_type: ``osid.type.Type``
        :return: the event record
        :rtype: ``osid.calendaring.records.EventRecord``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.EventRecord


class EventForm(osid_objects.OsidObjectForm, osid_objects.OsidTemporalForm, osid_objects.OsidContainableForm):
    """This is the form for creating and updating ``Events``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``EventAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_location_description_metadata(self):
        """Gets the metadata for a location description.

        :return: metadata for the location description
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    location_description_metadata = property(fget=get_location_description_metadata)

    def set_location_description(self, location):
        """Sets the location description.

        :param location: the new location description
        :type location: ``string``
        :raise: ``InvalidArgument`` -- ``location`` is invalid
        :raise: ``NoAccess`` -- ``location`` cannot be modified
        :raise: ``NullArgument`` -- ``location`` is ``null``

        """
        pass

    def clear_location_description(self):
        """Clears the location description.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    location_description = property(fset=set_location_description, fdel=clear_location_description)

    def get_location_metadata(self):
        """Gets the metadata for a location.

        :return: metadata for the location
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    location_metadata = property(fget=get_location_metadata)

    def set_location(self, location_id):
        """Sets the location.

        :param location_id: the new location
        :type location_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``location_id`` is invalid
        :raise: ``NoAccess`` -- ``location_id`` cannot be modified
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        """
        pass

    def clear_location(self):
        """Clears the location.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    location = property(fset=set_location, fdel=clear_location)

    def get_sponsor_metadata(self):
        """Gets the metadata for a sponsor.

        :return: metadata for the sponsor
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    sponsor_metadata = property(fget=get_sponsor_metadata)

    def set_sponsors(self, sponsor_ids):
        """Sets the sponsors.

        :param sponsor_ids: the new sponsor
        :type sponsor_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``sponsor_ids`` is invalid
        :raise: ``NoAccess`` -- ``sponsor_ids`` cannot be modified
        :raise: ``NullArgument`` -- ``sponsor_ids`` is ``null``

        """
        pass

    def clear_sponsors(self):
        """Clears the sponsors.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    sponsors = property(fset=set_sponsors, fdel=clear_sponsors)

    def get_event_form_record(self, event_record_type):
        """Gets the ``EventFormRecord`` corresponding to the given event record ``Type``.

        :param event_record_type: the event record type
        :type event_record_type: ``osid.type.Type``
        :return: the event form record
        :rtype: ``osid.calendaring.records.EventFormRecord``
        :raise: ``NullArgument`` -- ``event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.EventFormRecord


class EventList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``EventList`` provides a means for accessing ``Event`` elements sequentially either one at a time or many at a time.

    Examples: while (el.hasNext()) { Event event = el.getNextEvent(); }

    or
      while (el.hasNext()) {
           Event[] events = el.getNextEvents(el.available());
      }
    


    """
    def get_next_event(self):
        """Gets the next ``Event`` in this list.

        :return: the next ``Event`` in this list. The ``has_next()`` method should be used to test that a next ``Event`` is available before calling this method.
        :rtype: ``osid.calendaring.Event``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Event

    next_event = property(fget=get_next_event)

    def get_next_events(self, n):
        """Gets the next set of ``Event`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Event`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Event`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.Event``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Event


class RecurringEvent(osid_objects.OsidObject, osid_markers.Containable):
    """A ``RecurringEvent`` an event that repeats over a set of ``Schedules``."""
    def get_schedule_ids(self):
        """Gets the ``Schedule Id`` of this composite event.

        :return: the recurring schedule ``Ids``
        :rtype: ``osid.id.IdList``

        """
        return # osid.id.IdList

    schedule_ids = property(fget=get_schedule_ids)

    def get_schedules(self):
        """Gets the recurring schedule in this composite event.

        :return: the recurring schedules
        :rtype: ``osid.calendaring.ScheduleList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.ScheduleList

    schedules = property(fget=get_schedules)

    def get_superseding_event_ids(self):
        """Gets the superseding event ``Ids``.

        A superseding event is one that replaces another in a series.

        :return: list of superseding event ``Ids``
        :rtype: ``osid.id.IdList``

        """
        return # osid.id.IdList

    superseding_event_ids = property(fget=get_superseding_event_ids)

    def get_superseding_events(self):
        """Gets the superseding events.

        A superseding event is one that replaces another in a series.

        :return: list of superseding events
        :rtype: ``osid.calendaring.SupersedingEventList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.SupersedingEventList

    superseding_events = property(fget=get_superseding_events)

    def get_specific_meeting_times(self):
        """Gets specific dates for this event outside of the schedules.

        Specific dates are excluded from blackouts.

        :return: speciifc list of dates
        :rtype: ``osid.calendaring.MeetingTimeList``

        """
        return # osid.calendaring.MeetingTimeList

    specific_meeting_times = property(fget=get_specific_meeting_times)

    def get_event_ids(self):
        """Gets the composed event ``Ids``.

        :return: list of event ``Ids``
        :rtype: ``osid.id.IdList``

        """
        return # osid.id.IdList

    event_ids = property(fget=get_event_ids)

    def get_events(self):
        """Gets the composed events.

        :return: list of events
        :rtype: ``osid.calendaring.EventList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.EventList

    events = property(fget=get_events)

    def get_blackouts(self):
        """Gets the blackout dates for this recurring event.

        Recurring events overlapping with the time intervals do not
        appear in their series.

        :return: recurring event exceptions
        :rtype: ``osid.calendaring.DateTimeIntervalList``

        """
        return # osid.calendaring.DateTimeIntervalList

    blackouts = property(fget=get_blackouts)

    def has_sponsors(self):
        """Tests if a sponsor is associated with the overall recurring event.

        :return: ``true`` if there is an associated sponsor. ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_sponsor_ids(self):
        """Gets the ``Id`` of the recurring event sponsors.

        :return: the sponsor ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``has_sponsors()`` is ``false``

        """
        return # osid.id.IdList

    sponsor_ids = property(fget=get_sponsor_ids)

    def get_sponsors(self):
        """Gets the ``Sponsors``.

        :return: the sponsors
        :rtype: ``osid.resource.ResourceList``
        :raise: ``IllegalState`` -- ``has_sponsors()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.ResourceList

    sponsors = property(fget=get_sponsors)

    def get_recurring_event_record(self, recurring_event_record_type):
        """Gets the recurring event record corresponding to the given ``RecurringEvent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``recurring_event_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(recurring_event_record_type)`` is ``true`` .

        :param recurring_event_record_type: the type of the record to retrieve
        :type recurring_event_record_type: ``osid.type.Type``
        :return: the recurring event record
        :rtype: ``osid.calendaring.records.RecurringEventRecord``
        :raise: ``NullArgument`` -- ``recurring_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(recurring_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.RecurringEventRecord


class RecurringEventForm(osid_objects.OsidObjectForm, osid_objects.OsidContainableForm):
    """This is the form for creating and updating ``RecurringEvents``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RecurringEventAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    def get_sponsor_metadata(self):
        """Gets the metadata for a sponsor.

        :return: metadata for the sponsor
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    sponsor_metadata = property(fget=get_sponsor_metadata)

    def set_sponsors(self, sponsor_ids):
        """Sets the sponsors.

        :param sponsor_ids: the new sponsor
        :type sponsor_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``sponsor_ids`` is invalid
        :raise: ``NoAccess`` -- ``sponsor_ids`` cannot be modified
        :raise: ``NullArgument`` -- ``sponsor_ids`` is ``null``

        """
        pass

    def clear_sponsors(self):
        """Clears the sponsors.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    sponsors = property(fset=set_sponsors, fdel=clear_sponsors)

    def get_recurring_event_form_record(self, recurring_event_record_type):
        """Gets the ``RecurringEventFormRecord`` corresponding to the given recurring event record ``Type``.

        :param recurring_event_record_type: the recurring event record type
        :type recurring_event_record_type: ``osid.type.Type``
        :return: the recurring event form record
        :rtype: ``osid.calendaring.records.RecurringEventFormRecord``
        :raise: ``NullArgument`` -- ``recurring_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(recurring_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.RecurringEventFormRecord


class RecurringEventList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``RecurringEventList`` provides a means for accessing ``RecurringEvent`` elements sequentially either one at a time or many at a time.

    Examples: while (rel.hasNext()) { RecurringEvent event =
    rel.getNextRecurringEvent(); }

    or
      while (rel.hasNext()) {
           RecurringEvent[] events = rel.getNextRecurringEvents(rel.available());
      }
    


    """
    def get_next_recurring_event(self):
        """Gets the next ``RecurringEvent`` in this list.

        :return: the next ``RecurringEvent`` in this list. The ``has_next()`` method should be used to test that a next ``RecurringEvent`` is available before calling this method.
        :rtype: ``osid.calendaring.RecurringEvent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.RecurringEvent

    next_recurring_event = property(fget=get_next_recurring_event)

    def get_next_recurring_events(self, n):
        """Gets the next set of ``RecurringEvent`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``RecurringEvent`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``RecurringEvent`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.RecurringEvent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.RecurringEvent


class SupersedingEvent(osid_objects.OsidRule):
    """A ``SupersedingEvent`` represents an override of an event such as an individual item in a recurring series.

    The event which is to supersede another must already be created. The
    ``SupersedingEvent`` rule causes the superseded ``Event`` to be
    overidden with the superseding ``Event`` at the superseding
    ``Event`` 's date and time.

    """
    def get_superseded_event_id(self):
        """Gets the event ``Id`` that is to be superseded.

        :return: the superseding event ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    superseded_event_id = property(fget=get_superseded_event_id)

    def get_superseded_event(self):
        """Gets the event that is to be superseded.

        :return: the superseding event
        :rtype: ``osid.calendaring.Event``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Event

    superseded_event = property(fget=get_superseded_event)

    def get_superseding_event_id(self):
        """Gets the event ``Id`` that is superseding another.

        :return: the superseding event ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    superseding_event_id = property(fget=get_superseding_event_id)

    def get_superseding_event(self):
        """Gets the event that is superseding another.

        :return: the superseding event
        :rtype: ``osid.calendaring.Event``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Event

    superseding_event = property(fget=get_superseding_event)

    def supersedes_by_date(self):
        """Tests if the superseding event replaces an event within a recurring series offered at a specific date/time.

        If ``supersedes_by_date()`` is true, then
        ``supersedes_by_position()`` must be false.

        :return: ``true`` if an event is superseded by date, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_superseded_date(self):
        """Gets the date of an event to replace if a recurring event is offered on that date.

        :return: the date of the event to replace
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``supersedes_by_date()`` is ``false``

        """
        return # osid.calendaring.DateTime

    superseded_date = property(fget=get_superseded_date)

    def supersedes_by_position(self):
        """Tests if the superseding event replaces an event within a recurring series identified by its denormalized position in the series.

        A negative number counts from the end of the series. If
        ``supersedes_by_position()`` is ``true,`` then
        ``supersedes_by_date()`` must be ``false``.

        :return: ``true`` if an event is superseded by position, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_superseded_event_position(self):
        """Gets the position in the denormalized recurring series of the event to replace.

        Positive numbers count from the start and negative numbers count
        from the end. Zero is invalid.

        :return: the position of the event to replace
        :rtype: ``integer``
        :raise: ``IllegalState`` -- ``supersedes_by_position()`` is ``false``

        """
        return # integer

    superseded_event_position = property(fget=get_superseded_event_position)

    def get_superseding_event_record(self, superseding_event_record_type):
        """Gets the superseding event record corresponding to the given ``SupersedingEvent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``superseding_event_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(superseding_event_record_type)`` is ``true`` .

        :param superseding_event_record_type: the type of the record to retrieve
        :type superseding_event_record_type: ``osid.type.Type``
        :return: the superseding event record
        :rtype: ``osid.calendaring.records.SupersedingEventRecord``
        :raise: ``NullArgument`` -- ``superseding_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(superseding_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.SupersedingEventRecord


class SupersedingEventForm(osid_objects.OsidRuleForm):
    """This is the form for creating and updating ``SupersedingEvents``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``SupersedingEventAdminSession``. For each data element that may be
    set, metadata may be examined to provide display hints or data
    constraints.

    """
    def get_superseded_date_metadata(self):
        """Gets the metadata to superseding an event within a recurring series by date.

        :return: metadata for a superseded date
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    superseded_date_metadata = property(fget=get_superseded_date_metadata)

    def set_superseded_date(self, date):
        """Sets the superseded date.

        :param date: the new superseded date
        :type date: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``date`` is invalid
        :raise: ``NoAccess`` -- ``date`` cannot be modified
        :raise: ``NullArgument`` -- ``date`` is ``null``

        """
        pass

    def clear_superseded_date(self):
        """Clears the superseded date.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    superseded_date = property(fset=set_superseded_date, fdel=clear_superseded_date)

    def get_superseded_position_metadata(self):
        """Gets the metadata to superseding an event within a recurring series by date.

        :return: metadata for a superseded date
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    superseded_position_metadata = property(fget=get_superseded_position_metadata)

    def set_superseded_position(self, position):
        """Sets the superseded position.

        A negative number counts from the end of the series.

        :param position: the new superseded position
        :type position: ``integer``
        :raise: ``InvalidArgument`` -- ``position`` is invalid
        :raise: ``NoAccess`` -- ``position`` cannot be modified

        """
        pass

    def clear_superseded_position(self):
        """Clears the superseded position.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    superseded_position = property(fset=set_superseded_position, fdel=clear_superseded_position)

    def get_superseding_event_form_record(self, superseding_event_record_type):
        """Gets the ``SupersedingEventFormRecord`` corresponding to the given superseding event record ``Type``.

        :param superseding_event_record_type: the superseding event record type
        :type superseding_event_record_type: ``osid.type.Type``
        :return: the superseding event form record
        :rtype: ``osid.calendaring.records.SupersedingEventFormRecord``
        :raise: ``NullArgument`` -- ``superseding_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(superseding_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.SupersedingEventFormRecord


class SupersedingEventList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``SupersedingEventList`` provides a means for accessing ``SupersedingEvent`` elements sequentially either one at a time or many at a time.

    Examples: while (sel.hasNext()) { SupersedingEvent event =
    sel.getNextSupersedingEvent(); }

    or
      while (sel.hasNext()) {
           SupersedingEvent[] events = sel.getNextSupersedingEvents(sel.available());
      }
    


    """
    def get_next_superseding_event(self):
        """Gets the next ``SupersedingEvent`` in this list.

        :return: the next ``SupersedingEvent`` in this list. The ``has_next()`` method should be used to test that a next ``SupersedingEvent`` is available before calling this method.
        :rtype: ``osid.calendaring.SupersedingEvent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.SupersedingEvent

    next_superseding_event = property(fget=get_next_superseding_event)

    def get_next_superseding_events(self, n):
        """Gets the next set of ``SupersedingEvent`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``SupersedingEvent`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``SupersedingEvent`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.SupersedingEvent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.SupersedingEvent


class OffsetEvent(osid_objects.OsidRule):
    """An ``OffsetEvent`` describes events that are relative to other events.

    ``OffsetEvents`` may have a fixed or rubber start date as well as a
    fixed or rubber end date. A rubber start and end date has a variable
    duration based on the starting and ending milestones. An
    ``OffsetEvent`` with a fixed start date and a fixed duration behaves
    like a normal fixed ``Event``.

    Creating an ``OffsetEvent`` produces an ``Event`` that is based on
    these offset rules.

    """
    def has_fixed_start_time(self):
        """Tests if this offset event is based on a fixed start time.

        :return: ``true`` if this offset is based on a fixed start time, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_fixed_start_time(self):
        """Gets the fixed start time for this event.

        :return: the fixed start time
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- ``has_fixed_start_ime()`` is ``false``

        """
        return # osid.calendaring.DateTime

    fixed_start_time = property(fget=get_fixed_start_time)

    def get_start_reference_event_id(self):
        """Gets the ``Event Id`` to which the start of this event is offset.

        :return: the relative event ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_fixed_start_time()`` is ``true``

        """
        return # osid.id.Id

    start_reference_event_id = property(fget=get_start_reference_event_id)

    def get_start_reference_event(self):
        """Gets the ``Event`` to which the start of this event is offset.

        :return: the relative event
        :rtype: ``osid.calendaring.Event``
        :raise: ``IllegalState`` -- ``has_fixed_start_time()`` is ``true``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Event

    start_reference_event = property(fget=get_start_reference_event)

    def has_fixed_start_offset(self):
        """Tests if this offset start time based on a fixed period of time.

        :return: ``true`` if this offset is based on a fixed period of time, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_fixed_start_time()`` is ``true``

        """
        return # boolean

    def get_fixed_start_offset(self):
        """Gets the fixed starting time offset.

        :return: the offset
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- ``has_fixed_start_offset()`` is ``false``

        """
        return # osid.calendaring.Duration

    fixed_start_offset = property(fget=get_fixed_start_offset)

    def has_relative_weekday_start_offset(self):
        """Tests if this starting time offset is a based on a relative weekday.

        :return: ``true`` if this offset is based on a relative weekday, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_fixed_start_offset()`` is ``true``

        """
        return # boolean

    def get_relative_weekday_start_offset(self):
        """Gets the starting offset as the nth weekday from the relative event.

        Zero is no offset.

        :return: the offset
        :rtype: ``integer``
        :raise: ``IllegalState`` -- ``has_relative_weekday_start_offset()`` is ``false``

        """
        return # integer

    relative_weekday_start_offset = property(fget=get_relative_weekday_start_offset)

    def get_relative_start_weekday(self):
        """Gets the starting weekday number.

        The weekday is based on the calendar type. On the Gregorian
        calendar, 0 is Sunday.

        :return: the weekday number
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``has_relative_weekday_start_offset()`` is ``false``

        """
        return # cardinal

    relative_start_weekday = property(fget=get_relative_start_weekday)

    def has_fixed_duration(self):
        """Tests if this offset event is based on a fixed duration.

        :return: ``true`` if this offset is based on a fixed duration, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_duration(self, units):
        """Gets the duration of the offset event.

        :param units: the units of the duration
        :type units: ``osid.calendaring.DateTimeResolution``
        :return: the duration
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- ``has_fixed_duration()`` is ``false``
        :raise: ``NullArgument`` -- ``units`` is ``null``

        """
        return # osid.calendaring.Duration

    def get_end_reference_event_id(self):
        """Gets the ``Event Id`` to which the end of this event is offset.

        :return: the relative event ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_fixed_duration()`` is ``true``

        """
        return # osid.id.Id

    end_reference_event_id = property(fget=get_end_reference_event_id)

    def get_end_reference_event(self):
        """Gets the ``Event`` to which the end of this event is offset.

        :return: the relative event
        :rtype: ``osid.calendaring.Event``
        :raise: ``IllegalState`` -- ``has_fixed_duration()`` is ``true``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Event

    end_reference_event = property(fget=get_end_reference_event)

    def has_fixed_end_offset(self):
        """Tests if this offset end time based on a fixed period of time.

        :return: ``true`` if this offset is based on a fixed period of time, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_fixed_duration()`` is ``true``

        """
        return # boolean

    def get_fixed_end_offset(self):
        """Gets the fixed ending time offset.

        :return: the offset
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- ``has_fixed_end_offset()`` is ``false``

        """
        return # osid.calendaring.Duration

    fixed_end_offset = property(fget=get_fixed_end_offset)

    def has_relative_weekday_end_offset(self):
        """Tests if this ending time offset is a based on a relative weekday.

        :return: ``true`` if this offset is based on a relative weekday, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``IllegalState`` -- ``has_fixed_end_offset()`` is ``true``

        """
        return # boolean

    def get_relative_weekday_end_offset(self):
        """Gets the ending offset as the nth weekday from the relative event.

        Zero is no offset.

        :return: the offset
        :rtype: ``integer``
        :raise: ``IllegalState`` -- ``has_relative_weekday_end_offset()`` is ``false``

        """
        return # integer

    relative_weekday_end_offset = property(fget=get_relative_weekday_end_offset)

    def get_relative_end_weekday(self):
        """Gets the ending weekday number.

        The weekday is based on the calendar type. On the Gregorian
        calendar, 0 is Sunday.

        :return: the weekday number
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``has_relative_weekday_end_offset()`` is ``false``

        """
        return # cardinal

    relative_end_weekday = property(fget=get_relative_end_weekday)

    def get_location_description(self):
        """Gets a descriptive location.

        :return: the location
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    location_description = property(fget=get_location_description)

    def has_location(self):
        """Tests if a location is associated with this event.

        :return: ``true`` if there is an associated location, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_location_id(self):
        """Gets the location ``Id``.

        :return: a location ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``

        """
        return # osid.id.Id

    location_id = property(fget=get_location_id)

    def get_location(self):
        """Gets the ``Location``.

        :return: a location
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Location

    location = property(fget=get_location)

    def has_sponsors(self):
        """Tests if a sponsor is associated with this event.

        :return: ``true`` if there is an associated sponsor. ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_sponsor_ids(self):
        """Gets the ``Id`` of the event sponsors.

        :return: the sponsor ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``IllegalState`` -- ``has_sponsors()`` is ``false``

        """
        return # osid.id.IdList

    sponsor_ids = property(fget=get_sponsor_ids)

    def get_sponsors(self):
        """Gets the ``Sponsors``.

        :return: the sponsors
        :rtype: ``osid.resource.ResourceList``
        :raise: ``IllegalState`` -- ``has_sponsors()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.ResourceList

    sponsors = property(fget=get_sponsors)

    def get_offset_event_record(self, offset_event_record_type):
        """Gets the offset event record corresponding to the given ``OffsetEvent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``offset_event_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(offset_event_record_type)`` is ``true`` .

        :param offset_event_record_type: the type of the record to retrieve
        :type offset_event_record_type: ``osid.type.Type``
        :return: the offset event record
        :rtype: ``osid.calendaring.records.OffsetEventRecord``
        :raise: ``NullArgument`` -- ``offset_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(offset_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.OffsetEventRecord


class OffsetEventForm(osid_objects.OsidRuleForm):
    """This is the form for creating and updating ``OffsetEvents``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``OffsetEventAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_fixed_start_time_metadata(self):
        """Gets the metadata for the fixed start time.

        :return: metadata for the fixed start time
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    fixed_start_time_metadata = property(fget=get_fixed_start_time_metadata)

    def set_fixed_start_time(self, date):
        """Sets the fixed start time.

        :param date: the fixed start time
        :type date: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``date`` is invalid
        :raise: ``NoAccess`` -- ``date`` cannot be modified
        :raise: ``NullArgument`` -- ``date`` is ``null``

        """
        pass

    def clear_fixed_start_time(self):
        """Clears the fixed start time.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    fixed_start_time = property(fset=set_fixed_start_time, fdel=clear_fixed_start_time)

    def get_start_reference_event_metadata(self):
        """Gets the metadata for the starting reference event.

        :return: metadata for the starting reference event
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    start_reference_event_metadata = property(fget=get_start_reference_event_metadata)

    def set_start_reference_event(self, event_id):
        """Sets the fixed start time.

        :param event_id: the start reference event ``Id``
        :type event_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``event_id`` is invalid
        :raise: ``NoAccess`` -- ``event_id`` cannot be modified
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_start_reference_event(self):
        """Clears the start reference event.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    start_reference_event = property(fset=set_start_reference_event, fdel=clear_start_reference_event)

    def get_fixed_start_offset_metadata(self):
        """Gets the metadata for the fixed start offset.

        :return: metadata for the fixed start offset
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    fixed_start_offset_metadata = property(fget=get_fixed_start_offset_metadata)

    def set_fixed_start_offset(self, offset):
        """Sets the fixed start offset.

        :param offset: the fixed offset
        :type offset: ``osid.calendaring.Duration``
        :raise: ``InvalidArgument`` -- ``offset`` is invalid
        :raise: ``NoAccess`` -- ``offset`` cannot be modified
        :raise: ``NullArgument`` -- ``offset`` is ``null``

        """
        pass

    def clear_fixed_start_offset(self):
        """Clears the fixed start offset.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    fixed_start_offset = property(fset=set_fixed_start_offset, fdel=clear_fixed_start_offset)

    def get_relative_weekday_start_offset_metadata(self):
        """Gets the metadata for the relative weekday offset.

        :return: metadata for the relative weekday offset
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    relative_weekday_start_offset_metadata = property(fget=get_relative_weekday_start_offset_metadata)

    def set_relative_weekday_start_offset(self, offset):
        """Sets the relative weekday offset as the nth weekday from the relative event.

        :param offset: the week offset
        :type offset: ``integer``
        :raise: ``InvalidArgument`` -- ``offset`` is invalid
        :raise: ``NoAccess`` -- ``offset`` cannot be modified

        """
        pass

    def clear_relative_weekday_start_offset(self):
        """Clears the relative weekday offset.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    relative_weekday_start_offset = property(fset=set_relative_weekday_start_offset, fdel=clear_relative_weekday_start_offset)

    def get_relative_start_weekday_metadata(self):
        """Gets the metadata for the relative weekday.

        :return: metadata for the relative weekday
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    relative_start_weekday_metadata = property(fget=get_relative_start_weekday_metadata)

    def set_relative_start_weekday(self, weekday):
        """Sets the relative weekday.

        :param weekday: the weekday
        :type weekday: ``cardinal``
        :raise: ``InvalidArgument`` -- ``weekday`` is invalid
        :raise: ``NoAccess`` -- ``weekday`` cannot be modified

        """
        pass

    def clear_relative_start_weekday(self):
        """Clears the relative start weekday.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    relative_start_weekday = property(fset=set_relative_start_weekday, fdel=clear_relative_start_weekday)

    def get_fixed_duration_metadata(self):
        """Gets the metadata for the fixed duration.

        :return: metadata for the fixed duration
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    fixed_duration_metadata = property(fget=get_fixed_duration_metadata)

    def set_fixed_duration(self, duration):
        """Sets the fixed duration.

        :param duration: the fixed duration
        :type duration: ``osid.calendaring.Duration``
        :raise: ``InvalidArgument`` -- ``duration`` is invalid
        :raise: ``NoAccess`` -- ``duration`` cannot be modified
        :raise: ``NullArgument`` -- ``duration`` is ``null``

        """
        pass

    def clear_fixed_duration(self):
        """Clears the fixed duration.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    fixed_duration = property(fset=set_fixed_duration, fdel=clear_fixed_duration)

    def get_end_reference_event_metadata(self):
        """Gets the metadata for the ending reference event.

        :return: metadata for the ending reference event
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    end_reference_event_metadata = property(fget=get_end_reference_event_metadata)

    def set_end_reference_event(self, event_id):
        """Sets the fixed end time.

        :param event_id: the end reference event ``Id``
        :type event_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``event_id`` is invalid
        :raise: ``NoAccess`` -- ``event_id`` cannot be modified
        :raise: ``NullArgument`` -- ``event_id`` is ``null``

        """
        pass

    def clear_end_reference_event(self):
        """Clears the ending reference event.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    end_reference_event = property(fset=set_end_reference_event, fdel=clear_end_reference_event)

    def get_fixed_end_offset_metadata(self):
        """Gets the metadata for the fixed end offset.

        :return: metadata for the fixed end offset
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    fixed_end_offset_metadata = property(fget=get_fixed_end_offset_metadata)

    def set_fixed_end_offset(self, offset):
        """Sets the fixed end offset.

        :param offset: the fixed offset
        :type offset: ``osid.calendaring.Duration``
        :raise: ``InvalidArgument`` -- ``offset`` is invalid
        :raise: ``NoAccess`` -- ``offset`` cannot be modified
        :raise: ``NullArgument`` -- ``offset`` is ``null``

        """
        pass

    def clear_fixed_end_offset(self):
        """Clears the fixed end offset.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    fixed_end_offset = property(fset=set_fixed_end_offset, fdel=clear_fixed_end_offset)

    def get_relative_weekday_end_offset_metadata(self):
        """Gets the metadata for the relative weekday offset.

        :return: metadata for the relative weekday offset
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    relative_weekday_end_offset_metadata = property(fget=get_relative_weekday_end_offset_metadata)

    def set_relative_weekday_end_offset(self, offset):
        """Sets the relative weekday offset as the nth weekday from the relative event.

        :param offset: the week offset
        :type offset: ``integer``
        :raise: ``InvalidArgument`` -- ``offset`` is invalid
        :raise: ``NoAccess`` -- ``offset`` cannot be modified

        """
        pass

    def clear_relative_weekday_end_offset(self):
        """Clears the relative weekday offset.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    relative_weekday_end_offset = property(fset=set_relative_weekday_end_offset, fdel=clear_relative_weekday_end_offset)

    def get_relative_end_weekday_metadata(self):
        """Gets the metadata for the relative weekday.

        :return: metadata for the relative weekday
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    relative_end_weekday_metadata = property(fget=get_relative_end_weekday_metadata)

    def set_relative_end_weekday(self, weekday):
        """Sets the relative weekday.

        :param weekday: the weekday
        :type weekday: ``cardinal``
        :raise: ``InvalidArgument`` -- ``weekday`` is invalid
        :raise: ``NoAccess`` -- ``weekday`` cannot be modified

        """
        pass

    def clear_relative_end_weekday(self):
        """Clears the relative end weekday.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    relative_end_weekday = property(fset=set_relative_end_weekday, fdel=clear_relative_end_weekday)

    def get_location_description_metadata(self):
        """Gets the metadata for a location description.

        :return: metadata for the location description
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    location_description_metadata = property(fget=get_location_description_metadata)

    def set_location_description(self, location):
        """Sets the location description.

        :param location: the new location description
        :type location: ``string``
        :raise: ``InvalidArgument`` -- ``location`` is invalid
        :raise: ``NoAccess`` -- ``location`` cannot be modified
        :raise: ``NullArgument`` -- ``location`` is ``null``

        """
        pass

    def clear_location_description(self):
        """Clears the location description.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    location_description = property(fset=set_location_description, fdel=clear_location_description)

    def get_location_metadata(self):
        """Gets the metadata for a location.

        :return: metadata for the location
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    location_metadata = property(fget=get_location_metadata)

    def set_location(self, location_id):
        """Sets the location.

        :param location_id: the new location
        :type location_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``location_id`` is invalid
        :raise: ``NoAccess`` -- ``location_id`` cannot be modified
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        """
        pass

    def clear_location(self):
        """Clears the location.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    location = property(fset=set_location, fdel=clear_location)

    def get_sponsor_metadata(self):
        """Gets the metadata for a sponsor.

        :return: metadata for the sponsor
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    sponsor_metadata = property(fget=get_sponsor_metadata)

    def set_sponsors(self, sponsor_ids):
        """Sets the sponsors.

        :param sponsor_ids: the new sponsor
        :type sponsor_ids: ``osid.id.Id[]``
        :raise: ``InvalidArgument`` -- ``sponsor_ids`` is invalid
        :raise: ``NoAccess`` -- ``sponsor_ids`` cannot be modified
        :raise: ``NullArgument`` -- ``sponsor_ids`` is ``null``

        """
        pass

    def clear_sponsors(self):
        """Clears the sponsors.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    sponsors = property(fset=set_sponsors, fdel=clear_sponsors)

    def get_offset_event_form_record(self, offset_event_record_type):
        """Gets the ``OffsetEventFormRecord`` corresponding to the given schedule record ``Type``.

        :param offset_event_record_type: the offset event record type
        :type offset_event_record_type: ``osid.type.Type``
        :return: the offset event form record
        :rtype: ``osid.calendaring.records.OffsetEventFormRecord``
        :raise: ``NullArgument`` -- ``offset_event_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(offset_event_record_type)`` is ``false``

        """
        return # osid.calendaring.records.OffsetEventFormRecord


class OffsetEventList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``OffsetEventList`` provides a means for accessing ``OffsetEvent`` elements sequentially either one at a time or many at a time.

    Examples: while (oel.hasNext()) { OffsetEvent event =
    oel.getNextOffsetEvent(); }

    or
      while (oel.hasNext()) {
           OffsetEvent[] events = oel.getNextOffsetEvents(oel.available());
      }
    


    """
    def get_next_offset_event(self):
        """Gets the next ``OffsetEvent`` in this list.

        :return: the next ``OffsetEvent`` in this list. The ``has_next()`` method should be used to test that a next ``OffsetEvent`` is available before calling this method.
        :rtype: ``osid.calendaring.OffsetEvent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.OffsetEvent

    next_offset_event = property(fget=get_next_offset_event)

    def get_next_offset_events(self, n):
        """Gets the next set of ``OffsetEvent`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``OffsetEvent`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``OffsetEvent`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.OffsetEvent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.OffsetEvent


class Schedule(osid_objects.OsidObject):
    """A ``Schedule`` is a scheduled time slot offered within a time interval at a location."""
    def get_schedule_slot_id(self):
        """Gets the ``Id`` of the schedule slot.

        :return: the schedule slot ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    schedule_slot_id = property(fget=get_schedule_slot_id)

    def get_schedule_slot(self):
        """Gets the schedule slot included inside this one.

        :return: the schedule slot
        :rtype: ``osid.calendaring.ScheduleSlot``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.ScheduleSlot

    schedule_slot = property(fget=get_schedule_slot)

    def has_time_period(self):
        """Tests if a ``TimePeriod`` is associated with this schedule.

        The time period determines the start and end time of the
        recurring series.

        :return: ``true`` if there is an associated ``TimePeriod,``  ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_time_period_id(self):
        """Gets the ``TimePeriod Id`` for this recurring event.

        A ``Schedule`` with an associated ``TimePeriod`` overrides any
        start or end date set.

        :return: the time period ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_time_period()`` is ``false``

        """
        return # osid.id.Id

    time_period_id = property(fget=get_time_period_id)

    def get_time_period(self):
        """Gets the ``TimePeriod`` for this recurring event.

        A ``Schedule`` with an associated ``TimePeriod`` overrides any
        start or end date set.

        :return: the time period
        :rtype: ``osid.calendaring.TimePeriod``
        :raise: ``IllegalState`` -- ``has_time_period()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.TimePeriod

    time_period = property(fget=get_time_period)

    def get_schedule_start(self):
        """Gets the start date of this schedule.

        If ``has_time_period()`` is ``true,`` the start date is the
        start date of the associated ``TimePeriod``.

        :return: the start date
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    schedule_start = property(fget=get_schedule_start)

    def get_schedule_end(self):
        """Gets the end date of this schedule.

        If ``has_time_period()`` is ``true,`` the end date is the end
        date of the associated ``TimePeriod``.

        :return: the end date
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    schedule_end = property(fget=get_schedule_end)

    def has_limit(self):
        """Tests if this schedule has a limit on the number of occurrences.

        :return: ``true`` if there is a limit ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_limit(self):
        """Gets the limit of the number of occurences of this schedule.

        :return: the limit
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``has_limitl()`` is ``false``

        """
        return # cardinal

    limit = property(fget=get_limit)

    def get_location_description(self):
        """Gets a descriptive location.

        :return: the location
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    location_description = property(fget=get_location_description)

    def has_location(self):
        """Tests if a location is associated with this event.

        :return: ``true`` if there is an associated location, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_location_id(self):
        """Gets the location ``Id``.

        :return: a location ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``

        """
        return # osid.id.Id

    location_id = property(fget=get_location_id)

    def get_location(self):
        """Gets the ``Location``.

        :return: a location
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Location

    location = property(fget=get_location)

    def get_total_duration(self):
        """Gets a total duration for the entire schedule based on the duration of schedule slots and span of the schedule.

        :return: the total duration
        :rtype: ``osid.calendaring.Duration``

        """
        return # osid.calendaring.Duration

    total_duration = property(fget=get_total_duration)

    def get_schedule_record(self, schedule_record_type):
        """Gets the schedule record corresponding to the given ``Schedule`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``schedule_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(schedule_record_type)`` is ``true`` .

        :param schedule_record_type: the type of the record to retrieve
        :type schedule_record_type: ``osid.type.Type``
        :return: the schedule record
        :rtype: ``osid.calendaring.records.ScheduleRecord``
        :raise: ``NullArgument`` -- ``schedule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_record_type)`` is ``false``

        """
        return # osid.calendaring.records.ScheduleRecord


class ScheduleForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Schedules``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ScheduleAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_limit_metadata(self):
        """Gets the metadata for the weekdays of a weekly schedule.

        :return: metadata for the weekday
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    limit_metadata = property(fget=get_limit_metadata)

    def set_limit(self, weekdays):
        """Sets the weekdays of a weekly schedule.

        :param weekdays: the new weekday set
        :type weekdays: ``cardinal[]``
        :raise: ``InvalidArgument`` -- ``weekdays`` is invalid
        :raise: ``NoAccess`` -- ``weekdays`` cannot be modified
        :raise: ``NullArgument`` -- ``weekdays`` is ``null``

        """
        pass

    def clear_limit(self):
        """Clears the limit.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    limit = property(fset=set_limit, fdel=clear_limit)

    def set_location_description(self, location):
        """Sets the location description.

        :param location: the new location description
        :type location: ``string``
        :raise: ``InvalidArgument`` -- ``location`` is invalid
        :raise: ``NoAccess`` -- ``location`` cannot be modified
        :raise: ``NullArgument`` -- ``location`` is ``null``

        """
        pass

    def clear_location_description(self):
        """Clears the location description.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    location_description = property(fset=set_location_description, fdel=clear_location_description)

    def get_location_metadata(self):
        """Gets the metadata for a location.

        :return: metadata for the location
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    location_metadata = property(fget=get_location_metadata)

    def set_location(self, location_id):
        """Sets the location.

        :param location_id: the new location
        :type location_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``location_id`` is invalid
        :raise: ``NoAccess`` -- ``location_id`` cannot be modified
        :raise: ``NullArgument`` -- ``location_id`` is ``null``

        """
        pass

    def clear_location(self):
        """Clears the location.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    location = property(fset=set_location, fdel=clear_location)

    def get_schedule_slot_form_record(self, schedule_record_type):
        """Gets the ``ScheduleFormRecord`` corresponding to the given schedule record ``Type``.

        :param schedule_record_type: the schedule record type
        :type schedule_record_type: ``osid.type.Type``
        :return: the schedule form record
        :rtype: ``osid.calendaring.records.ScheduleFormRecord``
        :raise: ``NullArgument`` -- ``schedule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_record_type)`` is ``false``

        """
        return # osid.calendaring.records.ScheduleFormRecord


class ScheduleList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ScheduleList`` provides a means for accessing ``Schedule`` elements sequentially either one at a time or many at a time.

    Examples: while (sl.hasNext()) { Schedule schedule =
    sl.getNextSchedule(); }

    or
      while (sl.hasNext()) {
           Schedule[] schedules = sl.getNextSchedules(sl.available());
      }
    


    """
    def get_next_schedule(self):
        """Gets the next ``Schedule`` in this list.

        :return: the next ``Schedule`` in this list. The ``has_next()`` method should be used to test that a next ``Schedule`` is available before calling this method.
        :rtype: ``osid.calendaring.Schedule``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Schedule

    next_schedule = property(fget=get_next_schedule)

    def get_next_schedules(self, n):
        """Gets the next set of ``Schedule`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Schedule`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Schedule`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.Schedule``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Schedule


class ScheduleSlot(osid_objects.OsidObject, osid_markers.Containable):
    """A ``ScheduleSlot`` describes a repeating time slot.

    The time slot can be defined as a fixed time interval or be defined
    on a weekly interval specifying the days of the week.

    """
    def get_schedule_slot_ids(self):
        """Gets the ``Ids`` of the schedule slots included inside this one.

        :return: the schedules slot ``Ids``
        :rtype: ``osid.id.IdList``

        """
        return # osid.id.IdList

    schedule_slot_ids = property(fget=get_schedule_slot_ids)

    def get_schedule_slots(self):
        """Gets the schedule slots included inside this one.

        :return: the schedule slots
        :rtype: ``osid.calendaring.ScheduleSlotList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.ScheduleSlotList

    schedule_slots = property(fget=get_schedule_slots)

    def has_weekly_interval(self):
        """Tests if this schedule has a weekly interval.

        If ``true,`` ``has_fixed_interval()`` must be ``false``.

        :return: ``true`` if there is a weekly interval, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_weekdays(self):
        """Gets the weekdays of the schedule.

        On a Gregorian calendar, Sunday is zero.

        :return: the weekdays
        :rtype: ``cardinal``
        :raise: ``IllegalState`` -- ``has_weekly_interval()`` is ``false``

        """
        return # cardinal

    weekdays = property(fget=get_weekdays)

    def has_week_of_month_interval(self):
        """Tests if this schedule has a weekly interval based on the week of the month.

        This method must be ``false`` if ``has_weekly_interval()`` is
        ``false``.

        :return: ``true`` if there is a week of month specified, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_weekly_interval(self):
        """Gets the number of weeks of the interval.

        1 is every week. 2 is every other week. -1 is every week back in
        time.

        :return: ``the week interval``
        :rtype: ``integer``
        :raise: ``IllegalState`` -- ``has_weekdly_interval()`` is ``false`` or ``has_weekof_month_interval()`` is ``true``

        """
        return # integer

    weekly_interval = property(fget=get_weekly_interval)

    def get_week_of_month(self):
        """Gets the week of the month for the interval.

        1 is the first week of the month. -1 is the last week of the
        month. 0 is invalid.

        :return: ``the week interval``
        :rtype: ``integer``
        :raise: ``IllegalState`` -- ``has_weekly_interval()`` is ``false`` or ``has_weekof_month_interval()`` is ``false``

        """
        return # integer

    week_of_month = property(fget=get_week_of_month)

    def get_weekday_time(self):
        """Gets the time of this recurring schedule.

        :return: the time
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- ``has_weekly_interval()`` is ``false``

        """
        return # osid.calendaring.Time

    weekday_time = property(fget=get_weekday_time)

    def has_fixed_interval(self):
        """Tests if this schedule has a fixed time interval.

        :return: ``true`` if there is a fixed time interval, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_fixed_interval(self):
        """Gets the repeating interval.

        :return: the interval
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- ``has_fixed_interval()`` is ``false``

        """
        return # osid.calendaring.Duration

    fixed_interval = property(fget=get_fixed_interval)

    def get_duration(self):
        """Gets the duration of the schedule slot.

        :return: the duration
        :rtype: ``osid.calendaring.Duration``

        """
        return # osid.calendaring.Duration

    duration = property(fget=get_duration)

    def get_schedule_slot_record(self, schedule_slot_record_type):
        """Gets the schedule slot record corresponding to the given ``ScheduleSlot`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``schedule_slot_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(schedule_slot_record_type)`` is ``true`` .

        :param schedule_slot_record_type: the type of the record to retrieve
        :type schedule_slot_record_type: ``osid.type.Type``
        :return: the schedule slot record
        :rtype: ``osid.calendaring.records.ScheduleSlotRecord``
        :raise: ``NullArgument`` -- ``schedule_slot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_slot_record_type)`` is ``false``

        """
        return # osid.calendaring.records.ScheduleSlotRecord


class ScheduleSlotForm(osid_objects.OsidObjectForm, osid_objects.OsidContainableForm):
    """This is the form for creating and updating ``ScheduleSlots``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ScheduleSlotAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_weekday_metadata(self):
        """Gets the metadata for the weekdays of a weekly schedule.

        :return: metadata for the weekday
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    weekday_metadata = property(fget=get_weekday_metadata)

    def set_weekdays(self, weekdays):
        """Sets the weekdays of a weekly schedule.

        :param weekdays: the new weekday set
        :type weekdays: ``cardinal[]``
        :raise: ``InvalidArgument`` -- ``weekdays`` is invalid
        :raise: ``NoAccess`` -- ``weekdays`` cannot be modified
        :raise: ``NullArgument`` -- ``weekdays`` is ``null``

        """
        pass

    weekdays = property(fset=set_weekdays)

    def get_weekly_interval_metadata(self):
        """Gets the metadata for the interval of a weekly schedule.

        :return: metadata for the weekly interval
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    weekly_interval_metadata = property(fget=get_weekly_interval_metadata)

    def set_weekly_interval(self, interval):
        """Sets the interval of a weekly schedule.

        :param interval: the new weekly interval
        :type interval: ``integer``
        :raise: ``InvalidArgument`` -- ``interval`` is invalid
        :raise: ``NoAccess`` -- ``interval`` cannot be modified

        """
        pass

    weekly_interval = property(fset=set_weekly_interval)

    def get_week_of_month_metadata(self):
        """Gets the metadata for the week of the month of a weekly schedule.

        :return: metadata for the week of the month
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    week_of_month_metadata = property(fget=get_week_of_month_metadata)

    def set_week_of_the_month(self, week):
        """Sets the week of the month of a weekly schedule.

        :param week: the new week of the month
        :type week: ``integer``
        :raise: ``InvalidArgument`` -- ``week`` is invalid
        :raise: ``NoAccess`` -- ``week`` cannot be modified

        """
        pass

    week_of_the_month = property(fset=set_week_of_the_month)

    def get_weekday_time_metadata(self):
        """Gets the metadata for the weekday time of a weekly schedule.

        :return: metadata for the weekday time
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    weekday_time_metadata = property(fget=get_weekday_time_metadata)

    def set_weekday_time(self, time):
        """Sets the weekday time of a weekly schedule.

        :param time: the new time
        :type time: ``osid.calendaring.Time``
        :raise: ``InvalidArgument`` -- ``time`` is invalid
        :raise: ``NoAccess`` -- ``time`` cannot be modified
        :raise: ``NullArgument`` -- ``time`` is ``null``

        """
        pass

    weekday_time = property(fset=set_weekday_time)

    def clear_weekday_schedule(self):
        """Clears the weekday schedule items.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    weekday_schedule = property(fdel=clear_weekday_schedule)

    def get_fixed_interval_metadata(self):
        """Gets the metadata for the fixed interval.

        :return: metadata for the fixed interval.
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    fixed_interval_metadata = property(fget=get_fixed_interval_metadata)

    def set_fixed_interval(self, interval):
        """Sets the fixed interval.

        :param interval: the new fixed interval
        :type interval: ``osid.calendaring.Duration``
        :raise: ``InvalidArgument`` -- ``interval`` is invalid
        :raise: ``NoAccess`` -- ``interval`` cannot be modified
        :raise: ``NullArgument`` -- ``interval`` is ``null``

        """
        pass

    def clear_fixed_interval(self):
        """Clears the fixed interval items.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    fixed_interval = property(fset=set_fixed_interval, fdel=clear_fixed_interval)

    def ge_duration_metadata(self):
        """Gets the metadata for the duration of the slot.

        :return: metadata for the duration
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    def set_duration(self, duration):
        """Sets the duration.

        :param duration: the new duration
        :type duration: ``osid.calendaring.Duration``
        :raise: ``InvalidArgument`` -- ``duration`` is invalid
        :raise: ``NoAccess`` -- ``duration`` cannot be modified
        :raise: ``NullArgument`` -- ``duration`` is ``null``

        """
        pass

    def clear_duration(self):
        """Clears the duration terms.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    duration = property(fset=set_duration, fdel=clear_duration)

    def get_schedule_slot_form_record(self, schedule_slot_record_type):
        """Gets the ``ScheduleSlotFormRecord`` corresponding to the given schedule record ``Type``.

        :param schedule_slot_record_type: the schedule slot record type
        :type schedule_slot_record_type: ``osid.type.Type``
        :return: the schedule slot form record
        :rtype: ``osid.calendaring.records.ScheduleSlotFormRecord``
        :raise: ``NullArgument`` -- ``schedule_slot_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(schedule_slot_record_type)`` is ``false``

        """
        return # osid.calendaring.records.ScheduleSlotFormRecord


class ScheduleSlotList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ScheduleSlotList`` provides a means for accessing ``ScheduleSlot`` elements sequentially either one at a time or many at a time.

    Examples: while (ssl.hasNext()) { ScheduleSlot slot =
    ssl.getNextSchedulSlote(); }

    or
      while (ssl.hasNext()) {
           ScheduleSlot[] slots = ssl.getNextScheduleSlots(ssl.available());
      }
    


    """
    def get_next_schedule_slot(self):
        """Gets the next ``ScheduleSlot`` in this list.

        :return: the next ``ScheduleSlot`` in this list. The ``has_next()`` method should be used to test that a next ``ScheduleSlot`` is available before calling this method.
        :rtype: ``osid.calendaring.ScheduleSlot``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.ScheduleSlot

    next_schedule_slot = property(fget=get_next_schedule_slot)

    def get_next_schedule_slots(self, n):
        """Gets the next set of ``ScheduleSlot`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``ScheduleSlot`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ScheduleSlot`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.ScheduleSlot``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.ScheduleSlot


class TimePeriod(osid_objects.OsidObject):
    """A ``TimePeriod`` represents a span of time in which recurring events are expanded."""
    def get_start(self):
        """Gets the start time of the time period.

        :return: the start time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    start = property(fget=get_start)

    def get_end(self):
        """Gets the end time of the time period.

        :return: the end time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    end = property(fget=get_end)

    def get_exception_ids(self):
        """Gets the exception ``Ids`` to this time period.

        Recurring events overlapping with these events do not appear in
        any recurring event for this time period.

        :return: list of exception event ``Ids``
        :rtype: ``osid.id.IdList``

        """
        return # osid.id.IdList

    exception_ids = property(fget=get_exception_ids)

    def get_exceptions(self):
        """Gets the exceptions to this time period.

        Recurring events overlapping with these events do not appear in
        any recurring event for this time period.

        :return: event exceptions
        :rtype: ``osid.calendaring.EventList``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.EventList

    exceptions = property(fget=get_exceptions)

    def get_time_period_record(self, time_period_record_type):
        """Gets the time period record corresponding to the given ``TimePeriod`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``time_period_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(time_period_record_type)`` is ``true`` .

        :param time_period_record_type: the type of the record to retrieve
        :type time_period_record_type: ``osid.type.Type``
        :return: the time period record
        :rtype: ``osid.calendaring.records.TimePeriodRecord``
        :raise: ``NullArgument`` -- ``time_period_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(time_period_record_type)`` is ``false``

        """
        return # osid.calendaring.records.TimePeriodRecord


class TimePeriodForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``TimePeriods``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``TimePeriodAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_start_metadata(self):
        """Gets the metadata for a start time.

        :return: metadata for the start time
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    start_metadata = property(fget=get_start_metadata)

    def set_start(self, start):
        """Sets the start time.

        :param start: the new start time
        :type start: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``start`` is invalid
        :raise: ``NoAccess`` -- ``start`` cannot be modified
        :raise: ``NullArgument`` -- ``start`` is ``null``

        """
        pass

    def clear_start(self):
        """Clears the start time.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    start = property(fset=set_start, fdel=clear_start)

    def get_end_metadata(self):
        """Gets the metadata for an end time.

        :return: metadata for the end time
        :rtype: ``osid.Metadata``

        """
        return # osid.Metadata

    end_metadata = property(fget=get_end_metadata)

    def set_end(self, end):
        """Sets the end time.

        :param end: the new end time
        :type end: ``osid.calendaring.DateTime``
        :raise: ``InvalidArgument`` -- ``end`` is invalid
        :raise: ``NoAccess`` -- ``end`` cannot be modified
        :raise: ``NullArgument`` -- ``end`` is ``null``

        """
        pass

    def clear_end(self):
        """Clears the time period end.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        """
        pass

    end = property(fset=set_end, fdel=clear_end)

    def get_time_period_form_record(self, time_period_record_type):
        """Gets the ``TimePeriodFormRecord`` corresponding to the given time period record ``Type``.

        :param time_period_record_type: the time period record type
        :type time_period_record_type: ``osid.type.Type``
        :return: the time period form record
        :rtype: ``osid.calendaring.records.TimePeriodFormRecord``
        :raise: ``NullArgument`` -- ``time_period_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(time_period_record_type)`` is ``false``

        """
        return # osid.calendaring.records.TimePeriodFormRecord


class TimePeriodList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``TimePeriodList`` provides a means for accessing ``TimePeriod`` elements sequentially either one at a time or many at a time.

    Examples: while (tp.hasNext()) { TimePeriod period =
    tp.getNextTimePeriod(); }

    or
      while (tp.hasNext()) {
           TimePeriod[] periods = tp.getNextTimePeriods(tp.available());
      }
    


    """
    def get_next_time_period(self):
        """Gets the next ``TimePeriod`` in this list.

        :return: the next ``TimePeriod`` in this list. The ``has_next()`` method should be used to test that a next ``TimePeriod`` is available before calling this method.
        :rtype: ``osid.calendaring.TimePeriod``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.TimePeriod

    next_time_period = property(fget=get_next_time_period)

    def get_next_time_periods(self, n):
        """Gets the next set of ``TimePeriod`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``TimePeriod`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``TimePeriod`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.TimePeriod``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.TimePeriod


class Commitment(osid_objects.OsidRelationship):
    """A ``Commitment`` maps a ``Resource`` to an ``Event``."""
    def get_event_id(self):
        """Gets the event ``Id``.

        :return: the event ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    event_id = property(fget=get_event_id)

    def get_event(self):
        """Gets the ``Event``.

        :return: the event
        :rtype: ``osid.calendaring.Event``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Event

    event = property(fget=get_event)

    def get_resource_id(self):
        """Gets the resource ``Id``.

        :return: a resource ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the ``Resource``.

        :return: the resource
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    resource = property(fget=get_resource)

    def get_commitment_record(self, commitment_record_type):
        """Gets the record corresponding to the given ``Commitment`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``commitment_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(commitment_record_type)`` is ``true`` .

        :param commitment_record_type: the type of the record to retrieve
        :type commitment_record_type: ``osid.type.Type``
        :return: the commitment record
        :rtype: ``osid.calendaring.records.CommitmentRecord``
        :raise: ``NullArgument`` -- ``commitment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(commitment_record_type)`` is ``false``

        """
        return # osid.calendaring.records.CommitmentRecord


class CommitmentForm(osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Commitments``."""
    def get_commitment_form_record(self, commitment_record_type):
        """Gets the ``CommitmentFormRecord`` corresponding to the given event record ``Type``.

        :param commitment_record_type: the commitment record type
        :type commitment_record_type: ``osid.type.Type``
        :return: the commitment form record
        :rtype: ``osid.calendaring.records.CommitmentFormRecord``
        :raise: ``NullArgument`` -- ``commitment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(commitment_record_type)`` is ``false``

        """
        return # osid.calendaring.records.CommitmentFormRecord


class CommitmentList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CommitmentList`` provides a means for accessing ``Commitment`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Commitment commitment =
    cl.getNextCommitment(); }

    or
      while (cl.hasNext()) {
           Commitment[] commitments = cl.getNextCommitment(cl.available());
      }
    


    """
    def get_next_commitment(self):
        """Gets the next ``Commitment`` in this list.

        :return: the next ``Commitment`` in this list. The ``has_next()`` method should be used to test that a next ``Commitment`` is available before calling this method.
        :rtype: ``osid.calendaring.Commitment``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Commitment

    next_commitment = property(fget=get_next_commitment)

    def get_next_commitments(self, n):
        """Gets the next set of ``Commitment`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Commitment`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Commitment`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.Commitment``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Commitment


class Calendar(osid_objects.OsidCatalog):
    """A calendar defines a collection of events."""
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
        return # osid.calendaring.records.CalendarRecord


class CalendarForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating calendars.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CalendarAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_calendar_form_record(self, calendar_record_type):
        """Gets the ``CalendarFormRecord`` corresponding to the given calendar record ``Type``.

        :param calendar_record_type: a calendar record type
        :type calendar_record_type: ``osid.type.Type``
        :return: the calendar form record
        :rtype: ``osid.calendaring.records.CalendarFormRecord``
        :raise: ``NullArgument`` -- ``calendar_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(calendar_record_type)`` is ``false``

        """
        return # osid.calendaring.records.CalendarFormRecord


class CalendarList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CalendarList`` provides a means for accessing ``Calendar`` elements sequentially either one at a time or many at a time.

    Examples: while (cl.hasNext()) { Calendar calendar =
    cl.getNextCalendar(); }

    or
      while (cl.hasNext()) {
           Calendar[] calendars = cl.getNextCalendars(cl.available());
      }
    


    """
    def get_next_calendar(self):
        """Gets the next ``Calendar`` in this list.

        :return: the next ``Calendar`` in this list. The ``has_next()`` method should be used to test that a next ``Calendar`` is available before calling this method.
        :rtype: ``osid.calendaring.Calendar``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Calendar

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
        return # osid.calendaring.Calendar


class CalendarNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``CalendarHierarchySession``.

    """
    def get_calendar(self):
        """Gets the ``Calendar`` at this node.

        :return: the calendar represented by this node
        :rtype: ``osid.calendaring.Calendar``

        """
        return # osid.calendaring.Calendar

    calendar = property(fget=get_calendar)

    def get_parent_calendar_nodes(self):
        """Gets the parents of this calendar.

        :return: the parents of the ``id``
        :rtype: ``osid.calendaring.CalendarNodeList``

        """
        return # osid.calendaring.CalendarNodeList

    parent_calendar_nodes = property(fget=get_parent_calendar_nodes)

    def get_child_calendar_nodes(self):
        """Gets the children of this calendar.

        :return: the children of this calendar
        :rtype: ``osid.calendaring.CalendarNodeList``

        """
        return # osid.calendaring.CalendarNodeList

    child_calendar_nodes = property(fget=get_child_calendar_nodes)


class CalendarNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``CalendarNodeList`` provides a means for accessing ``CalendarNode`` elements sequentially either one at a time or many at a time.

    Examples: while (cnl.hasNext()) { CalendarNode node =
    cnl.getNextCalendarNode(); }

    or
      while (cnl.hasNext()) {
           CalendarNode[] nodes = cnl.getNextCalendarNodes(cnl.available());
      }
    


    """
    def get_next_calendar_node(self):
        """Gets the next ``CalendarNode`` in this list.

        :return: the next ``CalendarNode`` in this list. The ``has_next()`` method should be used to test that a next ``CalendarNode`` is available before calling this method.
        :rtype: ``osid.calendaring.CalendarNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.CalendarNode

    next_calendar_node = property(fget=get_next_calendar_node)

    def get_next_calendar_nodes(self, n):
        """Gets the next set of ``CalendarNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``CalendarNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``CalendarNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.CalendarNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.CalendarNode


class MeetingTime(osid_objects.OsidCapsule):
    """An individual meeting time."""
    def get_date(self):
        """Gets the date.

        :return: the date
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    date = property(fget=get_date)

    def get_location_description(self):
        """Gets a descriptive text for the location.

        :return: a location description
        :rtype: ``osid.locale.DisplayText``

        """
        return # osid.locale.DisplayText

    location_description = property(fget=get_location_description)

    def has_location(self):
        """Tests if a location is available.

        :return: ``true`` if a location is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_location_id(self):
        """Gets the location ``Id``.

        :return: a location ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``

        """
        return # osid.id.Id

    location_id = property(fget=get_location_id)

    def get_location(self):
        """Gets the ``Location``.

        :return: a location
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Location

    location = property(fget=get_location)


class MeetingTimeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``MeetingTimeList`` provides a means for accessing ``MeetingTime`` elements sequentially either one at a time or many at a time.

    Examples: while (mtl.hasNext()) { MeetingTime time =
    mtl.getNextMeetingTime(); }

    or
      while (mtl.hasNext()) {
           MeetingTime[] times = mtl.getNextMeetingTimes(mtl.available());
      }
    


    """
    def get_next_meeting_time(self):
        """Gets the next ``MeetingTime`` in this list.

        :return: the next ``MeetingTime`` in this list. The ``has_next()`` method should be used to test that a next ``MeetingTime`` is available before calling this method.
        :rtype: ``osid.calendaring.MeetingTime``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.MeetingTime

    next_meeting_time = property(fget=get_next_meeting_time)

    def get_next_meeting_times(self, n):
        """Gets the next set of ``MeetingTime`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``MeetingTime`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``MeetingTime`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.MeetingTime``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.MeetingTime


class TimeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``TimeList`` provides a means for accessing ``Time`` elements sequentially either one at a time or many at a time.

    Examples: while (tl.hasNext()) { Time time = tl.getNextTime(); }

    or
      while (tl.hasNext()) {
           Time[] times = tl.getNextTimes(tl.available());
      }
    


    """
    def get_next_time(self):
        """Gets the next ``Time`` in this list.

        :return: the next ``Time`` in this list. The ``has_next()`` method should be used to test that a next ``Time`` is available before calling this method.
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Time

    next_time = property(fget=get_next_time)

    def get_next_times(self, n):
        """Gets the next set of ``Time`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Time`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Time`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.Time``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Time


class DateTimeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``DateTimeList`` provides a means for accessing ``DateTime`` elements sequentially either one at a time or many at a time.

    Examples: while (dtl.hasNext()) { DateTime time =
    dtl.getNextDateTime(); }

    or
      while dtl.hasNext()) {
           DateTime[] times = dtl.getNextDateTimes(dtl.available());
      }
    


    """
    def get_next_date_time(self):
        """Gets the next ``DateTime`` in this list.

        :return: the next ``DateTime`` in this list. The ``has_next()`` method should be used to test that a next ``DateTime`` is available before calling this method.
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.DateTime

    next_date_time = property(fget=get_next_date_time)

    def get_next_date_times(self, n):
        """Gets the next set of ``DateTime`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``DateTime`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``DateTime`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.DateTime``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.DateTime


class DurationList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``DurationList`` provides a means for accessing ``Duration`` elements sequentially either one at a time or many at a time.

    Examples: while (dl.hasNext()) { Duration duration =
    dl.getNextDuration(); }

    or
      while dl.hasNext()) {
           Duration[] durations = dl.getNextDurations(dl.available());
      }
    


    """
    def get_next_duration(self):
        """Gets the next ``Duration`` in this list.

        :return: the next ``Duration`` in this list. The ``has_next()`` method should be used to test that a next ``Duration`` is available before calling this method.
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Duration

    next_duration = property(fget=get_next_duration)

    def get_next_durations(self, n):
        """Gets the next set of ``Duration`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Duration`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Duration`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.Duration``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.Duration


class DateTimeInterval:
    """The ``DateTimeInterval`` interface defines an interval between two date times."""
    def get_start(self):
        """Gets the starting time for this interval.

        :return: the starting time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    start = property(fget=get_start)

    def get_end(self):
        """Gets the ending time for this interval.

        The ending time is greater than or equal to the starting time.

        :return: the ending time
        :rtype: ``osid.calendaring.DateTime``

        """
        return # osid.calendaring.DateTime

    end = property(fget=get_end)


class DateTimeIntervalList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``DateTimeIntervalList`` provides a means for accessing ``DateTimeInterval`` elements sequentially either one at a time or many at a time.

    Examples: while (dtil.hasNext()) { DateTimeInterval interval =
    dtil.getNextDateTimeInterval(); }

    or
      while (dtil.hasNext()) {
           DateTimeInterval[] intervals = dtil.getNextDateTimeIntervals(dtil.available());
      }
    


    """
    def get_next_date_time_interval(self):
        """Gets the next ``DateTimeInterval`` in this list.

        :return: the next ``DateTimeInterval`` in this list. The ``has_next()`` method should be used to test that a next ``DateTimeInterval`` is available before calling this method.
        :rtype: ``osid.calendaring.DateTimeInterval``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.DateTimeInterval

    next_date_time_interval = property(fget=get_next_date_time_interval)

    def get_next_date_time_intervals(self, n):
        """Gets the next set of ``DateTimeInterval`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``DateTimeInterval`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``DateimeInterval`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.calendaring.DateTimeInterval``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.calendaring.DateTimeInterval


