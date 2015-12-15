

Objects
=======


Comment
-------

.. py:class:: Comment(abc_commenting_objects.Comment, osid_objects.OsidRelationship)
    A ``Comment`` represents a comment and/or rating related to a reference object in a book.

    .. py:method:: get_reference_id():
        :noindex:


    .. py:attribute:: reference_id
        :noindex:


    .. py:method:: get_commentor_id():
        :noindex:


    .. py:attribute:: commentor_id
        :noindex:


    .. py:method:: get_commentor():
        :noindex:


    .. py:attribute:: commentor
        :noindex:


    .. py:method:: get_commenting_agent_id():
        :noindex:


    .. py:attribute:: commenting_agent_id
        :noindex:


    .. py:method:: get_commenting_agent():
        :noindex:


    .. py:attribute:: commenting_agent
        :noindex:


    .. py:method:: get_text():
        :noindex:


    .. py:attribute:: text
        :noindex:


    .. py:method:: has_rating():
        :noindex:


    .. py:method:: get_rating_id():
        :noindex:


    .. py:attribute:: rating_id
        :noindex:


    .. py:method:: get_rating():
        :noindex:


    .. py:attribute:: rating
        :noindex:


    .. py:method:: get_comment_record(comment_record_type):
        :noindex:


Comment Form
------------

.. py:class:: CommentForm(abc_commenting_objects.CommentForm, osid_objects.OsidRelationshipForm)
    This is the form for creating and updating ``Comment`` objects.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``CommentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_text_metadata():
        :noindex:


    .. py:attribute:: text_metadata
        :noindex:


    .. py:method:: set_text(text):
        :noindex:


    .. py:method:: clear_text():
        :noindex:


    .. py:attribute:: text
        :noindex:


    .. py:method:: get_rating_metadata():
        :noindex:


    .. py:attribute:: rating_metadata
        :noindex:


    .. py:method:: set_rating(grade_id):
        :noindex:


    .. py:method:: clear_rating():
        :noindex:


    .. py:attribute:: rating
        :noindex:


    .. py:method:: get_comment_form_record(comment_record_type):
        :noindex:


Comment List
------------

.. py:class:: CommentList(abc_commenting_objects.CommentList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``CommentList`` provides a means for accessing ``Comment`` elements
    sequentially either one at a time or many at a time.


    Examples: while (cl.hasNext()) { Comment comment =
    cl.getNextComment(); }




    or
      while (cl.hasNext()) {
           Comment[] comments = cl.getNextComments(cl.available());
      }









    .. py:method:: get_next_comment():
        :noindex:


    .. py:attribute:: next_comment
        :noindex:


    .. py:method:: get_next_comments(n):
        :noindex:


Book
----

.. py:class:: Book(abc_commenting_objects.Book, osid_objects.OsidCatalog)
        :noindex:

    .. py:method:: get_book_record(book_record_type):
        :noindex:


Book Form
---------

.. py:class:: BookForm(abc_commenting_objects.BookForm, osid_objects.OsidCatalogForm)
    This is the form for creating and updating ``Books``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``BookAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.





    .. py:method:: get_book_form_record(book_record_type):
        :noindex:


Book List
---------

.. py:class:: BookList(abc_commenting_objects.BookList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``BookList`` provides a means for accessing ``Book`` elements
        sequentially
    either one at a time or many at a time.


    Examples: while (bl.hasNext()) { Book book = bl.getNextBook(); }




    or
      while (bl.hasNext()) {
           Book[] books = bl.getNextBooks(bl.available());
      }









    .. py:method:: get_next_book():
        :noindex:


    .. py:attribute:: next_book
        :noindex:


    .. py:method:: get_next_books(n):
        :noindex:


Book Node
---------

.. py:class:: BookNode(abc_commenting_objects.BookNode, osid_objects.OsidNode)
    This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BookHierarchySession``.





    .. py:method:: get_book():
        :noindex:


    .. py:attribute:: book
        :noindex:


    .. py:method:: get_parent_book_nodes():
        :noindex:


    .. py:attribute:: parent_book_nodes
        :noindex:


    .. py:method:: get_child_book_nodes():
        :noindex:


    .. py:attribute:: child_book_nodes
        :noindex:


Book Node List
--------------

.. py:class:: BookNodeList(abc_commenting_objects.BookNodeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``BookNodeList`` provides a means for accessing ``BookNode`` elements
    sequentially either one at a time or many at a time.


    Examples: while (bnl.hasNext()) { BookNode node =
    bnl.getNextBookNode(); }




    or
      while (bnl.hasNext()) {
           BookNode[] nodes = bnl.getNextBookNodes(bnl.available());
      }









    .. py:method:: get_next_book_node():
        :noindex:


    .. py:attribute:: next_book_node
        :noindex:


    .. py:method:: get_next_book_nodes(n):
        :noindex:


