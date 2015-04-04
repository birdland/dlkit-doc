.. currentmodule:: dlkit.configuration.queries
.. automodule:: dlkit.configuration.queries

Queries
=======


Parameter Query
---------------

.. autoclass:: ParameterQuery
   :show-inheritance:

   .. automethod:: ParameterQuery.match_value_syntax

   .. autoattribute:: ParameterQuery.value_syntax_terms

   .. automethod:: ParameterQuery.match_value_coordinate_type

   .. autoattribute:: ParameterQuery.value_coordinate_type_terms

   .. automethod:: ParameterQuery.match_value_heading_type

   .. autoattribute:: ParameterQuery.value_heading_type_terms

   .. automethod:: ParameterQuery.match_value_object_type

   .. autoattribute:: ParameterQuery.value_object_type_terms

   .. automethod:: ParameterQuery.match_value_spatial_unit_record_type

   .. autoattribute:: ParameterQuery.value_spatial_unit_record_type_terms

   .. automethod:: ParameterQuery.match_value_version_scheme

   .. autoattribute:: ParameterQuery.value_version_scheme_terms

   .. automethod:: ParameterQuery.supports_value_query

   .. autoattribute:: ParameterQuery.value_query

   .. automethod:: ParameterQuery.match_any_value

   .. autoattribute:: ParameterQuery.value_terms

   .. automethod:: ParameterQuery.match_values_shuffled

   .. automethod:: ParameterQuery.match_any_values_shuffled

   .. autoattribute:: ParameterQuery.values_shuffled_terms

   .. automethod:: ParameterQuery.match_configuration_id

   .. autoattribute:: ParameterQuery.configuration_id_terms

   .. automethod:: ParameterQuery.supports_configuration_query

   .. autoattribute:: ParameterQuery.configuration_query

   .. autoattribute:: ParameterQuery.configuration_terms

   .. automethod:: ParameterQuery.get_parameter_query_record



Value Query
-----------

.. autoclass:: ValueQuery
   :show-inheritance:

   .. automethod:: ValueQuery.match_priority

   .. automethod:: ValueQuery.match_any_priority

   .. autoattribute:: ValueQuery.priority_terms

   .. automethod:: ValueQuery.match_boolean_value

   .. autoattribute:: ValueQuery.boolean_value_terms

   .. automethod:: ValueQuery.match_bytes_value

   .. autoattribute:: ValueQuery.bytes_value_terms

   .. automethod:: ValueQuery.match_cardinal_value

   .. autoattribute:: ValueQuery.cardinal_value_terms

   .. automethod:: ValueQuery.match_coordinate_value

   .. autoattribute:: ValueQuery.coordinate_value_terms

   .. automethod:: ValueQuery.match_currency_value

   .. autoattribute:: ValueQuery.currency_value_terms

   .. automethod:: ValueQuery.match_date_time_value

   .. autoattribute:: ValueQuery.date_time_value_terms

   .. automethod:: ValueQuery.match_decimal_value

   .. autoattribute:: ValueQuery.decimal_value_terms

   .. automethod:: ValueQuery.match_distance_value

   .. autoattribute:: ValueQuery.distance_value_terms

   .. automethod:: ValueQuery.match_duration_value

   .. autoattribute:: ValueQuery.duration_value_terms

   .. automethod:: ValueQuery.match_heading_value

   .. autoattribute:: ValueQuery.heading_value_terms

   .. automethod:: ValueQuery.match_id_value

   .. autoattribute:: ValueQuery.id_value_terms

   .. automethod:: ValueQuery.match_integer_value

   .. autoattribute:: ValueQuery.integer_value_terms

   .. automethod:: ValueQuery.match_spatial_unit_value

   .. autoattribute:: ValueQuery.spatial_unit_value_terms

   .. automethod:: ValueQuery.match_speed_value

   .. autoattribute:: ValueQuery.speed_value_terms

   .. automethod:: ValueQuery.match_string_value

   .. autoattribute:: ValueQuery.string_value_terms

   .. automethod:: ValueQuery.match_time_value

   .. autoattribute:: ValueQuery.time_value_terms

   .. automethod:: ValueQuery.match_type_value

   .. autoattribute:: ValueQuery.type_value_terms

   .. automethod:: ValueQuery.match_version_value

   .. autoattribute:: ValueQuery.version_value_terms

   .. automethod:: ValueQuery.match_object_value_type

   .. autoattribute:: ValueQuery.object_value_type_terms

   .. automethod:: ValueQuery.match_object_value

   .. autoattribute:: ValueQuery.object_value_terms

   .. automethod:: ValueQuery.match_parameter_id

   .. autoattribute:: ValueQuery.parameter_id_terms

   .. automethod:: ValueQuery.supports_parameter_query

   .. autoattribute:: ValueQuery.parameter_query

   .. autoattribute:: ValueQuery.parameter_terms

   .. automethod:: ValueQuery.match_configuration_id

   .. autoattribute:: ValueQuery.configuration_id_terms

   .. automethod:: ValueQuery.supports_configuration_query

   .. autoattribute:: ValueQuery.configuration_query

   .. autoattribute:: ValueQuery.configuration_terms

   .. automethod:: ValueQuery.get_value_query_record



Configuration Query
-------------------

.. autoclass:: ConfigurationQuery
   :show-inheritance:

   .. automethod:: ConfigurationQuery.match_registry

   .. autoattribute:: ConfigurationQuery.registry_terms

   .. automethod:: ConfigurationQuery.match_parameter_id

   .. autoattribute:: ConfigurationQuery.parameter_id_terms

   .. automethod:: ConfigurationQuery.supports_parameter_query

   .. autoattribute:: ConfigurationQuery.parameter_query

   .. automethod:: ConfigurationQuery.match_any_parameter

   .. autoattribute:: ConfigurationQuery.parameter_terms

   .. automethod:: ConfigurationQuery.match_ancestor_configuration_id

   .. autoattribute:: ConfigurationQuery.ancestor_configuration_id_terms

   .. automethod:: ConfigurationQuery.supports_ancestor_configuration_query

   .. autoattribute:: ConfigurationQuery.ancestor_configuration_query

   .. automethod:: ConfigurationQuery.match_any_ancestor_configuration

   .. autoattribute:: ConfigurationQuery.ancestor_configuration_terms

   .. automethod:: ConfigurationQuery.match_descendant_configuration_id

   .. autoattribute:: ConfigurationQuery.descendant_configuration_id_terms

   .. automethod:: ConfigurationQuery.supports_descendant_configuration_query

   .. autoattribute:: ConfigurationQuery.descendant_configuration_query

   .. automethod:: ConfigurationQuery.match_any_descendant_configuration

   .. autoattribute:: ConfigurationQuery.descendant_configuration_terms

   .. automethod:: ConfigurationQuery.get_configuration_query_record



