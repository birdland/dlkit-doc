.. currentmodule:: dlkit.configuration.objects
.. automodule:: dlkit.configuration.objects

Objects
=======


Parameter
---------

.. autoclass:: Parameter
   :show-inheritance:

   .. autoattribute:: Parameter.value_syntax

   .. autoattribute:: Parameter.value_coordinate_type

   .. automethod:: Parameter.implements_value_coordinate_type

   .. autoattribute:: Parameter.value_heading_type

   .. automethod:: Parameter.implements_value_heading_type

   .. autoattribute:: Parameter.value_object_type

   .. automethod:: Parameter.implements_value_object_type

   .. autoattribute:: Parameter.value_spatial_unit_record_type

   .. automethod:: Parameter.implements_value_spatial_unit_record_type

   .. autoattribute:: Parameter.value_version_scheme

   .. automethod:: Parameter.implements_value_version_scheme

   .. automethod:: Parameter.are_values_shuffled

   .. automethod:: Parameter.get_parameter_record



Parameter Form
--------------

.. autoclass:: ParameterForm
   :show-inheritance:

   .. autoattribute:: ParameterForm.value_syntax_metadata

   .. autoattribute:: ParameterForm.value_syntax

   .. autoattribute:: ParameterForm.value_coordinate_type_metadata

   .. autoattribute:: ParameterForm.value_coordinate_type

   .. autoattribute:: ParameterForm.value_heading_type_metadata

   .. autoattribute:: ParameterForm.value_heading_type

   .. autoattribute:: ParameterForm.value_object_type_metadata

   .. autoattribute:: ParameterForm.value_object_type

   .. autoattribute:: ParameterForm.value_spatial_unit_record_type_metadata

   .. autoattribute:: ParameterForm.value_spatial_unit_record_type

   .. autoattribute:: ParameterForm.value_version_scheme_metadata

   .. autoattribute:: ParameterForm.value_version_scheme

   .. autoattribute:: ParameterForm.values_shuffled_metadata

   .. autoattribute:: ParameterForm.values_shuffled

   .. automethod:: ParameterForm.get_parameter_form_record



Parameter List
--------------

.. autoclass:: ParameterList
   :show-inheritance:

   .. autoattribute:: ParameterList.next_parameter

   .. automethod:: ParameterList.get_next_parameters



Value
-----

.. autoclass:: Value
   :show-inheritance:

   .. autoattribute:: Value.parameter_id

   .. autoattribute:: Value.parameter

   .. autoattribute:: Value.priority

   .. autoattribute:: Value.boolean_value

   .. autoattribute:: Value.bytes_value

   .. autoattribute:: Value.cardinal_value

   .. autoattribute:: Value.coordinate_value

   .. autoattribute:: Value.currency_value

   .. autoattribute:: Value.date_time_value

   .. autoattribute:: Value.decimal_value

   .. autoattribute:: Value.distance_value

   .. autoattribute:: Value.duration_value

   .. autoattribute:: Value.heading_value

   .. autoattribute:: Value.id_value

   .. autoattribute:: Value.integer_value

   .. autoattribute:: Value.object_value

   .. autoattribute:: Value.spatial_unit_value

   .. autoattribute:: Value.speed_value

   .. autoattribute:: Value.string_value

   .. autoattribute:: Value.time_value

   .. autoattribute:: Value.type_value

   .. autoattribute:: Value.version_value

   .. automethod:: Value.get_value_record



Value Form
----------

.. autoclass:: ValueForm
   :show-inheritance:

   .. autoattribute:: ValueForm.priority_metadata

   .. autoattribute:: ValueForm.priority

   .. autoattribute:: ValueForm.boolean_value_metadata

   .. autoattribute:: ValueForm.boolean_value

   .. autoattribute:: ValueForm.byte_value_metadata

   .. autoattribute:: ValueForm.bytes_value

   .. autoattribute:: ValueForm.cardinal_value_metadata

   .. autoattribute:: ValueForm.cardinal_value

   .. autoattribute:: ValueForm.coordinate_value_metadata

   .. autoattribute:: ValueForm.coordinate_value

   .. autoattribute:: ValueForm.currency_value_metadata

   .. autoattribute:: ValueForm.currency_value

   .. autoattribute:: ValueForm.date_time_value_metadata

   .. autoattribute:: ValueForm.date_time_value

   .. autoattribute:: ValueForm.decimal_value_metadata

   .. autoattribute:: ValueForm.decimal_value

   .. autoattribute:: ValueForm.distance_value_metadata

   .. autoattribute:: ValueForm.distance_value

   .. autoattribute:: ValueForm.duration_value_metadata

   .. autoattribute:: ValueForm.duration_value

   .. autoattribute:: ValueForm.id_value_metadata

   .. autoattribute:: ValueForm.id_value

   .. autoattribute:: ValueForm.integer_value_metadata

   .. autoattribute:: ValueForm.integer_value

   .. autoattribute:: ValueForm.spatial_unit_value_metadata

   .. autoattribute:: ValueForm.spatial_unit_value

   .. autoattribute:: ValueForm.speed_value_metadata

   .. autoattribute:: ValueForm.speed_value

   .. autoattribute:: ValueForm.string_value_metadata

   .. autoattribute:: ValueForm.string_value

   .. autoattribute:: ValueForm.time_value_metadata

   .. autoattribute:: ValueForm.time_value

   .. autoattribute:: ValueForm.type_value_metadata

   .. autoattribute:: ValueForm.type_value

   .. autoattribute:: ValueForm.version_value_metadata

   .. autoattribute:: ValueForm.version_value

   .. autoattribute:: ValueForm.object_value_metadata

   .. automethod:: ValueForm.set_object_value

   .. autoattribute:: ValueForm.value

   .. automethod:: ValueForm.get_value_form_record



Value List
----------

.. autoclass:: ValueList
   :show-inheritance:

   .. autoattribute:: ValueList.next_value

   .. automethod:: ValueList.get_next_values



Configuration Form
------------------

.. autoclass:: ConfigurationForm
   :show-inheritance:

   .. autoattribute:: ConfigurationForm.registry_metadata

   .. autoattribute:: ConfigurationForm.registry

   .. automethod:: ConfigurationForm.get_configuration_form_record



Configuration List
------------------

.. autoclass:: ConfigurationList
   :show-inheritance:

   .. autoattribute:: ConfigurationList.next_configuration

   .. automethod:: ConfigurationList.get_next_configurations



Configuration Node
------------------

.. autoclass:: ConfigurationNode
   :show-inheritance:

   .. autoattribute:: ConfigurationNode.configuration

   .. autoattribute:: ConfigurationNode.parent_configuration_nodes

   .. autoattribute:: ConfigurationNode.child_configuration_nodes



Configuration Node List
-----------------------

.. autoclass:: ConfigurationNodeList
   :show-inheritance:

   .. autoattribute:: ConfigurationNodeList.next_configuration_node

   .. automethod:: ConfigurationNodeList.get_next_configuration_nodes



