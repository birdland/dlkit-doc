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