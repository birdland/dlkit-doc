from ..osid import sessions as osid_sessions


class RulesSession(osid_sessions.OsidSession):
    """This session provides methods to evaluate and execute rules."""
    def get_engine_id(self):
        """Gets the ``Engine``  ``Id`` associated with this session.

        :return: the ``Engine Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    engine_id = property(fget=get_engine_id)

    def get_engine(self):
        """Gets the ``Engine`` associated with this session.

        :return: the engine
        :rtype: ``osid.rules.Engine``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Engine

    engine = property(fget=get_engine)

    def can_evaluate_rules(self):
        """Tests if this user can evaluate rules.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer these
        operations.

        :return: ``false`` if evaluation methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_condition_for_rule(self, rule_id):
        """Gets a condition for the given rule.

        :param rule_id: the ``Id`` of a ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: the returned ``Condition``
        :rtype: ``osid.rules.Condition``
        :raise: ``NotFound`` -- no ``Rule`` found with the given ``Id``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Condition

    def evaluate_rule(self, rule_id, condition):
        """Evaluates a rule based on an input condition.

        :param rule_id: a rule ``Id``
        :type rule_id: ``osid.id.Id``
        :param condition: input conditions
        :type condition: ``osid.rules.Condition``
        :return: result of the evaluation
        :rtype: ``boolean``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``rule_id`` or ``condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``condition`` not of this service

        """
        return # boolean

    def execute_rule(self, rule_id, condition):
        """Executes a rule based on an input condition and returns a result.

        :param rule_id: a rule ``Id``
        :type rule_id: ``osid.id.Id``
        :param condition: input conditions
        :type condition: ``osid.rules.Condition``
        :return: result of the execution
        :rtype: ``osid.rules.Result``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``rule_id`` or ``condition`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``condition`` not of this service

        """
        return # osid.rules.Result


class RuleLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Rule`` objects."""
    def get_engine_id(self):
        """Gets the ``Engine``  ``Id`` associated with this session.

        :return: the ``Engine Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    engine_id = property(fget=get_engine_id)

    def get_engine(self):
        """Gets the ``Engine`` associated with this session.

        :return: the engine
        :rtype: ``osid.rules.Engine``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Engine

    engine = property(fget=get_engine)

    def can_lookup_rules(self):
        """Tests if this user can perform ``Rule`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer lookup
        operations to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_rule_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_rule_view(self):
        """A complete view of the ``Rule`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def use_federated_engine_view(self):
        """Federates the view for methods in this session.

        A federated view will include rules in engines which are
        children of this engine in the engine hierarchy.



        """
        pass

    def use_isolated_engine_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this engine only.



        """
        pass

    def use_active_rule_view(self):
        """Only active rules are returned by methods in this session."""
        pass

    def use_any_status_rule_view(self):
        """All active and inactive rules are returned by methods in this session."""
        pass

    def get_rule(self, rule_id):
        """Gets the ``Rule`` specified by its ``Id``.

        :param rule_id: ``Id`` of the ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: the rule
        :rtype: ``osid.rules.Rule``
        :raise: ``NotFound`` -- ``rule_id`` not found
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Rule

    def get_rules_by_ids(self, rule_ids):
        """Gets a ``RuleList`` corresponding to the given ``IdList``.

        :param rule_ids: the list of ``Ids`` to retrieve
        :type rule_ids: ``osid.id.IdList``
        :return: the returned ``Rule`` list
        :rtype: ``osid.rules.RuleList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``rule_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.RuleList

    def get_rules_by_genus_type(self, rule_genus_type):
        """Gets a ``RuleList`` corresponding to the given rule genus ``Type`` which does not include rules of genus types derived from the specified ``Type``.

        :param rule_genus_type: a rule genus type
        :type rule_genus_type: ``osid.type.Type``
        :return: the returned ``Rule`` list
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``rule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.RuleList

    def get_rules_by_parent_genus_type(self, rule_genus_type):
        """Gets a ``RuleList`` corresponding to the given rule genus ``Type`` and include any additional rules with genus types derived from the specified ``Type``.

        :param rule_genus_type: a rule genus type
        :type rule_genus_type: ``osid.type.Type``
        :return: the returned ``Rule`` list
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``rule_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.RuleList

    def get_rules_by_record_type(self, rule_record_type):
        """Gets a ``RuleList`` containing the given repository record ``Type``.

        :param rule_record_type: a rule record type
        :type rule_record_type: ``osid.type.Type``
        :return: the returned ``Rule`` list
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``rule_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.RuleList

    def get_rules(self):
        """Gets all ``Rules``.

        :return: a list of ``Rules``
        :rtype: ``osid.rules.RuleList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.RuleList

    rules = property(fget=get_rules)


class RuleQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching ``Rule`` objects.

    The search query is constructed using the ``RuleQuery``. The rule
    record ``Type`` also specifies the record for the rule query.

    Rules may have a rule query record indicated by their respective
    record types. The rule query record is accessed via the
    ``RuleQuery``. The returns in this session may not be cast directly
    to these interfaces.

    """
    def get_engine_id(self):
        """Gets the ``Engine``  ``Id`` associated with this session.

        :return: the ``Engine Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    engine_id = property(fget=get_engine_id)

    def get_engine(self):
        """Gets the ``Engine`` associated with this session.

        :return: the engine
        :rtype: ``osid.rules.Engine``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Engine

    engine = property(fget=get_engine)

    def use_federated_engine_view(self):
        """Federates the view for methods in this session.

        A federated view will include rules in engines which are
        children of this engine in the engine hierarchy.



        """
        pass

    def use_isolated_engine_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts retrievals to this engine only.



        """
        pass

    def can_search_rules(self):
        """Tests if this user can perform ``Rule`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_rule_query(self):
        """Gets a rule query.

        :return: the rule query
        :rtype: ``osid.rules.RuleQuery``

        """
        return # osid.rules.RuleQuery

    rule_query = property(fget=get_rule_query)

    def get_rules_by_query(self, rule_query):
        """Gets a list of ``Rules`` matching the given rule query.

        :param rule_query: the rule query
        :type rule_query: ``osid.rules.RuleQuery``
        :return: the returned ``RuleList``
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``rule_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``rule_query`` is not of this service

        """
        return # osid.rules.RuleList


class RuleSearchSession(RuleQuerySession):
    """This session provides methods for searching ``Rule`` objects.

    The search query is constructed using the ``RuleQuery``. The rule
    record ``Type`` also specifies the record for the rule query.

    ``get_rules_by_query()`` is the basic search method and returns a
    list of ``Rule`` elements. A more advanced search may be performed
    with ``getRulesBySearch()``. It accepts a ``RuleSearch`` in addition
    to the query for the purpose of specifying additional options
    affecting the entire search, such as ordering.
    ``get_rules_by_search()`` returns a ``RuleSearchResults`` that can
    be used to access the resulting ``RuleList`` or be used to perform a
    search within the result set through ``RuleSearch``.
    
    Rules may have a query record indicated by their respective record
    types. The rule query record is accessed via the ``RuleQuery``. The
    returns in this session may not be cast directly to these
    interfaces.

    """
    def get_rule_search(self):
        """Gets a rule search.

        :return: the rule search
        :rtype: ``osid.rules.RuleSearch``

        """
        return # osid.rules.RuleSearch

    rule_search = property(fget=get_rule_search)

    def get_rule_search_order(self):
        """Gets a rule search order.

        The ``RuleSearchOrder`` is supplied to a ``RuleSearch`` to
        specify the ordering of results.

        :return: the rule search order
        :rtype: ``osid.rules.RuleSearchOrder``

        """
        return # osid.rules.RuleSearchOrder

    rule_search_order = property(fget=get_rule_search_order)

    def get_rules_by_search(self, rule_query, rule_search):
        """Gets the search results matching the given search.

        :param rule_query: the rule query
        :type rule_query: ``osid.rules.RuleQuery``
        :param rule_search: the rule search
        :type rule_search: ``osid.rules.RuleSearch``
        :return: the search results
        :rtype: ``osid.rules.RuleSearchResults``
        :raise: ``NullArgument`` -- ``rule_query`` or ``rule_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``rule_query`` or ``rule_search`` is not of this service

        """
        return # osid.rules.RuleSearchResults

    def get_rule_query_from_inspector(self, rule_query_inspector):
        """Gets a rule query from an inspector.

        The inspector is available from a ``RuleSearchResults``.

        :param rule_query_inspector: a rule query inspector
        :type rule_query_inspector: ``osid.rules.RuleQueryInspector``
        :return: the rule query
        :rtype: ``osid.rules.RuleQuery``
        :raise: ``NullArgument`` -- ``rule_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``rule_query_inspector`` is not of this service

        """
        return # osid.rules.RuleQuery


class RuleAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Rules``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create a
    ``Rule,`` a ``RuleForm`` is requested using
    ``get_rule_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``RuleForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``RuleForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``RuleForm`` corresponds
    to an attempted transaction.
    
    For updates, ``RuleForms`` are requested to the ``Rule``  ``Id``
    that is to be updated using ``getRuleFormForUpdate()``. Similarly,
    the ``RuleForm`` has metadata about the data that can be updated and
    it can perform validation before submitting the update. The
    ``RuleForm`` can only be used once for a successful update and
    cannot be reused.
    
    The delete operations delete ``Rules``. To unmap a ``Rule`` from the
    current ``Engine,`` the ``RuleEngineAssignmentSession`` should be
    used. These delete operations attempt to remove the ``Rule`` itself
    thus removing it from all known ``Engine`` catalogs.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def get_engine_id(self):
        """Gets the ``Engine``  ``Id`` associated with this session.

        :return: the ``Engine Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    engine_id = property(fget=get_engine_id)

    def get_engine(self):
        """Gets the ``Engine`` associated with this session.

        :return: the ``Engine`` associated with this session
        :rtype: ``osid.rules.Engine``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Engine

    engine = property(fget=get_engine)

    def can_create_rules(self):
        """Tests if this user can create ``Rules``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating a ``Rule``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer create
        operations to an unauthorized user.

        :return: ``false`` if ``Rule`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_rule_with_record_types(self, rule_record_types):
        """Tests if this user can create a single ``Rule`` using the desired record types.

        While ``RulesManager.getRuleRecordTypes()`` can be used to
        examine which records are supported, this method tests which
        record(s) are required for creating a specific ``Rule``.
        Providing an empty array tests if a ``Rule`` can be created with
        no records.

        :param rule_record_types: array of rule record types
        :type rule_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Rule`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``rule_record_types`` is ``null``

        """
        return # boolean

    def get_rule_form_for_create(self, rule_record_types):
        """Gets the rule form for creating new rules.

        A new form should be requested for each create transaction.

        :param rule_record_types: array of rule record types
        :type rule_record_types: ``osid.type.Type[]``
        :return: the rule form
        :rtype: ``osid.rules.RuleForm``
        :raise: ``NullArgument`` -- ``rule_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        return # osid.rules.RuleForm

    def create_rule(self, rule_form):
        """Creates a new ``Rule``.

        :param rule_form: the form for this ``Rule``
        :type rule_form: ``osid.rules.RuleForm``
        :return: the new ``Rule``
        :rtype: ``osid.rules.Rule``
        :raise: ``IllegalState`` -- ``rule_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``rule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``rule_form`` did not originate from ``get_rule_form_for_create()``

        """
        return # osid.rules.Rule

    def can_update_rules(self):
        """Tests if this user can update ``Rules``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating a ``Rule``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer update
        operations to an unauthorized user.

        :return: ``false`` if rule modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_rule_form_for_update(self, rule_id):
        """Gets the rule form for updating an existing rule.

        A new rule form should be requested for each update transaction.

        :param rule_id: the ``Id`` of the ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: the rule form
        :rtype: ``osid.rules.RuleForm``
        :raise: ``NotFound`` -- ``rule_id`` is not found
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.RuleForm

    def update_rule(self, rule_form):
        """Updates an existing rule.

        :param rule_form: the form containing the elements to be updated
        :type rule_form: ``osid.rules.RuleForm``
        :raise: ``IllegalState`` -- ``rule_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``rule_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``rule_form`` did not originate from ``get_rule_form_for_update()``

        """
        pass

    def can_delete_rules(self):
        """Tests if this user can delete ``Rules``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting a ``Rule``
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer delete
        operations to an unauthorized user.

        :return: ``false`` if ``Rule`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_rule(self, rule_id):
        """Deletes the ``Rule`` identified by the given ``Id``.

        :param rule_id: the ``Id`` of the ``Rule`` to delete
        :type rule_id: ``osid.id.Id``
        :raise: ``NotFound`` -- a ``Rule`` was not found identified by the given ``Id``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_rule_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Rules``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Rule`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_rule(self, rule_id, alias_id):
        """Adds an ``Id`` to a ``Rule`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Rule`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another rule, it is
        reassigned to the given rule ``Id``.

        :param rule_id: the ``Id`` of a ``Rule``
        :type rule_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``rule_id`` not found
        :raise: ``NullArgument`` -- ``rule_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class RuleNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Rule`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    """
    def get_engine_id(self):
        """Gets the ``Engine``  ``Id`` associated with this session.

        :return: the ``Engine Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    engine_id = property(fget=get_engine_id)

    def get_engine(self):
        """Gets the ``Engine`` associated with this session.

        :return: the ``Engine`` associated with this session
        :rtype: ``osid.rules.Engine``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Engine

    engine = property(fget=get_engine)

    def can_register_for_rule_notifications(self):
        """Tests if this user can register for ``Rule`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_federated_engine_view(self):
        """Federates the view for methods in this session.

        A federated view will include notifications for rules in engines
        which are children of this engine in the engine hierarchy.



        """
        pass

    def use_isolated_engine_view(self):
        """Isolates the view for methods in this session.

        An isolated view restricts notifications to this engine only.



        """
        pass

    def register_for_new_rules(self):
        """Register for notifications of new rules.

        ``RuleReceiver.newRule()`` is invoked when a new ``Rule`` is
        created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_rules(self):
        """Registers for notification of updated rules.

        ``RuleReceiver.changedRule()`` is invoked when a rule is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_rule(self, rule_id):
        """Registers for notification of an updated rule.

        ``RuleReceiver.changedRule()`` is invoked when the specified
        rule is changed.

        :param rule_id: the ``Id`` of the ``Rule`` to monitor
        :type rule_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_rules(self):
        """Registers for notification of deleted rules.

        ``RuleReceiver.deletedRule()`` is invoked when a rule is removed
        from this engine.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_rule(self, rule_id):
        """Registers for notification of a deleted rule.

        ``RuleReceiver.deletedRule()`` is invoked when the specified
        rule is removed from this engine.

        :param rule_id: the ``Id`` of the ``Rule`` to monitor
        :type rule_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class RuleEngineSession(osid_sessions.OsidSession):
    """This session provides methods to retrieve ``Rule`` to ``Engine`` mappings.

    A ``Rule`` may appear in multiple ``Engine`` objects. Each engine
    may have its own authorizations governing who is allowed to look at
    it.

    This lookup session defines several views:
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete result set or is an error
        condition


    """
    def can_lookup_rule_engine_mappings(self):
        """Tests if this user can perform lookups of rule/engine mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known lookup methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        lookup operations to unauthorized users.

        :return: ``false`` if looking up mappings is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_rule_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_rule_view(self):
        """A complete view of the ``Rule`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_rule_ids_by_engine(self, engine_id):
        """Gets the list of ``Rule Ids`` associated with an ``Engine``.

        :param engine_id: ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: list of related rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_rules_by_engine(self, engine_id):
        """Gets the list of ``Rules`` associated with an ``Engine``.

        :param engine_id: ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: list of related rules
        :rtype: ``osid.rules.RuleList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.RuleList

    def get_rule_ids_by_engines(self, engine_ids):
        """Gets the list of ``Rule Ids`` corresponding to a list of ``Engine`` objects.

        :param engine_ids: list of engine ``Ids``
        :type engine_ids: ``osid.id.IdList``
        :return: list of rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``engine_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_rules_by_engines(self, engine_ids):
        """Gets the list of ``Rules`` corresponding to a list of ``Engine`` objects.

        :param engine_ids: list of engine ``Ids``
        :type engine_ids: ``osid.id.IdList``
        :return: list of rules
        :rtype: ``osid.rules.RuleList``
        :raise: ``NullArgument`` -- ``engine_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.RuleList

    def get_engine_ids_by_rule(self, rule_id):
        """Gets the ``Engine``  ``Ids`` mapped to a ``Rule``.

        :param rule_id: ``Id`` of a ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: list of engines
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``rule_id`` is not found
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_engines_by_rule(self, rule_id):
        """Gets the ``Engine`` objects mapped to a ``Rule``.

        :param rule_id: ``Id`` of a ``Rule``
        :type rule_id: ``osid.id.Id``
        :return: list of engines
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- ``rule_id`` is not found
        :raise: ``NullArgument`` -- ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList


class RuleEngineAssignmentSession(osid_sessions.OsidSession):
    """This session provides methods to re-assign ``TerRulesms`` to ``Engine`` objects A ``Rule`` may appear in multiple ``Engine`` objects and removing the last reference to a ``Rule`` is the equivalent of deleting it.

    Each ``Rule`` may have its own authorizations governing who is
    allowed to operate on it.

    Adding a reference of a ``Rule`` to another ``Engine`` is not a copy
    operation (eg: does not change its ``Id`` ).

    """
    def can_assign_rules(self):
        """Tests if this user can alter rule/engine mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_assign_rules_to_engine(self, engine_id):
        """Tests if this user can alter rule/engine mappings.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known mapping methods in
        this session will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may opt not to offer
        assignment operations to unauthorized users.

        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: ``false`` if mapping is not authorized, ``true`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``

        """
        return # boolean

    def get_assignable_engine_ids(self, engine_id):
        """Gets a list of engines including and under the given engine node in which any rule can be assigned.

        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: list of assignable rule ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def get_assignable_engine_ids_for_rule(self, engine_id, rule_id):
        """Gets a list of engines including and under the given engine node in which a specific rule can be assigned.

        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :param rule_id: the ``Id`` of the ``Engine``
        :type rule_id: ``osid.id.Id``
        :return: list of assignable engine ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``NullArgument`` -- ``engine_id`` or ``rule_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.IdList

    def assign_rule_to_engine(self, rule_id, engine_id):
        """Adds an existing ``Rule`` to an ``Engine``.

        :param rule_id: the ``Id`` of the ``Rule``
        :type rule_id: ``osid.id.Id``
        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``rule_id`` is already assigned to ``engine_id``
        :raise: ``NotFound`` -- ``rule_id`` or ``engine_id`` not found
        :raise: ``NullArgument`` -- ``rule_id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def unassign_rule_from_engine(self, rule_id, engine_id):
        """Removes a ``Rule`` from an ``Engine``.

        :param rule_id: the ``Id`` of the ``Rule``
        :type rule_id: ``osid.id.Id``
        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``rule_id`` or ``engine_id`` not found or ``rule_id`` not assigned to ``engine_id``
        :raise: ``NullArgument`` -- ``rule_id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class RuleSmartEngineSession(osid_sessions.OsidSession):
    """This session manages queries and sequencing to create "smart" dynamic catalogs.

    A ``RuleQuery`` can be retrieved from this session and mapped to
    this ``Engine`` to create a virtual collection of ``Rules``. The
    rules may be sequenced using the ``RuleSearchOrder`` from this
    session.

    This ``Engine`` has a default query that matches any rule and a
    default search order that specifies no sequencing. The queries may
    be examined using a ``RuleQueryInspector``. The query may be
    modified by converting the inspector back to a ``RuleQuery``.

    """
    def get_engine_id(self):
        """Gets the ``Engine``  ``Id`` associated with this session.

        :return: the ``Engine Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    engine_id = property(fget=get_engine_id)

    def get_engine(self):
        """Gets the ``Engine`` associated with this session.

        :return: the ``Engine`` associated with this session
        :rtype: ``osid.rules.Engine``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Engine

    engine = property(fget=get_engine)

    def can_manage_smart_engines(self):
        """Tests if this user can manage smart engines.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer operations
        to unauthorized users.

        :return: ``false`` if smart engine management is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_rule_query(self):
        """Gets a rule query.

        :return: the rule query
        :rtype: ``osid.rules.RuleQuery``

        """
        return # osid.rules.RuleQuery

    rule_query = property(fget=get_rule_query)

    def get_rule_search_order(self):
        """Gets a rule search order.

        :return: the rule search order
        :rtype: ``osid.rules.RuleSearchOrder``

        """
        return # osid.rules.RuleSearchOrder

    rule_search_order = property(fget=get_rule_search_order)

    def apply_rule_query(self, rule_query):
        """Applies a rule query to this engine.

        :param rule_query: the rule query
        :type rule_query: ``osid.rules.RuleQuery``
        :raise: ``NullArgument`` -- ``rule_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``rule_query`` not of this service

        """
        pass

    def inspect_rule_query(self):
        """Gets a rule query inspector for this engine.

        :return: the rule query inspector
        :rtype: ``osid.rules.RuleQueryInspector``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred

        """
        return # osid.rules.RuleQueryInspector

    def apply_rule_sequencing(self, rule_search_order):
        """Applies a rule search order to this engine.

        :param rule_search_order: the rule search order
        :type rule_search_order: ``osid.rules.RuleSearchOrder``
        :raise: ``NullArgument`` -- ``rule_search_order`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure occurred
        :raise: ``Unsupported`` -- ``rule_search_order`` not of this service

        """
        pass

    def get_rule_query_from_inspector(self, rule_query_inspector):
        """Gets a rule query from an inspector.

        :param rule_query_inspector: a rule query inspector
        :type rule_query_inspector: ``osid.rules.RuleQueryInspector``
        :return: the rule query
        :rtype: ``osid.rules.RuleQuery``
        :raise: ``NullArgument`` -- ``rule_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``rule_query_inspector`` is not of this service

        """
        return # osid.rules.RuleQuery


class EngineLookupSession(osid_sessions.OsidSession):
    """This session provides methods for retrieving ``Engine`` objects.

    The ``Engine`` represents a collection of rules.

    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: elements may be silently omitted or re-ordered
      * plenary view: provides a complete set or is an error condition

    
    Generally, the comparative view should be used for most applications
    as it permits operation even if there is data that cannot be
    accessed. For example, a browsing application may only need to
    examine the ``Engines`` it can access, without breaking execution.
    However, an assessment may only be useful if all ``Engines``
    referenced by it are available, and a test-taking applicationmay
    sacrifice some interoperability for the sake of precision.

    """
    def can_lookup_engines(self):
        """Tests if this user can perform ``Engine`` lookups.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may not offer lookup operations
        to unauthorized users.

        :return: ``false`` if lookup methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_engine_view(self):
        """The returns from the lookup methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_engine_view(self):
        """A complete view of the ``Engine`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_engine(self, engine_id):
        """Gets the ``Engine`` specified by its ``Id``.

        In plenary mode, the exact ``Id`` is found or a ``NotFound``
        results. Otherwise, the returned ``Engine`` may have a different
        ``Id`` than requested, such as the case where a duplicate ``Id``
        was assigned to an ``Engine`` and retained for compatibility.

        :param engine_id: ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: the engine
        :rtype: ``osid.rules.Engine``
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.Engine

    def get_engines_by_ids(self, engine_ids):
        """Gets an ``EngineList`` corresponding to the given ``IdList``.

        In plenary mode, the returned list contains all of the engines
        specified in the ``Id`` list, in the order of the list,
        including duplicates, or an error results if an ``Id`` in the
        supplied list is not found or inaccessible. Otherwise,
        inaccessible ``Engines`` may be omitted from the list and may
        present the elements in any order including returning a unique
        set.

        :param engine_ids: the list of ``Ids`` to retrieve
        :type engine_ids: ``osid.id.IdList``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Id`` was not found
        :raise: ``NullArgument`` -- ``engine_ids`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    def get_engines_by_genus_type(self, engine_genus_type):
        """Gets an ``EngineList`` corresponding to the given engine genus ``Type`` which does not include engines of genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :param engine_genus_type: an engine genus type
        :type engine_genus_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    def get_engines_by_parent_genus_type(self, engine_genus_type):
        """Gets an ``EngineList`` corresponding to the given engine genus ``Type`` and include any additional engines with genus types derived from the specified ``Type``.

        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :param engine_genus_type: an engine genus type
        :type engine_genus_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_genus_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    def get_engines_by_record_type(self, engine_record_type):
        """Gets an ``EngineList`` containing the given repository record ``Type``.

        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :param engine_record_type: a engine record type
        :type engine_record_type: ``osid.type.Type``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_record_type`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    def get_engines_by_provider(self, resource_id):
        """Gets an ``EngineList`` from the given provider.

        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :param resource_id: a resource ``Id``
        :type resource_id: ``osid.id.Id``
        :return: the returned ``Engine`` list
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``resource_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    def get_engines(self):
        """Gets all ``Engines``.

        In plenary mode, the returned list contains all known engines or
        an error results. Otherwise, the returned list may contain only
        those engines that are accessible through this session.

        :return: a list of ``Engines``
        :rtype: ``osid.rules.EngineList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    engines = property(fget=get_engines)


class EngineQuerySession(osid_sessions.OsidSession):
    """This session provides methods for searching ``Engine`` objects.

    The search query is constructed using the ``EngineQuery``. The
    engine record ``Type`` also specifies the record for the engine
    query.

    Engines may have an engine query record indicated by their
    respective record types. The engine query record is accessed via the
    ``EngineQuery``. The returns in this session may not be cast
    directly to these interfaces.

    """
    def can_search_engines(self):
        """Tests if this user can perform ``Engine`` searches.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer search
        operations to unauthorized users.

        :return: ``false`` if search methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_engine_query(self):
        """Gets an engine query.

        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``

        """
        return # osid.rules.EngineQuery

    engine_query = property(fget=get_engine_query)

    def get_engines_by_query(self, engine_query):
        """Gets a list of ``Engines`` matching the given search.

        :param engine_query: the engine query
        :type engine_query: ``osid.rules.EngineQuery``
        :return: the returned ``EngineList``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NullArgument`` -- ``engine_query`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_query`` is not of this service

        """
        return # osid.rules.EngineList


class EngineSearchSession(EngineQuerySession):
    """This session provides methods for searching ``Engine`` objects.

    The search query is constructed using the ``EngineQuery``. The
    engine record ``Type`` also specifies the recod for the engine
    query.

    ``get_engines_by_query()`` is the basic search method and returns a
    list of ``Engine`` elements. A more advanced search may be performed
    with ``getEnginesBySearch()``. It accepts an ``EngineSearch`` in
    addition to the query for the purpose of specifying additional
    options affecting the entire search, such as ordering.
    ``get_engines_by_search()`` returns a ``EngineSearchResults`` that
    can be used to access the resulting ``EngineList`` or be used to
    perform a search within the result set through ``EngineSearch``.
    
    Engines may have an engine query record indicated by their
    respective record types. The engine query record is accessed via the
    ``EngineQuery``. The returns in this session may not be cast
    directly to these interfaces.

    """
    def get_engine_search(self):
        """Gets an engine search.

        :return: the engine search
        :rtype: ``osid.rules.EngineSearch``

        """
        return # osid.rules.EngineSearch

    engine_search = property(fget=get_engine_search)

    def get_engine_search_order(self):
        """Gets an engine search order.

        The ``EngineSearchOrder`` is supplied to a ``EngineSearch`` to
        specify the ordering of results.

        :return: the engine search order
        :rtype: ``osid.rules.EngineSearchOrder``

        """
        return # osid.rules.EngineSearchOrder

    engine_search_order = property(fget=get_engine_search_order)

    def get_engines_by_search(self, engine_query, engine_search):
        """Gets the search results matching the given search.

        :param engine_query: the engine query
        :type engine_query: ``osid.rules.EngineQuery``
        :param engine_search: the engine search
        :type engine_search: ``osid.rules.EngineSearch``
        :return: the engine search results
        :rtype: ``osid.rules.EngineSearchResults``
        :raise: ``NullArgument`` -- ``engine_query`` or ``engine_search`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_query`` or ``engine_search`` is not of this service

        """
        return # osid.rules.EngineSearchResults

    def get_engine_query_from_inspector(self, engine_query_inspector):
        """Gets an engine query from an inspector.

        The inspector is available from a ``EngineSearchResults``.

        :param engine_query_inspector: an engine query inspector
        :type engine_query_inspector: ``osid.rules.EngineQueryInspector``
        :return: the engine query
        :rtype: ``osid.rules.EngineQuery``
        :raise: ``NullArgument`` -- ``engine_query_inspector`` is ``null``
        :raise: ``Unsupported`` -- ``engine_query_inspector`` is not of this service

        """
        return # osid.rules.EngineQuery


class EngineAdminSession(osid_sessions.OsidSession):
    """This session creates, updates, and deletes ``Engines``.

    The data for create and update is provided by the consumer via the
    form object. ``OsidForms`` are requested for each create or update
    and may not be reused.

    Create and update operations differ in their usage. To create an
    ``Engine,`` an ``EngineForm`` is requested using
    ``get_engine_form_for_create()`` specifying the desired record
    ``Types`` or none if no record ``Types`` are needed. The returned
    ``EngineForm`` will indicate that it is to be used with a create
    operation and can be used to examine metdata or validate data prior
    to creation. Once the ``EngineForm`` is submiited to a create
    operation, it cannot be reused with another create operation unless
    the first operation was unsuccessful. Each ``EngineForm``
    corresponds to an attempted transaction.
    
    For updates, ``EngineForms`` are requested to the ``Engine``  ``Id``
    that is to be updated using ``getEngineFormForUpdate()``. Similarly,
    the ``EngineForm`` has metadata about the data that can be updated
    and it can perform validation before submitting the update. The
    ``EngineForm`` can only be used once for a successful update and
    cannot be reused.
    
    The delete operations delete ``Engines``. It is safer to remove all
    mappings to the ``Engine`` catalogs before deletion.
    
    This session includes an ``Id`` aliasing mechanism to assign an
    external ``Id`` to an internally assigned Id.

    """
    def can_create_engines(self):
        """Tests if this user can create ``Engines``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known creating an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        create operations to unauthorized users.

        :return: ``false`` if ``Engine`` creation is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def can_create_engine_with_record_types(self, engine_record_types):
        """Tests if this user can create a single ``Engine`` using the desired record interface types.

        While ``RulesManager.getEngineRecordTypes()`` can be used to
        examine which record interfaces are supported, this method tests
        which record(s) are required for creating a specific ``Engine``.
        Providing an empty array tests if an ``Engine`` can be created
        with no records.

        :param engine_record_types: array of engine record types
        :type engine_record_types: ``osid.type.Type[]``
        :return: ``true`` if ``Engine`` creation using the specified record ``Types`` is supported, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NullArgument`` -- ``engine_record_types`` is ``null``

        """
        return # boolean

    def get_engine_form_for_create(self, engine_record_types):
        """Gets the engine form for creating new engines.

        A new form should be requested for each create transaction.

        :param engine_record_types: array of engine record types
        :type engine_record_types: ``osid.type.Type[]``
        :return: the engine form
        :rtype: ``osid.rules.EngineForm``
        :raise: ``NullArgument`` -- ``engine_record_types`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- unable to get form with requested record types

        """
        return # osid.rules.EngineForm

    def create_engine(self, engine_form):
        """Creates a new ``Engine``.

        :param engine_form: the form for this ``Engine``
        :type engine_form: ``osid.rules.EngineForm``
        :return: the new ``Engine``
        :rtype: ``osid.rules.Engine``
        :raise: ``IllegalState`` -- ``engine_form`` already used in a create transaction
        :raise: ``InvalidArgument`` -- one or more of the form elements is invalid
        :raise: ``NullArgument`` -- ``engine_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_form`` did not originate from ``get_engine_form_for_create()``

        """
        return # osid.rules.Engine

    def can_update_engines(self):
        """Tests if this user can update ``Engines``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known updating an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        update operations to unauthorized users.

        :return: ``false`` if ``Engine`` modification is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_engine_form_for_update(self, engine_id):
        """Gets the engine form for updating an existing engine.

        A new engine form should be requested for each update
        transaction.

        :param engine_id: the ``Id`` of the ``Engine``
        :type engine_id: ``osid.id.Id``
        :return: the engine form
        :rtype: ``osid.rules.EngineForm``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineForm

    def update_engine(self, engine_form):
        """Updates an existing engine.

        :param engine_form: the form containing the elements to be updated
        :type engine_form: ``osid.rules.EngineForm``
        :raise: ``IllegalState`` -- ``engine_form`` already used in an update transaction
        :raise: ``InvalidArgument`` -- the form contains an invalid value
        :raise: ``NullArgument`` -- ``engine_form`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure
        :raise: ``Unsupported`` -- ``engine_form`` did not originate from ``get_engine_form_for_update()``

        """
        pass

    def can_delete_engines(self):
        """Tests if this user can delete ``Engines``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known deleting an
        ``Engine`` will result in a ``PermissionDenied``. This is
        intended as a hint to an application that may not wish to offer
        delete operations to unauthorized users.

        :return: ``false`` if ``Engine`` deletion is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def delete_engine(self, engine_id):
        """Deletes an ``Engine``.

        :param engine_id: the ``Id`` of the ``Engine`` to remove
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def can_manage_engine_aliases(self):
        """Tests if this user can manage ``Id`` aliases for ``Engines``.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known changing an alias
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer alias
        operations to an unauthorized user.

        :return: ``false`` if ``Engine`` aliasing is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def alias_engine(self, engine_id, alias_id):
        """Adds an ``Id`` to an ``Engine`` for the purpose of creating compatibility.

        The primary ``Id`` of the ``Engine`` is determined by the
        provider. The new ``Id`` performs as an alias to the primary
        ``Id``. If the alias is a pointer to another engine it is
        reassigned to the given engine ``Id``.

        :param engine_id: the ``Id`` of an ``Engine``
        :type engine_id: ``osid.id.Id``
        :param alias_id: the alias ``Id``
        :type alias_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``alias_id`` is already assigned
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` or ``alias_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class EngineNotificationSession(osid_sessions.OsidSession):
    """This session defines methods to receive notifications on adds/changes to ``Engine`` objects.

    This session is intended for consumers needing to synchronize their
    state with this service without the use of polling. Notifications
    are cancelled when this session is closed.

    Notifications are triggered with changes to the ``Engine`` object
    itself. Adding and removing rules result in notifications available
    from the notification session for rules.

    """
    def can_register_for_engine_notifications(self):
        """Tests if this user can register for ``Engine`` notifications.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an application that may opt not to offer
        notification operations.

        :return: ``false`` if notification methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def register_for_new_engines(self):
        """Register for notifications of new engines.

        ``EngineReceiver.newEngine()`` is invoked when a new ``Engine``
        is created.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_engine_ancestors(self, engine_id):
        """Registers for notification of an updated hierarchy structure that introduces a new ancestor of the specified engine.

        ``EngineReceiver.newAncestorEngine()`` is invoked when the
        specified engine node gets a new ancestor.

        :param engine_id: the ``Id`` of the ``Engine`` node to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_new_engine_descendants(self, engine_id):
        """Registers for notification of an updated hierarchy structure that introduces a new descendant of the specified engine.

        ``EngineReceiver.newDescendantEngine()`` is invoked when the
        specified engine node gets a new descendant.

        :param engine_id: the ``Id`` of the ``Engine`` node to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_engines(self):
        """Registers for notification of updated engines.

        ``EngineReceiver.changedEngine()`` is invoked when an engine is
        changed.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_changed_engine(self, engine_id):
        """Registers for notification of an updated engine.

        ``EngineReceiver.changedEngine()`` is invoked when the specified
        engine is changed.

        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_engines(self):
        """Registers for notification of deleted engines.

        ``EngineReceiver.deletedEngine()`` is invoked when an engine is
        deleted.

        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_engine(self, engine_id):
        """Registers for notification of a deleted engine.

        ``EngineReceiver.deletedEngine()`` is invoked when the specified
        engine is deleted.

        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_engine_ancestors(self, engine_id):
        """Registers for notification of an updated hierarchy structure that removes an ancestor of the specified engine.

        ``EngineReceiver.deletedAncestor()`` is invoked when the
        specified engine node loses an ancestor.

        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def register_for_deleted_engine_descendants(self, engine_id):
        """Registers for notification of an updated hierarchy structure that removes a descendant of the specified engine.

        ``EngineReceiver.deletedDescendant()`` is invoked when the
        specified engine node loses a descendant.

        :param engine_id: the ``Id`` of the ``Engine`` to monitor
        :type engine_id: ``osid.id.Id``
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


class EngineHierarchySession(osid_sessions.OsidSession):
    """This session defines methods for traversing a hierarchy of ``Engine`` objects.

    Each node in the hierarchy is a unique ``Engine``. The hierarchy may
    be traversed recursively to establish the tree structure through
    ``get_parent_engines()`` and ``getChildEngines()``. To relate these
    ``Ids`` to another OSID, ``get_engien_nodes()`` can be used for
    retrievals that can be used for bulk lookups in other OSIDs. Any
    ``Engine`` available in the Rule OSID is known to this hierarchy but
    does not appear in the hierarchy traversal until added as a root
    node or a child of another node.

    A user may not be authorized to traverse the entire hierarchy. Parts
    of the hierarchy may be made invisible through omission from the
    returns of ``get_parent_engines()`` or ``get_child_engines()`` in
    lieu of a ``PermissionDenied`` error that may disrupt the traversal
    through authorized pathways.
    
    This session defines views that offer differing behaviors when
    retrieving multiple objects.
    
      * comparative view: engine elements may be silently omitted or re-
        ordered
      * plenary view: provides a complete set or is an error condition


    """
    def get_engine_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    engine_hierarchy_id = property(fget=get_engine_hierarchy_id)

    def get_engine_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    engine_hierarchy = property(fget=get_engine_hierarchy)

    def can_access_engine_hierarchy(self):
        """Tests if this user can perform hierarchy queries.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known all methods in this
        session will result in a ``PermissionDenied``. This is intended
        as a hint to an an application that may wish not to offer
        traversal operations to unauthorized users.

        :return: ``false`` if hierarchy traversal methods are not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def use_comparative_engine_view(self):
        """The returns from the engine methods may omit or translate elements based on this session, such as authorization, and not result in an error.

        This view is used when greater interoperability is desired at
        the expense of precision.



        """
        pass

    def use_plenary_engine_view(self):
        """A complete view of the ``Engine`` returns is desired.

        Methods will return what is requested or result in an error.
        This view is used when greater precision is desired at the
        expense of interoperability.



        """
        pass

    def get_root_engine_ids(self):
        """Gets the root engine ``Ids`` in this hierarchy.

        :return: the root engine ``Ids``
        :rtype: ``osid.id.IdList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    root_engine_ids = property(fget=get_root_engine_ids)

    def get_root_engines(self):
        """Gets the root engines in this engine hierarchy.

        :return: the root engines
        :rtype: ``osid.rules.EngineList``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    root_engines = property(fget=get_root_engines)

    def has_parent_engines(self, engine_id):
        """Tests if the ``Engine`` has any parents.

        :param engine_id: the ``Id`` of a engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the engine has parents, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_parent_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is a direct parent of an engine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an egine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is a parent of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_parent_engine_ids(self, engine_id):
        """Gets the parent ``Ids`` of the given engine.

        :param engine_id: the ``Id`` of an egine
        :type engine_id: ``osid.id.Id``
        :return: the parent ``Ids`` of the engine
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_parent_engines(self, engine_id):
        """Gets the parent engines of the given ``id``.

        :param engine_id: the ``Id`` of the ``Engine`` to query
        :type engine_id: ``osid.id.Id``
        :return: the parent engines of the ``id``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Engine`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    def is_ancestor_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is an ancestor of an engine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if this ``id`` is an ancestor of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def has_child_engines(self, engine_id):
        """Tests if an engine has any children.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``engine_id`` has children, ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def is_child_of_engine(self, id_, engine_id):
        """Tests if an engine is a direct child of another.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a child of ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_child_engine_ids(self, engine_id):
        """Gets the child ``Ids`` of the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :return: the children of the engine
        :rtype: ``osid.id.IdList``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.id.IdList

    def get_child_engines(self, engine_id):
        """Gets the child engines of the given ``id``.

        :param engine_id: the ``Id`` of the ``Engine`` to query
        :type engine_id: ``osid.id.Id``
        :return: the child engines of the ``id``
        :rtype: ``osid.rules.EngineList``
        :raise: ``NotFound`` -- an ``Engine`` identified by ``Id is`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineList

    def is_descendant_of_engine(self, id_, engine_id):
        """Tests if an ``Id`` is a descendant of an egine.

        :param id: an ``Id``
        :type id: ``osid.id.Id``
        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :return: ``true`` if the ``id`` is a descendant of the ``engine_id,``  ``false`` otherwise
        :rtype: ``boolean``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``id`` or ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # boolean

    def get_engine_node_ids(self, engine_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an engine node
        :rtype: ``osid.hierarchy.Node``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Node

    def get_engine_nodes(self, engine_id, ancestor_levels, descendant_levels, include_siblings):
        """Gets a portion of the hierarchy for the given engine.

        :param engine_id: the ``Id`` to query
        :type engine_id: ``osid.id.Id``
        :param ancestor_levels: the maximum number of ancestor levels to include. A value of 0 returns no parents in the node.
        :type ancestor_levels: ``cardinal``
        :param descendant_levels: the maximum number of descendant levels to include. A value of 0 returns no children in the node.
        :type descendant_levels: ``cardinal``
        :param include_siblings: ``true`` to include the siblings of the given node, ``false`` to omit the siblings
        :type include_siblings: ``boolean``
        :return: an engine node
        :rtype: ``osid.rules.EngineNode``
        :raise: ``NotFound`` -- ``engine_id`` is not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.rules.EngineNode


class EngineHierarchyDesignSession(osid_sessions.OsidSession):
    """This session manages a hierarchy of engines.

    Engines may be organized into a hierarchy for organizing or
    federating. A parent ``Engine`` includes all of the rules of its
    children such that a single root node contains all of the rules of
    the federation.

    """
    def get_engine_hierarchy_id(self):
        """Gets the hierarchy ``Id`` associated with this session.

        :return: the hierarchy ``Id`` associated with this session
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    engine_hierarchy_id = property(fget=get_engine_hierarchy_id)

    def get_engine_hierarchy(self):
        """Gets the hierarchy associated with this session.

        :return: the hierarchy associated with this session
        :rtype: ``osid.hierarchy.Hierarchy``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        return # osid.hierarchy.Hierarchy

    engine_hierarchy = property(fget=get_engine_hierarchy)

    def can_modify_engine_hierarchy(self):
        """Tests if this user can change the hierarchy.

        A return of true does not guarantee successful authorization. A
        return of false indicates that it is known performing any update
        will result in a ``PermissionDenied``. This is intended as a
        hint to an application that may opt not to offer these
        operations to an unauthorized user.

        :return: ``false`` if changing this hierarchy is not authorized, ``true`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def add_root_engine(self, engine_id):
        """Adds a root engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``engine_id`` is already in hierarchy
        :raise: ``NotFound`` -- ``engine_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_root_engine(self, engine_id):
        """Removes a root engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not a root
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def add_child_engine(self, engine_id, child_id):
        """Adds a child to an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``AlreadyExists`` -- ``engine_id`` is already a parent of ``child_id``
        :raise: ``NotFound`` -- ``engine_id`` or ``child_id`` not found
        :raise: ``NullArgument`` -- ``engine_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_engine(self, engine_id, child_id):
        """Removes a child from an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :param child_id: the ``Id`` of the new child
        :type child_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not a parent of ``child_id``
        :raise: ``NullArgument`` -- ``engine_id`` or ``child_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass

    def remove_child_engines(self, engine_id):
        """Removes all children from an engine.

        :param engine_id: the ``Id`` of an engine
        :type engine_id: ``osid.id.Id``
        :raise: ``NotFound`` -- ``engine_id`` not in hierarchy
        :raise: ``NullArgument`` -- ``engine_id`` is ``null``
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``PermissionDenied`` -- authorization failure

        """
        pass


