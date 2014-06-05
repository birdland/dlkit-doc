.. currentmodule:: dlkit.services.ontology


Ontology
========


Ontology
--------

.. autoclass:: Ontology
   :show-inheritance:

   .. automethod:: Ontology.get_ontology_record



Subject Lookup Methods
----------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_lookup_subjects

   .. automethod:: Ontology.use_comparative_subject_view

   .. automethod:: Ontology.use_plenary_subject_view

   .. automethod:: Ontology.use_federated_ontology_view

   .. automethod:: Ontology.use_isolated_ontology_view

   .. automethod:: Ontology.get_subject

   .. automethod:: Ontology.get_subjects_by_ids

   .. automethod:: Ontology.get_subjects_by_genus_type

   .. automethod:: Ontology.get_subjects_by_parent_genus_type

   .. automethod:: Ontology.get_subjects_by_record_type

   .. autoattribute:: Ontology.subjects



Subject Query Methods
---------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_search_subjects

   .. automethod:: Ontology.use_federated_ontology_view

   .. automethod:: Ontology.use_isolated_ontology_view

   .. autoattribute:: Ontology.subject_query

   .. automethod:: Ontology.get_subjects_by_query



Subject Search Methods
----------------------

   .. autoattribute:: Ontology.subject_search

   .. autoattribute:: Ontology.subject_search_order

   .. automethod:: Ontology.get_subjects_by_search

   .. automethod:: Ontology.get_subject_query_from_inspector



Subject Admin Methods
---------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_create_subjects

   .. automethod:: Ontology.can_create_subject_with_record_types

   .. automethod:: Ontology.get_subject_form_for_create

   .. automethod:: Ontology.create_subject

   .. automethod:: Ontology.can_update_subjects

   .. automethod:: Ontology.get_subject_form_for_update

   .. automethod:: Ontology.update_subject

   .. automethod:: Ontology.can_delete_subjects

   .. automethod:: Ontology.delete_subject

   .. automethod:: Ontology.can_manage_subject_aliases

   .. automethod:: Ontology.alias_subject



Subject Notification Methods
----------------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_register_for_subject_notifications

   .. automethod:: Ontology.use_federated_ontology_view

   .. automethod:: Ontology.use_isolated_ontology_view

   .. automethod:: Ontology.register_for_new_subjects

   .. automethod:: Ontology.register_for_new_subject_ancestors

   .. automethod:: Ontology.register_for_new_subject_descendants

   .. automethod:: Ontology.register_for_changed_subjects

   .. automethod:: Ontology.register_for_changed_subject

   .. automethod:: Ontology.register_for_deleted_subjects

   .. automethod:: Ontology.register_for_deleted_subject

   .. automethod:: Ontology.register_for_deleted_subject_ancestors

   .. automethod:: Ontology.register_for_deleted_subject_descendants



Subject Hierarchy Methods
-------------------------

   .. autoattribute:: Ontology.subject_hierarchy_id

   .. autoattribute:: Ontology.subject_hierarchy

   .. automethod:: Ontology.can_access_subject_hierarchy

   .. automethod:: Ontology.use_comparative_subject_view

   .. automethod:: Ontology.use_plenary_subject_view

   .. autoattribute:: Ontology.root_subject_ids

   .. autoattribute:: Ontology.root_subjects

   .. automethod:: Ontology.has_parent_subjects

   .. automethod:: Ontology.is_parent_of_subject

   .. automethod:: Ontology.get_parent_subject_ids

   .. automethod:: Ontology.get_parent_subjects

   .. automethod:: Ontology.is_ancestor_of_subject

   .. automethod:: Ontology.has_child_subjects

   .. automethod:: Ontology.is_child_of_subject

   .. automethod:: Ontology.get_child_subject_ids

   .. automethod:: Ontology.get_child_subjects

   .. automethod:: Ontology.is_descendant_of_subject

   .. automethod:: Ontology.get_subject_node_ids

   .. automethod:: Ontology.get_subject_nodes



