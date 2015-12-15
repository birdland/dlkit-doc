

Metadata
========


Metadata
--------

.. py:class:: Metadata(abc_osid_metadata.Metadata)
    The ``Metadata`` interface defines a set of methods describing a the syntax and rules for
        creating
    and updating a data element inside an ``OsidForm``.


    This interface provides a means to retrieve special restrictions
    placed upon data elements such as sizes and ranges that may vary
    from provider to provider or from object to object.





    .. py:method:: get_element_id():
        :noindex:


    .. py:attribute:: element_id
        :noindex:


    .. py:method:: get_element_label():
        :noindex:


    .. py:attribute:: element_label
        :noindex:


    .. py:method:: get_instructions():
        :noindex:


    .. py:attribute:: instructions
        :noindex:


    .. py:method:: get_syntax():
        :noindex:


    .. py:attribute:: syntax
        :noindex:


    .. py:method:: is_array():
        :noindex:


    .. py:method:: is_required():
        :noindex:


    .. py:method:: is_read_only():
        :noindex:


    .. py:method:: is_linked():
        :noindex:


    .. py:method:: is_value_known():
        :noindex:


    .. py:method:: has_value():
        :noindex:


    .. py:method:: get_units():
        :noindex:


    .. py:attribute:: units
        :noindex:


    .. py:method:: get_minimum_elements():
        :noindex:


    .. py:attribute:: minimum_elements
        :noindex:


    .. py:method:: get_maximum_elements():
        :noindex:


    .. py:attribute:: maximum_elements
        :noindex:


    .. py:method:: get_minimum_cardinal():
        :noindex:


    .. py:attribute:: minimum_cardinal
        :noindex:


    .. py:method:: get_maximum_cardinal():
        :noindex:


    .. py:attribute:: maximum_cardinal
        :noindex:


    .. py:method:: get_cardinal_set():
        :noindex:


    .. py:attribute:: cardinal_set
        :noindex:


    .. py:method:: get_default_cardinal_values():
        :noindex:


    .. py:attribute:: default_cardinal_values
        :noindex:


    .. py:method:: get_existing_cardinal_values():
        :noindex:


    .. py:attribute:: existing_cardinal_values
        :noindex:


    .. py:method:: get_coordinate_types():
        :noindex:


    .. py:attribute:: coordinate_types
        :noindex:


    .. py:method:: supports_coordinate_type(coordinate_type):
        :noindex:


    .. py:method:: get_axes_for_coordinate_type(coordinate_type):
        :noindex:


    .. py:method:: get_minimum_coordinate_values(coordinate_type):
        :noindex:


    .. py:method:: get_maximum_coordinate_values(coordinate_type):
        :noindex:


    .. py:method:: get_coordinate_set():
        :noindex:


    .. py:attribute:: coordinate_set
        :noindex:


    .. py:method:: get_default_coordinate_values():
        :noindex:


    .. py:attribute:: default_coordinate_values
        :noindex:


    .. py:method:: get_existing_coordinate_values():
        :noindex:


    .. py:attribute:: existing_coordinate_values
        :noindex:


    .. py:method:: get_currency_types():
        :noindex:


    .. py:attribute:: currency_types
        :noindex:


    .. py:method:: supports_currency_type(currency_type):
        :noindex:


    .. py:method:: get_minimum_currency():
        :noindex:


    .. py:attribute:: minimum_currency
        :noindex:


    .. py:method:: get_maximum_currency():
        :noindex:


    .. py:attribute:: maximum_currency
        :noindex:


    .. py:method:: get_currency_set():
        :noindex:


    .. py:attribute:: currency_set
        :noindex:


    .. py:method:: get_default_currency_values():
        :noindex:


    .. py:attribute:: default_currency_values
        :noindex:


    .. py:method:: get_existing_currency_values():
        :noindex:


    .. py:attribute:: existing_currency_values
        :noindex:


    .. py:method:: get_date_time_resolution():
        :noindex:


    .. py:attribute:: date_time_resolution
        :noindex:


    .. py:method:: get_calendar_types():
        :noindex:


    .. py:attribute:: calendar_types
        :noindex:


    .. py:method:: supports_calendar_type(calendar_type):
        :noindex:


    .. py:method:: get_time_types():
        :noindex:


    .. py:attribute:: time_types
        :noindex:


    .. py:method:: supports_time_type(time_type):
        :noindex:


    .. py:method:: get_minimum_date_time():
        :noindex:


    .. py:attribute:: minimum_date_time
        :noindex:


    .. py:method:: get_maximum_date_time():
        :noindex:


    .. py:attribute:: maximum_date_time
        :noindex:


    .. py:method:: get_date_time_set():
        :noindex:


    .. py:attribute:: date_time_set
        :noindex:


    .. py:method:: get_default_date_time_values():
        :noindex:


    .. py:attribute:: default_date_time_values
        :noindex:


    .. py:method:: get_existing_date_time_values():
        :noindex:


    .. py:attribute:: existing_date_time_values
        :noindex:


    .. py:method:: get_decimal_scale():
        :noindex:


    .. py:attribute:: decimal_scale
        :noindex:


    .. py:method:: get_minimum_decimal():
        :noindex:


    .. py:attribute:: minimum_decimal
        :noindex:


    .. py:method:: get_maximum_decimal():
        :noindex:


    .. py:attribute:: maximum_decimal
        :noindex:


    .. py:method:: get_decimal_set():
        :noindex:


    .. py:attribute:: decimal_set
        :noindex:


    .. py:method:: get_default_decimal_values():
        :noindex:


    .. py:attribute:: default_decimal_values
        :noindex:


    .. py:method:: get_existing_decimal_values():
        :noindex:


    .. py:attribute:: existing_decimal_values
        :noindex:


    .. py:method:: get_distance_resolution():
        :noindex:


    .. py:attribute:: distance_resolution
        :noindex:


    .. py:method:: get_minimum_distance():
        :noindex:


    .. py:attribute:: minimum_distance
        :noindex:


    .. py:method:: get_maximum_distance():
        :noindex:


    .. py:attribute:: maximum_distance
        :noindex:


    .. py:method:: get_distance_set():
        :noindex:


    .. py:attribute:: distance_set
        :noindex:


    .. py:method:: get_default_distance_values():
        :noindex:


    .. py:attribute:: default_distance_values
        :noindex:


    .. py:method:: get_existing_distance_values():
        :noindex:


    .. py:attribute:: existing_distance_values
        :noindex:


    .. py:method:: get_minimum_duration():
        :noindex:


    .. py:attribute:: minimum_duration
        :noindex:


    .. py:method:: get_maximum_duration():
        :noindex:


    .. py:attribute:: maximum_duration
        :noindex:


    .. py:method:: get_duration_set():
        :noindex:


    .. py:attribute:: duration_set
        :noindex:


    .. py:method:: get_default_duration_values():
        :noindex:


    .. py:attribute:: default_duration_values
        :noindex:


    .. py:method:: get_existing_duration_values():
        :noindex:


    .. py:attribute:: existing_duration_values
        :noindex:


    .. py:method:: get_heading_types():
        :noindex:


    .. py:attribute:: heading_types
        :noindex:


    .. py:method:: supports_heading_type(heading_type):
        :noindex:


    .. py:method:: get_axes_for_heading_type(heading_type):
        :noindex:


    .. py:method:: get_minimum_heading_values(heading_type):
        :noindex:


    .. py:method:: get_maximum_heading_values(heading_type):
        :noindex:


    .. py:method:: get_heading_set():
        :noindex:


    .. py:attribute:: heading_set
        :noindex:


    .. py:method:: get_default_heading_values():
        :noindex:


    .. py:attribute:: default_heading_values
        :noindex:


    .. py:method:: get_existing_heading_values():
        :noindex:


    .. py:attribute:: existing_heading_values
        :noindex:


    .. py:method:: get_id_set():
        :noindex:


    .. py:attribute:: id_set
        :noindex:


    .. py:method:: get_default_id_values():
        :noindex:


    .. py:attribute:: default_id_values
        :noindex:


    .. py:method:: get_existing_id_values():
        :noindex:


    .. py:attribute:: existing_id_values
        :noindex:


    .. py:method:: get_minimum_integer():
        :noindex:


    .. py:attribute:: minimum_integer
        :noindex:


    .. py:method:: get_maximum_integer():
        :noindex:


    .. py:attribute:: maximum_integer
        :noindex:


    .. py:method:: get_integer_set():
        :noindex:


    .. py:attribute:: integer_set
        :noindex:


    .. py:method:: get_default_integer_values():
        :noindex:


    .. py:attribute:: default_integer_values
        :noindex:


    .. py:method:: get_existing_integer_values():
        :noindex:


    .. py:attribute:: existing_integer_values
        :noindex:


    .. py:method:: get_object_types():
        :noindex:


    .. py:attribute:: object_types
        :noindex:


    .. py:method:: supports_object_type(object_type):
        :noindex:


    .. py:method:: get_object_set():
        :noindex:


    .. py:attribute:: object_set
        :noindex:


    .. py:method:: get_default_object_values():
        :noindex:


    .. py:attribute:: default_object_values
        :noindex:


    .. py:method:: get_existing_object_values():
        :noindex:


    .. py:attribute:: existing_object_values
        :noindex:


    .. py:method:: get_spatial_unit_record_types():
        :noindex:


    .. py:attribute:: spatial_unit_record_types
        :noindex:


    .. py:method:: supports_spatial_unit_record_type(spatial_unit_record_type):
        :noindex:


    .. py:method:: get_spatial_unit_set():
        :noindex:


    .. py:attribute:: spatial_unit_set
        :noindex:


    .. py:method:: get_default_spatial_unit_values():
        :noindex:


    .. py:attribute:: default_spatial_unit_values
        :noindex:


    .. py:method:: get_existing_spatial_unit_values():
        :noindex:


    .. py:attribute:: existing_spatial_unit_values
        :noindex:


    .. py:method:: get_minimum_speed():
        :noindex:


    .. py:attribute:: minimum_speed
        :noindex:


    .. py:method:: get_maximum_speed():
        :noindex:


    .. py:attribute:: maximum_speed
        :noindex:


    .. py:method:: get_speed_set():
        :noindex:


    .. py:attribute:: speed_set
        :noindex:


    .. py:method:: get_default_speed_values():
        :noindex:


    .. py:attribute:: default_speed_values
        :noindex:


    .. py:method:: get_existing_speed_values():
        :noindex:


    .. py:attribute:: existing_speed_values
        :noindex:


    .. py:method:: get_minimum_string_length():
        :noindex:


    .. py:attribute:: minimum_string_length
        :noindex:


    .. py:method:: get_maximum_string_length():
        :noindex:


    .. py:attribute:: maximum_string_length
        :noindex:


    .. py:method:: get_string_match_types():
        :noindex:


    .. py:attribute:: string_match_types
        :noindex:


    .. py:method:: supports_string_match_type(string_match_type):
        :noindex:


    .. py:method:: get_string_expression(string_match_type):
        :noindex:


    .. py:method:: get_string_format_types():
        :noindex:


    .. py:attribute:: string_format_types
        :noindex:


    .. py:method:: get_string_set():
        :noindex:


    .. py:attribute:: string_set
        :noindex:


    .. py:method:: get_default_string_values():
        :noindex:


    .. py:attribute:: default_string_values
        :noindex:


    .. py:method:: get_existing_string_values():
        :noindex:


    .. py:attribute:: existing_string_values
        :noindex:


    .. py:method:: get_minimum_time():
        :noindex:


    .. py:attribute:: minimum_time
        :noindex:


    .. py:method:: get_maximum_time():
        :noindex:


    .. py:attribute:: maximum_time
        :noindex:


    .. py:method:: get_time_set():
        :noindex:


    .. py:attribute:: time_set
        :noindex:


    .. py:method:: get_default_time_values():
        :noindex:


    .. py:attribute:: default_time_values
        :noindex:


    .. py:method:: get_existing_time_values():
        :noindex:


    .. py:attribute:: existing_time_values
        :noindex:


    .. py:method:: get_type_set():
        :noindex:


    .. py:attribute:: type_set
        :noindex:


    .. py:method:: get_default_type_values():
        :noindex:


    .. py:attribute:: default_type_values
        :noindex:


    .. py:method:: get_existing_type_values():
        :noindex:


    .. py:attribute:: existing_type_values
        :noindex:


    .. py:method:: get_version_types():
        :noindex:


    .. py:attribute:: version_types
        :noindex:


    .. py:method:: supports_version_type(version_type):
        :noindex:


    .. py:method:: get_minimum_version():
        :noindex:


    .. py:attribute:: minimum_version
        :noindex:


    .. py:method:: get_maximum_version():
        :noindex:


    .. py:attribute:: maximum_version
        :noindex:


    .. py:method:: get_version_set():
        :noindex:


    .. py:attribute:: version_set
        :noindex:


    .. py:method:: get_default_version_values():
        :noindex:


    .. py:attribute:: default_version_values
        :noindex:


    .. py:method:: get_existing_version_values():
        :noindex:


    .. py:attribute:: existing_version_values
        :noindex:


