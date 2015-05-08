from ..osid import query_inspectors as osid_query_inspectors


class CommentQueryInspector(osid_query_inspectors.OsidRelationshipQueryInspector):
    """The comment query inspector for examining comment queries."""
    def get_reference_id_terms(self):
        """Gets the reference ``Id`` terms.

        :return: the reference ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    reference_id_terms = property(fget=get_reference_id_terms)

    def get_commentor_id_terms(self):
        """Gets the resource ``Id`` terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    commentor_id_terms = property(fget=get_commentor_id_terms)

    def get_commentor_terms(self):
        """Gets the resource terms.

        :return: the resource terms
        :rtype: ``osid.resource.ResourceQueryInspector``

        """
        return # osid.resource.ResourceQueryInspector

    commentor_terms = property(fget=get_commentor_terms)

    def get_commenting_agent_id_terms(self):
        """Gets the agent ``Id`` terms.

        :return: the agent ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    commenting_agent_id_terms = property(fget=get_commenting_agent_id_terms)

    def get_commenting_agent_terms(self):
        """Gets the agent terms.

        :return: the agent terms
        :rtype: ``osid.authentication.AgentQueryInspector``

        """
        return # osid.authentication.AgentQueryInspector

    commenting_agent_terms = property(fget=get_commenting_agent_terms)

    def get_text_terms(self):
        """Gets the text query terms.

        :return: the text query terms
        :rtype: ``osid.search.terms.StringTerm``

        """
        return # osid.search.terms.StringTerm

    text_terms = property(fget=get_text_terms)

    def get_rating_id_terms(self):
        """Gets the rating ``Id`` terms.

        :return: the rating ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    rating_id_terms = property(fget=get_rating_id_terms)

    def get_rating_terms(self):
        """Gets the rating terms.

        :return: the rating terms
        :rtype: ``osid.grading.GradeQueryInspector``

        """
        return # osid.grading.GradeQueryInspector

    rating_terms = property(fget=get_rating_terms)

    def get_book_id_terms(self):
        """Gets the book ``Id`` terms.

        :return: the book ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    book_id_terms = property(fget=get_book_id_terms)

    def get_book_terms(self):
        """Gets the book terms.

        :return: the book terms
        :rtype: ``osid.commenting.BookQueryInspector``

        """
        return # osid.commenting.BookQueryInspector

    book_terms = property(fget=get_book_terms)

    def get_comment_query_inspector_record(self, comment_record_type):
        """Gets the comment query inspector record corresponding to the given ``Comment`` record ``Type``.

        :param comment_record_type: a comment record type
        :type comment_record_type: ``osid.type.Type``
        :return: the comment query inspector record
        :rtype: ``osid.commenting.records.CommentQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``comment_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(comment_record_type)`` is ``false``

        """
        return # osid.commenting.records.CommentQueryInspectorRecord


class BookQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining bok queries."""
    def get_comment_id_terms(self):
        """Gets the comment ``Id`` terms.

        :return: the comment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    comment_id_terms = property(fget=get_comment_id_terms)

    def get_comment_terms(self):
        """Gets the comment terms.

        :return: the comment terms
        :rtype: ``osid.commenting.CommentQueryInspector``

        """
        return # osid.commenting.CommentQueryInspector

    comment_terms = property(fget=get_comment_terms)

    def get_ancestor_book_id_terms(self):
        """Gets the ancestor book ``Id`` terms.

        :return: the ancestor book ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_book_id_terms = property(fget=get_ancestor_book_id_terms)

    def get_ancestor_book_terms(self):
        """Gets the ancestor book terms.

        :return: the ancestor book terms
        :rtype: ``osid.commenting.BookQueryInspector``

        """
        return # osid.commenting.BookQueryInspector

    ancestor_book_terms = property(fget=get_ancestor_book_terms)

    def get_descendant_book_id_terms(self):
        """Gets the descendant book ``Id`` terms.

        :return: the descendant book ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_book_id_terms = property(fget=get_descendant_book_id_terms)

    def get_descendant_book_terms(self):
        """Gets the descendant book terms.

        :return: the descendant book terms
        :rtype: ``osid.commenting.BookQueryInspector``

        """
        return # osid.commenting.BookQueryInspector

    descendant_book_terms = property(fget=get_descendant_book_terms)

    def get_book_query_inspector_record(self, book_record_type):
        """Gets the book query inspector record corresponding to the given ``Book`` record ``Type``.

        :param book_record_type: a book record type
        :type book_record_type: ``osid.type.Type``
        :return: the book query inspector record
        :rtype: ``osid.commenting.records.BookQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``book_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(book_record_type)`` is ``false``

        """
        return # osid.commenting.records.BookQueryInspectorRecord


