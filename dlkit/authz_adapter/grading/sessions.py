"""AuthZ Adapter implementations of grading sessions."""
# pylint: disable=no-init
#     Numerous classes don't require __init__.
# pylint: disable=too-many-public-methods
#     Number of methods are defined in specification
# pylint: disable=too-many-ancestors
#     Inheritance defined in specification



from ...abstract_osid.grading import sessions as abc_grading_sessions
from ..osid.osid_errors import NotFound
from ..osid.osid_errors import PermissionDenied, NullArgument, Unimplemented
from ..osid.osid_errors import Unsupported
from ..primitives import Id
from ..utilities import QueryWrapper
from dlkit.authz_adapter.osid import sessions as osid_sessions




class GradeSystemLookupSession(abc_grading_sessions.GradeSystemLookupSession, osid_sessions.OsidSession):
    """Adapts underlying GradeSystemLookupSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradeSystem'
        self.use_federated_gradebook_view()
        self.use_comparative_grade_system_view()


    def _get_unauth_gradebook_ids(self, gradebook_id):
        if self._can('lookup', gradebook_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(gradebook_id)]
        if self._hierarchy_session.has_child_gradebooks(gradebook_id):
            for child_gradebook_id in self._hierarchy_session.get_child_gradebook_ids(gradebook_id):
                unauth_list = unauth_list + self._get_unauth_gradebook_ids(child_gradebook_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None or self._query_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for gradebook_id in self._get_unauth_gradebook_ids(self._qualifier_id):
            query.match_gradebook_id(gradebook_id, match=False)
        return self._query_session.get_grade_systems_by_query(query)


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_lookup_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._can('lookup')

    def use_comparative_grade_system_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_grade_system_view()

    def use_plenary_grade_system_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_grade_system_view()

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def get_grade_system(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_grade_system(grade_system_id)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_system_query()
            query.match_id(grade_system_id, match=True)
            results = self._try_harder(query)
            if results.available() > 0:
                return results.next()
            else:
                raise NotFound()

    def get_grade_system_by_grade(self, grade_id):
        raise Unimplemented()

    def get_grade_systems_by_ids(self, grade_system_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_grade_systems_by_ids(grade_system_ids)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_system_query()
            for grade_system_id in (grade_system_ids):
                query.match_id(grade_system_id, match=True)
            return self._try_harder(query)

    def get_grade_systems_by_genus_type(self, grade_system_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_grade_systems_by_genus_type(grade_system_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_system_query()
            query.match_genus_type(grade_system_genus_type, match=True)
            return self._try_harder(query)

    def get_grade_systems_by_parent_genus_type(self, grade_system_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_grade_systems_by_parent_genus_type(grade_system_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_system_query()
            query.match_parent_genus_type(grade_system_genus_type, match=True)
            return self._try_harder(query)

    def get_grade_systems_by_record_type(self, grade_system_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_grade_systems_by_record_type(grade_system_record_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_system_query()
            query.match_record_type(grade_system_record_type, match=True)
            return self._try_harder(query)

    def get_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_grade_systems()
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_system_query()
            query.match_any(match=True)
            return self._try_harder(query)

    grade_systems = property(fget=get_grade_systems)


class GradeSystemQuerySession(abc_grading_sessions.GradeSystemQuerySession, osid_sessions.OsidSession):
    """Adapts underlying GradeSystemQuerySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradeSystem'
        self.use_federated_gradebook_view()


    def _get_unauth_gradebook_ids(self, gradebook_id):
        if self._can('search', gradebook_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(gradebook_id)]
        if self._hierarchy_session.has_child_gradebooks(gradebook_id):
            for child_gradebook_id in self._hierarchy_session.get_child_gradebook_ids(gradebook_id):
                unauth_list = unauth_list + self._get_unauth_gradebook_ids(child_gradebook_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for gradebook_id in self._get_unauth_gradebook_ids(self._qualifier_id):
            query._provider_query.match_gradebook_id(gradebook_id, match=False)
        return self._provider_session.get_grade_systems_by_query(query)


    class GradeSystemQueryWrapper(QueryWrapper):
        """Wrapper for GradeSystemQueries to override match_gradebook_id method"""


        def match_gradebook_id(self, gradebook_id, match=True):
            self.cat_id_args_list.append({'gradebook_id': gradebook_id, 'match': match})


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_search_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._can('search')

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def get_grade_system_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and 
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.GradeSystemQueryWrapper(self._provider_session.get_grade_system_query())

    grade_system_query = property(fget=get_grade_system_query)

    def get_grade_systems_by_query(self, grade_system_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(grade_system_query, 'cat_id_args_list'):
            raise Unsupported('grade_system_query not from this session')
        for kwargs in grade_system_query.cat_id_args_list:
            if self._can('search', kwargs['gradebook_id']):
                grade_system_query._provider_query.match_gradebook_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_grade_systems_by_query(grade_system_query)
        elif self._is_isolated_catalog_view():
            raise PermissionDenied()
        else:
            result = self._try_harder(grade_system_query)
            grade_system_query._provider_query.clear_gradebook_terms()
            return result


class GradeSystemSearchSession(abc_grading_sessions.GradeSystemSearchSession, GradeSystemQuerySession):
    """Adapts underlying GradeSystemSearchSession methodswith authorization checks."""

    def get_grade_system_search(self):
        """Pass through to provider GradeSystemSearchSession.get_grade_system_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_system_search()

    grade_system_search = property(fget=get_grade_system_search)

    def get_grade_system_search_order(self):
        raise Unimplemented()

    grade_system_search_order = property(fget=get_grade_system_search_order)

    def get_grade_systems_by_search(self, grade_system_query, grade_system_search):
        """Pass through to provider GradeSystemSearchSession.get_grade_systems_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_systems_by_search(grade_system_query, grade_system_search)

    def get_grade_system_query_from_inspector(self, grade_system_query_inspector):
        raise Unimplemented()


class GradeSystemAdminSession(abc_grading_sessions.GradeSystemAdminSession, osid_sessions.OsidSession):
    """Adapts underlying GradeSystemAdminSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradeSystem'


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_create_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_grade_system_with_record_types(self, grade_system_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if grade_system_record_types == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_grade_system_form_for_create(self, grade_system_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_system_form_for_create(grade_system_record_types)

    def create_grade_system(self, grade_system_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_grade_system(grade_system_form)

    def can_update_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('update')

    def get_grade_system_form_for_update(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_system_form_for_update(grade_system_id)

    def duplicate_grade_system(self, grade_system_id):
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.duplicate_grade_system(grade_system_id)

    def update_grade_system(self, grade_system_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_grade_system(grade_system_form)

    def can_delete_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_grade_system(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_grade_system(grade_system_id)

    def can_manage_grade_system_aliases(self):
        raise Unimplemented()

    def alias_grade_system(self, grade_system_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_grade_system(grade_system_id, alias_id)

    def can_create_grades(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_grade_with_record_types(self, grade_system_id, grade_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if grade_system_id == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_grade_form_for_create(self, grade_system_id, grade_record_types):
        # Implemented from azosid template for -
        # osid.learning.ActivityAdminSession.get_activity_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_form_for_create(grade_system_id, grade_record_types)

    def create_grade(self, grade_form):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.create_asset_content_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_grade(grade_form)

    def can_update_grades(self, grade_system_id):
        raise Unimplemented()

    def get_grade_form_for_update(self, grade_id):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.get_asset_content_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_form_for_update(grade_id)

    def update_grade(self, grade_form):
        # Implemented from azosid template for -
        # osid.repository.AssetAdminSession.update_asset_content_template
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_grade(grade_form)

    def can_delete_grades(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_grade(self, grade_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_asset_content_template
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_grade(grade_id)

    def can_manage_grade_aliases(self):
        raise Unimplemented()

    def alias_grade(self, grade_id, alias_id):
        raise Unimplemented()


class GradeSystemNotificationSession(abc_grading_sessions.GradeSystemNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying GradeSystemNotificationSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradeSystem'


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_register_for_grade_system_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def register_for_new_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_grade_systems()

    def register_for_changed_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_grade_systems()

    def register_for_changed_grade_system(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_grade_system(grade_system_id)

    def register_for_deleted_grade_systems(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_grade_systems()

    def register_for_deleted_grade_system(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_grade_system(grade_system_id)

    def reliable_grade_system_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_grade_system_notifications()

    def unreliable_grade_system_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_grade_system_notifications()

    def acknowledge_grade_system_notification(self, notification_id):
        raise Unimplemented()


class GradeSystemGradebookSession(abc_grading_sessions.GradeSystemGradebookSession, osid_sessions.OsidSession):
    """Adapts underlying GradeSystemGradebookSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'grading.GradeSystemGradebook'


    def use_comparative_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_gradebook_view()

    def use_plenary_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_gradebook_view()

    def can_lookup_grade_system_gradebook_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def get_grade_system_ids_by_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_system_ids_by_gradebook(gradebook_id)

    def get_grade_systems_by_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_system_ids_by_gradebook(gradebook_id)

    def get_grade_system_ids_by_gradebooks(self, gradebook_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_system_ids_by_gradebooks(gradebook_ids)

    def get_grade_systems_by_gradebooks(self, gradebook_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_systems_ids_by_gradebooks(gradebook_ids)

    def get_gradebook_ids_by_grade_system(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_ids_by_grade_system(grade_system_id)

    def get_gradebooks_by_grade_system(self, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebooks_by_grade_system(grade_system_id)


class GradeSystemGradebookAssignmentSession(abc_grading_sessions.GradeSystemGradebookAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying GradeSystemGradebookAssignmentSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'grading.GradeSystemGradebook'


    def can_assign_grade_system(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    def can_assign_grade_systems_to_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bin_id)

    def get_assignable_gradebook_ids(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_gradebook_ids()

    def get_assignable_gradebook_ids_for_grade_system(self, gradebook_id, grade_system_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_gradebook_ids_for_grade_system(grade_system_id)

    def assign_grade_system_to_gradebook(self, grade_system_id, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.assign_grade_system_to_gradebook(grade_system_id, gradebook_id)

    def unassign_grade_system_from_gradebook(self, grade_system_id, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.unassign_grade_system_from_gradebook(grade_system_id, gradebook_id)


class GradeSystemSmartGradebookSession(abc_grading_sessions.GradeSystemSmartGradebookSession, osid_sessions.OsidSession):
    """Adapts underlying GradeSystemSmartGradebookSession methodswith authorization checks."""

    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_manage_smart_gradebooks(self):
        raise Unimplemented()

    def get_grade_system_query(self):
        raise Unimplemented()

    grade_system_query = property(fget=get_grade_system_query)

    def get_grade_system_search_order(self):
        raise Unimplemented()

    grade_system_search_order = property(fget=get_grade_system_search_order)

    def apply_grade_system_query(self, grade_system_query):
        raise Unimplemented()

    def inspect_grade_system_query(self):
        raise Unimplemented()

    def apply_grade_system_sequencing(self, grade_system_search_order):
        raise Unimplemented()

    def get_grade_system_query_from_inspector(self, grade_system_query_inspector):
        raise Unimplemented()


class GradeEntryLookupSession(abc_grading_sessions.GradeEntryLookupSession, osid_sessions.OsidSession):
    """Adapts underlying GradeEntryLookupSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None


        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradeEntry'


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_lookup_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._can('lookup')

    def use_comparative_grade_entry_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_grade_entry_view()

    def use_plenary_grade_entry_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_grade_entry_view()

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def use_effective_grade_entry_view(self):
        raise Unimplemented()

    def use_any_effective_grade_entry_view(self):
        raise Unimplemented()

    def get_grade_entry(self, grade_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_grade_entry(grade_entry_id)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_entry_query()
            query.match_id(grade_entry_id, match=True)
            results = self._try_harder(query)
            if results.available() > 0:
                return results.next()
            else:
                raise NotFound()

    def get_grade_entries_by_ids(self, grade_entry_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_grade_entries_by_ids(grade_entry_ids)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_entry_query()
            for grade_entry_id in (grade_entry_ids):
                query.match_id(grade_entry_id, match=True)
            return self._try_harder(query)

    def get_grade_entries_by_genus_type(self, grade_entry_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_grade_entries_by_genus_type(grade_entry_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_entry_query()
            query.match_genus_type(grade_entry_genus_type, match=True)
            return self._try_harder(query)

    def get_grade_entries_by_parent_genus_type(self, grade_entry_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_grade_entries_by_parent_genus_type(grade_entry_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_entry_query()
            query.match_parent_genus_type(grade_entry_genus_type, match=True)
            return self._try_harder(query)

    def get_grade_entries_by_record_type(self, grade_entry_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_grade_entries_by_record_type(grade_entry_record_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_entry_query()
            query.match_record_type(grade_entry_record_type, match=True)
            return self._try_harder(query)

    def get_grade_entries_on_date(self, from_, to):
        raise Unimplemented()

    def get_grade_entries_for_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.RelationshipLookupSession.get_relationships_for_source_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_entries_for_gradebook_column(gradebook_column_id)

    def get_grade_entries_for_gradebook_column_on_date(self, gradebook_column_id, from_, to):
        """Pass through to provider GradeEntryLookupSession.get_grade_entries_for_gradebook_column_on_date"""
        # Implemented from azosid template for -
        # osid.relationship.RelationshipLookupSession.get_relationships_for_source_on_date_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_entries_for_gradebook_column_on_date(gradebook_column_id, from_, to)

    def get_grade_entries_for_resource(self, resource_id):
        raise Unimplemented()

    def get_grade_entries_for_resource_on_date(self, resource_id, from_, to):
        raise Unimplemented()

    def get_grade_entries_for_gradebook_column_and_resource(self, gradebook_column_id, resource_id):
        raise Unimplemented()

    def get_grade_entries_for_gradebook_column_and_resource_on_date(self, gradebook_column_id, resource_id, from_, to):
        raise Unimplemented()

    def get_grade_entries_by_grader(self, resource_id):
        raise Unimplemented()

    def get_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_grade_entries()
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_grade_entry_query()
            query.match_any(match=True)
            return self._try_harder(query)

    grade_entries = property(fget=get_grade_entries)


class GradeEntryQuerySession(abc_grading_sessions.GradeEntryQuerySession, osid_sessions.OsidSession):
    """Adapts underlying GradeEntryQuerySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None


        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradeEntry'


    def _get_unauth_gradebook_ids(self, gradebook_id):
        if self._can('search', gradebook_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(gradebook_id)]
        if self._hierarchy_session.has_child_gradebooks(gradebook_id):
            for child_gradebook_id in self._hierarchy_session.get_child_gradebook_ids(gradebook_id):
                unauth_list = unauth_list + self._get_unauth_gradebook_ids(child_gradebook_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for gradebook_id in self._get_unauth_gradebook_ids(self._qualifier_id):
            query._provider_query.match_gradebook_id(gradebook_id, match=False)
        return self._provider_session.get_grade_entries_by_query(query)


    class GradeEntryQueryWrapper(QueryWrapper):
        """Wrapper for GradeEntryQueries to override match_gradebook_id method"""


        def match_gradebook_id(self, gradebook_id, match=True):
            self.cat_id_args_list.append({'gradebook_id': gradebook_id, 'match': match})


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_search_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._can('search')

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def get_grade_entry_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and 
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.GradeEntryQueryWrapper(self._provider_session.get_grade_entry_query())

    grade_entry_query = property(fget=get_grade_entry_query)

    def get_grade_entries_by_query(self, grade_entry_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(grade_entry_query, 'cat_id_args_list'):
            raise Unsupported('grade_entry_query not from this session')
        for kwargs in grade_entry_query.cat_id_args_list:
            if self._can('search', kwargs['gradebook_id']):
                grade_entry_query._provider_query.match_gradebook_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_grade_entries_by_query(grade_entry_query)
        elif self._is_isolated_catalog_view():
            raise PermissionDenied()
        else:
            result = self._try_harder(grade_entry_query)
            grade_entry_query._provider_query.clear_gradebook_terms()
            return result


class GradeEntrySearchSession(abc_grading_sessions.GradeEntrySearchSession, GradeEntryQuerySession):
    """Adapts underlying GradeEntrySearchSession methodswith authorization checks."""

    def get_grade_entry_search(self):
        """Pass through to provider GradeEntrySearchSession.get_grade_entry_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_entry_search()

    grade_entry_search = property(fget=get_grade_entry_search)

    def get_grade_entry_search_order(self):
        raise Unimplemented()

    grade_entry_search_order = property(fget=get_grade_entry_search_order)

    def get_grade_entries_by_search(self, grade_entry_query, grade_entry_search):
        """Pass through to provider GradeEntrySearchSession.get_grade_entries_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_entries_by_search(grade_entry_query, grade_entry_search)

    def get_grade_entry_query_from_inspector(self, grade_entry_query_inspector):
        raise Unimplemented()


class GradeEntryAdminSession(abc_grading_sessions.GradeEntryAdminSession, osid_sessions.OsidSession):
    """Adapts underlying GradeEntryAdminSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradeEntry'


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_create_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_grade_entry_with_record_types(self, grade_entry_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if grade_entry_record_types == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_grade_entry_form_for_create(self, gradebook_column_id, resource_id, grade_entry_record_types):
        # Implemented from azosid template for -
        # osid.resource.RelationshipAdminSession.get_relationship_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_entry_form_for_create(gradebook_column_id, resource_id, grade_entry_record_types)

    def create_grade_entry(self, grade_entry_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_grade_entry(grade_entry_form)

    def can_overridecalculated_grade_entries(self):
        raise Unimplemented()

    def get_grade_entry_form_for_override(self, grade_entry_id, grade_entry_record_types):
        raise Unimplemented()

    def override_calculated_grade_entry(self, grade_entry_form):
        raise Unimplemented()

    def can_update_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('update')

    def get_grade_entry_form_for_update(self, grade_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_grade_entry_form_for_update(grade_entry_id)

    def duplicate_grade_entry(self, grade_entry_id):
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.duplicate_grade_entry(grade_entry_id)

    def update_grade_entry(self, grade_entry_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_grade_entry(grade_entry_form)

    def can_delete_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_grade_entry(self, grade_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_grade_entry(grade_entry_id)

    def can_manage_grade_entry_aliases(self):
        raise Unimplemented()

    def alias_grade_entry(self, grade_entry_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_grade_entry(grade_entry_id, alias_id)


class GradeEntryNotificationSession(abc_grading_sessions.GradeEntryNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying GradeEntryNotificationSession methodswith authorization checks."""

    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_register_for_grade_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def register_for_new_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_grade_entries()

    def register_for_new_grade_entries_for_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_grade_entries_for_gradebook_column()

    def register_for_new_grade_entries_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_grade_entries_for_resource()

    def register_for_new_grade_entries_by_grader(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_grade_entries_by_grader()

    def register_for_changed_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_grade_entries()

    def register_for_changed_grade_entries_for_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_grade_entries_for_gradebook_column(gradebook_column_id)

    def register_for_changed_grade_entries_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_grade_entries_for_resource(resource_id)

    def register_for_changed_grade_entries_by_grader(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_grade_entries_by_grader(resource_id)

    def register_for_changed_grade_entry(self, grade_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_grade_entry(grade_entry_id)

    def register_for_deleted_grade_entries(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_grade_entries()

    def register_for_deleted_grade_entries_for_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_grade_entries_for_gradebook_column(gradebook_column_id)

    def register_for_deleted_grade_entries_for_resource(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_grade_entries_for_resource(resource_id)

    def register_for_deleted_grade_entries_by_grader(self, resource_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_grade_entries_by_grader(resource_id)

    def register_for_deleted_grade_entry(self, grade_entry_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_grade_entry(grade_entry_id)

    def reliable_grade_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_grade_entry_notifications()

    def unreliable_grade_entry_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_grade_entry_notifications()

    def acknowledge_grade_entry_notification(self, notification_id):
        raise Unimplemented()


class GradebookColumnLookupSession(abc_grading_sessions.GradebookColumnLookupSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookColumnLookupSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        if 'query_session' in kwargs:
            self._query_session = kwargs['query_session']
        else:
            self._query_session = None
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradebookColumn'
        self.use_federated_gradebook_view()
        self.use_comparative_gradebook_column_view()


    def _get_unauth_gradebook_ids(self, gradebook_id):
        if self._can('lookup', gradebook_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(gradebook_id)]
        if self._hierarchy_session.has_child_gradebooks(gradebook_id):
            for child_gradebook_id in self._hierarchy_session.get_child_gradebook_ids(gradebook_id):
                unauth_list = unauth_list + self._get_unauth_gradebook_ids(child_gradebook_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None or self._query_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for gradebook_id in self._get_unauth_gradebook_ids(self._qualifier_id):
            query.match_gradebook_id(gradebook_id, match=False)
        return self._query_session.get_gradebook_columns_by_query(query)


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_lookup_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._can('lookup')

    def use_comparative_gradebook_column_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_comparative_resource_view_template
        self._use_comparative_object_view()
        self._provider_session.use_comparative_gradebook_column_view()

    def use_plenary_gradebook_column_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_plenary_resource_view_template
        self._use_plenary_object_view()
        self._provider_session.use_plenary_gradebook_column_view()

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def get_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_gradebook_column(gradebook_column_id)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_gradebook_column_query()
            query.match_id(gradebook_column_id, match=True)
            results = self._try_harder(query)
            if results.available() > 0:
                return results.next()
            else:
                raise NotFound()

    def get_gradebook_columns_by_ids(self, gradebook_column_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_ids_template
        if self._can('lookup'):
            return self._provider_session.get_gradebook_columns_by_ids(gradebook_column_ids)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_gradebook_column_query()
            for gradebook_column_id in (gradebook_column_ids):
                query.match_id(gradebook_column_id, match=True)
            return self._try_harder(query)

    def get_gradebook_columns_by_genus_type(self, gradebook_column_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_gradebook_columns_by_genus_type(gradebook_column_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_gradebook_column_query()
            query.match_genus_type(gradebook_column_genus_type, match=True)
            return self._try_harder(query)

    def get_gradebook_columns_by_parent_genus_type(self, gradebook_column_genus_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_parent_genus_type_template
        if self._can('lookup'):
            return self._provider_session.get_gradebook_columns_by_parent_genus_type(gradebook_column_genus_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_gradebook_column_query()
            query.match_parent_genus_type(gradebook_column_genus_type, match=True)
            return self._try_harder(query)

    def get_gradebook_columns_by_record_type(self, gradebook_column_record_type):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_by_record_type_template
        if self._can('lookup'):
            return self._provider_session.get_gradebook_columns_by_record_type(gradebook_column_record_type)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_gradebook_column_query()
            query.match_record_type(gradebook_column_record_type, match=True)
            return self._try_harder(query)

    def get_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resources_template
        if self._can('lookup'):
            return self._provider_session.get_gradebook_columns()
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_gradebook_column_query()
            query.match_any(match=True)
            return self._try_harder(query)

    gradebook_columns = property(fget=get_gradebook_columns)

    def supports_summary(self):
        raise Unimplemented()

    def get_gradebook_column_summary(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_resource_template
        if self._can('lookup'):
            return self._provider_session.get_gradebook_column_summary(gradebook_column_id)
        elif self._is_isolated_catalog_view() or self._is_plenary_object_view():
            raise PermissionDenied()
        else:
            query = self._query_session.get_gradebook_column_query()
            query.match_id(gradebook_column_id, match=True)
            results = self._try_harder(query)
            if results.available() > 0:
                return results.next()
            else:
                raise NotFound()


class GradebookColumnQuerySession(abc_grading_sessions.GradebookColumnQuerySession, osid_sessions.OsidSession):
    """Adapts underlying GradebookColumnQuerySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None, **kwargs):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        if 'hierarchy_session' in kwargs:
            self._hierarchy_session = kwargs['hierarchy_session']
        else:
            self._hierarchy_session = None
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradebookColumn'
        self.use_federated_gradebook_view()


    def _get_unauth_gradebook_ids(self, gradebook_id):
        if self._can('search', gradebook_id):
            return [] # Don't go further - assumes authorizations inherited
        else:
            unauth_list = [str(gradebook_id)]
        if self._hierarchy_session.has_child_gradebooks(gradebook_id):
            for child_gradebook_id in self._hierarchy_session.get_child_gradebook_ids(gradebook_id):
                unauth_list = unauth_list + self._get_unauth_gradebook_ids(child_gradebook_id)
        return unauth_list


    def _try_harder(self, query):
        if self._hierarchy_session is None:
            # Should probably try to return empty result instead
            # perhaps through a query.match_any(match = None)?
            raise PermissionDenied()
        for gradebook_id in self._get_unauth_gradebook_ids(self._qualifier_id):
            query._provider_query.match_gradebook_id(gradebook_id, match=False)
        return self._provider_session.get_gradebook_columns_by_query(query)


    class GradebookColumnQueryWrapper(QueryWrapper):
        """Wrapper for GradebookColumnQueries to override match_gradebook_id method"""


        def match_gradebook_id(self, gradebook_id, match=True):
            self.cat_id_args_list.append({'gradebook_id': gradebook_id, 'match': match})


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_search_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._can('search')

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def get_gradebook_column_query(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resource_query_template
        if (not self._can('search') and 
                self._is_isolated_catalog_view()):
            raise PermissionDenied()
        else:
            return self.GradebookColumnQueryWrapper(self._provider_session.get_gradebook_column_query())

    gradebook_column_query = property(fget=get_gradebook_column_query)

    def get_gradebook_columns_by_query(self, gradebook_column_query):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.get_resources_by_query_template
        if not hasattr(gradebook_column_query, 'cat_id_args_list'):
            raise Unsupported('gradebook_column_query not from this session')
        for kwargs in gradebook_column_query.cat_id_args_list:
            if self._can('search', kwargs['gradebook_id']):
                gradebook_column_query._provider_query.match_gradebook_id(**kwargs)
        if self._can('search'):
            return self._provider_session.get_gradebook_columns_by_query(gradebook_column_query)
        elif self._is_isolated_catalog_view():
            raise PermissionDenied()
        else:
            result = self._try_harder(gradebook_column_query)
            gradebook_column_query._provider_query.clear_gradebook_terms()
            return result


class GradebookColumnSearchSession(abc_grading_sessions.GradebookColumnSearchSession, GradebookColumnQuerySession):
    """Adapts underlying GradebookColumnSearchSession methodswith authorization checks."""

    def get_gradebook_column_search(self):
        """Pass through to provider GradebookColumnSearchSession.get_gradebook_column_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resource_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_column_search()

    gradebook_column_search = property(fget=get_gradebook_column_search)

    def get_gradebook_column_search_order(self):
        raise Unimplemented()

    gradebook_column_search_order = property(fget=get_gradebook_column_search_order)

    def get_gradebook_columns_by_search(self, gradebook_column_query, gradebook_column_search):
        """Pass through to provider GradebookColumnSearchSession.get_gradebook_columns_by_search"""
        # Implemented from azosid template for -
        # osid.resource.ResourceSearchSession.get_resources_by_search_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_columns_by_search(gradebook_column_query, gradebook_column_search)

    def get_gradebook_column_query_from_inspector(self, gradebook_column_query_inspector):
        raise Unimplemented()


class GradebookColumnAdminSession(abc_grading_sessions.GradebookColumnAdminSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookColumnAdminSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradebookColumn'


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_create_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_gradebook_column_with_record_types(self, gradebook_column_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if gradebook_column_record_types == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_gradebook_column_form_for_create(self, gradebook_column_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_create
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_column_form_for_create(gradebook_column_record_types)

    def create_gradebook_column(self, gradebook_column_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.create_resource
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_gradebook_column(gradebook_column_form)

    def can_update_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('update')

    def get_gradebook_column_form_for_update(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.get_resource_form_for_update
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_column_form_for_update(gradebook_column_id)

    def duplicate_gradebook_column(self, gradebook_column_id):
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.duplicate_gradebook_column(gradebook_column_id)

    def update_gradebook_column(self, gradebook_column_form):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.update_resource
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_gradebook_column(gradebook_column_form)

    def sequence_gradebook_columns(self, gradebook_column_ids):
        raise Unimplemented()

    def move_gradebook_column(self, front_gradebook_column_id, back_gradebook_column_id):
        raise Unimplemented()

    def copy_gradebook_column_entries(self, source_gradebook_column_id, target_gradebook_column_id):
        raise Unimplemented()

    def can_delete_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.delete_resource
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_gradebook_column(gradebook_column_id)

    def can_manage_gradebook_column_aliases(self):
        raise Unimplemented()

    def alias_gradebook_column(self, gradebook_column_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.alias_resources
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_gradebook_column(gradebook_column_id, alias_id)


class GradebookColumnNotificationSession(abc_grading_sessions.GradebookColumnNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookColumnNotificationSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = provider_session.get_gradebook_id()
        self._id_namespace = 'grading.GradebookColumn'


    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_register_for_gradebook_column_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.can_register_for_resource_notifications
        return self._can('register')

    def use_federated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_federated_bin_view_template
        self._use_federated_catalog_view()
        self._provider_session.use_federated_gradebook_view()

    def use_isolated_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.use_isolated_bin_view_template
        self._use_isolated_catalog_view()
        self._provider_session.use_isolated_gradebook_view()

    def register_for_new_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_new_gradebook_columns()

    def register_for_changed_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_gradebook_columns()

    def register_for_changed_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_changed_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_changed_gradebook_column(gradebook_column_id)

    def register_for_deleted_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resources
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_gradebook_columns()

    def register_for_deleted_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_gradebook_column(gradebook_column_id)

    def reliable_gradebook_column_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_gradebook_column_notifications()

    def unreliable_gradebook_column_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_gradebook_column_notifications()

    def acknowledge_gradebook_column_notification(self, notification_id):
        raise Unimplemented()


class GradebookColumnGradebookSession(abc_grading_sessions.GradebookColumnGradebookSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookColumnGradebookSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'grading.GradebookColumnGradebook'


    def use_comparative_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_gradebook_view()

    def use_plenary_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_gradebook_view()

    def can_lookup_gradebook_column_gradebook_mappings(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.can_lookup_resource_bin_mappings
        return self._can('lookup')

    def get_gradebook_column_ids_by_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bin
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_column_ids_by_gradebook(gradebook_id)

    def get_gradebook_columns_by_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_column_ids_by_gradebook(gradebook_id)

    def get_gradebook_column_ids_by_gradebooks(self, gradebook_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resource_ids_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_column_ids_by_gradebooks(gradebook_ids)

    def get_gradebook_columns_by_gradebooks(self, gradebook_ids):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_resources_by_bins
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_columns_ids_by_gradebooks(gradebook_ids)

    def get_gradebook_ids_by_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bin_ids_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_ids_by_gradebook_column(gradebook_column_id)

    def get_gradebooks_by_gradebook_column(self, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinSession.get_bins_by_resource
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebooks_by_gradebook_column(gradebook_column_id)


class GradebookColumnGradebookAssignmentSession(abc_grading_sessions.GradebookColumnGradebookAssignmentSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookColumnGradebookAssignmentSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        self._qualifier_id = Id('authorization.Qualifier%3AROOT%40ODL.MIT.EDU') # This needs to be done right
        self._id_namespace = 'grading.GradebookColumnGradebook'


    def can_assign_gradebook_columns(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources
        return self._can('assign')

    def can_assign_gradebook_columns_to_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.can_assign_resources_to_bin
        return self._can('assign', qualifier_id=bin_id)

    def get_assignable_gradebook_ids(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_gradebook_ids()

    def get_assignable_gradebook_ids_for_gradebook_column(self, gradebook_id, gradebook_column_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.get_assignable_bin_ids_for_resource
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_assignable_gradebook_ids_for_gradebook_column(gradebook_column_id)

    def assign_gradebook_column_to_gradebook(self, gradebook_column_id, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.assign_gradebook_column_to_gradebook(gradebook_column_id, gradebook_id)

    def unassign_gradebook_column_from_gradebook(self, gradebook_column_id, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceBinAssignmentSession.assign_resource_to_bin
        if not self._can('assign'):
            raise PermissionDenied()
        else:
            return self._provider_session.unassign_gradebook_column_from_gradebook(gradebook_column_id, gradebook_id)


class GradebookColumnSmartGradebookSession(abc_grading_sessions.GradebookColumnSmartGradebookSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookColumnSmartGradebookSession methodswith authorization checks."""

    def get_gradebook_id(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_id_template
        return self._provider_session.get_gradebook_id()

    gradebook_id = property(fget=get_gradebook_id)

    def get_gradebook(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook()

    gradebook = property(fget=get_gradebook)

    def can_manage_smart_gradebooks(self):
        raise Unimplemented()

    def get_gradebook_column_query(self):
        raise Unimplemented()

    gradebook_column_query = property(fget=get_gradebook_column_query)

    def get_gradebook_column_search_order(self):
        raise Unimplemented()

    gradebook_column_search_order = property(fget=get_gradebook_column_search_order)

    def apply_gradebook_column_query(self, gradebook_column_query):
        raise Unimplemented()

    def inspect_gradebook_column_query(self):
        raise Unimplemented()

    def apply_gradebook_column_sequencing(self, gradebook_column_search_order):
        raise Unimplemented()

    def get_gradebook_column_query_from_inspector(self, gradebook_column_query_inspector):
        raise Unimplemented()


class GradebookLookupSession(abc_grading_sessions.GradebookLookupSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookLookupSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('grading.Gradebook%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'grading.Gradebook'


    def can_lookup_gradebooks(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceLookupSession.can_lookup_resources_template
        return self._can('lookup')

    def use_comparative_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_gradebook_view()

    def use_plenary_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_gradebook_view()

    def get_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bin_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook(gradebook_id)

    def get_gradebooks_by_ids(self, gradebook_ids):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_by_ids_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebooks_by_ids(gradebook_ids)

    def get_gradebooks_by_genus_type(self, gradebook_genus_type):
        raise Unimplemented()

    def get_gradebooks_by_parent_genus_type(self, gradebook_genus_type):
        raise Unimplemented()

    def get_gradebooks_by_record_type(self, gradebook_record_type):
        raise Unimplemented()

    def get_gradebooks_by_provider(self, resource_id):
        raise Unimplemented()

    def get_gradebooks(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.get_bins_template
        if not self._can('lookup'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebooks()

    gradebooks = property(fget=get_gradebooks)


class GradebookQuerySession(abc_grading_sessions.GradebookQuerySession, osid_sessions.OsidSession):
    """Adapts underlying GradebookQuerySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('grading.Gradebook%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'grading.Gradebook'


    def can_search_gradebooks(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceQuerySession.can_search_resources_template
        return self._can('search')

    def get_gradebook_query(self):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bin_query_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_query()

    gradebook_query = property(fget=get_gradebook_query)

    def get_gradebooks_by_query(self, gradebook_query):
        # Implemented from azosid template for -
        # osid.resource.BinQuerySession.get_bins_by_query_template
        if not self._can('search'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebooks_by_query(gradebook_query)


class GradebookSearchSession(abc_grading_sessions.GradebookSearchSession, GradebookQuerySession):
    """Adapts underlying GradebookSearchSession methodswith authorization checks."""

    def get_gradebook_search(self):
        raise Unimplemented()

    gradebook_search = property(fget=get_gradebook_search)

    def get_gradebook_search_order(self):
        raise Unimplemented()

    gradebook_search_order = property(fget=get_gradebook_search_order)

    def get_gradebooks_by_search(self, gradebook_query, gradebook_search):
        raise Unimplemented()

    def get_gradebook_query_from_inspector(self, gradebook_query_inspector):
        raise Unimplemented()


class GradebookAdminSession(abc_grading_sessions.GradebookAdminSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookAdminSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('grading.Gradebook%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'grading.Gradebook'


    def can_create_gradebooks(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('create')

    def can_create_gradebook_with_record_types(self, gradebook_record_types):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resource_with_record_types
        # This would like to be a real implementation someday:
        if gradebook_record_types == None:
            raise NullArgument() # Just 'cause the spec says to :)
        else:
            return self._can('create')

    def get_gradebook_form_for_create(self, gradebook_record_types):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_create_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_form_for_create(gradebook_record_types)

    def create_gradebook(self, gradebook_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.create_bin_template
        if not self._can('create'):
            raise PermissionDenied()
        else:
            return self._provider_session.create_gradebook(gradebook_form)

    def can_update_gradebooks(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('update')

    def get_gradebook_form_for_update(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.get_bin_form_for_update_template
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_form_for_update(gradebook_id)

    def update_gradebook(self, gradebook_form):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.update_bin_template
        if not self._can('update'):
            raise PermissionDenied()
        else:
            return self._provider_session.update_gradebook(gradebook_form)

    def can_delete_gradebooks(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceAdminSession.can_create_resources
        return self._can('delete')

    def delete_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.delete_bin_template
        if not self._can('delete'):
            raise PermissionDenied()
        else:
            return self._provider_session.delete_gradebook(gradebook_id)

    def can_manage_gradebook_aliases(self):
        raise Unimplemented()

    def alias_gradebook(self, gradebook_id, alias_id):
        # Implemented from azosid template for -
        # osid.resource.BinAdminSession.alias_bin_template
        if not self._can('alias'):
            raise PermissionDenied()
        else:
            return self._provider_session.alias_gradebook(gradebook_id)


class GradebookNotificationSession(abc_grading_sessions.GradebookNotificationSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookNotificationSession methodswith authorization checks."""

    def can_register_for_gradebook_notifications(self):
        raise Unimplemented()

    def register_for_new_gradebooks(self):
        raise Unimplemented()

    def register_for_new_gradebook_ancestors(self, gradebook_id):
        raise Unimplemented()

    def register_for_new_gradebook_descendants(self, gradebook_id):
        raise Unimplemented()

    def register_for_changed_gradebooks(self):
        raise Unimplemented()

    def register_for_changed_gradebook(self, gradebook_id):
        raise Unimplemented()

    def register_for_deleted_gradebooks(self):
        raise Unimplemented()

    def register_for_deleted_gradebook(self, gradebook_id):
        raise Unimplemented()

    def register_for_deleted_gradebook_ancestors(self, gradebook_id):
        raise Unimplemented()

    def register_for_deleted_gradebook_descendants(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_deleted_resource
        if not self._can('register'):
            raise PermissionDenied()
        else:
            self._provider_session.register_for_deleted_gradebook_descendants(gradebook_id)

    def reliable_gradebook_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.reliable_gradebook_notifications()

    def unreliable_gradebook_notifications(self):
        # Implemented from azosid template for -
        # osid.resource.ResourceNotificationSession.register_for_new_resources
        self._provider_session.unreliable_gradebook_notifications()

    def acknowledge_gradebook_notification(self, notification_id):
        raise Unimplemented()


class GradebookHierarchySession(abc_grading_sessions.GradebookHierarchySession, osid_sessions.OsidSession):
    """Adapts underlying GradebookHierarchySession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('grading.Gradebook%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'grading.Gradebook'


    def get_gradebook_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_gradebook_hierarchy_id()

    gradebook_hierarchy_id = property(fget=get_gradebook_hierarchy_id)

    def get_gradebook_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_hierarchy()

    gradebook_hierarchy = property(fget=get_gradebook_hierarchy)

    def can_access_gradebook_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.can_access_bin_hierarchy
        return self._can('access')

    def use_comparative_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_comparative_bin_view_template
        self._provider_session.use_comparative_gradebook_view()

    def use_plenary_gradebook_view(self):
        # Implemented from azosid template for -
        # osid.resource.BinLookupSession.use_plenary_bin_view_template
        self._provider_session.use_plenary_gradebook_view()

    def get_root_gradebook_ids(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_root_gradebook_ids()

    root_gradebook_ids = property(fget=get_root_gradebook_ids)

    def get_root_gradebooks(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_root_bins
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_root_gradebooks()

    root_gradebooks = property(fget=get_root_gradebooks)

    def has_parent_gradebooks(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.has_parent_gradebooks(gradebook_id)

    def is_parent_of_gradebook(self, id_, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_parent_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.is_parent_of_gradebook(id_, gradebook_id)

    def get_parent_gradebook_ids(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_parent_gradebook_ids(gradebook_id)

    def get_parent_gradebooks(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_parent_bins
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_parent_gradebooks(gradebook_id)

    def is_ancestor_of_gradebook(self, id_, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_ancestor_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.is_ancestor_of_gradebook(id_, gradebook_id)

    def has_child_gradebooks(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.has_child_bins
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.has_child_gradebooks(gradebook_id)

    def is_child_of_gradebook(self, id_, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_child_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.is_child_of_gradebook(id_, gradebook_id)

    def get_child_gradebook_ids(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_child_bin_ids
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_child_gradebook_ids(gradebook_id)

    def get_child_gradebooks(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_child_gradebooks(gradebook_id)

    def is_descendant_of_gradebook(self, id_, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.is_descendant_of_bin
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.is_descendant_of_gradebook(id_, gradebook_id)

    def get_gradebook_node_ids(self, gradebook_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_node_ids
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_node_ids(
                gradebook_id,
                ancestor_levels,
                descendant_levels,
                include_siblings)

    def get_gradebook_nodes(self, gradebook_id, ancestor_levels, descendant_levels, include_siblings):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_nodes
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_nodes(
                gradebook_id,
                ancestor_levels,
                descendant_levels,
                include_siblings)


class GradebookHierarchyDesignSession(abc_grading_sessions.GradebookHierarchyDesignSession, osid_sessions.OsidSession):
    """Adapts underlying GradebookHierarchyDesignSession methodswith authorization checks."""


    def __init__(self, provider_session, authz_session, proxy=None):
        osid_sessions.OsidSession.__init__(self, provider_session, authz_session, proxy)
        # This needs to be done right
        # Build from authority in config
        self._qualifier_id = Id('grading.Gradebook%3AROOT%40ODL.MIT.EDU')
        self._id_namespace = 'grading.Gradebook' # should this be 'grading.GradebookHierarchy' ?


    def get_gradebook_hierarchy_id(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy_id
        return self._provider_session.get_gradebook_hierarchy_id()

    gradebook_hierarchy_id = property(fget=get_gradebook_hierarchy_id)

    def get_gradebook_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchySession.get_bin_hierarchy
        if not self._can('access'):
            raise PermissionDenied()
        else:
            return self._provider_session.get_gradebook_hierarchy()

    gradebook_hierarchy = property(fget=get_gradebook_hierarchy)

    def can_modify_gradebook_hierarchy(self):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.can_modify_bin_hierarchy
        return self._can('modify')

    def add_root_gradebook(self, gradebook_id):
        # Implemented from azosid template for -
        # osid.resource.BinHierarchyDesignSession.add_root_bin_template
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.add_root_gradebook(gradebook_id)

    def remove_root_gradebook(self, gradebook_id):
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.remove_root_gradebook(gradebook_id)

    def add_child_gradebook(self, gradebook_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.add_child_gradebook(gradebook_id, child_id)

    def remove_child_gradebook(self, gradebook_id, child_id):
        if not self._can('modify'):
            raise PermissionDenied()
        else:
            return self._provider_session.remove_child_gradebook(gradebook_id, child_id)


