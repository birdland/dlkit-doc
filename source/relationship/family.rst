
.. currentmodule:: dlkit.services.relationship

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



