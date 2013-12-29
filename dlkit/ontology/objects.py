from ..osid import objects as osid_objects
from ..osid import markers as osid_markers


class Subject(osid_objects.OsidObject, osid_markers.Federateable):
    """A ``Subject`` represents a span of time and an optional location.

    Subjects may be managed individually, or in repeatable sets using
    ``RecuringSubject``.

    """
    def get_subject_record(self, subject_record_type):
        """Gets the subject record corresponding to the given ``Subject`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``subject_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(subject_record_type)`` is ``true`` .

        :param subject_record_type: the type of the record to retrieve
        :type subject_record_type: ``osid.type.Type``
        :return: the subject record
        :rtype: ``osid.ontology.records.SubjectRecord``
        :raise: ``NullArgument`` -- ``subject_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(subject_record_type)`` is ``false``

        """
        return # osid.ontology.records.SubjectRecord


class SubjectForm(osid_objects.OsidObjectForm, osid_objects.OsidFederateableForm):
    """This is the form for creating and updating ``Subjects``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``SubjectAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_subject_form_record(self, subject_record_type):
        """Gets the ``SubjectFormRecord`` corresponding to the given subject record ``Type``.

        :param subject_record_type: the subject record type
        :type subject_record_type: ``osid.type.Type``
        :return: the subject form record
        :rtype: ``osid.ontology.records.SubjectFormRecord``
        :raise: ``NullArgument`` -- ``subject_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(subject_record_type)`` is ``false``

        """
        return # osid.ontology.records.SubjectFormRecord


class SubjectList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``SubjectList`` provides a means for accessing ``Subject`` elements sequentially either one at a time or many at a time.

    Examples: while (sl.hasNext()) { Subject subject =
    sl.getNextSubject(); }

    or
      while (sl.hasNext()) {
           Subject[] subjects = sl.getNextSubjects(sl.available());
      }
    


    """
    def get_next_subject(self):
        """Gets the next ``Subject`` in this list.

        :return: the next ``Subject`` in this list. The ``has_next()`` method should be used to test that a next ``Subject`` is available before calling this method.
        :rtype: ``osid.ontology.Subject``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.Subject

    next_subject = property(fget=get_next_subject)

    def get_next_subjects(self, n):
        """Gets the next set of ``Subject`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Subject`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Subject`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.ontology.Subject``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.Subject


class SubjectNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``SubjectHierarchySession``.

    """
    def get_subject(self):
        """Gets the ``Subject`` at this node.

        :return: the subject represented by this node
        :rtype: ``osid.ontology.Subject``

        """
        return # osid.ontology.Subject

    subject = property(fget=get_subject)

    def get_parent_subject_nodes(self):
        """Gets the parents of this subject.

        :return: the parents of the ``id``
        :rtype: ``osid.ontology.SubjectNodeList``

        """
        return # osid.ontology.SubjectNodeList

    parent_subject_nodes = property(fget=get_parent_subject_nodes)

    def get_child_subject_nodes(self):
        """Gets the children of this subject.

        :return: the children of this subject
        :rtype: ``osid.ontology.SubjectNodeList``

        """
        return # osid.ontology.SubjectNodeList

    child_subject_nodes = property(fget=get_child_subject_nodes)


class SubjectNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``SubjectNodeList`` provides a means for accessing ``SubjectNode`` elements sequentially either one at a time or many at a time.

    Examples: while (snl.hasNext()) { SubjectNode node =
    snl.getNextSubjectNode(); }

    or
      while (snl.hasNext()) {
           SubjectNode[] nodes = snl.getNextSubjectNodes(snl.available());
      }
    


    """
    def get_next_subject_node(self):
        """Gets the next ``SubjectNode`` in this list.

        :return: the next ``SubjectNode`` in this list. The ``has_next()`` method should be used to test that a next ``SubjectNode`` is available before calling this method.
        :rtype: ``osid.ontology.SubjectNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.SubjectNode

    next_subject_node = property(fget=get_next_subject_node)

    def get_next_subject_nodes(self, n):
        """Gets the next set of ``SubjectNode`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``SubjectNode`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``SubjectNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.ontology.SubjectNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.SubjectNode


class Relevancy(osid_objects.OsidRelationship):
    """A ``Relevancy`` maps an ``Id`` to an ``Subject``."""
    def get_subject_id(self):
        """Gets the subject ``Id``.

        :return: the subject ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    subject_id = property(fget=get_subject_id)

    def get_subject(self):
        """Gets the ``Subject``.

        :return: the subject
        :rtype: ``osid.ontology.Subject``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.Subject

    subject = property(fget=get_subject)

    def get_mapped_id(self):
        """Gets the ``Id`` mapped to this ``Subject``.

        :return: a mapped ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    mapped_id = property(fget=get_mapped_id)

    def get_relevancy_record(self, relevancy_record_type):
        """Gets the relevancy record corresponding to the given ``Relevancy`` record ``Type``.

        This method must is to retrieve an object implementing the
        requested record. The ``relevancy_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(relevancy_record_type)`` is ``true`` .

        :param relevancy_record_type: the type of the record to retrieve
        :type relevancy_record_type: ``osid.type.Type``
        :return: the relevancy record
        :rtype: ``osid.ontology.records.RelevancyRecord``
        :raise: ``NullArgument`` -- ``relevancy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(relevancy_record_type)`` is ``false``

        """
        return # osid.ontology.records.RelevancyRecord


class RelevancyForm(osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Relevancy`` objects."""
    def get_relevancy_form_record(self, relevancy_record_type):
        """Gets the ``RelevancyFormRecord`` corresponding to the given relevancy record ``Type``.

        :param relevancy_record_type: the relevancy record type
        :type relevancy_record_type: ``osid.type.Type``
        :return: the relevancy form record
        :rtype: ``osid.ontology.records.RelevancyFormRecord``
        :raise: ``NullArgument`` -- ``relevancy_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(relevancy_record_type)`` is ``false``

        """
        return # osid.ontology.records.RelevancyFormRecord


class RelevancyList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``RelevancyList`` provides a means for accessing ``Relevancy`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Relevancy relevancy =
    rl.getNextRelevancy(); }

    or
      while (rl.hasNext()) {
           Relevancy[] relevancies = rl.getNextRelevancies(rl.available());
      }
    


    """
    def get_next_relevancy(self):
        """Gets the next ``Relevancy`` in this list.

        :return: the next ``Relevancy`` in this list. The ``has_next()`` method should be used to test that a next ``Relevancy`` is available before calling this method.
        :rtype: ``osid.ontology.Relevancy``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.Relevancy

    next_relevancy = property(fget=get_next_relevancy)

    def get_next_relevancies(self, n):
        """Gets the next set of ``Relevancy`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Relevancy`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Relevancy`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.ontology.Relevancy``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.Relevancy


class Ontology(osid_objects.OsidCatalog):
    """An ontology defines a collection of subjects."""
    def get_ontology_record(self, ontology_record_type):
        """Gets the ontology record corresponding to the given ``Ontology`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``ontology_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(ontology_record_type)`` is ``true`` .

        :param ontology_record_type: an ontology record type
        :type ontology_record_type: ``osid.type.Type``
        :return: the ontology record
        :rtype: ``osid.ontology.records.OntologyRecord``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(ontology_record_type)`` is ``false``

        """
        return # osid.ontology.records.OntologyRecord


class OntologyForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ontologies.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``OntologyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_ontology_form_record(self, ontology_record_type):
        """Gets the ``OntologyFormRecord`` corresponding to the given ontology record ``Type``.

        :param ontology_record_type: an ontology record type
        :type ontology_record_type: ``osid.type.Type``
        :return: the ontology form record
        :rtype: ``osid.ontology.records.OntologyFormRecord``
        :raise: ``NullArgument`` -- ``ontology_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(ontology_record_type)`` is ``false``

        """
        return # osid.ontology.records.OntologyFormRecord


class OntologyList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``OntologyList`` provides a means for accessing ``Ontology`` elements sequentially either one at a time or many at a time.

    Examples: while (ol.hasNext()) { Ontology ontology =
    ol.getNextOntology(); }

    or
      while (ol.hasNext()) {
           Ontology[] ontologies = ol.getNextOntologies(ol.available());
      }
    


    """
    def get_next_ontology(self):
        """Gets the next ``Ontology`` in this list.

        :return: the next ``Ontology`` in this list. The ``has_next()`` method should be used to test that a next ``Ontology`` is available before calling this method.
        :rtype: ``osid.ontology.Ontology``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.Ontology

    next_ontology = property(fget=get_next_ontology)

    def get_next_ontologies(self, n):
        """Gets the next set of ``Ontology`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Ontology`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Ontology`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.ontology.Ontology``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.Ontology


class OntologyNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``OntologyHierarchySession``.

    """
    def get_ontology(self):
        """Gets the ``Ontology`` at this node.

        :return: the ontology represented by this node
        :rtype: ``osid.ontology.Ontology``

        """
        return # osid.ontology.Ontology

    ontology = property(fget=get_ontology)

    def get_parent_ontology_nodes(self):
        """Gets the parents of this ontology.

        :return: the parents of the ``id``
        :rtype: ``osid.ontology.OntologyNodeList``

        """
        return # osid.ontology.OntologyNodeList

    parent_ontology_nodes = property(fget=get_parent_ontology_nodes)

    def get_child_ontology_nodes(self):
        """Gets the children of this ontology.

        :return: the children of this ontology
        :rtype: ``osid.ontology.OntologyNodeList``

        """
        return # osid.ontology.OntologyNodeList

    child_ontology_nodes = property(fget=get_child_ontology_nodes)


class OntologyNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``OntologyNodeList`` provides a means for accessing ``OntologyNode`` elements sequentially either one at a time or many at a time.

    Examples: while (onl.hasNext()) { OntologyNode node =
    onl.getNextOntologyNode(); }

    or
      while (onl.hasNext()) {
           OntologyNode[] nodes = onl.getNextOntologyNodes(onl.available());
      }
    


    """
    def get_next_ontology_node(self):
        """Gets the next ``OntologyNode`` in this list.

        :return: the next ``OntologyNode`` in this list. The ``has_next()`` method should be used to test that a next ``OntologyNode`` is available before calling this method.
        :rtype: ``osid.ontology.OntologyNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.OntologyNode

    next_ontology_node = property(fget=get_next_ontology_node)

    def get_next_ontology_nodes(self, n):
        """Gets the next set of ``OntologyNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``OntologyNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``OntologyNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.ontology.OntologyNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.ontology.OntologyNode


