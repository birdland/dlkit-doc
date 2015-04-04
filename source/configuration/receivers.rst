.. currentmodule:: dlkit.configuration.receivers
.. automodule:: dlkit.configuration.receivers

Receivers
=========


Parameter Receiver
------------------

.. autoclass:: ParameterReceiver
   :show-inheritance:

   .. automethod:: ParameterReceiver.new_parameter

   .. automethod:: ParameterReceiver.changed_parameter

   .. automethod:: ParameterReceiver.deleted_parameter



Value Receiver
--------------

.. autoclass:: ValueReceiver
   :show-inheritance:

   .. automethod:: ValueReceiver.new_value

   .. automethod:: ValueReceiver.changed_value

   .. automethod:: ValueReceiver.deleted_value



Configuration Receiver
----------------------

.. autoclass:: ConfigurationReceiver
   :show-inheritance:

   .. automethod:: ConfigurationReceiver.new_configuration

   .. automethod:: ConfigurationReceiver.new_ancestor_configuration

   .. automethod:: ConfigurationReceiver.new_descendant_configuration

   .. automethod:: ConfigurationReceiver.changed_configuration

   .. automethod:: ConfigurationReceiver.deleted_configuration

   .. automethod:: ConfigurationReceiver.deleted_ancestor_configuration

   .. automethod:: ConfigurationReceiver.deleted_descendant_configuration



