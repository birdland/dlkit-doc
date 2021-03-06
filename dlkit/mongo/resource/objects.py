"""Mongodb implementations of resource objects."""

# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods,too-few-public-methods
#     Number of methods are defined in specification
# pylint: disable=protected-access
#     Access to protected methods allowed in package mongo package scope
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification

#from ..id.objects import IdList
#import importlib


import importlib


from . import mdata_conf
from .. import utilities
from ...abstract_osid.resource import objects as abc_resource_objects
from ..osid.metadata import Metadata
from ..primitives import Id
from ..utilities import get_provider_manager
from dlkit.abstract_osid.osid import errors
from dlkit.mongo.osid import objects as osid_objects
from dlkit.primordium.id.primitives import Id




class Resource(abc_resource_objects.Resource, osid_objects.OsidObject):
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


    _record_type_data_sets = {}
    _namespace = 'resource.Resource'


    def __init__(self, osid_object_map, runtime=None):
        osid_objects.OsidObject.__init__(self, osid_object_map, runtime)
        self._record_type_data_sets = self._get_registry('RESOURCE_RECORD_TYPES')
        self._records = dict()
        self._load_records(osid_object_map['recordTypeIds'])
        self._catalog_name = 'bin'


    def is_group(self):
        """Tests if this resource is a group.


        A resource that is a group can be used in the group sessions.


        return: (boolean) - ``true`` if this resource is a group,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.Resource.is_group_template
        return self._my_map['group']

    def is_demographic(self):
        """Tests if this resource is a demographic.


        A resource that is a demographic can be used in the demographic
        service and the group sessions.


        return: (boolean) - ``true`` if this resource is a demographic,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        return self._demographic

    def has_avatar(self):
        """Tests if this resource has an avatar.


        return: (boolean) - ``true`` if this resource has an avatar,
                ``false`` otherwise
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.Resource.has_avatar_template
        return bool(self._my_map['avatarId'])

    def get_avatar_id(self):
        """Gets the asset ``Id``.


        return: (osid.id.Id) - the asset ``Id``
        raise:  IllegalState - ``has_avatar()`` is ``false``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.Resource.get_avatar_id_template
        if not self._my_map['avatarId']:
            raise errors.IllegalState('this Resource has no avatar')
        else:
            return Id(self._my_map['avatarId'])

    avatar_id = property(fget=get_avatar_id)

    def get_avatar(self):
        """Gets the asset.


        return: (osid.repository.Asset) - the asset
        raise:  IllegalState - ``has_avatar()`` is ``false``
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.Resource.get_avatar_template
        if not self._my_map['avatarId']:
            raise errors.IllegalState('this Resource has no avatar')
        mgr = self._get_provider_manager('REPOSITORY')
        if not mgr.supports_asset_lookup():
            raise errors.OperationFailed('Repository does not support Asset lookup')
        lookup_session = mgr.get_asset_lookup_session()
        lookup_session.use_federated_repository_view()
        osid_object = lookup_session.get_asset(self.get_avatar_id())
        return osid_object

    avatar = property(fget=get_avatar)

    @utilities.arguments_not_none
    def get_resource_record(self, resource_record_type):
        """Gets the resource record corresponding to the given ``Resource`` record ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``resource_record_type`` may be the
        ``Type`` returned in ``get_record_types()`` or any of its
        parents in a ``Type`` hierarchy where
        ``has_record_type(resource_record_type)`` is ``true`` .


        arg:    resource_record_type (osid.type.Type): the resource
                record type
        return: (osid.resource.records.ResourceRecord) - the resource
                record
        raise:  NullArgument - ``resource_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(resource_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*


        """
        return self._get_record(resource_record_type)

    def get_object_map(self):
        obj_map = dict(self._my_map)
        if 'agentIds' in obj_map:
            del obj_map['agentIds']
        return osid_objects.OsidObject.get_object_map(self, obj_map)

    object_map = property(fget=get_object_map)


class ResourceForm(abc_resource_objects.ResourceForm, osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Resources``.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``ResourceAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.




    Resources can be designated as a group. The group metadata indicates
    if it is possible to convert a resource to a group and vice-versa.


    """


    _record_type_data_sets = {}
    _namespace = 'resource.Resource'


    def __init__(self, osid_object_map=None, record_types=None, runtime=None, **kwargs):
        osid_objects.OsidForm.__init__(self, runtime=runtime)
        self._record_type_data_sets = self._get_registry('RESOURCE_RECORD_TYPES')
        self._kwargs = kwargs
        if 'catalog_id' in kwargs:
            self._catalog_id = kwargs['catalog_id']
        self._init_metadata(**kwargs)
        self._records = dict()
        self._supported_record_type_ids = []
        if osid_object_map is not None:
            self._for_update = True
            self._my_map = osid_object_map
            self._load_records(osid_object_map['recordTypeIds'])
        else:
            self._my_map = {}
            self._for_update = False
            self._init_map(**kwargs)
            if record_types is not None:
                self._init_records(record_types)
        self._supported_record_type_ids = self._my_map['recordTypeIds']


    def _init_metadata(self, **kwargs):
        osid_objects.OsidObjectForm._init_metadata(self, **kwargs)
        self._group_metadata = {
            'element_id': Id(
                self._authority,
                self._namespace,
                'group')}
        self._group_metadata.update(mdata_conf.RESOURCE_GROUP)
        self._avatar_metadata = {
            'element_id': Id(
                self._authority,
                self._namespace,
                'avatar')}
        self._avatar_metadata.update(mdata_conf.RESOURCE_AVATAR)
        self._group_default = None
        self._avatar_default = self._avatar_metadata['default_id_values'][0]




    def _init_map(self, **kwargs):
        osid_objects.OsidObjectForm._init_map(self)
        self._my_map['assignedBinIds'] = [str(kwargs['bin_id'])]
        self._my_map['group'] = self._group_default
        self._my_map['avatarId'] = self._avatar_default


    def get_group_metadata(self):
        """Gets the metadata for a group.


        return: (osid.Metadata) - metadata for the group
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._group_metadata)
        metadata.update({'existing_group_values': self._my_map['group']})
        return Metadata(**metadata)

    group_metadata = property(fget=get_group_metadata)

    @utilities.arguments_not_none
    def set_group(self, group):
        """Sets the resource as a group.


        arg:    group (boolean): ``true`` if this resource is a group,
                ``false`` otherwise
        raise:  InvalidArgument - ``group`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceForm.set_group_template
        if self.get_group_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_boolean(group):
            raise errors.InvalidArgument()
        self._my_map['group'] = group

    def clear_group(self):
        """Clears the group designation.


        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceForm.clear_group_template
        if (self.get_group_metadata().is_read_only() or
                self.get_group_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['group'] = self._group_default

    group = property(fset=set_group, fdel=clear_group)

    def get_avatar_metadata(self):
        """Gets the metadata for an asset.


        return: (osid.Metadata) - metadata for the asset
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceForm.get_group_metadata_template
        metadata = dict(self._avatar_metadata)
        metadata.update({'existing_avatar_values': self._my_map['avatarId']})
        return Metadata(**metadata)

    avatar_metadata = property(fget=get_avatar_metadata)

    @utilities.arguments_not_none
    def set_avatar(self, asset_id):
        """Sets the avatar asset.


        arg:    asset_id (osid.id.Id): an asset ``Id``
        raise:  InvalidArgument - ``asset_id`` is invalid
        raise:  NoAccess - ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceForm.set_avatar_template
        if self.get_avatar_metadata().is_read_only():
            raise errors.NoAccess()
        if not self._is_valid_id(asset_id):
            raise errors.InvalidArgument()
        self._my_map['avatarId'] = str(asset_id)

    def clear_avatar(self):
        """Clears the asset.


        raise:  NoAccess - ``Metadata.isRequired()`` or
                ``Metadata.isReadOnly()`` is ``true``
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceForm.clear_avatar_template
        if (self.get_avatar_metadata().is_read_only() or
                self.get_avatar_metadata().is_required()):
            raise errors.NoAccess()
        self._my_map['avatarId'] = self._avatar_default

    avatar = property(fset=set_avatar, fdel=clear_avatar)

    @utilities.arguments_not_none
    def get_resource_form_record(self, resource_record_type):
        """Gets the ``ResourceFormRecord`` corresponding to the given ``Resource`` record ``Type``.


        arg:    resource_record_type (osid.type.Type): the resource
                record type
        return: (osid.resource.records.ResourceFormRecord) - the
                resource form record
        raise:  NullArgument - ``resource_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(resource_record_type)``
                is ``false``
        *compliance: mandatory -- This method must be implemented.*


        """
        return self._get_record(resource_record_type)


class ResourceList(abc_resource_objects.ResourceList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ResourceList`` provides a means for accessing ``Resource`` elements sequentially
        either one
    at a time or many at a time.


    Examples: while (rl.hasNext()) { Resource resource =
    rl.getNextResource(); }




    or
      while (rl.hasNext()) {
           Resource[] resources = rl.getNextResources(rl.available());
      }






    """

    def get_next_resource(self):
        """Gets the next ``Resource`` in this list.


        return: (osid.resource.Resource) - the next ``Resource`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``Resource`` is available before calling
                this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return self.next()


    def next(self):
        return self._get_next_object(Resource)

    next_resource = property(fget=get_next_resource)

    @utilities.arguments_not_none
    def get_next_resources(self, n):
        """Gets the next set of ``Resources`` in this list which must be less than or equal to the return from
            ``available()``.


        arg:    n (cardinal): the number of ``Resource`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.resource.Resource) - an array of ``Resource``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(n)


class ResourceNode(abc_resource_objects.ResourceNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BinHierarchySession``.


    """

    def get_resource(self):
        """Gets the ``Resource`` at this node.


        return: (osid.resource.Resource) - the resource represented by
                this node
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    resource = property(fget=get_resource)

    def get_parent_resource_nodes(self):
        """Gets the parents of this resource.


        return: (osid.resource.ResourceNodeList) - the parents of the
                resource
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    parent_resource_nodes = property(fget=get_parent_resource_nodes)

    def get_child_resource_nodes(self):
        """Gets the children of this resource.


        return: (osid.resource.ResourceNodeList) - the children of this
                resource
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()

    child_resource_nodes = property(fget=get_child_resource_nodes)


class ResourceNodeList(abc_resource_objects.ResourceNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``ResourceNodeList`` provides a means for accessing ``ResourceNode`` elements
        sequentially
    either one at a time or many at a time.


    Examples: while (rnl.hasNext()) { ResourceNode node =
    rnl.getNextResourceNode(); }




    or
      while rnl.hasNext()) {
           ResourceNode[] nodes = rnl.getNextResourceNodes(rnl.available());
      }






    """

    def get_next_resource_node(self):
        """Gets the next ``ResourceNode`` in this list.


        return: (osid.resource.ResourceNode) - the next ``ResourceNode``
                in this list. The ``has_next()`` method should be used
                to test that a next ``ResourceNode`` is available before
                calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return self.next()


    def next(self):
        return self._get_next_object(ResourceNode)

    next_resource_node = property(fget=get_next_resource_node)

    @utilities.arguments_not_none
    def get_next_resource_nodes(self, n):
        """Gets the next set of ``ResourceNode`` elements in this list which must be less than or equal to the return
            from ``available()``.


        arg:    n (cardinal): the number of ``ResourceNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.resource.ResourceNode) - an array of
                ``ResourceNode`` elements.The length of the array is
                less than or equal to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(n)


class Bin(abc_resource_objects.Bin, osid_objects.OsidCatalog):
    """An inventory defines a collection of resources."""


    _record_type_data_sets = {}
    _namespace = 'resource.Bin'


    def __init__(self, osid_catalog_map, runtime=None):
        osid_objects.OsidCatalog.__init__(self, osid_catalog_map, runtime)
        self._record_type_data_sets = self._get_registry('BIN_RECORD_TYPES')
        self._records = dict()
        # This check is here for transition purposes:
        try:
            self._load_records(osid_catalog_map['recordTypeIds'])
        except KeyError:
            print 'KeyError: recordTypeIds key not found in ', self._my_map['displayName']['text']
            self._load_records([]) # In place for transition purposes
    @utilities.arguments_not_none
    def get_bin_record(self, bin_record_type):
        """Gets the bin record corresponding to the given ``Bin`` record ``Type``.


        This method is used to retrieve an object implementing the
        requested record. The ``bin_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(bin_record_type)`` is
        ``true`` .


        arg:    bin_record_type (osid.type.Type): the bin record type
        return: (osid.resource.records.BinRecord) - the bin record
        raise:  NullArgument - ``bin_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(bin_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()


class BinForm(abc_resource_objects.BinForm, osid_objects.OsidCatalogForm):
    """This is the form for creating and updating bins.


    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the ``BinAdminSession``.
    For each data element that may be set, metadata may be examined to
    provide display hints or data constraints.


    """


    _record_type_data_sets = {}
    _namespace = 'resource.Bin'


    def __init__(self, osid_catalog_map=None, record_types=None, runtime=None, **kwargs):
        osid_objects.OsidForm.__init__(self, runtime=runtime)
        self._record_type_data_sets = self._get_registry('BIN_RECORD_TYPES')
        self._kwargs = kwargs
        self._init_metadata(**kwargs)
        self._records = dict()
        if osid_catalog_map is not None:
            self._for_update = True
            self._my_map = osid_catalog_map
            self._load_records(osid_catalog_map['recordTypeIds'])
        else:
            self._my_map = {}
            self._for_update = False
            self._init_map(**kwargs)
            if record_types is not None:
                self._init_records(record_types)
        self._supported_record_type_ids = self._my_map['recordTypeIds']


    def _init_metadata(self, **kwargs):
        osid_objects.OsidObjectForm._init_metadata(self)
        osid_objects.OsidSourceableForm._init_metadata(self)


    def _init_map(self, **kwargs):
        osid_objects.OsidObjectForm._init_map(self)
        osid_objects.OsidSourceableForm._init_map(self, **kwargs)
    @utilities.arguments_not_none
    def get_bin_form_record(self, bin_record_type):
        """Gets the ``BinFormRecord`` corresponding to the given bin record ``Type``.


        arg:    bin_record_type (osid.type.Type): the bin record type
        return: (osid.resource.records.BinFormRecord) - the bin form
                record
        raise:  NullArgument - ``bin_record_type`` is ``null``
        raise:  OperationFailed - unable to complete request
        raise:  Unsupported - ``has_record_type(bin_record_type)`` is
                ``false``
        *compliance: mandatory -- This method must be implemented.*


        """
        raise errors.Unimplemented()


class BinList(abc_resource_objects.BinList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BinList`` provides a means for accessing ``Bin`` elements sequentially either one at a
        time
    or many at a time.


    Examples: while (bl.hasNext()) { Bin bin = bl.getNextBin(); }




    or
      while (bl.hasNext()) {
           Bin[] bins = bl.getNextBins(bl.available());
      }






    """

    def get_next_bin(self):
        """Gets the next ``Bin`` in this list.


        return: (osid.resource.Bin) - the next ``Bin`` in this list. The
                ``has_next()`` method should be used to test that a next
                ``Bin`` is available before calling this method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return self.next()


    def next(self):
        return self._get_next_object(Bin)

    next_bin = property(fget=get_next_bin)

    @utilities.arguments_not_none
    def get_next_bins(self, n):
        """Gets the next set of ``Bin`` elements in this list which must be less than or equal to the return from
            ``available()``.


        arg:    n (cardinal): the number of ``Bin`` elements requested
                which must be less than or equal to ``available()``
        return: (osid.resource.Bin) - an array of ``Bin`` elements.The
                length of the array is less than or equal to the number
                specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(n)


