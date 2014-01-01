.. currentmodule:: dlkit.repository.receivers
.. automodule:: dlkit.repository.receivers

Receivers
=========


Asset Receiver
--------------

.. autoclass:: AssetReceiver
   :show-inheritance:

   .. automethod:: AssetReceiver.new_asset

   .. automethod:: AssetReceiver.changed_asset

   .. automethod:: AssetReceiver.deleted_asset



Composition Receiver
--------------------

.. autoclass:: CompositionReceiver
   :show-inheritance:

   .. automethod:: CompositionReceiver.new_composition

   .. automethod:: CompositionReceiver.new_composition_asset

   .. automethod:: CompositionReceiver.new_composition_ancestor

   .. automethod:: CompositionReceiver.new_composition_descendant

   .. automethod:: CompositionReceiver.changed_composition

   .. automethod:: CompositionReceiver.deleted_composition

   .. automethod:: CompositionReceiver.deleted_composition_asset

   .. automethod:: CompositionReceiver.deleted_composition_ancestor

   .. automethod:: CompositionReceiver.deleted_composition_descendant



Repository Receiver
-------------------

.. autoclass:: RepositoryReceiver
   :show-inheritance:

   .. automethod:: RepositoryReceiver.new_repository

   .. automethod:: RepositoryReceiver.new_ancestor_repository

   .. automethod:: RepositoryReceiver.new_descendant_repository

   .. automethod:: RepositoryReceiver.changed_repository

   .. automethod:: RepositoryReceiver.deleted_repository

   .. automethod:: RepositoryReceiver.deleted_ancestor_repository

   .. automethod:: RepositoryReceiver.deleted_descendant_repository



