# -*- coding: utf-8 -*-
"""Configuration Open Service Interface Definitions
configuration version 3.0.0

The Configuration OSID defines a set of interfaces for configuration
retrieval and management. The Configuration service may be used to store
user profiles or as a means to assist OSID implementors modularize
configuration data.

Parameters

Configuration data is expressed through a set of ``Parameters and
Values``. A ``Parameter`` is an ``OsidRule`` with a unique ``Id`` and a
syntax that indicates a primitive type. A ``Parameter`` may map to zero
or more Values of the same syntax. An application requesting a
configuration looks up ``Values`` given a ``Parameter``  ``Id`` through
a ``ValueLookupSession``.

As an ``OsidRule`` , ``Parameters`` may resolve to implicitly created
``Values`` based on external rule evaluations.

Values

``Values`` represent primitive types that are assigned to ``Parameters``
and constrained by the syntax specified in its ``Parameter``. In the
most basic case, a single ``Value`` is created for a ``Parameter`` and
returned when the ``Parameter`` is resolved. ``Parameters`` can have
multiple ``Values`` where the Configuration OSID Consumer can request
all ``Values,`` or a single ``Value`` selected by the OSID Provider.

``Values`` are ``Operable`` such that Values in multi-valued
``Parameter`` may be enabled or disabled manually or based on a rule.
For example, the configuration of a service may change based on time of
day or may change based on some out-of-band context. ``Value``
retrievals in the ``ValueRetrievalSession`` support passing of a
``ValueCondition`` to supply contextual information to feed the rule
evaluation.

Configuration Cataloging

To create a configuration for an application, a ``Configuration`` object
is created. The ``Configuration`` maps a set of ``Parameters`` and their
``Values``. A ``Configuration`` may be positioned as a child of another
``Configuration`` to inherit its ``Parameters`` and ``Values``. The
desired ``Parameters`` are then mapped to the ``Configuration`` and
``Values`` assigned.

``Parameters`` may be stored without values in separate
``Configurations`` for reuse or standardization.

OSID Provider implementations should get their configurations via the
``OsidRuntimeManager``.

Sub Packages

The Configuration OSID includes a rules subpackage for governing the
available ``Values`` for a ``Parameter`` based on a set of rules and an
Configuration Batch OSID for managing parameters and values in bulk.

Example
  Id parameterId = what I'm looking for;
  
  ValueLookupSession valueSession = mgr.getValueLookupSession();
  valueSession.federateParameterView();
  
  if (valueSession.parameterExists(parameterId)) {
      Parameter param = valueSession.getParameter(parameterId);
      ValueList values = valueSession.getValues(param.getId());
      while (values.hasNext()) {
          Value value = values.getNextValue();
          if (param.implementsType(typeString)
              String value = (String) param.getValue();
          else 
              print "unexpected type";
      }
  }





"""
from ..osid import managers as osid_managers
from .osid_errors import Unimplemented, IllegalState, OperationFailed
from ..osid import sessions as osid_sessions
from ..osid import objects as osid_objects


