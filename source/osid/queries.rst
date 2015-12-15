

Queries
=======


Osid Query
----------

.. py:class:: OsidQuery(abc_osid_queries.OsidQuery, osid_markers.Suppliable)
    The ``OsidQuery`` is used to assemble search queries.


    An ``OsidQuery`` is available from an ``OsidQuerySession`` and
    defines methods to match objects. Once the desired parameters are
    set, the ``OsidQuery`` is given to the designated search method. The
    same ``OsidQuery`` returned from the session must be used in the
    search as the provider may utilize implementation-specific data
    wiithin the object.




    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.




    Any match method inside an ``OsidQuery`` may be invoked multiple
    times. In the case of a match method, each invocation adds an
    element to an ``OR`` expression. Any of these terms may also be
    negated through the ``match`` flag.
      OsidQuery { OsidQuery.matchDisplayName AND (OsidQuery.matchDescription OR
          OsidQuery.matchDescription)}












    ``OsidObjects`` allow for the definition of an additonal records and
    the ``OsidQuery`` parallels this mechanism. An interface type of an
    ``OsidObject`` record must also define the corresponding
    ``OsidQuery`` record which is available through query interfaces.
    Multiple requests of these typed interfaces may return the same
    underlying object and thus it is only useful to request once.




    An ``OsidQuery`` may be used to query for set or unset values using
    the "match any" methods. A field that has not bee explicitly
    assigned may default to a value. If multiple language translations
    exist and the query session is placed in a non-default locale,
    fields that have not been explicitly assigned in the non-default
    locale are considered unset even if the values from the default
    locale appear in the objects.





    .. py:method:: get_string_match_types():
        :noindex:


    .. py:attribute:: string_match_types
        :noindex:


    .. py:method:: supports_string_match_type(string_match_type):
        :noindex:


    .. py:method:: match_keyword(keyword, string_match_type=DEFAULT_STRING_MATCH_TYPE, match=True):
        :noindex:


    .. py:method:: clear_keyword_terms():
        :noindex:


    .. py:attribute:: keyword_terms
        :noindex:


    .. py:method:: match_any(match):
        :noindex:


    .. py:method:: clear_any_terms():
        :noindex:


    .. py:attribute:: any_terms
        :noindex:


Osid Identifiable Query
-----------------------

.. py:class:: OsidIdentifiableQuery(abc_osid_queries.OsidIdentifiableQuery, OsidQuery)
    The ``OsidIdentiableQuery`` is used to assemble search queries for ``Identifiable`` objects.


    An ``OsidIdentifiableQuery`` is available from an
    ``OsidQuerySession`` and defines methods to match objects. Once the
    desired parameters are set, the ``OsidIdentifiableQuery`` is given
    to the designated search method. The same ``OsidIdentifiableQuery``
    returned from the session must be used in the search as the provider
    may utilize implementation-specific data wiithin the object.




    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.





    .. py:method:: match_id(id_, match):
        :noindex:


    .. py:method:: clear_id_terms():
        :noindex:


    .. py:attribute:: id_terms
        :noindex:


Osid Extensible Query
---------------------

.. py:class:: OsidExtensibleQuery(abc_osid_queries.OsidExtensibleQuery, OsidQuery, osid_markers.Extensible)
    The ``OsidExtensibleQuery`` is used to assemble search queries for ``Extensible`` objects.


    An ``OsidExtensibleQuery`` is available from an ``OsidQuerySession``
    and defines methods to match objects. Once the desired parameters
    are set, the ``OsidExtensibleQuery`` is given to the designated
    search method. The same ``OsidExtensibleQuery`` returned from the
    session must be used in the search as the provider may utilize
    implementation-specific data wiithin the object.




    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.





    .. py:method:: match_record_type(record_type, match):
        :noindex:


    .. py:method:: match_any_record(match):
        :noindex:


    .. py:method:: clear_record_terms():
        :noindex:


    .. py:attribute:: record_terms
        :noindex:


