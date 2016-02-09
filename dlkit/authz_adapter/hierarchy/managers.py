"""AuthZ Adapter implementations of hierarchy managers."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from . import sessions
from ..osid.osid_errors import Unimplemented, OperationFailed
from ..osid.osid_errors import Unsupported
from ..primitives import Id
from dlkit.authz_adapter.osid import managers as osid_managers
from dlkit.manager_impls.hierarchy import managers as hierarchy_managers




class HierarchyProfile(osid_managers.OsidProfile, hierarchy_managers.HierarchyProfile):
    """Adapts underlying HierarchyProfile methodswith authorization checks."""


    def __init__(self, interface_name):
        osid_managers.OsidProfile.__init__(self)


    def _get_hierarchy_session(self):
        try:
            return self._provider_manager.get_hierarchy_hierarchy_session(
                Id(authority='HIERARCHY',
                   namespace='CATALOG',
                   identifier='HIERARCHY'))
        except Unsupported:
            return None


    def supports_hierarchy_traversal(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_hierarchy_traversal()

    def supports_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_hierarchy_design()

    def supports_hierarchy_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_hierarchy_lookup()

    def supports_hierarchy_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_hierarchy_admin()

    def get_hierarchy_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_hierarchy_record_types()

    hierarchy_record_types = property(fget=get_hierarchy_record_types)

    def get_hierarchy_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_hierarchy_search_record_types()

    hierarchy_search_record_types = property(fget=get_hierarchy_search_record_types)


class HierarchyManager(osid_managers.OsidManager, HierarchyProfile, hierarchy_managers.HierarchyManager):
    """Adapts underlying HierarchyManager methodswith authorization checks."""


    def __init__(self):
        HierarchyProfile.__init__(self)


    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:hierarchyProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('HIERARCHY', provider_impl) # need to add version argument


    def get_hierarchy_traversal_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'HierarchyTraversalSession')(
                self._provider_manager.get_hierarchy_traversal_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    hierarchy_traversal_session = property(fget=get_hierarchy_traversal_session)

    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'HierarchyTraversalSession')(
                self._provider_manager.get_hierarchy_traversal_session_for_hierarchy(hierarchy_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'HierarchyDesignSession')(
                self._provider_manager.get_hierarchy_design_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    hierarchy_design_session = property(fget=get_hierarchy_design_session)

    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'HierarchyDesignSession')(
                self._provider_manager.get_hierarchy_design_session_for_hierarchy(hierarchy_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_hierarchy_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'HierarchyLookupSession')(
                self._provider_manager.get_hierarchy_lookup_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    hierarchy_lookup_session = property(fget=get_hierarchy_lookup_session)

    def get_hierarchy_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'HierarchyAdminSession')(
                self._provider_manager.get_hierarchy_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    hierarchy_admin_session = property(fget=get_hierarchy_admin_session)


class HierarchyProxyManager(osid_managers.OsidProxyManager, HierarchyProfile, hierarchy_managers.HierarchyProxyManager):
    """Adapts underlying HierarchyProxyManager methodswith authorization checks."""


    def __init__(self):
        HierarchyProfile.__init__(self, 'HierarchyProxyManager')


    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:hierarchyProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('HIERARCHY', provider_impl) # need to add version argument


    def get_hierarchy_traversal_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'HierarchyTraversalSession')(
                self._provider_manager.get_hierarchy_traversal_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_hierarchy_traversal_session_for_hierarchy(self, hierarchy_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'HierarchyTraversalSession')(
                self._provider_manager.get_hierarchy_traversal_session_for_hierarchy(hierarchy_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'HierarchyDesignSession')(
                self._provider_manager.get_hierarchy_design_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_hierarchy_design_session_for_hierarchy(self, hierarchy_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'HierarchyDesignSession')(
                self._provider_manager.get_hierarchy_design_session_for_hierarchy(hierarchy_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_hierarchy_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'HierarchyLookupSession')(
                self._provider_manager.get_hierarchy_lookup_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_hierarchy_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'HierarchyAdminSession')(
                self._provider_manager.get_hierarchy_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()


