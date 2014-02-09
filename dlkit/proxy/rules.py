from ..osid import rules as osid_rules


class Proxy(osid_rules.OsidResult):
    """A ``Proxy`` is used to transfer external information from an application server into an OSID Provider."""
    def has_authentication(self):
        """Tests if an authentication is available.

        :return: ``true`` if an ``Authentication`` is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_authentication(self):
        """Gets the ``Authentication`` for this proxy.

        :return: the authentication
        :rtype: ``osid.authentication.process.Authentication``
        :raise: ``IllegalState`` -- ``has_authentication()`` is ``false``

        """
        return # osid.authentication.process.Authentication

    authentication = property(fget=get_authentication)

    def has_effective_agent(self):
        """Tests if an effective agent is available.

        :return: ``true`` if an effective agent is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_effective_agent_id(self):
        """Gets the effective ``Agent Id`` for this proxy.

        :return: the effective agent ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_effective_agent()`` is ``false``

        """
        return # osid.id.Id

    effective_agent_id = property(fget=get_effective_agent_id)

    def has_effective_date(self):
        """Tests if an effective date is available.

        :return: ``true`` if an effective date is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_effective_date(self):
        """Gets the effective date.

        :return: the effective date
        :rtype: ``timestamp``
        :raise: ``IllegalState`` -- ``has_effective_date()`` is ``false``

        """
        return # timestamp

    effective_date = property(fget=get_effective_date)

    def get_effective_clock_rate(self):
        """Gets the rate of the clock.

        :return: the rate
        :rtype: ``decimal``
        :raise: ``IllegalState`` -- ``has_effective_date()`` is ``false``

        """
        return # decimal

    effective_clock_rate = property(fget=get_effective_clock_rate)

    def get_locale(self):
        """Gets the locale.

        :return: a locale
        :rtype: ``osid.locale.Locale``

        """
        return # osid.locale.Locale

    locale = property(fget=get_locale)

    def has_format_type(self):
        """Tests if a ``DisplayText`` format ``Type`` is available.

        :return: ``true`` if a format type is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_format_type(self):
        """Gets the ``DisplayText`` format ``Type``.

        :return: the format ``Type``
        :rtype: ``osid.type.Type``
        :raise: ``IllegalState`` -- ``has_format_type()`` is ``false``

        """
        return # osid.type.Type

    format_type = property(fget=get_format_type)

    def get_proxy_record(self, proxy_record_type):
        """Gets the proxy record corresponding to the given ``Proxy`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``proxy_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(proxy_record_type)``
        is ``true`` .

        :param proxy_record_type: the type of proxy record to retrieve
        :type proxy_record_type: ``osid.type.Type``
        :return: the proxy record
        :rtype: ``osid.proxy.records.ProxyRecord``
        :raise: ``NullArgument`` -- ``proxy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proxy_record_type)`` is ``false``

        """
        return # osid.proxy.records.ProxyRecord


class ProxyCondition(osid_rules.OsidCondition):
    """A ``ProxyCondition`` is used to transfer external information into a proxy."""
    def set_effective_agent_id(self, agent_id):
        """Sets the effective agent ``Id`` to indicate acting on behalf of.

        :param agent_id: an agent ``Id``
        :type agent_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``

        """
        pass

    effective_agent_id = property(fset=set_effective_agent_id)

    def set_effective_date(self, date, rate):
        """Sets the effective date.

        :param date: a date
        :type date: ``timestamp``
        :param rate: the rate at which the clock should tick from the given effective date. 0 is a clock that is fixed
        :type rate: ``decimal``
        :raise: ``NullArgument`` -- ``date`` is ``null``

        """
        pass

    def set_language_type(self, language_type):
        """Sets the language type.

        :param language_type: the language type
        :type language_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``language_type`` is ``null``

        """
        pass

    language_type = property(fset=set_language_type)

    def set_script_type(self, script_type):
        """Sets the script type.

        :param script_type: the script type
        :type script_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``script_type`` is ``null``

        """
        pass

    script_type = property(fset=set_script_type)

    def set_calendar_type(self, calendar_type):
        """Sets the calendar type.

        :param calendar_type: the calendar type
        :type calendar_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``calendar_type`` is ``null``

        """
        pass

    calendar_type = property(fset=set_calendar_type)

    def set_time_type(self, time_type):
        """Sets the time type.

        :param time_type: the time type
        :type time_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``time_type`` is ``null``

        """
        pass

    time_type = property(fset=set_time_type)

    def set_currency_type(self, currency_type):
        """Sets the currency type.

        :param currency_type: the currency type
        :type currency_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``currency_type`` is ``null``

        """
        pass

    currency_type = property(fset=set_currency_type)

    def set_unit_system_type(self, unit_system_type):
        """Sets the unit system type.

        :param unit_system_type: the unit system type
        :type unit_system_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``unit_system_type`` is ``null``

        """
        pass

    unit_system_type = property(fset=set_unit_system_type)

    def set_format_type(self, format_type):
        """Sets the ``DisplayText`` format type.

        :param format_type: the format type
        :type format_type: ``osid.type.Type``
        :raise: ``NullArgument`` -- ``format_type`` is ``null``

        """
        pass

    format_type = property(fset=set_format_type)

    def get_proxy_condition_record(self, proxy_condition_type):
        """Gets the proxy condition record corresponding to the given ``Proxy`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``proxy_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(proxy_record_type)``
        is ``true`` .

        :param proxy_condition_type: the type of proxy condition record to retrieve
        :type proxy_condition_type: ``osid.type.Type``
        :return: the proxy condition record
        :rtype: ``osid.proxy.records.ProxyConditionRecord``
        :raise: ``NullArgument`` -- ``proxy_condition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(proxy_condition_record_type)`` is ``false``

        """
        return # osid.proxy.records.ProxyConditionRecord