Osid Browsable Query
--------------------

.. py:class:: OsidBrowsableQuery(abc_osid_queries.OsidBrowsableQuery, OsidQuery)
    The ``OsidBrowsableQuery`` is used to assemble search queries for ``Browsable`` objects.


    An ``OsidBrowsableQuery`` is available from an ``OsidQuerySession``
    and defines methods to match objects. Once the desired parameters
    are set, the ``OsidBrowsableQuery`` is given to the designated
    search method. The same ``OsidBrowsableQuery`` returned from the
    session must be used in the search as the provider may utilize
    implementation-specific data wiithin the object.




    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.







Osid Temporal Query
-------------------

.. py:class:: OsidTemporalQuery(abc_osid_queries.OsidTemporalQuery, OsidQuery)
    This is the query interface for searching temporal objects.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_effective(match):
        :noindex:


    .. py:method:: clear_effective_terms():
        :noindex:


    .. py:attribute:: effective_terms
        :noindex:


    .. py:method:: match_start_date(start, end, match):
        :noindex:


    .. py:method:: match_any_start_date(match):
        :noindex:


    .. py:method:: clear_start_date_terms():
        :noindex:


    .. py:attribute:: start_date_terms
        :noindex:


    .. py:method:: match_end_date(start, end, match):
        :noindex:


    .. py:method:: match_any_end_date(match):
        :noindex:


    .. py:method:: clear_end_date_terms():
        :noindex:


    .. py:attribute:: end_date_terms
        :noindex:


    .. py:method:: match_date(from_, to, match):
        :noindex:


    .. py:method:: clear_date_terms():
        :noindex:


    .. py:attribute:: date_terms
        :noindex:


Osid Subjugateable Query
------------------------

.. py:class:: OsidSubjugateableQuery(abc_osid_queries.OsidSubjugateableQuery, OsidQuery)
    The ``OsidSubjugateableQuery`` is used to assemble search queries for dependent objects.



Osid Aggregateable Query
------------------------

.. py:class:: OsidAggregateableQuery(abc_osid_queries.OsidAggregateableQuery, OsidQuery)
    The ``OsidAggregateableQuery`` is used to assemble search queries for assemblages.



Osid Containable Query
----------------------

.. py:class:: OsidContainableQuery(abc_osid_queries.OsidContainableQuery, OsidQuery)
    This is the query interface for searching containers.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_sequestered(match):
        :noindex:


    .. py:method:: clear_sequestered_terms():
        :noindex:


    .. py:attribute:: sequestered_terms
        :noindex:


Osid Sourceable Query
---------------------

.. py:class:: OsidSourceableQuery(abc_osid_queries.OsidSourceableQuery, OsidQuery)
    The ``OsidSourceableQuery`` is used to assemble search queries for sourceables.

    .. py:method:: match_provider_id(resource_id, match):
        :noindex:


    .. py:method:: clear_provider_id_terms():
        :noindex:


    .. py:attribute:: provider_id_terms
        :noindex:


    .. py:method:: supports_provider_query():
        :noindex:


    .. py:method:: get_provider_query(match):
        :noindex:


    .. py:method:: match_any_provider(match):
        :noindex:


    .. py:method:: clear_provider_terms():
        :noindex:


    .. py:attribute:: provider_terms
        :noindex:


    .. py:method:: match_branding_id(asset_id, match):
        :noindex:


    .. py:method:: clear_branding_id_terms():
        :noindex:


    .. py:attribute:: branding_id_terms
        :noindex:


    .. py:method:: supports_branding_query():
        :noindex:


    .. py:method:: get_branding_query(match):
        :noindex:


    .. py:method:: match_any_branding(match):
        :noindex:


    .. py:method:: clear_branding_terms():
        :noindex:


    .. py:attribute:: branding_terms
        :noindex:


    .. py:method:: match_license(license_, string_match_type, match):
        :noindex:


    .. py:method:: match_any_license(match):
        :noindex:


    .. py:method:: clear_license_terms():
        :noindex:


    .. py:attribute:: license_terms
        :noindex:


Osid Federateable Query
-----------------------

.. py:class:: OsidFederateableQuery(abc_osid_queries.OsidFederateableQuery, OsidQuery)
    The ``OsidFederateableQuery`` is used to assemble search queries for federated objects.



Osid Operable Query
-------------------

.. py:class:: OsidOperableQuery(abc_osid_queries.OsidOperableQuery, OsidQuery)
    This is the query interface for searching operables.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_active(match):
        :noindex:


    .. py:method:: clear_active_terms():
        :noindex:


    .. py:attribute:: active_terms
        :noindex:


    .. py:method:: match_enabled(match):
        :noindex:


    .. py:method:: clear_enabled_terms():
        :noindex:


    .. py:attribute:: enabled_terms
        :noindex:


    .. py:method:: match_disabled(match):
        :noindex:


    .. py:method:: clear_disabled_terms():
        :noindex:


    .. py:attribute:: disabled_terms
        :noindex:


    .. py:method:: match_operational(match):
        :noindex:


    .. py:method:: clear_operational_terms():
        :noindex:


    .. py:attribute:: operational_terms
        :noindex:


Osid Object Query
-----------------

.. py:class:: OsidObjectQuery(abc_osid_queries.OsidObjectQuery, OsidIdentifiableQuery, OsidExtensibleQuery, OsidBrowsableQuery)
    The ``OsidObjectQuery`` is used to assemble search queries.


    An ``OsidObjectQuery`` is available from an ``OsidSession`` and
    defines methods to query for an ``OsidObject`` that includes setting
    a display name and a description. Once the desired parameters are
    set, the ``OsidQuery`` is given to the designated search method. The
    same ``OsidQuery`` returned from the session must be used in the
    search as the provider may utilize implementation-specific data
    wiithin the object.




    If multiple data elements are set in this interface, the results
    matching all the given data (eg: AND) are returned.




    Any match method inside an ``OsidObjectQuery`` may be invoked
    multiple times. In the case of a match method, each invocation adds
    an element to an ``OR`` expression. Any of these terms may also be
    negated through the ``match`` flag.
      OsidObjectQuery { OsidQuery.matchDisplayName AND (OsidQuery.matchDescription OR
          OsidObjectQuery.matchDescription)}












    ``OsidObjects`` allow for the definition of an additonal records and
    the ``OsidQuery`` parallels this mechanism. An interface type of an
    ``OsidObject`` record must also define the corresponding
    ``OsidQuery`` record which is available through query interfaces.
    Multiple requests of these typed interfaces may return the same
    underlying object and thus it is only useful to request once.




    String searches are described using a string search ``Type`` that
    indicates the type of regular expression or wildcarding encoding.
    Compatibility with a strings search ``Type`` can be tested within
    this interface.




    As with all aspects of OSIDs, nulls cannot be used. Separate tests
    are available for querying for unset values except for required
    fields.




    An example to find all objects whose name starts with "Fred" or
    whose name starts with "Barney", but the word "dinosaur" does not
    appear in the description and not the color is not purple.
    ``ColorQuery`` is a record of the object that defines a color.
      ObjectObjectQuery query;
      query = session.getObjectQuery();
      query.matchDisplayName("Fred*", wildcardStringMatchType, true);
      query.matchDisplayName("Barney*", wildcardStringMatchType, true);
      query.matchDescriptionMatch("dinosaur", wordStringMatchType, false);




      ColorQuery recordQuery;
      recordQuery = query.getObjectRecord(colorRecordType);
      recordQuery.matchColor("purple", false);
      ObjectList list = session.getObjectsByQuery(query);









    .. py:method:: match_display_name(display_name, string_match_type=DEFAULT_STRING_MATCH_TYPE, match=True):
        :noindex:


    .. py:method:: match_any_display_name(match):
        :noindex:


    .. py:method:: clear_display_name_terms():
        :noindex:


    .. py:attribute:: display_name_terms
        :noindex:


    .. py:method:: match_description(description, string_match_type=DEFAULT_STRING_MATCH_TYPE, match=True):
        :noindex:


    .. py:method:: match_any_description(match):
        :noindex:


    .. py:method:: clear_description_terms():
        :noindex:


    .. py:attribute:: description_terms
        :noindex:


    .. py:method:: match_genus_type(genus_type, match):
        :noindex:


    .. py:method:: match_any_genus_type(match):
        :noindex:


    .. py:method:: clear_genus_type_terms():
        :noindex:


    .. py:attribute:: genus_type_terms
        :noindex:


    .. py:method:: match_parent_genus_type(genus_type, match):
        :noindex:


    .. py:method:: clear_parent_genus_type_terms():
        :noindex:


    .. py:attribute:: parent_genus_type_terms
        :noindex:


    .. py:method:: match_subject_id(subject_id, match):
        :noindex:


    .. py:method:: clear_subject_id_terms():
        :noindex:


    .. py:attribute:: subject_id_terms
        :noindex:


    .. py:method:: supports_subject_query():
        :noindex:


    .. py:method:: get_subject_query():
        :noindex:


    .. py:attribute:: subject_query
        :noindex:


    .. py:method:: match_any_subject(match):
        :noindex:


    .. py:method:: clear_subject_terms():
        :noindex:


    .. py:attribute:: subject_terms
        :noindex:


    .. py:method:: supports_subject_relevancy_query():
        :noindex:


    .. py:method:: get_subject_relevancy_query():
        :noindex:


    .. py:attribute:: subject_relevancy_query
        :noindex:


    .. py:method:: clear_subject_relevancy_terms():
        :noindex:


    .. py:attribute:: subject_relevancy_terms
        :noindex:


    .. py:method:: match_state_id(state_id, match):
        :noindex:


    .. py:method:: clear_state_id_terms():
        :noindex:


    .. py:attribute:: state_id_terms
        :noindex:


    .. py:method:: supports_state_query():
        :noindex:


    .. py:method:: get_state_query():
        :noindex:


    .. py:attribute:: state_query
        :noindex:


    .. py:method:: match_any_state(match):
        :noindex:


    .. py:method:: clear_state_terms():
        :noindex:


    .. py:attribute:: state_terms
        :noindex:


    .. py:method:: match_comment_id(comment_id, match):
        :noindex:


    .. py:method:: clear_comment_id_terms():
        :noindex:


    .. py:attribute:: comment_id_terms
        :noindex:


    .. py:method:: supports_comment_query():
        :noindex:


    .. py:method:: get_comment_query():
        :noindex:


    .. py:attribute:: comment_query
        :noindex:


    .. py:method:: match_any_comment(match):
        :noindex:


    .. py:method:: clear_comment_terms():
        :noindex:


    .. py:attribute:: comment_terms
        :noindex:


    .. py:method:: match_journal_entry_id(journal_entry_id, match):
        :noindex:


    .. py:method:: clear_journal_entry_id_terms():
        :noindex:


    .. py:attribute:: journal_entry_id_terms
        :noindex:


    .. py:method:: supports_journal_entry_query():
        :noindex:


    .. py:method:: get_journal_entry_query():
        :noindex:


    .. py:attribute:: journal_entry_query
        :noindex:


    .. py:method:: match_any_journal_entry(match):
        :noindex:


    .. py:method:: clear_journal_entry_terms():
        :noindex:


    .. py:attribute:: journal_entry_terms
        :noindex:


    .. py:method:: supports_statistic_query():
        :noindex:


    .. py:method:: get_statistic_query():
        :noindex:


    .. py:attribute:: statistic_query
        :noindex:


    .. py:method:: match_any_statistic(match):
        :noindex:


    .. py:method:: clear_statistic_terms():
        :noindex:


    .. py:attribute:: statistic_terms
        :noindex:


    .. py:method:: match_credit_id(credit_id, match):
        :noindex:


    .. py:method:: clear_credit_id_terms():
        :noindex:


    .. py:attribute:: credit_id_terms
        :noindex:


    .. py:method:: supports_credit_query():
        :noindex:


    .. py:method:: get_credit_query():
        :noindex:


    .. py:attribute:: credit_query
        :noindex:


    .. py:method:: match_any_credit(match):
        :noindex:


    .. py:method:: clear_credit_terms():
        :noindex:


    .. py:attribute:: credit_terms
        :noindex:


    .. py:method:: match_relationship_id(relationship_id, match):
        :noindex:


    .. py:method:: clear_relationship_id_terms():
        :noindex:


    .. py:attribute:: relationship_id_terms
        :noindex:


    .. py:method:: supports_relationship_query():
        :noindex:


    .. py:method:: get_relationship_query():
        :noindex:


    .. py:attribute:: relationship_query
        :noindex:


    .. py:method:: match_any_relationship(match):
        :noindex:


    .. py:method:: clear_relationship_terms():
        :noindex:


    .. py:attribute:: relationship_terms
        :noindex:


    .. py:method:: match_relationship_peer_id(peer_id, match):
        :noindex:


    .. py:method:: clear_relationship_peer_id_terms():
        :noindex:


    .. py:attribute:: relationship_peer_id_terms
        :noindex:


Osid Relationship Query
-----------------------

.. py:class:: OsidRelationshipQuery(abc_osid_queries.OsidRelationshipQuery, OsidObjectQuery, OsidTemporalQuery)
    This is the query interface for searching relationships.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_end_reason_id(state_id, match):
        :noindex:


    .. py:method:: clear_end_reason_id_terms():
        :noindex:


    .. py:attribute:: end_reason_id_terms
        :noindex:


    .. py:method:: supports_end_reason_query():
        :noindex:


    .. py:method:: get_end_reason_query(match):
        :noindex:


    .. py:method:: match_any_end_reason(match):
        :noindex:


    .. py:method:: clear_end_reason_terms():
        :noindex:


    .. py:attribute:: end_reason_terms
        :noindex:


Osid Catalog Query
------------------

.. py:class:: OsidCatalogQuery(abc_osid_queries.OsidCatalogQuery, OsidObjectQuery, OsidSourceableQuery, OsidFederateableQuery)
    The ``OsidCatalogQuery`` is used to assemble search queries for catalogs.



Osid Rule Query
---------------

.. py:class:: OsidRuleQuery(abc_osid_queries.OsidRuleQuery, OsidObjectQuery, OsidOperableQuery)
    This is the query interface for searching rules.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_rule_id(rule_id, match):
        :noindex:


    .. py:method:: clear_rule_id_terms():
        :noindex:


    .. py:attribute:: rule_id_terms
        :noindex:


    .. py:method:: supports_rule_query():
        :noindex:


    .. py:method:: get_rule_query(match):
        :noindex:


    .. py:method:: match_any_rule(match):
        :noindex:


    .. py:method:: clear_rule_terms():
        :noindex:


    .. py:attribute:: rule_terms
        :noindex:


Osid Enabler Query
------------------

.. py:class:: OsidEnablerQuery(abc_osid_queries.OsidEnablerQuery, OsidRuleQuery, OsidTemporalQuery)
    This is the query interface for searching enablers.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_schedule_id(schedule_id, match):
        :noindex:


    .. py:method:: clear_schedule_id_terms():
        :noindex:


    .. py:attribute:: schedule_id_terms
        :noindex:


    .. py:method:: supports_schedule_query():
        :noindex:


    .. py:method:: get_schedule_query(match):
        :noindex:


    .. py:method:: match_any_schedule(match):
        :noindex:


    .. py:method:: clear_schedule_terms():
        :noindex:


    .. py:attribute:: schedule_terms
        :noindex:


    .. py:method:: match_event_id(event_id, match):
        :noindex:


    .. py:method:: clear_event_id_terms():
        :noindex:


    .. py:attribute:: event_id_terms
        :noindex:


    .. py:method:: supports_event_query():
        :noindex:


    .. py:method:: get_event_query(match):
        :noindex:


    .. py:method:: match_any_event(match):
        :noindex:


    .. py:method:: clear_event_terms():
        :noindex:


    .. py:attribute:: event_terms
        :noindex:


    .. py:method:: match_cyclic_event_id(cyclic_event_id, match):
        :noindex:


    .. py:method:: clear_cyclic_event_id_terms():
        :noindex:


    .. py:attribute:: cyclic_event_id_terms
        :noindex:


    .. py:method:: supports_cyclic_event_query():
        :noindex:


    .. py:method:: get_cyclic_event_query():
        :noindex:


    .. py:attribute:: cyclic_event_query
        :noindex:


    .. py:method:: match_any_cyclic_event(match):
        :noindex:


    .. py:method:: clear_cyclic_event_terms():
        :noindex:


    .. py:attribute:: cyclic_event_terms
        :noindex:


    .. py:method:: match_demographic_id(resource_id, match):
        :noindex:


    .. py:method:: clear_demographic_id_terms():
        :noindex:


    .. py:attribute:: demographic_id_terms
        :noindex:


    .. py:method:: supports_demographic_query():
        :noindex:


    .. py:method:: get_demographic_query(match):
        :noindex:


    .. py:method:: match_any_demographic(match):
        :noindex:


    .. py:method:: clear_demographic_terms():
        :noindex:


    .. py:attribute:: demographic_terms
        :noindex:


Osid Constrainer Query
----------------------

.. py:class:: OsidConstrainerQuery(abc_osid_queries.OsidConstrainerQuery, OsidRuleQuery)
    This is the query interface for searching constrainers.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.







Osid Processor Query
--------------------

.. py:class:: OsidProcessorQuery(abc_osid_queries.OsidProcessorQuery, OsidRuleQuery)
    This is the query interface for searching processors.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.







Osid Governator Query
---------------------

.. py:class:: OsidGovernatorQuery(abc_osid_queries.OsidGovernatorQuery, OsidObjectQuery, OsidOperableQuery, OsidSourceableQuery)
    This is the query interface for searching governers.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.







Osid Compendium Query
---------------------

.. py:class:: OsidCompendiumQuery(abc_osid_queries.OsidCompendiumQuery, OsidObjectQuery, OsidSubjugateableQuery)
    This is the query interface for searching reports.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_start_date(start, end, match):
        :noindex:


    .. py:method:: match_any_start_date(match):
        :noindex:


    .. py:method:: clear_start_date_terms():
        :noindex:


    .. py:attribute:: start_date_terms
        :noindex:


    .. py:method:: match_end_date(start, end, match):
        :noindex:


    .. py:method:: match_any_end_date(match):
        :noindex:


    .. py:method:: clear_end_date_terms():
        :noindex:


    .. py:attribute:: end_date_terms
        :noindex:


    .. py:method:: match_interpolated(match):
        :noindex:


    .. py:method:: clear_interpolated_terms():
        :noindex:


    .. py:attribute:: interpolated_terms
        :noindex:


    .. py:method:: match_extrapolated(match):
        :noindex:


    .. py:method:: clear_extrapolated_terms():
        :noindex:


    .. py:attribute:: extrapolated_terms
        :noindex:


Osid Capsule Query
------------------

.. py:class:: OsidCapsuleQuery(abc_osid_queries.OsidCapsuleQuery, OsidQuery)
    This is the query interface for searching capsulating interfaces.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.







