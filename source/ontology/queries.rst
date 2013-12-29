.. currentmodule:: dlkit.ontology.queries
.. automodule:: dlkit.ontology.queries

Queries
=======


Subject Query
-------------

.. autoclass:: SubjectQuery
   :show-inheritance:

.. automethod:: SubjectQuery.match_ancestor_subject_id

.. autoattribute:: SubjectQuery.ancestor_subject_id_terms

.. automethod:: SubjectQuery.supports_ancestor_subject_query

.. autoattribute:: SubjectQuery.ancestor_subject_query

.. automethod:: SubjectQuery.match_any_ancestor_subject

.. autoattribute:: SubjectQuery.ancestor_subject_terms

.. automethod:: SubjectQuery.match_descendant_subject_id

.. autoattribute:: SubjectQuery.descendant_subject_id_terms

.. automethod:: SubjectQuery.supports_descendant_subject_query

.. autoattribute:: SubjectQuery.descendant_subject_query

.. automethod:: SubjectQuery.match_any_descendant_subject

.. autoattribute:: SubjectQuery.descendant_subject_terms

.. automethod:: SubjectQuery.match_relevancy_id

.. autoattribute:: SubjectQuery.relevancy_id_terms

.. automethod:: SubjectQuery.supports_relevancy_query

.. autoattribute:: SubjectQuery.relevancy_query

.. automethod:: SubjectQuery.match_any_relevancy

.. autoattribute:: SubjectQuery.relevancy_terms

.. automethod:: SubjectQuery.match_ontology_id

.. autoattribute:: SubjectQuery.ontology_id_terms

.. automethod:: SubjectQuery.supports_ontology_query

.. autoattribute:: SubjectQuery.ontology_query

.. autoattribute:: SubjectQuery.ontology_terms

.. automethod:: SubjectQuery.get_subject_query_record



Relevancy Query
---------------

.. autoclass:: RelevancyQuery
   :show-inheritance:

.. automethod:: RelevancyQuery.match_subject_id

.. autoattribute:: RelevancyQuery.subject_id_terms

.. automethod:: RelevancyQuery.supports_subject_query

.. autoattribute:: RelevancyQuery.subject_query

.. autoattribute:: RelevancyQuery.subject_terms

.. automethod:: RelevancyQuery.match_mapped_id

.. autoattribute:: RelevancyQuery.mapped_id_terms

.. automethod:: RelevancyQuery.match_ontology_id

.. autoattribute:: RelevancyQuery.ontology_id_terms

.. automethod:: RelevancyQuery.supports_ontology_query

.. autoattribute:: RelevancyQuery.ontology_query

.. autoattribute:: RelevancyQuery.ontology_terms

.. automethod:: RelevancyQuery.get_relevancy_query_record



Ontology Query
--------------

.. autoclass:: OntologyQuery
   :show-inheritance:

.. automethod:: OntologyQuery.match_subject_id

.. autoattribute:: OntologyQuery.subject_id_terms

.. automethod:: OntologyQuery.supports_subject_query

.. autoattribute:: OntologyQuery.subject_query

.. automethod:: OntologyQuery.match_any_subject

.. autoattribute:: OntologyQuery.subject_terms

.. automethod:: OntologyQuery.match_relevancy_id

.. autoattribute:: OntologyQuery.relevancy_id_terms

.. automethod:: OntologyQuery.supports_relevancy_query

.. autoattribute:: OntologyQuery.relevancy_query

.. automethod:: OntologyQuery.match_any_relevancy

.. autoattribute:: OntologyQuery.relevancy_terms

.. automethod:: OntologyQuery.match_ancestor_ontology_id

.. autoattribute:: OntologyQuery.ancestor_ontology_id_terms

.. automethod:: OntologyQuery.supports_ancestor_ontology_query

.. autoattribute:: OntologyQuery.ancestor_ontology_query

.. automethod:: OntologyQuery.match_any_ancestor_ontology

.. autoattribute:: OntologyQuery.ancestor_ontology_terms

.. automethod:: OntologyQuery.match_descendant_ontology_id

.. autoattribute:: OntologyQuery.descendant_ontology_id_terms

.. automethod:: OntologyQuery.supports_descendant_ontology_query

.. autoattribute:: OntologyQuery.descendant_ontology_query

.. automethod:: OntologyQuery.match_any_descendant_ontology

.. autoattribute:: OntologyQuery.descendant_ontology_terms

.. automethod:: OntologyQuery.get_ontology_query_record



