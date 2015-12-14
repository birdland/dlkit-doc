
from ..osid import searches as osid_searches


class RelationshipSearch(osid_searches.OsidSearch):
    """The search interface for governing relationship searches."""

    def search_among_relationships(self, relationship_ids):
        """Execute this search among the given list of relationships.


        :param relationship_ids: list of relationships
        :type relationship_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``relationship_ids`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def order_relationship_results(self, relationship_search_order):
        """Specify an ordering to the search results.


        :param relationship_search_order: relationship search order
        :type relationship_search_order: ``osid.relationship.RelationshipSearchOrder``
        :raise: ``NullArgument`` -- ``relationship_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``relationship_search_order`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def get_relationship_search_record(self, relationship_search_record_type):
        """Gets the relationship search record corresponding to the given relationship search record ``Type``.


        This method is used to retrieve an object implementing the
        requested record.


        :param relationship_search_record_type: a relationship search record type
        :type relationship_search_record_type: ``osid.type.Type``
        :return: the relationship search record
        :rtype: ``osid.relationship.records.RelationshipSearchRecord``
        :raise: ``NullArgument`` -- ``relationship_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_search_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.relationship.records.RelationshipSearchRecord


class RelationshipSearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search."""

    def get_relationships(self):
        """Gets the relationship list resulting from a search.


        :return: the relationship list
        :rtype: ``osid.relationship.RelationshipList``
        :raise: ``IllegalState`` -- list already retrieved


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.relationship.RelationshipList

    relationships = property(fget=get_relationships)

    def get_relationship_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.


        :return: the relationship query inspector
        :rtype: ``osid.relationship.RelationshipQueryInspector``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.relationship.RelationshipQueryInspector

    relationship_query_inspector = property(fget=get_relationship_query_inspector)

    def get_relationship_search_results_record(self, relationship_search_record_type):
        """Gets the relationship search results record corresponding to the given relationship search record ``Type``.


        This method must be used to retrieve an object implementing the
        requested record interface along with all of its ancestor
        interfaces.


        :param relationship_search_record_type: a relationship search record type
        :type relationship_search_record_type: ``osid.type.Type``
        :return: the relationship search results record
        :rtype: ``osid.relationship.records.RelationshipSearchResultsRecord``
        :raise: ``NullArgument`` -- ``relationship_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(relationship_search_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.relationship.records.RelationshipSearchResultsRecord


class FamilySearch(osid_searches.OsidSearch):
    """The search interface for governing family searches."""

    def search_among_families(self, family_ids):
        """Execute this search among the given list of families.


        :param family_ids: list of families
        :type family_ids: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``family_ids`` is ``null``


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def order_family_results(self, family_search_order):
        """Specify an ordering to the search results.


        :param family_search_order: family search order
        :type family_search_order: ``osid.relationship.FamilySearchOrder``
        :raise: ``NullArgument`` -- ``family_search_order`` is ``null``
        :raise: ``Unsupported`` -- ``family_search_order`` is not of this service


        *compliance: mandatory -- This method must be implemented.*


        """
        pass

    def get_family_search_record(self, family_search_record_type):
        """Gets the family search record corresponding to the given family search record ``Type``.


        This method is used to retrieve an object implementing the
        requested record.


        :param family_search_record_type: a family search record type
        :type family_search_record_type: ``osid.type.Type``
        :return: the family search record
        :rtype: ``osid.relationship.records.FamilySearchRecord``
        :raise: ``NullArgument`` -- ``family_search_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_search_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.relationship.records.FamilySearchRecord


class FamilySearchResults(osid_searches.OsidSearchResults):
    """This interface provides a means to capture results of a search and is used as a vehicle to perform a search
        within a
        previous result set."""

    def get_families(self):
        """Gets the family list resulting from a search.


        :return: the family list
        :rtype: ``osid.relationship.FamilyList``
        :raise: ``IllegalState`` -- list already retrieved


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.relationship.FamilyList

    families = property(fget=get_families)

    def get_family_query_inspector(self):
        """Gets the inspector for the query to examine the terms used in the search.


        :return: the family query inspector
        :rtype: ``osid.relationship.FamilyQueryInspector``




        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.relationship.FamilyQueryInspector

    family_query_inspector = property(fget=get_family_query_inspector)

    def get_family_search_results_record(self, family_search_record_type):
        """Gets the family search results record corresponding to the given family search record Type.


        This method is used to retrieve an object implementing the
        requested record.


        :param family_search_record_type: a family search record type
        :type family_search_record_type: ``osid.type.Type``
        :return: the family search results record
        :rtype: ``osid.relationship.records.FamilySearchResultsRecord``
        :raise: ``NullArgument`` -- ``FamilySearchRecordType`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(family_search_record_type)`` is ``false``


        *compliance: mandatory -- This method must be implemented.*


        """
        return # osid.relationship.records.FamilySearchResultsRecord


