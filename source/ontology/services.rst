.. currentmodule:: dlkit.services.ontology
.. automodule:: dlkit.services.ontology

Services
========


Ontology Manager
----------------

.. autoclass:: OntologyManager
   :show-inheritance:

   .. autoattribute:: OntologyManager.ontology_batch_manager

   .. autoattribute:: OntologyManager.ontology_rules_manager



Ontology Profile Methods
________________

   .. automethod:: OntologyManager.supports_visible_federation

   .. automethod:: OntologyManager.supports_subject_lookup

   .. automethod:: OntologyManager.supports_subject_query

   .. automethod:: OntologyManager.supports_subject_search

   .. automethod:: OntologyManager.supports_subject_admin

   .. automethod:: OntologyManager.supports_subject_notification

   .. automethod:: OntologyManager.supports_subject_hierarchy

   .. automethod:: OntologyManager.supports_subject_hierarchy_design

   .. automethod:: OntologyManager.supports_subject_ontology

   .. automethod:: OntologyManager.supports_subject_ontology_assignment

   .. automethod:: OntologyManager.supports_subject_smart_ontology

   .. automethod:: OntologyManager.supports_relevancy_lookup

   .. automethod:: OntologyManager.supports_relevancy_query

   .. automethod:: OntologyManager.supports_relevancy_search

   .. automethod:: OntologyManager.supports_relevancy_admin

   .. automethod:: OntologyManager.supports_relevancy_notification

   .. automethod:: OntologyManager.supports_ontology_lookup

   .. automethod:: OntologyManager.supports_relevancy_ontology

   .. automethod:: OntologyManager.supports_relevancy_ontology_assignment

   .. automethod:: OntologyManager.supports_relevancy_smart_ontology

   .. automethod:: OntologyManager.supports_ontology_query

   .. automethod:: OntologyManager.supports_ontology_search

   .. automethod:: OntologyManager.supports_ontology_admin

   .. automethod:: OntologyManager.supports_ontology_notification

   .. automethod:: OntologyManager.supports_ontology_hierarchy

   .. automethod:: OntologyManager.supports_ontology_hierarchy_design

   .. automethod:: OntologyManager.supports_ontology_assignment

   .. automethod:: OntologyManager.supports_ontology_batch

   .. automethod:: OntologyManager.supports_ontology_rules

   .. autoattribute:: OntologyManager.subject_record_types

   .. automethod:: OntologyManager.supports_subject_record_type

   .. autoattribute:: OntologyManager.subject_search_record_types

   .. automethod:: OntologyManager.supports_subject_search_record_type

   .. autoattribute:: OntologyManager.relevancy_record_types

   .. automethod:: OntologyManager.supports_relevancy_record_type

   .. autoattribute:: OntologyManager.relevancy_search_record_types

   .. automethod:: OntologyManager.supports_relevancy_search_record_type

   .. autoattribute:: OntologyManager.ontology_record_types

   .. automethod:: OntologyManager.supports_ontology_record_type

   .. autoattribute:: OntologyManager.ontology_search_record_types

   .. automethod:: OntologyManager.supports_ontology_search_record_type



Ontology Lookup
_______________

   .. automethod:: OntologyManager.can_lookup_ontologies

   .. automethod:: OntologyManager.use_comparative_ontology_view

   .. automethod:: OntologyManager.use_plenary_ontology_view

   .. automethod:: OntologyManager.get_ontology

   .. automethod:: OntologyManager.get_ontologies_by_ids

   .. automethod:: OntologyManager.get_ontologies_by_genus_type

   .. automethod:: OntologyManager.get_ontologies_by_parent_genus_type

   .. automethod:: OntologyManager.get_ontologies_by_record_type

   .. automethod:: OntologyManager.get_ontologies_by_provider

   .. autoattribute:: OntologyManager.ontologies



Ontology Query
______________

   .. automethod:: OntologyManager.can_search_ontologies

   .. autoattribute:: OntologyManager.ontology_query

   .. automethod:: OntologyManager.get_ontologies_by_query



Ontology Search
_______________

   .. autoattribute:: OntologyManager.ontology_search

   .. autoattribute:: OntologyManager.ontology_search_order

   .. automethod:: OntologyManager.get_ontologies_by_search

   .. automethod:: OntologyManager.get_ontology_query_from_inspector



Ontology Admin
______________

   .. automethod:: OntologyManager.can_create_ontologies

   .. automethod:: OntologyManager.can_create_ontology_with_record_types

   .. automethod:: OntologyManager.get_ontology_form_for_create

   .. automethod:: OntologyManager.create_ontology

   .. automethod:: OntologyManager.can_update_ontologies

   .. automethod:: OntologyManager.get_ontology_form_for_update

   .. automethod:: OntologyManager.update_ontology

   .. automethod:: OntologyManager.can_delete_ontologies

   .. automethod:: OntologyManager.delete_ontology

   .. automethod:: OntologyManager.can_manage_ontology_aliases

   .. automethod:: OntologyManager.alias_ontology



Ontology Notification
_____________________

   .. automethod:: OntologyManager.can_register_for_ontology_notifications

   .. automethod:: OntologyManager.register_for_new_ontologies

   .. automethod:: OntologyManager.register_for_new_ontology_ancestors

   .. automethod:: OntologyManager.register_for_new_ontology_descendants

   .. automethod:: OntologyManager.register_for_changed_ontologies

   .. automethod:: OntologyManager.register_for_changed_ontology

   .. automethod:: OntologyManager.register_for_deleted_ontologies

   .. automethod:: OntologyManager.register_for_deleted_ontology

   .. automethod:: OntologyManager.register_for_deleted_ontology_ancestors

   .. automethod:: OntologyManager.register_for_deleted_ontology_descendants