class BinNode(abc_resource_objects.BinNode, osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.


    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``BinHierarchySession``.


    """


    def __init__(self, node_map, runtime=None, proxy=None, lookup_session=None):
        osid_objects.OsidNode.__init__(self, node_map)
        self._lookup_session = lookup_session
        self._runtime = runtime
        self._proxy = proxy


    def get_object_node_map(self):
        node_map = dict(self.get_bin().get_object_map())
        node_map['type'] = 'BinNode'
        node_map['parentNodes'] = []
        node_map['childNodes'] = []
        for bin_node in self.get_parent_bin_nodes():
            node_map['parentNodes'].append(bin_node.get_object_node_map())
        for bin_node in self.get_child_bin_nodes():
            node_map['childNodes'].append(bin_node.get_object_node_map())
        return node_map
    def get_bin(self):
        """Gets the ``Bin`` at this node.


        return: (osid.resource.Bin) - the bin represented by this node
        *compliance: mandatory -- This method must be implemented.*


        """
        if self._lookup_session is None:
            mgr = get_provider_manager('RESOURCE', runtime=self._runtime, proxy=self._proxy)
            self._lookup_session = mgr.get_bin_lookup_session()
        return self._lookup_session.get_bin(Id(self._my_map['id']))

    bin = property(fget=get_bin)

    def get_parent_bin_nodes(self):
        """Gets the parents of this bin.


        return: (osid.resource.BinNodeList) - the parents of the ``id``
        *compliance: mandatory -- This method must be implemented.*


        """
        parent_bin_nodes = []
        for node in self._my_map['parentNodes']:
            parent_bin_nodes.append(BinNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return BinNodeList(parent_bin_nodes)

    parent_bin_nodes = property(fget=get_parent_bin_nodes)

    def get_child_bin_nodes(self):
        """Gets the children of this bin.


        return: (osid.resource.BinNodeList) - the children of this bin
        *compliance: mandatory -- This method must be implemented.*


        """
        parent_bin_nodes = []
        for node in self._my_map['childNodes']:
            parent_bin_nodes.append(BinNode(
                node._my_map,
                runtime=self._runtime,
                proxy=self._proxy,
                lookup_session=self._lookup_session))
        return BinNodeList(parent_bin_nodes)

    child_bin_nodes = property(fget=get_child_bin_nodes)


class BinNodeList(abc_resource_objects.BinNodeList, osid_objects.OsidList):
    """Like all ``OsidLists,``  ``BinNodeList`` provides a means for accessing ``BinNode`` elements sequentially either
        one at
    a time or many at a time.


    Examples: while (bnl.hasNext()) { BinNode node =
    bnl.getNextBinNode(); }




    or
      while (bnl.hasNext()) {
           BinNode[] nodes = bnl.getNextBinNodes(bnl.available());
      }






    """

    def get_next_bin_node(self):
        """Gets the next ``BinNode`` in this list.


        return: (osid.resource.BinNode) - the next ``BinNode`` in this
                list. The ``has_next()`` method should be used to test
                that a next ``BinNode`` is available before calling this
                method.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceList.get_next_resource
        return self.next()


    def next(self):
        return self._get_next_object(BinNode)

    next_bin_node = property(fget=get_next_bin_node)

    @utilities.arguments_not_none
    def get_next_bin_nodes(self, n):
        """Gets the next set of ``BinNode`` elements in this list which must be less than or equal to the return from
            ``available()``.


        arg:    n (cardinal): the number of ``BinNode`` elements
                requested which must be less than or equal to
                ``available()``
        return: (osid.resource.BinNode) - an array of ``BinNode``
                elements.The length of the array is less than or equal
                to the number specified.
        raise:  IllegalState - no more elements available in this list
        raise:  OperationFailed - unable to complete request
        *compliance: mandatory -- This method must be implemented.*


        """
        # Implemented from template for osid.resource.ResourceList.get_next_resources
        return self._get_next_n(n)


