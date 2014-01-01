.. currentmodule:: dlkit.ontology.objects
.. automodule:: dlkit.ontology.objects

Objects
=======


Subject
-------

.. autoclass:: Subject
   :show-inheritance:

   .. automethod:: Subject.get_subject_record



Subject Form
------------

.. autoclass:: SubjectForm
   :show-inheritance:

   .. automethod:: SubjectForm.get_subject_form_record



Subject List
------------

.. autoclass:: SubjectList
   :show-inheritance:

   .. autoattribute:: SubjectList.next_subject

   .. automethod:: SubjectList.get_next_subjects



Subject Node
------------

.. autoclass:: SubjectNode
   :show-inheritance:

   .. autoattribute:: SubjectNode.subject

   .. autoattribute:: SubjectNode.parent_subject_nodes

   .. autoattribute:: SubjectNode.child_subject_nodes



Subject Node List
-----------------

.. autoclass:: SubjectNodeList
   :show-inheritance:

   .. autoattribute:: SubjectNodeList.next_subject_node

   .. automethod:: SubjectNodeList.get_next_subject_nodes



Relevancy
---------

.. autoclass:: Relevancy
   :show-inheritance:

   .. autoattribute:: Relevancy.subject_id

   .. autoattribute:: Relevancy.subject

   .. autoattribute:: Relevancy.mapped_id

   .. automethod:: Relevancy.get_relevancy_record



Relevancy Form
--------------

.. autoclass:: RelevancyForm
   :show-inheritance:

   .. automethod:: RelevancyForm.get_relevancy_form_record



Relevancy List
--------------

.. autoclass:: RelevancyList
   :show-inheritance:

   .. autoattribute:: RelevancyList.next_relevancy

   .. automethod:: RelevancyList.get_next_relevancies



Ontology Form
-------------

.. autoclass:: OntologyForm
   :show-inheritance:

   .. automethod:: OntologyForm.get_ontology_form_record



Ontology List
-------------

.. autoclass:: OntologyList
   :show-inheritance:

   .. autoattribute:: OntologyList.next_ontology

   .. automethod:: OntologyList.get_next_ontologies



Ontology Node
-------------

.. autoclass:: OntologyNode
   :show-inheritance:

   .. autoattribute:: OntologyNode.ontology

   .. autoattribute:: OntologyNode.parent_ontology_nodes

   .. autoattribute:: OntologyNode.child_ontology_nodes



Ontology Node List
------------------

.. autoclass:: OntologyNodeList
   :show-inheritance:

   .. autoattribute:: OntologyNodeList.next_ontology_node

   .. automethod:: OntologyNodeList.get_next_ontology_nodes



