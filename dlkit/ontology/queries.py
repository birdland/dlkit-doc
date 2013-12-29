from ..osid import queries as osid_queries


class SubjectQuery(osid_queries.OsidObjectQuery, osid_queries.OsidFederateableQuery):
    """This is the query for searching subjects.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_ancestor_subject_id(self, subject_id, match):
        """Sets the subject ``Id`` for this query to match subjects that have the specified subject as an ancestor.

        :param subject_id: a subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``

        """
        pass

    def clear_ancestor_subject_id_terms(self):
        """Clears the ancestor subject ``Id`` terms for this query."""
        pass

    ancestor_subject_id_terms = property(fdel=clear_ancestor_subject_id_terms)

    def supports_ancestor_subject_query(self):
        """Tests if a ``SubjectQuery`` is available.

        :return: ``true`` if a subject query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_subject_query(self):
        """Gets the query for a subject.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_subject_query()`` is ``false``

        """
        return # osid.ontology.SubjectQuery

    ancestor_subject_query = property(fget=get_ancestor_subject_query)

    def match_any_ancestor_subject(self, match):
        """Matches subjects with any ancestor.

        :param match: ``true`` to match subjects with any ancestor, ``false`` to match root subjects
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_subject_terms(self):
        """Clears the ancestor subject terms for this query."""
        pass

    ancestor_subject_terms = property(fdel=clear_ancestor_subject_terms)

    def match_descendant_subject_id(self, subject_id, match):
        """Sets the subject ``Id`` for this query to match subjects that have the specified subject as a descendant.

        :param subject_id: a subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``

        """
        pass

    def clear_descendant_subject_id_terms(self):
        """Clears the descendant subject ``Id`` terms for this query."""
        pass

    descendant_subject_id_terms = property(fdel=clear_descendant_subject_id_terms)

    def supports_descendant_subject_query(self):
        """Tests if a ``SubjectQuery`` is available.

        :return: ``true`` if a subject query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_subject_query(self):
        """Gets the query for a subject.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_subject_query()`` is ``false``

        """
        return # osid.ontology.SubjectQuery

    descendant_subject_query = property(fget=get_descendant_subject_query)

    def match_any_descendant_subject(self, match):
        """Matches subjects with any descendant.

        :param match: ``true`` to match subjects with any descendant, ``false`` to match leaf subjects
        :type match: ``boolean``

        """
        pass

    def clear_descendant_subject_terms(self):
        """Clears the descendant subject terms for this query."""
        pass

    descendant_subject_terms = property(fdel=clear_descendant_subject_terms)

    def match_relevancy_id(self, relevancy_id, match):
        """Sets the relevancy ``Id`` for this query.

        :param relevancy_id: a relevancy ``Id``
        :type relevancy_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``relevancy_id`` is ``null``

        """
        pass

    def clear_relevancy_id_terms(self):
        """Clears the relevancy ``Id`` terms for this query."""
        pass

    relevancy_id_terms = property(fdel=clear_relevancy_id_terms)

    def supports_relevancy_query(self):
        """Tests if a ``RelevancyQuery`` is available.

        :return: ``true`` if a relevancy query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_relevancy_query(self):
        """Gets the query for a relevancy.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the relevancy query
        :rtype: ``osid.ontology.RelevancyQuery``
        :raise: ``Unimplemented`` -- ``supports_relevancy_query()`` is ``false``

        """
        return # osid.ontology.RelevancyQuery

    relevancy_query = property(fget=get_relevancy_query)

    def match_any_relevancy(self, match):
        """Matches ontologies that have any relevancy.

        :param match: ``true`` to match ontologies with any relevancy, ``false`` to match ontologies with no relevancy
        :type match: ``boolean``

        """
        pass

    def clear_relevancy_terms(self):
        """Clears the relevancy terms for this query."""
        pass

    relevancy_terms = property(fdel=clear_relevancy_terms)

    def match_ontology_id(self, ontology_id, match):
        """Sets the ontology ``Id`` for this query.

        :param ontology_id: a ontology ``Id``
        :type ontology_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``

        """
        pass

    def clear_ontology_id_terms(self):
        """Clears the ontology ``Id`` terms for this query."""
        pass

    ontology_id_terms = property(fdel=clear_ontology_id_terms)

    def supports_ontology_query(self):
        """Tests if a ``OntologyQuery`` is available for querying ontologies.

        :return: ``true`` if a ontology query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ontology_query(self):
        """Gets the query for a ontology.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the ontology query
        :rtype: ``osid.ontology.OntologyQuery``
        :raise: ``Unimplemented`` -- ``supports_ontology_query()`` is ``false``

        """
        return # osid.ontology.OntologyQuery

    ontology_query = property(fget=get_ontology_query)

    def clear_ontology_terms(self):
        """Clears the ontology terms for this query."""
        pass

    ontology_terms = property(fdel=clear_ontology_terms)

    def get_subject_query_record(self, subject_record_type):
        """Gets the subject query record corresponding to the given ``Subject`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param subject_record_type: a subject query record type
        :type subject_record_type: ``osid.type.Type``
        :return: the subject query record
        :rtype: ``osid.ontology.records.SubjectQueryRecord``
        :raise: ``NullArgument`` -- ``subject_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(subject_record_type)`` is ``false``

        """
        return # osid.ontology.records.SubjectQueryRecord


class RelevancyQuery(osid_queries.OsidRelationshipQuery):
    """This is the query for searching relevancies.

    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.

    """
    def match_subject_id(self, subject_id, match):
        """Sets the subject ``Id`` for this query.

        :param subject_id: a subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``

        """
        pass

    def clear_subject_id_terms(self):
        """Clears the subject ``Id`` terms for this query."""
        pass

    subject_id_terms = property(fdel=clear_subject_id_terms)

    def supports_subject_query(self):
        """Tests if a ``SubjectQuery`` is available.

        :return: ``true`` if a subject query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_subject_query(self):
        """Gets the query for an subject.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``
        :raise: ``Unimplemented`` -- ``supports_subject_query()`` is ``false``

        """
        return # osid.ontology.SubjectQuery

    subject_query = property(fget=get_subject_query)

    def clear_subject_terms(self):
        """Clears the subject terms for this query."""
        pass

    subject_terms = property(fdel=clear_subject_terms)

    def match_mapped_id(self, id_, match):
        """Sets the mapped ``Id`` for this query.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``id`` is ``null``

        """
        pass

    def clear_mapped_id_terms(self):
        """Clears the mapped ``Id`` terms for this query."""
        pass

    mapped_id_terms = property(fdel=clear_mapped_id_terms)

    def match_ontology_id(self, ontology_id, match):
        """Sets the ontology ``Id`` for this query.

        :param ontology_id: a ontology ``Id``
        :type ontology_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``

        """
        pass

    def clear_ontology_id_terms(self):
        """Clears the ontology ``Id`` terms for this query."""
        pass

    ontology_id_terms = property(fdel=clear_ontology_id_terms)

    def supports_ontology_query(self):
        """Tests if a ``OntologyQuery`` is available for querying ontologies.

        :return: ``true`` if a ontology query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ontology_query(self):
        """Gets the query for a ontology.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the ontology query
        :rtype: ``osid.ontology.OntologyQuery``
        :raise: ``Unimplemented`` -- ``supports_ontology_query()`` is ``false``

        """
        return # osid.ontology.OntologyQuery

    ontology_query = property(fget=get_ontology_query)

    def clear_ontology_terms(self):
        """Clears the ontology terms for this query."""
        pass

    ontology_terms = property(fdel=clear_ontology_terms)

    def get_relevancy_query_record(self, relevancyt_record_type):
        """Gets the relevancy query record corresponding to the given ``Relevancy`` record ``Type``.

        Multiple retrievals produce a nested ``OR`` term.

        :param relevancyt_record_type: an relevancy query record type
        :type relevancyt_record_type: ``osid.type.Type``
        :return: the relevancy query record
        :rtype: ``osid.ontology.records.RelevancyQueryRecord``
        :raise: ``NullArgument`` -- ``relevancy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(relevancy_record_type)`` is ``false``

        """
        return # osid.ontology.records.RelevancyQueryRecord


class OntologyQuery(osid_queries.OsidCatalogQuery):
    """This is the query for searching ontologies.

    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.

    """
    def match_subject_id(self, subject_id, match):
        """Sets the subject ``Id`` for this query.

        :param subject_id: a subject ``Id``
        :type subject_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``subject_id`` is ``null``

        """
        pass

    def clear_subject_id_terms(self):
        """Clears the subject ``Id`` terms for this query."""
        pass

    subject_id_terms = property(fdel=clear_subject_id_terms)

    def supports_subject_query(self):
        """Tests if a ``SubjectQuery`` is available.

        :return: ``true`` if a subject query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_subject_query(self):
        """Gets the query for a subject.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the subject query
        :rtype: ``osid.ontology.SubjectQuery``
        :raise: ``Unimplemented`` -- ``supports_subject_query()`` is ``false``

        """
        return # osid.ontology.SubjectQuery

    subject_query = property(fget=get_subject_query)

    def match_any_subject(self, match):
        """Matches ontologies that have any subject.

        :param match: ``true`` to match ontologies with any subject, ``false`` to match ontologies with no subject
        :type match: ``boolean``

        """
        pass

    def clear_subject_terms(self):
        """Clears the subject terms for this query."""
        pass

    subject_terms = property(fdel=clear_subject_terms)

    def match_relevancy_id(self, relevancy_id, match):
        """Sets the relevancy ``Id`` for this query.

        :param relevancy_id: a relevancy ``Id``
        :type relevancy_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``relevancy_id`` is ``null``

        """
        pass

    def clear_relevancy_id_terms(self):
        """Clears the relevancy ``Id`` terms for this query."""
        pass

    relevancy_id_terms = property(fdel=clear_relevancy_id_terms)

    def supports_relevancy_query(self):
        """Tests if a ``RelevancyQuery`` is available.

        :return: ``true`` if a relevancy query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_relevancy_query(self):
        """Gets the query for a relevancy.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the relevancy query
        :rtype: ``osid.ontology.RelevancyQuery``
        :raise: ``Unimplemented`` -- ``supports_relevancy_query()`` is ``false``

        """
        return # osid.ontology.RelevancyQuery

    relevancy_query = property(fget=get_relevancy_query)

    def match_any_relevancy(self, match):
        """Matches ontologies that have any relevancy.

        :param match: ``true`` to match ontologies with any relevancy, ``false`` to match ontologies with no relevancy
        :type match: ``boolean``

        """
        pass

    def clear_relevancy_terms(self):
        """Clears the relevancy terms for this query."""
        pass

    relevancy_terms = property(fdel=clear_relevancy_terms)

    def match_ancestor_ontology_id(self, ontology_id, match):
        """Sets the ontology ``Id`` for this query to match ontologies that have the specified ontology as an ancestor.

        :param ontology_id: an ontology ``Id``
        :type ontology_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``

        """
        pass

    def clear_ancestor_ontology_id_terms(self):
        """Clears the ancestor ontology ``Id`` terms for this query."""
        pass

    ancestor_ontology_id_terms = property(fdel=clear_ancestor_ontology_id_terms)

    def supports_ancestor_ontology_query(self):
        """Tests if an ``OntologyQuery`` is available.

        :return: ``true`` if an ontology query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_ancestor_ontology_query(self):
        """Gets the query for an ontology.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the ontology query
        :rtype: ``osid.ontology.OntologyQuery``
        :raise: ``Unimplemented`` -- ``supports_ancestor_ontology_query()`` is ``false``

        """
        return # osid.ontology.OntologyQuery

    ancestor_ontology_query = property(fget=get_ancestor_ontology_query)

    def match_any_ancestor_ontology(self, match):
        """Matches ontologies with any ancestor.

        :param match: ``true`` to match ontologies with any ancestor, ``false`` to match root ontologies
        :type match: ``boolean``

        """
        pass

    def clear_ancestor_ontology_terms(self):
        """Clears the ancestor ontology terms for this query."""
        pass

    ancestor_ontology_terms = property(fdel=clear_ancestor_ontology_terms)

    def match_descendant_ontology_id(self, ontology_id, match):
        """Sets the ontology ``Id`` for this query to match ontologies that have the specified ontology as a descendant.

        :param ontology_id: an ontology ``Id``
        :type ontology_id: ``osid.id.Id``
        :param match: ``true`` for a positive match, ``false`` for a negative match
        :type match: ``boolean``
        :raise: ``NullArgument`` -- ``ontology_id`` is ``null``

        """
        pass

    def clear_descendant_ontology_id_terms(self):
        """Clears the descendant ontology ``Id`` terms for this query."""
        pass

    descendant_ontology_id_terms = property(fdel=clear_descendant_ontology_id_terms)

    def supports_descendant_ontology_query(self):
        """Tests if an ``OntologyQuery`` is available.

        :return: ``true`` if an ontology query is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_descendant_ontology_query(self):
        """Gets the query for an ontology.

        Multiple retrievals produce a nested ``OR`` term.

        :return: the ontology query
        :rtype: ``osid.ontology.OntologyQuery``
        :raise: ``Unimplemented`` -- ``supports_descendant_ontology_query()`` is ``false``

        """
        return # osid.ontology.OntologyQuery

    descendant_ontology_query = property(fget=get_descendant_ontology_query)

    def match_any_descendant_ontology(self, match):
        """Matches ontologies with any descendant.

        :param match: ``true`` to match ontologies with any descendant, ``false`` to match leaf ontologies
        :type match: ``boolean``

        """
        pass

    def clear_descendant_ontology_terms(self):
        """Clears the descendant ontology terms for this query."""
        pass

    descendant_ontology_terms = property(fdel=clear_descendant_ontology_terms)

    def get_ontology_query_record(self, ontology_record_type):
        """Gets the ontology query record corresponding to the given ``Ontology`` record ``Type``.

        Multiple record retrievals produce a nested ``OR`` term.

        :param ontology_record_type: a ontology record type
        :type ontology_record_type: ``osid.type.Type``
        :return: the ontology query record
        :rtype: ``osid.ontology.records.OntologyQueryRecord``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(ontology_record_type)`` is ``false``

        """
        return # osid.ontology.records.OntologyQueryRecord


