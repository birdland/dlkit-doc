.. currentmodule:: dlkit.abstract_osid.ontology.search_orders
.. automodule:: dlkit.abstract_osid.ontology.search_orders

Search_Orders
=============


Subject Search Order
--------------------

.. autoclass:: SubjectSearchOrder
   :show-inheritance:

.. automethod:: SubjectSearchOrder.get_subject_search_order_record



Relevancy Search Order
----------------------

.. autoclass:: RelevancySearchOrder
   :show-inheritance:

.. automethod:: RelevancySearchOrder.order_by_subject

.. automethod:: RelevancySearchOrder.supports_subject_search_order

.. autoattribute:: RelevancySearchOrder.subject_search_order

.. automethod:: RelevancySearchOrder.get_relevancy_search_order_record



Ontology Search Order
---------------------

.. autoclass:: OntologySearchOrder
   :show-inheritance:

.. automethod:: OntologySearchOrder.get_ontology_search_order_record



