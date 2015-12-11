
from ..osid import rules as osid_rules


class Proxy(osid_rules.OsidResult):
    """A ``Proxy`` is used to transfer external information from an application server into an OSID Provider."""
    



    def has_authentication(self):
        """Tests if an authentication is available.

        return: (boolean) - ``true`` if an ``Authentication`` is
                available, ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_authentication(self):
        """Gets the ``Authentication`` for this proxy.

        return: (osid.authentication.process.Authentication) - the
                authentication
        raise:  IllegalState - ``has_authentication()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.process.Authentication

    authentication = property(fget=get_authentication)


    def has_effective_agent(self):
        """Tests if an effective agent is available.

        return: (boolean) - ``true`` if an effective agent is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_effective_agent_id(self):
        """Gets the effective ``Agent Id`` for this proxy.

        return: (osid.id.Id) - the effective agent ``Id``
        raise:  IllegalState - ``has_effective_agent()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    effective_agent_id = property(fget=get_effective_agent_id)


    def get_effective_agent(self):
        """Gets the effective ``Agent`` for this proxy.

        return: (osid.authentication.Agent) - the effective agent
        raise:  IllegalState - ``has_effective_agent()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    effective_agent = property(fget=get_effective_agent)


    def has_effective_date(self):
        """Tests if an effective date is available.

        return: (boolean) - ``true`` if an effective date is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_effective_date(self):
        """Gets the effective date.

        return: (timestamp) - the effective date
        raise:  IllegalState - ``has_effective_date()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # timestamp

    effective_date = property(fget=get_effective_date)


    def get_effective_clock_rate(self):
        """Gets the rate of the clock.

        return: (decimal) - the rate
        raise:  IllegalState - ``has_effective_date()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # decimal

    effective_clock_rate = property(fget=get_effective_clock_rate)


    def get_locale(self):
        """Gets the locale.

        return: (osid.locale.Locale) - a locale
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.locale.Locale

    locale = property(fget=get_locale)


    def has_format_type(self):
        """Tests if a ``DisplayText`` format ``Type`` is available.

        return: (boolean) - ``true`` if a format type is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_format_type(self):
        """Gets the ``DisplayText`` format ``Type``.

        return: (osid.type.Type) - the format ``Type``
        raise:  IllegalState - ``has_format_type()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*

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

        arg:    proxy_record_type (osid.type.Type): the type of proxy
                record to retrieve
        return: (osid.proxy.records.ProxyRecord) - the proxy record
        raise:  NullArgument - ``proxy_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(proxy_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.proxy.records.ProxyRecord


class ProxyCondition(osid_rules.OsidCondition):
    """A ``ProxyCondition`` is used to transfer external information into a proxy."""
    



    def set_effective_agent_id(self, agent_id):
        """Sets the effective agent ``Id`` to indicate acting on behalf of.

        arg:    agent_id (osid.id.Id): an agent ``Id``
        raise:  NullArgument - ``agent_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    effective_agent_id = property(fset=set_effective_agent_id)


    def set_effective_date(self, date, rate):
        """Sets the effective date.

        arg:    date (timestamp): a date
        arg:    rate (decimal): the rate at which the clock should tick
                from the given effective date. 0 is a clock that is
                fixed
        raise:  NullArgument - ``date`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def set_language_type(self, language_type):
        """Sets the language type.

        arg:    language_type (osid.type.Type): the language type
        raise:  NullArgument - ``language_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    language_type = property(fset=set_language_type)


    def set_script_type(self, script_type):
        """Sets the script type.

        arg:    script_type (osid.type.Type): the script type
        raise:  NullArgument - ``script_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    script_type = property(fset=set_script_type)


    def set_calendar_type(self, calendar_type):
        """Sets the calendar type.

        arg:    calendar_type (osid.type.Type): the calendar type
        raise:  NullArgument - ``calendar_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    calendar_type = property(fset=set_calendar_type)


    def set_time_type(self, time_type):
        """Sets the time type.

        arg:    time_type (osid.type.Type): the time type
        raise:  NullArgument - ``time_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    time_type = property(fset=set_time_type)


    def set_currency_type(self, currency_type):
        """Sets the currency type.

        arg:    currency_type (osid.type.Type): the currency type
        raise:  NullArgument - ``currency_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    currency_type = property(fset=set_currency_type)


    def set_unit_system_type(self, unit_system_type):
        """Sets the unit system type.

        arg:    unit_system_type (osid.type.Type): the unit system type
        raise:  NullArgument - ``unit_system_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    unit_system_type = property(fset=set_unit_system_type)


    def set_format_type(self, format_type):
        """Sets the ``DisplayText`` format type.

        arg:    format_type (osid.type.Type): the format type
        raise:  NullArgument - ``format_type`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

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

        arg:    proxy_condition_type (osid.type.Type): the type of proxy
                condition record to retrieve
        return: (osid.proxy.records.ProxyConditionRecord) - the proxy
                condition record
        raise:  NullArgument - ``proxy_condition_record_type`` is
                ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported -
                ``has_record_type(proxy_condition_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.proxy.records.ProxyConditionRecord


