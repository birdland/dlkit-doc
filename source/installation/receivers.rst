.. currentmodule:: dlkit.installation.receivers
.. automodule:: dlkit.installation.receivers

Receivers
=========


Package Receiver
----------------

.. autoclass:: PackageReceiver
   :show-inheritance:

   .. automethod:: PackageReceiver.new_package

   .. automethod:: PackageReceiver.changed_package

   .. automethod:: PackageReceiver.deleted_package



Depot Receiver
--------------

.. autoclass:: DepotReceiver
   :show-inheritance:

   .. automethod:: DepotReceiver.new_depot

   .. automethod:: DepotReceiver.new_ancestor_depot

   .. automethod:: DepotReceiver.new_descendant_depot

   .. automethod:: DepotReceiver.changed_depot

   .. automethod:: DepotReceiver.deleted_depot

   .. automethod:: DepotReceiver.deleted_ancestor_depot

   .. automethod:: DepotReceiver.deleted_descendant_depot



Installation Receiver
---------------------

.. autoclass:: InstallationReceiver
   :show-inheritance:

   .. automethod:: InstallationReceiver.new_installation

   .. automethod:: InstallationReceiver.deleted_installation



