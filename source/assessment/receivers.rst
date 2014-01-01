.. currentmodule:: dlkit.assessment.receivers
.. automodule:: dlkit.assessment.receivers

Receivers
=========


Item Receiver
-------------

.. autoclass:: ItemReceiver
   :show-inheritance:

   .. automethod:: ItemReceiver.new_item

   .. automethod:: ItemReceiver.changed_item

   .. automethod:: ItemReceiver.deleted_item



Assessment Receiver
-------------------

.. autoclass:: AssessmentReceiver
   :show-inheritance:

   .. automethod:: AssessmentReceiver.new_assessment

   .. automethod:: AssessmentReceiver.changed_assessment

   .. automethod:: AssessmentReceiver.deleted_assessment



Assessment Offered Receiver
---------------------------

.. autoclass:: AssessmentOfferedReceiver
   :show-inheritance:

   .. automethod:: AssessmentOfferedReceiver.new_assessment_offered

   .. automethod:: AssessmentOfferedReceiver.changed_assessment_offered

   .. automethod:: AssessmentOfferedReceiver.deleted_assessment_offered



Assessment Taken Receiver
-------------------------

.. autoclass:: AssessmentTakenReceiver
   :show-inheritance:

   .. automethod:: AssessmentTakenReceiver.new_assessment_taken

   .. automethod:: AssessmentTakenReceiver.changed_assessment_taken

   .. automethod:: AssessmentTakenReceiver.deleted_assessment_taken



Bank Receiver
-------------

.. autoclass:: BankReceiver
   :show-inheritance:

   .. automethod:: BankReceiver.new_bank

   .. automethod:: BankReceiver.new_ancestor_bank

   .. automethod:: BankReceiver.new_descendant_bank

   .. automethod:: BankReceiver.changed_bank

   .. automethod:: BankReceiver.deleted_bank

   .. automethod:: BankReceiver.deleted_ancestor_bank

   .. automethod:: BankReceiver.deleted_descendant_bank