class ConfigurationProfile(osid_managers.OsidProfile):

    def supports_visible_federation(self):
        """Tests if federation is visible for this service.

        :return: ``true`` if visible federation is supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_value_retrieval(self):
        """Tests for the availability of a configuration value retrieval service.

        :return: ``true`` if value retrieval is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_value_lookup(self):
        """Tests for the availability of a configuration value lookup service.

        :return: ``true`` if value lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_value_query(self):
        """Tests for the availability of a configuration value query service.

        :return: ``true`` if value query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_value_search(self):
        """Tests for the availability of a configuration value search service.

        :return: ``true`` if value search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_value_admin(self):
        """Tests for the availability of a configuration value administration service.

        :return: ``true`` if value administration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_value_notification(self):
        """Tests for the availability of a configuration value notification service.

        :return: ``true`` if value notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_parameter_lookup(self):
        """Tests for the availability of a parameter lookup service.

        :return: ``true`` if parameter lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_parameter_query(self):
        """Tests for the availability of a parameter query service.

        :return: ``true`` if parameter query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_parameter_search(self):
        """Tests for the availability of a parameter search service.

        :return: ``true`` if parameter search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_parameter_admin(self):
        """Tests for the availability of a parameter update service.

        :return: ``true`` if parameter update is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_parameter_notification(self):
        """Tests for the availability of a parameter notification service.

        :return: ``true`` if parameter notification is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_parameter_configuration(self):
        """Tests for the availability of a service to lookup mappings of parameters to configurations.

        :return: ``true`` if parameter configuration is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_parameter_configuration_assignment(self):
        """Tests for the availability of a service to map parameters to configurations.

        :return: ``true`` if parameter configuration assignment is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_parameter_smart_configuration(self):
        """Tests for the availability of a parameter smart configuration service.

        :return: ``true`` if parameter smart configuration service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_lookup(self):
        """Tests for the availability of a configuration lookup service.

        :return: ``true`` if configuration lookup is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_query(self):
        """Tests for the availability of a configuration query service.

        :return: ``true`` if configuration query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_search(self):
        """Tests for the availability of a configuration search service.

        :return: ``true`` if configuration search is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_admin(self):
        """Tests for the availability of a configuration admin service.

        :return: ``true`` if configuration admin is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_notification(self):
        """Tests for the availability of a notification service for subscribing to changes to configurations.

        :return: ``true`` if a configuration notification service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_hierarchy(self):
        """Tests for the availability of a configuration hierarchy traversal service.

        :return: ``true`` if a configuration hierarchy traversal is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_hierarchy_design(self):
        """Tests for the availability of a configuration hierarchy design service.

        :return: ``true`` if a configuration hierarchy design is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_batch(self):
        """Tests for the availability of a configuration batch service.

        :return: ``true`` if a configuration batch service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def supports_configuration_rules(self):
        """Tests for the availability of a configuration rules service.

        :return: ``true`` if a configuration rules service is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_value_condition_record_types(self):
        """Gets the supported value condition record types.

        :return: a list containing the supported ``ValueCondition`` record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    value_condition_record_types = property(fget=get_value_condition_record_types)

    def supports_value_condition_record_type(self, value_condition_record_type):
        """Tests if the given ``ValueCondition`` record type is supported.

        :param value_condition_record_type: a ``Type`` indicating a ``ValueCondition`` record type
        :type value_condition_record_type: ``osid.type.Type``
        :return: ``true`` if the given value condition record ``Type`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``value_condition_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_value_record_types(self):
        """Gets all the value record types supported.

        :return: the list of supported value record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    value_record_types = property(fget=get_value_record_types)

    def supports_value_record_type(self, value_record_type):
        """Tests if a given value record type is supported.

        :param value_record_type: the value record type
        :type value_record_type: ``osid.type.Type``
        :return: ``true`` if the value record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_value_search_record_types(self):
        """Gets all the value search record types supported.

        :return: the list of supported value search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    value_search_record_types = property(fget=get_value_search_record_types)

    def supports_value_search_record_type(self, value_search_record_type):
        """Tests if a given value search type is supported.

        :param value_search_record_type: the value search record type
        :type value_search_record_type: ``osid.type.Type``
        :return: ``true`` if the value search record type is supported ``,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``value_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_parameter_record_types(self):
        """Gets all the parameter record types supported.

        :return: the list of supported parameter record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    parameter_record_types = property(fget=get_parameter_record_types)

    def supports_parameter_record_type(self, parameter_record_type):
        """Tests if a given parameter record type is supported.

        :param parameter_record_type: a parameter record type
        :type parameter_record_type: ``osid.type.Type``
        :return: ``true`` if the parameter record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_parameter_search_record_types(self):
        """Gets all the parameter search record types supported.

        :return: the list of supported parameter search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    parameter_search_record_types = property(fget=get_parameter_search_record_types)

    def supports_parameter_search_record_type(self, parameter_search_record_type):
        """Tests if a given parameter search record type is supported.

        :param parameter_search_record_type: the value search type
        :type parameter_search_record_type: ``osid.type.Type``
        :return: ``true`` if the parameter search record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``parameter_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_configuration_record_types(self):
        """Gets all the configuration record types supported.

        :return: the list of supported configuration record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    configuration_record_types = property(fget=get_configuration_record_types)

    def supports_configuration_record_type(self, configuration_record_type):
        """Tests if a given configuration record type is supported.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: ``true`` if the configuration record type is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_configuration_search_record_types(self):
        """Gets all the configuration search record types supported.

        :return: the list of supported configuration search record types
        :rtype: ``osid.type.TypeList``

        """
        raise UNIMPLEMENTED()

    configuration_search_record_types = property(fget=get_configuration_search_record_types)

    def supports_configuration_search_record_type(self, configuration_search_record_type):
        """Tests if a given configuration search record type is supported.

        :param configuration_search_record_type: the configuration search record type
        :type configuration_search_record_type: ``osid.type.Type``
        :return: ``true`` if the configuration search record type is support ``e`` d, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_search_record_type`` is ``null``

        """
        raise UNIMPLEMENTED()



class ConfigurationManager(osid_managers.OsidManager, osid_sessions.OsidSession, ConfigurationProfile):

    def get_value_retrieval_session(self):
        """Gets a configuration value retrieval session.

        :return: a ``ValueRetrievalSession``
        :rtype: ``osid.configuration.ValueRetrievalSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_retrieval()`` is ``false``

        """
        raise UNIMPLEMENTED()

    value_retrieval_session = property(fget=get_value_retrieval_session)

    def get_value_retrieval_session_for_configuration(self, configuration_id):
        """Gets a configuration value retrieval session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueRetrievalSession``
        :rtype: ``osid.configuration.ValueRetrievalSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_retrieval()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_lookup_session(self):
        """Gets a configuration value lookup session.

        :return: a ``ValueLookupSession``
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    value_lookup_session = property(fget=get_value_lookup_session)

    def get_value_lookup_session_for_configuration(self, configuration_id):
        """Gets a configuration value lookup session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueLookupSession``
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_query_session(self):
        """Gets a configuration value query session.

        :return: a ``ValueQuerySession``
        :rtype: ``osid.configuration.ValueQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    value_query_session = property(fget=get_value_query_session)

    def get_value_query_session_for_configuration(self, configuration_id):
        """Gets a configuration value query session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueQuerySession``
        :rtype: ``osid.configuration.ValueQuerySession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_search_session(self):
        """Gets a configuration value search session.

        :return: a ``ValueSearchSession``
        :rtype: ``osid.configuration.ValueSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    value_search_session = property(fget=get_value_search_session)

    def get_value_search_session_for_configuration(self, configuration_id):
        """Gets a configuration value search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueSearchSession``
        :rtype: ``osid.configuration.ValueSearchSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_admin_session(self):
        """Gets a configuration value administration session.

        :return: a ``ValueAdminSession``
        :rtype: ``osid.configuration.ValueAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    value_admin_session = property(fget=get_value_admin_session)

    def get_value_admin_session_for_configuration(self, configuration_id):
        """Gets a value administration session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueAdminSession``
        :rtype: ``osid.configuration.ValueAdminSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- ``supports_value_admin()`` or ``supports_visible_federation()`` is ``false``
        :raise: ``Unimplemented`` -- ``supports_value_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_notification_session(self, value_receiver):
        """Gets a value notification session.

        :param value_receiver: the notification callback
        :type value_receiver: ``osid.configuration.ValueReceiver``
        :return: a ``ValueNotificationSession``
        :rtype: ``osid.configuration.ValueNotificationSession``
        :raise: ``NullArgument`` -- ``value_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_notification_session_for_configuration(self, value_receiver, configuration_id):
        """Gets a value notification session using the specified configuration.

        :param value_receiver: the notification callback
        :type value_receiver: ``osid.configuration.ValueReceiver``
        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ValueNotificationSession``
        :rtype: ``osid.configuration.ValueNotificationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``value_receiver`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_lookup_session(self):
        """Gets a parameter lookup session.

        :return: a ``ParameterLookupSession``
        :rtype: ``osid.configuration.ParameterLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    parameter_lookup_session = property(fget=get_parameter_lookup_session)

    def get_parameter_lookup_session_for_configuration(self, configuration_id):
        """Gets a parameter lookup session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParamaterLookupSession``
        :rtype: ``osid.configuration.ParameterLookupSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_lookup()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_query_session(self):
        """Gets a parameter query session.

        :return: a ``ParameterQuerySession``
        :rtype: ``osid.configuration.ParameterQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    parameter_query_session = property(fget=get_parameter_query_session)

    def get_parameter_query_session_for_configuration(self, configuration_id):
        """Gets a parameter search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParamaterQuerySession``
        :rtype: ``osid.configuration.ParameterQuerySession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_query()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_search_session(self):
        """Gets a parameter search session.

        :return: a ``ParameterSearchSession``
        :rtype: ``osid.configuration.ParameterSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    parameter_search_session = property(fget=get_parameter_search_session)

    def get_parameter_search_session_for_configuration(self, configuration_id):
        """Gets a parameter search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParamaterSearchSession``
        :rtype: ``osid.configuration.ParameterSearchSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_admin_session(self):
        """Gets a parameter administration session.

        :return: a ``ParameterAdminSession``
        :rtype: ``osid.configuration.ParameterAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    parameter_admin_session = property(fget=get_parameter_admin_session)

    def get_parameter_admin_session_for_configuration(self, configuration_id):
        """Gets a parameter administration session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParameterAdminSession``
        :rtype: ``osid.configuration.ParameterAdminSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_notification_session(self, parameter_receiver):
        """Gets a parameter notification session.

        :param parameter_receiver: the notification callback
        :type parameter_receiver: ``osid.configuration.ParameterReceiver``
        :return: a ``ParameterNotificationSession``
        :rtype: ``osid.configuration.ParameterNotificationSession``
        :raise: ``NullArgument`` -- ``parameter_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_notification_session_for_configuration(self, parameter_receiver, configuration_id):
        """Gets a parameter notification session using the specified configuration.

        :param parameter_receiver: the notification callback
        :type parameter_receiver: ``osid.configuration.ParameterReceiver``
        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParameterNotificationSession``
        :rtype: ``osid.configuration.ParameterNotificationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_receiver`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_configuration_session(self):
        """Gets a session for looking up mappings of parameters to configurations.

        :return: a ``ParameterConfigurationSession``
        :rtype: ``osid.configuration.ParameterConfigurationSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_configuration()`` is ``false``

        """
        raise UNIMPLEMENTED()

    parameter_configuration_session = property(fget=get_parameter_configuration_session)

    def get_parameter_configuration_assignment_session(self):
        """Gets a session for managing mappings of parameters to configurations.

        :return: a ``ParameterConfigurationAssignmentSession``
        :rtype: ``osid.configuration.ParameterConfigurationAssignmentSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_configuration_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    parameter_configuration_assignment_session = property(fget=get_parameter_configuration_assignment_session)

    def get_parameter_smart_configuration_session(self, configuration_id):
        """Gets a session for managing smart configurations.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :return: a ``ParameterSmartConfigurationSession``
        :rtype: ``osid.configuration.ParameterSmartConfigurationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_smart_configuration()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_lookup_session(self):
        """Gets a configuration lookup session.

        :return: a ``ConfigurationLookupSession``
        :rtype: ``osid.configuration.ConfigurationLookupSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_lookup_session = property(fget=get_configuration_lookup_session)

    def get_configuration_query_session(self):
        """Gets a configuration query session.

        :return: a ``ConfigurationQuerySession``
        :rtype: ``osid.configuration.ConfigurationQuerySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_query_session = property(fget=get_configuration_query_session)

    def get_configuration_search_session(self):
        """Gets a configuration search session.

        :return: a ``ConfigurationSearchSession``
        :rtype: ``osid.configuration.ConfigurationSearchSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_search_session = property(fget=get_configuration_search_session)

    def get_configuration_admin_session(self):
        """Gets a configuration administration session.

        :return: a ``ConfigurationAdminSession``
        :rtype: ``osid.configuration.ConfigurationAdminSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_admin_session = property(fget=get_configuration_admin_session)

    def get_configuration_notification_session(self, configuration_receiver):
        """Gets the notification session for subscribing to changes to configurations.

        :param configuration_receiver: the notification callback
        :type configuration_receiver: ``osid.configuration.ConfigurationReceiver``
        :return: a ``ConfigurationNotificationSession``
        :rtype: ``osid.configuration.ConfigurationNotificationSession``
        :raise: ``NullArgument`` -- ``configuration_receiver`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_hierarchy_session(self):
        """Gets a hierarchy traversal service for configurations.

        :return: a ``ConfigurationHierarchySession``
        :rtype: ``osid.configuration.ConfigurationHierarchySession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_hierarchy_session = property(fget=get_configuration_hierarchy_session)

    def get_configuration_hierarchy_design_session(self):
        """Gets a hierarchy design service for configurations.

        :return: a ``ConfigurationHierarchyDesignSession``
        :rtype: ``osid.configuration.ConfigurationHierarchyDesignSession``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_hierarchy_design_session = property(fget=get_configuration_hierarchy_design_session)

    def get_configuration_batch_manager(self):
        """Gets a ``ConfigurationBatchManager``.

        :return: a ``ConfigurationBatchManager``
        :rtype: ``osid.configuration.batch.ConfigurationBatchManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_batch_manager = property(fget=get_configuration_batch_manager)

    def get_configuration_rules_manager(self):
        """Gets a ``ConfigurationRulesManager``.

        :return: a ``ConfigurationRulesManager``
        :rtype: ``osid.configuration.rules.ConfigurationRulesManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_rules_manager = property(fget=get_configuration_rules_manager)


##
# The following methods are from osid.configuration.ConfigurationLookupSession

    def can_lookup_configurations(self):
        """Tests if this user can perform ``Configuration`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_configuration_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_configuration_view(self):
        """A complete view of the ``Configuration`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def get_configuration(self, configuration_id):
        """Gets the ``Configuration`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Configuration`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Configuration`` and
        retained for compatibility.

        :param configuration_id: the ``Id`` of the ``Configuration`` to retrieve
        :type configuration_id: ``osid.id.Id``
        :return: the ``Configuration``
        :rtype: ``osid.configuration.Configuration``
        :raise: ``NotFound`` -- no ``Configuration`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_ids(self, configuration_ids):
        """Gets a ``ConfigurationList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        configurations specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Configurations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.

        :param configuration_ids: the list of ``Ids`` to retrieve
        :type configuration_ids: ``osid.id.IdList``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_genus_type(self, configuration_genus_type):
        """Gets an ``ConfigurationList`` corresponding to the given configuration genus ``Type`` which does not include configuration types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.

        :param configuration_genus_type: a configuration genus type
        :type configuration_genus_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_parent_genus_type(self, configuration_genus_type):
        """Gets an ``ConfigurationList`` corresponding to the given configuration genus ``Type`` and include any additional configurations with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.

        :param configuration_genus_type: a configuration genus type
        :type configuration_genus_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_record_type(self, configuration_record_type):
        """Gets a ``ConfigurationList`` containing the given configuration record ``Type``.
        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.

        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_provider(self, resource_id):
        """Gets a ``ConfigurationList`` from the given provider ````.
        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations(self):
        """Gets all ``Configurations,`` In plenary mode, the returned list contains all known configurations or an error results.
        Otherwise, the returned list may contain only those
        configurations that are accessible through this session.

        :return: a list of ``Configurations``
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    configurations = property(fget=get_configurations)


