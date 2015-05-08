.. currentmodule:: dlkit.learning.objects
.. automodule:: dlkit.learning.objects

Objects
=======


Objective
---------

.. autoclass:: Objective
   :show-inheritance:

   .. automethod:: Objective.has_assessment

   .. autoattribute:: Objective.assessment_id

   .. autoattribute:: Objective.assessment

   .. automethod:: Objective.has_knowledge_category

   .. autoattribute:: Objective.knowledge_category_id

   .. autoattribute:: Objective.knowledge_category

   .. automethod:: Objective.has_cognitive_process

   .. autoattribute:: Objective.cognitive_process_id

   .. autoattribute:: Objective.cognitive_process

   .. automethod:: Objective.get_objective_record



Objective Form
--------------

.. autoclass:: ObjectiveForm
   :show-inheritance:

   .. autoattribute:: ObjectiveForm.assessment_metadata

   .. autoattribute:: ObjectiveForm.assessment

   .. autoattribute:: ObjectiveForm.knowledge_category_metadata

   .. autoattribute:: ObjectiveForm.knowledge_category

   .. autoattribute:: ObjectiveForm.cognitive_process_metadata

   .. autoattribute:: ObjectiveForm.cognitive_process

   .. automethod:: ObjectiveForm.get_objective_form_record



Objective List
--------------

.. autoclass:: ObjectiveList
   :show-inheritance:

   .. autoattribute:: ObjectiveList.next_objective

   .. automethod:: ObjectiveList.get_next_objectives



Activity
--------

.. autoclass:: Activity
   :show-inheritance:

   .. autoattribute:: Activity.objective_id

   .. autoattribute:: Activity.objective

   .. automethod:: Activity.is_asset_based_activity

   .. autoattribute:: Activity.asset_ids

   .. autoattribute:: Activity.assets

   .. automethod:: Activity.is_course_based_activity

   .. autoattribute:: Activity.course_ids

   .. autoattribute:: Activity.courses

   .. automethod:: Activity.is_assessment_based_activity

   .. autoattribute:: Activity.assessment_ids

   .. autoattribute:: Activity.assessments

   .. automethod:: Activity.get_activity_record



Activity Form
-------------

.. autoclass:: ActivityForm
   :show-inheritance:

   .. autoattribute:: ActivityForm.assets_metadata

   .. autoattribute:: ActivityForm.assets

   .. autoattribute:: ActivityForm.courses_metadata

   .. autoattribute:: ActivityForm.courses

   .. autoattribute:: ActivityForm.assessments_metadata

   .. autoattribute:: ActivityForm.assessments

   .. automethod:: ActivityForm.get_activity_form_record



Activity List
-------------

.. autoclass:: ActivityList
   :show-inheritance:

   .. autoattribute:: ActivityList.next_activity

   .. automethod:: ActivityList.get_next_activities



Objective Bank Form
-------------------

.. autoclass:: ObjectiveBankForm
   :show-inheritance:

   .. automethod:: ObjectiveBankForm.get_objective_bank_form_record



Objective Bank List
-------------------

.. autoclass:: ObjectiveBankList
   :show-inheritance:

   .. autoattribute:: ObjectiveBankList.next_objective_bank

   .. automethod:: ObjectiveBankList.get_next_objective_banks



