.. currentmodule:: dlkit.abstract_osid.ontology.query_inspectors
.. automodule:: dlkit.abstract_osid.ontology.query_inspectors

Query_Inspectors
================


Subject Query Inspector
-----------------------

.. autoclass:: SubjectQueryInspector
   :show-inheritance:

.. autoattribute:: SubjectQueryInspector.ancestor_subject_id_terms

.. autoattribute:: SubjectQueryInspector.ancestor_subject_terms

.. autoattribute:: SubjectQueryInspector.descendant_subject_id_terms

.. autoattribute:: SubjectQueryInspector.descendant_subject_terms

.. autoattribute:: SubjectQueryInspector.relevancy_id_terms

.. autoattribute:: SubjectQueryInspector.relevancy_terms

.. autoattribute:: SubjectQueryInspector.ontology_id_terms

.. autoattribute:: SubjectQueryInspector.ontology_terms

.. automethod:: SubjectQueryInspector.get_subject_query_inspector_record



Relevancy Query Inspector
-------------------------

.. autoclass:: RelevancyQueryInspector
   :show-inheritance:

.. autoattribute:: RelevancyQueryInspector.subject_id_terms

.. autoattribute:: RelevancyQueryInspector.subject_terms

.. autoattribute:: RelevancyQueryInspector.mapped_id_terms

.. autoattribute:: RelevancyQueryInspector.ontology_id_terms

.. autoattribute:: RelevancyQueryInspector.ontology_terms

.. automethod:: RelevancyQueryInspector.get_relevancy_query_inspector_record



Ontology Query Inspector
------------------------

.. autoclass:: OntologyQueryInspector
   :show-inheritance:

.. autoattribute:: OntologyQueryInspector.subject_id_terms

.. autoattribute:: OntologyQueryInspector.subject_terms

.. autoattribute:: OntologyQueryInspector.relevancy_id_terms

.. autoattribute:: OntologyQueryInspector.relevancy_terms

.. autoattribute:: OntologyQueryInspector.ancestor_ontology_id_terms

.. autoattribute:: OntologyQueryInspector.ancestor_ontology_terms

.. autoattribute:: OntologyQueryInspector.descendant_ontology_id_terms

.. autoattribute:: OntologyQueryInspector.descendant_ontology_terms

.. automethod:: OntologyQueryInspector.get_ontology_query_inspector_record



