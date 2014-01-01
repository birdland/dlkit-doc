.. currentmodule:: dlkit.forum.objects
.. automodule:: dlkit.forum.objects

Objects
=======


Post
----

.. autoclass:: Post
   :show-inheritance:

   .. autoattribute:: Post.timestamp

   .. autoattribute:: Post.poster_id

   .. autoattribute:: Post.poster

   .. autoattribute:: Post.posting_agent_id

   .. autoattribute:: Post.posting_agent

   .. autoattribute:: Post.subject_line

   .. autoattribute:: Post.text

   .. automethod:: Post.get_post_record



Post Form
---------

.. autoclass:: PostForm
   :show-inheritance:

   .. autoattribute:: PostForm.subject_line_metadata

   .. autoattribute:: PostForm.timestamp

   .. autoattribute:: PostForm.subject_line

   .. autoattribute:: PostForm.text_metadata

   .. autoattribute:: PostForm.text

   .. automethod:: PostForm.get_post_form_record



Post List
---------

.. autoclass:: PostList
   :show-inheritance:

   .. autoattribute:: PostList.next_post

   .. automethod:: PostList.get_next_posts



Reply
-----

.. autoclass:: Reply
   :show-inheritance:

   .. autoattribute:: Reply.post_id

   .. autoattribute:: Reply.post

   .. autoattribute:: Reply.reply_ids

   .. autoattribute:: Reply.replies

   .. autoattribute:: Reply.timestamp

   .. autoattribute:: Reply.poster_id

   .. autoattribute:: Reply.poster

   .. autoattribute:: Reply.posting_agent_id

   .. autoattribute:: Reply.posting_agent

   .. autoattribute:: Reply.subject_line

   .. autoattribute:: Reply.text

   .. automethod:: Reply.get_reply_record



Reply Form
----------

.. autoclass:: ReplyForm
   :show-inheritance:

   .. autoattribute:: ReplyForm.subject_line_metadata

   .. autoattribute:: ReplyForm.timestamp

   .. autoattribute:: ReplyForm.subject_line

   .. autoattribute:: ReplyForm.text_metadata

   .. autoattribute:: ReplyForm.text

   .. automethod:: ReplyForm.get_reply_form_record



Reply List
----------

.. autoclass:: ReplyList
   :show-inheritance:

   .. autoattribute:: ReplyList.next_reply

   .. automethod:: ReplyList.get_next_replies



Forum Form
----------

.. autoclass:: ForumForm
   :show-inheritance:

   .. automethod:: ForumForm.get_forum_form_record



Forum List
----------

.. autoclass:: ForumList
   :show-inheritance:

   .. autoattribute:: ForumList.next_forum

   .. automethod:: ForumList.get_next_forums



Forum Node
----------

.. autoclass:: ForumNode
   :show-inheritance:

   .. autoattribute:: ForumNode.forum

   .. autoattribute:: ForumNode.parent_forum_nodes

   .. autoattribute:: ForumNode.child_forum_nodes



Forum Node List
---------------

.. autoclass:: ForumNodeList
   :show-inheritance:

   .. autoattribute:: ForumNodeList.next_forum_node

   .. automethod:: ForumNodeList.get_next_forum_nodes



