from ..osid import markers as osid_markers


class ResourceLocation(osid_markers.Extensible, osid_markers.Browsable):
    """This interface defines a resource at a location."""
    def get_resource_id(self):
        """Gets the ``Id`` of the resource on the route.

        :return: the resource ``Id``
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    resource_id = property(fget=get_resource_id)

    def get_resource(self):
        """Gets the resource on the route.

        :return: the resource
        :rtype: ``osid.resource.Resource``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.resource.Resource

    resource = property(fget=get_resource)

    def has_location(self):
        """Tests if this resource has a known location.

        :return: ``true`` if a location is known, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_location_id(self):
        """Gets the location ``Id`` of the resource.

        :return: the location ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``

        """
        return # osid.id.Id

    location_id = property(fget=get_location_id)

    def get_location(self):
        """Gets the location of the resource.

        :return: the location
        :rtype: ``osid.mapping.Location``
        :raise: ``IllegalState`` -- ``has_location()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.mapping.Location

    location = property(fget=get_location)

    def has_coordinate(self):
        """Tests if this resource has a known coordinate.

        :return: ``true`` if a coordinate is known, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_coordinate(self):
        """Gets the coordinate of the resource.

        :return: the coordinate of the resource
        :rtype: ``osid.mapping.Coordinate``
        :raise: ``IllegalState`` -- ``has_coordinate()`` is ``false``

        """
        return # osid.mapping.Coordinate

    coordinate = property(fget=get_coordinate)

    def get_resource_location_record(self, resource_location_record_type):
        """Gets the map record corresponding to the given ``ResourceLocation`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``resource_location_record_type`` may be
        the ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(resource_location_record_type)`` is ``true`` .

        :param resource_location_record_type: the type of resource location record to retrieve
        :type resource_location_record_type: ``osid.type.Type``
        :return: the resource location record
        :rtype: ``osid.mapping.records.ResourceLocationRecord``
        :raise: ``NullArgument`` -- ``resource_location_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_location_record_type)`` is ``false``

        """
        return # osid.mapping.records.ResourceLocationRecord


