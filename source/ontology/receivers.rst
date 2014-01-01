.. currentmodule:: dlkit.ontology.receivers
.. automodule:: dlkit.ontology.receivers

Receivers
=========


Subject Receiver
----------------

.. autoclass:: SubjectReceiver
   :show-inheritance:

   .. automethod:: SubjectReceiver.new_subject

   .. automethod:: SubjectReceiver.new_ancestor_subject

   .. automethod:: SubjectReceiver.new_descendant_subject

   .. automethod:: SubjectReceiver.changed_subject

   .. automethod:: SubjectReceiver.deleted_subject

   .. automethod:: SubjectReceiver.deleted_ancestor_subject

   .. automethod:: SubjectReceiver.deleted_descendant_subject



Relevancy Receiver
------------------

.. autoclass:: RelevancyReceiver
   :show-inheritance:

   .. automethod:: RelevancyReceiver.new_relevancy

   .. automethod:: RelevancyReceiver.new_relevancy_for_subject

   .. automethod:: RelevancyReceiver.new_relevancy_for_id

   .. automethod:: RelevancyReceiver.changed_relevancy

   .. automethod:: RelevancyReceiver.changed_relevancy_for_subject

   .. automethod:: RelevancyReceiver.changed_relevancy_for_id

   .. automethod:: RelevancyReceiver.deleted_relevancy

   .. automethod:: RelevancyReceiver.deleted_relevancy_for_subject

   .. automethod:: RelevancyReceiver.deleted_relevancy_for_id



Ontology Receiver
-----------------

.. autoclass:: OntologyReceiver
   :show-inheritance:

   .. automethod:: OntologyReceiver.new_ontology

   .. automethod:: OntologyReceiver.new_ancestor_ontology

   .. automethod:: OntologyReceiver.new_descendant_ontology

   .. automethod:: OntologyReceiver.changed_ontology

   .. automethod:: OntologyReceiver.deleted_ontology

   .. automethod:: OntologyReceiver.deleted_ancestor_ontology

   .. automethod:: OntologyReceiver.deleted_descendant_ontology



