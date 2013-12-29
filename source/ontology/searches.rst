.. currentmodule:: dlkit.ontology.searches
.. automodule:: dlkit.ontology.searches

Searches
========


Subject Search
--------------

.. autoclass:: SubjectSearch
   :show-inheritance:

.. automethod:: SubjectSearch.search_among_subjects

.. automethod:: SubjectSearch.order_subject_results

.. automethod:: SubjectSearch.get_subject_search_record



Subject Search Results
----------------------

.. autoclass:: SubjectSearchResults
   :show-inheritance:

.. autoattribute:: SubjectSearchResults.subjects

.. autoattribute:: SubjectSearchResults.subject_query_inspector

.. automethod:: SubjectSearchResults.get_subject_search_results_record



Relevancy Search
----------------

.. autoclass:: RelevancySearch
   :show-inheritance:

.. automethod:: RelevancySearch.search_among_relevancies

.. automethod:: RelevancySearch.order_relevancy_results

.. automethod:: RelevancySearch.get_relevancy_search_record



Relevancy Search Results
------------------------

.. autoclass:: RelevancySearchResults
   :show-inheritance:

.. autoattribute:: RelevancySearchResults.relevancies

.. autoattribute:: RelevancySearchResults.relevancy_query_inspector

.. automethod:: RelevancySearchResults.get_relevancy_search_results_record



Ontology Search
---------------

.. autoclass:: OntologySearch
   :show-inheritance:

.. automethod:: OntologySearch.search_among_ontologies

.. automethod:: OntologySearch.order_ontology_results

.. automethod:: OntologySearch.get_ontology_search_record



Ontology Search Results
-----------------------

.. autoclass:: OntologySearchResults
   :show-inheritance:

.. autoattribute:: OntologySearchResults.ontologies

.. autoattribute:: OntologySearchResults.ontology_query_inspector

.. automethod:: OntologySearchResults.get_ontology_search_results_record



