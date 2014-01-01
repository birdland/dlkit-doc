.. currentmodule:: dlkit.learning.queries
.. automodule:: dlkit.learning.queries

Queries
=======


Objective Query
---------------

.. autoclass:: ObjectiveQuery
   :show-inheritance:

   .. automethod:: ObjectiveQuery.match_assessment_id

   .. autoattribute:: ObjectiveQuery.assessment_id_terms

   .. automethod:: ObjectiveQuery.supports_assessment_query

   .. autoattribute:: ObjectiveQuery.assessment_query

   .. automethod:: ObjectiveQuery.match_any_assessment

   .. autoattribute:: ObjectiveQuery.assessment_terms

   .. automethod:: ObjectiveQuery.match_knowledge_category_id

   .. autoattribute:: ObjectiveQuery.knowledge_category_id_terms

   .. automethod:: ObjectiveQuery.supports_knowledge_category_query

   .. autoattribute:: ObjectiveQuery.knowledge_category_query

   .. automethod:: ObjectiveQuery.match_any_knowledge_category

   .. autoattribute:: ObjectiveQuery.knowlege_category_terms

   .. automethod:: ObjectiveQuery.match_cognitive_process_id

   .. autoattribute:: ObjectiveQuery.cognitive_process_id_terms

   .. automethod:: ObjectiveQuery.supports_cognitive_process_query

   .. autoattribute:: ObjectiveQuery.cognitive_process_query

   .. automethod:: ObjectiveQuery.match_any_cognitive_process

   .. autoattribute:: ObjectiveQuery.cognitive_process_terms

   .. automethod:: ObjectiveQuery.match_activity_id

   .. autoattribute:: ObjectiveQuery.activity_id_terms

   .. automethod:: ObjectiveQuery.supports_activity_query

   .. autoattribute:: ObjectiveQuery.activity_query

   .. automethod:: ObjectiveQuery.match_any_activity

   .. autoattribute:: ObjectiveQuery.activity_terms

   .. automethod:: ObjectiveQuery.match_requisite_objective_ids

   .. autoattribute:: ObjectiveQuery.requisite_objective_id_terms

   .. automethod:: ObjectiveQuery.supports_requisite_objective_query

   .. autoattribute:: ObjectiveQuery.requisite_objective_query

   .. automethod:: ObjectiveQuery.match_any_requisite_objective

   .. autoattribute:: ObjectiveQuery.requisite_objective_terms

   .. automethod:: ObjectiveQuery.match_dependent_objective_ids

   .. autoattribute:: ObjectiveQuery.dependent_objective_id_terms

   .. automethod:: ObjectiveQuery.supports_depndent_objective_query

   .. autoattribute:: ObjectiveQuery.dependent_objective_query

   .. automethod:: ObjectiveQuery.match_any_dependent_objective

   .. autoattribute:: ObjectiveQuery.dependent_objective_terms

   .. automethod:: ObjectiveQuery.match_equivalent_objective_ids

   .. autoattribute:: ObjectiveQuery.equivalent_objective_id_terms

   .. automethod:: ObjectiveQuery.supports_equivalent_objective_query

   .. autoattribute:: ObjectiveQuery.equivalent_objective_query

   .. automethod:: ObjectiveQuery.match_any_equivalent_objective

   .. autoattribute:: ObjectiveQuery.equivalent_objective_terms

   .. automethod:: ObjectiveQuery.match_ancestor_objective_id

   .. autoattribute:: ObjectiveQuery.ancestor_objective_id_terms

   .. automethod:: ObjectiveQuery.supports_ancestor_objective_query

   .. autoattribute:: ObjectiveQuery.ancestor_objective_query

   .. automethod:: ObjectiveQuery.match_any_ancestor_objective

   .. autoattribute:: ObjectiveQuery.ancestor_objective_terms

   .. automethod:: ObjectiveQuery.match_descendant_objective_id

   .. autoattribute:: ObjectiveQuery.descendant_objective_id_terms

   .. automethod:: ObjectiveQuery.supports_descendant_objective_query

   .. autoattribute:: ObjectiveQuery.descendant_objective_query

   .. automethod:: ObjectiveQuery.match_any_descendant_objective

   .. autoattribute:: ObjectiveQuery.descendant_objective_terms

   .. automethod:: ObjectiveQuery.match_objective_bank_id

   .. autoattribute:: ObjectiveQuery.objective_bank_id_terms

   .. automethod:: ObjectiveQuery.supports_objective_bank_query

   .. autoattribute:: ObjectiveQuery.objective_bank_query

   .. autoattribute:: ObjectiveQuery.objective_bank_terms

   .. automethod:: ObjectiveQuery.get_objective_query_record



Activity Query
--------------

