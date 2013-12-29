from ..osid import search_orders as osid_search_orders


class AssetSearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidAggregateableSearchOrder, osid_search_orders.OsidSourceableSearchOrder):
    """An interface for specifying the ordering of search results."""
    def order_by_title(self, style):
        """Specifies a preference for ordering the result set by asset title.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_public_domain(self, style):
        """Specifies a preference for grouping the result set by published domain.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_distribute_verbatim(self, style):
        """Specifies a preference for grouping the result set by the ability to distribute copies.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_distribute_alterations(self, style):
        """Specifies a preference for grouping the result set by the ability to distribute alterations.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_distribute_compositions(self, style):
        """Specifies a preference for grouping the result set by the ability to distribute compositions.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_source(self, style):
        """Specifies a preference for ordering the result set by asset source.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def supports_source_search_order(self):
        """Tests if a source order interface is available.

        :return: ``true`` if a source search order is available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_source_search_order(self):
        """Gets the source order.

        :return: the resource search order for the source
        :rtype: ``osid.resource.ResourceSearchOrder``
        :raise: ``Unimplemented`` -- ``supports_source_search_order()`` is ``false``

        """
        return # osid.resource.ResourceSearchOrder

    source_search_order = property(fget=get_source_search_order)

    def order_by_created_date(self, style):
        """Specifies a preference for ordering the result set by created date.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_published(self, style):
        """Specifies a preference for grouping the result set by published status.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_published_date(self, style):
        """Specifies a preference for ordering the result set by published date.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_principal_credit_string(self, style):
        """Specifies a preference for ordering the result set by the principal credit string.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def order_by_temporal_coverage(self, style):
        """Specifies a preference for ordering the result set by temporal coverage.

        :param style: search order record
        :type style: ``osid.SearchOrderStyle``
        :raise: ``NullArgument`` -- ``style`` is ``null``

        """
        pass

    def get_asset_search_order_record(self, asset_record_type):
        """Gets the asset search order record corresponding to the given asset record ``Type``.

        Multiple retrievals return the same underlying object.

        :param asset_record_type: an asset record type
        :type asset_record_type: ``osid.type.Type``
        :return: the asset search order record
        :rtype: ``osid.repository.records.AssetSearchOrderRecord``
        :raise: ``NullArgument`` -- ``asset_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(asset_record_type)`` is ``false``

        """
        return # osid.repository.records.AssetSearchOrderRecord


class CompositionSearchOrder(osid_search_orders.OsidObjectSearchOrder, osid_search_orders.OsidContainableSearchOrder, osid_search_orders.OsidOperableSearchOrder, osid_search_orders.OsidSourceableSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_composition_search_order_record(self, composition_record_type):
        """Gets the composition search order record corresponding to the given repository record ``Type``.

        Multiple retrievals return the same underlying object.

        :param composition_record_type: a composition record type
        :type composition_record_type: ``osid.type.Type``
        :return: the composition search order record
        :rtype: ``osid.repository.records.CompositionSearchOrderRecord``
        :raise: ``NullArgument`` -- ``composition_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``has_record_type(composition_record_type)`` is ``false``

        """
        return # osid.repository.records.CompositionSearchOrderRecord


class RepositorySearchOrder(osid_search_orders.OsidCatalogSearchOrder):
    """An interface for specifying the ordering of search results."""
    def get_repository_search_order_record(self, repository_record_type):
        """Gets the repository search order record corresponding to the given repository record ``Type``.

        Multiple retrievals return the same underlying object.

        :param repository_record_type: a repository record type
        :type repository_record_type: ``osid.type.Type``
        :return: the repository search order record
        :rtype: ``osid.repository.records.RepositorySearchOrderRecord``
        :raise: ``NullArgument`` -- ``repository_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(repository_record_type)`` is ``false``

        """
        return # osid.repository.records.RepositorySearchOrderRecord