Subject Hierarchy Design Methods
--------------------------------

   .. autoattribute:: Ontology.subject_hierarchy_id

   .. autoattribute:: Ontology.subject_hierarchy

   .. automethod:: Ontology.can_modify_subject_hierarchy

   .. automethod:: Ontology.add_root_subject

   .. automethod:: Ontology.remove_root_subject

   .. automethod:: Ontology.add_child_subject

   .. automethod:: Ontology.remove_child_subject

   .. automethod:: Ontology.remove_child_subjects



Subject Ontology Methods
------------------------

   .. automethod:: Ontology.can_lookup_subject_ontology_mappings

   .. automethod:: Ontology.use_comparative_ontology_view

   .. automethod:: Ontology.use_plenary_ontology_view

   .. automethod:: Ontology.get_subject_ids_by_ontology

   .. automethod:: Ontology.get_subjects_by_ontology

   .. automethod:: Ontology.get_subject_ids_by_ontologies

   .. automethod:: Ontology.get_subjects_by_ontologies

   .. automethod:: Ontology.get_ontology_ids_by_subject

   .. automethod:: Ontology.get_ontologies_by_subject



Subject Ontology Assignment Methods
-----------------------------------

   .. automethod:: Ontology.can_assign_subjects

   .. automethod:: Ontology.can_assign_subjects_to_ontology

   .. automethod:: Ontology.get_assignable_ontology_ids

   .. automethod:: Ontology.get_assignable_ontology_ids_for_subject

   .. automethod:: Ontology.assign_subject_to_ontology

   .. automethod:: Ontology.unassign_subject_from_ontology



Subject Smart Ontology Methods
------------------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_manage_smart_ontologies

   .. autoattribute:: Ontology.subject_query

   .. autoattribute:: Ontology.subject_search_order

   .. automethod:: Ontology.apply_subject_query

   .. automethod:: Ontology.inspect_subject_query

   .. automethod:: Ontology.apply_subject_sequencing

   .. automethod:: Ontology.get_subject_query_from_inspector



Relevancy Lookup Methods
------------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_lookup_relevancies

   .. automethod:: Ontology.use_comparative_relevancy_view

   .. automethod:: Ontology.use_plenary_relevancy_view

   .. automethod:: Ontology.use_federated_ontology_view

   .. automethod:: Ontology.use_isolated_ontology_view

   .. automethod:: Ontology.use_effective_relevancy_view

   .. automethod:: Ontology.use_any_effective_relevancy_view

   .. automethod:: Ontology.get_relevancy

   .. automethod:: Ontology.get_relevancies_by_ids

   .. automethod:: Ontology.get_relevancies_by_genus_type

   .. automethod:: Ontology.get_relevancies_by_parent_genus_type

   .. automethod:: Ontology.get_relevancies_by_record_type

   .. automethod:: Ontology.get_relevancies_on_date

   .. automethod:: Ontology.get_relevancies_by_genus_type_on_date

   .. automethod:: Ontology.get_relevancies_for_subject

   .. automethod:: Ontology.get_relevancies_for_subject_on_date

   .. automethod:: Ontology.get_relevancies_by_genus_type_for_subject

   .. automethod:: Ontology.get_relevancies_by_genus_type_for_subject_on_date

   .. automethod:: Ontology.get_relevancies_for_subjects

   .. automethod:: Ontology.get_relevancies_for_mapped_id

   .. automethod:: Ontology.get_relevancies_for_mapped_id_on_date

   .. automethod:: Ontology.get_relevancies_by_genus_type_for_mapped_id

   .. automethod:: Ontology.get_relevancies_by_genus_type_for_mapped_id_on_date

   .. automethod:: Ontology.get_relevancies_for_mapped_ids

   .. automethod:: Ontology.get_relevancies_for_subject_and_mapped_id

   .. automethod:: Ontology.get_relevancies_for_subject_and_mapped_id_on_date

   .. automethod:: Ontology.get_relevancies_by_genus_type_for_subject_and_mapped_id

   .. automethod:: Ontology.get_relevancies_by_genus_type_for_subject_and_mapped_id_on_date

   .. autoattribute:: Ontology.relevancies



