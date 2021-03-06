
from ..osid import markers as osid_markers


class OsidSearchOrder(osid_markers.Suppliable):
    """``OsidSearchOrder`` specifies preferred ordering of search results.

    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch`` interface. OsidSearch os =
    session.getObjectSearch(); os.limitResultSet(1, 25); OsidSearchOrder
    order = session.getObjectSearchOrder(); order.orderByDisplayName();
    os.orderResults(order); OsidQuery queru; query =
    session.getObjectQuery(); query.addDescriptionMatch("*food*",
    wildcardStringMatchType, true); ObjectSearchResults results =
    session.getObjectsBySearch(query, os); ObjectList list =
    results.getObjectList();

    """




class OsidIdentifiableSearchOrder(OsidSearchOrder):
    """``OsidIdentifiableSearchOrder`` specifies preferred ordering of search results.

    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch``.

    """

    def order_by_id(self, style):
        """Specifies a preference for ordering the result set by the ``Id``.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidExtensibleSearchOrder(OsidSearchOrder, osid_markers.Extensible):
    """``OsidExtensibleSearchOrder`` specifies preferred ordering of search results.

    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch``.

    """




class OsidBrowsableSearchOrder(OsidSearchOrder):
    """``OsidBrowsableSearchOrder`` specifies preferred ordering of search results.

    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch``.

    """




class OsidTemporalSearchOrder(OsidSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_effective(self, style):
        """Specifies a preference for ordering the result set by the effective status.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_start_date(self, style):
        """Specifies a preference for ordering the result set by the start date.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_end_date(self, style):
        """Specifies a preference for ordering the result set by the end date.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidSubjugateableSearchOrder(OsidSearchOrder):
    """An interface for specifying the ordering of dependent object search results."""




class OsidAggregateableSearchOrder(OsidSearchOrder):
    """An interface for specifying the ordering of assemblage search results."""




