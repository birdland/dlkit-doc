from ..osid import searches as osid_searches


class SubjectSearch(osid_searches.OsidSearch):
    """``SubjectSearch`` defines the interface for specifying subject search options."""
    def search_among_subjects(self, subject_ids):
        """Execute this search among the given list of subjects.

        :param subject_ids: list of subjects
        :type subject_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``subject_ids`` is ``null``

        """
        pass

    def order_subject_results(self, subject_search_order):
        """Specify an ordering to the search results.

        :param subject_search_order: subject search order
        :type subject_search_order: ``osid.ontology.SubjectSearchOrder``
        :raise: ``NullArgument`` -- ``subject_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``subject_search_order`` is not of this service

        """
        pass

    def get_subject_search_record(self, subject_search_record_type):
        """Gets the subject search record corresponding to the given subject search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param subject_search_record_type: a subject search record type
        :type subject_search_record_type: ``osid.type.Type``
        :return: the subject search record
        :rtype: ``osid.ontology.records.SubjectSearchRecord``
        :raise: ``NullArgument`` -- ``subject_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(subject_search_record_type)`` is ``false``

        """
        return # osid.ontology.records.SubjectSearchRecord


class SubjectSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_subjects(self):
        """Gets the subject list resulting from the search.

        :return: the subject list
        :rtype: ``osid.ontology.SubjectList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.ontology.SubjectList

    subjects = property(fget=get_subjects)

    def get_subject_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the subject query inspector
        :rtype: ``osid.ontology.SubjectQueryInspector``

        """
        return # osid.ontology.SubjectQueryInspector

    subject_query_inspector = property(fget=get_subject_query_inspector)

    def get_subject_search_results_record(self, subject_search_record_type):
        """Gets the subject search results record corresponding to the given subject search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param subject_search_record_type: a subject search record type
        :type subject_search_record_type: ``osid.type.Type``
        :return: the subject search results record
        :rtype: ``osid.ontology.records.SubjectSearchResultsRecord``
        :raise: ``NullArgument`` -- ``subject_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(subject_search_record_type)`` is ``false``

        """
        return # osid.ontology.records.SubjectSearchResultsRecord


class RelevancySearch(osid_searches.OsidSearch):
    """``RelevancySearch`` defines the interface for specifying relevancy search options."""
    def search_among_relevancies(self, relevancy_ids):
        """Execute this search among the given list of relevancies.

        :param relevancy_ids: list of relevancies
        :type relevancy_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``relevancy_ids`` is ``null``

        """
        pass

    def order_relevancy_results(self, relevancy_search_order):
        """Specify an ordering to the search results.

        :param relevancy_search_order: relevancy search order
        :type relevancy_search_order: ``osid.ontology.RelevancySearchOrder``
        :raise: ``NullArgument`` -- ``relevancy_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``relevancy_search_order`` is not of this service

        """
        pass

    def get_relevancy_search_record(self, relevancy_search_record_type):
        """Gets the relevancy search record corresponding to the given relevancy search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param relevancy_search_record_type: a relevancy search record type
        :type relevancy_search_record_type: ``osid.type.Type``
        :return: the relevancy search record
        :rtype: ``osid.ontology.records.RelevancySearchRecord``
        :raise: ``NullArgument`` -- ``relevancy_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relevancy_search_record_type)`` is ``false``

        """
        return # osid.ontology.records.RelevancySearchRecord


class RelevancySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_relevancies(self):
        """Gets the relevancy list resulting from the search.

        :return: the relevancy list
        :rtype: ``osid.ontology.RelevancyList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.ontology.RelevancyList

    relevancies = property(fget=get_relevancies)

    def get_relevancy_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the relevancy query inspector
        :rtype: ``osid.ontology.RelevancyQueryInspector``

        """
        return # osid.ontology.RelevancyQueryInspector

    relevancy_query_inspector = property(fget=get_relevancy_query_inspector)

    def get_relevancy_search_results_record(self, relevancy_search_record_type):
        """Gets the relevancy search results record corresponding to the given relevancy search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param relevancy_search_record_type: a relevancy search record type
        :type relevancy_search_record_type: ``osid.type.Type``
        :return: the relevancy search results record
        :rtype: ``osid.ontology.records.RelevancySearchResultsRecord``
        :raise: ``NullArgument`` -- ``relevancy_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(relevancy_search_record_type)`` is ``false``

        """
        return # osid.ontology.records.RelevancySearchResultsRecord


class OntologySearch(osid_searches.OsidSearch):
    """The interface for governing ontology searches."""
    def search_among_ontologies(self, ontology_ids):
        """Execute this search among the given list of ontologies.

        :param ontology_ids: list of ontologies
        :type ontology_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``ontology_ids`` is ``null``

        """
        pass

    def order_ontology_results(self, ontology_search_order):
        """Specify an ordering to the search results.

        :param ontology_search_order: ontology search order
        :type ontology_search_order: ``osid.ontology.OntologySearchOrder``
        :raise: ``NullArgument`` -- ``ontology_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``ontology_search_order`` is not of this service

        """
        pass

    def get_ontology_search_record(self, ontology_search_record_type):
        """Gets the ontology search record corresponding to the given ontology search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param ontology_search_record_type: an ontology search record type
        :type ontology_search_record_type: ``osid.type.Type``
        :return: the ontology search record
        :rtype: ``osid.ontology.records.OntologySearchRecord``
        :raise: ``NullArgument`` -- ``ontology_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(ontology_search_record_type)`` is ``false``

        """
        return # osid.ontology.records.OntologySearchRecord


class OntologySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""
    def get_ontologies(self):
        """Gets the ontology list resulting from the search.

        :return: the ontology list
        :rtype: ``osid.ontology.OntologyList``
        :raise: ``IllegalState`` -- list already retrieved

        """
        return # osid.ontology.OntologyList

    ontologies = property(fget=get_ontologies)

    def get_ontology_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.

        :return: the ontology query inspector
        :rtype: ``osid.ontology.OntologyQueryInspector``

        """
        return # osid.ontology.OntologyQueryInspector

    ontology_query_inspector = property(fget=get_ontology_query_inspector)

    def get_ontology_search_results_record(self, ontology_search_record_type):
        """Gets the ontology search results record corresponding to the given calndar search record ``Type``.

        This method is used to retrieve an object implementing the
        requested record.

        :param ontology_search_record_type: an ontology search record type
        :type ontology_search_record_type: ``osid.type.Type``
        :return: the ontology search results record
        :rtype: ``osid.ontology.records.OntologySearchResultsRecord``
        :raise: ``NullArgument`` -- ``ontology_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(ontology_search_record_type)`` is ``false``

        """
        return # osid.ontology.records.OntologySearchResultsRecord


