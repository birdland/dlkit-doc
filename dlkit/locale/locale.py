
from ..osid import managers as osid_managers
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class LocaleProfile(osid_managers.OsidProfile):
    """The locale profile describes the interoperability of locale services."""

    def __init__(self):
        self._provider_manager = None


    def get_language_types_for_source(self, source_language_type, source_script_type):
        """Gets the list of target language types for a given source language type.

        :param source_language_type: the type of the source language
        :type source_language_type: ``osid.type.Type``
        :param source_script_type: the type of the source script
        :type source_script_type: ``osid.type.Type``
        :return: the list of supported types for the given source language type
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_language_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_source_language_types(self):
        """Gets all the source language types supported.

        :return: the list of supported language types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    source_language_types = property(fget=get_source_language_types)

    def get_script_types_for_language_type(self, language_type):
        """Gets the list of script types available for a given language type.

        :param language_type: the type of the language
        :type language_type: ``osid.type.Type``
        :return: the list of supported script types for the given language type
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``language_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_numeric_format_types(self):
        """Gets all the numeric format types supported.

        :return: the list of supported numeric format types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    numeric_format_types = property(fget=get_numeric_format_types)

    def get_calendar_types_for_formatting(self):
        """Gets all the calendar types for which formats are available.

        :return: the list of calendar types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    calendar_types_for_formatting = property(fget=get_calendar_types_for_formatting)

    def get_date_format_types_for_calendar_type(self, calendar_type):
        """Gets the list of date format types for a given calendar type.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :return: the list of supported date format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``calendar_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_time_types_for_formatting(self):
        """Gets all the time types for which formatting is available.

        :return: the list of time types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    time_types_for_formatting = property(fget=get_time_types_for_formatting)

    def get_time_format_types_for_time_type(self, time_type):
        """Gets the list of time format types for a given time type.

        :param time_type: the type of the time
        :type time_type: ``osid.type.Type``
        :return: the list of supported time format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``time_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_currency_types_for_formatting(self):
        """Gets all the currency types for which formatting is available.

        :return: the list of currency types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    currency_types_for_formatting = property(fget=get_currency_types_for_formatting)

    def get_currency_format_types_for_currency_type(self, currency_type):
        """Gets the list of currency format types for a given currency type.

        :param currency_type: the type of the currency
        :type currency_type: ``osid.type.Type``
        :return: the list of supported currency format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``currency_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_coordinate_types_for_formatting(self):
        """Gets all the coordinate types for which formatting is available.

        :return: the list of coordinate types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    coordinate_types_for_formatting = property(fget=get_coordinate_types_for_formatting)

    def get_coordinate_format_types_for_coordinate_type(self, coordinate_type):
        """Gets the list of coordinate format types for a given coordinate type.

        :param coordinate_type: the type of the coordinate
        :type coordinate_type: ``osid.type.Type``
        :return: the list of supported coordinate format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``coordinater_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_unit_types_for_source(self, source_unit_type):
        """Gets the list of target measure types for a given source measure type.

        :param source_unit_type: the type of the source measure
        :type source_unit_type: ``osid.type.Type``
        :return: the list of supported target measure types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_unit_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_source_unit_types(self):
        """Gets all the source unit types supported.

        :return: the list of supported source unit types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    source_unit_types = property(fget=get_source_unit_types)

    def get_currency_types_for_source(self, source_currency_type):
        """Gets the list of target currency types for a given source currency type.

        :param source_currency_type: the type of the source currency
        :type source_currency_type: ``osid.type.Type``
        :return: the list of supported currency types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_currency_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_source_currency_types(self):
        """Gets the list of source currency types.

        :return: the list of supported source currency types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    source_currency_types = property(fget=get_source_currency_types)

    def get_calendar_types_for_source(self, source_calendar_type):
        """Gets the list of target calendar types for a given source calendar type.

        :param source_calendar_type: the type of the source calendar
        :type source_calendar_type: ``osid.type.Type``
        :return: the list of supported calendar types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_calendar_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_source_calendar_types(self):
        """Gets the list of source calendar types.

        :return: the list of supported source calendar types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    source_calendar_types = property(fget=get_source_calendar_types)

    def get_time_types_for_source(self, source_time_type):
        """Gets the list of target time types for a given source time type.

        :param source_time_type: the type of the source time
        :type source_time_type: ``osid.type.Type``
        :return: the list of supported time types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_time_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_source_time_types(self):
        """Gets the list of source time types.

        :return: the list of supported source time types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    source_time_types = property(fget=get_source_time_types)

    def get_time_types_for_calendar_type(self, calendar_type):
        """Gets the list of time types supported for a given calendar type where they are both used in a ``DateTime``.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :return: the list of supported time types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``calendar_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_calendar_types_for_time_type(self, time_type):
        """Gets the list of calendar types supported for a given time type where they are both used in a ``DateTime``.

        :param time_type: the type of the time system
        :type time_type: ``osid.type.Type``
        :return: the list of supported calendar types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``time_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_coordinate_types_for_source(self, source_coordinate_type):
        """Gets the list of target coordinate types for a given source coordinate type.

        :param source_coordinate_type: the type of the source coordinate
        :type source_coordinate_type: ``osid.type.Type``
        :return: the list of supported target coordinate types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_coordinate_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_source_coordinate_types(self):
        """Gets the list of source coordinate types.

        :return: the list of supported source coordinate types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    source_coordinate_types = property(fget=get_source_coordinate_types)

    def get_spatial_unit_record_types_for_source(self, source_spatial_unit_record_type):
        """Gets the list of target spatial unit types for a given source spatial unit type.

        :param source_spatial_unit_record_type: the type of the source spatial unit record
        :type source_spatial_unit_record_type: ``osid.type.Type``
        :return: the list of supported target spatial unit record types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_spatial_unit_record_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_source_spatial_unit_record_types(self):
        """Gets the list of source spatial unit record types.

        :return: the list of supported source spatial unit record types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    source_spatial_unit_record_types = property(fget=get_source_spatial_unit_record_types)

    def get_format_types_for_source(self, source_format_type):
        """Gets the list of target format types for a given source spatial unit type.

        :param source_format_type: the type of the source format
        :type source_format_type: ``osid.type.Type``
        :return: the list of supported target format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_format_type`` is ``null``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    def get_source_format_types(self):
        """Gets the list of source format types.

        :return: the list of supported source format types
        :rtype: ``osid.type.TypeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.type.TypeList

    source_format_types = property(fget=get_source_format_types)


class LocaleManager(osid_managers.OsidManager, osid_sessions.OsidSession, LocaleProfile):
    """The locale manager provides access to locale sessions and provides interoperability tests for various aspects of this service.

    The sessions included in this manager are:

      * ``TranslationSession:`` a session translate strings
      * ``TranslationAdminSession: a`` session to update the string
        translations for a locale
      * ``NumericFormattingSession:`` a session for formatting and
        parsing numbers
      * ``CalendarFormattingSession:`` a session for formatting and
        parsing dates and times
      * ``CurrencyFormattingSession`` : a session for formatting and
        parsing currency amounts
      * ``CoordinateFormattingSession:`` a session for formatting and
        parsing coordinates
      * ``UnitConversionSession:`` a session to convert measurement
        units ``None``
      * ``CurrencyConversionSession:`` a session to convert currency
      * ``CalendarConversionSession:`` a session to convert dates across
        calendars
      * ``CoordinateConversionSession:`` a session to convert coordinate
        systems
      * ``SpatialUnitConversionSession:`` a session to convert spatial
        units
      * ``FormatConversionSession:`` a session to convert text formats
      * ``CalendarInfoSession:`` a session for examining calendaring and
        time systems

    """

    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._no_catalog_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)
        self._sub_package_provider_managers = dict()

    def _set_no_catalog_view(self, session):
        """Sets the underlying no_catalog view to match current view"""
        if self._no_catalog_view == COMPARATIVE:
            try:
                session.use_comparative_no_catalog_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_no_catalog_view()
            except AttributeError:
                pass

    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_no_catalog_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _get_sub_package_provider_manager(self, sub_package_name):
        if sub_package_name in self._sub_package_provider_managers:
            return self._sub_package_provider_managers[sub_package_name]
        config = self._runtime.get_configuration()
        parameter_id = Id('parameter:{0}ProviderImpl@dlkit_service'.format(sub_package_name))
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            sub_package = self._runtime.get_manager(sub_package_name.upper(), provider_impl)
        else:
            # need to add version argument
            sub_package = self._runtime.get_proxy_manager(sub_package_name.upper(), provider_impl)
        self._sub_package_provider_managers[sub_package_name] = sub_package
        return sub_package

    def _get_sub_package_provider_session(self, sub_package, session_name, proxy=None):
        """Gets the session from a sub-package"""
        agent_key = self._get_agent_key(proxy)
        if session_name in self._provider_sessions[agent_key]:
            return self._provider_sessions[agent_key][session_name]
        else:
            manager = self._get_sub_package_provider_manager(sub_package)
            session = self._instantiate_session('get_' + session_name + '_for_bank',
                                                proxy=self._proxy,
                                                manager=manager)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[agent_key][session_name] = session
            return session

    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            try:
                return session_class(bank_id=self._catalog_id, *args, **kwargs)
            except AttributeError:
                return session_class(*args, **kwargs)
        else:
            try:
                return session_class(bank_id=self._catalog_id, proxy=proxy, *args, **kwargs)
            except AttributeError:
                return session_class(proxy=proxy, *args, **kwargs)

    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:localeProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('LOCALE', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('LOCALE', provider_impl)

    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()

    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC

    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY

    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()




class LocaleProxyManager(osid_managers.OsidProxyManager, LocaleProfile):
    """The locale manager provides access to locale sessions and provides interoperability tests for various aspects of this service.

    Methods in this manager support the passing of a ``Proxy`` for
    passing information from server environments. The sessions included
    in this manager are:

      * ``TranslationSession:`` a session translate strings
      * ``TranslationAdminSession: a`` session to update the string
        translations for a locale
      * ``NumericFormattingSession:`` a session for formatting and
        parsing numbers
      * ``CalendarFormattingSession:`` a session for formatting and
        parsing dates and times
      * ``CurrencyFormattingSession`` : a session for formatting and
        parsing currency amounts
      * ``CoordinateFormattingSession:`` a session for formatting and
        parsing coordinates
      * ``UnitConversionSession:`` a session to convert measurement
        units ``None``
      * ``CurrencyConversionSession:`` a session to convert currency
      * ``CalendarConversionSession:`` a session to convert dates across
        calendars
      * ``CoordinateConversionSession:`` a session to convert coordinate
        systems
      * ``SpatialUnitConversionSession:`` a session to convert spatial
        units
      * ``FormatConversionSession:`` a session to convert text formats
      * ``CalendarInfoSession:`` a session for examining calendaring and
        time systems

    """
    pass



