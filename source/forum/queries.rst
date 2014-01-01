.. currentmodule:: dlkit.forum.queries
.. automodule:: dlkit.forum.queries

Queries
=======


Post Query
----------

.. autoclass:: PostQuery
   :show-inheritance:

   .. automethod:: PostQuery.match_timestamp

   .. autoattribute:: PostQuery.timestamp_terms

   .. automethod:: PostQuery.match_poster_id

   .. autoattribute:: PostQuery.poster_id_terms

   .. automethod:: PostQuery.supports_poster_query

   .. autoattribute:: PostQuery.poster_query

   .. autoattribute:: PostQuery.poster_terms

   .. automethod:: PostQuery.match_posting_agent_id

   .. autoattribute:: PostQuery.posting_agent_id_terms

   .. automethod:: PostQuery.supports_posting_agent_query

   .. autoattribute:: PostQuery.posting_agent_query

   .. autoattribute:: PostQuery.posting_agent_terms

   .. automethod:: PostQuery.match_subject_line

   .. automethod:: PostQuery.match_any_subject_line

   .. autoattribute:: PostQuery.subject_line_terms

   .. automethod:: PostQuery.match_text

   .. automethod:: PostQuery.match_any_text

   .. autoattribute:: PostQuery.text_terms

   .. automethod:: PostQuery.match_reply_id

   .. autoattribute:: PostQuery.reply_id_terms

   .. automethod:: PostQuery.supports_reply_query

   .. autoattribute:: PostQuery.reply_query

   .. automethod:: PostQuery.match_any_reply

   .. autoattribute:: PostQuery.reply_terms

   .. automethod:: PostQuery.match_forum_id

   .. autoattribute:: PostQuery.forum_id_terms

   .. automethod:: PostQuery.supports_forum_query

   .. autoattribute:: PostQuery.forum_query

   .. autoattribute:: PostQuery.forum_terms

   .. automethod:: PostQuery.get_post_query_record



Reply Query
-----------

.. autoclass:: ReplyQuery
   :show-inheritance:

   .. automethod:: ReplyQuery.match_post_id

   .. autoattribute:: ReplyQuery.post_id_terms

   .. automethod:: ReplyQuery.supports_post_query

   .. autoattribute:: ReplyQuery.post_query

   .. autoattribute:: ReplyQuery.post_terms

   .. automethod:: ReplyQuery.match_timestamp

   .. autoattribute:: ReplyQuery.timestamp_terms

   .. automethod:: ReplyQuery.match_poster_id

   .. autoattribute:: ReplyQuery.poster_id_terms

   .. automethod:: ReplyQuery.supports_poster_query

   .. autoattribute:: ReplyQuery.poster_query

   .. autoattribute:: ReplyQuery.poster_terms

   .. automethod:: ReplyQuery.match_posting_agent_id

   .. autoattribute:: ReplyQuery.posting_agent_id_terms

   .. automethod:: ReplyQuery.supports_posting_agent_query

   .. autoattribute:: ReplyQuery.posting_agent_query

   .. autoattribute:: ReplyQuery.posting_agent_terms

   .. automethod:: ReplyQuery.match_subject_line

   .. automethod:: ReplyQuery.match_any_subject_line

   .. autoattribute:: ReplyQuery.subject_line_terms

   .. automethod:: ReplyQuery.match_text

   .. automethod:: ReplyQuery.match_any_text

   .. autoattribute:: ReplyQuery.text_terms

   .. automethod:: ReplyQuery.match_containing_reply_id

   .. autoattribute:: ReplyQuery.containing_reply_id_terms

   .. automethod:: ReplyQuery.supports_containing_reply_query

   .. autoattribute:: ReplyQuery.containing_reply_query

   .. automethod:: ReplyQuery.match_any_containing_reply

   .. autoattribute:: ReplyQuery.containing_reply_terms

   .. automethod:: ReplyQuery.match_contained_reply_id

   .. autoattribute:: ReplyQuery.contained_reply_id_terms

   .. automethod:: ReplyQuery.supports_contained_reply_query

   .. autoattribute:: ReplyQuery.contained_reply_query

   .. automethod:: ReplyQuery.match_any_contained_reply

   .. autoattribute:: ReplyQuery.contained_reply_terms

   .. automethod:: ReplyQuery.match_forum_id

   .. autoattribute:: ReplyQuery.forum_id_terms

   .. automethod:: ReplyQuery.supports_forum_query

   .. autoattribute:: ReplyQuery.forum_query

   .. autoattribute:: ReplyQuery.forum_terms

   .. automethod:: ReplyQuery.get_reply_query_record



Forum Query
-----------

.. autoclass:: ForumQuery
   :show-inheritance:

   .. automethod:: ForumQuery.match_reply_id

   .. autoattribute:: ForumQuery.reply_id_terms

   .. automethod:: ForumQuery.supports_reply_query

   .. autoattribute:: ForumQuery.reply_query

   .. automethod:: ForumQuery.match_any_reply

   .. autoattribute:: ForumQuery.reply_terms

   .. automethod:: ForumQuery.match_post_id

   .. autoattribute:: ForumQuery.post_id_terms

   .. automethod:: ForumQuery.supports_post_query

   .. autoattribute:: ForumQuery.post_query

   .. automethod:: ForumQuery.match_any_post

   .. autoattribute:: ForumQuery.post_terms

   .. automethod:: ForumQuery.match_ancestor_forum_id

   .. autoattribute:: ForumQuery.ancestor_forum_id_terms

   .. automethod:: ForumQuery.supports_ancestor_forum_query

   .. autoattribute:: ForumQuery.ancestor_forum_query

   .. automethod:: ForumQuery.match_any_ancestor_forum

   .. autoattribute:: ForumQuery.ancestor_forum_terms

   .. automethod:: ForumQuery.match_descendant_forum_id

   .. autoattribute:: ForumQuery.descendant_forum_id_terms

   .. automethod:: ForumQuery.supports_descendant_forum_query

   .. autoattribute:: ForumQuery.descendant_forum_query

   .. automethod:: ForumQuery.match_any_descendant_forum

   .. autoattribute:: ForumQuery.descendant_forum_terms

   .. automethod:: ForumQuery.get_forum_query_record



