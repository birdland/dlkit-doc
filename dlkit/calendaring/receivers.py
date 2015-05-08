from ..osid import receivers as osid_receivers


class EventReceiver(osid_receivers.OsidReceiver):
    """The event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Events``."""
    def new_events(self, notification_id, event_ids):
        """The callback for notifications of new events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param event_ids: the ``Ids`` of the new ``Events``
        :type event_ids: ``osid.id.IdList``

        """
        pass

    def changed_events(self, notification_id, event_ids):
        """The callback for notification of updated events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param event_ids: the ``Ids`` of the updated ``Events``
        :type event_ids: ``osid.id.IdList``

        """
        pass

    def deleted_events(self, notification_id, event_ids):
        """The callback for notification of deleted events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param event_ids: the ``Ids`` of the deleted ``Events``
        :type event_ids: ``osid.id.IdList``

        """
        pass


class RecurringEventReceiver(osid_receivers.OsidReceiver):
    """The recurring event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``RecurringEvents``."""
    def new_recurring_events(self, notification_id, recurring_event_ids):
        """The callback for notifications of new recurring events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param recurring_event_ids: the ``Ids`` of the new ``RecurringEvents``
        :type recurring_event_ids: ``osid.id.IdList``

        """
        pass

    def changed_recurring_events(self, notification_id, recurring_event_ids):
        """The callback for notification of updated recurring events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param recurring_event_ids: the ``Ids`` of the updated ``RecurringEvents``
        :type recurring_event_ids: ``osid.id.IdList``

        """
        pass

    def deleted_recurring_events(self, notification_id, recurring_event_ids):
        """The callback for notification of deleted recurring events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param recurring_event_ids: the ``Ids`` of the deleted ``RecurringEvents``
        :type recurring_event_ids: ``osid.id.IdList``

        """
        pass


class SupersedingEventReceiver(osid_receivers.OsidReceiver):
    """The superseding event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``SupersedingEvents``."""
    def new_superseding_events(self, notification_id, superseding_event_ids):
        """The callback for notifications of new superseding events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param superseding_event_ids: the ``Ids`` of the new ``SupersedingEvents``
        :type superseding_event_ids: ``osid.id.IdList``

        """
        pass

    def changed_superseding_events(self, notification_id, superseding_event_ids):
        """The callback for notification of updated superseding events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param superseding_event_ids: the ``Ids`` of the updated ``SupersedingEvents``
        :type superseding_event_ids: ``osid.id.IdList``

        """
        pass

    def deleted_superseding_events(self, notification_id, superseding_event_ids):
        """The callback for notification of deleted superseding events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param superseding_event_ids: the ``Ids`` of the deleted ``SupersedingEvents``
        :type superseding_event_ids: ``osid.id.IdList``

        """
        pass


class OffsetEventReceiver(osid_receivers.OsidReceiver):
    """The event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``OffsetEvents``."""
    def new_offset_events(self, notification_id, offset_event_ids):
        """The callback for notifications of new offset events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param offset_event_ids: the ``Ids`` of the new ``OffsetEvents``
        :type offset_event_ids: ``osid.id.IdList``

        """
        pass

    def changed_offset_events(self, notification_id, offset_event_ids):
        """The callback for notification of updated offset events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param offset_event_ids: the ``Ids`` of the updated ``OffsetEvents``
        :type offset_event_ids: ``osid.id.IdList``

        """
        pass

    def deleted_offset_events(self, notification_id, offset_event_ids):
        """The callback for notification of deleted offset events.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param offset_event_ids: the ``Ids`` of the deleted ``OffsetEvents``
        :type offset_event_ids: ``osid.id.IdList``

        """
        pass


class ScheduleReceiver(osid_receivers.OsidReceiver):
    """The schedule receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Schedules``."""
    def new_schedules(self, notification_id, schedule_ids):
        """The callback for notifications of new schedules.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param schedule_ids: the ``Ids`` of the new ``Schedules``
        :type schedule_ids: ``osid.id.IdList``

        """
        pass

    def changed_schedules(self, notification_id, schedule_ids):
        """The callback for notification of updated schedules.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param schedule_ids: the ``Ids`` of the updated ``Schedules``
        :type schedule_ids: ``osid.id.IdList``

        """
        pass

    def deleted_schedules(self, notification_id, schedule_ids):
        """The callback for notification of deleted schedules.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param schedule_ids: the ``Ids`` of the deleted ``Schedules``
        :type schedule_ids: ``osid.id.IdList``

        """
        pass


