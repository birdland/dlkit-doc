# -*- coding: utf-8 -*-
"""Rules Open Service Interface Definitions
rules version 3.0.0

The Rules OSID provides a means to evaluate rules and retrieve results.
A ``Rule`` represents a something that can be executed and can be
organized into ``Engines``. The rule evaluation accepts a ``Condition``
that is used to supply input conditions to the rule engine.

The Rules OSID does not define a means for authoring rules. Definitions
exist for evaluating, examining and organizing rules. A ``Rule`` is
identified by an Id such that a consumer wishing to evaluate a rule must
have knowledge of the ``Rule Id`` along with the expectations of data
(recod ``Type`` ) required in the ``Condition``. The Rule also implies
the structure of the ``Result,`` which can be a simple boolean value or
another structure defined in a Result Record.

Engines can be organized into hierarchies for federation. An engine that
is a parent of another engine makes visible the rules of its children.

Example where the consumer executes a rule with knowledge of the ``Rule
Id`` , ``ConditionRecord``  ``Type,`` and the meaning of the ``Result``.
  RulesSession session = manager.getRulesSession();
  Condition condition = session.getConditionForRule(shouldIWearACoatRuleId);
  if (!condition.hasRecordType(temperatureConditionRecordType) {
      error ("temperature condition record not supported");
  }
  
  TemperatureCondition temp = condition.getConditionRecord(temperatureConditionRecordType);
  temp.setTemperature(28);
  
  if (session.evaluateRule(shouldIWearACoatRuleId, condition) {
      putOnACoat();
  }



"""