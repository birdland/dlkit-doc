
.. currentmodule:: dlkit.services.logging
.. automodule:: dlkit.services.logging

Service Managers
================


Logging Profile
---------------

.. autoclass:: LoggingProfile
   :show-inheritance:

   .. automethod:: LoggingProfile.supports_logging

   .. automethod:: LoggingProfile.supports_log_entry_lookup

   .. automethod:: LoggingProfile.supports_log_entry_query

   .. automethod:: LoggingProfile.supports_log_lookup

   .. automethod:: LoggingProfile.supports_log_admin

   .. autoattribute:: LoggingProfile.log_entry_record_types

   .. autoattribute:: LoggingProfile.log_entry_search_record_types

   .. autoattribute:: LoggingProfile.log_record_types

   .. autoattribute:: LoggingProfile.log_search_record_types

   .. autoattribute:: LoggingProfile.priority_types

   .. autoattribute:: LoggingProfile.content_types

   .. automethod:: LoggingProfile.supports_log_entry_admin

Logging Manager
---------------

.. autoclass:: LoggingManager
   :show-inheritance:

   .. autoattribute:: LoggingManager.logging_batch_manager



Logging Methods
---------------

   .. autoattribute:: LoggingManager.log_id

   .. autoattribute:: LoggingManager.log

   .. automethod:: LoggingManager.can_log

   .. automethod:: LoggingManager.log

   .. automethod:: LoggingManager.log_at_priority

   .. autoattribute:: LoggingManager.log_entry_form

   .. automethod:: LoggingManager.create_log_entry



Log Entry Lookup Methods
------------------------

   .. autoattribute:: LoggingManager.log_id

   .. autoattribute:: LoggingManager.log

   .. automethod:: LoggingManager.can_read_log

   .. automethod:: LoggingManager.use_comparative_log_entry_view

   .. automethod:: LoggingManager.use_plenary_log_entry_view

   .. automethod:: LoggingManager.use_federated_log_view

   .. automethod:: LoggingManager.use_isolated_log_view

   .. automethod:: LoggingManager.get_log_entry

   .. automethod:: LoggingManager.get_log_entries_by_ids

   .. automethod:: LoggingManager.get_log_entries_by_genus_type

   .. automethod:: LoggingManager.get_log_entries_by_parent_genus_type

   .. automethod:: LoggingManager.get_log_entries_by_record_type

   .. automethod:: LoggingManager.get_log_entries_by_priority_type

   .. automethod:: LoggingManager.get_log_entries_by_date

   .. automethod:: LoggingManager.get_log_entries_by_priority_type_and_date

   .. automethod:: LoggingManager.get_log_entries_for_resource

   .. automethod:: LoggingManager.get_log_entries_by_date_for_resource

   .. automethod:: LoggingManager.get_log_entries_by_priority_type_and_date_for_resource

   .. autoattribute:: LoggingManager.log_entries



Log Entry Query Methods
-----------------------

   .. autoattribute:: LoggingManager.log_id

   .. autoattribute:: LoggingManager.log

   .. automethod:: LoggingManager.can_search_log_entries

   .. automethod:: LoggingManager.use_federated_log_view

   .. automethod:: LoggingManager.use_isolated_log_view

   .. autoattribute:: LoggingManager.log_entry_query

   .. automethod:: LoggingManager.get_log_entries_by_query



Log Entry Admin Methods
-----------------------

   .. autoattribute:: LoggingManager.log_id

   .. autoattribute:: LoggingManager.log

   .. automethod:: LoggingManager.can_create_log_entries

   .. automethod:: LoggingManager.can_create_log_entry_with_record_types

   .. automethod:: LoggingManager.get_log_entry_form_for_create

   .. automethod:: LoggingManager.create_log_entry

   .. automethod:: LoggingManager.can_update_log_entries

   .. automethod:: LoggingManager.get_log_entry_form_for_update

   .. automethod:: LoggingManager.update_log_entry

   .. automethod:: LoggingManager.can_delete_log_entries

   .. automethod:: LoggingManager.delete_log_entry

   .. automethod:: LoggingManager.can_manage_log_entry_aliases

   .. automethod:: LoggingManager.alias_log_entry



Log Lookup Methods
------------------

   .. automethod:: LoggingManager.can_lookup_logs

   .. automethod:: LoggingManager.use_comparative_log_view

   .. automethod:: LoggingManager.use_plenary_log_view

   .. automethod:: LoggingManager.get_log

   .. automethod:: LoggingManager.get_logs_by_ids

   .. automethod:: LoggingManager.get_logs_by_genus_type

   .. automethod:: LoggingManager.get_logs_by_parent_genus_type

   .. automethod:: LoggingManager.get_logs_by_record_type

   .. automethod:: LoggingManager.get_logs_by_provider

   .. autoattribute:: LoggingManager.logs



Log Admin Methods
-----------------

   .. automethod:: LoggingManager.can_create_logs

   .. automethod:: LoggingManager.can_create_log_with_record_types

   .. automethod:: LoggingManager.get_log_form_for_create

   .. automethod:: LoggingManager.create_log

   .. automethod:: LoggingManager.can_update_logs

   .. automethod:: LoggingManager.get_log_form_for_update

   .. automethod:: LoggingManager.update_log

   .. automethod:: LoggingManager.can_delete_logs

   .. automethod:: LoggingManager.delete_log

   .. automethod:: LoggingManager.can_manage_log_aliases

   .. automethod:: LoggingManager.alias_log



