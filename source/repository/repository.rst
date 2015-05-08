.. currentmodule:: dlkit.services.repository
.. automodule:: dlkit.services.repository

Repository
==========


Repository
----------

.. autoclass:: Repository
   :show-inheritance:

   .. automethod:: Repository.get_repository_record



Asset Lookup Methods
--------------------

   .. autoattribute:: Repository.repository_id

   .. autoattribute:: Repository.repository

   .. automethod:: Repository.can_lookup_assets

   .. automethod:: Repository.use_comparative_asset_view

   .. automethod:: Repository.use_plenary_asset_view

   .. automethod:: Repository.use_federated_repository_view

   .. automethod:: Repository.use_isolated_repository_view

   .. automethod:: Repository.get_asset

   .. automethod:: Repository.get_assets_by_ids

   .. automethod:: Repository.get_assets_by_genus_type

   .. automethod:: Repository.get_assets_by_parent_genus_type

   .. automethod:: Repository.get_assets_by_record_type

   .. automethod:: Repository.get_assets_by_provider

   .. autoattribute:: Repository.assets



Asset Query Methods
-------------------

   .. autoattribute:: Repository.repository_id

   .. autoattribute:: Repository.repository

   .. automethod:: Repository.can_search_assets

   .. automethod:: Repository.use_federated_repository_view

   .. automethod:: Repository.use_isolated_repository_view

   .. autoattribute:: Repository.asset_query

   .. automethod:: Repository.get_assets_by_query



Asset Admin Methods
-------------------

   .. autoattribute:: Repository.repository_id

   .. autoattribute:: Repository.repository

   .. automethod:: Repository.can_create_assets

   .. automethod:: Repository.can_create_asset_with_record_types

   .. automethod:: Repository.get_asset_form_for_create

   .. automethod:: Repository.create_asset

   .. automethod:: Repository.can_update_assets

   .. automethod:: Repository.get_asset_form_for_update

   .. automethod:: Repository.update_asset

   .. automethod:: Repository.can_delete_assets

   .. automethod:: Repository.delete_asset

   .. automethod:: Repository.can_manage_asset_aliases

   .. automethod:: Repository.alias_asset

   .. automethod:: Repository.can_create_asset_content

   .. automethod:: Repository.can_create_asset_content_with_record_types

   .. automethod:: Repository.get_asset_content_form_for_create

   .. automethod:: Repository.create_asset_content

   .. automethod:: Repository.can_update_asset_contents

   .. automethod:: Repository.get_asset_content_form_for_update

   .. automethod:: Repository.update_asset_content

   .. automethod:: Repository.can_delete_asset_contents

   .. automethod:: Repository.delete_asset_content



