"""DLKit Services implementations of assessment service."""
# pylint: disable=no-init
#     osid specification includes some 'marker' interfaces.
# pylint: disable=too-many-ancestors
#     number of ancestors defined in spec.
# pylint: disable=too-few-public-methods,too-many-public-methods
#     number of methods defined in spec. Worse yet, these are aggregates.
# pylint: disable=invalid-name
#     method and class names defined in spec.
# pylint: disable=no-self-use,unused-argument
#     to catch unimplemented methods.
# pylint: disable=super-init-not-called
#     it just isn't.



from . import osid
from ..abstract_osid.assessment import objects as abc_assessment_objects
from .osid_errors import Unimplemented, IllegalState
from dlkit.manager_impls.assessment import managers as assessment_managers



DEFAULT = 0
COMPARATIVE = 0
PLENARY = 1
FEDERATED = 0
ISOLATED = 1
AUTOMATIC = 0
MANDATORY = 1
DISABLED = -1


class AssessmentProfile(osid.OsidProfile, assessment_managers.AssessmentProfile):
    """AssessmentProfile convenience adapter including related Session methods."""


    def __init__(self):
        self._provider_manager = None
    def supports_assessment(self):
        """Pass through to provider supports_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment()

    def supports_item_lookup(self):
        """Pass through to provider supports_item_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_lookup()

    def supports_item_query(self):
        """Pass through to provider supports_item_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_query()

    def supports_item_search(self):
        """Pass through to provider supports_item_search"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_search()

    def supports_item_admin(self):
        """Pass through to provider supports_item_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_admin()

    def supports_item_notification(self):
        """Pass through to provider supports_item_notification"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_notification()

    def supports_item_bank(self):
        """Pass through to provider supports_item_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_bank()

    def supports_item_bank_assignment(self):
        """Pass through to provider supports_item_bank_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_bank_assignment()

    def supports_assessment_lookup(self):
        """Pass through to provider supports_assessment_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_lookup()

    def supports_assessment_query(self):
        """Pass through to provider supports_assessment_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_query()

    def supports_assessment_admin(self):
        """Pass through to provider supports_assessment_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_admin()

    def supports_assessment_bank(self):
        """Pass through to provider supports_assessment_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_bank()

    def supports_assessment_bank_assignment(self):
        """Pass through to provider supports_assessment_bank_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_bank_assignment()

    def supports_assessment_basic_authoring(self):
        """Pass through to provider supports_assessment_basic_authoring"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_basic_authoring()

    def supports_assessment_offered_lookup(self):
        """Pass through to provider supports_assessment_offered_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_lookup()

    def supports_assessment_offered_query(self):
        """Pass through to provider supports_assessment_offered_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_query()

    def supports_assessment_offered_admin(self):
        """Pass through to provider supports_assessment_offered_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_admin()

    def supports_assessment_offered_bank(self):
        """Pass through to provider supports_assessment_offered_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_bank()

    def supports_assessment_offered_bank_assignment(self):
        """Pass through to provider supports_assessment_offered_bank_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_bank_assignment()

    def supports_assessment_taken_lookup(self):
        """Pass through to provider supports_assessment_taken_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_lookup()

    def supports_assessment_taken_query(self):
        """Pass through to provider supports_assessment_taken_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_query()

    def supports_assessment_taken_admin(self):
        """Pass through to provider supports_assessment_taken_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_admin()

    def supports_assessment_taken_bank(self):
        """Pass through to provider supports_assessment_taken_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_bank()

    def supports_assessment_taken_bank_assignment(self):
        """Pass through to provider supports_assessment_taken_bank_assignment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_bank_assignment()

    def supports_bank_lookup(self):
        """Pass through to provider supports_bank_lookup"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_lookup()

    def supports_bank_query(self):
        """Pass through to provider supports_bank_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_query()

    def supports_bank_admin(self):
        """Pass through to provider supports_bank_admin"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_admin()

    def supports_bank_hierarchy(self):
        """Pass through to provider supports_bank_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_hierarchy()

    def supports_bank_hierarchy_design(self):
        """Pass through to provider supports_bank_hierarchy_design"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_hierarchy_design()

    def get_item_record_types(self):
        """Pass through to provider get_item_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_item_record_types()

    item_record_types = property(fget=get_item_record_types)

    def get_item_search_record_types(self):
        """Pass through to provider get_item_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_item_search_record_types()

    item_search_record_types = property(fget=get_item_search_record_types)

    def get_assessment_record_types(self):
        """Pass through to provider get_assessment_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_record_types()

    assessment_record_types = property(fget=get_assessment_record_types)

    def get_assessment_search_record_types(self):
        """Pass through to provider get_assessment_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_search_record_types()

    assessment_search_record_types = property(fget=get_assessment_search_record_types)

    def get_assessment_offered_record_types(self):
        """Pass through to provider get_assessment_offered_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_offered_record_types()

    assessment_offered_record_types = property(fget=get_assessment_offered_record_types)

    def get_assessment_offered_search_record_types(self):
        """Pass through to provider get_assessment_offered_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_offered_search_record_types()

    assessment_offered_search_record_types = property(fget=get_assessment_offered_search_record_types)

    def get_assessment_taken_record_types(self):
        """Pass through to provider get_assessment_taken_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_taken_record_types()

    assessment_taken_record_types = property(fget=get_assessment_taken_record_types)

    def get_assessment_taken_search_record_types(self):
        """Pass through to provider get_assessment_taken_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_taken_search_record_types()

    assessment_taken_search_record_types = property(fget=get_assessment_taken_search_record_types)

    def get_assessment_section_record_types(self):
        """Pass through to provider get_assessment_section_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_section_record_types()

    assessment_section_record_types = property(fget=get_assessment_section_record_types)

    def get_bank_record_types(self):
        """Pass through to provider get_bank_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_bank_record_types()

    bank_record_types = property(fget=get_bank_record_types)

    def get_bank_search_record_types(self):
        """Pass through to provider get_bank_search_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_bank_search_record_types()

    bank_search_record_types = property(fget=get_bank_search_record_types)


