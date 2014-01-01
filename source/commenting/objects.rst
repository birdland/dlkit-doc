.. currentmodule:: dlkit.commenting.objects
.. automodule:: dlkit.commenting.objects

Objects
=======


Comment
-------

.. autoclass:: Comment
   :show-inheritance:

   .. autoattribute:: Comment.reference_id

   .. autoattribute:: Comment.commentor_id

   .. autoattribute:: Comment.commentor

   .. autoattribute:: Comment.commenting_agent_id

   .. autoattribute:: Comment.commenting_agent

   .. autoattribute:: Comment.text

   .. automethod:: Comment.has_rating

   .. autoattribute:: Comment.rating_id

   .. autoattribute:: Comment.rating

   .. automethod:: Comment.get_comment_record



Comment Form
------------

.. autoclass:: CommentForm
   :show-inheritance:

   .. autoattribute:: CommentForm.text_metadata

   .. autoattribute:: CommentForm.text

   .. autoattribute:: CommentForm.rating_metadata

   .. autoattribute:: CommentForm.rating

   .. automethod:: CommentForm.get_comment_form_record



Comment List
------------

.. autoclass:: CommentList
   :show-inheritance:

   .. autoattribute:: CommentList.next_comment

   .. automethod:: CommentList.get_next_comments



Book Form
---------

.. autoclass:: BookForm
   :show-inheritance:

   .. automethod:: BookForm.get_book_form_record



Book List
---------

.. autoclass:: BookList
   :show-inheritance:

   .. autoattribute:: BookList.next_book

   .. automethod:: BookList.get_next_books



Book Node
---------

.. autoclass:: BookNode
   :show-inheritance:

   .. autoattribute:: BookNode.book

   .. autoattribute:: BookNode.parent_book_nodes

   .. autoattribute:: BookNode.child_book_nodes



Book Node List
--------------

.. autoclass:: BookNodeList
   :show-inheritance:

   .. autoattribute:: BookNodeList.next_book_node

   .. automethod:: BookNodeList.get_next_book_nodes



