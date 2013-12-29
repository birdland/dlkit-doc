from ..osid import receivers as osid_receivers


class SubjectReceiver(osid_receivers.OsidReceiver):
    """The subject receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Subjects``."""
    def new_subject(self, subject_id):
        """The callback for notifications of new subjects.

        :param subject_id: the ``Id`` of the new ``Subject``
        :type subject_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_subject(self, subject_id, ancestor_id):
        """The callback for notifications of new subject ancestors.

        :param subject_id: the Id of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the new ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_subject(self, subject_id, descendant_id):
        """The callback for notifications of new subject descendants.

        :param subject_id: the Id of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :param descendant_id: the Id of the new ``Subject`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_subject(self, subject_id):
        """The callback for notification of updated subjects.

        :param subject_id: the ``Id`` of the updated ``Subject``
        :type subject_id: ``osid.id.Id``

        """
        pass

    def deleted_subject(self, subject_id):
        """The callback for notification of deleted subjects.

        :param subject_id: the ``Id`` of the deleted ``Subject``
        :type subject_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_subject(self, subject_id, ancestor_id):
        """The callback for notifications of deleted subject ancestors.

        :param subject_id: the Id of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :param ancestor_id: the Id of the removed ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_subject(self, subject_id, descendant_id):
        """The callback for notifications of deleted subject descendants.

        :param subject_id: the Id of the ``Subject``
        :type subject_id: ``osid.id.Id``
        :param descendant_id: the Id of the removed descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


class RelevancyReceiver(osid_receivers.OsidReceiver):
    """This receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted relevancies."""
    def new_relevancy(self, relevancy_id):
        """The callback for notifications of new relevancies.

        :param relevancy_id: the ``Id`` of the new ``Relevancy``
        :type relevancy_id: ``osid.id.Id``

        """
        pass

    def new_relevancy_for_subject(self, relevancy_id, subject_id):
        """The callback for notifications of new relevancies.

        :param relevancy_id: the ``Id`` of the new ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param subject_id: the ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``

        """
        pass

    def new_relevancy_for_id(self, relevancy_id, id_):
        """The callback for notifications of new relevancies.

        :param relevancy_id: the ``Id`` of the new ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param id: the mapped ``Id``
        :type id: ``osid.id.Id``

        """
        pass

    def changed_relevancy(self, relevancy_id):
        """The callback for notification of updated relevancies.

        :param relevancy_id: the ``Id`` of the updated ``Relevancy``
        :type relevancy_id: ``osid.id.Id``

        """
        pass

    def changed_relevancy_for_subject(self, relevancy_id, subject_id):
        """The callback for notifications of updated relevancies.

        :param relevancy_id: the ``Id`` of the updated ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param subject_id: the ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``

        """
        pass

    def changed_relevancy_for_id(self, relevancy_id, id_):
        """The callback for notifications of updated relevancies.

        :param relevancy_id: the ``Id`` of the updated ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param id: the mapped ``Id``
        :type id: ``osid.id.Id``

        """
        pass

    def deleted_relevancy(self, relevancy_id):
        """The callback for notification of deleted relevancies.

        :param relevancy_id: the ``Id`` of the deleted ``Relevancy``
        :type relevancy_id: ``osid.id.Id``

        """
        pass

    def deleted_relevancy_for_subject(self, relevancy_id, subject_id):
        """The callback for notifications of deleted relevancies.

        :param relevancy_id: the ``Id`` of the deleted ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param subject_id: the ``Id`` of the ``Subject``
        :type subject_id: ``osid.id.Id``

        """
        pass

    def deleted_relevancy_for_id(self, relevancy_id, id_):
        """The callback for notifications of deleted relevancies.

        :param relevancy_id: the ``Id`` of the deleted ``Relevancy``
        :type relevancy_id: ``osid.id.Id``
        :param id: the mapped ``Id``
        :type id: ``osid.id.Id``

        """
        pass


class OntologyReceiver(osid_receivers.OsidReceiver):
    """The vault receiver is the consumer supplied interface for receiving notifications pertaining to new, updated or deleted ``Ontology`` objects."""
    def new_ontology(self, ontology_id):
        """The callback for notifications of new ontologies.

        :param ontology_id: the ``Id`` of the new ``Ontology``
        :type ontology_id: ``osid.id.Id``

        """
        pass

    def new_ancestor_ontology(self, ontology_id, ancestor_id):
        """The callback for notifications of new ontology ancestors.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :param ancestor_id: ``has_record_type(ontology_record_type) is false``
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def new_descendant_ontology(self, ontology_id, descendant_id):
        """The callback for notifications of new ontology descendants.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the new ``Ontology`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass

    def changed_ontology(self, ontology_id):
        """The callback for notification of updated ontologies.

        :param ontology_id: the ``Id`` of the updated ``Ontology``
        :type ontology_id: ``osid.id.Id``

        """
        pass

    def deleted_ontology(self, ontology_id):
        """The callback for notification of deleted ontologies.

        :param ontology_id: the ``Id`` of the deleted ``Ontology``
        :type ontology_id: ``osid.id.Id``

        """
        pass

    def deleted_ancestor_ontology(self, ontology_id, ancestor_id):
        """The callback for notifications of deleted ontology ancestors.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :param ancestor_id: the ``Id`` of the removed ``Ontology`` ancestor
        :type ancestor_id: ``osid.id.Id``

        """
        pass

    def deleted_descendant_ontology(self, ontology_id, descendant_id):
        """The callback for notifications of deleted ontology descendants.

        :param ontology_id: the ``Id`` of the ``Ontology``
        :type ontology_id: ``osid.id.Id``
        :param descendant_id: the ``Id`` of the removed ``Ontology`` descendant
        :type descendant_id: ``osid.id.Id``

        """
        pass


