.. currentmodule:: dlkit.services.locale
.. automodule:: dlkit.services.locale

Services
========


Locale Manager
--------------

.. autoclass:: LocaleManager
   :show-inheritance:





Locale Profile Methods
______________

.. automethod:: LocaleManager.supports_visible_federation

.. automethod:: LocaleManager.supports_translation

.. automethod:: LocaleManager.supports_translation_admin

.. automethod:: LocaleManager.supports_numeric_formatting

.. automethod:: LocaleManager.supports_calendar_formatting

.. automethod:: LocaleManager.supports_currency_formatting

.. automethod:: LocaleManager.supports_coordinate_formatting

.. automethod:: LocaleManager.supports_unit_conversion

.. automethod:: LocaleManager.supports_currency_conversion

.. automethod:: LocaleManager.supports_calendar_conversion

.. automethod:: LocaleManager.supports_coordinate_conversion

.. automethod:: LocaleManager.supports_spatial_unit_conversion

.. automethod:: LocaleManager.supports_calendar_info

.. automethod:: LocaleManager.supports_language_types_for_translation

.. automethod:: LocaleManager.get_language_types_for_source

.. autoattribute:: LocaleManager.source_language_types

.. automethod:: LocaleManager.get_script_types_for_language_type

.. automethod:: LocaleManager.supports_numeric_format_types

.. autoattribute:: LocaleManager.numeric_format_types

.. automethod:: LocaleManager.supports_calendar_types_for_formatting

.. autoattribute:: LocaleManager.calendar_types_for_formatting

.. automethod:: LocaleManager.get_date_format_types_for_calendar_type

.. autoattribute:: LocaleManager.time_types_for_formatting

.. automethod:: LocaleManager.get_time_format_types_for_time_type

.. automethod:: LocaleManager.supports_currency_types_for_formatting

.. autoattribute:: LocaleManager.currency_types_for_formatting

.. automethod:: LocaleManager.get_currency_format_types_for_currency_type

.. automethod:: LocaleManager.supports_coordinate_types_for_formatting

.. autoattribute:: LocaleManager.coordinate_types_for_formatting

.. automethod:: LocaleManager.get_coordinate_format_types_for_coordinate_type

.. automethod:: LocaleManager.supports_unit_types_for_conversion

.. automethod:: LocaleManager.get_unit_types_for_source

.. autoattribute:: LocaleManager.source_unit_types

.. automethod:: LocaleManager.supports_currency_types_for_conversion

.. automethod:: LocaleManager.get_currency_types_for_source

.. autoattribute:: LocaleManager.source_currency_types

.. automethod:: LocaleManager.supports_calendar_types_for_conversion

.. automethod:: LocaleManager.get_calendar_types_for_source

.. autoattribute:: LocaleManager.source_calendar_types

.. automethod:: LocaleManager.supports_time_types_for_conversion

.. automethod:: LocaleManager.get_time_types_for_source

.. autoattribute:: LocaleManager.source_time_types

.. automethod:: LocaleManager.get_time_types_for_calendar_type

.. automethod:: LocaleManager.get_calendar_types_for_time_type

.. automethod:: LocaleManager.supports_calendar_time_types

.. automethod:: LocaleManager.supports_coordinate_types_for_conversion

.. automethod:: LocaleManager.get_coordinate_types_for_source

.. autoattribute:: LocaleManager.source_coordinate_types

.. automethod:: LocaleManager.supports_spatial_unit_record_types_for_conversion

.. automethod:: LocaleManager.get_spatial_unit_record_types_for_source

.. autoattribute:: LocaleManager.source_spatial_unit_record_types



Locale Proxy Manager
--------------------

.. autoclass:: LocaleProxyManager
   :show-inheritance:

.. automethod:: LocaleProxyManager.get_translation_session

.. automethod:: LocaleProxyManager.get_translation_session_for_type

.. automethod:: LocaleProxyManager.get_translation_admin_session

.. automethod:: LocaleProxyManager.get_translation_admin_session_for_type

.. automethod:: LocaleProxyManager.get_numeric_formatting_session

.. automethod:: LocaleProxyManager.get_numeric_formatting_session_for_type

.. automethod:: LocaleProxyManager.get_calendar_formatting_session

.. automethod:: LocaleProxyManager.get_calendar_formatting_session_for_type

.. automethod:: LocaleProxyManager.get_currency_formatting_session

.. automethod:: LocaleProxyManager.get_currency_formatting_session_for_type

.. automethod:: LocaleProxyManager.get_coordinate_formatting_session

.. automethod:: LocaleProxyManager.get_coordinate_formatting_session_for_type

.. automethod:: LocaleProxyManager.get_unit_conversion_session

.. automethod:: LocaleProxyManager.get_currency_conversion_session

.. automethod:: LocaleProxyManager.get_currency_conversion_session_for_type

.. automethod:: LocaleProxyManager.get_calendar_conversion_session

.. automethod:: LocaleProxyManager.get_calendar_conversion_session_for_type

.. automethod:: LocaleProxyManager.get_coordinate_conversion_session

.. automethod:: LocaleProxyManager.get_coordinate_conversion_session_for_type

.. automethod:: LocaleProxyManager.get_spatial_unit_conversion_session

.. automethod:: LocaleProxyManager.get_spatial_unit_conversion_session_for_type

.. automethod:: LocaleProxyManager.get_calendar_info_session

.. automethod:: LocaleProxyManager.get_calendar_info_session_for_type