class AssessmentManager(osid.OsidManager, osid.OsidSession, AssessmentProfile, assessment_managers.AssessmentManager):
    """AssessmentManager convenience adapter including related Session methods."""


    def __init__(self, proxy=None):
        self._runtime = None
        self._provider_manager = None
        self._provider_sessions = dict()
        self._session_management = AUTOMATIC
        self._bank_view = DEFAULT
        # This is to initialize self._proxy
        osid.OsidSession.__init__(self, proxy)


    # def _get_view(self, view):
    #     """Gets the currently set view"""
    #     if view in self._views:
    #         return self._views[view]
    #     else:
    #         self._views[view] = DEFAULT
    #         return DEFAULT


    def _set_bank_view(self, session):
        """Sets the underlying bank view to match current view"""
        if self._bank_view == COMPARATIVE:
            try:
                session.use_comparative_bank_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_plenary_bank_view()
            except AttributeError:
                pass


    def _get_provider_session(self, session_name, proxy=None):
        """Gets the session for the provider"""
        if self._proxy is None:
            self._proxy = proxy
        if session_name in self._provider_sessions:
            return self._provider_sessions[session_name]
        else:
            session = self._instantiate_session('get_' + session_name, self._proxy)
            self._set_bank_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session


    def _instantiate_session(self, method_name, proxy=None, *args, **kwargs):
        """Instantiates a provider session"""
        session_class = getattr(self._provider_manager, method_name)
        if proxy is None:
            return session_class(*args, **kwargs)
        else:
            return session_class(proxy=proxy, *args, **kwargs)


    def initialize(self, runtime):
        """OSID Manager initialize"""
        from .primitives import Id
        if self._runtime is not None:
            raise IllegalState('Manager has already been initialized')
        self._runtime = runtime
        config = runtime.get_configuration()
        parameter_id = Id('parameter:assessmentProviderImpl@dlkit_service')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        if self._proxy is None:
            # need to add version argument
            self._provider_manager = runtime.get_manager('ASSESSMENT', provider_impl)
        else:
            # need to add version argument
            self._provider_manager = runtime.get_proxy_manager('ASSESSMENT', provider_impl)


    def close_sessions(self):
        """Close all sessions, unless session management is set to MANDATORY"""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()


    def use_automatic_session_management(self):
        """Session state will be saved unless closed by consumers"""
        self._session_management = AUTOMATIC


    def use_mandatory_session_management(self):
        """Session state will be saved and can not be closed by consumers"""
        self._session_management = MANDATORY


    def disable_session_management(self):
        """Session state will never be saved"""
        self._session_management = DISABLED
        self.close_sessions()
    def get_assessment_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_session=session)

    assessment_session = property(fget=get_assessment_session)

    def get_assessment_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_session=session)

    def get_item_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_item_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_item_lookup_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, item_lookup_session=session)

    item_lookup_session = property(fget=get_item_lookup_session)

    def get_item_lookup_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_item_lookup_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_item_lookup_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_item_lookup_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            item_lookup_session=session)

    def get_item_query_session(self, *args, **kwargs):
        """Pass through to provider get_item_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_item_query_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, item_query_session=session)

    item_query_session = property(fget=get_item_query_session)

    def get_item_query_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_item_query_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_item_query_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_item_query_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            item_query_session=session)

    def get_item_search_session(self, *args, **kwargs):
        """Pass through to provider get_item_search_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_item_search_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, item_search_session=session)

    item_search_session = property(fget=get_item_search_session)

    def get_item_search_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_item_search_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_item_search_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_item_search_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            item_search_session=session)

    def get_item_admin_session(self, *args, **kwargs):
        """Pass through to provider get_item_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_item_admin_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, item_admin_session=session)

    item_admin_session = property(fget=get_item_admin_session)

    def get_item_admin_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_item_admin_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_item_admin_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_item_admin_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            item_admin_session=session)

    def get_item_notification_session(self, *args, **kwargs):
        """Pass through to provider get_item_notification_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_notification_session_catalog_template
        session = self._instantiate_session(method_name='get_item_notification_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, item_notification_session=session)

    def get_item_bank_session(self, *args, **kwargs):
        """Pass through to provider get_item_bank_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('item_bank_session', *args, **kwargs)
        return self

    item_bank_session = property(fget=get_item_bank_session)

    def get_item_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_item_bank_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('item_bank_assignment_session', *args, **kwargs)
        return self

    item_bank_assignment_session = property(fget=get_item_bank_assignment_session)

    def get_assessment_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_lookup_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_lookup_session=session)

    assessment_lookup_session = property(fget=get_assessment_lookup_session)

    def get_assessment_lookup_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_lookup_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_lookup_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_lookup_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_lookup_session=session)

    def get_assessment_query_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_query_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_query_session=session)

    assessment_query_session = property(fget=get_assessment_query_session)

    def get_assessment_query_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_query_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_query_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_query_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_query_session=session)

    def get_assessment_admin_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_admin_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_admin_session=session)

    assessment_admin_session = property(fget=get_assessment_admin_session)

    def get_assessment_admin_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_admin_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_admin_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_admin_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_admin_session=session)

    def get_assessment_bank_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_bank_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('assessment_bank_session', *args, **kwargs)
        return self

    assessment_bank_session = property(fget=get_assessment_bank_session)

    def get_assessment_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_bank_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('assessment_bank_assignment_session', *args, **kwargs)
        return self

    assessment_bank_assignment_session = property(fget=get_assessment_bank_assignment_session)

    def get_assessment_basic_authoring_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_basic_authoring_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_basic_authoring_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_basic_authoring_session=session)

    assessment_basic_authoring_session = property(fget=get_assessment_basic_authoring_session)

    def get_assessment_basic_authoring_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_basic_authoring_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_basic_authoring_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_basic_authoring_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_basic_authoring_session=session)

    def get_assessment_offered_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_offered_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_offered_lookup_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_offered_lookup_session=session)

    assessment_offered_lookup_session = property(fget=get_assessment_offered_lookup_session)

    def get_assessment_offered_lookup_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_offered_lookup_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_offered_lookup_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_offered_lookup_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_offered_lookup_session=session)

    def get_assessment_offered_query_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_offered_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_offered_query_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_offered_query_session=session)

    assessment_offered_query_session = property(fget=get_assessment_offered_query_session)

    def get_assessment_offered_query_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_offered_query_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_offered_query_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_offered_query_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_offered_query_session=session)

    def get_assessment_offered_admin_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_offered_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_offered_admin_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_offered_admin_session=session)

    assessment_offered_admin_session = property(fget=get_assessment_offered_admin_session)

    def get_assessment_offered_admin_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_offered_admin_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_offered_admin_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_offered_admin_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_offered_admin_session=session)

    def get_assessment_offered_bank_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_offered_bank_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('assessment_offered_bank_session', *args, **kwargs)
        return self

    assessment_offered_bank_session = property(fget=get_assessment_offered_bank_session)

    def get_assessment_offered_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_offered_bank_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('assessment_offered_bank_assignment_session', *args, **kwargs)
        return self

    assessment_offered_bank_assignment_session = property(fget=get_assessment_offered_bank_assignment_session)

    def get_assessment_taken_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_taken_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_taken_lookup_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_taken_lookup_session=session)

    assessment_taken_lookup_session = property(fget=get_assessment_taken_lookup_session)

    def get_assessment_taken_lookup_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_taken_lookup_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_taken_lookup_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_taken_lookup_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_taken_lookup_session=session)

    def get_assessment_taken_query_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_taken_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_taken_query_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_taken_query_session=session)

    assessment_taken_query_session = property(fget=get_assessment_taken_query_session)

    def get_assessment_taken_query_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_taken_query_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_taken_query_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_taken_query_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_taken_query_session=session)

    def get_assessment_taken_admin_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_taken_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_catalog_template
        session = self._instantiate_session(method_name='get_assessment_taken_admin_session', proxy=self._proxy, *args, **kwargs)
        return Bank(
            self._provider_manager,
            session.get_bank(),
            self._proxy, assessment_taken_admin_session=session)

    assessment_taken_admin_session = property(fget=get_assessment_taken_admin_session)

    def get_assessment_taken_admin_session_for_bank(self, *args, **kwargs):
        """Pass through to provider get_assessment_taken_admin_session_for_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_catalog_template
        if self._proxy:
            session = self._provider_manager.get_assessment_taken_admin_session_for_bank(proxy=self._proxy, *args, **kwargs)
        else:
            session = self._provider_manager.get_assessment_taken_admin_session_for_bank(*args, **kwargs)
        return Bank(
            self._provider_manager,
            self.get_bank(*args, **kwargs),
            self._proxy,
            assessment_taken_admin_session=session)

    def get_assessment_taken_bank_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_taken_bank_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('assessment_taken_bank_session', *args, **kwargs)
        return self

    assessment_taken_bank_session = property(fget=get_assessment_taken_bank_session)

    def get_assessment_taken_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider get_assessment_taken_bank_assignment_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('assessment_taken_bank_assignment_session', *args, **kwargs)
        return self

    assessment_taken_bank_assignment_session = property(fget=get_assessment_taken_bank_assignment_session)

    def get_bank_lookup_session(self, *args, **kwargs):
        """Pass through to provider get_bank_lookup_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('bank_lookup_session', *args, **kwargs)
        return self

    bank_lookup_session = property(fget=get_bank_lookup_session)

    def get_bank_query_session(self, *args, **kwargs):
        """Pass through to provider get_bank_query_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('bank_query_session', *args, **kwargs)
        return self

    bank_query_session = property(fget=get_bank_query_session)

    def get_bank_admin_session(self, *args, **kwargs):
        """Pass through to provider get_bank_admin_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('bank_admin_session', *args, **kwargs)
        return self

    bank_admin_session = property(fget=get_bank_admin_session)

    def get_bank_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider get_bank_hierarchy_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('bank_hierarchy_session', *args, **kwargs)
        return self

    bank_hierarchy_session = property(fget=get_bank_hierarchy_session)

    def get_bank_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider get_bank_hierarchy_design_session"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_manager_template
        if self._session_management != DISABLED:
            self._get_provider_session('bank_hierarchy_design_session', *args, **kwargs)
        return self

    bank_hierarchy_design_session = property(fget=get_bank_hierarchy_design_session)

    def get_assessment_authoring_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    assessment_authoring_manager = property(fget=get_assessment_authoring_manager)

    def get_assessment_batch_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    assessment_batch_manager = property(fget=get_assessment_batch_manager)
##
# The following methods are from osid.assessment.ItemBankSession

    def can_lookup_item_bank_mappings(self):
        """Pass through to provider ItemBankSession.can_lookup_item_bank_mappings"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._get_provider_session('item_bank_session').can_lookup_item_bank_mappings()

    def use_comparative_bank_view(self):
        """Pass through to provider ItemBankSession.use_comparative_bank_view"""
        self._bank_view = COMPARATIVE
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_comparative_bank_view()
            except AttributeError:
                pass

    def use_plenary_bank_view(self):
        """Pass through to provider ItemBankSession.use_plenary_bank_view"""
        self._bank_view = PLENARY
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_plenary_bank_view()
            except AttributeError:
                pass

    def get_item_ids_by_bank(self, *args, **kwargs):
        """Pass through to provider ItemBankSession.get_item_ids_by_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        return self._get_provider_session('item_bank_session').get_item_ids_by_bank(*args, **kwargs)

    def get_items_by_bank(self, *args, **kwargs):
        """Pass through to provider ItemBankSession.get_items_by_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._get_provider_session('item_bank_session').get_items_by_bank(*args, **kwargs)

    def get_item_ids_by_banks(self, *args, **kwargs):
        """Pass through to provider ItemBankSession.get_item_ids_by_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        return self._get_provider_session('item_bank_session').get_item_ids_by_banks(*args, **kwargs)

    def get_items_by_banks(self, *args, **kwargs):
        """Pass through to provider ItemBankSession.get_items_by_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        return self._get_provider_session('item_bank_session').get_items_by_banks(*args, **kwargs)

    def get_bank_ids_by_item(self, *args, **kwargs):
        """Pass through to provider ItemBankSession.get_bank_ids_by_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        return self._get_provider_session('item_bank_session').get_bank_ids_by_item(*args, **kwargs)

    def get_banks_by_item(self, *args, **kwargs):
        """Pass through to provider ItemBankSession.get_banks_by_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        return self._get_provider_session('item_bank_session').get_banks_by_item(*args, **kwargs)


##
# The following methods are from osid.assessment.ItemBankAssignmentSession

    def can_assign_items(self):
        """Pass through to provider ItemBankAssignmentSession.can_assign_items"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._get_provider_session('item_bank_assignment_session').can_assign_items()

    def can_assign_items_to_bank(self, *args, **kwargs):
        """Pass through to provider ItemBankAssignmentSession.can_assign_items_to_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._get_provider_session('item_bank_assignment_session').can_assign_items_to_bank(*args, **kwargs)

    def get_assignable_bank_ids(self, *args, **kwargs):
        """Pass through to provider ItemBankAssignmentSession.get_assignable_bank_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        return self._get_provider_session('item_bank_assignment_session').get_assignable_bank_ids(*args, **kwargs)

    def get_assignable_bank_ids_for_item(self, *args, **kwargs):
        """Pass through to provider ItemBankAssignmentSession.get_assignable_bank_ids_for_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        return self._get_provider_session('item_bank_assignment_session').get_assignable_bank_ids_for_item(*args, **kwargs)

    def assign_item_to_bank(self, *args, **kwargs):
        """Pass through to provider ItemBankAssignmentSession.assign_item_to_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        self._get_provider_session('item_bank_assignment_session').assign_item_to_bank(*args, **kwargs)

    def unassign_item_from_bank(self, *args, **kwargs):
        """Pass through to provider ItemBankAssignmentSession.unassign_item_from_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        self._get_provider_session('item_bank_assignment_session').unassign_item_from_bank(*args, **kwargs)

    def reassign_item_to_billing(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


##
# The following methods are from osid.assessment.AssessmentBankSession

    def can_lookup_assessment_bank_mappings(self):
        """Pass through to provider AssessmentBankSession.can_lookup_assessment_bank_mappings"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._get_provider_session('assessment_bank_session').can_lookup_assessment_bank_mappings()

    def get_assessment_ids_by_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentBankSession.get_assessment_ids_by_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        return self._get_provider_session('assessment_bank_session').get_assessment_ids_by_bank(*args, **kwargs)

    def get_assessments_by_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentBankSession.get_assessments_by_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._get_provider_session('assessment_bank_session').get_assessments_by_bank(*args, **kwargs)

    def get_assessment_ids_by_banks(self, *args, **kwargs):
        """Pass through to provider AssessmentBankSession.get_assessment_ids_by_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        return self._get_provider_session('assessment_bank_session').get_assessment_ids_by_banks(*args, **kwargs)

    def get_assessments_by_banks(self, *args, **kwargs):
        """Pass through to provider AssessmentBankSession.get_assessments_by_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        return self._get_provider_session('assessment_bank_session').get_assessments_by_banks(*args, **kwargs)

    def get_bank_ids_by_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentBankSession.get_bank_ids_by_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        return self._get_provider_session('assessment_bank_session').get_bank_ids_by_assessment(*args, **kwargs)

    def get_banks_by_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentBankSession.get_banks_by_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        return self._get_provider_session('assessment_bank_session').get_banks_by_assessment(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentBankAssignmentSession

    def can_assign_assessments(self):
        """Pass through to provider AssessmentBankAssignmentSession.can_assign_assessments"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._get_provider_session('assessment_bank_assignment_session').can_assign_assessments()

    def can_assign_assessments_to_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentBankAssignmentSession.can_assign_assessments_to_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._get_provider_session('assessment_bank_assignment_session').can_assign_assessments_to_bank(*args, **kwargs)

    def get_assignable_bank_ids_for_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentBankAssignmentSession.get_assignable_bank_ids_for_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        return self._get_provider_session('assessment_bank_assignment_session').get_assignable_bank_ids_for_assessment(*args, **kwargs)

    def assign_assessment_to_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentBankAssignmentSession.assign_assessment_to_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        self._get_provider_session('assessment_bank_assignment_session').assign_assessment_to_bank(*args, **kwargs)

    def unassign_assessment_from_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentBankAssignmentSession.unassign_assessment_from_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        self._get_provider_session('assessment_bank_assignment_session').unassign_assessment_from_bank(*args, **kwargs)

    def reassign_assessment_to_billing(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


##
# The following methods are from osid.assessment.AssessmentOfferedBankSession

    def can_lookup_assessment_offered_bank_mappings(self):
        """Pass through to provider AssessmentOfferedBankSession.can_lookup_assessment_offered_bank_mappings"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._get_provider_session('assessment_offered_bank_session').can_lookup_assessment_offered_bank_mappings()

    def get_assessment_offered_ids_by_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankSession.get_assessment_offered_ids_by_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        return self._get_provider_session('assessment_offered_bank_session').get_assessment_offered_ids_by_bank(*args, **kwargs)

    def get_assessments_offered_by_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankSession.get_assessments_offered_by_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._get_provider_session('assessment_offered_bank_session').get_assessments_offered_by_bank(*args, **kwargs)

    def get_assessment_offered_ids_by_banks(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankSession.get_assessment_offered_ids_by_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        return self._get_provider_session('assessment_offered_bank_session').get_assessment_offered_ids_by_banks(*args, **kwargs)

    def get_assessments_offered_by_banks(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankSession.get_assessments_offered_by_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        return self._get_provider_session('assessment_offered_bank_session').get_assessments_offered_by_banks(*args, **kwargs)

    def get_bank_ids_by_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankSession.get_bank_ids_by_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        return self._get_provider_session('assessment_offered_bank_session').get_bank_ids_by_assessment_offered(*args, **kwargs)

    def get_banks_by_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankSession.get_banks_by_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        return self._get_provider_session('assessment_offered_bank_session').get_banks_by_assessment_offered(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentOfferedBankAssignmentSession

    def can_assign_assessments_offered(self):
        """Pass through to provider AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._get_provider_session('assessment_offered_bank_assignment_session').can_assign_assessments_offered()

    def can_assign_assessments_offered_to_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankAssignmentSession.can_assign_assessments_offered_to_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._get_provider_session('assessment_offered_bank_assignment_session').can_assign_assessments_offered_to_bank(*args, **kwargs)

    def get_assignable_bank_ids_for_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankAssignmentSession.get_assignable_bank_ids_for_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        return self._get_provider_session('assessment_offered_bank_assignment_session').get_assignable_bank_ids_for_assessment_offered(*args, **kwargs)

    def assign_assessment_offered_to_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankAssignmentSession.assign_assessment_offered_to_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        self._get_provider_session('assessment_offered_bank_assignment_session').assign_assessment_offered_to_bank(*args, **kwargs)

    def unassign_assessment_offered_from_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedBankAssignmentSession.unassign_assessment_offered_from_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        self._get_provider_session('assessment_offered_bank_assignment_session').unassign_assessment_offered_from_bank(*args, **kwargs)

    def reassign_assessment_offered_to_billing(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


##
# The following methods are from osid.assessment.AssessmentTakenBankSession

    def can_lookup_assessment_taken_bank_mappings(self):
        """Pass through to provider AssessmentTakenBankSession.can_lookup_assessment_taken_bank_mappings"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._get_provider_session('assessment_taken_bank_session').can_lookup_assessment_taken_bank_mappings()

    def get_assessment_taken_ids_by_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankSession.get_assessment_taken_ids_by_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        return self._get_provider_session('assessment_taken_bank_session').get_assessment_taken_ids_by_bank(*args, **kwargs)

    def get_assessments_taken_by_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankSession.get_assessments_taken_by_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin
        return self._get_provider_session('assessment_taken_bank_session').get_assessments_taken_by_bank(*args, **kwargs)

    def get_assessment_taken_ids_by_banks(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankSession.get_assessment_taken_ids_by_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        return self._get_provider_session('assessment_taken_bank_session').get_assessment_taken_ids_by_banks(*args, **kwargs)

    def get_assessments_taken_by_banks(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankSession.get_assessments_taken_by_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        return self._get_provider_session('assessment_taken_bank_session').get_assessments_taken_by_banks(*args, **kwargs)

    def get_bank_ids_by_assessment_taken(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankSession.get_bank_ids_by_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        return self._get_provider_session('assessment_taken_bank_session').get_bank_ids_by_assessment_taken(*args, **kwargs)

    def get_banks_by_assessment_taken(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankSession.get_banks_by_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        return self._get_provider_session('assessment_taken_bank_session').get_banks_by_assessment_taken(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentTakenBankAssignmentSession

    def can_assign_assessments_taken(self):
        """Pass through to provider AssessmentTakenBankAssignmentSession.can_assign_assessments_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._get_provider_session('assessment_taken_bank_assignment_session').can_assign_assessments_taken()

    def can_assign_assessments_taken_to_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankAssignmentSession.can_assign_assessments_taken_to_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._get_provider_session('assessment_taken_bank_assignment_session').can_assign_assessments_taken_to_bank(*args, **kwargs)

    def get_assignable_bank_ids_for_assessment_taken(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankAssignmentSession.get_assignable_bank_ids_for_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        return self._get_provider_session('assessment_taken_bank_assignment_session').get_assignable_bank_ids_for_assessment_taken(*args, **kwargs)

    def assign_assessment_taken_to_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankAssignmentSession.assign_assessment_taken_to_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        self._get_provider_session('assessment_taken_bank_assignment_session').assign_assessment_taken_to_bank(*args, **kwargs)

    def unassign_assessment_taken_from_bank(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenBankAssignmentSession.unassign_assessment_taken_from_bank"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceBinAssignmentSession.unassign_resource_from_bin
        self._get_provider_session('assessment_taken_bank_assignment_session').unassign_assessment_taken_from_bank(*args, **kwargs)

    def reassign_assessment_taken_to_billing(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


##
# The following methods are from osid.assessment.BankLookupSession

    def can_lookup_banks(self):
        """Pass through to provider BankLookupSession.can_lookup_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('bank_lookup_session').can_lookup_banks()

    def get_bank(self, *args, **kwargs):
        """Pass through to provider BankLookupSession.get_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bin
        return Bank(self._provider_manager, self._get_provider_session('bank_lookup_session').get_bank(*args, **kwargs), self._proxy)

    def get_banks_by_ids(self, *args, **kwargs):
        """Pass through to provider BankLookupSession.get_banks_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids
        catalogs = self._get_provider_session('bank_lookup_session').get_banks_by_ids(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bank(self._provider_manager, cat, self._proxy))
        return BankList(cat_list)

    def get_banks_by_genus_type(self, *args, **kwargs):
        """Pass through to provider BankLookupSession.get_banks_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_genus_type
        catalogs = self._get_provider_session('bank_lookup_session').get_banks_by_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bank(self._provider_manager, cat, self._proxy))
        return BankList(cat_list)

    def get_banks_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider BankLookupSession.get_banks_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_parent_genus_type
        catalogs = self._get_provider_session('bank_lookup_session').get_banks_by_parent_genus_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bank(self._provider_manager, cat, self._proxy))
        return BankList(cat_list)

    def get_banks_by_record_type(self, *args, **kwargs):
        """Pass through to provider BankLookupSession.get_banks_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_record_type
        catalogs = self._get_provider_session('bank_lookup_session').get_banks_by_record_type(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bank(self._provider_manager, cat, self._proxy))
        return BankList(cat_list)

    def get_banks_by_provider(self, *args, **kwargs):
        """Pass through to provider BankLookupSession.get_banks_by_provider"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_by_provider
        catalogs = self._get_provider_session('bank_lookup_session').get_banks_by_provider(*args, **kwargs)
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bank(self._provider_manager, cat, self._proxy))
        return BankList(cat_list)

    def get_banks(self):
        """Pass through to provider BankLookupSession.get_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        catalogs = self._get_provider_session('bank_lookup_session').get_banks()
        cat_list = []
        for cat in catalogs:
            cat_list.append(Bank(self._provider_manager, cat, self._proxy))
        return BankList(cat_list)

    banks = property(fget=get_banks)


##
# The following methods are from osid.assessment.BankQuerySession

    def can_search_banks(self):
        """Pass through to provider BankQuerySession.can_search_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('bank_query_session').can_search_banks()

    def get_bank_query(self):
        """Pass through to provider BankQuerySession.get_bank_query"""
        # Implemented from kitosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        return self._get_provider_session('bank_query_session').get_bank_query()

    bank_query = property(fget=get_bank_query)

    def get_banks_by_query(self, *args, **kwargs):
        """Pass through to provider BankQuerySession.get_banks_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        return self._get_provider_session('bank_query_session').get_banks_by_query(*args, **kwargs)


##
# The following methods are from osid.assessment.BankAdminSession

    def can_create_banks(self):
        """Pass through to provider BankAdminSession.can_create_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('bank_admin_session').can_create_banks()

    def can_create_bank_with_record_types(self, *args, **kwargs):
        """Pass through to provider BankAdminSession.can_create_bank_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('bank_admin_session').can_create_bank_with_record_types(*args, **kwargs)

    def get_bank_form_for_create(self, *args, **kwargs):
        """Pass through to provider BankAdminSession.get_bank_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create
        return self._get_provider_session('bank_admin_session').get_bank_form_for_create(*args, **kwargs)

    def create_bank(self, *args, **kwargs):
        """Pass through to provider BankAdminSession.create_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.create_bin
        return Bank(self._provider_manager, self._get_provider_session('bank_admin_session').create_bank(*args, **kwargs), self._proxy)

    def can_update_banks(self):
        """Pass through to provider BankAdminSession.can_update_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('bank_admin_session').can_update_banks()

    def get_bank_form_for_update(self, *args, **kwargs):
        """Pass through to provider BankAdminSession.get_bank_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update
        return self._get_provider_session('bank_admin_session').get_bank_form_for_update(*args, **kwargs)

    def get_bank_form(self, *args, **kwargs):
        """Pass through to provider BankAdminSession.get_bank_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'bank_record_types' in kwargs:
            return self.get_bank_form_for_create(*args, **kwargs)
        else:
            return self.get_bank_form_for_update(*args, **kwargs)

    def update_bank(self, *args, **kwargs):
        """Pass through to provider BankAdminSession.update_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        # OSID spec does not require returning updated catalog
        return Bank(self._provider_manager, self._get_provider_session('bank_admin_session').update_bank(*args, **kwargs), self._proxy)

    def save_bank(self, bank_form, *args, **kwargs):
        """Pass through to provider BankAdminSession.update_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.update_bin
        if bank_form.is_for_update():
            return self.update_bank(bank_form, *args, **kwargs)
        else:
            return self.create_bank(bank_form, *args, **kwargs)

    def can_delete_banks(self):
        """Pass through to provider BankAdminSession.can_delete_banks"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('bank_admin_session').can_delete_banks()

    def delete_bank(self, *args, **kwargs):
        """Pass through to provider BankAdminSession.delete_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinAdminSession.delete_bin
        self._get_provider_session('bank_admin_session').delete_bank(*args, **kwargs)

    def can_manage_bank_aliases(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def alias_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


##
# The following methods are from osid.assessment.BankHierarchySession

    def get_bank_hierarchy_id(self):
        """Pass through to provider BankHierarchySession.get_bank_hierarchy_id"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._get_provider_session('bank_hierarchy_session').get_bank_hierarchy_id()

    bank_hierarchy_id = property(fget=get_bank_hierarchy_id)

    def get_bank_hierarchy(self):
        """Pass through to provider BankHierarchySession.get_bank_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        return self._get_provider_session('bank_hierarchy_session').get_bank_hierarchy()

    bank_hierarchy = property(fget=get_bank_hierarchy)

    def can_access_bank_hierarchy(self):
        """Pass through to provider BankHierarchySession.can_access_bank_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._get_provider_session('bank_hierarchy_session').can_access_bank_hierarchy()

    def get_root_bank_ids(self):
        """Pass through to provider BankHierarchySession.get_root_bank_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        return self._get_provider_session('bank_hierarchy_session').get_root_bank_ids()

    root_bank_ids = property(fget=get_root_bank_ids)

    def get_root_banks(self):
        """Pass through to provider BankHierarchySession.get_root_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        return self._get_provider_session('bank_hierarchy_session').get_root_banks()

    root_banks = property(fget=get_root_banks)

    def has_parent_banks(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.has_parent_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        return self._get_provider_session('bank_hierarchy_session').has_parent_banks(*args, **kwargs)

    def is_parent_of_bank(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.is_parent_of_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        return self._get_provider_session('bank_hierarchy_session').is_parent_of_bank(*args, **kwargs)

    def get_parent_bank_ids(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.get_parent_bank_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        return self._get_provider_session('bank_hierarchy_session').get_parent_bank_ids(*args, **kwargs)

    def get_parent_banks(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.get_parent_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        return self._get_provider_session('bank_hierarchy_session').get_parent_banks(*args, **kwargs)

    def is_ancestor_of_bank(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.is_ancestor_of_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        return self._get_provider_session('bank_hierarchy_session').is_ancestor_of_bank(*args, **kwargs)

    def has_child_banks(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.has_child_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        return self._get_provider_session('bank_hierarchy_session').has_child_banks(*args, **kwargs)

    def is_child_of_bank(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.is_child_of_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        return self._get_provider_session('bank_hierarchy_session').is_child_of_bank(*args, **kwargs)

    def get_child_bank_ids(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.get_child_bank_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        return self._get_provider_session('bank_hierarchy_session').get_child_bank_ids(*args, **kwargs)

    def get_child_banks(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.get_child_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_child_bins
        return self._get_provider_session('bank_hierarchy_session').get_child_banks(*args, **kwargs)

    def is_descendant_of_bank(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.is_descendant_of_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        return self._get_provider_session('bank_hierarchy_session').is_descendant_of_bank(*args, **kwargs)

    def get_bank_node_ids(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.get_bank_node_ids"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        return self._get_provider_session('bank_hierarchy_session').get_bank_node_ids(*args, **kwargs)

    def get_bank_nodes(self, *args, **kwargs):
        """Pass through to provider BankHierarchySession.get_bank_nodes"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        return self._get_provider_session('bank_hierarchy_session').get_bank_nodes(*args, **kwargs)


##
# The following methods are from osid.assessment.BankHierarchyDesignSession

    def can_modify_bank_hierarchy(self):
        """Pass through to provider BankHierarchyDesignSession.can_modify_bank_hierarchy"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._get_provider_session('bank_hierarchy_design_session').can_modify_bank_hierarchy()

    def create_bank_hierarchy(self, *args, **kwargs):
        """Pass through to provider BankHierarchyDesignSession.can_modify_bank_hierarchy"""
        # Patched in by cjshaw@mit.edu, Jul 23, 2014, added by birdland to template on Aug 8, 2014
        # Is not part of specs for catalog hierarchy design sessions, but may want to be in hierarchy service instead
        # Will not return an actual object, just JSON
        # since a BankHierarchy does not seem to be an OSID thing.
        return self._get_provider_session('bank_hierarchy_design_session').create_bank_hierarchy(*args, **kwargs)

    def delete_bank_hierarchy(self, *args, **kwargs):
        """Pass through to provider BankHierarchyDesignSession.can_modify_bank_hierarchy"""
        # Patched in by cjshaw@mit.edu, Jul 23, 2014, added by birdland to template on Aug 8, 2014
        # Is not part of specs for catalog hierarchy design sessions, but may want to be in hierarchy service instead
        # Will not return an actual object, just JSON
        # since a BankHierarchy does not seem to be an OSID thing.
        return self._get_provider_session('bank_hierarchy_design_session').delete_bank_hierarchy(*args, **kwargs)

    def add_root_bank(self, *args, **kwargs):
        """Pass through to provider BankHierarchyDesignSession.add_root_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin
        self._get_provider_session('bank_hierarchy_design_session').add_root_bank(*args, **kwargs)

    def remove_root_bank(self, *args, **kwargs):
        """Pass through to provider BankHierarchyDesignSession.remove_root_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_root_bin
        self._get_provider_session('bank_hierarchy_design_session').remove_root_bank(*args, **kwargs)

    def add_child_bank(self, *args, **kwargs):
        """Pass through to provider BankHierarchyDesignSession.add_child_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.add_child_bin
        self._get_provider_session('bank_hierarchy_design_session').add_child_bank(*args, **kwargs)

    def remove_child_bank(self, *args, **kwargs):
        """Pass through to provider BankHierarchyDesignSession.remove_child_bank"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_child_bin
        self._get_provider_session('bank_hierarchy_design_session').remove_child_bank(*args, **kwargs)

    def remove_child_banks(self, *args, **kwargs):
        """Pass through to provider BankHierarchyDesignSession.remove_child_banks"""
        # Implemented from kitosid template for -
        # osid.resource.BinHierarchyDesignSession.remove_child_bins
        self._get_provider_session('bank_hierarchy_design_session').remove_child_banks(*args, **kwargs)




class AssessmentProxyManager(osid.OsidProxyManager, AssessmentProfile, assessment_managers.AssessmentProxyManager):
    """AssessmentProxyManager convenience adapter including related Session methods."""

    def get_assessment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_session_for_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_item_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AssessmentManager.get_item_lookup_session(*args, **kwargs)

    def get_item_lookup_session_for_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AssessmentManager.get_item_lookup_session_for_bank(*args, **kwargs)

    def get_item_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AssessmentManager.get_item_query_session(*args, **kwargs)

    def get_item_query_session_for_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AssessmentManager.get_item_query_session_for_bank(*args, **kwargs)

    def get_item_search_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_item_search_session_for_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_item_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_item_admin_session_for_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_item_notification_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_item_bank_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_item_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AssessmentManager.get_assessment_lookup_session(*args, **kwargs)

    def get_assessment_lookup_session_for_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AssessmentManager.get_assessment_lookup_session_for_bank(*args, **kwargs)

    def get_assessment_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AssessmentManager.get_assessment_query_session(*args, **kwargs)

    def get_assessment_query_session_for_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AssessmentManager.get_assessment_query_session_for_bank(*args, **kwargs)

    def get_assessment_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_admin_session_for_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_bank_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_basic_authoring_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_basic_authoring_session_for_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_offered_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AssessmentManager.get_assessment_offered_lookup_session(*args, **kwargs)

    def get_assessment_offered_lookup_session_for_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AssessmentManager.get_assessment_offered_lookup_session_for_bank(*args, **kwargs)

    def get_assessment_offered_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AssessmentManager.get_assessment_offered_query_session(*args, **kwargs)

    def get_assessment_offered_query_session_for_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AssessmentManager.get_assessment_offered_query_session_for_bank(*args, **kwargs)

    def get_assessment_offered_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_offered_admin_session_for_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_offered_bank_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_offered_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_taken_lookup_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AssessmentManager.get_assessment_taken_lookup_session(*args, **kwargs)

    def get_assessment_taken_lookup_session_for_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AssessmentManager.get_assessment_taken_lookup_session_for_bank(*args, **kwargs)

    def get_assessment_taken_query_session(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_template
        return AssessmentManager.get_assessment_taken_query_session(*args, **kwargs)

    def get_assessment_taken_query_session_for_bank(self, *args, **kwargs):
        """Sends control to Manager"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceProxyManager.get_resource_lookup_session_for_bin_template
        return AssessmentManager.get_assessment_taken_query_session_for_bank(*args, **kwargs)

    def get_assessment_taken_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_taken_admin_session_for_bank(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_taken_bank_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_taken_bank_assignment_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bank_lookup_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bank_query_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bank_admin_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bank_hierarchy_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_bank_hierarchy_design_session(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessment_authoring_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    assessment_authoring_proxy_manager = property(fget=get_assessment_authoring_proxy_manager)

    def get_assessment_batch_proxy_manager(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    assessment_batch_proxy_manager = property(fget=get_assessment_batch_proxy_manager)


class Bank(abc_assessment_objects.Bank, osid.OsidSession, osid.OsidCatalog):
    """Bank convenience adapter including related Session methods."""


    # WILL THIS EVER BE CALLED DIRECTLY - OUTSIDE OF A MANAGER?
    def __init__(self, provider_manager, catalog, proxy, **kwargs):
        self._provider_manager = provider_manager
        self._catalog = catalog
        osid.OsidObject.__init__(self, self._catalog) # This is to initialize self._object
        osid.OsidSession.__init__(self, proxy) # This is to initialize self._proxy
        self._catalog_id = catalog.get_id()
        self._provider_sessions = kwargs
        self._session_management = AUTOMATIC
        self._bank_view = DEFAULT
        self._object_views = dict()


    def _set_bank_view(self, session):
        """Sets the underlying bank view to match current view"""
        if self._bank_view == FEDERATED:
            try:
                session.use_federated_bank_view()
            except AttributeError:
                pass
        else:
            try:
                session.use_isolated_bank_view()
            except AttributeError:
                pass


    def _set_object_view(self, session):
        """Sets the underlying object views to match current view"""
        for obj_name in self._object_views:
            if self._object_views[obj_name] == PLENARY:
                try:
                    getattr(session, 'use_plenary_' + obj_name + '_view')()
                except AttributeError:
                    pass
            else:
                try:
                    getattr(session, 'use_comparative_' + obj_name + '_view')()
                except AttributeError:
                    pass


    def _get_provider_session(self, session_name):
        """Returns the requested provider session."""
        if session_name in self._provider_sessions:
            return self._provider_sessions[session_name]
        else:
            session_class = getattr(self._provider_manager, 'get_' + session_name + '_for_bank')
            if self._proxy is None:
                session = session_class(self._catalog.get_id())
            else:
                session = session_class(self._catalog.get_id(), self._proxy)
            self._set_bank_view(session)
            self._set_object_view(session)
            if self._session_management != DISABLED:
                self._provider_sessions[session_name] = session
            return session


    def get_bank_id(self):
        """Gets the Id of this bank."""
        return self._catalog_id


    def get_bank(self):
        """Strange little method to assure conformance for inherited Sessions."""
        return self


    def get_objective_hierarchy_id(self):
        """WHAT am I doing here?"""
        return self._catalog_id


    def get_objective_hierarchy(self):
        """WHAT am I doing here?"""
        return self


    def __getattr__(self, name):
        if '_catalog' in self.__dict__:
            try:
                return self._catalog[name]
            except AttributeError:
                pass
        raise AttributeError


    def close_sessions(self):
        """Close all sessions currently being managed by this Manager to save memory."""
        if self._session_management != MANDATORY:
            self._provider_sessions = dict()
        raise IllegalState()


    def use_automatic_session_management(self):
        """Session state will be saved until closed by consumers."""
        self._session_management = AUTOMATIC


    def use_mandatory_session_management(self):
        """Session state will always be saved and can not be closed by consumers."""
        # Session state will be saved and can not be closed by consumers
        self._session_management = MANDATORY


    def disable_session_management(self):
        """Session state will never be saved."""
        self._session_management = DISABLED
        self.close_sessions()
    def get_bank_record(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))
##
# The following methods are from osid.assessment.AssessmentSession

    def can_take_assessments(self):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').can_take_assessments()

    def has_assessment_begun(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_assessment_begun(*args, **kwargs)

    def is_assessment_over(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').is_assessment_over(*args, **kwargs)

    def requires_synchronous_sections(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').requires_synchronous_sections(*args, **kwargs)

    def get_first_assessment_section(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_first_assessment_section(*args, **kwargs)

    def has_next_assessment_section(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_next_assessment_section(*args, **kwargs)

    def get_next_assessment_section(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_next_assessment_section(*args, **kwargs)

    def has_previous_assessment_section(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_previous_assessment_section(*args, **kwargs)

    def get_previous_assessment_section(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_previous_assessment_section(*args, **kwargs)

    def get_assessment_section(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_assessment_section(*args, **kwargs)

    def get_assessment_sections(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_assessment_sections(*args, **kwargs)

    def is_assessment_section_complete(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').is_assessment_section_complete(*args, **kwargs)

    def get_incomplete_assessment_sections(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_incomplete_assessment_sections(*args, **kwargs)

    def has_assessment_section_begun(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_assessment_section_begun(*args, **kwargs)

    def is_assessment_section_over(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').is_assessment_section_over(*args, **kwargs)

    def requires_synchronous_responses(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').requires_synchronous_responses(*args, **kwargs)

    def get_first_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_first_question(*args, **kwargs)

    def has_next_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_next_question(*args, **kwargs)

    def get_next_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_next_question(*args, **kwargs)

    def has_previous_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_previous_question(*args, **kwargs)

    def get_previous_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_previous_question(*args, **kwargs)

    def get_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_question(*args, **kwargs)

    def get_questions(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_questions(*args, **kwargs)

    def get_response_form(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_response_form(*args, **kwargs)

    def submit_response(self, *args, **kwargs):
        """Pass through to provider method"""
        self._get_provider_session('assessment_session').submit_response(*args, **kwargs)

    def skip_item(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').skip_item(*args, **kwargs)

    def is_question_answered(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').is_question_answered(*args, **kwargs)

    def get_unanswered_questions(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_unanswered_questions(*args, **kwargs)

    def has_unanswered_questions(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_unanswered_questions(*args, **kwargs)

    def get_first_unanswered_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_first_unanswered_question(*args, **kwargs)

    def has_next_unanswered_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_next_unanswered_question(*args, **kwargs)

    def get_next_unanswered_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_next_unanswered_question(*args, **kwargs)

    def has_previous_unanswered_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').has_previous_unanswered_question(*args, **kwargs)

    def get_previous_unanswered_question(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_previous_unanswered_question(*args, **kwargs)

    def get_response(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_response(*args, **kwargs)

    def get_responses(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_responses(*args, **kwargs)

    def clear_response(self, *args, **kwargs):
        """Pass through to provider method"""
        self._get_provider_session('assessment_session').clear_response(*args, **kwargs)

    def finish_assessment_section(self, *args, **kwargs):
        """Pass through to provider method"""
        self._get_provider_session('assessment_session').finish_assessment_section(*args, **kwargs)

    def is_answer_available(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').is_answer_available(*args, **kwargs)

    def get_answers(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_session').get_answers(*args, **kwargs)

    def finish_assessment(self, *args, **kwargs):
        """Pass through to provider method"""
        self._get_provider_session('assessment_session').finish_assessment(*args, **kwargs)


##
# The following methods are from osid.assessment.ItemLookupSession

    def can_lookup_items(self):
        """Pass through to provider ItemLookupSession.can_lookup_items"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('item_lookup_session').can_lookup_items()

    def use_comparative_item_view(self):
        """Pass through to provider ItemLookupSession.use_comparative_item_view"""
        self._object_views['item'] = COMPARATIVE
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_comparative_item_view()
            except AttributeError:
                pass

    def use_plenary_item_view(self):
        """Pass through to provider ItemLookupSession.use_plenary_item_view"""
        self._object_views['item'] = PLENARY
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_plenary_item_view()
            except AttributeError:
                pass

    def use_federated_bank_view(self):
        """Pass through to provider ItemLookupSession.use_federated_bank_view"""
        self._bank_view = FEDERATED
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_federated_bank_view()
            except AttributeError:
                pass

    def use_isolated_bank_view(self):
        """Pass through to provider ItemLookupSession.use_isolated_bank_view"""
        self._bank_view = ISOLATED
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_isolated_bank_view()
            except AttributeError:
                pass

    def get_item(self, *args, **kwargs):
        """Pass through to provider ItemLookupSession.get_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('item_lookup_session').get_item(*args, **kwargs)

    def get_items_by_ids(self, *args, **kwargs):
        """Pass through to provider ItemLookupSession.get_items_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('item_lookup_session').get_items_by_ids(*args, **kwargs)

    def get_items_by_genus_type(self, *args, **kwargs):
        """Pass through to provider ItemLookupSession.get_items_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('item_lookup_session').get_items_by_genus_type(*args, **kwargs)

    def get_items_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider ItemLookupSession.get_items_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('item_lookup_session').get_items_by_parent_genus_type(*args, **kwargs)

    def get_items_by_record_type(self, *args, **kwargs):
        """Pass through to provider ItemLookupSession.get_items_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('item_lookup_session').get_items_by_record_type(*args, **kwargs)

    def get_items_by_question(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_items_by_answer(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_items_by_learning_objective(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_items_by_learning_objectives(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_items(self):
        """Pass through to provider ItemLookupSession.get_items"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('item_lookup_session').get_items()

    items = property(fget=get_items)


##
# The following methods are from osid.assessment.ItemQuerySession

    def can_search_items(self):
        """Pass through to provider ItemQuerySession.can_search_items"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('item_query_session').can_search_items()

    def get_item_query(self):
        """Pass through to provider ItemQuerySession.get_item_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('item_query_session').get_item_query()

    item_query = property(fget=get_item_query)

    def get_items_by_query(self, *args, **kwargs):
        """Pass through to provider ItemQuerySession.get_items_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('item_query_session').get_items_by_query(*args, **kwargs)


##
# The following methods are from osid.assessment.ItemSearchSession

    def get_item_search(self):
        """Pass through to provider ItemSearchSession.get_item_search"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        return self._get_provider_session('item_search_session').get_item_search()

    item_search = property(fget=get_item_search)

    def get_item_search_order(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    item_search_order = property(fget=get_item_search_order)

    def get_items_by_search(self, *args, **kwargs):
        """Pass through to provider ItemSearchSession.get_items_by_search"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        return self._get_provider_session('item_search_session').get_items_by_search(*args, **kwargs)

    def get_item_query_from_inspector(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))


##
# The following methods are from osid.assessment.ItemAdminSession

    def can_create_items(self):
        """Pass through to provider ItemAdminSession.can_create_items"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_create_items()

    def can_create_item_with_record_types(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.can_create_item_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('item_admin_session').can_create_item_with_record_types(*args, **kwargs)

    def get_item_form_for_create(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.get_item_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        return self._get_provider_session('item_admin_session').get_item_form_for_create(*args, **kwargs)

    def create_item(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.create_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('item_admin_session').create_item(*args, **kwargs)

    def can_update_items(self):
        """Pass through to provider ItemAdminSession.can_update_items"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_update_items()

    def get_item_form_for_update(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.get_item_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('item_admin_session').get_item_form_for_update(*args, **kwargs)

    def get_item_form(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.get_item_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'item_record_types' in kwargs:
            return self.get_item_form_for_create(*args, **kwargs)
        else:
            return self.get_item_form_for_update(*args, **kwargs)

    def duplicate_item(self, item_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('item_admin_session').duplicate_item(item_id)

    def update_item(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.update_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('item_admin_session').update_item(*args, **kwargs)

    def save_item(self, item_form, *args, **kwargs):
        """Pass through to provider ItemAdminSession.update_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if item_form.is_for_update():
            return self.update_item(item_form, *args, **kwargs)
        else:
            return self.create_item(item_form, *args, **kwargs)

    def can_delete_items(self):
        """Pass through to provider ItemAdminSession.can_delete_items"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_delete_items()

    def delete_item(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.delete_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('item_admin_session').delete_item(*args, **kwargs)

    def can_manage_item_aliases(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def alias_item(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.alias_item"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('item_admin_session').alias_item(*args, **kwargs)

    def can_create_questions(self):
        """Pass through to provider ItemAdminSession.can_create_questions"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_create_questions()

    def can_create_question_with_record_types(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.can_create_question_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('item_admin_session').can_create_question_with_record_types(*args, **kwargs)

    def get_question_form_for_create(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.get_question_form_for_create"""
        # Implemented from -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        return self._get_provider_session('item_admin_session').get_question_form_for_create(*args, **kwargs)

    def create_question(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.create_question"""
        # Implemented from -
        # osid.repository.AssetAdminSession.create_asset_content_template
        return self._get_provider_session('item_admin_session').create_question(*args, **kwargs)

    def can_update_questions(self):
        """Pass through to provider ItemAdminSession.can_update_questions"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_update_questions()

    def get_question_form_for_update(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.get_question_form_for_update"""
        # Implemented from -
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        return self._get_provider_session('item_admin_session').get_question_form_for_update(*args, **kwargs)

    def update_question(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.update_question"""
        # Implemented from -
        # osid.repository.AssetAdminSession.update_asset_template
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('item_admin_session').update_question(*args, **kwargs)

    def can_delete_questions(self):
        """Pass through to provider ItemAdminSession.can_delete_questions"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_delete_questions()

    def delete_question(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.delete_question"""
        # Implemented from -
        # osid.repository.AssetAdminSession.delete_asset_content_template
        # Note: The OSID spec does not require returning updated object
        self._get_provider_session('item_admin_session').delete_question(*args, **kwargs)

    def can_create_answers(self):
        """Pass through to provider ItemAdminSession.can_create_answers"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_create_answers()

    def can_create_answers_with_record_types(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.can_create_answers_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('item_admin_session').can_create_answers_with_record_types(*args, **kwargs)

    def get_answer_form_for_create(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.get_answer_form_for_create"""
        # Implemented from -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        return self._get_provider_session('item_admin_session').get_answer_form_for_create(*args, **kwargs)

    def create_answer(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.create_answer"""
        # Implemented from -
        # osid.repository.AssetAdminSession.create_asset_content_template
        return self._get_provider_session('item_admin_session').create_answer(*args, **kwargs)

    def can_update_answers(self):
        """Pass through to provider ItemAdminSession.can_update_answers"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_update_answers()

    def get_answer_form_for_update(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.get_answer_form_for_update"""
        # Implemented from -
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        return self._get_provider_session('item_admin_session').get_answer_form_for_update(*args, **kwargs)

    def update_answer(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.update_answer"""
        # Implemented from -
        # osid.repository.AssetAdminSession.update_asset_template
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('item_admin_session').update_answer(*args, **kwargs)

    def can_delete_answers(self):
        """Pass through to provider ItemAdminSession.can_delete_answers"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('item_admin_session').can_delete_answers()

    def delete_answer(self, *args, **kwargs):
        """Pass through to provider ItemAdminSession.delete_answer"""
        # Implemented from -
        # osid.repository.AssetAdminSession.delete_asset_content_template
        # Note: The OSID spec does not require returning updated object
        self._get_provider_session('item_admin_session').delete_answer(*args, **kwargs)


##
# The following methods are from osid.assessment.ItemNotificationSession

    def can_register_for_item_notifications(self):
        """Pass through to provider ItemNotificationSession.can_register_for_item_notifications"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._get_provider_session('item_notification_session').can_register_for_item_notifications()

    def reliable_item_notifications(self):
        """Pass through to provider ItemNotificationSession.reliable_item_notifications"""
        self._get_provider_session('item_notification_session').reliable_item_notifications()

    def unreliable_item_notifications(self):
        """Pass through to provider ItemNotificationSession.unreliable_item_notifications"""
        self._get_provider_session('item_notification_session').unreliable_item_notifications()

    def acknowledge_item_notification(self, *args, **kwargs):
        """Pass through to provider ItemNotificationSession.acknowledge_item_notification"""
        self._get_provider_session('item_notification_session').acknowledge_item_notification(*args, **kwargs)

    def register_for_new_items(self):
        """Pass through to provider ItemNotificationSession.register_for_new_items"""
        self._get_provider_session('item_notification_session').register_for_new_items()

    def register_for_changed_items(self):
        """Pass through to provider ItemNotificationSession.register_for_changed_items"""
        self._get_provider_session('item_notification_session').register_for_changed_items()

    def register_for_changed_item(self, *args, **kwargs):
        """Pass through to provider ItemNotificationSession.register_for_changed_item"""
        self._get_provider_session('item_notification_session').register_for_changed_item(*args, **kwargs)

    def register_for_deleted_items(self):
        """Pass through to provider ItemNotificationSession.register_for_deleted_items"""
        self._get_provider_session('item_notification_session').register_for_deleted_items()

    def register_for_deleted_item(self, *args, **kwargs):
        """Pass through to provider ItemNotificationSession.register_for_deleted_item"""
        self._get_provider_session('item_notification_session').register_for_deleted_item(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentLookupSession

    def can_lookup_assessments(self):
        """Pass through to provider AssessmentLookupSession.can_lookup_assessments"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('assessment_lookup_session').can_lookup_assessments()

    def use_comparative_assessment_view(self):
        """Pass through to provider AssessmentLookupSession.use_comparative_assessment_view"""
        self._object_views['assessment'] = COMPARATIVE
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_comparative_assessment_view()
            except AttributeError:
                pass

    def use_plenary_assessment_view(self):
        """Pass through to provider AssessmentLookupSession.use_plenary_assessment_view"""
        self._object_views['assessment'] = PLENARY
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_plenary_assessment_view()
            except AttributeError:
                pass

    def get_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentLookupSession.get_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('assessment_lookup_session').get_assessment(*args, **kwargs)

    def get_assessments_by_ids(self, *args, **kwargs):
        """Pass through to provider AssessmentLookupSession.get_assessments_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('assessment_lookup_session').get_assessments_by_ids(*args, **kwargs)

    def get_assessments_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AssessmentLookupSession.get_assessments_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('assessment_lookup_session').get_assessments_by_genus_type(*args, **kwargs)

    def get_assessments_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider AssessmentLookupSession.get_assessments_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('assessment_lookup_session').get_assessments_by_parent_genus_type(*args, **kwargs)

    def get_assessments_by_record_type(self, *args, **kwargs):
        """Pass through to provider AssessmentLookupSession.get_assessments_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('assessment_lookup_session').get_assessments_by_record_type(*args, **kwargs)

    def get_assessments(self):
        """Pass through to provider AssessmentLookupSession.get_assessments"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('assessment_lookup_session').get_assessments()

    assessments = property(fget=get_assessments)


##
# The following methods are from osid.assessment.AssessmentQuerySession

    def can_search_assessments(self):
        """Pass through to provider AssessmentQuerySession.can_search_assessments"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('assessment_query_session').can_search_assessments()

    def get_assessment_query(self):
        """Pass through to provider AssessmentQuerySession.get_assessment_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('assessment_query_session').get_assessment_query()

    assessment_query = property(fget=get_assessment_query)

    def get_assessments_by_query(self, *args, **kwargs):
        """Pass through to provider AssessmentQuerySession.get_assessments_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('assessment_query_session').get_assessments_by_query(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentAdminSession

    def can_create_assessments(self):
        """Pass through to provider AssessmentAdminSession.can_create_assessments"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_admin_session').can_create_assessments()

    def can_create_assessment_with_record_types(self, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.can_create_assessment_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('assessment_admin_session').can_create_assessment_with_record_types(*args, **kwargs)

    def get_assessment_form_for_create(self, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.get_assessment_form_for_create"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        return self._get_provider_session('assessment_admin_session').get_assessment_form_for_create(*args, **kwargs)

    def create_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.create_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('assessment_admin_session').create_assessment(*args, **kwargs)

    def can_update_assessments(self):
        """Pass through to provider AssessmentAdminSession.can_update_assessments"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_admin_session').can_update_assessments()

    def get_assessment_form_for_update(self, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.get_assessment_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('assessment_admin_session').get_assessment_form_for_update(*args, **kwargs)

    def get_assessment_form(self, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.get_assessment_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'assessment_record_types' in kwargs:
            return self.get_assessment_form_for_create(*args, **kwargs)
        else:
            return self.get_assessment_form_for_update(*args, **kwargs)

    def duplicate_assessment(self, assessment_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('assessment_admin_session').duplicate_assessment(assessment_id)

    def update_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.update_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('assessment_admin_session').update_assessment(*args, **kwargs)

    def save_assessment(self, assessment_form, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.update_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if assessment_form.is_for_update():
            return self.update_assessment(assessment_form, *args, **kwargs)
        else:
            return self.create_assessment(assessment_form, *args, **kwargs)

    def can_delete_assessments(self):
        """Pass through to provider AssessmentAdminSession.can_delete_assessments"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_admin_session').can_delete_assessments()

    def delete_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.delete_assessment"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveAdminSession.delete_objective
        self._get_provider_session('assessment_admin_session').delete_assessment(*args, **kwargs)

    def can_manage_assessment_aliases(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def alias_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentAdminSession.alias_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('assessment_admin_session').alias_assessment(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentBasicAuthoringSession

    def can_author_assessments(self):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_basic_authoring_session').can_author_assessments()

    def get_assessment_items(self, *args, **kwargs):
        """Pass through to provider method"""
        # Note: this method is differenct from the underlying signature
        return self._get_provider_session('assessment_basic_authoring_session').get_items(*args, **kwargs)

    def add_item(self, *args, **kwargs):
        """Pass through to provider method"""
        self._get_provider_session('assessment_basic_authoring_session').add_item(*args, **kwargs)

    def remove_item(self, *args, **kwargs):
        """Pass through to provider method"""
        self._get_provider_session('assessment_basic_authoring_session').remove_item(*args, **kwargs)

    def move_item(self, *args, **kwargs):
        """Pass through to provider method"""
        self._get_provider_session('assessment_basic_authoring_session').move_item(*args, **kwargs)

    def order_items(self, *args, **kwargs):
        """Pass through to provider method"""
        self._get_provider_session('assessment_basic_authoring_session').order_items(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentOfferedLookupSession

    def can_lookup_assessments_offered(self):
        """Pass through to provider AssessmentOfferedLookupSession.can_lookup_assessments_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('assessment_offered_lookup_session').can_lookup_assessments_offered()

    def use_comparative_assessment_offered_view(self):
        """Pass through to provider AssessmentOfferedLookupSession.use_comparative_assessment_offered_view"""
        self._object_views['assessment_offered'] = COMPARATIVE
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_comparative_assessment_offered_view()
            except AttributeError:
                pass

    def use_plenary_assessment_offered_view(self):
        """Pass through to provider AssessmentOfferedLookupSession.use_plenary_assessment_offered_view"""
        self._object_views['assessment_offered'] = PLENARY
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_plenary_assessment_offered_view()
            except AttributeError:
                pass

    def get_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedLookupSession.get_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('assessment_offered_lookup_session').get_assessment_offered(*args, **kwargs)

    def get_assessments_offered_by_ids(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedLookupSession.get_assessments_offered_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('assessment_offered_lookup_session').get_assessments_offered_by_ids(*args, **kwargs)

    def get_assessments_offered_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedLookupSession.get_assessments_offered_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('assessment_offered_lookup_session').get_assessments_offered_by_genus_type(*args, **kwargs)

    def get_assessments_offered_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedLookupSession.get_assessments_offered_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('assessment_offered_lookup_session').get_assessments_offered_by_parent_genus_type(*args, **kwargs)

    def get_assessments_offered_by_record_type(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedLookupSession.get_assessments_offered_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('assessment_offered_lookup_session').get_assessments_offered_by_record_type(*args, **kwargs)

    def get_assessments_offered_by_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_offered_for_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedLookupSession.get_assessments_offered_for_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ActivityLookupSession.get_activities_for_objective
        return self._get_provider_session('assessment_offered_lookup_session').get_assessments_offered_for_assessment(*args, **kwargs)

    def get_assessments_offered(self):
        """Pass through to provider AssessmentOfferedLookupSession.get_assessments_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('assessment_offered_lookup_session').get_assessments_offered()

    assessments_offered = property(fget=get_assessments_offered)


##
# The following methods are from osid.assessment.AssessmentOfferedQuerySession

    def can_search_assessments_offered(self):
        """Pass through to provider AssessmentOfferedQuerySession.can_search_assessments_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('assessment_offered_query_session').can_search_assessments_offered()

    def get_assessment_offered_query(self):
        """Pass through to provider AssessmentOfferedQuerySession.get_assessment_offered_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('assessment_offered_query_session').get_assessment_offered_query()

    assessment_offered_query = property(fget=get_assessment_offered_query)

    def get_assessments_offered_by_query(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedQuerySession.get_assessments_offered_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('assessment_offered_query_session').get_assessments_offered_by_query(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentOfferedAdminSession

    def can_create_assessments_offered(self):
        """Pass through to provider AssessmentOfferedAdminSession.can_create_assessments_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_offered_admin_session').can_create_assessments_offered()

    def can_create_assessment_offered_with_record_types(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.can_create_assessment_offered_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('assessment_offered_admin_session').can_create_assessment_offered_with_record_types(*args, **kwargs)

    def get_assessment_offered_form_for_create(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.get_assessment_offered_form_for_create"""
        # Implemented from -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        return self._get_provider_session('assessment_offered_admin_session').get_assessment_offered_form_for_create(*args, **kwargs)

    def create_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.create_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('assessment_offered_admin_session').create_assessment_offered(*args, **kwargs)

    def can_update_assessments_offered(self):
        """Pass through to provider AssessmentOfferedAdminSession.can_update_assessments_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_offered_admin_session').can_update_assessments_offered()

    def get_assessment_offered_form_for_update(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.get_assessment_offered_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('assessment_offered_admin_session').get_assessment_offered_form_for_update(*args, **kwargs)

    def get_assessment_offered_form(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.get_assessment_offered_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'assessment_offered_record_types' in kwargs:
            return self.get_assessment_offered_form_for_create(*args, **kwargs)
        else:
            return self.get_assessment_offered_form_for_update(*args, **kwargs)

    def duplicate_assessment_offered(self, assessment_offered_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('assessment_offered_admin_session').duplicate_assessment_offered(assessment_offered_id)

    def update_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.update_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('assessment_offered_admin_session').update_assessment_offered(*args, **kwargs)

    def save_assessment_offered(self, assessment_offered_form, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.update_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if assessment_offered_form.is_for_update():
            return self.update_assessment_offered(assessment_offered_form, *args, **kwargs)
        else:
            return self.create_assessment_offered(assessment_offered_form, *args, **kwargs)

    def can_delete_assessments_offered(self):
        """Pass through to provider AssessmentOfferedAdminSession.can_delete_assessments_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_offered_admin_session').can_delete_assessments_offered()

    def delete_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.delete_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.learning.ObjectiveAdminSession.delete_objective
        self._get_provider_session('assessment_offered_admin_session').delete_assessment_offered(*args, **kwargs)

    def can_manage_assessment_offered_aliases(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def alias_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentOfferedAdminSession.alias_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('assessment_offered_admin_session').alias_assessment_offered(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentTakenLookupSession

    def can_lookup_assessments_taken(self):
        """Pass through to provider AssessmentTakenLookupSession.can_lookup_assessments_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._get_provider_session('assessment_taken_lookup_session').can_lookup_assessments_taken()

    def use_comparative_assessment_taken_view(self):
        """Pass through to provider AssessmentTakenLookupSession.use_comparative_assessment_taken_view"""
        self._object_views['assessment_taken'] = COMPARATIVE
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_comparative_assessment_taken_view()
            except AttributeError:
                pass

    def use_plenary_assessment_taken_view(self):
        """Pass through to provider AssessmentTakenLookupSession.use_plenary_assessment_taken_view"""
        self._object_views['assessment_taken'] = PLENARY
        for session in self._provider_sessions:
            try:
                self._provider_sessions[session].use_plenary_assessment_taken_view()
            except AttributeError:
                pass

    def get_assessment_taken(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenLookupSession.get_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        return self._get_provider_session('assessment_taken_lookup_session').get_assessment_taken(*args, **kwargs)

    def get_assessments_taken_by_ids(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenLookupSession.get_assessments_taken_by_ids"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        return self._get_provider_session('assessment_taken_lookup_session').get_assessments_taken_by_ids(*args, **kwargs)

    def get_assessments_taken_by_genus_type(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenLookupSession.get_assessments_taken_by_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        return self._get_provider_session('assessment_taken_lookup_session').get_assessments_taken_by_genus_type(*args, **kwargs)

    def get_assessments_taken_by_parent_genus_type(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenLookupSession.get_assessments_taken_by_parent_genus_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        return self._get_provider_session('assessment_taken_lookup_session').get_assessments_taken_by_parent_genus_type(*args, **kwargs)

    def get_assessments_taken_by_record_type(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenLookupSession.get_assessments_taken_by_record_type"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        return self._get_provider_session('assessment_taken_lookup_session').get_assessments_taken_by_record_type(*args, **kwargs)

    def get_assessments_taken_by_date(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_taken_for_taker(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_taken_by_date_for_taker(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_taken_for_assessment(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenLookupSession.get_assessments_taken_for_assessment"""
        # Implemented from kitosid template for -
        # osid.resource.ActivityLookupSession.get_activities_for_objective
        return self._get_provider_session('assessment_taken_lookup_session').get_assessments_taken_for_assessment(*args, **kwargs)

    def get_assessments_taken_by_date_for_assessment(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_taken_for_taker_and_assessment(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_taken_by_date_for_taker_and_assessment(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_taken_for_assessment_offered(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenLookupSession.get_assessments_taken_for_assessment_offered"""
        # Implemented from kitosid template for -
        # osid.resource.ActivityLookupSession.get_activities_for_objective
        return self._get_provider_session('assessment_taken_lookup_session').get_assessments_taken_for_assessment_offered(*args, **kwargs)

    def get_assessments_taken_by_date_for_assessment_offered(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_taken_for_taker_and_assessment_offered(self, *args, **kwargs):
        """Pass through to provider method"""
        return self._get_provider_session('assessment_taken_lookup_session').get_assessments_taken_for_taker_and_assessment_offered(*args, **kwargs)

    def get_assessments_taken_by_date_for_taker_and_assessment_offered(self, *args, **kwargs):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services - args=' + str(args) + ', kwargs=' + str(kwargs))

    def get_assessments_taken(self):
        """Pass through to provider AssessmentTakenLookupSession.get_assessments_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        return self._get_provider_session('assessment_taken_lookup_session').get_assessments_taken()

    assessments_taken = property(fget=get_assessments_taken)


##
# The following methods are from osid.assessment.AssessmentTakenQuerySession

    def can_search_assessments_taken(self):
        """Pass through to provider AssessmentTakenQuerySession.can_search_assessments_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._get_provider_session('assessment_taken_query_session').can_search_assessments_taken()

    def get_assessment_taken_query(self):
        """Pass through to provider AssessmentTakenQuerySession.get_assessment_taken_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_item_query_template
        return self._get_provider_session('assessment_taken_query_session').get_assessment_taken_query()

    assessment_taken_query = property(fget=get_assessment_taken_query)

    def get_assessments_taken_by_query(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenQuerySession.get_assessments_taken_by_query"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceQuerySession.get_items_by_query_template
        return self._get_provider_session('assessment_taken_query_session').get_assessments_taken_by_query(*args, **kwargs)


##
# The following methods are from osid.assessment.AssessmentTakenAdminSession

    def can_create_assessments_taken(self):
        """Pass through to provider AssessmentTakenAdminSession.can_create_assessments_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_taken_admin_session').can_create_assessments_taken()

    def can_create_assessment_taken_with_record_types(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.can_create_assessment_taken_with_record_types"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        return self._get_provider_session('assessment_taken_admin_session').can_create_assessment_taken_with_record_types(*args, **kwargs)

    def get_assessment_taken_form_for_create(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.get_assessment_taken_form_for_create"""
        # Implemented from -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        return self._get_provider_session('assessment_taken_admin_session').get_assessment_taken_form_for_create(*args, **kwargs)

    def create_assessment_taken(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.create_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        return self._get_provider_session('assessment_taken_admin_session').create_assessment_taken(*args, **kwargs)

    def can_update_assessments_taken(self):
        """Pass through to provider AssessmentTakenAdminSession.can_update_assessments_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_taken_admin_session').can_update_assessments_taken()

    def get_assessment_taken_form_for_update(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.get_assessment_taken_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('assessment_taken_admin_session').get_assessment_taken_form_for_update(*args, **kwargs)

    def get_assessment_taken_form(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.get_assessment_taken_form_for_update"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        # This method might be a bit sketchy. Time will tell.
        if isinstance(args[-1], list) or 'assessment_taken_record_types' in kwargs:
            return self.get_assessment_taken_form_for_create(*args, **kwargs)
        else:
            return self.get_assessment_taken_form_for_update(*args, **kwargs)

    def duplicate_assessment_taken(self, assessment_taken_id):
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        return self._get_provider_session('assessment_taken_admin_session').duplicate_assessment_taken(assessment_taken_id)

    def update_assessment_taken(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.update_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        # Note: The OSID spec does not require returning updated object
        return self._get_provider_session('assessment_taken_admin_session').update_assessment_taken(*args, **kwargs)

    def save_assessment_taken(self, assessment_taken_form, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.update_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if assessment_taken_form.is_for_update():
            return self.update_assessment_taken(assessment_taken_form, *args, **kwargs)
        else:
            return self.create_assessment_taken(assessment_taken_form, *args, **kwargs)

    def can_delete_assessments_taken(self):
        """Pass through to provider AssessmentTakenAdminSession.can_delete_assessments_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._get_provider_session('assessment_taken_admin_session').can_delete_assessments_taken()

    def delete_assessment_taken(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.delete_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        self._get_provider_session('assessment_taken_admin_session').delete_assessment_taken(*args, **kwargs)

    def can_manage_assessment_taken_aliases(self):
        """Pass through to provider unimplemented"""
        raise Unimplemented('Unimplemented in dlkit.services')

    def alias_assessment_taken(self, *args, **kwargs):
        """Pass through to provider AssessmentTakenAdminSession.alias_assessment_taken"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        self._get_provider_session('assessment_taken_admin_session').alias_assessment_taken(*args, **kwargs)




class BankList(abc_assessment_objects.BankList, osid.OsidList):
    """BankList convenience adapter including related Session methods."""

    def get_next_bank(self):
        """Gets next object"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resource
        try:
            next_item = self.next()
        except StopIteration:
            raise IllegalState('no more elements available in this list')
        else:
            return next_item

    def next(self):
        """next method for enumerator"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resource
        next_item = osid.OsidList.next(self)
        return next_item

    next_bank = property(fget=get_next_bank)

    def get_next_banks(self, n):
        """gets next n objects from list"""
        # Implemented from kitosid template for -
        # osid.resource.ResourceList.get_next_resources
        if n > self.available():
            # !!! This is not quite as specified (see method docs) !!!
            raise IllegalState('not enough elements available in this list')
        else:
            next_list = []
            i = 0
            while i < n:
                try:
                    next_list.append(self.next())
                except StopIteration:
                    break
                i += 1
            return next_list


