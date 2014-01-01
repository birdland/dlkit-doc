.. currentmodule:: dlkit.learning.query_inspectors
.. automodule:: dlkit.learning.query_inspectors

Query_Inspectors
================


Objective Query Inspector
-------------------------

.. autoclass:: ObjectiveQueryInspector
   :show-inheritance:

   .. autoattribute:: ObjectiveQueryInspector.assessment_id_terms

   .. autoattribute:: ObjectiveQueryInspector.assessment_terms

   .. autoattribute:: ObjectiveQueryInspector.knowledge_category_id_terms

   .. autoattribute:: ObjectiveQueryInspector.knowledge_category_terms

   .. autoattribute:: ObjectiveQueryInspector.cognitive_process_id_terms

   .. autoattribute:: ObjectiveQueryInspector.cognitive_process_terms

   .. autoattribute:: ObjectiveQueryInspector.requisite_objective_id_terms

   .. autoattribute:: ObjectiveQueryInspector.requisite_objective_terms

   .. autoattribute:: ObjectiveQueryInspector.dependent_objective_id_terms

   .. autoattribute:: ObjectiveQueryInspector.dependent_objective_terms

   .. autoattribute:: ObjectiveQueryInspector.equivalent_objective_id_terms

   .. autoattribute:: ObjectiveQueryInspector.equivalent_objective_terms

   .. autoattribute:: ObjectiveQueryInspector.ancestor_objective_id_terms

   .. autoattribute:: ObjectiveQueryInspector.ancestor_objective_terms

   .. autoattribute:: ObjectiveQueryInspector.descendant_objective_id_terms

   .. autoattribute:: ObjectiveQueryInspector.descendant_objective_terms

   .. autoattribute:: ObjectiveQueryInspector.activity_id_terms

   .. autoattribute:: ObjectiveQueryInspector.activity_terms

   .. autoattribute:: ObjectiveQueryInspector.objective_bank_id_terms

   .. autoattribute:: ObjectiveQueryInspector.objective_bank_terms

   .. automethod:: ObjectiveQueryInspector.get_objective_query_inspector_record



Activity Query Inspector
------------------------

.. autoclass:: ActivityQueryInspector
   :show-inheritance:

   .. autoattribute:: ActivityQueryInspector.objective_id_terms

   .. autoattribute:: ActivityQueryInspector.objective_terms

   .. autoattribute:: ActivityQueryInspector.asset_id_terms

   .. autoattribute:: ActivityQueryInspector.asset_terms

   .. autoattribute:: ActivityQueryInspector.course_id_terms

   .. autoattribute:: ActivityQueryInspector.course_terms

   .. autoattribute:: ActivityQueryInspector.assessment_id_terms

   .. autoattribute:: ActivityQueryInspector.assessment_terms

   .. autoattribute:: ActivityQueryInspector.objective_bank_id_terms

   .. autoattribute:: ActivityQueryInspector.objective_bank_terms

   .. automethod:: ActivityQueryInspector.get_activity_query_inspector_record



Proficiency Query Inspector
---------------------------

.. autoclass:: ProficiencyQueryInspector
   :show-inheritance:

   .. autoattribute:: ProficiencyQueryInspector.resource_id_terms

   .. autoattribute:: ProficiencyQueryInspector.resource_terms

   .. autoattribute:: ProficiencyQueryInspector.objective_id_terms

   .. autoattribute:: ProficiencyQueryInspector.objective_terms

   .. autoattribute:: ProficiencyQueryInspector.completion_terms

   .. autoattribute:: ProficiencyQueryInspector.minimum_completion_terms

   .. autoattribute:: ProficiencyQueryInspector.level_id_terms

   .. autoattribute:: ProficiencyQueryInspector.level_terms

   .. autoattribute:: ProficiencyQueryInspector.objective_bank_id_terms

   .. autoattribute:: ProficiencyQueryInspector.objective_bank_terms

   .. automethod:: ProficiencyQueryInspector.get_proficiency_query_inspector_record



Objective Bank Query Inspector
------------------------------

.. autoclass:: ObjectiveBankQueryInspector
   :show-inheritance:

   .. autoattribute:: ObjectiveBankQueryInspector.objective_id_terms

   .. autoattribute:: ObjectiveBankQueryInspector.objective_terms

   .. autoattribute:: ObjectiveBankQueryInspector.activity_id_terms

   .. autoattribute:: ObjectiveBankQueryInspector.activity_terms

   .. autoattribute:: ObjectiveBankQueryInspector.ancestor_objective_bank_id_terms

   .. autoattribute:: ObjectiveBankQueryInspector.ancestor_objective_bank_terms

   .. autoattribute:: ObjectiveBankQueryInspector.descendant_objective_bank_id_terms

   .. autoattribute:: ObjectiveBankQueryInspector.descendant_objective_bank_terms

   .. automethod:: ObjectiveBankQueryInspector.get_objective_bank_query_inspector_record



