.. currentmodule:: dlkit.osid.queries
.. automodule:: dlkit.osid.queries

Queries
=======


Osid Query
----------

.. autoclass:: OsidQuery
   :show-inheritance:

   .. autoattribute:: OsidQuery.string_match_types

   .. automethod:: OsidQuery.supports_string_match_type

   .. automethod:: OsidQuery.match_keyword

   .. autoattribute:: OsidQuery.keyword_terms

   .. automethod:: OsidQuery.match_any

   .. autoattribute:: OsidQuery.any_terms



Osid Identifiable Query
-----------------------

.. autoclass:: OsidIdentifiableQuery
   :show-inheritance:

   .. automethod:: OsidIdentifiableQuery.match_id

   .. autoattribute:: OsidIdentifiableQuery.id_terms



Osid Extensible Query
---------------------

.. autoclass:: OsidExtensibleQuery
   :show-inheritance:

   .. automethod:: OsidExtensibleQuery.match_record_type

   .. automethod:: OsidExtensibleQuery.match_any_record

   .. autoattribute:: OsidExtensibleQuery.record_terms



Osid Browsable Query
--------------------

.. autoclass:: OsidBrowsableQuery
   :show-inheritance:





Osid Temporal Query
-------------------

.. autoclass:: OsidTemporalQuery
   :show-inheritance:

   .. automethod:: OsidTemporalQuery.match_effective

   .. autoattribute:: OsidTemporalQuery.effective_terms

   .. automethod:: OsidTemporalQuery.match_start_date

   .. automethod:: OsidTemporalQuery.match_any_start_date

   .. autoattribute:: OsidTemporalQuery.start_date_terms

   .. automethod:: OsidTemporalQuery.match_end_date

   .. automethod:: OsidTemporalQuery.match_any_end_date

   .. autoattribute:: OsidTemporalQuery.end_date_terms

   .. automethod:: OsidTemporalQuery.match_date

   .. autoattribute:: OsidTemporalQuery.date_terms



Osid Subjugateable Query
------------------------

.. autoclass:: OsidSubjugateableQuery
   :show-inheritance:





Osid Aggregateable Query
------------------------

.. autoclass:: OsidAggregateableQuery
   :show-inheritance:





Osid Containable Query
----------------------

.. autoclass:: OsidContainableQuery
   :show-inheritance:

   .. automethod:: OsidContainableQuery.match_sequestered

   .. autoattribute:: OsidContainableQuery.sequestered_terms



Osid Sourceable Query
---------------------

.. autoclass:: OsidSourceableQuery
   :show-inheritance:

   .. automethod:: OsidSourceableQuery.match_provider_id

   .. autoattribute:: OsidSourceableQuery.provider_id_terms

   .. automethod:: OsidSourceableQuery.supports_provider_query

   .. automethod:: OsidSourceableQuery.get_provider_query

   .. automethod:: OsidSourceableQuery.match_any_provider

   .. autoattribute:: OsidSourceableQuery.provider_terms

   .. automethod:: OsidSourceableQuery.match_branding_id

   .. autoattribute:: OsidSourceableQuery.branding_id_terms

   .. automethod:: OsidSourceableQuery.supports_branding_query

   .. automethod:: OsidSourceableQuery.get_branding_query

   .. automethod:: OsidSourceableQuery.match_any_branding

   .. autoattribute:: OsidSourceableQuery.branding_terms

   .. automethod:: OsidSourceableQuery.match_license

   .. automethod:: OsidSourceableQuery.match_any_license

   .. autoattribute:: OsidSourceableQuery.license_terms



Osid Federateable Query
-----------------------

.. autoclass:: OsidFederateableQuery
   :show-inheritance:





Osid Operable Query
-------------------

.. autoclass:: OsidOperableQuery
   :show-inheritance:

   .. automethod:: OsidOperableQuery.match_active

   .. autoattribute:: OsidOperableQuery.active_terms

   .. automethod:: OsidOperableQuery.match_enabled

   .. autoattribute:: OsidOperableQuery.enabled_terms

   .. automethod:: OsidOperableQuery.match_disabled

   .. autoattribute:: OsidOperableQuery.disabled_terms

   .. automethod:: OsidOperableQuery.match_operational

   .. autoattribute:: OsidOperableQuery.operational_terms



Osid Object Query
-----------------

.. autoclass:: OsidObjectQuery
   :show-inheritance:

   .. automethod:: OsidObjectQuery.match_display_name

   .. automethod:: OsidObjectQuery.match_any_display_name

   .. autoattribute:: OsidObjectQuery.display_name_terms

   .. automethod:: OsidObjectQuery.match_description

   .. automethod:: OsidObjectQuery.match_any_description

   .. autoattribute:: OsidObjectQuery.description_terms

   .. automethod:: OsidObjectQuery.match_genus_type

   .. automethod:: OsidObjectQuery.match_any_genus_type

   .. autoattribute:: OsidObjectQuery.genus_type_terms

   .. automethod:: OsidObjectQuery.match_parent_genus_type

   .. autoattribute:: OsidObjectQuery.parent_genus_type_terms

   .. automethod:: OsidObjectQuery.match_subject_id

   .. autoattribute:: OsidObjectQuery.subject_id_terms

   .. automethod:: OsidObjectQuery.supports_subject_query

   .. autoattribute:: OsidObjectQuery.subject_query

   .. automethod:: OsidObjectQuery.match_any_subject

   .. autoattribute:: OsidObjectQuery.subject_terms

   .. automethod:: OsidObjectQuery.supports_subject_relevancy_query

   .. autoattribute:: OsidObjectQuery.subject_relevancy_query

   .. autoattribute:: OsidObjectQuery.subject_relevancy_terms

   .. automethod:: OsidObjectQuery.match_state_id

   .. autoattribute:: OsidObjectQuery.state_id_terms

   .. automethod:: OsidObjectQuery.supports_state_query

   .. autoattribute:: OsidObjectQuery.state_query

   .. automethod:: OsidObjectQuery.match_any_state

   .. autoattribute:: OsidObjectQuery.state_terms

   .. automethod:: OsidObjectQuery.match_comment_id

   .. autoattribute:: OsidObjectQuery.comment_id_terms

   .. automethod:: OsidObjectQuery.supports_comment_query

   .. autoattribute:: OsidObjectQuery.comment_query

   .. automethod:: OsidObjectQuery.match_any_comment

   .. autoattribute:: OsidObjectQuery.comment_terms

   .. automethod:: OsidObjectQuery.match_journal_entry_id

   .. autoattribute:: OsidObjectQuery.journal_entry_id_terms

   .. automethod:: OsidObjectQuery.supports_journal_entry_query

   .. autoattribute:: OsidObjectQuery.journal_entry_query

   .. automethod:: OsidObjectQuery.match_any_journal_entry

   .. autoattribute:: OsidObjectQuery.journal_entry_terms

   .. automethod:: OsidObjectQuery.supports_statistic_query

   .. autoattribute:: OsidObjectQuery.statistic_query

   .. automethod:: OsidObjectQuery.match_any_statistic

   .. autoattribute:: OsidObjectQuery.statistic_terms

   .. automethod:: OsidObjectQuery.match_credit_id

   .. autoattribute:: OsidObjectQuery.credit_id_terms

   .. automethod:: OsidObjectQuery.supports_credit_query

   .. autoattribute:: OsidObjectQuery.credit_query

   .. automethod:: OsidObjectQuery.match_any_credit

   .. autoattribute:: OsidObjectQuery.credit_terms

   .. automethod:: OsidObjectQuery.match_relationship_id

   .. autoattribute:: OsidObjectQuery.relationship_id_terms

   .. automethod:: OsidObjectQuery.supports_relationship_query

   .. autoattribute:: OsidObjectQuery.relationship_query

   .. automethod:: OsidObjectQuery.match_any_relationship

   .. autoattribute:: OsidObjectQuery.relationship_terms

   .. automethod:: OsidObjectQuery.match_relationship_peer_id

   .. autoattribute:: OsidObjectQuery.relationship_peer_id_terms



Osid Relationship Query
-----------------------

