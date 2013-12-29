from ..osid import query_inspectors as osid_query_inspectors


class SubjectQueryInspector(osid_query_inspectors.OsidObjectQueryInspector, osid_query_inspectors.OsidFederateableQueryInspector):
    """This is the query inspector for examining subject queries."""
    def get_ancestor_subject_id_terms(self):
        """Gets the ancestor subject ``Id`` terms.

        :return: the ancestor subject ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_subject_id_terms = property(fget=get_ancestor_subject_id_terms)

    def get_ancestor_subject_terms(self):
        """Gets the ancestor subject terms.

        :return: the ancestor subject terms
        :rtype: ``osid.ontology.SubjectQueryInspector``

        """
        return # osid.ontology.SubjectQueryInspector

    ancestor_subject_terms = property(fget=get_ancestor_subject_terms)

    def get_descendant_subject_id_terms(self):
        """Gets the descendant subject ``Id`` terms.

        :return: the descendant subject ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_subject_id_terms = property(fget=get_descendant_subject_id_terms)

    def get_descendant_subject_terms(self):
        """Gets the descendant subject terms.

        :return: the descendant subject terms
        :rtype: ``osid.ontology.SubjectQueryInspector``

        """
        return # osid.ontology.SubjectQueryInspector

    descendant_subject_terms = property(fget=get_descendant_subject_terms)

    def get_relevancy_id_terms(self):
        """Gets the relevancy ``Id`` terms.

        :return: the relevancy ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    relevancy_id_terms = property(fget=get_relevancy_id_terms)

    def get_relevancy_terms(self):
        """Gets the relevancy terms.

        :return: the relevancy terms
        :rtype: ``osid.ontology.RelevancyQueryInspector``

        """
        return # osid.ontology.RelevancyQueryInspector

    relevancy_terms = property(fget=get_relevancy_terms)

    def get_ontology_id_terms(self):
        """Gets the ontology ``Id`` terms.

        :return: the ontology ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ontology_id_terms = property(fget=get_ontology_id_terms)

    def get_ontology_terms(self):
        """Gets the ontology terms.

        :return: the ontology terms
        :rtype: ``osid.ontology.OntologyQueryInspector``

        """
        return # osid.ontology.OntologyQueryInspector

    ontology_terms = property(fget=get_ontology_terms)

    def get_subject_query_inspector_record(self, subject_record_type):
        """Gets the subject query inspector record corresponding to the given ``Subject`` record ``Type``.

        :param subject_record_type: a subject record type
        :type subject_record_type: ``osid.type.Type``
        :return: the subject query inspector record
        :rtype: ``osid.ontology.records.SubjectQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``subject_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(subject_record_type)`` is ``false``

        """
        return # osid.ontology.records.SubjectQueryInspectorRecord


class RelevancyQueryInspector(osid_query_inspectors.OsidRelationshipQueryInspector):
    """This is the query inspector for examining relevancy queries."""
    def get_subject_id_terms(self):
        """Gets the subject ``Id`` terms.

        :return: the subject ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    subject_id_terms = property(fget=get_subject_id_terms)

    def get_subject_terms(self):
        """Gets the subject terms.

        :return: the subject terms
        :rtype: ``osid.ontology.SubjectQueryInspector``

        """
        return # osid.ontology.SubjectQueryInspector

    subject_terms = property(fget=get_subject_terms)

    def get_mapped_id_terms(self):
        """Gets the mapped ``Id`` terms.

        :return: the mapped ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    mapped_id_terms = property(fget=get_mapped_id_terms)

    def get_ontology_id_terms(self):
        """Gets the ontology ``Id`` terms.

        :return: the ontology ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ontology_id_terms = property(fget=get_ontology_id_terms)

    def get_ontology_terms(self):
        """Gets the ontology terms.

        :return: the ontology terms
        :rtype: ``osid.ontology.OntologyQueryInspector``

        """
        return # osid.ontology.OntologyQueryInspector

    ontology_terms = property(fget=get_ontology_terms)

    def get_relevancy_query_inspector_record(self, relevancy_record_type):
        """Gets the relevancy query inspector record corresponding to the given ``Relevancy`` record ``Type``.

        :param relevancy_record_type: a relevancy record type
        :type relevancy_record_type: ``osid.type.Type``
        :return: the relevancy query inspector record
        :rtype: ``osid.ontology.records.RelevancyQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``relevancy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(relevancy_record_type)`` is ``false``

        """
        return # osid.ontology.records.RelevancyQueryInspectorRecord


class OntologyQueryInspector(osid_query_inspectors.OsidCatalogQueryInspector):
    """This is the query inspector for examining ontology queries."""
    def get_subject_id_terms(self):
        """Gets the subject ``Id`` terms.

        :return: the subject ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    subject_id_terms = property(fget=get_subject_id_terms)

    def get_subject_terms(self):
        """Gets the subject terms.

        :return: the subject terms
        :rtype: ``osid.ontology.SubjectQueryInspector``

        """
        return # osid.ontology.SubjectQueryInspector

    subject_terms = property(fget=get_subject_terms)

    def get_relevancy_id_terms(self):
        """Gets the relevancy ``Id`` terms.

        :return: the relevancy ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    relevancy_id_terms = property(fget=get_relevancy_id_terms)

    def get_relevancy_terms(self):
        """Gets the relevancy terms.

        :return: the relevancy terms
        :rtype: ``osid.ontology.RelevancyQueryInspector``

        """
        return # osid.ontology.RelevancyQueryInspector

    relevancy_terms = property(fget=get_relevancy_terms)

    def get_ancestor_ontology_id_terms(self):
        """Gets the ancestor ontology ``Id`` terms.

        :return: the ancestor ontology ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    ancestor_ontology_id_terms = property(fget=get_ancestor_ontology_id_terms)

    def get_ancestor_ontology_terms(self):
        """Gets the ancestor ontology terms.

        :return: the ancestor ontology terms
        :rtype: ``osid.ontology.OntologyQueryInspector``

        """
        return # osid.ontology.OntologyQueryInspector

    ancestor_ontology_terms = property(fget=get_ancestor_ontology_terms)

    def get_descendant_ontology_id_terms(self):
        """Gets the descendant ontology ``Id`` terms.

        :return: the descendant ontology ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``

        """
        return # osid.search.terms.IdTerm

    descendant_ontology_id_terms = property(fget=get_descendant_ontology_id_terms)

    def get_descendant_ontology_terms(self):
        """Gets the descendant ontology terms.

        :return: the descendant ontology terms
        :rtype: ``osid.ontology.OntologyQueryInspector``

        """
        return # osid.ontology.OntologyQueryInspector

    descendant_ontology_terms = property(fget=get_descendant_ontology_terms)

    def get_ontology_query_inspector_record(self, ontology_record_type):
        """Gets the ontology query inspector record corresponding to the given ``Ontology`` record ``Type``.

        :param ontology_record_type: an ontology record type
        :type ontology_record_type: ``osid.type.Type``
        :return: the ontology query inspector record
        :rtype: ``osid.ontology.records.OntologyQueryInspectorRecord``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(ontology_record_type)`` is ``false``

        """
        return # osid.ontology.records.OntologyQueryInspectorRecord