##
# The following methods are from osid.configuration.ConfigurationQuerySession

    def can_search_configurations(self):
        """Tests if this user can perform ``Configuration`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_configuration_query(self):
        """Gets a configuration query.

        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``

        """
        raise UNIMPLEMENTED()

    configuration_query = property(fget=get_configuration_query)

    def get_configurations_by_query(self, configuration_query):
        """Gets a list of ``Configurations`` matching the given search.

        :param configuration_query: the configuration query
        :type configuration_query: ``osid.configuration.ConfigurationQuery``
        :return: the returned ``ConfigurationList``
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationSearchSession

    def get_configuration_search(self):
        """Gets a configuration search.

        :return: the configuration search
        :rtype: ``osid.configuration.ConfigurationSearch``

        """
        raise UNIMPLEMENTED()

    configuration_search = property(fget=get_configuration_search)

    def get_configuration_search_order(self):
        """Gets a log search order.
        The ``ConfigurationSearchOrder`` is supplied to a
        ``ConfigurationSearch`` to specify the ordering of results.

        :return: the configuration search order
        :rtype: ``osid.configuration.ConfigurationSearchOrder``

        """
        raise UNIMPLEMENTED()

    configuration_search_order = property(fget=get_configuration_search_order)

    def get_configurations_by_search(self, configuration_query, configuration_search):
        """Gets a list of ``Configurations`` matching the given search.
        Each element in the array is OR'd.

        :param configuration_query: the configuration query
        :type configuration_query: ``osid.configuration.ConfigurationQuery``
        :param configuration_search: the configuration search
        :type configuration_search: ``osid.configuration.ConfigurationSearch``
        :return: the configuration search results
        :rtype: ``osid.configuration.ConfigurationSearchResults``
        :raise: ``NullArgument`` -- ``configuration_query`` or ``configuration_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_query`` or ``configuration_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_configuration_query_from_inspector(self, configuration_query_inspector):
        """Gets a configuration query from an inspector.
        The inspector is available from a
        ``ConfigurationSearchResults``.

        :param configuration_query_inspector: a configuration query inspector
        :type configuration_query_inspector: ``osid.configuration.ConfigurationQueryInspector``
        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``
        :raise: ``NullArgument`` -- ``configuration_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``configuration_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationAdminSession

    def can_create_configurations(self):
        """Tests if this user can create ``Configurations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a C
        ``onfiguration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Configuration`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_configuration_with_record_types(self, configuration_record_types):
        """Tests if this user can create a single ``Configuration`` using the desired record types.
        While ``ConfigurationManager.getConfigurationRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Configuration``. Providing an empty array tests if a
        ``Configuration`` can be created with no records.

        :param configuration_record_types: array of configuration record types
        :type configuration_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Configuration`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_configuration_form_for_create(self, configuration_record_types):
        """Gets the configuration form for creating new configurations.
        A new form should be requested for each create transaction.

        :param configuration_record_types: array of configuration record types
        :type configuration_record_types: ``osid.type.Type[]``
        :return: the configuration form
        :rtype: ``osid.configuration.ConfigurationForm``
        :raise: ``NullArgument`` -- ``configuration_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_configuration(self, configuration_form):
        """Creates a new ``Configuration``.

        :param configuration_form: the configuration form
        :type configuration_form: ``osid.configuration.ConfigurationForm``
        :return: the new ``Configuration``
        :rtype: ``osid.configuration.Configuration``
        :raise: ``IllegalState`` -- ``configuration_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``configuration_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_form`` did not originate from ``get_configuration_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_configurations(self):
        """Tests if this user can update ``Configurations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a C
        ``onfiguration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Configuration`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_configuration_form_for_update(self, configuration_id):
        """Gets the configuration form for updating existing configurations.
        A new configuration form should be requested for each update
        transaction.

        :param configuration_id: ``Id`` of a ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: the configuration form
        :rtype: ``osid.configuration.ConfigurationForm``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_configuration(self, configuration_form):
        """Updates an existing ``Configuration``.

        :param configuration_form: the configuration form
        :type configuration_form: ``osid.configuration.ConfigurationForm``
        :raise: ``IllegalState`` -- ``configuration_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``configuration_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_form`` did not originate from ``get_configuration_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_configurations(self):
        """Tests if this user can delete ``Configurations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Configuration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Configuration`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_configuration(self, configuration_id):
        """Deletes a ``Configuration``.

        :param configuration_id: the ``Id`` of the ``Configuration`` to delete
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_configuration_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Configurations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Configuration`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_configuration(self, configuration_id, alias_id):
        """Adds an ``Id`` to a ``Configuration`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Configuration`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another configuration it is
        reassigned to the given configuration ``Id``.

        :param configuration_id: the ``Id`` of a ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationNotificationSession

    def can_register_for_configuration_notifications(self):
        """Tests if this user can register for ``Configuration`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_configurations(self):
        """Registers for notifications of new configurations.
        ``ConfigurationReceiver.newConfiguration()`` is invoked when a
        new ``Configuration`` is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_configuration_ancestors(self, configuration_id):
        """Registers for notification if an ancestor is added to the specified configuration in the configuration hierarchy.
        ``ConfigurationReceiver.newConfigurationAncestor()`` is invoked
        when the specified configuration experiences an addition in
        ancestry.

        :param configuration_id: the ``Id`` of the configuration to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a configuration was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_configuration_descendants(self, configuration_id):
        """Registers for notification if a descendant is added to the specified configuration in the configuration hierarchy.
        ``ConfigurationReceiver.newConfigurationDescendant()`` is
        invoked when the specified configuration experiences an addition
        in descendants.

        :param configuration_id: the ``Id`` of the configuration to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a configuration was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_configurations(self):
        """Registers for notification of updated configurations.
        ``ConfigurationReceiver.changedConfiguration()`` is invoked when
        a configuration is changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_configuration(self, configuration_id):
        """Registers for notifications of an update to a configuration.
        ``ConfigurationReceiver.changedConfiguration()`` is invoked when
        the specified ``Configuration`` is changed.

        :param configuration_id: the ``Id`` of the ``Configuration`` to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Configuration`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_configurations(self):
        """Registers for notification of deleted configurations.
        ``ConfigurationReceiver.deletedConfiguration()`` is invoked when
        a ``Configuration`` is deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_configuration(self, configuration_id):
        """Registers for notifications of a deleted configuration.
        ``ConfiguratinReceiver.deletedConfiguration()`` is invoked when
        the specified configuration is deleted.

        :param configuration_id: the ``Id`` of the ``Configuration`` to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Configuration`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_configuration_ancestors(self, configuration_id):
        """Registers for notification if an ancestor is removed from the specified configuration in the configuration hierarchy.
        ``ConfigurationReceiver.deletedConfigurationAncestor()`` is
        invoked when the specified configuration experiences a removal
        of an ancestor.

        :param configuration_id: the ``Id`` of the configuration to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a configuration was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_configuration_descendants(self, configuration_id):
        """Registers for notification if a descendant is removed from fthe specified configuration in the configuration hierarchy.
        ``ConfigurationReceiver.deletedConfigurationDescendant()`` is
        invoked when the specified configuration experiences a removal
        of one of its descdendents.

        :param configuration_id: the ``Id`` of the configuration to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a configuration was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationHierarchySession

    def get_configuration_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the configuration ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    configuration_hierarchy_id = property(fget=get_configuration_hierarchy_id)

    def get_configuration_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    configuration_hierarchy = property(fget=get_configuration_hierarchy)

    def can_access_configuration_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_configuration_ids(self):
        """Gets the root configuration ``Ids`` in this hierarchy.

        :return: the root configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_configuration_ids = property(fget=get_root_configuration_ids)

    def get_root_configurations(self):
        """Gets the root configurations in the configuration hierarchy.
        A node with no parents is an orphan. While all configuration
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.

        :return: the root configurations
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_configurations = property(fget=get_root_configurations)

    def has_parent_configurations(self, configuration_id):
        """Tests if the ``Configuration`` has any parents.

        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the configuration has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_configuration(self, id_, configuration_id):
        """Tests if an ``Id`` is a direct parent of configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``configuration_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_configuration_ids(self, configuration_id):
        """Gets the parent ``Ids`` of the given configuration.

        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: the parent Ids of the configuration
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_configurations(self, configuration_id):
        """Gets the parents of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the parents of the configuration
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_configuration(self, id_, configuration_id):
        """Tests if an Id is an ancestor of a configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_configurations(self, configuration_id):
        """Tests if a configuration has any children.

        :param configuration_id: a ``configuration_id``
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``configuration_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_configuration(self, id_, configuration_id):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_configuration_ids(self, configuration_id):
        """Gets the child ``Ids`` of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the children of the configuration
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_configurations(self, configuration_id):
        """Gets the children of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the children of the configuration
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_configuration(self, id_, configuration_id):
        """Tests if an ``Id`` is a descendant of a configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configuration_node_ids(self, configuration_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a configuration node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configuration_nodes(self, configuration_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a configuration node
        :rtype: ``osid.configuration.ConfigurationNode``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationHierarchyDesignSession

    def can_modify_configuration_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_configuration(self, configuration_id):
        """Adds a root configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``configuration_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_configuration(self, configuration_id):
        """Removes a root configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not a root
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_configuration(self, configuration_id, child_id):
        """Adds a child to a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``configuration_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``configuration_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_configuration(self, configuration_id, child_id):
        """Removes a child from a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``configuration_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_configurations(self, configuration_id):
        """Removes all children from a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class ConfigurationProxyManager(osid_managers.OsidProxyManager, ConfigurationProfile):

    def get_value_retrieval_session(self, proxy):
        """Gets a configuration value retrieval session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueRetrievalSession``
        :rtype: ``osid.configuration.ValueRetrievalSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_retrieval()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_retrieval_session_for_configuration(self, configuration_id, proxy):
        """Gets a configuration value retrieval session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueRetrievalSession``
        :rtype: ``osid.configuration.ValueRetrievalSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_retrieval()`` or ``supports_visible_federation()`` is ``False``

        """
        raise UNIMPLEMENTED()

    def get_value_lookup_session(self, proxy):
        """Gets a configuration value lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueLookupSession``
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_lookup_session_for_configuration(self, configuration_id, proxy):
        """Gets a configuration value lookup session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueLookupSession``
        :rtype: ``osid.configuration.ValueLookupSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_lookup()`` or ``supports_visible_federation()`` is ``False``

        """
        raise UNIMPLEMENTED()

    def get_value_query_session(self, proxy):
        """Gets a configuration value query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueQuerySession``
        :rtype: ``osid.configuration.ValueQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_query_session_for_configuration(self, configuration_id, proxy):
        """Gets a configuration value query session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueQuerySession``
        :rtype: ``osid.configuration.ValueQuerySession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_query()`` or ``supports_visible_federation()`` is ``False``

        """
        raise UNIMPLEMENTED()

    def get_value_search_session(self, proxy):
        """Gets a configuration value search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueSearchSession``
        :rtype: ``osid.configuration.ValueSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_search_session_for_configuration(self, configuration_id, proxy):
        """Gets a configuration value search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueSearchSession``
        :rtype: ``osid.configuration.ValueSearchSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` or ``supports_visible_federation()`` is ``False``

        """
        raise UNIMPLEMENTED()

    def get_value_notification_session(self, value_receiver, proxy):
        """Gets a value notification session.

        :param value_receiver: notification callback
        :type value_receiver: ``osid.configuration.ValueReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueNotificationSession``
        :rtype: ``osid.configuration.ValueNotificationSession``
        :raise: ``NullArgument`` -- ``value_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_notification_session_for_configuration(self, value_receiver, configuration_id, proxy):
        """Gets a value notification session using the specified configuration.

        :param value_receiver: notification callback
        :type value_receiver: ``osid.configuration.ValueReceiver``
        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueNotificationSession``
        :rtype: ``osid.configuration.ValueNotificationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``value_receiver, configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_admin_session(self, proxy):
        """Gets a configuration value administration session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueAdminSession``
        :rtype: ``osid.configuration.ValueAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_value_admin_session_for_configuration(self, configuration_id, proxy):
        """Gets a value administration session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ValueAdminSession``
        :rtype: ``osid.configuration.ValueAdminSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_value_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_lookup_session(self, proxy):
        """Gets a parameter lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterLookupSession``
        :rtype: ``osid.configuration.ParameterLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_lookup_session_for_configuration(self, configuration_id, proxy):
        """Gets a parameter lookup session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParamaterLookupSession``
        :rtype: ``osid.configuration.ParameterLookupSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_parameter_query_session(self, proxy):
        """Gets a parameter query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterQuerySession``
        :rtype: ``osid.configuration.ParameterQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_query_session_for_configuration(self, configuration_id, proxy):
        """Gets a parameter query session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParamaterQuerySession``
        :rtype: ``osid.configuration.ParameterQuerySession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_parameter_search_session(self, proxy):
        """Gets a parameter search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterSearchSession``
        :rtype: ``osid.configuration.ParameterSearchSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_search_session_for_configuration(self, configuration_id, proxy):
        """Gets a parameter search session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParamaterSearchSession``
        :rtype: ``osid.configuration.ParameterSearchSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_search()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_admin_session(self, proxy):
        """Gets a parameter administration session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterAdminSession``
        :rtype: ``osid.configuration.ParameterAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_admin_session_for_configuration(self, configuration_id, proxy):
        """Gets a parameter administration session using the supplied configuration.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterAdminSession``
        :rtype: ``osid.configuration.ParameterAdminSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_admin()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_notification_session(self, parameter_receiver, proxy):
        """Gets a parameter notification session.

        :param parameter_receiver: notification callback
        :type parameter_receiver: ``osid.configuration.ParameterReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterNotificationSession``
        :rtype: ``osid.configuration.ParameterNotificationSession``
        :raise: ``NullArgument`` -- ``parameter_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_notification_session_for_configuration(self, parameter_receiver, configuration_id, proxy):
        """Gets a parameter notification session using the specified configuration.

        :param parameter_receiver: notification callback
        :type parameter_receiver: ``osid.configuration.ParameterReceiver``
        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterNotificationSession``
        :rtype: ``osid.configuration.ParameterNotificationSession``
        :raise: ``NotFound`` -- ``registry_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_receiver, configuration_id,`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_notification()`` or ``supports_visible_federation()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_configuration_session(self, proxy):
        """Gets a session for examining mappings of parameters to configurations.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterConfigurationSession``
        :rtype: ``osid.configuration.ParameterConfigurationSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_configuration()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_configuration_assignment_session(self, proxy):
        """Gets a session for managing mappings of parameters to configurations.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterConfigurationAssignmentSession``
        :rtype: ``osid.configuration.ParameterConfigurationAssignmentSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_configuration_assignment()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_parameter_smart_configuration_session(self, configuration_id, proxy):
        """Gets a session for managing smart configurations of parameters.

        :param configuration_id: the ``Id`` of the ``Configuration`` to use
        :type configuration_id: ``osid.id.Id``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ParameterSmartConfigurationSession``
        :rtype: ``osid.configuration.ParameterSmartConfigurationSession``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuratin_id`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_parameter_smart_configuration()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_lookup_session(self, proxy):
        """Gets a configuration lookup session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationLookupSession``
        :rtype: ``osid.configuration.ConfigurationLookupSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_lookup()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_query_session(self, proxy):
        """Gets a configuration query session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationQuerySession``
        :rtype: ``osid.configuration.ConfigurationQuerySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_query()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_search_session(self, proxy):
        """Gets a configuration search session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationSearchSession``
        :rtype: ``osid.configuration.ConfigurationSearchSession``
        :raise: ``OperationFailed`` -- ``proxy`` is ``null``
        :raise: ``NullArgument`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_search()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_notification_session(self, configuration_receiver, proxy):
        """Gets the notification session for subscribing to changes to configurations.

        :param configuration_receiver: notification callback
        :type configuration_receiver: ``osid.configuration.ConfigurationReceiver``
        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationNotificationSession``
        :rtype: ``osid.configuration.ConfigurationNotificationSession``
        :raise: ``NullArgument`` -- ``configuration_receiver`` or ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_notification()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_admin_session(self, proxy):
        """Gets a configuration administration session.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationAdminSession``
        :rtype: ``osid.configuration.ConfigurationAdminSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_admin()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_hierarchy_session(self, proxy):
        """Gets a hierarchy traversal service for configurations.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfiguraqtionHierarchySession``
        :rtype: ``osid.configuration.ConfigurationHierarchySession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_hierarchy()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_hierarchy_design_session(self, proxy):
        """Gets a hierarchy design service for configurations.

        :param proxy: a proxy
        :type proxy: ``osid.proxy.Proxy``
        :return: a ``ConfigurationHierarchyDesignSession``
        :rtype: ``osid.configuration.ConfigurationHierarchyDesignSession``
        :raise: ``NullArgument`` -- ``proxy`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_hierarchy_design()`` is ``false``

        """
        raise UNIMPLEMENTED()

    def get_configuration_batch_proxy_manager(self):
        """Gets a ``ConfigurationProxyManager``.

        :return: a ``ConfigurationBatchProxyManager``
        :rtype: ``osid.configuration.batch.ConfigurationBatchProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_batch()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_batch_proxy_manager = property(fget=get_configuration_batch_proxy_manager)

    def get_configuration_rules_proxy_manager(self):
        """Gets a ``ConfigurationProxyManager``.

        :return: a ``ConfigurationRulesProxyManager``
        :rtype: ``osid.configuration.rules.ConfigurationRulesProxyManager``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unimplemented`` -- ``supports_configuration_rules()`` is ``false``

        """
        raise UNIMPLEMENTED()

    configuration_rules_proxy_manager = property(fget=get_configuration_rules_proxy_manager)


##
# The following methods are from osid.configuration.ConfigurationLookupSession

    def can_lookup_configurations(self):
        """Tests if this user can perform ``Configuration`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.


        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_configuration_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.




        """
        raise UNIMPLEMENTED()

    def use_plenary_configuration_view(self):
        """A complete view of the ``Configuration`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.




        """
        raise UNIMPLEMENTED()

    def get_configuration(self, configuration_id):
        """Gets the ``Configuration`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Configuration`` may have a
        different ``Id`` than requested, such as the case where a
        duplicate ``Id`` was assigned to a ``Configuration`` and
        retained for compatibility.


        :param configuration_id: the ``Id`` of the ``Configuration`` to retrieve
        :type configuration_id: ``osid.id.Id``
        :return: the ``Configuration``
        :rtype: ``osid.configuration.Configuration``
        :raise: ``NotFound`` -- no ``Configuration`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_ids(self, configuration_ids):
        """Gets a ``ConfigurationList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the
        configurations specified in the ``Id`` list, in the order of the
        list, including duplicates, or an error results if an ``Id`` in
        the supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Configurations`` may be omitted from the list and
        may present the elements in any order including returning a
        unique set.


        :param configuration_ids: the list of ``Ids`` to retrieve
        :type configuration_ids: ``osid.id.IdList``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_genus_type(self, configuration_genus_type):
        """Gets an ``ConfigurationList`` corresponding to the given configuration genus ``Type`` which does not include configuration types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.


        :param configuration_genus_type: a configuration genus type
        :type configuration_genus_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_parent_genus_type(self, configuration_genus_type):
        """Gets an ``ConfigurationList`` corresponding to the given configuration genus ``Type`` and include any additional configurations with genus types derived from the specified ``Type``.
        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.


        :param configuration_genus_type: a configuration genus type
        :type configuration_genus_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_record_type(self, configuration_record_type):
        """Gets a ``ConfigurationList`` containing the given configuration record ``Type``.
        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.


        :param configuration_record_type: a configuration record type
        :type configuration_record_type: ``osid.type.Type``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_provider(self, resource_id):
        """Gets a ``ConfigurationList`` from the given provider ````.
        In plenary mode, the returned list contains all known
        configurations or an error results. Otherwise, the returned list
        may contain only those configurations that are accessible
        through this session.


        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Configuration`` list
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations(self):
        """Gets all ``Configurations,`` In plenary mode, the returned list contains all known configurations or an error results.
        Otherwise, the returned list may contain only those
        configurations that are accessible through this session.


        :return: a list of ``Configurations``
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    configurations = property(fget=get_configurations)


##
# The following methods are from osid.configuration.ConfigurationQuerySession

    def can_search_configurations(self):
        """Tests if this user can perform ``Configuration`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.


        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_configuration_query(self):
        """Gets a configuration query.

        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``

        """
        raise UNIMPLEMENTED()

    configuration_query = property(fget=get_configuration_query)

    def get_configurations_by_query(self, configuration_query):
        """Gets a list of ``Configurations`` matching the given search.

        :param configuration_query: the configuration query
        :type configuration_query: ``osid.configuration.ConfigurationQuery``
        :return: the returned ``ConfigurationList``
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NullArgument`` -- ``configuration_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_query`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationSearchSession

    def get_configuration_search(self):
        """Gets a configuration search.

        :return: the configuration search
        :rtype: ``osid.configuration.ConfigurationSearch``

        """
        raise UNIMPLEMENTED()

    configuration_search = property(fget=get_configuration_search)

    def get_configuration_search_order(self):
        """Gets a log search order.
        The ``ConfigurationSearchOrder`` is supplied to a
        ``ConfigurationSearch`` to specify the ordering of results.


        :return: the configuration search order
        :rtype: ``osid.configuration.ConfigurationSearchOrder``

        """
        raise UNIMPLEMENTED()

    configuration_search_order = property(fget=get_configuration_search_order)

    def get_configurations_by_search(self, configuration_query, configuration_search):
        """Gets a list of ``Configurations`` matching the given search.
        Each element in the array is OR'd.


        :param configuration_query: the configuration query
        :type configuration_query: ``osid.configuration.ConfigurationQuery``
        :param configuration_search: the configuration search
        :type configuration_search: ``osid.configuration.ConfigurationSearch``
        :return: the configuration search results
        :rtype: ``osid.configuration.ConfigurationSearchResults``
        :raise: ``NullArgument`` -- ``configuration_query`` or ``configuration_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_query`` or ``configuration_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_configuration_query_from_inspector(self, configuration_query_inspector):
        """Gets a configuration query from an inspector.
        The inspector is available from a
        ``ConfigurationSearchResults``.


        :param configuration_query_inspector: a configuration query inspector
        :type configuration_query_inspector: ``osid.configuration.ConfigurationQueryInspector``
        :return: the configuration query
        :rtype: ``osid.configuration.ConfigurationQuery``
        :raise: ``NullArgument`` -- ``configuration_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``configuration_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationAdminSession

    def can_create_configurations(self):
        """Tests if this user can create ``Configurations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a C
        ``onfiguration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.


        :return: ``false`` if ``Configuration`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_configuration_with_record_types(self, configuration_record_types):
        """Tests if this user can create a single ``Configuration`` using the desired record types.
        While ``ConfigurationManager.getConfigurationRecordTypes()`` can
        be used to examine which records are supported, this method
        tests which record(s) are required for creating a specific
        ``Configuration``. Providing an empty array tests if a
        ``Configuration`` can be created with no records.


        :param configuration_record_types: array of configuration record types
        :type configuration_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Configuration`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_configuration_form_for_create(self, configuration_record_types):
        """Gets the configuration form for creating new configurations.
        A new form should be requested for each create transaction.


        :param configuration_record_types: array of configuration record types
        :type configuration_record_types: ``osid.type.Type[]``
        :return: the configuration form
        :rtype: ``osid.configuration.ConfigurationForm``
        :raise: ``NullArgument`` -- ``configuration_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_configuration(self, configuration_form):
        """Creates a new ``Configuration``.

        :param configuration_form: the configuration form
        :type configuration_form: ``osid.configuration.ConfigurationForm``
        :return: the new ``Configuration``
        :rtype: ``osid.configuration.Configuration``
        :raise: ``IllegalState`` -- ``configuration_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``configuration_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_form`` did not originate from ``get_configuration_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_configurations(self):
        """Tests if this user can update ``Configurations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a C
        ``onfiguration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.


        :return: ``false`` if ``Configuration`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_configuration_form_for_update(self, configuration_id):
        """Gets the configuration form for updating existing configurations.
        A new configuration form should be requested for each update
        transaction.


        :param configuration_id: ``Id`` of a ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: the configuration form
        :rtype: ``osid.configuration.ConfigurationForm``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_configuration(self, configuration_form):
        """Updates an existing ``Configuration``.

        :param configuration_form: the configuration form
        :type configuration_form: ``osid.configuration.ConfigurationForm``
        :raise: ``IllegalState`` -- ``configuration_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``configuration_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``configuration_form`` did not originate from ``get_configuration_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_configurations(self):
        """Tests if this user can delete ``Configurations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Configuration`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.


        :return: ``false`` if ``Configuration`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_configuration(self, configuration_id):
        """Deletes a ``Configuration``.

        :param configuration_id: the ``Id`` of the ``Configuration`` to delete
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_configuration_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Configurations``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.


        :return: ``false`` if ``Configuration`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_configuration(self, configuration_id, alias_id):
        """Adds an ``Id`` to a ``Configuration`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Configuration`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another configuration it is
        reassigned to the given configuration ``Id``.


        :param configuration_id: the ``Id`` of a ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationNotificationSession

    def can_register_for_configuration_notifications(self):
        """Tests if this user can register for ``Configuration`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.


        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_configurations(self):
        """Registers for notifications of new configurations.
        ``ConfigurationReceiver.newConfiguration()`` is invoked when a
        new ``Configuration`` is created.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_configuration_ancestors(self, configuration_id):
        """Registers for notification if an ancestor is added to the specified configuration in the configuration hierarchy.
        ``ConfigurationReceiver.newConfigurationAncestor()`` is invoked
        when the specified configuration experiences an addition in
        ancestry.


        :param configuration_id: the ``Id`` of the configuration to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a configuration was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_configuration_descendants(self, configuration_id):
        """Registers for notification if a descendant is added to the specified configuration in the configuration hierarchy.
        ``ConfigurationReceiver.newConfigurationDescendant()`` is
        invoked when the specified configuration experiences an addition
        in descendants.


        :param configuration_id: the ``Id`` of the configuration to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a configuration was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_configurations(self):
        """Registers for notification of updated configurations.
        ``ConfigurationReceiver.changedConfiguration()`` is invoked when
        a configuration is changed.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_configuration(self, configuration_id):
        """Registers for notifications of an update to a configuration.
        ``ConfigurationReceiver.changedConfiguration()`` is invoked when
        the specified ``Configuration`` is changed.


        :param configuration_id: the ``Id`` of the ``Configuration`` to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Configuration`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_configurations(self):
        """Registers for notification of deleted configurations.
        ``ConfigurationReceiver.deletedConfiguration()`` is invoked when
        a ``Configuration`` is deleted.


        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_configuration(self, configuration_id):
        """Registers for notifications of a deleted configuration.
        ``ConfiguratinReceiver.deletedConfiguration()`` is invoked when
        the specified configuration is deleted.


        :param configuration_id: the ``Id`` of the ``Configuration`` to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Configuration`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_configuration_ancestors(self, configuration_id):
        """Registers for notification if an ancestor is removed from the specified configuration in the configuration hierarchy.
        ``ConfigurationReceiver.deletedConfigurationAncestor()`` is
        invoked when the specified configuration experiences a removal
        of an ancestor.


        :param configuration_id: the ``Id`` of the configuration to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a configuration was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_configuration_descendants(self, configuration_id):
        """Registers for notification if a descendant is removed from fthe specified configuration in the configuration hierarchy.
        ``ConfigurationReceiver.deletedConfigurationDescendant()`` is
        invoked when the specified configuration experiences a removal
        of one of its descdendents.


        :param configuration_id: the ``Id`` of the configuration to monitor
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a configuration was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationHierarchySession

    def get_configuration_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the configuration ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    configuration_hierarchy_id = property(fget=get_configuration_hierarchy_id)

    def get_configuration_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    configuration_hierarchy = property(fget=get_configuration_hierarchy)

    def can_access_configuration_hierarchy(self):
        """Tests if this user can perform hierarchy queries.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.


        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_root_configuration_ids(self):
        """Gets the root configuration ``Ids`` in this hierarchy.

        :return: the root configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_configuration_ids = property(fget=get_root_configuration_ids)

    def get_root_configurations(self):
        """Gets the root configurations in the configuration hierarchy.
        A node with no parents is an orphan. While all configuration
        ``Ids`` are known to the hierarchy, an orphan does not appear in
        the hierarchy unless explicitly added as a root node or child of
        another node.


        :return: the root configurations
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    root_configurations = property(fget=get_root_configurations)

    def has_parent_configurations(self, configuration_id):
        """Tests if the ``Configuration`` has any parents.

        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the configuration has parents, f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_parent_of_configuration(self, id_, configuration_id):
        """Tests if an ``Id`` is a direct parent of configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``configuration_id,`` f ``alse`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_configuration_ids(self, configuration_id):
        """Gets the parent ``Ids`` of the given configuration.

        :param configuration_id: a configuration Id
        :type configuration_id: ``osid.id.Id``
        :return: the parent Ids of the configuration
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parent_configurations(self, configuration_id):
        """Gets the parents of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the parents of the configuration
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_ancestor_of_configuration(self, id_, configuration_id):
        """Tests if an Id is an ancestor of a configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``tru`` e if this ``id`` is an ancestor of ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def has_child_configurations(self, configuration_id):
        """Tests if a configuration has any children.

        :param configuration_id: a ``configuration_id``
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``configuration_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_child_of_configuration(self, id_, configuration_id):
        """Tests if a node is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_configuration_ids(self, configuration_id):
        """Gets the child ``Ids`` of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the children of the configuration
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_child_configurations(self, configuration_id):
        """Gets the children of the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :return: the children of the configuration
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def is_descendant_of_configuration(self, id_, configuration_id):
        """Tests if an ``Id`` is a descendant of a configuration.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``configuration_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configuration_node_ids(self, configuration_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a configuration node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configuration_nodes(self, configuration_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given configuration.

        :param configuration_id: the ``Id`` to query
        :type configuration_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: a configuration node
        :rtype: ``osid.configuration.ConfigurationNode``
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ConfigurationHierarchyDesignSession

    def can_modify_configuration_hierarchy(self):
        """Tests if this user can change the hierarchy.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.


        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def add_root_configuration(self, configuration_id):
        """Adds a root configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``configuration_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_root_configuration(self, configuration_id):
        """Removes a root configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not a root
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def add_child_configuration(self, configuration_id, child_id):
        """Adds a child to a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``configuration_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``configuration_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``configuration_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_configuration(self, configuration_id, child_id):
        """Removes a child from a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``configuration_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def remove_child_configurations(self, configuration_id):
        """Removes all children from a configuration.

        :param configuration_id: the ``Id`` of a configuration
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``configuration_id`` is not in hierarchy
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()



class Configuration(osid_objects.OsidCatalog, osid_sessions.OsidSession):

    def is_registry(self):
        """Tests if this configuration is a parameter registry.
        A parameter registry contains parameter definitions with no
        values.

        :return: ``true`` if this is a registry, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_configuration_record(self, configuration_record_type):
        """Gets the configuration record corresponding to the given ``Configuration`` record ``Type``.
        This method is used to retrieve an object implementing the
        requested record. The ``configuration_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(configuration_record_type)`` is ``true`` .

        :param configuration_record_type: the type of configuration record to retrieve
        :type configuration_record_type: ``osid.type.Type``
        :return: the configuration record
        :rtype: ``osid.configuration.records.ConfigurationRecord``
        :raise: ``NullArgument`` -- ``configuration_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(configuration_record_type)`` is ``false``

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ValueRetrievalSession

    def get_configuration_id(self):
        """Gets the ``Configuration``  ``Id`` associated with this session.

        :return: the ``Configuration``  ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        raise UNIMPLEMENTED()

    configuration_id = property(fget=get_configuration_id)

    def get_configuration(self):
        """Gets the ``Configuration`` associated with this session.

        :return: the ``Configuration`` associated with this session
        :rtype: ``osid.configuration.Configuration``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    configuration = property(fget=get_configuration)

    def can_lookup_values(self):
        """Tests if this user can perform ``Value`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_value_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_value_view(self):
        """A complete view of the ``Value`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_federated_configuration_view(self):
        """Federates the view for methods in this session.
        A federated view will include values from parent configurations
        in the configuration hierarchy.



        """
        raise UNIMPLEMENTED()

    def use_isolated_configuration_view(self):
        """Isolates the view for methods in this session.
        An isolated view restricts lookups to this configuration only.



        """
        raise UNIMPLEMENTED()

    def use_conditional_view(self):
        """Returns only values that pass the defined parameter condition.
        Some parameter conditions do not require explicit conditional
        data to be passed and the ``Values`` returned from any method in
        this session are filtered on an implicit condition.



        """
        raise UNIMPLEMENTED()

    def use_unconditional_view(self):
        """Values that are filtered based on an implicit condition are not filtered out from methods in this session.
        Methods that take an explicit condition as a parameter are
        filtered on only those conditions that are specified.



        """
        raise UNIMPLEMENTED()

    def get_value_by_parameter(self, parameter_id):
        """Gets a ``Value`` for the given parameter ``Id``.
        If more than one value exists for the given parameter, the most
        preferred value is returned. This method can be used as a
        convenience when only one value is expected.
        ``get_values_by_parameters()`` should be used for getting all
        the active values.

        :param parameter_id: the ``Id`` of the ``Parameter`` to retrieve
        :type parameter_id: ``osid.id.Id``
        :return: the value
        :rtype: ``osid.configuration.Value``
        :raise: ``NotFound`` -- the ``parameter_id`` not found or no value available
        :raise: ``NullArgument`` -- the ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_values_by_parameter(self, parameter_id):
        """Gets all the ``Values`` for the given parameter ``Id``.

        :param parameter_id: the ``Id`` of the ``Parameter`` to retrieve
        :type parameter_id: ``osid.id.Id``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- the ``parameter_id`` not found
        :raise: ``NullArgument`` -- the ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_values_by_parameters(self, parameter_ids):
        """Gets the ``Values`` for the given parameter ``Ids``.

        :param parameter_ids: the ``Id`` of the ``Parameter`` to retrieve
        :type parameter_ids: ``osid.id.IdList``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- a parameter ``Id`` is not found
        :raise: ``NullArgument`` -- ``parameter_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_value_condition(self, parameter_id):
        """Gets a value condition for the given parameter.

        :param parameter_id: the ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: a value condition
        :rtype: ``osid.configuration.ValueCondition``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_value_by_parameter_on_condition(self, parameter_id, value_condition):
        """Gets a value in this configuration based on a condition.
        If multiple values are available the most preferred one is
        returned. The condition specified is applied to any or all
        parameters in this configuration as applicable.

        :param parameter_id: the ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param value_condition: the condition
        :type value_condition: ``osid.configuration.ValueCondition``
        :return: the value
        :rtype: ``osid.configuration.Value``
        :raise: ``NotFound`` -- parameter ``Id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``value_condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_condition`` not of this service

        """
        raise UNIMPLEMENTED()

    def get_values_by_parameter_on_condition(self, parameter_id, value_condition):
        """Gets all the values for a parameter based on a condition.
        In plenary mode, all values are returned or an error results. In
        comparative mode, inaccessible values may be omitted.

        :param parameter_id: the ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param value_condition: the condition
        :type value_condition: ``osid.configuration.ValueCondition``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- parameter ``Id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``value_condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_condition`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_values_by_parameters_on_condition(self, parameter_ids, value_condition):
        """Gets the values for parameters based on a condition.
        The specified condition is applied to any or all of the
        parameters as applicable. In plenary mode, all values are
        returned or an error results. In comparative mode, inaccessible
        values may be omitted.

        :param parameter_ids: the ``Id`` of a ``Parameter``
        :type parameter_ids: ``osid.id.IdList``
        :param value_condition: the condition
        :type value_condition: ``osid.configuration.ValueCondition``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- a parameter ``Id`` is not found
        :raise: ``NullArgument`` -- ``parameter_ids`` or ``value_condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_condition`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ValueLookupSession

    def use_active_value_view(self):
        """Only active values are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_status_value_view(self):
        """All active and inactive values are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_value(self, value_id):
        """Gets the ``Value`` specified by its ``Id``.
        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Value`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to a ``Value`` and retained for compatibility.

        :param value_id: the ``Id`` of the ``Value`` to retrieve
        :type value_id: ``osid.id.Id``
        :return: the returned ``Value``
        :rtype: ``osid.configuration.Value``
        :raise: ``NotFound`` -- no ``Value`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_values_by_ids(self, value_ids):
        """Gets a ``ValueList`` corresponding to the given ``IdList``.
        In plenary mode, the returned list contains all of the values
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Values`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param value_ids: the list of ``Ids`` to retrieve
        :type value_ids: ``osid.id.IdList``
        :return: the returned ``Value`` list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``value_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_values_by_genus_type(self, value_genus_type):
        """Gets a ``ValueList`` corresponding to the given value genus ``Type`` which does not include values of genus types derived from the specified ``Type``.

        :param value_genus_type: a value genus type
        :type value_genus_type: ``osid.type.Type``
        :return: the returned ``Value list``
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_values_by_parent_genus_type(self, value_genus_type):
        """Gets a ``ValueList`` corresponding to the given value genus ``Type`` and include any additional values with genus types derived from the specified ``Type``.

        :param value_genus_type: a value genus type
        :type value_genus_type: ``osid.type.Type``
        :return: the returned ``Value list``
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_values_by_record_type(self, value_record_type):
        """Gets a ``ValueList`` corresponding to the given value record ``Type`` which does not include values of record types derived from the specified ``Type``.

        :param value_record_type: a value type
        :type value_record_type: ``osid.type.Type``
        :return: the returned ``Value`` list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_values(self):
        """Gets all the values in this configuration.
        In plenary mode, all values are returned or an error results. In
        comparative mode, inaccessible values may be omitted.

        In plenary mode, the returned list contains all known values or
        an error results. Otherwise, the returned list may contain only
        those values that are accessible through this session.
        
        In active mode, values are returned that are currently active.
        In any status mode, active and inactive values are returned.

        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    values = property(fget=get_values)

    def get_values_on_condition(self, value_condition):
        """Gets the values in this configuration based on a condition.
        The condition specified is applied to any or all parameters in
        this configuration as applicable. In plenary mode, all values
        are returned or an error results. In comparative mode,
        inaccessible values may be omitted.

        :param value_condition: a value condition
        :type value_condition: ``osid.configuration.ValueCondition``
        :return: the value list
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_condition`` not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ValueQuerySession

    def can_search_values(self):
        """Tests if this user can perform ``Value`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_value_query(self):
        """Gets a value query.

        :return: the value query
        :rtype: ``osid.configuration.ValueQuery``

        """
        raise UNIMPLEMENTED()

    value_query = property(fget=get_value_query)

    def get_values_by_query(self, value_query):
        """Gets a list of ``Values`` matching the given value query.

        :param value_query: the value query
        :type value_query: ``osid.configuration.ValueQuery``
        :return: the returned ``ValueList``
        :rtype: ``osid.configuration.ValueList``
        :raise: ``NullArgument`` -- ``value_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a query form is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ValueSearchSession

    def get_value_search(self):
        """Gets a value search.

        :return: the value search
        :rtype: ``osid.configuration.ValueSearch``

        """
        raise UNIMPLEMENTED()

    value_search = property(fget=get_value_search)

    def get_value_search_order(self):
        """Gets a value search order.
        The ``ValueSearchOrder`` is supplied to a ``ValueSearch`` to
        specify the ordering of results.

        :return: the value search order
        :rtype: ``osid.configuration.ValueSearchOrder``

        """
        raise UNIMPLEMENTED()

    value_search_order = property(fget=get_value_search_order)

    def get_values_by_search(self, value_query, value_search):
        """Gets a list of ``Values`` matching the given search query using the given search.

        :param value_query: the value query
        :type value_query: ``osid.configuration.ValueQuery``
        :param value_search: the value search
        :type value_search: ``osid.configuration.ValueSearch``
        :return: the serach results
        :rtype: ``osid.configuration.ValueSearchResults``
        :raise: ``NullArgument`` -- ``value_query`` or ``value_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_query`` or ``value_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_value_query_from_inspector(self, value_query_inspector):
        """Gets a value query from an inspector.
        The inspector is available from a ``ValueSearchResults``.

        :param value_query_inspector: a value query inspector
        :type value_query_inspector: ``osid.configuration.ValueQueryInspector``
        :return: the value query
        :rtype: ``osid.configuration.ValueQuery``
        :raise: ``NullArgument`` -- ``value_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``value_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ValueAdminSession

    def support_value_conditions(self):
        """Tests if applying conditions to values is supported.

        :return: ``true`` if ``Value`` conditions are supported, ``false`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_values(self):
        """Tests if this user can create ``Values``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Value``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Value`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_value_with_record_types(self, value_record_types):
        """Tests if this user can create a single ``Value`` using the desired record types.
        While ``ConfigurationManager.getValueRecordTypes()`` can be used
        to examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Value``.
        Providing an empty array tests if a ``Value`` can be created
        with no records.

        :param value_record_types: array of value record types
        :type value_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Value`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``value_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_value_form_for_create(self, parameter_id, value_record_types):
        """Gets the form for creating new values.
        A new form should be requested for each create transaction.

        :param parameter_id: the parameter
        :type parameter_id: ``osid.id.Id``
        :param value_record_types: array of value record types
        :type value_record_types: ``osid.type.Type[]``
        :return: the value form
        :rtype: ``osid.configuration.ValueForm``
        :raise: ``NotFound`` -- ``parameter_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``value_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_value(self, value_form):
        """Creates a value.

        :param value_form: the form
        :type value_form: ``osid.configuration.ValueForm``
        :return: the value
        :rtype: ``osid.configuration.Value``
        :raise: ``IllegalState`` -- ``value_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``value_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_form`` did not originate from ``get_value_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_values(self):
        """Tests if this user can update ``Values``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Value``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if ``Value`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_value_form_for_update(self, value_id):
        """Gets the value form for updating an existing value.
        A new value form should be requested for each update
        transaction.

        :param value_id: the ``Id`` of the ``Value``
        :type value_id: ``osid.id.Id``
        :return: the value form
        :rtype: ``osid.configuration.ValueForm``
        :raise: ``NotFound`` -- the value is not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_value(self, value_form):
        """Updates an existing value.

        :param value_form: the form containing the elemnts to be updated
        :type value_form: ``osid.configuration.ValueForm``
        :raise: ``IllegalState`` -- ``value_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``parameter_id, value_id`` or ``value_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``value_form`` did not originate from ``get_value_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_values(self):
        """Tests if this user can delete ``Values``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Value``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Value`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_value(self, value_id):
        """Deletes the specified value.

        :param value_id: the ``Id`` of the ``Value`` to delete
        :type value_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``value_id`` is not found
        :raise: ``NullArgument`` -- ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_value_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Values``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Value`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_value(self, value_id, alias_id):
        """Adds an ``Id`` to a ``Value`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Value`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another value it is
        reassigned to the given value ``Id``.

        :param value_id: the ``Id`` of a ``Value``
        :type value_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``value_id`` not found
        :raise: ``NullArgument`` -- ``value_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ValueNotificationSession

    def can_register_for_value_notifications(self):
        """Tests if this user can register for ``Value`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_values(self):
        """Assigns a callback for notifications of new values.
        ``ValueReceiver.newValue()`` is invoked when a new ``Value`` is
        added to this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_new_values_for_parameter(self, parameter_id):
        """Assigns a callback for notifications of new values for the given parameter.
        ``ValueReceiver.newValue()`` is invoked when a new ``Value`` is
        added to this configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_values(self):
        """Assigns a callback for notification of updated parameter values in this configuration.
        ``ValueReceiver.changedValue()`` is invoked when a ``Value`` is
        changed in this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_values_for_parameter(self, parameter_id):
        """Assigns a callback for notifications of changed values for the given parameter.
        ``ValueReceiver.changedValue()`` is invoked when a ``Value`` is
        updated to this configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_value(self, value_id):
        """Assigns a callback for notifications of an update to a value in this configuration.
        ``ValueReceiver.changedValue()`` is invoked when the specified
        ``Value`` is updated in this configuration.

        :param value_id: the ``Id`` of the ``Value`` to monitor
        :type value_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_values(self):
        """Assigns a callback for notification of deleted values in this configuration.
        ``ValueReceiver.changedValue()`` is invoked when a ``Value`` is
        removed from this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_values_for_parameter(self, parameter_id):
        """Assigns a callback for notifications of changed values for the given parameter.
        ``ValueReceiver.changedValue()`` is invoked when a ``Value`` is
        removed from this configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_value(self, value_id):
        """Assigns a callback for notifications of an update to a value in this configuration.
        ``ValueReceiver.changedValue()`` is invoked when the specified
        ``Value`` is removed from this configuration.

        :param value_id: the ``Id`` of the ``Value`` to monitor
        :type value_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``value_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ParameterLookupSession

    def can_lookup_parameters(self):
        """Tests if this user can perform ``Parameter`` lookups.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def use_comparative_parameter_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.
        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        raise UNIMPLEMENTED()

    def use_plenary_parameter_view(self):
        """A complete view of the ``Parameter`` returns is desired.
        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        raise UNIMPLEMENTED()

    def use_active_parameter_view(self):
        """Only active parameters are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def use_any_status_parameter_view(self):
        """All active and inactive parameters are returned by methods in this session."""
        raise UNIMPLEMENTED()

    def get_parameter(self, parameter_id):
        """Gets the ``Parameter`` specified by its ``Id``.

        :param parameter_id: the ``Id`` of the ``Parameter`` to retrieve
        :type parameter_id: ``osid.id.Id``
        :return: the returned ``Parameter``
        :rtype: ``osid.configuration.Parameter``
        :raise: ``NotFound`` -- no ``Parameter`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parameters_by_ids(self, parameter_ids):
        """Gets a ``ParameterList`` corresponding to the given ``IdList``.

        :param parameter_ids: the list of ``Ids`` to retrieve
        :type parameter_ids: ``osid.id.IdList``
        :return: the returned ``Parameter`` list
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``parameter_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parameters_by_genus_type(self, parameter_genus_type):
        """Gets a ``ParameterList`` corresponding to the given parameter genus ``Type`` which does not include parameters of genus types derived from the specified ``Type``.

        :param parameter_genus_type: a parameter genus type
        :type parameter_genus_type: ``osid.type.Type``
        :return: the returned ``Parameter list``
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``parameter_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parameters_by_parent_genus_type(self, parameter_genus_type):
        """Gets a ``ParameterList`` corresponding to the given parameters genus ``Type`` and include any additional parameters with genus types derived from the specified ``Type``.

        :param parameter_genus_type: a parameter genus type
        :type parameter_genus_type: ``osid.type.Type``
        :return: the returned ``Parameter list``
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``parameter_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parameters_by_record_type(self, parameter_record_type):
        """Gets a ``ParameterList`` corresponding to the given parameter record ``Type`` which does not include parameters of record types derived from the specified ``Type``.

        :param parameter_record_type: a parameter type
        :type parameter_record_type: ``osid.type.Type``
        :return: the returned ``Parameter`` list
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``parameter_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parameters(self):
        """Gets all ``Parameters``.

        :return: a list of ``Parameters``
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    parameters = property(fget=get_parameters)


##
# The following methods are from osid.configuration.ParameterQuerySession

    def can_search_parameters(self):
        """Tests if this user can perform ``Parameter`` searches.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_parameter_query(self):
        """Gets a paraameter query.

        :return: the parameter query
        :rtype: ``osid.configuration.ParameterQuery``

        """
        raise UNIMPLEMENTED()

    parameter_query = property(fget=get_parameter_query)

    def get_parameters_by_query(self, parameter_query):
        """Gets a list of ``Parameters`` matching the given query.

        :param parameter_query: the parameter query
        :type parameter_query: ``osid.configuration.ParameterQuery``
        :return: the returned ``ParameterList``
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``parameter_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- a query form is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ParameterSearchSession

    def get_parameter_search(self):
        """Gets a parameter search.

        :return: the parameter search
        :rtype: ``osid.configuration.ParameterSearch``

        """
        raise UNIMPLEMENTED()

    parameter_search = property(fget=get_parameter_search)

    def get_parameter_search_order(self):
        """Gets a parameter entry search order.
        The ``ParameterEntrySearchOrder`` is supplied to an
        ``ParameterEntrySearch`` to specify the ordering of results.

        :return: the parameter search order
        :rtype: ``osid.configuration.ParameterSearchOrder``

        """
        raise UNIMPLEMENTED()

    parameter_search_order = property(fget=get_parameter_search_order)

    def get_parameters_by_search(self, parameter_query, parameter_search):
        """Gets a list of ``Parameters`` matching the given search query using the given search.

        :param parameter_query: the parameter query
        :type parameter_query: ``osid.configuration.ParameterQuery``
        :param parameter_search: the parameter search
        :type parameter_search: ``osid.configuration.ParameterSearch``
        :return: the parameter search results
        :rtype: ``osid.configuration.ParameterSearchResults``
        :raise: ``NullArgument`` -- ``parameter_query`` or ``parameter_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``parameter_query`` or ``parameter_search`` is not of this service

        """
        raise UNIMPLEMENTED()

    def get_parameter_query_from_inspector(self, parameter_query_inspector):
        """Gets a parameter query from an inspector.
        The inspector is available from a ``ParameterSearchResults``.

        :param parameter_query_inspector: a parameter query inspector
        :type parameter_query_inspector: ``osid.configuration.ParameterQueryInspector``
        :return: the parameter query
        :rtype: ``osid.configuration.ParameterQuery``
        :raise: ``NullArgument`` -- ``parameter_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``parameter_query_inspector`` is not of this service

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ParameterAdminSession

    def can_create_parameters(self):
        """Tests if this user can create ``Parameters``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a
        ``Parameter`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        create operations to an unauthorized user.

        :return: ``false`` if ``Parameter`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_create_parameter_with_record_types(self, parameter_record_types):
        """Tests if this user can create a single ``Parameter`` using the desired record types.
        While ``ConfigurationManager.getParameterRecordTypes()`` can be
        used to examine which records are supported, this method tests
        which record(s) are required for creating a specific
        ``Parameter``. Providing an empty array tests if a ``Parameter``
        can be created with no records.

        :param parameter_record_types: array of parameter record types
        :type parameter_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Parameter`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``parameter_record_types`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_parameter_form_for_create(self, parameter_record_types):
        """Gets the paramater form for creating new parameters.

        :param parameter_record_types: array of parameter record types
        :type parameter_record_types: ``osid.type.Type[]``
        :return: the parameter form
        :rtype: ``osid.configuration.ParameterForm``
        :raise: ``NullArgument`` -- ``configuration_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form for requested record types

        """
        raise UNIMPLEMENTED()

    def create_parameter(self, parameter_form):
        """Creates a new ``Parameter``.

        :param parameter_form: the form for this ``Parameter``
        :type parameter_form: ``osid.configuration.ParameterForm``
        :return: the new ``Parameter``
        :rtype: ``osid.configuration.Parameter``
        :raise: ``IllegalState`` -- ``parameter_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``parameter_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``parameter_form`` did not originate from ``get_parameter_form_for_create()``

        """
        raise UNIMPLEMENTED()

    def can_update_parameters(self):
        """Tests if this user can update ``Parameters``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a
        ``Parameter`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        update operations to an unauthorized user.

        :return: ``false`` if ``Parameter`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_parameter_form_for_update(self, parameter_id):
        """Gets the parameter form for updating an existing parameters.

        :param parameter_id: the ``Id`` of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: the parameter form
        :rtype: ``osid.configuration.ParameterForm``
        :raise: ``NotFound`` -- ``parameter_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def update_parameter(self, parameter_form):
        """Updates an existing parameter.

        :param parameter_form: the form containing the elements to be updated
        :type parameter_form: ``osid.configuration.ParameterForm``
        :raise: ``IllegalState`` -- ``parameter_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``parameter_id`` or ``parameter_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``parameter_form`` did not originate from ``get_parameter_form_for_update()``

        """
        raise UNIMPLEMENTED()

    def can_delete_parameters(self):
        """Tests if this user can delete ``Parameters``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a
        ``Parameter`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        delete operations to an unauthorized user.

        :return: ``false`` if ``Parameter`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def delete_parameter(self, parameter_id):
        """Deletes a ``Parameter``.

        :param parameter_id: the ``Id`` of the ``Parameter`` to remove
        :type parameter_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parameter_id`` not found
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def can_manage_parameter_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Parameters``.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Parameter`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def alias_parameter(self, parameter_id, alias_id):
        """Adds an ``Id`` to a ``Parameter`` for the purpose of creating compatibility.
        The primary ``Id`` of the ``Parameter`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another parameter it is
        reassigned to the given parameter ``Id``.

        :param parameter_id: the ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``parameter_id`` not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ParameterNotificationSession

    def can_register_for_parameter_notifications(self):
        """Tests if this user can register for ``Parameter`` notifications.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def register_for_new_parameters(self):
        """Assigns a callback for notifications of new parameters.
        ``ParameterReceiver.newParameter()`` is invoked when a new
        ``Parameter`` is added to this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_parameters(self):
        """Assigns a callback for notification of updated parameters.
        ``ParameterReceiver.changedParameter()`` is invoked when a
        ``Parameter`` is changed in this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_changed_parameter(self, parameter_id):
        """Assigns a callback for notifications of an update to a parameter.
        ``ParamaterReceiver.changedParameter()`` is invoked when the
        specified ``Parameter`` is changed in this configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_parameters(self):
        """Assigns a callback for notification of deleted parameters.
        ``ParameterReceiver.deletedParamater()`` is invoked when a
        ``Parameter`` is deleted or removed from this configuration.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def register_for_deleted_parameter(self, parameter_id):
        """Assigns a callback for notifications of a deleted parameter.
        ``ParameterReceiver.deletedParameter()`` is invoked when the
        specified ``Parameter`` is deleted or removed from this
        configuration.

        :param parameter_id: the ``Id`` of the ``Parameter`` to monitor
        :type parameter_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ParameterConfigurationSession

    def can_lookup_parameter_configurations(self):
        """Tests if this user can perform lookups on configurations of parameters.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookups are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def get_parameter_ids_by_configuration(self, configuration_id):
        """Gets the list of ``Parameter``  ``Ids`` associated with a ``Configuration``.

        :param configuration_id: ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: list of matching parameter ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parameters_by_configuration(self, configuration_id):
        """Gets the list of ``Parameters`` associated with a ``Configuration``.

        :param configuration_id: ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: list of matching parameters
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NotFound`` -- ``configuration_id`` is not found
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parameter_ids_by_configurations(self, configuration_ids):
        """Gets the list of ``Parameter Ids`` associated with a list of ``Configurations``.

        :param configuration_ids: list of configurations
        :type configuration_ids: ``osid.id.IdList``
        :return: list of parameter ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_parameters_by_configurations(self, configuration_ids):
        """Gets the list of ``Parameters`` associated with a list of ``Configurations``.

        :param configuration_ids: list of configurations
        :type configuration_ids: ``osid.id.IdList``
        :return: list of parameters
        :rtype: ``osid.configuration.ParameterList``
        :raise: ``NullArgument`` -- ``configuration_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configuration_ids_by_parameter(self, parameter_id):
        """Gets the ``Configuration Ids`` mapped to a ``Parameter``.

        :param parameter_id: ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: list of configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``parameter_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def get_configurations_by_parameter(self, parameter_id):
        """Gets the ``Configurations`` mapped to a ``Parameter``.

        :param parameter_id: ``Id`` of a ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: list of configurations
        :rtype: ``osid.configuration.ConfigurationList``
        :raise: ``NotFound`` -- ``parameter_id`` is not found
        :raise: ``NullArgument`` -- ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ParameterConfigurationAssignmentSession

    def can_assign_parameter_configurations(self):
        """Tests if this user can change parameter configuration mappings.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not wish to offer
        assignment operations.

        :return: ``false`` if parameter configuration assignment is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def can_assign_parameters_to_configuration(self, configuration_id):
        """Tests if this user can alter parameter/configuration parameters.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known parameter methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: ``false`` if configuration is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``

        """
        raise UNIMPLEMENTED()

    def get_assignable_configuration_ids(self, configuration_id):
        """Gets a list of configurations including and under the given configuration node in which any parameter can be assigned.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :return: list of assignable configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def get_assignable_configuration_ids_for_parameter(self, configuration_id, parameter_id):
        """Gets a list of configurations including and under the given configuration node in which a specific parameter can be assigned.

        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :param parameter_id: the ``Id`` of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :return: list of assignable configuration ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``configuration_id`` or ``parameter_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    def assign_parameter_to_configuration(self, parameter_id, configuration_id):
        """Adds an existing ``Parameter`` to a ``Configuration``.

        :param parameter_id: the ``Id`` of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param configuration_id: the ``Id`` of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``parameter_id`` and ``configuration_id`` already mapped
        :raise: ``NotFound`` -- ``parameter_id`` or ``configuration_id`` not found
        :raise: ``NullArgument`` -- ``parameter_id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()

    def unassign_parameter_from_configuration(self, parameter_id, configuration_id):
        """Removes a ``Parameter`` from a ``Configuration``.

        :param parameter_id: the Id of the ``Parameter``
        :type parameter_id: ``osid.id.Id``
        :param configuration_id: the Id of the ``Configuration``
        :type configuration_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``parameter_id`` or ``configuration_id`` not found or is not mapped
        :raise: ``NullArgument`` -- ``parameter_id`` or ``configuration_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        raise UNIMPLEMENTED()


##
# The following methods are from osid.configuration.ParameterSmartConfigurationSession

    def can_manage_smart_configurations(self):
        """Tests if this user can manage smart configurations.
        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart cobfiguration management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        raise UNIMPLEMENTED()

    def apply_parameter_query(self, parameter_query):
        """Applies a parameter query to this configuration.

        :param parameter_query: the parameter query
        :type parameter_query: ``osid.configuration.ParameterQuery``
        :raise: ``NullArgument`` -- ``parameter_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``parameter_query`` not of this service

        """
        raise UNIMPLEMENTED()

    def inspec_parameter_query(self):
        """Gets a parameter query inspector for this configuration.

        :return: the parameter query inspector
        :rtype: ``osid.configuration.ParameterQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        raise UNIMPLEMENTED()

    def apply_parameter_sequencing(self, parameter_search_order):
        """Applies a parameter search order to this configuration.

        :param parameter_search_order: the parameter search order
        :type parameter_search_order: ``osid.configuration.ParameterSearchOrder``
        :raise: ``NullArgument`` -- ``parameter_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``parameter_search_order`` not of this service

        """
        raise UNIMPLEMENTED()



class ConfigurationList(osid_objects.OsidList):

    def get_next_configuration(self):
        """Gets the next ``Configuration`` in this list.

        :return: the next ``Configuration`` in this list. The ``has_next()`` method should be used to test that a next ``Configuration`` is available before calling this method.
        :rtype: ``osid.configuration.Configuration``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()

    next_configuration = property(fget=get_next_configuration)

    def get_next_configurations(self, n):
        """Gets the next set of ``Configuration`` objects in this lis which must be less than or equal to whst is returned from ``available()``.

        :param n: the number of ``Configuration`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Configuration`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.configuration.Configuration``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        raise UNIMPLEMENTED()



class Configurations(ConfigurationManager):
    pass


