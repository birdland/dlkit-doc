
from ..osid import objects as osid_objects


class Agent(osid_objects.OsidObject):
    """An ``Agent`` represents an authenticatable identity.

    Like all OSID objects, an ``Agent`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """

    def get_agent_record(self, agent_record_type):
        """Gets the agent record corresponding to the given ``Agent`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``agent_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(agent_record_type)``
        is ``true`` .

        :param agent_record_type: the type of the record to retrieve
        :type agent_record_type: ``osid.type.Type``
        :return: the agent record
        :rtype: ``osid.authentication.records.AgentRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.records.AgentRecord


class AgentForm(osid_objects.OsidObjectForm):
    """This is the form for creating and updating ``Agents``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``AgentAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """

    def get_agent_form_record(self, agent_record_type):
        """Gets the ``AgentFormRecord`` corresponding to the given agent record ``Type``.

        :param agent_record_type: the agent record type
        :type agent_record_type: ``osid.type.Type``
        :return: the agent form record
        :rtype: ``osid.authentication.records.AgentFormRecord``
        :raise: ``NullArgument`` -- ``agent_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(agent_record_type)`` is ``false``

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.records.AgentFormRecord


class AgentList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``AgentList`` provides a means for accessing ``Agent`` elements sequentially either one at a time or many at a time.

    Examples: while (al.hasNext()) { Agent agent = al.getNextAgent(); }

    or
      while (al.hasNext()) {
           Agent[] agents = al.getNextAgents(al.available());
      }

    """

    def get_next_agent(self):
        """Gets the next ``Agent`` in this list.

        :return: the next ``Agent`` in this list. The ``has_next()`` method should be used to test that a next ``Agent`` is available before calling this method.
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent

    next_agent = property(fget=get_next_agent)

    def get_next_agents(self, n):
        """Gets the next set of ``Agent`` elements in this list which must be less than or equal to the number returned from ``available()``.

        :param n: the number of ``Agent`` elements requested which should be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Agent`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.authentication.Agent


