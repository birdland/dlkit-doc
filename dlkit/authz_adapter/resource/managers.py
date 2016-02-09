"""AuthZ Adapter implementations of resource managers."""
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
from dlkit.manager_impls.resource import managers as resource_managers




class ResourceProfile(osid_managers.OsidProfile, resource_managers.ResourceProfile):
    """Adapts underlying ResourceProfile methodswith authorization checks."""


    def __init__(self, interface_name):
        osid_managers.OsidProfile.__init__(self)


    def _get_hierarchy_session(self):
        try:
            return self._provider_manager.get_bin_hierarchy_session(
                Id(authority='RESOURCE',
                   namespace='CATALOG',
                   identifier='BIN'))
        except Unsupported:
            return None


    def supports_resource_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_lookup()

    def supports_resource_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_query()

    def supports_resource_search(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_search()

    def supports_resource_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_admin()

    def supports_resource_notification(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_notification()

    def supports_resource_bin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_bin()

    def supports_resource_bin_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_bin_assignment()

    def supports_resource_agent(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_agent()

    def supports_resource_agent_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_resource_agent_assignment()

    def supports_bin_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_lookup()

    def supports_bin_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_query()

    def supports_bin_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_admin()

    def supports_bin_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_hierarchy()

    def supports_bin_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bin_hierarchy_design()

    def get_resource_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_resource_record_types()

    resource_record_types = property(fget=get_resource_record_types)

    def get_resource_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_resource_search_record_types()

    resource_search_record_types = property(fget=get_resource_search_record_types)

    def get_resource_relationship_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_resource_relationship_record_types()

    resource_relationship_record_types = property(fget=get_resource_relationship_record_types)

    def get_resource_relationship_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_resource_relationship_search_record_types()

    resource_relationship_search_record_types = property(fget=get_resource_relationship_search_record_types)

    def get_bin_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_bin_record_types()

    bin_record_types = property(fget=get_bin_record_types)

    def get_bin_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_bin_search_record_types()

    bin_search_record_types = property(fget=get_bin_search_record_types)


class ResourceManager(osid_managers.OsidManager, ResourceProfile, resource_managers.ResourceManager):
    """Adapts underlying ResourceManager methodswith authorization checks."""


    def __init__(self):
        ResourceProfile.__init__(self)


    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:resourceProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('RESOURCE', provider_impl) # need to add version argument


    def get_resource_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_resource_query_session()
            query_session.use_federated_bin_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ResourceLookupSession')(
                self._provider_manager.get_resource_lookup_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    resource_lookup_session = property(fget=get_resource_lookup_session)

    def get_resource_lookup_session_for_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_resource_query_session_for_bin(bin_id)
            query_session.use_federated_bin_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ResourceLookupSession')(
                self._provider_manager.get_resource_lookup_session_for_bin(bin_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_resource_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_resource_query_session()
            query_session.use_federated_bin_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ResourceQuerySession')(
                self._provider_manager.get_resource_query_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    resource_query_session = property(fget=get_resource_query_session)

    def get_resource_query_session_for_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_resource_query_session_for_bin(bin_id)
            query_session.use_federated_bin_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ResourceQuerySession')(
                self._provider_manager.get_resource_query_session_for_bin(bin_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_resource_search_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceSearchSession')(
                self._provider_manager.get_resource_search_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    resource_search_session = property(fget=get_resource_search_session)

    def get_resource_search_session_for_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ResourceSearchSession')(
                self._provider_manager.get_resource_search_session_for_bin(bin_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_resource_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceAdminSession')(
                self._provider_manager.get_resource_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    resource_admin_session = property(fget=get_resource_admin_session)

    def get_resource_admin_session_for_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ResourceAdminSession')(
                self._provider_manager.get_resource_admin_session_for_bin(bin_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_resource_notification_session(self, resource_receiver):
        raise Unimplemented()

    def get_resource_notification_session_for_bin(self, resource_receiver, bin_id):
        raise Unimplemented()

    def get_resource_bin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceBinSession')(
                self._provider_manager.get_resource_bin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    resource_bin_session = property(fget=get_resource_bin_session)

    def get_resource_bin_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceBinAssignmentSession')(
                self._provider_manager.get_resource_bin_assignment_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    resource_bin_assignment_session = property(fget=get_resource_bin_assignment_session)

    def get_resource_agent_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceAgentSession')(
                self._provider_manager.get_resource_agent_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    resource_agent_session = property(fget=get_resource_agent_session)

    def get_resource_agent_session_for_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ResourceAgentSession')(
                self._provider_manager.get_resource_agent_session_for_bin(bin_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_resource_agent_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceAgentAssignmentSession')(
                self._provider_manager.get_resource_agent_assignment_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    resource_agent_assignment_session = property(fget=get_resource_agent_assignment_session)

    def get_resource_agent_assignment_session_for_bin(self, bin_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ResourceAgentAssignmentSession')(
                self._provider_manager.get_resource_agent_assignment_session_for_bin(bin_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_bin_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinLookupSession')(
                self._provider_manager.get_bin_lookup_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bin_lookup_session = property(fget=get_bin_lookup_session)

    def get_bin_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinQuerySession')(
                self._provider_manager.get_bin_query_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bin_query_session = property(fget=get_bin_query_session)

    def get_bin_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinAdminSession')(
                self._provider_manager.get_bin_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bin_admin_session = property(fget=get_bin_admin_session)

    def get_bin_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinHierarchySession')(
                self._provider_manager.get_bin_hierarchy_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bin_hierarchy_session = property(fget=get_bin_hierarchy_session)

    def get_bin_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinHierarchyDesignSession')(
                self._provider_manager.get_bin_hierarchy_design_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bin_hierarchy_design_session = property(fget=get_bin_hierarchy_design_session)

    def get_resource_batch_manager(self):
        raise Unimplemented()

    resource_batch_manager = property(fget=get_resource_batch_manager)

    def get_resource_demographic_manager(self):
        raise Unimplemented()

    resource_demographic_manager = property(fget=get_resource_demographic_manager)


class ResourceProxyManager(osid_managers.OsidProxyManager, ResourceProfile, resource_managers.ResourceProxyManager):
    """Adapts underlying ResourceProxyManager methodswith authorization checks."""


    def __init__(self):
        ResourceProfile.__init__(self, 'ResourceProxyManager')


    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:resourceProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('RESOURCE', provider_impl) # need to add version argument


    def get_resource_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_resource_query_session(proxy)
            query_session.use_federated_bin_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ResourceLookupSession')(
                self._provider_manager.get_resource_lookup_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_resource_lookup_session_for_bin(self, bin_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_resource_query_session_for_bin(bin_id, proxy)
            query_session.use_federated_bin_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ResourceLookupSession')(
                self._provider_manager.get_resource_lookup_session_for_bin(bin_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_resource_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_resource_query_session(proxy)
            query_session.use_federated_bin_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ResourceQuerySession')(
                self._provider_manager.get_resource_query_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_resource_query_session_for_bin(self, bin_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_resource_query_session_for_bin(bin_id, proxy)
            query_session.use_federated_bin_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ResourceQuerySession')(
                self._provider_manager.get_resource_query_session_for_bin(bin_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_resource_search_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceSearchSession')(
                self._provider_manager.get_resource_search_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_search_session_for_bin(self, bin_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ResourceSearchSession')(
                self._provider_manager.get_resource_search_session_for_bin(bin_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceAdminSession')(
                self._provider_manager.get_resource_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_admin_session_for_bin(self, bin_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ResourceAdminSession')(
                self._provider_manager.get_resource_admin_session_for_bin(bin_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_notification_session(self, resource_receiver, proxy):
        raise Unimplemented()

    def get_resource_notification_session_for_bin(self, resource_receiver, bin_id, proxy):
        raise Unimplemented()

    def get_resource_bin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceBinSession')(
                self._provider_manager.get_resource_bin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_bin_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceBinAssignmentSession')(
                self._provider_manager.get_resource_bin_assignment_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_group_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinHierarchySession')(
                self._provider_manager.get_group_hierarchy_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_agent_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceAgentSession')(
                self._provider_manager.get_resource_agent_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_agent_session_for_bin(self, bin_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ResourceAgentSession')(
                self._provider_manager.get_resource_agent_session_for_bin(bin_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_agent_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ResourceAgentAssignmentSession')(
                self._provider_manager.get_resource_agent_assignment_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_agent_assignment_session_for_bin(self, bin_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ResourceAgentAssignmentSession')(
                self._provider_manager.get_resource_agent_assignment_session_for_bin(bin_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bin_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinLookupSession')(
                self._provider_manager.get_bin_lookup_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bin_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinQuerySession')(
                self._provider_manager.get_bin_query_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bin_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinAdminSession')(
                self._provider_manager.get_bin_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bin_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinHierarchySession')(
                self._provider_manager.get_bin_hierarchy_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bin_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BinHierarchyDesignSession')(
                self._provider_manager.get_bin_hierarchy_design_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_resource_batch_proxy_manager(self):
        raise Unimplemented()

    resource_batch_proxy_manager = property(fget=get_resource_batch_proxy_manager)

    def get_resource_demographic_proxy_manager(self):
        raise Unimplemented()

    resource_demographic_proxy_manager = property(fget=get_resource_demographic_proxy_manager)