Ontology Hierarchy
__________________

   .. autoattribute:: OntologyManager.ontology_hierarchy_id

   .. autoattribute:: OntologyManager.ontology_hierarchy

   .. automethod:: OntologyManager.can_access_ontology_hierarchy

   .. automethod:: OntologyManager.use_comparative_ontology_view

   .. automethod:: OntologyManager.use_plenary_ontology_view

   .. autoattribute:: OntologyManager.root_ontology_ids

   .. autoattribute:: OntologyManager.root_ontologies

   .. automethod:: OntologyManager.has_parent_ontologies

   .. automethod:: OntologyManager.is_parent_of_ontology

   .. automethod:: OntologyManager.get_parent_ontology_ids

   .. automethod:: OntologyManager.get_parent_ontologies

   .. automethod:: OntologyManager.is_ancestor_of_ontology

   .. automethod:: OntologyManager.has_child_ontologies

   .. automethod:: OntologyManager.is_child_of_ontology

   .. automethod:: OntologyManager.get_child_ontology_ids

   .. automethod:: OntologyManager.get_child_ontologies

   .. automethod:: OntologyManager.is_descendant_of_ontology

   .. automethod:: OntologyManager.get_ontology_node_ids

   .. automethod:: OntologyManager.get_ontology_nodes



Ontology Hierarchy Design
_________________________

   .. autoattribute:: OntologyManager.ontology_hierarchy_id

   .. autoattribute:: OntologyManager.ontology_hierarchy

   .. automethod:: OntologyManager.can_modify_ontology_hierarchy

   .. automethod:: OntologyManager.add_root_ontology

   .. automethod:: OntologyManager.remove_root_ontology

   .. automethod:: OntologyManager.add_child_ontology

   .. automethod:: OntologyManager.remove_child_ontology

   .. automethod:: OntologyManager.remove_child_ontologies



Ontology Assignment
___________________

   .. automethod:: OntologyManager.can_assign_ontologies

   .. automethod:: OntologyManager.assign_ontology

   .. automethod:: OntologyManager.unassign_ontology

   .. automethod:: OntologyManager.get_ontology

   .. automethod:: OntologyManager.get_ids



Ontology Proxy Manager
----------------------

.. autoclass:: OntologyProxyManager
   :show-inheritance:

   .. automethod:: OntologyProxyManager.get_subject_lookup_session

   .. automethod:: OntologyProxyManager.get_subject_lookup_session_for_ontology

   .. automethod:: OntologyProxyManager.get_subject_lookup_session_for_id

   .. automethod:: OntologyProxyManager.get_subject_query_session

   .. automethod:: OntologyProxyManager.get_subject_query_session_for_ontology

   .. automethod:: OntologyProxyManager.get_subject_search_session

   .. automethod:: OntologyProxyManager.get_subject_search_session_for_ontology

   .. automethod:: OntologyProxyManager.get_subject_admin_session

   .. automethod:: OntologyProxyManager.get_subject_admin_session_for_ontology

   .. automethod:: OntologyProxyManager.get_subject_notification_session

   .. automethod:: OntologyProxyManager.get_subject_notification_session_for_ontology

   .. automethod:: OntologyProxyManager.get_subject_hierarchy_session

   .. automethod:: OntologyProxyManager.get_subject_hierarchy_session_for_ontology

   .. automethod:: OntologyProxyManager.get_subject_hierarchy_session_for_id

   .. automethod:: OntologyProxyManager.get_subject_hierarchy_design_session

   .. automethod:: OntologyProxyManager.get_subject_hierarchy_design_session_for_ontology

   .. automethod:: OntologyProxyManager.get_subject_ontology_session

   .. automethod:: OntologyProxyManager.get_subject_ontology_assignment_session

   .. automethod:: OntologyProxyManager.get_subject_smart_ontology_session

   .. automethod:: OntologyProxyManager.get_relevancy_lookup_session

   .. automethod:: OntologyProxyManager.get_relevancy_lookup_session_for_ontology

   .. automethod:: OntologyProxyManager.get_relevancy_query_session

   .. automethod:: OntologyProxyManager.get_relevancy_query_session_for_ontology

   .. automethod:: OntologyProxyManager.get_relevancy_search_session

   .. automethod:: OntologyProxyManager.get_relevancy_search_session_for_ontology

   .. automethod:: OntologyProxyManager.get_relevancy_admin_session

   .. automethod:: OntologyProxyManager.get_relevancy_admin_session_for_ontology

   .. automethod:: OntologyProxyManager.get_relevancy_notification_session

   .. automethod:: OntologyProxyManager.get_relevancy_notification_session_for_ontology

   .. automethod:: OntologyProxyManager.get_relevancy_ontology_session

   .. automethod:: OntologyProxyManager.get_relevancy_ontology_assignment_session

   .. automethod:: OntologyProxyManager.get_relevancy_smart_ontology_session

   .. automethod:: OntologyProxyManager.get_ontology_lookup_session

   .. automethod:: OntologyProxyManager.get_ontology_query_session

   .. automethod:: OntologyProxyManager.get_ontology_search_session

   .. automethod:: OntologyProxyManager.get_ontology_admin_session

   .. automethod:: OntologyProxyManager.get_ontology_notification_session

   .. automethod:: OntologyProxyManager.get_ontology_hierarchy_session

   .. automethod:: OntologyProxyManager.get_ontology_hierarchy_design_session

   .. automethod:: OntologyProxyManager.get_ontology_assignment_session

   .. autoattribute:: OntologyProxyManager.ontology_batch_proxy_manager

   .. autoattribute:: OntologyProxyManager.ontology_rules_proxy_manager