Relevancy Query Methods
-----------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_search_relevancies

   .. automethod:: Ontology.use_federated_ontology_view

   .. automethod:: Ontology.use_isolated_ontology_view

   .. autoattribute:: Ontology.relevancy_query

   .. automethod:: Ontology.get_relevancies_by_query



Relevancy Search Methods
------------------------

   .. autoattribute:: Ontology.relevancy_search

   .. autoattribute:: Ontology.relevancy_search_order

   .. automethod:: Ontology.get_relevancies_by_search

   .. automethod:: Ontology.get_relevancy_query_from_inspector



Relevancy Admin Methods
-----------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_create_relevancies

   .. automethod:: Ontology.can_create_relevancy_with_record_types

   .. automethod:: Ontology.get_relevancy_form_for_create

   .. automethod:: Ontology.create_relevancy

   .. automethod:: Ontology.can_update_relevancies

   .. automethod:: Ontology.get_relevancy_form_for_update

   .. automethod:: Ontology.update_relevancy

   .. automethod:: Ontology.can_delete_relevancies

   .. automethod:: Ontology.delete_relevancy

   .. automethod:: Ontology.can_manage_relevancy_aliases

   .. automethod:: Ontology.alias_relevancy



Relevancy Notification Methods
------------------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_register_for_relevancy_notifications

   .. automethod:: Ontology.use_federated_ontology_view

   .. automethod:: Ontology.use_isolated_ontology_view

   .. automethod:: Ontology.register_for_new_relevancies

   .. automethod:: Ontology.register_for_new_relevancies_by_genus_type

   .. automethod:: Ontology.register_for_new_relevancies_for_subject

   .. automethod:: Ontology.register_for_new_relevancies_for_id

   .. automethod:: Ontology.register_for_changed_relevancies

   .. automethod:: Ontology.register_for_changed_relevancies_by_genus_type

   .. automethod:: Ontology.register_for_changed_relevancies_for_subject

   .. automethod:: Ontology.register_for_changed_relevancies_for_id

   .. automethod:: Ontology.register_for_changed_relevancy

   .. automethod:: Ontology.register_for_deleted_relevancies

   .. automethod:: Ontology.register_for_deleted_relevancies_by_genus_type

   .. automethod:: Ontology.register_for_deleted_relevancies_for_subject

   .. automethod:: Ontology.register_for_deleted_relevancies_for_id

   .. automethod:: Ontology.register_for_deleted_relevancy



Relevancy Ontology Methods
--------------------------

   .. automethod:: Ontology.can_lookup_relevancy_ontology_mappings

   .. automethod:: Ontology.use_comparative_ontology_view

   .. automethod:: Ontology.use_plenary_ontology_view

   .. automethod:: Ontology.get_relevancy_ids_by_ontology

   .. automethod:: Ontology.get_relevancies_by_ontology

   .. automethod:: Ontology.get_relevancy_ids_by_ontologies

   .. automethod:: Ontology.get_relevancies_by_ontologies

   .. automethod:: Ontology.get_ontology_ids_by_relevancy

   .. automethod:: Ontology.get_ontologies_by_relevancy



Relevancy Ontology Assignment Methods
-------------------------------------

   .. automethod:: Ontology.can_assign_relevancies

   .. automethod:: Ontology.can_assign_relevancies_to_ontology

   .. automethod:: Ontology.get_assignable_ontology_ids

   .. automethod:: Ontology.get_assignable_ontology_ids_for_relevancy

   .. automethod:: Ontology.assign_relevancy_to_ontology

   .. automethod:: Ontology.unassign_relevancy_from_ontology



Relevancy Smart Ontology Methods
--------------------------------

   .. autoattribute:: Ontology.ontology_id

   .. autoattribute:: Ontology.ontology

   .. automethod:: Ontology.can_manage_smart_ontologies

   .. autoattribute:: Ontology.relevancy_query

   .. autoattribute:: Ontology.relevancy_search_order

   .. automethod:: Ontology.apply_relevancy_query

   .. automethod:: Ontology.inspect_relevancy_query

   .. automethod:: Ontology.apply_relevancy_sequencing

   .. automethod:: Ontology.get_relevancy_query_from_inspector