.. autoclass:: ActivityQuery
   :show-inheritance:

   .. automethod:: ActivityQuery.match_objective_id

   .. autoattribute:: ActivityQuery.objective_id_terms

   .. automethod:: ActivityQuery.supports_objective_query

   .. autoattribute:: ActivityQuery.objective_query

   .. autoattribute:: ActivityQuery.objective_terms

   .. automethod:: ActivityQuery.match_asset_id

   .. autoattribute:: ActivityQuery.asset_id_terms

   .. automethod:: ActivityQuery.supports_asset_query

   .. autoattribute:: ActivityQuery.asset_query

   .. automethod:: ActivityQuery.match_any_asset

   .. autoattribute:: ActivityQuery.asset_terms

   .. automethod:: ActivityQuery.match_course_id

   .. autoattribute:: ActivityQuery.course_id_terms

   .. automethod:: ActivityQuery.supports_course_query

   .. autoattribute:: ActivityQuery.course_query

   .. automethod:: ActivityQuery.match_any_course

   .. autoattribute:: ActivityQuery.course_terms

   .. automethod:: ActivityQuery.match_assessment_id

   .. autoattribute:: ActivityQuery.assessment_id_terms

   .. automethod:: ActivityQuery.supports_assessment_query

   .. autoattribute:: ActivityQuery.assessment_query

   .. automethod:: ActivityQuery.match_any_assessment

   .. autoattribute:: ActivityQuery.assessment_terms

   .. automethod:: ActivityQuery.match_objective_bank_id

   .. autoattribute:: ActivityQuery.objective_bank_id_terms

   .. automethod:: ActivityQuery.supports_objective_bank_query

   .. autoattribute:: ActivityQuery.objective_bank_query

   .. autoattribute:: ActivityQuery.objective_bank_terms

   .. automethod:: ActivityQuery.get_activity_query_record



Proficiency Query
-----------------

.. autoclass:: ProficiencyQuery
   :show-inheritance:

   .. automethod:: ProficiencyQuery.match_resource_id

   .. autoattribute:: ProficiencyQuery.resource_id_terms

   .. automethod:: ProficiencyQuery.supports_resource_query

   .. autoattribute:: ProficiencyQuery.resource_query

   .. autoattribute:: ProficiencyQuery.resource_terms

   .. automethod:: ProficiencyQuery.match_objective_id

   .. autoattribute:: ProficiencyQuery.objective_id_terms

   .. automethod:: ProficiencyQuery.supports_objective_query

   .. autoattribute:: ProficiencyQuery.objective_query

   .. automethod:: ProficiencyQuery.match_any_objective

   .. autoattribute:: ProficiencyQuery.objective_terms

   .. automethod:: ProficiencyQuery.match_completion

   .. autoattribute:: ProficiencyQuery.completion_terms

   .. automethod:: ProficiencyQuery.match_minimum_completion

   .. autoattribute:: ProficiencyQuery.minimum_completion_terms

   .. automethod:: ProficiencyQuery.match_level_id

   .. autoattribute:: ProficiencyQuery.level_id_terms

   .. automethod:: ProficiencyQuery.supports_level_query

   .. autoattribute:: ProficiencyQuery.level_query

   .. automethod:: ProficiencyQuery.match_any_level

   .. autoattribute:: ProficiencyQuery.level_terms

   .. automethod:: ProficiencyQuery.match_objective_bank_id

   .. autoattribute:: ProficiencyQuery.objective_bank_id_terms

   .. automethod:: ProficiencyQuery.supports_objective_bank_query

   .. autoattribute:: ProficiencyQuery.objective_bank_query

   .. autoattribute:: ProficiencyQuery.objective_bank_terms

   .. automethod:: ProficiencyQuery.get_proficiency_query_record



Objective Bank Query
--------------------

.. autoclass:: ObjectiveBankQuery
   :show-inheritance:

   .. automethod:: ObjectiveBankQuery.match_objective_id

   .. autoattribute:: ObjectiveBankQuery.objective_id_terms

   .. automethod:: ObjectiveBankQuery.supports_objective_query

   .. autoattribute:: ObjectiveBankQuery.objective_query

   .. automethod:: ObjectiveBankQuery.match_any_objective

   .. autoattribute:: ObjectiveBankQuery.objective_terms

   .. automethod:: ObjectiveBankQuery.match_activity_id

   .. autoattribute:: ObjectiveBankQuery.activity_id_terms

   .. automethod:: ObjectiveBankQuery.supports_activity_query

   .. autoattribute:: ObjectiveBankQuery.activity_query

   .. automethod:: ObjectiveBankQuery.match_any_activity

   .. autoattribute:: ObjectiveBankQuery.activity_terms

   .. automethod:: ObjectiveBankQuery.match_ancestor_objective_bank_id

   .. autoattribute:: ObjectiveBankQuery.ancestor_objective_bank_id_terms

   .. automethod:: ObjectiveBankQuery.supports_ancestor_objective_bank_query

   .. autoattribute:: ObjectiveBankQuery.ancestor_objective_bank_query

   .. automethod:: ObjectiveBankQuery.match_any_ancestor_objective_bank

   .. autoattribute:: ObjectiveBankQuery.ancestor_objective_bank_terms

   .. automethod:: ObjectiveBankQuery.match_descendant_objective_bank_id

   .. autoattribute:: ObjectiveBankQuery.descendant_objective_bank_id_terms

   .. automethod:: ObjectiveBankQuery.supports_descendant_objective_bank_query

   .. autoattribute:: ObjectiveBankQuery.descendant_objective_bank_query

   .. automethod:: ObjectiveBankQuery.match_any_descendant_objective_bank

   .. autoattribute:: ObjectiveBankQuery.descendant_objective_bank_terms

   .. automethod:: ObjectiveBankQuery.get_objective_bank_query_record