class ScheduleSlotReceiver(osid_receivers.OsidReceiver):
    """The schedule slot receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``ScheduleSlots``."""
    def new_schedule_slots(self, notification_id, schedule_slot_ids):
        """The callback for notifications of new schedule slots.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param schedule_slot_ids: the ``Ids`` of the new ``ScheduleSlots``
        :type schedule_slot_ids: ``osid.id.IdList``

        """
        pass

    def changed_schedule_slots(self, notification_id, schedule_slot_ids):
        """The callback for notification of updated schedule slots.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param schedule_slot_ids: the ``Ids`` of the updated ``ScheduleSlots``
        :type schedule_slot_ids: ``osid.id.IdList``

        """
        pass

    def deleted_schedule_slots(self, notification_id, schedule_slot_ids):
        """The callback for notification of deleted schedule slots.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param schedule_slot_ids: the ``Ids`` of the deleted ``ScheduleSlots``
        :type schedule_slot_ids: ``osid.id.IdList``

        """
        pass


class TimePeriodReceiver(osid_receivers.OsidReceiver):
    """The time period receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``TimePeriods``."""
    def new_time_periods(self, notification_id, time_period_ids):
        """The callback for notifications of new time periods.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param time_period_ids: the ``Id`` of the new ``TimePeriods``
        :type time_period_ids: ``osid.id.IdList``

        """
        pass

    def changed_time_periods(self, notification_id, time_period_ids):
        """The callback for notification of updated time periods.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param time_period_ids: the ``Id`` of the updated ``TimePeriods``
        :type time_period_ids: ``osid.id.IdList``

        """
        pass

    def deleted_time_periods(self, notification_id, time_period_ids):
        """The callback for notification of deleted time periods.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param time_period_ids: the ``Id`` of the deleted ``TimePeriods``
        :type time_period_ids: ``osid.id.IdList``

        """
        pass


class CommitmentReceiver(osid_receivers.OsidReceiver):
    """The event receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Commitments``."""
    def new_commitmentss(self, notification_id, commitment_ids):
        """The callback for notifications of new commitments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param commitment_ids: the ``Id`` of the new ``Commitments``
        :type commitment_ids: ``osid.id.IdList``

        """
        pass

    def changed_commitments(self, notification_id, commitment_ids):
        """The callback for notification of updated commitments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param commitment_ids: the ``Id`` of the updated ``Commitments``
        :type commitment_ids: ``osid.id.IdList``

        """
        pass

    def deleted_commitments(self, notification_id, commitment_ids):
        """The callback for notification of deleted commitments.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param commitment_ids: the ``Id`` of the deleted ``Commitments``
        :type commitment_ids: ``osid.id.IdList``

        """
        pass


class CalendarReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Calendar`` objects."""
    def new_calendars(self, notification_id, calendar_ids):
        """The callback for notifications of new calendars.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param calendar_ids: the ``Ids`` of the new ``Calendars``
        :type calendar_ids: ``osid.id.IdList``

        """
        pass

    def changed_calendars(self, notification_id, calendar_ids):
        """The callback for notification of updated calendars.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param calendar_ids: the ``Ids`` of the updated ``Calendars``
        :type calendar_ids: ``osid.id.IdList``

        """
        pass

    def deleted_calendars(self, notification_id, calendar_ids):
        """The callback for notification of deleted calendars.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param calendar_ids: the ``Ids`` of the deleted ``Calendars``
        :type calendar_ids: ``osid.id.IdList``

        """
        pass

    def changed_child_of_calendars(self, notification_id, calendar_ids):
        """The callback for notifications of changes to children of calendar hierarchy nodes.

        :param notification_id: the notification ``Id``
        :type notification_id: ``osid.id.Id``
        :param calendar_ids: the ``Ids`` of the ``Calendars`` whose children have changed
        :type calendar_ids: ``osid.id.IdList``

        """
        pass