class OsidContainableSearchOrder(OsidSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_sequestered(self, style):
        """Specifies a preference for ordering the result set by the sequestered flag.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidSourceableSearchOrder(OsidSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_provider(self, style):
        """Specifies a preference for ordering the results by provider.

        The element of the provider to order is not specified but may be
        managed through the provider ordering interface.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_provider_search_order(self):
        """Tests if a ``ProviderSearchOrder`` interface is available.

        :return: ``true`` if a provider search order interface is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_provider_search_order(self):
        """Gets the search order interface for a provider.

        :return: the provider search order interface
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_provider_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_provider_search_order()`` is ``true``.*

        """
        return # osid.resource.ResourceSearchOrder

    provider_search_order = property(fget=get_provider_search_order)


class OsidFederateableSearchOrder(OsidSearchOrder):
    """An interface for specifying the ordering of search results."""




class OsidOperableSearchOrder(OsidSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_active(self, style):
        """Specifies a preference for ordering the result set by the active status.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_enabled(self, style):
        """Specifies a preference for ordering the result set by the administratively enabled status.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_disabled(self, style):
        """Specifies a preference for ordering the result set by the administratively disabled status.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_operational(self, style):
        """Specifies a preference for ordering the results by the operational status.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidObjectSearchOrder(OsidIdentifiableSearchOrder, OsidExtensibleSearchOrder, OsidBrowsableSearchOrder):
    """``OsidObjectSearchOrder`` specifies preferred ordering of search results.

    An ``OsidSearchOrder`` is available from an search session and
    supplied to an ``OsidSearch``. OsidObjectSearch os =
    session.getObjectSearch(); os.limitResultSet(1, 25);
    OsidObjectSearchOrder order = session.getObjectSearchOrder();
    order.orderByDisplayName(); os.orderResults(order); OsidObjectQuery
    query; query = session.getObjectQuery();
    query.addDescriptionMatch("*food*", wildcardStringMatchType, true);
    ObjectSearchResults results = session.getObjectsBySearch(query, os);
    ObjectList list = results.getObjectList();

    """

    def order_by_display_name(self, style):
        """Specifies a preference for ordering the result set by the display name.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_description(self, style):
        """Specifies a preference for ordering the result set by the description.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_genus_type(self, style):
        """Specifies a preference for ordering the result set by the genus type.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_state(self, process_id, style):
        """Orders by the state in a given ``Process``.

        :param process_id: a process ``Id``
        :type process_id: ``osid.id.Id``
        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``process_id`` or ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_cumulative_rating(self, book_id, style):
        """Orders by the cumulative rating in a given ``Book``.

        :param book_id: a book ``Id``
        :type book_id: ``osid.id.Id``
        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``book_id`` or ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_statistic(self, meter_id, style):
        """Orders by a statistic for a given ``Meter``.

        :param meter_id: a meter ``Id``
        :type meter_id: ``osid.id.Id``
        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``meter_id`` or ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_create_time(self, style):
        """Orders by the timestamp of the first journal entry.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_last_modified_time(self, style):
        """Orders by the timestamp of the last journal entry.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidRelationshipSearchOrder(OsidObjectSearchOrder, OsidTemporalSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_end_reason(self, style):
        """Specifies a preference for ordering the results by the end reason state.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_end_reason_search_order(self):
        """Tests if a ``StateSearchOrder`` is available.

        :return: ``true`` if a state search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_end_reason_search_order(self):
        """Gets the search order for a state.

        :return: the state search order
        :rtype: ``osid.process.StateSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_end_reason_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_end_reason_search_order()`` is ``true``.*

        """
        return # osid.process.StateSearchOrder

    end_reason_search_order = property(fget=get_end_reason_search_order)


class OsidCatalogSearchOrder(OsidObjectSearchOrder, OsidSourceableSearchOrder, OsidFederateableSearchOrder):
    """An interface for specifying the ordering of catalog search results."""




class OsidRuleSearchOrder(OsidObjectSearchOrder, OsidOperableSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_rule(self, style):
        """Specifies a preference for ordering the results by the associated rule.

        The element of the rule to order is not specified but may be
        managed through a ``RuleSearchOrder``.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_rule_search_order(self):
        """Tests if a ``RuleSearchOrder`` is available.

        :return: ``true`` if a rule search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_rule_search_order(self):
        """Gets the search order for a rule.

        :return: the rule search order
        :rtype: ``osid.rules.RuleSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_rule_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_rule_search_order()`` is ``true``.*

        """
        return # osid.rules.RuleSearchOrder

    rule_search_order = property(fget=get_rule_search_order)


class OsidEnablerSearchOrder(OsidRuleSearchOrder, OsidTemporalSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_schedule(self, style):
        """Specifies a preference for ordering the results by the associated schedule.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_schedule_search_order(self):
        """Tests if a ``ScheduleSearchOrder`` is available.

        :return: ``true`` if a schedule search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_schedule_search_order(self):
        """Gets the search order for a schedule.

        :return: the schedule search order
        :rtype: ``osid.calendaring.ScheduleSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_schedule_search_order() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_schedule_search_order()`` is true.*

        """
        return # osid.calendaring.ScheduleSearchOrder

    schedule_search_order = property(fget=get_schedule_search_order)

    def order_by_event(self, style):
        """Specifies a preference for ordering the results by the associated event.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_event_search_order(self):
        """Tests if an ``EventSearchOrder`` is available.

        :return: ``true`` if an event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_event_search_order(self):
        """Gets the search order for an event.

        :return: the event search order
        :rtype: ``osid.calendaring.EventSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_event_search_order() is false``

        *compliance: optional -- This method must be implemented if
        ``supports_event_search_order()`` is true.*

        """
        return # osid.calendaring.EventSearchOrder

    event_search_order = property(fget=get_event_search_order)

    def order_by_cyclic_event(self, style):
        """Orders the results by cyclic event.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_cyclic_event_search_order(self):
        """Tests if a cyclic event search order is available.

        :return: ``true`` if a cyclic event search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_cyclic_event_search_order(self):
        """Gets the cyclic event search order.

        :return: the cyclic event search order
        :rtype: ``osid.calendaring.cycle.CyclicEventSearchOrder``
        :raise: ``IllegalState`` -- ``supports_cyclic_event_search_order()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.cycle.CyclicEventSearchOrder

    cyclic_event_search_order = property(fget=get_cyclic_event_search_order)

    def order_by_demographic(self, style):
        """Specifies a preference for ordering the results by the associated demographic resource.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def supports_demographic_search_order(self):
        """Tests if a ``ResourceSearchOrder`` is available.

        :return: ``true`` if a resource search order is available, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_demographic_search_order(self):
        """Gets the search order for a demographic resource.

        :return: the resource search order
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_demographic_search_order()`` is ``false``

        *compliance: optional -- This method must be implemented if
        ``supports_demographic_search_order()`` is ``true``.*

        """
        return # osid.resource.ResourceSearchOrder

    demographic_search_order = property(fget=get_demographic_search_order)


class OsidConstrainerSearchOrder(OsidRuleSearchOrder):
    """An interface for specifying the ordering of search results."""




class OsidProcessorSearchOrder(OsidRuleSearchOrder):
    """An interface for specifying the ordering of search results."""




class OsidGovernatorSearchOrder(OsidObjectSearchOrder, OsidOperableSearchOrder, OsidSourceableSearchOrder):
    """An interface for specifying the ordering of search results."""




class OsidCompendiumSearchOrder(OsidObjectSearchOrder, OsidSubjugateableSearchOrder):
    """An interface for specifying the ordering of search results."""

    def order_by_start_date(self, style):
        """Specifies a preference for ordering the result set by the start date.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_end_date(self, style):
        """Specifies a preference for ordering the result set by the end date.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_interpolated(self, style):
        """Specifies a preference for ordering the result set by interpolated results.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def order_by_extrapolated(self, style):
        """Specifies a preference for ordering the result set by extrapolated results.

        :param style: the search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass


class OsidCapsuleSearchOrder(OsidSearchOrder):
    """An interface for specifying the ordering of search results."""




