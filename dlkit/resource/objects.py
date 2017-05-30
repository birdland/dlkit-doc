
from ..osid import objects as osid_objects
from ..osid import sessions as osid_sessions


class Resource(osid_objects.OsidObject):
    """A ``Resource`` represents an arbitrary entity.

    Resources are used to define an object to accompany an OSID ``Id``
    used in other OSIDs. A resource may be used to represent a meeting
    room in the Scheduling OSID, or a student in the Course OSID.

    A ``Resource`` may also represent a group or organization. A
    provider may present such a group in an opaque manner through a
    single resource definition, or the provider may expose the resource
    collection for examination or manipulation. If such a resource
    collection is visible, ``is_group()`` is ``true`` and can be used in
    one of the group sessions available in this OSID.

    """

    def is_group(self):
        """Tests if this resource is a group.

        A resource that is a group can be used in the group sessions.

        :return: ``true`` if this resource is a group, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def is_demographic(self):
        """Tests if this resource is a demographic.

        A resource that is a demographic can be used in the demographic
        service and the group sessions.

        :return: ``true`` if this resource is a demographic, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def has_avatar(self):
        """Tests if this resource has an avatar.

        :return: ``true`` if this resource has an avatar, ``false`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def get_avatar_id(self):
        """Gets the asset ``Id``.

        :return: the asset ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``has_avatar()`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    avatar_id = property(fget=get_avatar_id)

    def get_avatar(self):
        """Gets the asset.

        :return: the asset
        :rtype: ``osid.repository.Asset``
        :raise: ``IllegalState`` -- ``has_avatar()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.Asset

    avatar = property(fget=get_avatar)

    def get_resource_record(self, resource_record_type):
        """Gets the resource record corresponding to the given ``Resource`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``resource_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(resource_record_type)`` is ``true`` .

        :param resource_record_type: the resource record type
        :type resource_record_type: ``osid.type.Type``
        :return: the resource record
        :rtype: ``osid.resource.records.ResourceRecord``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.ResourceRecord


class ResourceForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Resources``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ResourceAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    Resources can be designated as a group. The group metadata indicates
    if it is possible to convert a resource to a group and vice-versa.

    """

    def get_group_metadata(self):
        """Gets the metadata for a group.

        :return: metadata for the group
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    group_metadata = property(fget=get_group_metadata)

    def set_group(self, group):
        """Sets the resource as a group.

        :param group: ``true`` if this resource is a group, ``false`` otherwise
        :type group: ``boolean``
        :raise: ``InvalidArgument`` -- ``group`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_group(self):
        """Clears the group designation.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    group = property(fset=set_group, fdel=clear_group)

    def get_avatar_metadata(self):
        """Gets the metadata for an asset.

        :return: metadata for the asset
        :rtype: ``osid.Metadata``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.Metadata

    avatar_metadata = property(fget=get_avatar_metadata)

    def set_avatar(self, asset_id):
        """Sets the avatar asset.

        :param asset_id: an asset ``Id``
        :type asset_id: ``osid.id.Id``
        :raise: ``InvalidArgument`` -- ``asset_id`` is invalid
        :raise: ``NoAccess`` -- ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    def clear_avatar(self):
        """Clears the asset.

        :raise: ``NoAccess`` -- ``Metadata.isRequired()`` or ``Metadata.isReadOnly()`` is ``true``

        *compliance: mandatory -- This method must be implemented.*

        """
        pass

    avatar = property(fset=set_avatar, fdel=clear_avatar)

    def get_resource_form_record(self, resource_record_type):
        """Gets the ``ResourceFormRecord`` corresponding to the given ``Resource`` record ``Type``.

        :param resource_record_type: the resource record type
        :type resource_record_type: ``osid.type.Type``
        :return: the resource form record
        :rtype: ``osid.resource.records.ResourceFormRecord``
        :raise: ``NullArgument`` -- ``resource_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(resource_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.ResourceFormRecord


class ResourceList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ResourceList`` provides a means for accessing ``Resource`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Resource resource =
    rl.getNextResource(); }

    or
      while (rl.hasNext()) {
           Resource[] resources = rl.getNextResources(rl.available());
      }

    """

    def get_next_resource(self):
        """Gets the next ``Resource`` in this list.

        :return: the next ``Resource`` in this list. The ``has_next()`` method should be used to test that a next ``Resource`` is available before calling this method.
        :rtype: ``osid.resource.Resource``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    next_resource = property(fget=get_next_resource)

    def get_next_resources(self, n):
        """Gets the next set of ``Resources`` in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Resource`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Resource`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.resource.Resource``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource


class ResourceNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BinHierarchySession``.

    """

    def get_resource(self):
        """Gets the ``Resource`` at this node.

        :return: the resource represented by this node
        :rtype: ``osid.resource.Resource``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Resource

    resource = property(fget=get_resource)

    def get_parent_resource_nodes(self):
        """Gets the parents of this resource.

        :return: the parents of the resource
        :rtype: ``osid.resource.ResourceNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceNodeList

    parent_resource_nodes = property(fget=get_parent_resource_nodes)

    def get_child_resource_nodes(self):
        """Gets the children of this resource.

        :return: the children of this resource
        :rtype: ``osid.resource.ResourceNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceNodeList

    child_resource_nodes = property(fget=get_child_resource_nodes)


class ResourceNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ResourceNodeList`` provides a means for accessing ``ResourceNode`` elements sequentially either one at a time or many at a time.

    Examples: while (rnl.hasNext()) { ResourceNode node =
    rnl.getNextResourceNode(); }

    or
      while rnl.hasNext()) {
           ResourceNode[] nodes = rnl.getNextResourceNodes(rnl.available());
      }

    """

    def get_next_resource_node(self):
        """Gets the next ``ResourceNode`` in this list.

        :return: the next ``ResourceNode`` in this list. The ``has_next()`` method should be used to test that a next ``ResourceNode`` is available before calling this method.
        :rtype: ``osid.resource.ResourceNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceNode

    next_resource_node = property(fget=get_next_resource_node)

    def get_next_resource_nodes(self, n):
        """Gets the next set of ``ResourceNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``ResourceNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``ResourceNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.resource.ResourceNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceNode


class Bin(osid_objects.OsidCatalog, osid_sessions.OsidSession):
    """An inventory defines a collection of resources."""

    def get_bin_record(self, bin_record_type):
        """Gets the bin record corresponding to the given ``Bin`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``bin_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(bin_record_type)`` is
        ``true`` .

        :param bin_record_type: the bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the bin record
        :rtype: ``osid.resource.records.BinRecord``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.BinRecord


class BinForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating bins.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the ``BinAdminSession``.
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.

    """

    def get_bin_form_record(self, bin_record_type):
        """Gets the ``BinFormRecord`` corresponding to the given bin record ``Type``.

        :param bin_record_type: the bin record type
        :type bin_record_type: ``osid.type.Type``
        :return: the bin form record
        :rtype: ``osid.resource.records.BinFormRecord``
        :raise: ``NullArgument`` -- ``bin_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(bin_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.records.BinFormRecord


class BinList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BinList`` provides a means for accessing ``Bin`` elements sequentially either one at a time or many at a time.

    Examples: while (bl.hasNext()) { Bin bin = bl.getNextBin(); }

    or
      while (bl.hasNext()) {
           Bin[] bins = bl.getNextBins(bl.available());
      }

    """

    def get_next_bin(self):
        """Gets the next ``Bin`` in this list.

        :return: the next ``Bin`` in this list. The ``has_next()`` method should be used to test that a next ``Bin`` is available before calling this method.
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    next_bin = property(fget=get_next_bin)

    def get_next_bins(self, n):
        """Gets the next set of ``Bin`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``Bin`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Bin`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.resource.Bin``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin


class BinNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BinHierarchySession``.

    """

    def get_bin(self):
        """Gets the ``Bin`` at this node.

        :return: the bin represented by this node
        :rtype: ``osid.resource.Bin``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.Bin

    bin = property(fget=get_bin)

    def get_parent_bin_nodes(self):
        """Gets the parents of this bin.

        :return: the parents of the ``id``
        :rtype: ``osid.resource.BinNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinNodeList

    parent_bin_nodes = property(fget=get_parent_bin_nodes)

    def get_child_bin_nodes(self):
        """Gets the children of this bin.

        :return: the children of this bin
        :rtype: ``osid.resource.BinNodeList``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinNodeList

    child_bin_nodes = property(fget=get_child_bin_nodes)


class BinNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BinNodeList`` provides a means for accessing ``BinNode`` elements sequentially either one at a time or many at a time.

    Examples: while (bnl.hasNext()) { BinNode node =
    bnl.getNextBinNode(); }

    or
      while (bnl.hasNext()) {
           BinNode[] nodes = bnl.getNextBinNodes(bnl.available());
      }

    """

    def get_next_bin_node(self):
        """Gets the next ``BinNode`` in this list.

        :return: the next ``BinNode`` in this list. The ``has_next()`` method should be used to test that a next ``BinNode`` is available before calling this method.
        :rtype: ``osid.resource.BinNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinNode

    next_bin_node = property(fget=get_next_bin_node)

    def get_next_bin_nodes(self, n):
        """Gets the next set of ``BinNode`` elements in this list which must be less than or equal to the return from ``available()``.

        :param n: the number of ``BinNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``BinNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.resource.BinNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.BinNode


