
.. currentmodule:: dlkit.logging_.objects
.. automodule:: dlkit.logging_.objects

Objects
=======


Log Entry
---------

.. autoclass:: LogEntry
   :show-inheritance:

   .. autoattribute:: LogEntry.priority

   .. autoattribute:: LogEntry.timestamp

   .. autoattribute:: LogEntry.resource_id

   .. autoattribute:: LogEntry.resource

   .. autoattribute:: LogEntry.agent_id

   .. autoattribute:: LogEntry.agent

   .. automethod:: LogEntry.get_log_entry_record

Log Entry Form
--------------

.. autoclass:: LogEntryForm
   :show-inheritance:

   .. autoattribute:: LogEntryForm.priority_metadata

   .. autoattribute:: LogEntryForm.priority

   .. autoattribute:: LogEntryForm.timestamp_metadata

   .. autoattribute:: LogEntryForm.timestamp

   .. autoattribute:: LogEntryForm.agent_metadata

   .. autoattribute:: LogEntryForm.agent

   .. automethod:: LogEntryForm.get_log_entry_form_record

Log Entry List
--------------

.. autoclass:: LogEntryList
   :show-inheritance:

   .. autoattribute:: LogEntryList.next_log_entry

   .. automethod:: LogEntryList.get_next_log_entries

Log
---

.. py:class:: Log(abc_logging_objects.Log, osid_objects.OsidCatalog)
        :noindex:

   .. automethod:: Log.get_log_record

Log Form
--------

.. autoclass:: LogForm
   :show-inheritance:

   .. automethod:: LogForm.get_log_form_record

Log List
--------

.. autoclass:: LogList
   :show-inheritance:

   .. autoattribute:: LogList.next_log

   .. automethod:: LogList.get_next_logs

Log Node
--------

.. autoclass:: LogNode
   :show-inheritance:

   .. autoattribute:: LogNode.log

   .. autoattribute:: LogNode.parent_log_nodes

   .. autoattribute:: LogNode.child_log_nodes

Log Node List
-------------

.. autoclass:: LogNodeList
   :show-inheritance:

   .. autoattribute:: LogNodeList.next_log_node

   .. automethod:: LogNodeList.get_next_log_nodes

