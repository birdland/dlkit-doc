.. currentmodule:: dlkit.repository.objects
.. automodule:: dlkit.repository.objects

Objects
=======


Asset
-----

.. autoclass:: Asset
   :show-inheritance:

   .. autoattribute:: Asset.title

   .. automethod:: Asset.is_copyright_status_known

   .. automethod:: Asset.is_public_domain

   .. autoattribute:: Asset.copyright

   .. autoattribute:: Asset.copyright_registration

   .. automethod:: Asset.can_distribute_verbatim

   .. automethod:: Asset.can_distribute_alterations

   .. automethod:: Asset.can_distribute_compositions

   .. autoattribute:: Asset.source_id

   .. autoattribute:: Asset.source

   .. autoattribute:: Asset.provider_link_ids

   .. autoattribute:: Asset.provider_links

   .. autoattribute:: Asset.created_date

   .. automethod:: Asset.is_published

   .. autoattribute:: Asset.published_date

   .. autoattribute:: Asset.principal_credit_string

   .. autoattribute:: Asset.asset_content_ids

   .. autoattribute:: Asset.asset_contents

   .. automethod:: Asset.is_composition

   .. autoattribute:: Asset.composition_id

   .. autoattribute:: Asset.composition

   .. automethod:: Asset.get_asset_record



Asset Form
----------

.. autoclass:: AssetForm
   :show-inheritance:

   .. autoattribute:: AssetForm.title_metadata

   .. autoattribute:: AssetForm.title

   .. autoattribute:: AssetForm.public_domain_metadata

   .. autoattribute:: AssetForm.public_domain

   .. autoattribute:: AssetForm.copyright_metadata

   .. autoattribute:: AssetForm.copyright

   .. autoattribute:: AssetForm.copyright_registration_metadata

   .. autoattribute:: AssetForm.copyright_registration

   .. autoattribute:: AssetForm.distribute_verbatim_metadata

   .. autoattribute:: AssetForm.distribute_verbatim

   .. autoattribute:: AssetForm.distribute_alterations_metadata

   .. autoattribute:: AssetForm.distribute_alterations

   .. autoattribute:: AssetForm.distribute_compositions_metadata

   .. autoattribute:: AssetForm.distribute_compositions

   .. autoattribute:: AssetForm.source_metadata

   .. autoattribute:: AssetForm.source

   .. autoattribute:: AssetForm.provider_links_metadata

   .. autoattribute:: AssetForm.provider_links

   .. autoattribute:: AssetForm.created_date_metadata

   .. autoattribute:: AssetForm.created_date

   .. autoattribute:: AssetForm.published_metadata

   .. autoattribute:: AssetForm.published

   .. autoattribute:: AssetForm.published_date_metadata

   .. autoattribute:: AssetForm.published_date

   .. autoattribute:: AssetForm.principal_credit_string_metadata

   .. autoattribute:: AssetForm.principal_credit_string

   .. autoattribute:: AssetForm.composition_metadata

   .. autoattribute:: AssetForm.composition

   .. automethod:: AssetForm.get_asset_form_record



Asset List
----------

.. autoclass:: AssetList
   :show-inheritance:

   .. autoattribute:: AssetList.next_asset

   .. automethod:: AssetList.get_next_assets



Asset Content
-------------

.. autoclass:: AssetContent
   :show-inheritance:

   .. autoattribute:: AssetContent.asset_id

   .. autoattribute:: AssetContent.asset

   .. autoattribute:: AssetContent.accessibility_types

   .. automethod:: AssetContent.has_data_length

   .. autoattribute:: AssetContent.data_length

   .. autoattribute:: AssetContent.data

   .. automethod:: AssetContent.has_url

   .. autoattribute:: AssetContent.url

   .. automethod:: AssetContent.get_asset_content_record



Asset Content Form
------------------

.. autoclass:: AssetContentForm
   :show-inheritance:

   .. autoattribute:: AssetContentForm.accessibility_type_metadata

   .. automethod:: AssetContentForm.add_accessibility_type

   .. automethod:: AssetContentForm.remove_accessibility_type

   .. autoattribute:: AssetContentForm.accessibility_types

   .. autoattribute:: AssetContentForm.data_metadata

   .. autoattribute:: AssetContentForm.data

   .. autoattribute:: AssetContentForm.url_metadata

   .. autoattribute:: AssetContentForm.url

   .. automethod:: AssetContentForm.get_asset_content_form_record



Asset Content List
------------------

.. autoclass:: AssetContentList
   :show-inheritance:

   .. autoattribute:: AssetContentList.next_asset_content

   .. automethod:: AssetContentList.get_next_asset_contents



Repository Form
---------------

.. autoclass:: RepositoryForm
   :show-inheritance:

   .. automethod:: RepositoryForm.get_repository_form_record



Repository List
---------------

.. autoclass:: RepositoryList
   :show-inheritance:

   .. autoattribute:: RepositoryList.next_repository

   .. automethod:: RepositoryList.get_next_repositories