.. autoclass:: OsidRelationshipQuery
   :show-inheritance:

   .. automethod:: OsidRelationshipQuery.match_end_reason_id

   .. autoattribute:: OsidRelationshipQuery.end_reason_id_terms

   .. automethod:: OsidRelationshipQuery.supports_end_reason_query

   .. automethod:: OsidRelationshipQuery.get_end_reason_query

   .. automethod:: OsidRelationshipQuery.match_any_end_reason

   .. autoattribute:: OsidRelationshipQuery.end_reason_terms



Osid Catalog Query
------------------

.. autoclass:: OsidCatalogQuery
   :show-inheritance:





Osid Rule Query
---------------

.. autoclass:: OsidRuleQuery
   :show-inheritance:

   .. automethod:: OsidRuleQuery.match_rule_id

   .. autoattribute:: OsidRuleQuery.rule_id_terms

   .. automethod:: OsidRuleQuery.supports_rule_query

   .. automethod:: OsidRuleQuery.get_rule_query

   .. automethod:: OsidRuleQuery.match_any_rule

   .. autoattribute:: OsidRuleQuery.rule_terms



Osid Enabler Query
------------------

.. autoclass:: OsidEnablerQuery
   :show-inheritance:

   .. automethod:: OsidEnablerQuery.match_schedule_id

   .. autoattribute:: OsidEnablerQuery.schedule_id_terms

   .. automethod:: OsidEnablerQuery.supports_schedule_query

   .. automethod:: OsidEnablerQuery.get_schedule_query

   .. automethod:: OsidEnablerQuery.match_any_schedule

   .. autoattribute:: OsidEnablerQuery.schedule_terms

   .. automethod:: OsidEnablerQuery.match_event_id

   .. autoattribute:: OsidEnablerQuery.event_id_terms

   .. automethod:: OsidEnablerQuery.supports_event_query

   .. automethod:: OsidEnablerQuery.get_event_query

   .. automethod:: OsidEnablerQuery.match_any_event

   .. autoattribute:: OsidEnablerQuery.event_terms

   .. automethod:: OsidEnablerQuery.match_cyclic_event_id

   .. autoattribute:: OsidEnablerQuery.cyclic_event_id_terms

   .. automethod:: OsidEnablerQuery.supports_cyclic_event_query

   .. autoattribute:: OsidEnablerQuery.cyclic_event_query

   .. automethod:: OsidEnablerQuery.match_any_cyclic_event

   .. autoattribute:: OsidEnablerQuery.cyclic_event_terms

   .. automethod:: OsidEnablerQuery.match_demographic_id

   .. autoattribute:: OsidEnablerQuery.demographic_id_terms

   .. automethod:: OsidEnablerQuery.supports_demographic_query

   .. automethod:: OsidEnablerQuery.get_demographic_query

   .. automethod:: OsidEnablerQuery.match_any_demographic

   .. autoattribute:: OsidEnablerQuery.demographic_terms



Osid Constrainer Query
----------------------

.. autoclass:: OsidConstrainerQuery
   :show-inheritance:





Osid Processor Query
--------------------

.. autoclass:: OsidProcessorQuery
   :show-inheritance:





Osid Governator Query
---------------------

.. autoclass:: OsidGovernatorQuery
   :show-inheritance:





Osid Compendium Query
---------------------

.. autoclass:: OsidCompendiumQuery
   :show-inheritance:

   .. automethod:: OsidCompendiumQuery.match_start_date

   .. automethod:: OsidCompendiumQuery.match_any_start_date

   .. autoattribute:: OsidCompendiumQuery.start_date_terms

   .. automethod:: OsidCompendiumQuery.match_end_date

   .. automethod:: OsidCompendiumQuery.match_any_end_date

   .. autoattribute:: OsidCompendiumQuery.end_date_terms

   .. automethod:: OsidCompendiumQuery.match_interpolated

   .. autoattribute:: OsidCompendiumQuery.interpolated_terms

   .. automethod:: OsidCompendiumQuery.match_extrapolated

   .. autoattribute:: OsidCompendiumQuery.extrapolated_terms



Osid Capsule Query
------------------

.. autoclass:: OsidCapsuleQuery
   :show-inheritance:





