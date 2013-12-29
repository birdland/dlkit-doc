.. currentmodule:: dlkit.locale.objects
.. automodule:: dlkit.locale.objects

Objects
=======


Calendar Info
-------------

.. autoclass:: CalendarInfo
   :show-inheritance:

.. autoattribute:: CalendarInfo.calendar_type

.. autoattribute:: CalendarInfo.display_name

.. autoattribute:: CalendarInfo.description

.. autoattribute:: CalendarInfo.common_era_name

.. autoattribute:: CalendarInfo.common_era_abbrev

.. autoattribute:: CalendarInfo.before_common_era_name

.. autoattribute:: CalendarInfo.before_common_era_abbrev

.. autoattribute:: CalendarInfo.first_year_in_common_era

.. autoattribute:: CalendarInfo.last_year_before_common_era

.. autoattribute:: CalendarInfo.year_name

.. autoattribute:: CalendarInfo.month_name

.. automethod:: CalendarInfo.has_variable_months

.. autoattribute:: CalendarInfo.num_months

.. automethod:: CalendarInfo.get_num_months_for_year

.. autoattribute:: CalendarInfo.months

.. automethod:: CalendarInfo.get_months_for_year

.. autoattribute:: CalendarInfo.day_name

.. automethod:: CalendarInfo.has_variable_days

.. autoattribute:: CalendarInfo.num_days

.. automethod:: CalendarInfo.get_num_days_for_month

.. autoattribute:: CalendarInfo.days

.. automethod:: CalendarInfo.get_days_for_month

.. autoattribute:: CalendarInfo.first_day_of_year

.. autoattribute:: CalendarInfo.end_of_days_name

.. autoattribute:: CalendarInfo.origin

.. autoattribute:: CalendarInfo.end_of_days

.. autoattribute:: CalendarInfo.weekdays



Time Info
---------

.. autoclass:: TimeInfo
   :show-inheritance:

.. autoattribute:: TimeInfo.time_type

.. autoattribute:: TimeInfo.display_name

.. autoattribute:: TimeInfo.display_label

.. autoattribute:: TimeInfo.description

.. autoattribute:: TimeInfo.hour_name

.. autoattribute:: TimeInfo.hour_abbrev

.. autoattribute:: TimeInfo.hour_initial

.. automethod:: TimeInfo.has_variable_hours

.. autoattribute:: TimeInfo.num_hours

.. automethod:: TimeInfo.get_num_hours_for_day

.. autoattribute:: TimeInfo.minute_name

.. autoattribute:: TimeInfo.minute_abbrev

.. autoattribute:: TimeInfo.minute_initial

.. automethod:: TimeInfo.has_variable_minutes

.. autoattribute:: TimeInfo.num_minutes

.. automethod:: TimeInfo.get_num_minutes_for_hour

.. autoattribute:: TimeInfo.second_name

.. autoattribute:: TimeInfo.second_abbrev

.. autoattribute:: TimeInfo.second_initial

.. automethod:: TimeInfo.has_variable_seconds

.. autoattribute:: TimeInfo.num_seconds

.. automethod:: TimeInfo.get_num_seconds_for_minute



Calendar Unit
-------------

.. autoclass:: CalendarUnit
   :show-inheritance:

.. autoattribute:: CalendarUnit.name

.. autoattribute:: CalendarUnit.abbrev3

.. autoattribute:: CalendarUnit.abbrev2

.. autoattribute:: CalendarUnit.initial

.. autoattribute:: CalendarUnit.date_time_code

.. autoattribute:: CalendarUnit.description



Locale
------

.. autoclass:: Locale
   :show-inheritance:

.. autoattribute:: Locale.language_type

.. autoattribute:: Locale.script_type

.. autoattribute:: Locale.calendar_type

.. autoattribute:: Locale.time_type

.. autoattribute:: Locale.currency_type

.. autoattribute:: Locale.unit_system_type

.. autoattribute:: Locale.numeric_format_type

.. autoattribute:: Locale.calendar_format_type

.. autoattribute:: Locale.time_format_type

.. autoattribute:: Locale.currency_format_type

.. autoattribute:: Locale.coordinate_format_type



Locale List
-----------

.. autoclass:: LocaleList
   :show-inheritance:

.. autoattribute:: LocaleList.next_locale

.. automethod:: LocaleList.get_next_locales



