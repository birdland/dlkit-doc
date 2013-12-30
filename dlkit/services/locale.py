# -*- coding: utf-8 -*-
"""Locale Open Service Interface Definitions
locale version 3.0.0

The Locale OSID provides the service of localizing applications defining
interfaces for string translation, measurement unit conversion, calendar
conversion, spatial conversion, and currency conversion.

String Translation

The Locale OSID can access and manage string translations using the
``TranslationSession`` and ``TranslationAdminSession`` respectively.
Translations map a pair of strings with language and script Types. The
translation services provide a simple means for an OSID Consumer to
localize known display strings for an application.

Numeric Formatting

The ``NumericFormattingSession`` provides the service of converting
numbers to display strings and parsing display strings into numbers. The
format of the display string is identified by a numeric format ``Type``.
It supports the various numeric types defined among OSID Primitives such
as integers, decimals, and cardinal numbers.

Calendar Formatting

The ``CalendarFormattingSession`` converts ``DateTime`` and ``Time``
OSID Primitives to display strings and parses display strings back into
``DateTimes`` and ``Times``. The display string formats are specified by
a date format ``Type`` and time format ``Type`` respectively. The
calendaring and time systems implemented by ``DateTime`` and ``Time``
are specified by a calendar ``Type`` and time ``Type``. Conversions
among calendaring systems are performed using the
``CalendarConversionSession``.

Currency Formatting

The ``CurrencyFormattingSession`` converts currency amounts to display
strings and parses display strings into currency amounts. The format of
the display string is identified by both a currency and a numeric format
``Type``. Conversions among currencies are performed using the
``CurrencyConversionSession``.

Coordinate Formatting

The ``CoordinateFormattingSession`` converts ``Coordinate`` OSID
Primitives to display strings and parses display strings back into
``Coordinates``. The display string formats are specified by a
coordinate format ``Type``. The coordinate data is identified by the
coordinate record ``Type``. Conversions among calendaring systems are
performed using the ``CoordinateConversionSession``.

Unit Conversion

The ``UnitConversionSession`` converts units of measurement among unit
types. The unit types may represent different units within the same
system of measurement or units among different measurement systems where
a conversion exists.

Currency Conversion

The ``CurrencyConversionSession`` converts a currency amount from one
currency system to another where a means for transforming the currency
values exists.

Spatial Unit Conversion

The ``SpatialUnitConversionSession`` converts a spatial units from one
spatial system to another where a means for transforming the spatial
units exists.

Informational Objects

The Locale OSID includes a ``CalendarInfo`` and ``TimeInfo`` interfaces
for inspecting the details of the respective ``Types`` to assist in
displaying calendars and clocks without knowledge of the specific
system.

The ``Locale`` interface defines a set of types that together define the
formatting, language, calendaring, and currency for a locale or culture.
Locale is referenced in OsidSessions to convey the localization of the
service.

"""
from . import osid
from .osid_errors import Unimplemented, IllegalState, OperationFailed


class LocaleProfile(osid.OsidProfile):

    def supports_visible_federation(self):
        """Tests if visible federation is supported.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_translation(self):
        """Tests if translation is supported.

        :return: ``true`` if translation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_translation_admin(self):
        """Tests if translation administration is supported.

        :return: ``true`` if translation administration is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_numeric_formatting(self):
        """Tests if numeric formatting is supported.

        :return: ``true`` if numeric formatting is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_formatting(self):
        """Tests if calendar formatting is supported.

        :return: ``true`` if calendar formatting is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_currency_formatting(self):
        """Tests if currency formatting is supported.

        :return: ``true`` if currency formatting is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_coordinate_formatting(self):
        """Tests if coordinate formatting is supported.

        :return: ``true`` if coordinate formatting is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_unit_conversion(self):
        """Tests if unit conversion is supported.

        :return: ``true`` if unit conversion is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_currency_conversion(self):
        """Tests if currency conversion is supported.

        :return: ``true`` if currency conversion is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_conversion(self):
        """Tests if calendar conversion is supported.

        :return: ``true`` if calendar conversion is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_coordinate_conversion(self):
        """Tests if coordnate conversion is supported.

        :return: ``true`` if coordinate conversion is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_spatial_unit_conversion(self):
        """Tests if spatial unit conversion is supported.

        :return: ``true`` if spatial unit conversion is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_info(self):
        """Tests if a calendar informational service is supported.

        :return: ``true`` if calendar info is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_language_types_for_translation(self, source_language_type, source_script_type, target_language_type, target_script_type):
        """Tests if a given language translation is supported.

        :param source_language_type: the type of the source language
        :type source_language_type: ``osid.type.Type``
        :param source_script_type: the type of the source script
        :type source_script_type: ``osid.type.Type``
        :param target_language_type: the type of the target language
        :type target_language_type: ``osid.type.Type``
        :param target_script_type: the type of the target script
        :type target_script_type: ``osid.type.Type``
        :return: ``true`` if the given source and target translation is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``source_language_type, source_script_type, target_language_type`` or ``target_script_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_language_types_for_source(self, source_language_type, source_script_type):
        """Gets the list of target language types for a given source language type.

        :param source_language_type: the type of the source language
        :type source_language_type: ``osid.type.Type``
        :param source_script_type: the type of the source script
        :type source_script_type: ``osid.type.Type``
        :return: the list of supported types for the given source language type
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_language_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_source_language_types(self):
        """Gets all the source language types supported.

        :return: the list of supported language types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    source_language_types = property(fget=get_source_language_types)

    def get_script_types_for_language_type(self, language_type):
        """Gets the list of script types available for a given language type.

        :param language_type: the type of the language
        :type language_type: ``osid.type.Type``
        :return: the list of supported script types for the given language type
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``language_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def supports_numeric_format_types(self, numeric_format_type):
        """Tests if a given numeric format type is supported.

        :param numeric_format_type: the type of the numeric format
        :type numeric_format_type: ``osid.type.Type``
        :return: ``true`` if the given numeric format type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``numeric_format_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_numeric_format_types(self):
        """Gets all the numeric format types supported.

        :return: the list of supported numeric format types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    numeric_format_types = property(fget=get_numeric_format_types)

    def supports_calendar_types_for_formatting(self, calendar_type, time_type, date_format_type, time_format_type):
        """Tests if a given calendaring formatting is supported.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :param time_type: the type of the time system
        :type time_type: ``osid.type.Type``
        :param date_format_type: the type of the output date format
        :type date_format_type: ``osid.type.Type``
        :param time_format_type: the type of the output time format
        :type time_format_type: ``osid.type.Type``
        :return: ``true`` if formatting with the given types is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_type, calendar_format_type, time_type,`` or ``time_format_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_calendar_types_for_formatting(self):
        """Gets all the calendar types for which formats are available.

        :return: the list of calendar types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    calendar_types_for_formatting = property(fget=get_calendar_types_for_formatting)

    def get_date_format_types_for_calendar_type(self, calendar_type):
        """Gets the list of date format types for a given calendar type.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :return: the list of supported date format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``calendar_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_time_types_for_formatting(self):
        """Gets all the time types for which formatting is available.

        :return: the list of time types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    time_types_for_formatting = property(fget=get_time_types_for_formatting)

    def get_time_format_types_for_time_type(self, time_type):
        """Gets the list of time format types for a given time type.

        :param time_type: the type of the time
        :type time_type: ``osid.type.Type``
        :return: the list of supported time format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``time_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def supports_currency_types_for_formatting(self, currency_type, numeric_format_type):
        """Tests if a given currency formatting is supported.

        :param currency_type: the type of the currency
        :type currency_type: ``osid.type.Type``
        :param numeric_format_type: the type of the output currency format
        :type numeric_format_type: ``osid.type.Type``
        :return: ``true`` if formatting with the given types is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``currency_type`` or ``numeric_format_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_currency_types_for_formatting(self):
        """Gets all the currency types for which formatting is available.

        :return: the list of currency types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    currency_types_for_formatting = property(fget=get_currency_types_for_formatting)

    def get_currency_format_types_for_currency_type(self, currency_type):
        """Gets the list of currency format types for a given currency type.

        :param currency_type: the type of the currency
        :type currency_type: ``osid.type.Type``
        :return: the list of supported currency format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``currency_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def supports_coordinate_types_for_formatting(self, coordinate_type, coordinate_format_type):
        """Tests if a given coordinate formatting is supported.

        :param coordinate_type: the type of the coordinate
        :type coordinate_type: ``osid.type.Type``
        :param coordinate_format_type: the type of the output coordinate format
        :type coordinate_format_type: ``osid.type.Type``
        :return: ``true`` if formatting with the given types is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``cooridinate_type`` or ``coodinate_format_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_types_for_formatting(self):
        """Gets all the coordinate types for which formatting is available.

        :return: the list of coordinate types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    coordinate_types_for_formatting = property(fget=get_coordinate_types_for_formatting)

    def get_coordinate_format_types_for_coordinate_type(self, coordinate_type):
        """Gets the list of coordinate format types for a given coordinate type.

        :param coordinate_type: the type of the coordinate
        :type coordinate_type: ``osid.type.Type``
        :return: the list of supported coordinate format types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``coordinater_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def supports_unit_types_for_conversion(self, source_unit_type, target_unit_type):
        """Tests if a given measure conversion is supported.

        :param source_unit_type: the type of the source measure
        :type source_unit_type: ``osid.type.Type``
        :param target_unit_type: the type of the target measure
        :type target_unit_type: ``osid.type.Type``
        :return: ``true`` if the given source and target conversion is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``source_unit_type`` or ``target_unit_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_unit_types_for_source(self, source_unit_type):
        """Gets the list of target measure types for a given source measure type.

        :param source_unit_type: the type of the source measure
        :type source_unit_type: ``osid.type.Type``
        :return: the list of supported measure types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_unit_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_source_unit_types(self):
        """Gets all the source unit types supported.

        :return: the list of supported unit types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    source_unit_types = property(fget=get_source_unit_types)

    def supports_currency_types_for_conversion(self, source_currency_type, target_currency_type):
        """Tests if a given currency conversion is supported.

        :param source_currency_type: the type of the source currency
        :type source_currency_type: ``osid.type.Type``
        :param target_currency_type: the type of the target currency
        :type target_currency_type: ``osid.type.Type``
        :return: ``true`` if the given source and target conversion is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``source_currency_type`` or ``target_currency_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_currency_types_for_source(self, source_currency_type):
        """Gets the list of target currency types for a given source currency type.

        :param source_currency_type: the type of the source currency
        :type source_currency_type: ``osid.type.Type``
        :return: the list of supported currency types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_currency_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_source_currency_types(self):
        """Gets the list of source currency types.

        :return: the list of supported currency types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    source_currency_types = property(fget=get_source_currency_types)

    def supports_calendar_types_for_conversion(self, source_calendar_type, target_calendar_type):
        """Tests if a given calendar conversion is supported.

        :param source_calendar_type: the type of the source calendar
        :type source_calendar_type: ``osid.type.Type``
        :param target_calendar_type: the type of the target calendar
        :type target_calendar_type: ``osid.type.Type``
        :return: ``true`` if the given source and target conversion is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``source_calendar_type`` or ``target_calendar_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_calendar_types_for_source(self, source_calendar_type):
        """Gets the list of target calendar types for a given source calendar type.

        :param source_calendar_type: the type of the source calendar
        :type source_calendar_type: ``osid.type.Type``
        :return: the list of supported calendar types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_calendar_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_source_calendar_types(self):
        """Gets the list of target calendar types for a given source calendar type.

        :return: the list of supported calendar types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    source_calendar_types = property(fget=get_source_calendar_types)

    def supports_time_types_for_conversion(self, source_time_type, target_time_type):
        """Tests if a given time conversion is supported.

        :param source_time_type: the type of the source time
        :type source_time_type: ``osid.type.Type``
        :param target_time_type: the type of the target time
        :type target_time_type: ``osid.type.Type``
        :return: ``true`` if the given source and target conversion is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``source_time_type`` or ``target_time_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_time_types_for_source(self, source_time_type):
        """Gets the list of target time types for a given source time type.

        :param source_time_type: the type of the source time
        :type source_time_type: ``osid.type.Type``
        :return: the list of supported time types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_time_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_source_time_types(self):
        """Gets the list of target time types for a given source time type.

        :return: the list of supported time types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    source_time_types = property(fget=get_source_time_types)

    def get_time_types_for_calendar_type(self, calendar_type):
        """Gets the list of time types supported for a given calendar type where they are both used in a ``DateTime``.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :return: the list of supported time types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``calendar_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_calendar_types_for_time_type(self, time_type):
        """Gets the list of calendar types supported for a given time type where they are both used in a ``DateTime``.

        :param time_type: the type of the time system
        :type time_type: ``osid.type.Type``
        :return: the list of supported calendar types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``time_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def supports_calendar_time_types(self, calendar_type, time_type):
        """Tests if a given calendar and time type are used together in a ``DateTime``.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :param time_type: the type of the time system
        :type time_type: ``osid.type.Type``
        :return: ``true`` if the given calendar and time types are supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``calendar_type`` or ``time_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def supports_coordinate_types_for_conversion(self, source_coordinate_type, target_coordinate_type):
        """Tests if a given coordinate type for conversion is supported.

        :param source_coordinate_type: the type of the source coordinate
        :type source_coordinate_type: ``osid.type.Type``
        :param target_coordinate_type: the type of the target coordinate
        :type target_coordinate_type: ``osid.type.Type``
        :return: ``true`` if the given source and target conversion is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``source_coordinate_type`` or ``target_coordinate_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_types_for_source(self, source_coordinate_type):
        """Gets the list of target coordinate types for a given source coordinate type.

        :param source_coordinate_type: the type of the source coordinate
        :type source_coordinate_type: ``osid.type.Type``
        :return: the list of supported coordinate types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_coordinate_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_source_coordinate_types(self):
        """Gets the list of target coordinate types for a given source coordinate type.

        :return: the list of supported coordinate types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    source_coordinate_types = property(fget=get_source_coordinate_types)

    def supports_spatial_unit_record_types_for_conversion(self, source_spatial_unit_record_type, target_spatial_unit_record_type):
        """Tests if a given spatial unit conversion is supported.

        :param source_spatial_unit_record_type: the type of the source spatial unit record
        :type source_spatial_unit_record_type: ``osid.type.Type``
        :param target_spatial_unit_record_type: the type of the target spatial unit record
        :type target_spatial_unit_record_type: ``osid.type.Type``
        :return: ``true`` if the given source and target conversion is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``source_spatial_unit_record_type`` or ``target_spatial_unit_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_spatial_unit_record_types_for_source(self, source_spatial_unit_record_type):
        """Gets the list of target spatial unit types for a given source spatial unit type.

        :param source_spatial_unit_record_type: the type of the source spatial unit record
        :type source_spatial_unit_record_type: ``osid.type.Type``
        :return: the list of supported spatial unit record types
        :rtype: ``osid.type.TypeList``
        :raise: ``NullArgument`` -- ``source_spatial_unit_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_source_spatial_unit_record_types(self):
        """Gets the list of target spatial unit record types for a given source spatial unit type.

        :return: the list of supported spatial unit recod types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    source_spatial_unit_record_types = property(fget=get_source_spatial_unit_record_types)



class LocaleManager(osid.OsidManager, osid.OsidSession, LocaleProfile):

    def get_translation_session(self):
        """Gets an ``OsidSession`` associated with the language translation service.

        :return: a ``TranslationSession``
        :rtype: ``osid.locale.TranslationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_translation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    translation_session = property(fget=get_translation_session)

    def get_translation_session_for_type(self, source_language_type, source_script_type, target_language_type, target_script_type):
        """Gets an ``OsidSession`` associated with the language translation service and the given language and script types.

        :param source_language_type: the type of the source language
        :type source_language_type: ``osid.type.Type``
        :param source_script_type: the type of the source script
        :type source_script_type: ``osid.type.Type``
        :param target_language_type: the type of the target language
        :type target_language_type: ``osid.type.Type``
        :param target_script_type: the type of the target script
        :type target_script_type: ``osid.type.Type``
        :return: a ``TranslationSession``
        :rtype: ``osid.locale.TranslationSession``
        :raise: ``NullArgument`` -- ``source_language_type, source_script_type, target_language_type`` or ``target_script_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_translation()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_language_types_for_translation(source_language_type, source_script_type, target_language_type, target_script_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_translation_admin_session(self):
        """Gets a language translation administration service for updating a locale dictionary.

        :return: a ``TranslationAdminSession``
        :rtype: ``osid.locale.TranslationAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_translation_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    translation_admin_session = property(fget=get_translation_admin_session)

    def get_translation_admin_session_for_type(self, source_language_type, source_script_type, target_language_type, target_script_type):
        """Gets a language trabslation administration service for updating a locale dictionary using the given language and script types.

        :param source_language_type: the type of the source language
        :type source_language_type: ``osid.type.Type``
        :param source_script_type: the type of the source script
        :type source_script_type: ``osid.type.Type``
        :param target_language_type: the type of the target language
        :type target_language_type: ``osid.type.Type``
        :param target_script_type: the type of the target script
        :type target_script_type: ``osid.type.Type``
        :return: a ``TranslationAdminSession``
        :rtype: ``osid.locale.TranslationAdminSession``
        :raise: ``NullArgument`` -- ``source_language_type, source_script_type, target_language_type`` or ``target_script_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_translation_admin()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_language_types_for_translation(source_language_type, source_script_type, target_language_type, target_script_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_numeric_formatting_session(self):
        """Gets an ``OsidSession`` associated with the numeric formatting service.

        :return: a ``NumericFormattingSession``
        :rtype: ``osid.locale.NumericFormattingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_numeric_formatting()`` is ``false``

        """
        raise UNIMPLEMENTED()

    numeric_formatting_session = property(fget=get_numeric_formatting_session)

    def get_numeric_formatting_session_for_type(self, numeric_format_type):
        """Gets an ``OsidSession`` associated with the numeric formatting service and the given numeric format type.

        :param numeric_format_type: the type of the numeric format
        :type numeric_format_type: ``osid.type.Type``
        :return: a ``NumericFormattingSession``
        :rtype: ``osid.locale.NumericFormattingSession``
        :raise: ``NullArgument`` -- ``numeric_format_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_numeric_formatting()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_numeric_format_type(numeric_format_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_formatting_session(self):
        """Gets an ``OsidSession`` associated with the calendar formatting service.

        :return: a ``CalendarFormattingSession``
        :rtype: ``osid.locale.CalendarFormattingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_formatting()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calendar_formatting_session = property(fget=get_calendar_formatting_session)

    def get_calendar_formatting_session_for_type(self, calendar_type, calendar_format_type, time_type, time_format_type):
        """Gets an ``OsidSession`` associated with the calendar formatting service and the given calendar and time types.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :param calendar_format_type: the type of the calendar format
        :type calendar_format_type: ``osid.type.Type``
        :param time_type: the type of the time system
        :type time_type: ``osid.type.Type``
        :param time_format_type: the type of the time format
        :type time_format_type: ``osid.type.Type``
        :return: a ``CalendarFormattingSession``
        :rtype: ``osid.locale.CalendarFormattingSession``
        :raise: ``NullArgument`` -- ``calendar_type, calendar_format_type, time_type`` or ``time_format_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_formatting()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_calendar_types_for_formattinge(calendar_type, calendar_format_type, time_type, time_format_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_currency_formatting_session(self):
        """Gets an ``OsidSession`` associated with the currency formatting service.

        :return: a ``CurrencyFormattingSession``
        :rtype: ``osid.locale.CurrencyFormattingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_currency_formatting()`` is ``false``

        """
        raise UNIMPLEMENTED()

    currency_formatting_session = property(fget=get_currency_formatting_session)

    def get_currency_formatting_session_for_type(self, currency_type, numeric_format_type):
        """Gets an ``OsidSession`` associated with the currency formatting service and the given currency and numeric format types.

        :param currency_type: the type of the currency
        :type currency_type: ``osid.type.Type``
        :param numeric_format_type: the type of the numeric format
        :type numeric_format_type: ``osid.type.Type``
        :return: a ``CurrencyFormattingSession``
        :rtype: ``osid.locale.CurrencyFormattingSession``
        :raise: ``NullArgument`` -- ``currency_type`` or ``numeric_format_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_currency_formatting()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_currency_types_for_fomatting(currency_type, numeric_format_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_formatting_session(self):
        """Gets an ``OsidSession`` associated with the coordinate formatting service.

        :return: a ``CoordinateFormattingSession``
        :rtype: ``osid.locale.CoordinateFormattingSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_coordinate_formatting()`` is ``false``

        """
        raise UNIMPLEMENTED()

    coordinate_formatting_session = property(fget=get_coordinate_formatting_session)

    def get_coordinate_formatting_session_for_type(self, coordinate_type, coordinate_format_type):
        """Gets an ``OsidSession`` associated with the coordinate formatting service and the given coordinate and format types.

        :param coordinate_type: the type of the coordinate
        :type coordinate_type: ``osid.type.Type``
        :param coordinate_format_type: the type of the coordinate format
        :type coordinate_format_type: ``osid.type.Type``
        :return: a ``CoordinateFormattingSession``
        :rtype: ``osid.locale.CoordinateFormattingSession``
        :raise: ``NullArgument`` -- ``coordinate_type`` or ``coordinate_format_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_coordinate_formatting()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_coordinate_types_for_fomatting(coordinate_type, coordinate_format_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_unit_conversion_session(self):
        """Gets a unit conversion session.

        :return: a ``UnitConversionSession``
        :rtype: ``osid.locale.UnitConversionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_unit_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    unit_conversion_session = property(fget=get_unit_conversion_session)

    def get_currency_conversion_session(self):
        """Gets a currency conversion session.

        :return: a ``CurrencyConversionSession``
        :rtype: ``osid.locale.CurrencyConversionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_currency_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    currency_conversion_session = property(fget=get_currency_conversion_session)

    def get_currency_conversion_session_for_type(self, source_currency_type, target_currency_type):
        """Gets an ``OsidSession`` associated with the currency conversion service and the given currency types.

        :param source_currency_type: the type of the source currency
        :type source_currency_type: ``osid.type.Type``
        :param target_currency_type: the type of the target currency
        :type target_currency_type: ``osid.type.Type``
        :return: a ``CurrencyConversionSession``
        :rtype: ``osid.locale.CurrencyConversionSession``
        :raise: ``NullArgument`` -- ``source_currency_type`` or ``target_currency_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_currency_conversion()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_currency_types_for_conversion(source_currency_type, target_currency_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_conversion_session(self):
        """Gets a calendar conversion session.

        :return: a ``CalendarConversionSession``
        :rtype: ``osid.locale.CalendarConversionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calendar_conversion_session = property(fget=get_calendar_conversion_session)

    def get_calendar_conversion_session_for_type(self, source_calendar_type, source_time_type, target_calendar_type, target_time_type):
        """Gets an ``OsidSession`` associated with the calendar conversion service and the given calendar types.

        :param source_calendar_type: the type of the source calendar
        :type source_calendar_type: ``osid.type.Type``
        :param source_time_type: the type of the source time
        :type source_time_type: ``osid.type.Type``
        :param target_calendar_type: the type of the target calendar
        :type target_calendar_type: ``osid.type.Type``
        :param target_time_type: the type of the target time
        :type target_time_type: ``osid.type.Type``
        :return: a ``CalendarConversionSession``
        :rtype: ``osid.locale.CalendarConversionSession``
        :raise: ``NullArgument`` -- ``source_calendar_type, source_time_type,``  ``target_calendar_type`` or ``target_time_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_conversion()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_calendar_types_for_conversion(source_calendar_type, target_calendar_type)`` or ``supports_time_types_for_conversion(source_time_type, target_time_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_conversion_session(self):
        """Gets a coordinate conversion session.

        :return: a ``CoordinateConversionSession``
        :rtype: ``osid.locale.CoordinateConversionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_coordinate_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    coordinate_conversion_session = property(fget=get_coordinate_conversion_session)

    def get_coordinate_conversion_session_for_type(self, source_coordinate_type, target_coordinate_type):
        """Gets an ``OsidSession`` associated with the coordinate conversion service and the given coordinate types.

        :param source_coordinate_type: the type of the source coordinate
        :type source_coordinate_type: ``osid.type.Type``
        :param target_coordinate_type: the type of the target coordinate
        :type target_coordinate_type: ``osid.type.Type``
        :return: a ``CoordinateConversionSession``
        :rtype: ``osid.locale.CoordinateConversionSession``
        :raise: ``NullArgument`` -- ``source_coordinate_type`` or ``target_coordinate_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_coordinate_conversion()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_coordinate_record_types_for_conversion(source_coordinate_type, target_coordinate_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_spatial_unit_conversion_session(self):
        """Gets a spatial unit conversion session.

        :return: a ``SpatialUnitConversionSession``
        :rtype: ``osid.locale.SpatialUnitConversionSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_spatial_unit_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    spatial_unit_conversion_session = property(fget=get_spatial_unit_conversion_session)

    def get_spatial_unit_conversion_session_for_type(self, source_spatial_unit_record_type, target_spatial_unit_record_type):
        """Gets an ``OsidSession`` associated with the spatial unit conversion service and the given coordinate record types.

        :param source_spatial_unit_record_type: the type of the source spatial unit record
        :type source_spatial_unit_record_type: ``osid.type.Type``
        :param target_spatial_unit_record_type: the type of the target spatial unit record
        :type target_spatial_unit_record_type: ``osid.type.Type``
        :return: a ``SpatialUnitConversionSession``
        :rtype: ``osid.locale.SpatialUnitConversionSession``
        :raise: ``NullArgument`` -- ``source_spatial_unit_record_type`` or ``target_spatial_unit_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_spatial_unit_conversion()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_spatial_unit_record_types_for_conversion(source_spatial_unit_record_type, target_spatial_unit_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_info_session(self):
        """Gets a calendar informational session session.

        :return: a ``CalendarInfoSession``
        :rtype: ``osid.locale.CalendarInfoSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_info()`` is ``false``

        """
        raise UNIMPLEMENTED()

    calendar_info_session = property(fget=get_calendar_info_session)

    def get_calendar_info_session_for_type(self, calendar_type, time_type):
        """Gets an ``OsidSession`` associated with the calendar informational service and the given calendar and time types.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :param time_type: the type of the time system
        :type time_type: ``osid.type.Type``
        :return: a ``CalendarInfoSession``
        :rtype: ``osid.locale.CalendarInfoSession``
        :raise: ``NullArgument`` -- ``calendar_type`` or ``time_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_type()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_calendar_time_types(calendar_type, time_type)`` is ``false``

        """
        raise UNIMPLEMENTED()



class LocaleProxyManager(osid.OsidProxyManager, LocaleProfile):

    def get_translation_session(self, proxy):
        """Gets an ``OsidSession`` associated with the language translation service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TranslationSession``
        :rtype: ``osid.locale.TranslationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_translation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_translation_session_for_type(self, source_language_type, source_script_type, target_language_type, target_script_type, proxy):
        """Gets an ``OsidSession`` associated with the language translation service and the given language and script types.

        :param source_language_type: the type of the source language
        :type source_language_type: ``osid.type.Type``
        :param source_script_type: the type of the source script
        :type source_script_type: ``osid.type.Type``
        :param target_language_type: the type of the target language
        :type target_language_type: ``osid.type.Type``
        :param target_script_type: the type of the target script
        :type target_script_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TranslationSession``
        :rtype: ``osid.locale.TranslationSession``
        :raise: ``NullArgument`` -- ``source_language_type, source_script_type, target_language_type, target_script_type`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_translation()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_language_types_for_translation(source_language_type, source_script_type, target_language_type, target_script_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_translation_admin_session(self, proxy):
        """Gets a language translation administration service for updating a locale dictionary.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TranslationAdminSession``
        :rtype: ``osid.locale.TranslationAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_translation_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_translation_admin_session_for_type(self, source_language_type, source_script_type, target_language_type, target_script_type, proxy):
        """Gets a language trabslation administration service for updating a locale dictionary using the given language and script types.

        :param source_language_type: the type of the source language
        :type source_language_type: ``osid.type.Type``
        :param source_script_type: the type of the source script
        :type source_script_type: ``osid.type.Type``
        :param target_language_type: the type of the target language
        :type target_language_type: ``osid.type.Type``
        :param target_script_type: the type of the target script
        :type target_script_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``TranslationAdminSession``
        :rtype: ``osid.locale.TranslationAdminSession``
        :raise: ``NullArgument`` -- ``source_language_type, source_script_type, target_language_type, target_script_type`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_translation_admin()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_language_types_for_translation(source_language_type, source_script_type, target_language_type, target_script_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_numeric_formatting_session(self, proxy):
        """Gets an ``OsidSession`` associated with the numeric formatting service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``NumericFormattingSession``
        :rtype: ``osid.locale.NumericFormattingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_numeric_formatting()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_numeric_formatting_session_for_type(self, numeric_format_type, proxy):
        """Gets an ``OsidSession`` associated with the numeric formatting service and the given numeric format type.

        :param numeric_format_type: the type of the numeric format
        :type numeric_format_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``NumericFormattingSession``
        :rtype: ``osid.locale.NumericFormattingSession``
        :raise: ``NullArgument`` -- ``numeric_format_type`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_numeric_formatting()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_numeric_format_type(numeric_format_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_formatting_session(self, proxy):
        """Gets an ``OsidSession`` associated with the calendar formatting service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarFormattingSession``
        :rtype: ``osid.locale.CalendarFormattingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_formatting()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_formatting_session_for_type(self, calendar_type, calendar_format_type, time_type, time_format_type, proxy):
        """Gets an ``OsidSession`` associated with the calendar formatting service and the given calendar and time types.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :param calendar_format_type: the type of the calendar format
        :type calendar_format_type: ``osid.type.Type``
        :param time_type: the type of the time system
        :type time_type: ``osid.type.Type``
        :param time_format_type: the type of the time format
        :type time_format_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarFormattingSession``
        :rtype: ``osid.locale.CalendarFormattingSession``
        :raise: ``NullArgument`` -- ``calendar_type, calendar_format_type, time_typ, time_format_type`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_formatting()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_calendar_types_for_formattinge(calendar_type, calendar_format_type, time_type, time_format_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_currency_formatting_session(self, proxy):
        """Gets an ``OsidSession`` associated with the currency formatting service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CurrencyFormattingSession``
        :rtype: ``osid.locale.CurrencyFormattingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_currency_formatting()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_currency_formatting_session_for_type(self, currency_type, numeric_format_type, proxy):
        """Gets an ``OsidSession`` associated with the currency formatting service and the given currency and numeric format types.

        :param currency_type: the type of the currency
        :type currency_type: ``osid.type.Type``
        :param numeric_format_type: the type of the numeric format
        :type numeric_format_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CurrencyFormattingSession``
        :rtype: ``osid.locale.CurrencyFormattingSession``
        :raise: ``NullArgument`` -- ``currency_type, numeric_format_type`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_currency_formatting()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_currency_types_for_fomatting(currency_type, numeric_format_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_formatting_session(self, proxy):
        """Gets an ``OsidSession`` associated with the coordinate formatting service.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CoordinateFormattingSession``
        :rtype: ``osid.locale.CoordinateFormattingSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_coordinate_formatting()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_formatting_session_for_type(self, coordinate_type, coordinate_format_type, proxy):
        """Gets an ``OsidSession`` associated with the coordinate formatting service and the given coordinate and format types.

        :param coordinate_type: the type of the coordinate
        :type coordinate_type: ``osid.type.Type``
        :param coordinate_format_type: the type of the coordinate format
        :type coordinate_format_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CoordinateFormattingSession``
        :rtype: ``osid.locale.CoordinateFormattingSession``
        :raise: ``NullArgument`` -- ``coordinate_type, coordinate_format_type,`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_coordinate_formatting()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_coordinate_types_for_fomatting(coordinate_type, coordinate_format_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_unit_conversion_session(self, proxy):
        """Gets a unit conversion session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``UnitConversionSession``
        :rtype: ``osid.locale.UnitConversionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_unit_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_currency_conversion_session(self, proxy):
        """Gets a currency conversion session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CurrencyConversionSession``
        :rtype: ``osid.locale.CurrencyConversionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_currency_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_currency_conversion_session_for_type(self, source_currency_type, target_currency_type, proxy):
        """Gets an ``OsidSession`` associated with the currency conversion service and the given currency types.

        :param source_currency_type: the type of the source currency
        :type source_currency_type: ``osid.type.Type``
        :param target_currency_type: the type of the target currency
        :type target_currency_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CurrencyConversionSession``
        :rtype: ``osid.locale.CurrencyConversionSession``
        :raise: ``NullArgument`` -- ``source_currency_type, target_currency_type`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_currency_conversion()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_currency_types_for_conversion(source_currency_type, target_currency_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_conversion_session(self, proxy):
        """Gets a calendar conversion session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarConversionSession``
        :rtype: ``osid.locale.CalendarConversionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_conversion_session_for_type(self, source_calendar_type, source_time_type, target_calendar_type, target_time_type, proxy):
        """Gets an ``OsidSession`` associated with the calendar conversion service and the given calendar types.

        :param source_calendar_type: the type of the source calendar
        :type source_calendar_type: ``osid.type.Type``
        :param source_time_type: the type of the source time
        :type source_time_type: ``osid.type.Type``
        :param target_calendar_type: the type of the target calendar
        :type target_calendar_type: ``osid.type.Type``
        :param target_time_type: the type of the target time
        :type target_time_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarConversionSession``
        :rtype: ``osid.locale.CalendarConversionSession``
        :raise: ``NullArgument`` -- ``source_calendar_type, source_time_type, target_calendar_type, target_time_type`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_conversion()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_calendar_types_for_conversion(source_calendar_type, target_calendar_type)`` or ``supports_time_types_for_conversion(source_time_type, target_time_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_conversion_session(self, proxy):
        """Gets a coordinate conversion session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CoordinateConversionSession``
        :rtype: ``osid.locale.CoordinateConversionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_coordinate_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_coordinate_conversion_session_for_type(self, source_coordinate_type, target_coordinate_type, proxy):
        """Gets an ``OsidSession`` associated with the coordinate conversion service and the given coordinate types.

        :param source_coordinate_type: the type of the source coordinate
        :type source_coordinate_type: ``osid.type.Type``
        :param target_coordinate_type: the type of the target coordinate
        :type target_coordinate_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CoordinateConversionSession``
        :rtype: ``osid.locale.CoordinateConversionSession``
        :raise: ``NullArgument`` -- ``source_coordinate_type,``  ``target_coordinate_type,`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_coordinate_conversion()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_coordinate_record_types_for_conversion(source_coordinate_type, target_coordinate_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_spatial_unit_conversion_session(self, proxy):
        """Gets a spatial unit conversion session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SpatialUnitConversionSession``
        :rtype: ``osid.locale.SpatialUnitConversionSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_spatial_unit_conversion()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_spatial_unit_conversion_session_for_type(self, source_spatial_unit_record_type, target_spatial_unit_record_type, proxy):
        """Gets an ``OsidSession`` associated with the spatial unit conversion service and the given coordinate record types.

        :param source_spatial_unit_record_type: the type of the source spatial unit record
        :type source_spatial_unit_record_type: ``osid.type.Type``
        :param target_spatial_unit_record_type: the type of the target spatial unit record
        :type target_spatial_unit_record_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``SpatialUnitConversionSession``
        :rtype: ``osid.locale.SpatialUnitConversionSession``
        :raise: ``NullArgument`` -- ``source_spatial_unit_record_type,``  ``target_spatial_unit_record_type or`` proxy is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_spatial_unit_conversion()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_spatial_unit_record_types_for_conversion(source_spatial_unit_record_type, target_spatial_unit_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_info_session(self, proxy):
        """Gets a calendar informational session session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarInfoSession``
        :rtype: ``osid.locale.CalendarInfoSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_info()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_calendar_info_session_for_type(self, calendar_type, time_type, proxy):
        """Gets an ``OsidSession`` associated with the calendar informational service and the given calendar and time types.

        :param calendar_type: the type of the calendar
        :type calendar_type: ``osid.type.Type``
        :param time_type: the type of the time system
        :type time_type: ``osid.type.Type``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``CalendarInfoSession``
        :rtype: ``osid.locale.CalendarInfoSession``
        :raise: ``NullArgument`` -- ``calendar_type, time_type`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_calendar_type()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unsupported`` -- ``supports_calendar_time_types(calendar_type, time_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


