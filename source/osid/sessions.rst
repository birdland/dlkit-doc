

Sessions
========


Osid Session
------------

.. py:class:: OsidSession(abc_osid_sessions.OsidSession)
    The ``OsidSession`` is the top level interface for all OSID sessions.


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





    .. py:method:: get_locale():
        :noindex:


    .. py:attribute:: locale
        :noindex:


    .. py:method:: is_authenticated():
        :noindex:


    .. py:method:: get_authenticated_agent_id():
        :noindex:


    .. py:attribute:: authenticated_agent_id
        :noindex:


    .. py:method:: get_authenticated_agent():
        :noindex:


    .. py:attribute:: authenticated_agent
        :noindex:


    .. py:method:: get_effective_agent_id():
        :noindex:


    .. py:attribute:: effective_agent_id
        :noindex:


    .. py:method:: get_effective_agent():
        :noindex:


    .. py:attribute:: effective_agent
        :noindex:


    .. py:method:: get_date():
        :noindex:


    .. py:attribute:: date
        :noindex:


    .. py:method:: get_clock_rate():
        :noindex:


    .. py:attribute:: clock_rate
        :noindex:


    .. py:method:: get_format_type():
        :noindex:


    .. py:attribute:: format_type
        :noindex:


    .. py:method:: supports_transactions():
        :noindex:


    .. py:method:: start_transaction():
        :noindex:


