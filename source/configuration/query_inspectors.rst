.. currentmodule:: dlkit.configuration.query_inspectors
.. automodule:: dlkit.configuration.query_inspectors

Query_Inspectors
================


Parameter Query Inspector
-------------------------

.. autoclass:: ParameterQueryInspector
   :show-inheritance:

   .. autoattribute:: ParameterQueryInspector.value_syntax_terms

   .. autoattribute:: ParameterQueryInspector.value_coordinate_type_terms

   .. autoattribute:: ParameterQueryInspector.value_heading_type_terms

   .. autoattribute:: ParameterQueryInspector.value_object_type_terms

   .. autoattribute:: ParameterQueryInspector.value_spatial_unit_record_type_terms

   .. autoattribute:: ParameterQueryInspector.value_version_scheme_terms

   .. autoattribute:: ParameterQueryInspector.value_terms

   .. autoattribute:: ParameterQueryInspector.values_shuffled_terms

   .. autoattribute:: ParameterQueryInspector.configuration_id_terms

   .. autoattribute:: ParameterQueryInspector.configuration_terms

   .. automethod:: ParameterQueryInspector.get_parameter_query_inspector_record



Value Query Inspector
---------------------

.. autoclass:: ValueQueryInspector
   :show-inheritance:

   .. autoattribute:: ValueQueryInspector.priority_terms

   .. autoattribute:: ValueQueryInspector.boolean_value_terms

   .. autoattribute:: ValueQueryInspector.bytes_value_terms

   .. autoattribute:: ValueQueryInspector.cardinal_value_terms

   .. autoattribute:: ValueQueryInspector.coordinate_value_terms

   .. autoattribute:: ValueQueryInspector.currency_value_terms

   .. autoattribute:: ValueQueryInspector.date_time_value_terms

   .. autoattribute:: ValueQueryInspector.decimal_value_terms

   .. autoattribute:: ValueQueryInspector.distance_value_terms

   .. autoattribute:: ValueQueryInspector.duration_value_terms

   .. autoattribute:: ValueQueryInspector.heading_value_terms

   .. autoattribute:: ValueQueryInspector.id_value_terms

   .. autoattribute:: ValueQueryInspector.integer_value_terms

   .. autoattribute:: ValueQueryInspector.spatial_unit_value_terms

   .. autoattribute:: ValueQueryInspector.speed_value_terms

   .. autoattribute:: ValueQueryInspector.string_value_terms

   .. autoattribute:: ValueQueryInspector.time_value_terms

   .. autoattribute:: ValueQueryInspector.type_value_terms

   .. autoattribute:: ValueQueryInspector.version_value_terms

   .. autoattribute:: ValueQueryInspector.object_value_type_terms

   .. autoattribute:: ValueQueryInspector.object_value_terms

   .. autoattribute:: ValueQueryInspector.parameter_id_terms

   .. autoattribute:: ValueQueryInspector.parameter_terms

   .. autoattribute:: ValueQueryInspector.configuration_id_terms

   .. autoattribute:: ValueQueryInspector.configuration_terms

   .. automethod:: ValueQueryInspector.get_value_query_inspector_record



Configuration Query Inspector
-----------------------------

.. autoclass:: ConfigurationQueryInspector
   :show-inheritance:

   .. autoattribute:: ConfigurationQueryInspector.registry_terms

   .. autoattribute:: ConfigurationQueryInspector.parameter_id_terms

   .. autoattribute:: ConfigurationQueryInspector.parameter_terms

   .. autoattribute:: ConfigurationQueryInspector.ancestor_configuration_id_terms

   .. autoattribute:: ConfigurationQueryInspector.ancestor_configuration_terms

   .. autoattribute:: ConfigurationQueryInspector.descendant_configuration_id_terms

   .. autoattribute:: ConfigurationQueryInspector.descendant_configuration_terms

   .. automethod:: ConfigurationQueryInspector.get_configuration_query_inspector_record



