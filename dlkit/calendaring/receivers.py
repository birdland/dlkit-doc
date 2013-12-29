from ..osid import receivers as osid_receivers


class EventReceiver(osid_receivers.OsidReceiver):
    """The event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Events``."""
    def new_event(self, event_id):
        """The callback for notifications of new events.

        :param event_id: the ``Id`` of the new ``Event``
        :type event_id: ``osid.id.Id``

        """
        pass

    def changed_event(self, event_id):
        """The callback for notification of updated events.

        :param event_id: the ``Id`` of the updated ``Event``
        :type event_id: ``osid.id.Id``

        """
        pass

    def deleted_event(self, event_id):
        """The callback for notification of deleted events.

        :param event_id: the ``Id`` of the deleted ``Event``
        :type event_id: ``osid.id.Id``

        """
        pass


class RecurringEventReceiver(osid_receivers.OsidReceiver):
    """The recurring event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``RecurringEvents``."""
    def new_recurring_event(self, recurring_event_id):
        """The callback for notifications of new recurring events.

        :param recurring_event_id: the ``Id`` of the new ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``

        """
        pass

    def changed_recurring_event(self, recurring_event_id):
        """The callback for notification of updated recurring events.

        :param recurring_event_id: the ``Id`` of the updated ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``

        """
        pass

    def deleted_recurring_event(self, recurring_event_id):
        """The callback for notification of deleted recurring events.

        :param recurring_event_id: the ``Id`` of the deleted ``RecurringEvent``
        :type recurring_event_id: ``osid.id.Id``

        """
        pass


class SupersedingEventReceiver(osid_receivers.OsidReceiver):
    """The superseding event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``SupersedingEvents``."""
    def new_superseding_event(self, superseding_event_id):
        """The callback for notifications of new superseding events.

        :param superseding_event_id: the ``Id`` of the new ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``

        """
        pass

    def changed_superseding_event(self, superseding_event_id):
        """The callback for notification of updated superseding events.

        :param superseding_event_id: the ``Id`` of the updated ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``

        """
        pass

    def deleted_superseding_event(self, superseding_event_id):
        """The callback for notification of deleted superseding events.

        :param superseding_event_id: the ``Id`` of the deleted ``SupersedingEvent``
        :type superseding_event_id: ``osid.id.Id``

        """
        pass


class OffsetEventReceiver(osid_receivers.OsidReceiver):
    """The event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``OffsetEvents``."""
    def new_offset_event(self, offset_event_id):
        """The callback for notifications of new offset events.

        :param offset_event_id: the ``Id`` of the new ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``

        """
        pass

    def changed_offset_event(self, offset_event_id):
        """The callback for notification of updated offset events.

        :param offset_event_id: the ``Id`` of the updated ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``

        """
        pass

    def deleted_offset_event(self, offset_event_id):
        """The callback for notification of deleted offset events.

        :param offset_event_id: the ``Id`` of the deleted ``OffsetEvent``
        :type offset_event_id: ``osid.id.Id``

        """
        pass


class ScheduleReceiver(osid_receivers.OsidReceiver):
    """The schedule receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Schedules``."""
    def new_schedule(self, schedule_id):
        """The callback for notifications of new schedules.

        :param schedule_id: the ``Id`` of the new ``Schedule``
        :type schedule_id: ``osid.id.Id``

        """
        pass

    def changed_schedule(self, schedule_id):
        """The callback for notification of updated schedules.

        :param schedule_id: the ``Id`` of the updated ``Schedule``
        :type schedule_id: ``osid.id.Id``

        """
        pass

    def deleted_schedule(self, schedule_id):
        """The callback for notification of deleted schedules.

        :param schedule_id: the ``Id`` of the deleted ``Schedule``
        :type schedule_id: ``osid.id.Id``

        """
        pass


class ScheduleSlotReceiver(osid_receivers.OsidReceiver):
    """The schedule slot receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``ScheduleSlots``."""
    def new_schedule_slot(self, schedule_slot_id):
        """The callback for notifications of new schedule slots.

        :param schedule_slot_id: the ``Id`` of the new ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``

        """
        pass

    def new_schedule_slot_ancestor(self, schedule_slot_id, ancestor_id):
        """The callback for notifications of new schedule slot ancestors.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ``ScheduleSlot`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_schedule_slot_descendant(self, schedule_slot_id, descendant_id):
        """The callback for notifications of new schedule slot descendants.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``ScheduleSlot`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_schedule_slot(self, schedule_slot_id):
        """The callback for notification of updated schedule slots.

        :param schedule_slot_id: the ``Id`` of the updated ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``

        """
        pass

    def deleted_schedule_slot(self, schedule_slot_id):
        """The callback for notification of deleted schedule slots.

        :param schedule_slot_id: the ``Id`` of the deleted ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``

        """
        pass

    def deleted_schedule_slot_descendant(self, schedule_slot_id, ancestor_id):
        """The callback for notifications of deleted schedule slot descendants.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``ScheduleSlot`` descendant
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_schedule_slot_ancestor(self, schedule_slot_id, descendant_id):
        """The callback for notifications of deleted schedule slot ancestors.

        :param schedule_slot_id: the ``Id`` of the ``ScheduleSlot``
        :type schedule_slot_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``ScheduleSlot`` ancestor
        :type descendant_id: ``osid.id.Id``

        """
        pass


class TimePeriodReceiver(osid_receivers.OsidReceiver):
    """The time period receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``TimePeriods``."""
    def new_time_period(self, time_period_id):
        """The callback for notifications of new time periods.

        :param time_period_id: the ``Id`` of the new ``TimePeriod``
        :type time_period_id: ``osid.id.Id``

        """
        pass

    def changed_time_period(self, time_period_id):
        """The callback for notification of updated time periods.

        :param time_period_id: the ``Id`` of the updated ``TimePeriod``
        :type time_period_id: ``osid.id.Id``

        """
        pass

    def deleted_time_period(self, time_period_id):
        """The callback for notification of deleted time periods.

        :param time_period_id: the ``Id`` of the deleted ``TimePeriod``
        :type time_period_id: ``osid.id.Id``

        """
        pass


class CommitmentReceiver(osid_receivers.OsidReceiver):
    """The event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Commitments``."""
    def new_commitment(self, commitment_id):
        """The callback for notifications of new commitments.

        :param commitment_id: the ``Id`` of the new ``Commitment``
        :type commitment_id: ``osid.id.Id``

        """
        pass

    def new_commitment_for_event(self, commitment_id, event_id):
        """The callback for notifications of new commitments.

        :param commitment_id: the ``Id`` of the new ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param event_id: the ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``

        """
        pass

    def new_commitment_for_resource(self, commitment_id, resource_id):
        """The callback for notifications of new commitments.

        :param commitment_id: the ``Id`` of the new ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass

    def changed_commitment(self, commitment_id):
        """The callback for notification of updated commitments.

        :param commitment_id: the ``Id`` of the updated ``Commitment``
        :type commitment_id: ``osid.id.Id``

        """
        pass

    def changed_commitment_for_event(self, commitment_id, event_id):
        """The callback for notifications of updated commitments.

        :param commitment_id: the ``Id`` of the updated ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param event_id: the ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``

        """
        pass

    def changed_commitment_for_resource(self, commitment_id, resource_id):
        """The callback for notifications of updated commitments.

        :param commitment_id: the ``Id`` of the updated ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass

    def changed_commitment_state(self, commitment_id, process_id):
        """The callback for notification of changed commitment states.

        :param commitment_id: the ``Id`` of the ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param process_id: the ``Id`` of the ``process``
        :type process_id: ``osid.id.Id``

        """
        pass

    def deleted_commitment(self, commitment_id):
        """The callback for notification of deleted commitments.

        :param commitment_id: the ``Id`` of the deleted ``Commitment``
        :type commitment_id: ``osid.id.Id``

        """
        pass

    def deleted_commitment_for_event(self, commitment_id, event_id):
        """The callback for notifications of deleted commitments.

        :param commitment_id: the ``Id`` of the deleted ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param event_id: the ``Id`` of the ``Event``
        :type event_id: ``osid.id.Id``

        """
        pass

    def deleted_commitment_for_resource(self, commitment_id, resource_id):
        """The callback for notifications of deleted commitments.

        :param commitment_id: the ``Id`` of the deleted ``Commitment``
        :type commitment_id: ``osid.id.Id``
        :param resource_id: the ``Id`` of the ``Resource``
        :type resource_id: ``osid.id.Id``

        """
        pass


class CalendarReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Calendar`` objects."""
    def new_calendar(self, calendar_id):
        """The callback for notifications of new calendars.

        :param calendar_id: the ``Id`` of the new ``Calendar``
        :type calendar_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_calendar(self, calendar_id, ancestor_id):
        """The callback for notifications of new calendar ancestors.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(calendar_record_type) is false``
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_calendar(self, calendar_id, descendant_id):
        """The callback for notifications of new calendar descendants.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Calendar`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_calendar(self, calendar_id):
        """The callback for notification of updated calendars.

        :param calendar_id: the ``Id`` of the updated ``Calendar``
        :type calendar_id: ``osid.id.Id``

        """
        pass

    def deleted_calendar(self, calendar_id):
        """The callback for notification of deleted calendars.

        :param calendar_id: the ``Id`` of the deleted ``Calendar``
        :type calendar_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_calendar(self, calendar_id, ancestor_id):
        """The callback for notifications of deleted calendar ancestors.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Calendar`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_calendar(self, calendar_id, descendant_id):
        """The callback for notifications of deleted calendar descendants.

        :param calendar_id: the ``Id`` of the ``Calendar``
        :type calendar_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Calendar`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


