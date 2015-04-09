Summary
=======
.. currentmodule:: dlkit.services.type
.. automodule:: dlkit.services.type

Service Managers
================


Type Manager
------------

.. autoclass:: TypeManager
   :show-inheritance:





Type
____

   .. automethod:: TypeManager.supports_type_lookup

   .. automethod:: TypeManager.supports_type_admin



Type
____





Type Proxy
__________





Type Lookup
___________

   .. automethod:: TypeManager.can_lookup_types

   .. automethod:: TypeManager.get_type

   .. automethod:: TypeManager.has_type

   .. automethod:: TypeManager.get_types_by_domain

   .. automethod:: TypeManager.get_types_by_authority

   .. automethod:: TypeManager.get_types_by_domain_and_authority

   .. autoattribute:: TypeManager.types

   .. automethod:: TypeManager.is_equivalent

   .. automethod:: TypeManager.implies_support

   .. automethod:: TypeManager.has_base_type

   .. automethod:: TypeManager.get_base_types

   .. autoattribute:: TypeManager.relation_types

   .. automethod:: TypeManager.get_source_types_by_relation_type

   .. automethod:: TypeManager.get_destination_types_by_source

   .. automethod:: TypeManager.get_destination_types_by_source_and_relation_type

   .. automethod:: TypeManager.get_destination_types_by_relation_type

   .. automethod:: TypeManager.get_source_types_by_destination

   .. automethod:: TypeManager.get_source_types_by_destination_and_relation_type



Type Admin
__________

   .. automethod:: TypeManager.can_create_types

   .. automethod:: TypeManager.get_type_form_for_create

   .. automethod:: TypeManager.create_type

   .. automethod:: TypeManager.can_update_types

   .. automethod:: TypeManager.get_type_form_for_update

   .. automethod:: TypeManager.update_type

   .. automethod:: TypeManager.can_delete_types

   .. automethod:: TypeManager.can_delete_type

   .. automethod:: TypeManager.delete_type

   .. automethod:: TypeManager.make_equivalent

   .. automethod:: TypeManager.add_base_type

   .. automethod:: TypeManager.remove_base_type

   .. automethod:: TypeManager.add_type_relation

   .. automethod:: TypeManager.remove_type_relation






   .. autoattribute:: TypeManager.display_name

   .. autoattribute:: TypeManager.display_label

   .. autoattribute:: TypeManager.description

   .. autoattribute:: TypeManager.domain

   .. autoattribute:: TypeManager.authority

   .. autoattribute:: TypeManager.namespace

   .. autoattribute:: TypeManager.identifier



Type
____

   .. autoattribute:: TypeManager.display_name_metadata

   .. autoattribute:: TypeManager.display_name

   .. autoattribute:: TypeManager.display_label_metadata

   .. autoattribute:: TypeManager.display_label

   .. autoattribute:: TypeManager.description_metadata

   .. autoattribute:: TypeManager.description

   .. autoattribute:: TypeManager.domain_metadata

   .. autoattribute:: TypeManager.domain



Type
____

   .. autoattribute:: TypeManager.next_type

   .. automethod:: TypeManager.get_next_types



Type Proxy Manager
------------------

.. autoclass:: TypeProxyManager
   :show-inheritance:





Type
____

   .. automethod:: TypeProxyManager.supports_type_lookup

   .. automethod:: TypeProxyManager.supports_type_admin



Type
____





Type Proxy
__________





Type Lookup
___________

   .. automethod:: TypeProxyManager.can_lookup_types

   .. automethod:: TypeProxyManager.get_type

   .. automethod:: TypeProxyManager.has_type

   .. automethod:: TypeProxyManager.get_types_by_domain

   .. automethod:: TypeProxyManager.get_types_by_authority

   .. automethod:: TypeProxyManager.get_types_by_domain_and_authority

   .. autoattribute:: TypeProxyManager.types

   .. automethod:: TypeProxyManager.is_equivalent

   .. automethod:: TypeProxyManager.implies_support

   .. automethod:: TypeProxyManager.has_base_type

   .. automethod:: TypeProxyManager.get_base_types

   .. autoattribute:: TypeProxyManager.relation_types

   .. automethod:: TypeProxyManager.get_source_types_by_relation_type

   .. automethod:: TypeProxyManager.get_destination_types_by_source

   .. automethod:: TypeProxyManager.get_destination_types_by_source_and_relation_type

   .. automethod:: TypeProxyManager.get_destination_types_by_relation_type

   .. automethod:: TypeProxyManager.get_source_types_by_destination

   .. automethod:: TypeProxyManager.get_source_types_by_destination_and_relation_type



Type Admin
__________

   .. automethod:: TypeProxyManager.can_create_types

   .. automethod:: TypeProxyManager.get_type_form_for_create

   .. automethod:: TypeProxyManager.create_type

   .. automethod:: TypeProxyManager.can_update_types

   .. automethod:: TypeProxyManager.get_type_form_for_update

   .. automethod:: TypeProxyManager.update_type

   .. automethod:: TypeProxyManager.can_delete_types

   .. automethod:: TypeProxyManager.can_delete_type

   .. automethod:: TypeProxyManager.delete_type

   .. automethod:: TypeProxyManager.make_equivalent

   .. automethod:: TypeProxyManager.add_base_type

   .. automethod:: TypeProxyManager.remove_base_type

   .. automethod:: TypeProxyManager.add_type_relation

   .. automethod:: TypeProxyManager.remove_type_relation






   .. autoattribute:: TypeProxyManager.display_name

   .. autoattribute:: TypeProxyManager.display_label

   .. autoattribute:: TypeProxyManager.description

   .. autoattribute:: TypeProxyManager.domain

   .. autoattribute:: TypeProxyManager.authority

   .. autoattribute:: TypeProxyManager.namespace

   .. autoattribute:: TypeProxyManager.identifier



Type
____

   .. autoattribute:: TypeProxyManager.display_name_metadata

   .. autoattribute:: TypeProxyManager.display_name

   .. autoattribute:: TypeProxyManager.display_label_metadata

   .. autoattribute:: TypeProxyManager.display_label

   .. autoattribute:: TypeProxyManager.description_metadata

   .. autoattribute:: TypeProxyManager.description

   .. autoattribute:: TypeProxyManager.domain_metadata

   .. autoattribute:: TypeProxyManager.domain



Type
____

   .. autoattribute:: TypeProxyManager.next_type

   .. automethod:: TypeProxyManager.get_next_types



