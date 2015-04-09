.. currentmodule:: dlkit.forum.query_inspectors
.. automodule:: dlkit.forum.query_inspectors

Query Inspectors
================


Post Query Inspector
--------------------

.. autoclass:: PostQueryInspector
   :show-inheritance:

   .. autoattribute:: PostQueryInspector.timestamp_terms

   .. autoattribute:: PostQueryInspector.poster_id_terms

   .. autoattribute:: PostQueryInspector.poster_terms

   .. autoattribute:: PostQueryInspector.posting_agent_id_terms

   .. autoattribute:: PostQueryInspector.posting_agent_terms

   .. autoattribute:: PostQueryInspector.subject_line_terms

   .. autoattribute:: PostQueryInspector.text_terms

   .. autoattribute:: PostQueryInspector.reply_id_terms

   .. autoattribute:: PostQueryInspector.reply_terms

   .. autoattribute:: PostQueryInspector.forum_id_terms

   .. autoattribute:: PostQueryInspector.forum_terms

   .. automethod:: PostQueryInspector.get_post_query_inspector_record



Reply Query Inspector
---------------------

.. autoclass:: ReplyQueryInspector
   :show-inheritance:

   .. autoattribute:: ReplyQueryInspector.post_id_terms

   .. autoattribute:: ReplyQueryInspector.post_terms

   .. autoattribute:: ReplyQueryInspector.timestamp_terms

   .. autoattribute:: ReplyQueryInspector.poster_id_terms

   .. autoattribute:: ReplyQueryInspector.poster_terms

   .. autoattribute:: ReplyQueryInspector.posting_agent_id_terms

   .. autoattribute:: ReplyQueryInspector.posting_agent_terms

   .. autoattribute:: ReplyQueryInspector.subject_line_terms

   .. autoattribute:: ReplyQueryInspector.text_terms

   .. autoattribute:: ReplyQueryInspector.containing_reply_id_terms

   .. autoattribute:: ReplyQueryInspector.containing_reply_terms

   .. autoattribute:: ReplyQueryInspector.contained_reply_id_terms

   .. autoattribute:: ReplyQueryInspector.contained_reply_terms

   .. autoattribute:: ReplyQueryInspector.forum_id_terms

   .. autoattribute:: ReplyQueryInspector.forum_terms

   .. automethod:: ReplyQueryInspector.get_reply_query_inspector_record



Forum Query Inspector
---------------------

.. autoclass:: ForumQueryInspector
   :show-inheritance:

   .. autoattribute:: ForumQueryInspector.reply_id_terms

   .. autoattribute:: ForumQueryInspector.reply_terms

   .. autoattribute:: ForumQueryInspector.post_id_terms

   .. autoattribute:: ForumQueryInspector.post_terms

   .. autoattribute:: ForumQueryInspector.ancestor_forum_id_terms

   .. autoattribute:: ForumQueryInspector.ancestor_forum_terms

   .. autoattribute:: ForumQueryInspector.descendant_forum_id_terms

   .. autoattribute:: ForumQueryInspector.descendant_forum_terms

   .. automethod:: ForumQueryInspector.get_forum_query_inspector_record



