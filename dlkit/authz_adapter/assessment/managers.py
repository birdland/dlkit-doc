"""AuthZ Adapter implementations of assessment managers."""
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
from dlkit.manager_impls.assessment import managers as assessment_managers




class AssessmentProfile(osid_managers.OsidProfile, assessment_managers.AssessmentProfile):
    """Adapts underlying AssessmentProfile methodswith authorization checks."""


    def __init__(self, interface_name):
        osid_managers.OsidProfile.__init__(self)


    def _get_hierarchy_session(self):
        try:
            return self._provider_manager.get_bank_hierarchy_session(
                Id(authority='ASSESSMENT',
                   namespace='CATALOG',
                   identifier='BANK'))
        except Unsupported:
            return None


    def supports_assessment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment()

    def supports_item_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_lookup()

    def supports_item_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_query()

    def supports_item_search(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_search()

    def supports_item_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_admin()

    def supports_item_notification(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_notification()

    def supports_item_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_bank()

    def supports_item_bank_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_item_bank_assignment()

    def supports_assessment_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_lookup()

    def supports_assessment_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_query()

    def supports_assessment_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_admin()

    def supports_assessment_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_bank()

    def supports_assessment_bank_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_bank_assignment()

    def supports_assessment_basic_authoring(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_basic_authoring()

    def supports_assessment_offered_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_lookup()

    def supports_assessment_offered_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_query()

    def supports_assessment_offered_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_admin()

    def supports_assessment_offered_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_bank()

    def supports_assessment_offered_bank_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_offered_bank_assignment()

    def supports_assessment_taken_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_lookup()

    def supports_assessment_taken_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_query()

    def supports_assessment_taken_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_admin()

    def supports_assessment_taken_bank(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_bank()

    def supports_assessment_taken_bank_assignment(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_assessment_taken_bank_assignment()

    def supports_bank_lookup(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_lookup()

    def supports_bank_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_query()

    def supports_bank_admin(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_admin()

    def supports_bank_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_hierarchy()

    def supports_bank_hierarchy_design(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.supports_resource_lookup
        return self._provider_manager.supports_bank_hierarchy_design()

    def get_item_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_item_record_types()

    item_record_types = property(fget=get_item_record_types)

    def get_item_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_item_search_record_types()

    item_search_record_types = property(fget=get_item_search_record_types)

    def get_assessment_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_record_types()

    assessment_record_types = property(fget=get_assessment_record_types)

    def get_assessment_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_search_record_types()

    assessment_search_record_types = property(fget=get_assessment_search_record_types)

    def get_assessment_offered_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_offered_record_types()

    assessment_offered_record_types = property(fget=get_assessment_offered_record_types)

    def get_assessment_offered_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_offered_search_record_types()

    assessment_offered_search_record_types = property(fget=get_assessment_offered_search_record_types)

    def get_assessment_taken_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_taken_record_types()

    assessment_taken_record_types = property(fget=get_assessment_taken_record_types)

    def get_assessment_taken_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_taken_search_record_types()

    assessment_taken_search_record_types = property(fget=get_assessment_taken_search_record_types)

    def get_assessment_section_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_assessment_section_record_types()

    assessment_section_record_types = property(fget=get_assessment_section_record_types)

    def get_bank_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_bank_record_types()

    bank_record_types = property(fget=get_bank_record_types)

    def get_bank_search_record_types(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceProfile.get_resource_record_types
        return self._provider_manager.get_bank_search_record_types()

    bank_search_record_types = property(fget=get_bank_search_record_types)


class AssessmentManager(osid_managers.OsidManager, AssessmentProfile, assessment_managers.AssessmentManager):
    """Adapts underlying AssessmentManager methodswith authorization checks."""


    def __init__(self):
        AssessmentProfile.__init__(self)


    def initialize(self, runtime):
        osid_managers.OsidManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:assessmentProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_manager('ASSESSMENT', provider_impl) # need to add version argument


    def get_assessment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentSession')(
                self._provider_manager.get_assessment_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_session = property(fget=get_assessment_session)

    def get_assessment_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentSession')(
                self._provider_manager.get_assessment_session_for_bank(bank_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_item_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_item_query_session()
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ItemLookupSession')(
                self._provider_manager.get_item_lookup_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    item_lookup_session = property(fget=get_item_lookup_session)

    def get_item_lookup_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_item_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ItemLookupSession')(
                self._provider_manager.get_item_lookup_session_for_bank(bank_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_item_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_item_query_session()
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ItemQuerySession')(
                self._provider_manager.get_item_query_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    item_query_session = property(fget=get_item_query_session)

    def get_item_query_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_item_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ItemQuerySession')(
                self._provider_manager.get_item_query_session_for_bank(bank_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_item_search_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ItemSearchSession')(
                self._provider_manager.get_item_search_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    item_search_session = property(fget=get_item_search_session)

    def get_item_search_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ItemSearchSession')(
                self._provider_manager.get_item_search_session_for_bank(bank_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_item_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ItemAdminSession')(
                self._provider_manager.get_item_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    item_admin_session = property(fget=get_item_admin_session)

    def get_item_admin_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ItemAdminSession')(
                self._provider_manager.get_item_admin_session_for_bank(bank_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_item_notification_session(self, item_receiver):
        raise Unimplemented()

    def get_item_bank_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ItemBankSession')(
                self._provider_manager.get_item_bank_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    item_bank_session = property(fget=get_item_bank_session)

    def get_item_bank_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ItemBankAssignmentSession')(
                self._provider_manager.get_item_bank_assignment_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    item_bank_assignment_session = property(fget=get_item_bank_assignment_session)

    def get_assessment_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_query_session()
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentLookupSession')(
                self._provider_manager.get_assessment_lookup_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    assessment_lookup_session = property(fget=get_assessment_lookup_session)

    def get_assessment_lookup_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentLookupSession')(
                self._provider_manager.get_assessment_lookup_session_for_bank(bank_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_query_session()
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentQuerySession')(
                self._provider_manager.get_assessment_query_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    assessment_query_session = property(fget=get_assessment_query_session)

    def get_assessment_query_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentQuerySession')(
                self._provider_manager.get_assessment_query_session_for_bank(bank_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentAdminSession')(
                self._provider_manager.get_assessment_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_admin_session = property(fget=get_assessment_admin_session)

    def get_assessment_admin_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentAdminSession')(
                self._provider_manager.get_assessment_admin_session_for_bank(bank_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_assessment_bank_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentBankSession')(
                self._provider_manager.get_assessment_bank_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_bank_session = property(fget=get_assessment_bank_session)

    def get_assessment_bank_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentBankAssignmentSession')(
                self._provider_manager.get_assessment_bank_assignment_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_bank_assignment_session = property(fget=get_assessment_bank_assignment_session)

    def get_assessment_basic_authoring_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentBasicAuthoringSession')(
                self._provider_manager.get_assessment_basic_authoring_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_basic_authoring_session = property(fget=get_assessment_basic_authoring_session)

    def get_assessment_basic_authoring_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentBasicAuthoringSession')(
                self._provider_manager.get_assessment_basic_authoring_session_for_bank(bank_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_offered_query_session()
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentOfferedLookupSession')(
                self._provider_manager.get_assessment_offered_lookup_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    assessment_offered_lookup_session = property(fget=get_assessment_offered_lookup_session)

    def get_assessment_offered_lookup_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_offered_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentOfferedLookupSession')(
                self._provider_manager.get_assessment_offered_lookup_session_for_bank(bank_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_offered_query_session()
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentOfferedQuerySession')(
                self._provider_manager.get_assessment_offered_query_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    assessment_offered_query_session = property(fget=get_assessment_offered_query_session)

    def get_assessment_offered_query_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_offered_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentOfferedQuerySession')(
                self._provider_manager.get_assessment_offered_query_session_for_bank(bank_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentOfferedAdminSession')(
                self._provider_manager.get_assessment_offered_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_offered_admin_session = property(fget=get_assessment_offered_admin_session)

    def get_assessment_offered_admin_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentOfferedAdminSession')(
                self._provider_manager.get_assessment_offered_admin_session_for_bank(bank_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_bank_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentOfferedBankSession')(
                self._provider_manager.get_assessment_offered_bank_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_offered_bank_session = property(fget=get_assessment_offered_bank_session)

    def get_assessment_offered_bank_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentOfferedBankAssignmentSession')(
                self._provider_manager.get_assessment_offered_bank_assignment_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_offered_bank_assignment_session = property(fget=get_assessment_offered_bank_assignment_session)

    def get_assessment_taken_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_taken_query_session()
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentTakenLookupSession')(
                self._provider_manager.get_assessment_taken_lookup_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    assessment_taken_lookup_session = property(fget=get_assessment_taken_lookup_session)

    def get_assessment_taken_lookup_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_taken_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentTakenLookupSession')(
                self._provider_manager.get_assessment_taken_lookup_session_for_bank(bank_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_taken_query_session()
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentTakenQuerySession')(
                self._provider_manager.get_assessment_taken_query_session(),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    assessment_taken_query_session = property(fget=get_assessment_taken_query_session)

    def get_assessment_taken_query_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_taken_query_session_for_bank(bank_id)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentTakenQuerySession')(
                self._provider_manager.get_assessment_taken_query_session_for_bank(bank_id),
                self._get_authz_session(),
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentTakenAdminSession')(
                self._provider_manager.get_assessment_taken_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_taken_admin_session = property(fget=get_assessment_taken_admin_session)

    def get_assessment_taken_admin_session_for_bank(self, bank_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentTakenAdminSession')(
                self._provider_manager.get_assessment_taken_admin_session_for_bank(bank_id),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_bank_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentTakenBankSession')(
                self._provider_manager.get_assessment_taken_bank_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_taken_bank_session = property(fget=get_assessment_taken_bank_session)

    def get_assessment_taken_bank_assignment_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentTakenBankAssignmentSession')(
                self._provider_manager.get_assessment_taken_bank_assignment_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    assessment_taken_bank_assignment_session = property(fget=get_assessment_taken_bank_assignment_session)

    def get_bank_lookup_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankLookupSession')(
                self._provider_manager.get_bank_lookup_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bank_lookup_session = property(fget=get_bank_lookup_session)

    def get_bank_query_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankQuerySession')(
                self._provider_manager.get_bank_query_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bank_query_session = property(fget=get_bank_query_session)

    def get_bank_admin_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankAdminSession')(
                self._provider_manager.get_bank_admin_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bank_admin_session = property(fget=get_bank_admin_session)

    def get_bank_hierarchy_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankHierarchySession')(
                self._provider_manager.get_bank_hierarchy_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bank_hierarchy_session = property(fget=get_bank_hierarchy_session)

    def get_bank_hierarchy_design_session(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankHierarchyDesignSession')(
                self._provider_manager.get_bank_hierarchy_design_session(),
                self._get_authz_session())
        except AttributeError:
            raise OperationFailed()

    bank_hierarchy_design_session = property(fget=get_bank_hierarchy_design_session)

    def get_assessment_authoring_manager(self):
        raise Unimplemented()

    assessment_authoring_manager = property(fget=get_assessment_authoring_manager)

    def get_assessment_batch_manager(self):
        raise Unimplemented()

    assessment_batch_manager = property(fget=get_assessment_batch_manager)


class AssessmentProxyManager(osid_managers.OsidProxyManager, AssessmentProfile, assessment_managers.AssessmentProxyManager):
    """Adapts underlying AssessmentProxyManager methodswith authorization checks."""


    def __init__(self):
        AssessmentProfile.__init__(self, 'AssessmentProxyManager')


    def initialize(self, runtime):
        osid_managers.OsidProxyManager.initialize(self, runtime)
        config = self._my_runtime.get_configuration()
        parameter_id = Id('parameter:assessmentProviderImpl@authz_adapter')
        provider_impl = config.get_value_by_parameter(parameter_id).get_string_value()
        self._provider_manager = runtime.get_proxy_manager('ASSESSMENT', provider_impl) # need to add version argument


    def get_assessment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentSession')(
                self._provider_manager.get_assessment_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentSession')(
                self._provider_manager.get_assessment_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_item_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_item_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ItemLookupSession')(
                self._provider_manager.get_item_lookup_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_item_lookup_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_item_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ItemLookupSession')(
                self._provider_manager.get_item_lookup_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_item_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_item_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ItemQuerySession')(
                self._provider_manager.get_item_query_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_item_query_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_item_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'ItemQuerySession')(
                self._provider_manager.get_item_query_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_item_search_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ItemSearchSession')(
                self._provider_manager.get_item_search_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_item_search_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ItemSearchSession')(
                self._provider_manager.get_item_search_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_item_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ItemAdminSession')(
                self._provider_manager.get_item_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_item_admin_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'ItemAdminSession')(
                self._provider_manager.get_item_admin_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_item_notification_session(self, item_receiver, proxy):
        raise Unimplemented()

    def get_item_bank_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ItemBankSession')(
                self._provider_manager.get_item_bank_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_item_bank_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'ItemBankAssignmentSession')(
                self._provider_manager.get_item_bank_assignment_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentLookupSession')(
                self._provider_manager.get_assessment_lookup_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_lookup_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentLookupSession')(
                self._provider_manager.get_assessment_lookup_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentQuerySession')(
                self._provider_manager.get_assessment_query_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_query_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentQuerySession')(
                self._provider_manager.get_assessment_query_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentAdminSession')(
                self._provider_manager.get_assessment_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_admin_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentAdminSession')(
                self._provider_manager.get_assessment_admin_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_bank_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentBankSession')(
                self._provider_manager.get_assessment_bank_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_bank_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentBankAssignmentSession')(
                self._provider_manager.get_assessment_bank_assignment_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_basic_authoring_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentBasicAuthoringSession')(
                self._provider_manager.get_assessment_basic_authoring_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_basic_authoring_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentBasicAuthoringSession')(
                self._provider_manager.get_assessment_basic_authoring_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_offered_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentOfferedLookupSession')(
                self._provider_manager.get_assessment_offered_lookup_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_lookup_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_offered_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentOfferedLookupSession')(
                self._provider_manager.get_assessment_offered_lookup_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_offered_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentOfferedQuerySession')(
                self._provider_manager.get_assessment_offered_query_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_query_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_offered_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentOfferedQuerySession')(
                self._provider_manager.get_assessment_offered_query_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentOfferedAdminSession')(
                self._provider_manager.get_assessment_offered_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_admin_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentOfferedAdminSession')(
                self._provider_manager.get_assessment_offered_admin_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_bank_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentOfferedBankSession')(
                self._provider_manager.get_assessment_offered_bank_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_offered_bank_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentOfferedBankAssignmentSession')(
                self._provider_manager.get_assessment_offered_bank_assignment_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_taken_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentTakenLookupSession')(
                self._provider_manager.get_assessment_taken_lookup_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_lookup_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_taken_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentTakenLookupSession')(
                self._provider_manager.get_assessment_taken_lookup_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            query_session = self._provider_manager.get_assessment_taken_query_session(proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentTakenQuerySession')(
                self._provider_manager.get_assessment_taken_query_session(proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_query_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            query_session = self._provider_manager.get_assessment_taken_query_session_for_bank(bank_id, proxy)
            query_session.use_federated_bank_view()
        except Unsupported:
            query_session = None
        try:
            return getattr(sessions, 'AssessmentTakenQuerySession')(
                self._provider_manager.get_assessment_taken_query_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy,
                hierarchy_session=self._get_hierarchy_session(),
                query_session=query_session)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentTakenAdminSession')(
                self._provider_manager.get_assessment_taken_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_admin_session_for_bank(self, bank_id, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_for_bin_template
        try:
            return getattr(sessions, 'AssessmentTakenAdminSession')(
                self._provider_manager.get_assessment_taken_admin_session_for_bank(bank_id, proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_bank_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentTakenBankSession')(
                self._provider_manager.get_assessment_taken_bank_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_taken_bank_assignment_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'AssessmentTakenBankAssignmentSession')(
                self._provider_manager.get_assessment_taken_bank_assignment_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bank_lookup_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankLookupSession')(
                self._provider_manager.get_bank_lookup_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bank_query_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankQuerySession')(
                self._provider_manager.get_bank_query_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bank_admin_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankAdminSession')(
                self._provider_manager.get_bank_admin_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bank_hierarchy_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankHierarchySession')(
                self._provider_manager.get_bank_hierarchy_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_bank_hierarchy_design_session(self, proxy):
        # Implemented from azosid template for -
        # osid.resource.ResourceManager.get_resource_lookup_session_template
        try:
            return getattr(sessions, 'BankHierarchyDesignSession')(
                self._provider_manager.get_bank_hierarchy_design_session(proxy),
                self._get_authz_session(),
                proxy)
        except AttributeError:
            raise OperationFailed()

    def get_assessment_authoring_proxy_manager(self):
        raise Unimplemented()

    assessment_authoring_proxy_manager = property(fget=get_assessment_authoring_proxy_manager)

    def get_assessment_batch_proxy_manager(self):
        raise Unimplemented()

    assessment_batch_proxy_manager = property(fget=get_assessment_batch_proxy_manager)


