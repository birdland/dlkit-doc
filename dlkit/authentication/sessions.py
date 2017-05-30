
from ..osid import sessions as osid_sessions


class AgentLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Agent`` objects.

    The ``Agent`` represents the authenticated entity. Agents generally
    map to resources although this isn't always the case.

    This session defines two sets of views which offer differing
    behaviors when retrieving multiple objects.

      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete and ordered result set or is
        an error condition
      * isolated agency view: All agent methods in this session operate,
        retrieve and pertain to agents defined explicitly in the current
        agency. Using an isolated view is useful for managing agents
        with the AgentAdminSession.
      * federated agency view: All agent methods in this session
        operate, retrieve and pertain to all agents defined in this
        agency and any other agents implicitly available in this agency
        through agency inheritence.


    Generally, the comparative view should be used for most applications
    as it permits operation even if there a particular element is
    inaccessible. For example, a hierarchy output can be plugged into a
    lookup method to retrieve all objects known to a hierarchy, but it
    may not be necessary to break execution if a node from the hierarchy
    no longer exists. However, some administrative applications may need
    to know whether it had retrieved an entire set of objects and may
    sacrifice some interoperability for the sake of precision.

    Agents may have an additional records indicated by their respective
    record types. The record may not be accessed through a cast of the
    ``Agent``.

    """

    def get_agency_id(self):
        """Gets the ``Agency``  ``Id`` associated with this session.

        :return: the ``Agency Id`` associated with this session
        :rtype: ``osid.id.Id``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.id.Id

    agency_id = property(fget=get_agency_id)

    def get_agency(self):
        """Gets the ``Agency`` associated with this session.

        :return: the ``Agency`` associated with this session
        :rtype: ``osid.authentication.Agency``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agency

    agency = property(fget=get_agency)

    def can_lookup_agents(self):
        """Tests if this user can perform ``Agent`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # boolean

    def use_comparative_agent_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_plenary_agent_view(self):
        """A complete view of the ``Agent`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_federated_agency_view(self):
        """Federates the view for methods in this session.

        A federated view will include agents in agencies which are
        children of this agency in the agency hierarchy.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def use_isolated_agency_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts lookups to this agency only.



        *compliance: mandatory -- This method is must be implemented.*

        """
        pass

    def get_agent(self, agent_id):
        """Gets the ``Agent`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Agent`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Agent`` and retained for compatibility.

        :param agent_id: the ``Id`` of an ``Agent``
        :type agent_id: ``osid.id.Id``
        :return: the returned ``Agent``
        :rtype: ``osid.authentication.Agent``
        :raise: ``NotFound`` -- no ``Agent`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``agent_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    def get_agents_by_ids(self, agent_ids):
        """Gets an ``AgentList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the agents
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Agents`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param agent_ids: a list of agent ``Ids``
        :type agent_ids: ``osid.id.IdList``
        :return: the returned ``Agent list``
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NotFound`` -- an ``Id was`` not found
        :raise: ``NullArgument`` -- ``agent_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.AgentList

    def get_agents_by_genus_type(self, agent_genus_type):
        """Gets an ``AgentList`` corresponding to the given agent genus ``Type`` which does not include agents of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_genus_type: an agent genus type
        :type agent_genus_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.AgentList

    def get_agents_by_parent_genus_type(self, agent_genus_type):
        """Gets an ``AgentList`` corresponding to the given agent genus ``Type`` and include any additional agents with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_genus_type: an agent genus type
        :type agent_genus_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.AgentList

    def get_agents_by_record_type(self, agent_record_type):
        """Gets an ``AgentList`` containing the given agent record ``Type``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :param agent_record_type: an agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the returned ``Agent`` list
        :rtype: ``osid.authentication.AgentList``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.AgentList

    def get_agents(self):
        """Gets all ``Agents``.

        In plenary mode, the returned list contains all known agents or
        an error results. Otherwise, the returned list may contain only
        those agents that are accessible through this session.

        :return: a list of ``Agents``
        :rtype: ``osid.authentication.AgentList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.AgentList

    agents = property(fget=get_agents)


