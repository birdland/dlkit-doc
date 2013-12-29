.. currentmodule:: dlkit_doc.relationship
.. automodule:: dlkit_doc.relationship

Family
======


Family
------

.. autoclass:: Family
   :show-inheritance:

.. automethod:: Family.get_family_record



Relationship Lookup Methods
---------------------------

.. autoattribute:: Family.family_id

.. autoattribute:: Family.family

.. automethod:: Family.can_lookup_relationships

.. automethod:: Family.use_comparative_relationship_view

.. automethod:: Family.use_plenary_relationship_view

.. automethod:: Family.use_federated_family_view

.. automethod:: Family.use_isolated_family_view

.. automethod:: Family.use_effective_relationship_view

.. automethod:: Family.use_any_effective_relationship_view

.. automethod:: Family.get_relationship

.. automethod:: Family.get_relationships_by_ids

.. automethod:: Family.get_relationships_by_genus_type

.. automethod:: Family.get_relationships_by_parent_genus_type

.. automethod:: Family.get_relationships_by_record_type

.. automethod:: Family.get_relationships_on_date

.. automethod:: Family.get_relationships_for_source

.. automethod:: Family.get_relationships_for_source_on_date

.. automethod:: Family.get_relationships_by_genus_type_for_source

.. automethod:: Family.get_relationships_by_genus_type_for_source_on_date

.. automethod:: Family.get_relationships_for_destination

.. automethod:: Family.get_relationships_for_destination_on_date

.. automethod:: Family.get_relationships_by_genus_type_for_destination

.. automethod:: Family.get_relationships_by_genus_type_for_destination_on_date

.. automethod:: Family.get_relationships_for_peers

.. automethod:: Family.get_relationships_for_peers_on_date

.. automethod:: Family.get_relationships_by_genus_type_for_peers

.. automethod:: Family.get_relationships_by_genus_type_for_peers_on_date

.. autoattribute:: Family.relationships



Relationship Query Methods
--------------------------

.. autoattribute:: Family.family_id

.. autoattribute:: Family.family

.. automethod:: Family.use_federated_family_view

.. automethod:: Family.use_isolated_family_view

.. automethod:: Family.can_search_relationships

.. autoattribute:: Family.relationship_query

.. automethod:: Family.get_relationships_by_query



Relationship Search Methods
---------------------------

.. autoattribute:: Family.relationship_search

.. autoattribute:: Family.relationship_search_order

.. automethod:: Family.get_relationships_by_search

.. automethod:: Family.get_relationship_query_from_inspector



Relationship Admin Methods
--------------------------

.. autoattribute:: Family.family_id

.. autoattribute:: Family.family

.. automethod:: Family.can_create_relationships

.. automethod:: Family.can_create_relationship_with_record_types

.. automethod:: Family.get_relationship_form_for_create

.. automethod:: Family.create_relationship

.. automethod:: Family.can_update_relationships

.. automethod:: Family.get_relationship_form_for_update

.. automethod:: Family.update_relationship

.. automethod:: Family.can_delete_relationships

.. automethod:: Family.delete_relationship

.. automethod:: Family.can_manage_relationship_aliases

.. automethod:: Family.alias_relationship



Relationship Notification Methods
---------------------------------

.. autoattribute:: Family.family_id

.. autoattribute:: Family.family

.. automethod:: Family.can_register_for_relationship_notifications

.. automethod:: Family.use_federated_family_view

.. automethod:: Family.use_isolated_family_view

.. automethod:: Family.register_for_new_relationships

.. automethod:: Family.register_for_new_relationships_for_peer

.. automethod:: Family.register_for_new_relationships_by_genus_type

.. automethod:: Family.register_for_changed_relationships

.. automethod:: Family.register_for_changed_relationships_for_peer

.. automethod:: Family.register_for_changed_relationships_by_genus_type

.. automethod:: Family.register_for_changed_relationship

.. automethod:: Family.register_for_deleted_relationships

.. automethod:: Family.register_for_deleted_relationships_for_peer

.. automethod:: Family.register_for_deleted_relationships_by_genus_type

.. automethod:: Family.register_for_deleted_relationship



Relationship Family Methods
---------------------------

.. automethod:: Family.can_lookup_relationship_family_mappings

.. automethod:: Family.use_comparative_family_view

.. automethod:: Family.use_plenary_family_view

.. automethod:: Family.get_relationship_ids_by_family

.. automethod:: Family.get_relationships_by_family

.. automethod:: Family.get_relationship_ids_by_families

.. automethod:: Family.get_relationships_by_families

.. automethod:: Family.get_family_ids_by_relationship

.. automethod:: Family.get_families_by_relationship



Relationship Family Assignment Methods
--------------------------------------

.. automethod:: Family.can_assign_relationships

.. automethod:: Family.can_assign_relationships_to_family

.. automethod:: Family.get_assignable_family_ids

.. automethod:: Family.get_assignable_family_ids_for_relationship

.. automethod:: Family.assign_relationship_to_family

.. automethod:: Family.unassign_relationship_from_family



Relationship Smart Family Methods
---------------------------------

.. autoattribute:: Family.family_id

.. autoattribute:: Family.family

.. automethod:: Family.can_manage_smart_families

.. autoattribute:: Family.relationship_query

.. autoattribute:: Family.relationship_search_order

.. automethod:: Family.apply_relationship_query

.. automethod:: Family.inspect_relationship_query

.. automethod:: Family.apply_relationship_sequencing

.. automethod:: Family.get_relationship_query_from_inspector



