from ..osid import search_orders as osid_search_orders


class SubjectSearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidFederateableSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_subject_search_order_record(self, subject_record_type):
        """Gets the subject search order record corresponding to the given subject record ``Type``.

        Multiple retrievals return the same underlying object.

        :param subject_record_type: a subject record type
        :type subject_record_type: ``osid.type.Type``
        :return: the subject search order record
        :rtype: ``osid.ontology.records.SubjectSearchOrderRecord``
        :raise: ``NullArgument`` -- ``subject_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(subject_record_type)`` is ``false``

        """
        return # osid.ontology.records.SubjectSearchOrderRecord


class RelevancySearchOrder(osid_search_orders.OsidRelationshipSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_subject(self, style):
        """Specified a preference for ordering results by the subject.

        :param style: search order style
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_subject_search_order(self):
        """Tests if a ``SubjectSearchOrder`` is available.

        :return: ``true`` if a subject search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_subject_search_order(self):
        """Gets the search order for a subject.

        :return: the subject search order
        :rtype: ``osid.ontology.SubjectSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_subject_search_order()`` is ``false``

        """
        return # osid.ontology.SubjectSearchOrder

    subject_search_order = property(fget=get_subject_search_order)

    def get_relevancy_search_order_record(self, relevancy_record_type):
        """Gets the relevancy search order record corresponding to the given commitment record ``Type``.

        Multiple retrievals return the same underlying object.

        :param relevancy_record_type: a relevancy record type
        :type relevancy_record_type: ``osid.type.Type``
        :return: the relevancy search order record
        :rtype: ``osid.ontology.records.RelevancySearchOrderRecord``
        :raise: ``NullArgument`` -- ``relevancy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(relevancy_record_type)`` is ``false``

        """
        return # osid.ontology.records.RelevancySearchOrderRecord


class OntologySearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_ontology_search_order_record(self, ontology_record_type):
        """Gets the ontology search order record corresponding to the given ontology record ``Type``.

        Multiple retrievals return the same underlying object.

        :param ontology_record_type: an ontology record type
        :type ontology_record_type: ``osid.type.Type``
        :return: the ontology search order record
        :rtype: ``osid.ontology.records.OntologySearchOrderRecord``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(ontology_record_type)`` is ``false``

        """
        return # osid.ontology.records.OntologySearchOrderRecord


