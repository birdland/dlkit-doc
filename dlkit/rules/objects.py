from ..osid import objects as osid_objects


class Rule(osid_objects.OsidRule):
    """A ``Rule`` represents an entity that can be executed in a rules engine."""
    def get_rule_record(self, rule_record_type):
        """Gets the rule record corresponding to the given ``Rule`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``rule_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(rule_record_type)``
        is ``true`` .

        :param rule_record_type: the type of rule record to retrieve
        :type rule_record_type: ``osid.type.Type``
        :return: the rule record
        :rtype: ``osid.rules.records.RuleRecord``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(rule_record_type)`` is ``false``

        """
        return # osid.rules.records.RuleRecord


class RuleForm(osid_objects.OsidForm):
    """This is the form for creating and updating ``Rules``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``RuleAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_rule_form_record(self, rule_record_type):
        """Gets the ``RuleFormRecord`` corresponding to the given rule record ``Type``.

        :param rule_record_type: the rule record type
        :type rule_record_type: ``osid.type.Type``
        :return: the record
        :rtype: ``osid.rules.records.RuleFormRecord``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(rule_record_type)`` is ``false``

        """
        return # osid.rules.records.RuleFormRecord


class RuleList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``RuleList`` provides a means for accessing ``Rule`` elements sequentially either one at a time or many at a time.

    Examples: while (rl.hasNext()) { Rule rule = rl.getNextRule(); }

    or
      while (rl.hasNext()) {
           Rule[] rules = rl.getNextRules(rl.available());
      }
    


    """
    def get_next_rule(self):
        """Gets the next ``Rule`` in this list.

        :return: the next ``Rule`` in this list. The ``has_next()`` method should be used to test that a next ``Rule`` is available before calling this method.
        :rtype: ``osid.rules.Rule``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.rules.Rule

    next_rule = property(fget=get_next_rule)

    def get_next_rules(self, n):
        """Gets the next set of ``Rule`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Rule`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Rule`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.rules.Rule``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.rules.Rule


class Engine(osid_objects.OsidCatalog):
    """An ``Engine`` represents a collection of rules.

    Like all OSID objects, an ``Engine`` is identified by its ``Id`` and
    any persisted references should use the ``Id``.

    """
    def get_engine_record(self, engine_record_type):
        """Gets the engine record corresponding to the given ``Engine`` record ``Type``.

        This method is used to retrieve an object implementing the
        requested record. The ``engine_record_type`` may be the ``Type``
        returned in ``get_record_types()`` or any of its parents in a
        ``Type`` hierarchy where ``has_record_type(engine_record_type)``
        is ``true`` .

        :param engine_record_type: the type of engine record to retrieve
        :type engine_record_type: ``osid.type.Type``
        :return: the engine record
        :rtype: ``osid.rules.records.EngineRecord``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(engine_record_type)`` is ``false``

        """
        return # osid.rules.records.EngineRecord


class EngineForm(osid_objects.OsidCatalogForm):
    """This is the form for creating and updating ``Engines``.

    Like all ``OsidForm`` objects, various data elements may be set here
    for use in the create and update methods in the
    ``EngineAdminSession``. For each data element that may be set,
    metadata may be examined to provide display hints or data
    constraints.

    """
    def get_engine_form_record(self, engine_record_type):
        """Gets the ``EngineFormRecord`` corresponding to the given engine record ``Type``.

        :param engine_record_type: the engine record type
        :type engine_record_type: ``osid.type.Type``
        :return: the record
        :rtype: ``osid.rules.records.EngineFormRecord``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- ``has_record_type(engine_record_type)`` is ``false``

        """
        return # osid.rules.records.EngineFormRecord


class EngineList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``EngineList`` provides a means for accessing ``Engine`` elements sequentially either one at a time or many at a time.

    Examples: while (el.hasNext()) { Engine engine = el.getNextEngine();
    }

    or
      while (el.hasNext()) {
           Engine[] engines = el.getNextEngines(el.available());
      }
    


    """
    def get_next_engine(self):
        """Gets the next ``Engine`` in this list.

        :return: the next ``Engine`` in this list. The ``has_next()`` method should be used to test that a next ``Engine`` is available before calling this method.
        :rtype: ``osid.rules.Engine``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.rules.Engine

    next_engine = property(fget=get_next_engine)

    def get_next_engines(self, n):
        """Gets the next set of ``Engine`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Engine`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Engine`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.rules.Engine``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.rules.Engine


class EngineNode(osid_objects.OsidNode):
    """This interface is a container for a partial hierarchy retrieval.

    The number of hierarchy levels traversable through this interface
    depend on the number of levels requested in the
    ``EngineHierarchySession``.

    """
    def get_engine(self):
        """Gets the ``Engine`` at this node.

        :return: the engine represented by this node
        :rtype: ``osid.rules.Engine``

        """
        return # osid.rules.Engine

    engine = property(fget=get_engine)

    def get_parent_engine_nodes(self):
        """Gets the parents of this engine.

        :return: the parents of the ``id``
        :rtype: ``osid.rules.EngineNodeList``

        """
        return # osid.rules.EngineNodeList

    parent_engine_nodes = property(fget=get_parent_engine_nodes)

    def get_child_engine_nodes(self):
        """Gets the children of this engine.

        :return: the children of this engine
        :rtype: ``osid.rules.EngineNodeList``

        """
        return # osid.rules.EngineNodeList

    child_engine_nodes = property(fget=get_child_engine_nodes)


class EngineNodeList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``EngineNodeList`` provides a means for accessing ``EngineNode`` elements sequentially either one at a time or many at a time.

    Examples: while (enl.hasNext()) { EngineNode node =
    enl.getNextEngineNode(); }

    or
      while (enl.hasNext()) {
           EngineNode[] nodes = enl.getNextEngineNodes(enl.available());
      }
    


    """
    def get_next_engine_node(self):
        """Gets the next ``EngineNode`` in this list.

        :return: the next ``EngineNode`` in this list. The ``has_next()`` method should be used to test that a next ``EngineNode`` is available before calling this method.
        :rtype: ``osid.rules.EngineNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.rules.EngineNode

    next_engine_node = property(fget=get_next_engine_node)

    def get_next_engine_nodes(self, n):
        """Gets the next set of ``EngineNode`` elements in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``EngineNode`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``EngineNode`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.rules.EngineNode``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.rules.EngineNode


