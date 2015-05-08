from ..osid import objects as osid_objects


class Relationship(osid_objects.OsidRelationship):
    """A ``Relationship`` is an object between two peers.

    The genus type indicates the relationship between the peer and the
    related peer.

    """
    def get_source_id(self):
        """Gets the from peer ``Id`` in this relationship.

        :return: the peer
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    source_id = property(fget=get_source_id)

    def get_destination_id(self):
        """Gets the to peer ``Id`` in this relationship.

        :return: the related peer
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    destination_id = property(fget=get_destination_id)

    def get_relationship_record(self, relationship_record_type):
        """Gets the relationshop record corresponding to the given ``Relationship`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``relationship_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(relationship_record_type)`` is ``true`` .

        :param relationship_record_type: the type of relationship record to retrieve
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationship record
        :rtype: ``osid.relationship.records.RelationshipRecord``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_record_type)`` is ``false``

        """
        return # osid.relationship.records.RelationshipRecord


class RelationshipForm(osid_objects.OsidRelationshipForm):
    """This is the form for creating and updating ``Relationships``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RelationshipAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_relationship_form_record(self, relationship_record_type):
        """Gets the ``RelationshipFormRecord`` corresponding to the given relationship record ``Type``.

        :param relationship_record_type: a relationship record type
        :type relationship_record_type: ``osid.type.Type``
        :return: the relationship form record
        :rtype: ``osid.relationship.records.RelationshipFormRecord``
        :raise: ``NullArgument`` -- ``relationship_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_record_type)`` is ``false``

        """
        return # osid.relationship.records.RelationshipFormRecord


class RelationshipList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``Relationship`` provides a means for accessing ``Relationship`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Relationship relationship =
    rl.getNextRelationship(); }

    or
      while (rl.hasNext()) {
           Relationship[] relationships = rl.getNextRelationships(rl.available());
      }



    """
    def get_next_relationship(self):
        """Gets the next ``Relationship`` in this list.

        :return: the next ``Relationship`` in this list. The ``has_next()`` method should be used to test that a next ``Relationship`` is available before calling this method.
        :rtype: ``osid.relationship.Relationship``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.relationship.Relationship

    next_relationship = property(fget=get_next_relationship)

    def get_next_relationships(self, n):
        """Gets the next set of ``Relationships`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Relationship`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Relationship`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.relationship.Relationship``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.relationship.Relationship


class Family(osid_objects.OsidCatalog):
    """A ``Family`` represents a collection of relationships.

    Like all OSID objects, a ``Family`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    def get_family_record(self, family_record_type):
        """Gets the famly record corresponding to the given ``Family`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``family_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(family_record_type)``
        is ``true`` .

        :param family_record_type: the type of family record to retrieve
        :type family_record_type: ``osid.type.Type``
        :return: the family record
        :rtype: ``osid.relationship.records.FamilyRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        """
        return # osid.relationship.records.FamilyRecord


class FamilyForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Family`` objects.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``FamilyAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_family_form_record(self, family_record_type):
        """Gets the ``FamilyFormRecord`` corresponding to the given family record ``Type``.

        :param family_record_type: the family record type
        :type family_record_type: ``osid.type.Type``
        :return: the family form record
        :rtype: ``osid.relationship.records.FamilyFormRecord``
        :raise: ``NullArgument`` -- ``family_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_record_type)`` is ``false``

        """
        return # osid.relationship.records.FamilyFormRecord


class FamilyList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``FamilyList`` provides a means for accessing ``Family`` elements sequentially either one at a time or many at a time.

    Examples: while (fl.hasNext()) { Family family = fl.getNextFamily();
    }

    or
      while (fl.hasNext()) {
           Family[] families = fl.getNextFamilies(fl.available());
      }



    """
    def get_next_family(self):
        """Gets the next ``Family`` in this list.

        :return: the next ``Family`` in this list. The ``has_next()`` method should be used to test that a next ``Family`` is available before calling this method.
        :rtype: ``osid.relationship.Family``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.relationship.Family

    next_family = property(fget=get_next_family)

    def get_next_families(self, n):
        """Gets the next set of ``Family elements`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Family`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Family`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.relationship.Family``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.relationship.Family


