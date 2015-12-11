
from ..osid import queries as osid_queries


class CommentQuery(osid_queries.OsidRelationshipQuery):
    """This is the query for searching comments.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    



    def match_reference_id(self, source_id, match):
        """Sets reference ``Id``.

        arg:    source_id (osid.id.Id): a source ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``source_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_reference_id_terms(self):
        """Clears the reference ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    reference_id_terms = property(fdel=clear_reference_id_terms)


    def match_commentor_id(self, resource_id, match):
        """Sets a resource ``Id`` to match a commentor.

        arg:    resource_id (osid.id.Id): a resource ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``resource_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_commentor_id_terms(self):
        """Clears the resource ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    commentor_id_terms = property(fdel=clear_commentor_id_terms)


    def supports_commentor_query(self):
        """Tests if a ``ResourceQuery`` is available.

        return: (boolean) - ``true`` if a resource query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_commentor_query(self):
        """Gets the query for a resource query.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.resource.ResourceQuery) - the resource query
        raise:  Unimplemented - ``supports_commentor_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_commentor_query()`` is ``true``.*

        """
        return # osid.resource.ResourceQuery

    commentor_query = property(fget=get_commentor_query)


    def clear_commentor_terms(self):
        """Clears the resource terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    commentor_terms = property(fdel=clear_commentor_terms)


    def match_commenting_agent_id(self, agent_id, match):
        """Sets an agent ``Id``.

        arg:    agent_id (osid.id.Id): an agent ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``agent_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_commenting_agent_id_terms(self):
        """Clears the agent ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    commenting_agent_id_terms = property(fdel=clear_commenting_agent_id_terms)


    def supports_commenting_agent_query(self):
        """Tests if an ``AgentQuery`` is available.

        return: (boolean) - ``true`` if an agent query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_commenting_agent_query(self):
        """Gets the query for an agent query.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.authentication.AgentQuery) - the agent query
        raise:  Unimplemented - ``supports_commenting_agent_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_commenting_agent_query()`` is ``true``.*

        """
        return # osid.authentication.AgentQuery

    commenting_agent_query = property(fget=get_commenting_agent_query)


    def clear_commenting_agent_terms(self):
        """Clears the agent terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    commenting_agent_terms = property(fdel=clear_commenting_agent_terms)


    def match_text(self, text, string_match_type, match):
        """Matches text.

        arg:    text (string): the text
        arg:    string_match_type (osid.type.Type): a string match type
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  InvalidArgument - ``text`` is not of
                ``string_match_type``
        raise:  NullArgument - ``text`` is ``null``
        raise:  Unsupported -
                ``supports_string_match_type(string_match_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def match_any_text(self, match):
        """Matches a comment that has any text assigned.

        arg:    match (boolean): ``true`` to match comments with any
                text, ``false`` to match comments with no text
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_text_terms(self):
        """Clears the text terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    text_terms = property(fdel=clear_text_terms)


    def match_rating_id(self, grade_id, match):
        """Sets a grade ``Id``.

        arg:    grade_id (osid.id.Id): a grade ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``grade_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_rating_id_terms(self):
        """Clears the rating ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rating_id_terms = property(fdel=clear_rating_id_terms)


    def supports_rating_query(self):
        """Tests if a ``GradeQuery`` is available.

        return: (boolean) - ``true`` if a rating query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_rating_query(self):
        """Gets the query for a rating query.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.grading.GradeQuery) - the rating query
        raise:  Unimplemented - ``supports_rating_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_rating_query()`` is ``true``.*

        """
        return # osid.grading.GradeQuery

    rating_query = property(fget=get_rating_query)


    def match_any_rating(self, match):
        """Matches books with any rating.

        arg:    match (boolean): ``true`` to match comments with any
                rating, ``false`` to match comments with no ratings
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_rating_terms(self):
        """Clears the rating terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    rating_terms = property(fdel=clear_rating_terms)


    def match_book_id(self, book_id, match):
        """Sets the book ``Id`` for this query to match comments assigned to books.

        arg:    book_id (osid.id.Id): a book ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``book_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_book_id_terms(self):
        """Clears the book ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    book_id_terms = property(fdel=clear_book_id_terms)


    def supports_book_query(self):
        """Tests if a ``BookQuery`` is available.

        return: (boolean) - ``true`` if a book query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_book_query(self):
        """Gets the query for a book query.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.commenting.BookQuery) - the book query
        raise:  Unimplemented - ``supports_book_query()`` is ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_book_query()`` is ``true``.*

        """
        return # osid.commenting.BookQuery

    book_query = property(fget=get_book_query)


    def clear_book_terms(self):
        """Clears the book terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    book_terms = property(fdel=clear_book_terms)


    def get_comment_query_record(self, comment_record_type):
        """Gets the comment query record corresponding to the given ``Comment`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        arg:    comment_record_type (osid.type.Type): a comment record
                type
        return: (osid.commenting.records.CommentQueryRecord) - the
                comment query record
        raise:  NullArgument - ``comment_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(comment_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.records.CommentQueryRecord


class BookQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching books.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    



    def match_comment_id(self, comment_id, match):
        """Sets the comment ``Id`` for this query to match comments assigned to books.

        arg:    comment_id (osid.id.Id): a comment ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``comment_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_comment_id_terms(self):
        """Clears the comment ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    comment_id_terms = property(fdel=clear_comment_id_terms)


    def supports_comment_query(self):
        """Tests if a comment query is available.

        return: (boolean) - ``true`` if a comment query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_comment_query(self):
        """Gets the query for a comment.

        return: (osid.commenting.CommentQuery) - the comment query
        raise:  Unimplemented - ``supports_comment_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_comment_query()`` is ``true``.*

        """
        return # osid.commenting.CommentQuery

    comment_query = property(fget=get_comment_query)


    def match_any_comment(self, match):
        """Matches books with any comment.

        arg:    match (boolean): ``true`` to match books with any
                comment, ``false`` to match books with no comments
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_comment_terms(self):
        """Clears the comment terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    comment_terms = property(fdel=clear_comment_terms)


    def match_ancestor_book_id(self, book_id, match):
        """Sets the book ``Id`` for this query to match books that have the specified book as an ancestor.

        arg:    book_id (osid.id.Id): a book ``Id``
        arg:    match (boolean): ``true`` for a positive match, a
                ``false`` for a negative match
        raise:  NullArgument - ``book_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ancestor_book_id_terms(self):
        """Clears the ancestor book ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_book_id_terms = property(fdel=clear_ancestor_book_id_terms)


    def supports_ancestor_book_query(self):
        """Tests if a ``BookQuery`` is available.

        return: (boolean) - ``true`` if a book query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_ancestor_book_query(self):
        """Gets the query for a book.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.commenting.BookQuery) - the book query
        raise:  Unimplemented - ``supports_ancestor_book_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_ancestor_book_query()`` is ``true``.*

        """
        return # osid.commenting.BookQuery

    ancestor_book_query = property(fget=get_ancestor_book_query)


    def match_any_ancestor_book(self, match):
        """Matches books with any ancestor.

        arg:    match (boolean): ``true`` to match books with any
                ancestor, ``false`` to match root books
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_ancestor_book_terms(self):
        """Clears the ancestor book terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    ancestor_book_terms = property(fdel=clear_ancestor_book_terms)


    def match_descendant_book_id(self, book_id, match):
        """Sets the book ``Id`` for this query to match books that have the specified book as a descendant.

        arg:    book_id (osid.id.Id): a book ``Id``
        arg:    match (boolean): ``true`` for a positive match,
                ``false`` for a negative match
        raise:  NullArgument - ``book_id`` is ``null``
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_descendant_book_id_terms(self):
        """Clears the descendant book ``Id`` terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_book_id_terms = property(fdel=clear_descendant_book_id_terms)


    def supports_descendant_book_query(self):
        """Tests if a ``BookQuery`` is available.

        return: (boolean) - ``true`` if a book query is available,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean


    def get_descendant_book_query(self):
        """Gets the query for a book.

        Multiple retrievals produce a nested ``OR`` term.

        return: (osid.commenting.BookQuery) - the book query
        raise:  Unimplemented - ``supports_descendant_book_query()`` is
                ``false``
        *compliance: optional -- This method must be implemented if
        ``supports_descendant_book_query()`` is ``true``.*

        """
        return # osid.commenting.BookQuery

    descendant_book_query = property(fget=get_descendant_book_query)


    def match_any_descendant_book(self, match):
        """Matches books with any descendant.

        arg:    match (boolean): ``true`` to match books with any
                descendant, ``false`` to match leaf books
        *compliance: mandatory -- This method must be implemented.*

        """
        pass


    def clear_descendant_book_terms(self):
        """Clears the descendant book terms.

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    descendant_book_terms = property(fdel=clear_descendant_book_terms)


    def get_book_query_record(self, book_record_type):
        """Gets the book query record corresponding to the given ``Book`` record ``Type``.

        Multiple record retrievals produce a nested boolean ``OR`` term.

        arg:    book_record_type (osid.type.Type): a book record type
        return: (osid.commenting.records.BookQueryRecord) - the book
                query record
        raise:  NullArgument - ``book_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(book_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.records.BookQueryRecord


