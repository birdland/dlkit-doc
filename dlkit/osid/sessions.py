


class OsidSession:
    """The ``OsidSession`` is the top level interface for all OSID sessions.

    An ``OsidSession`` is created through its corresponding
    ``OsidManager``. A new ``OsidSession`` should be created for each
    user of a service and for each processing thread. A session
    maintains a single authenticated user and is not required to ensure
    thread-protection. A typical OSID session defines a set of service
    methods corresponding to some compliance level as defined by the
    service and is generally responsible for the management and
    retrieval of ``OsidObjects``.

    ``OsidSession`` defines a set of common methods used throughout all
    OSID sessions. An OSID session may optionally support transactions
    through the transaction interface.

    """
    def get_locale(self):
        """Gets the locale indicating the localization preferences in effect for this session.

        :return: the locale
        :rtype: ``osid.locale.Locale``

        """
        return # osid.locale.Locale

    locale = property(fget=get_locale)

    def is_authenticated(self):
        """Tests if an agent is authenticated to this session.

        :return: ``true`` if valid authentication credentials exist, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def get_authenticated_agent_id(self):
        """Gets the ``Id`` of the agent authenticated to this session.

        This is the agent for which credentials are used either acquired
        natively or via an ``OsidProxyManager``.

        :return: the authenticated agent ``Id``
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- ``is_authenticated()`` is ``false``

        """
        return # osid.id.Id

    authenticated_agent_id = property(fget=get_authenticated_agent_id)

    def get_authenticated_agent(self):
        """Gets the agent authenticated to this session.

        This is the agent for which credentials are used either acquired
        natively or via an ``OsidProxyManager``.

        :return: the authenticated agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``IllegalState`` -- ``is_authenticated()`` is ``false``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.authentication.Agent

    authenticated_agent = property(fget=get_authenticated_agent)

    def get_effective_agent_id(self):
        """Gets the ``Id`` of the effective agent in use by this session.

        If ``is_authenticated()`` is true, then the effective agent may
        be the same as the agent returned by
        ``getAuthenticatedAgent()``. If ``is_authenticated()`` is
        ``false,`` then the effective agent may be a default agent used
        for authorization by an unknwon or anonymous user.

        :return: the effective agent
        :rtype: ``osid.id.Id``

        """
        return # osid.id.Id

    effective_agent_id = property(fget=get_effective_agent_id)

    def get_effective_agent(self):
        """Gets the effective agent in use by this session.

        If ``is_authenticated()`` is true, then the effective agent may
        be the same as the agent returned by
        ``getAuthenticatedAgent()``. If ``is_authenticated()`` is
        ``false,`` then the effective agent may be a default agent used
        for authorization by an unknwon or anonymous user.

        :return: the effective agent
        :rtype: ``osid.authentication.Agent``
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.authentication.Agent

    effective_agent = property(fget=get_effective_agent)

    def get_date(self):
        """Gets the service date which may be the current date or the effective date in which this session exists.

        :return: the service date
        :rtype: ``timestamp``

        """
        return # timestamp

    date = property(fget=get_date)

    def get_clock_rate(self):
        """Gets the rate of the service clock.

        :return: the clock rate
        :rtype: ``decimal``

        """
        return # decimal

    clock_rate = property(fget=get_clock_rate)

    def get_format_type(self):
        """Gets the ``DisplayText`` format ``Type`` preference in effect for this session.

        :return: the effective ``DisplayText`` format ``Type``
        :rtype: ``osid.type.Type``

        """
        return # osid.type.Type

    format_type = property(fget=get_format_type)

    def supports_transactions(self):
        """Tests for the availability of transactions.

        :return: ``true`` if transaction methods are available, ``false`` otherwise
        :rtype: ``boolean``

        """
        return # boolean

    def start_transaction(self):
        """Starts a new transaction for this sesson.

        Transactions are a means for an OSID to provide an all-or-
        nothing set of operations within a session and may be used to
        coordinate this service from an external transaction manager. A
        session supports one transaction at a time. Starting a second
        transaction before the previous has been committed or aborted
        results in an ``IllegalState`` error.

        :return: a new transaction
        :rtype: ``osid.transaction.Transaction``
        :raise: ``IllegalState`` -- a transaction is already open
        :raise: ``OperationFailed`` -- unable to complete request
        :raise: ``Unsupported`` -- transactions not supported

        """
        return # osid.transaction.Transaction


