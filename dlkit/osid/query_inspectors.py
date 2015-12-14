
from ..osid import markers as osid_markers


class OsidQueryInspector:
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_keyword_terms(self):
        """Gets the keyword query terms.

        :return: the keyword string terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.StringTerm

    keyword_terms = property(fget=get_keyword_terms)

    def get_any_terms(self):
        """Gets the any query terms.

        :return: the any terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    any_terms = property(fget=get_any_terms)


class OsidIdentifiableQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_id_terms(self):
        """Gets the ``Id`` query terms.

        :return: the ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    id_terms = property(fget=get_id_terms)


class OsidExtensibleQueryInspector(OsidQueryInspector, osid_markers.Extensible):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_record_type_terms(self):
        """Gets the record type query terms.

        :return: the record type terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.TypeTerm

    record_type_terms = property(fget=get_record_type_terms)


class OsidBrowsableQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




class OsidTemporalQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_effective_terms(self):
        """Gets the effective query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    effective_terms = property(fget=get_effective_terms)

    def get_start_date_terms(self):
        """Gets the start date query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.DateTimeRangeTerm

    start_date_terms = property(fget=get_start_date_terms)

    def get_end_date_terms(self):
        """Gets the end date query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.DateTimeRangeTerm

    end_date_terms = property(fget=get_end_date_terms)

    def get_date_terms(self):
        """Gets the date query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.DateTimeRangeTerm

    date_terms = property(fget=get_date_terms)


class OsidSubjugateableQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




class OsidAggregateableQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




class OsidContainableQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_sequestered_terms(self):
        """Gets the sequestered query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    sequestered_terms = property(fget=get_sequestered_terms)


class OsidSourceableQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_provider_id_terms(self):
        """Gets the provider ``Id`` query terms.

        :return: the provider ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    provider_id_terms = property(fget=get_provider_id_terms)

    def get_provider_terms(self):
        """Gets the provider query terms.

        :return: the provider terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceQueryInspector

    provider_terms = property(fget=get_provider_terms)

    def get_branding_id_terms(self):
        """Gets the asset ``Id`` query terms.

        :return: the asset ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    branding_id_terms = property(fget=get_branding_id_terms)

    def get_branding_terms(self):
        """Gets the asset query terms.

        :return: the branding terms
        :rtype: ``osid.repository.AssetQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.repository.AssetQueryInspector

    branding_terms = property(fget=get_branding_terms)

    def get_license_terms(self):
        """Gets the license query terms.

        :return: the license terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.StringTerm

    license_terms = property(fget=get_license_terms)


class OsidFederateableQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




class OsidOperableQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_active_terms(self):
        """Gets the active query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    active_terms = property(fget=get_active_terms)

    def get_enabled_terms(self):
        """Gets the administratively enabled query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    enabled_terms = property(fget=get_enabled_terms)

    def get_disabled_terms(self):
        """Gets the administratively disabled query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    disabled_terms = property(fget=get_disabled_terms)

    def get_operational_terms(self):
        """Gets the operational query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    operational_terms = property(fget=get_operational_terms)


class OsidObjectQueryInspector(OsidIdentifiableQueryInspector, OsidExtensibleQueryInspector, OsidBrowsableQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_display_name_terms(self):
        """Gets the display name query terms.

        :return: the display name terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.StringTerm

    display_name_terms = property(fget=get_display_name_terms)

    def get_description_terms(self):
        """Gets the description query terms.

        :return: the description terms
        :rtype: ``osid.search.terms.StringTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.StringTerm

    description_terms = property(fget=get_description_terms)

    def get_genus_type_terms(self):
        """Gets the genus type query terms.

        :return: the genus type terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.TypeTerm

    genus_type_terms = property(fget=get_genus_type_terms)

    def get_parent_genus_type_terms(self):
        """Gets the parent genus type query terms.

        :return: the parent genus type terms
        :rtype: ``osid.search.terms.TypeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.TypeTerm

    parent_genus_type_terms = property(fget=get_parent_genus_type_terms)

    def get_subject_id_terms(self):
        """Gets the subject ``Id`` query terms.

        :return: the subject ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    subject_id_terms = property(fget=get_subject_id_terms)

    def get_subject_terms(self):
        """Gets the subject query terms.

        :return: the subject query terms
        :rtype: ``osid.ontology.SubjectQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.ontology.SubjectQueryInspector

    subject_terms = property(fget=get_subject_terms)

    def get_subject_relevancy_terms(self):
        """Gets the subject relevancy query terms.

        :return: the subject relevancy query terms
        :rtype: ``osid.ontology.RelevancyQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.ontology.RelevancyQueryInspector

    subject_relevancy_terms = property(fget=get_subject_relevancy_terms)

    def get_state_id_terms(self):
        """Gets the state ``Id`` query terms.

        :return: the state ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    state_id_terms = property(fget=get_state_id_terms)

    def get_state_terms(self):
        """Gets the state query terms.

        :return: the state query terms
        :rtype: ``osid.process.StateQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.process.StateQueryInspector

    state_terms = property(fget=get_state_terms)

    def get_comment_id_terms(self):
        """Gets the comment ``Id`` query terms.

        :return: the comment ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    comment_id_terms = property(fget=get_comment_id_terms)

    def get_comment_terms(self):
        """Gets the comment query terms.

        :return: the comment query terms
        :rtype: ``osid.commenting.CommentQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.commenting.CommentQueryInspector

    comment_terms = property(fget=get_comment_terms)

    def get_journal_entry_id_terms(self):
        """Gets the journal entry ``Id`` query terms.

        :return: the journal entry ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    journal_entry_id_terms = property(fget=get_journal_entry_id_terms)

    def get_journal_entry_terms(self):
        """Gets the journal entry query terms.

        :return: the journal entry query terms
        :rtype: ``osid.journaling.JournalEntryQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.journaling.JournalEntryQueryInspector

    journal_entry_terms = property(fget=get_journal_entry_terms)

    def get_statistic_terms(self):
        """Gets the statistic query terms.

        :return: the statistic query terms
        :rtype: ``osid.metering.StatisticQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.metering.StatisticQueryInspector

    statistic_terms = property(fget=get_statistic_terms)

    def get_credit_id_terms(self):
        """Gets the credit ``Id`` query terms.

        :return: the credit ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    credit_id_terms = property(fget=get_credit_id_terms)

    def get_credit_terms(self):
        """Gets the credit query terms.

        :return: the credit query terms
        :rtype: ``osid.acknowledgement.CreditQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.acknowledgement.CreditQueryInspector

    credit_terms = property(fget=get_credit_terms)

    def get_relationship_id_terms(self):
        """Gets the relationship ``Id`` query terms.

        :return: the relationship ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    relationship_id_terms = property(fget=get_relationship_id_terms)

    def get_relationship_terms(self):
        """Gets the relationship query terms.

        :return: the relationship query terms
        :rtype: ``osid.relationship.RelationshipQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.relationship.RelationshipQueryInspector

    relationship_terms = property(fget=get_relationship_terms)

    def get_relationship_peer_id_terms(self):
        """Gets the relationship peer ``Id`` query terms.

        :return: the relationship peer ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    relationship_peer_id_terms = property(fget=get_relationship_peer_id_terms)


class OsidRelationshipQueryInspector(OsidObjectQueryInspector, OsidTemporalQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_end_reason_id_terms(self):
        """Gets the end reaosn state ``Id`` query terms.

        :return: the state ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    end_reason_id_terms = property(fget=get_end_reason_id_terms)

    def get_end_reason_terms(self):
        """Gets the end reaosn state query terms.

        :return: the state query terms
        :rtype: ``osid.process.StateQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.process.StateQueryInspector

    end_reason_terms = property(fget=get_end_reason_terms)


class OsidCatalogQueryInspector(OsidObjectQueryInspector, OsidSourceableQueryInspector, OsidFederateableQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




class OsidRuleQueryInspector(OsidObjectQueryInspector, OsidOperableQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_rule_id_terms(self):
        """Gets the rule ``Id`` query terms.

        :return: the rule ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    rule_id_terms = property(fget=get_rule_id_terms)

    def get_rule_terms(self):
        """Gets the rule query terms.

        :return: the rule query terms
        :rtype: ``osid.rules.RuleQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.rules.RuleQueryInspector

    rule_terms = property(fget=get_rule_terms)


class OsidEnablerQueryInspector(OsidRuleQueryInspector, OsidTemporalQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_schedule_id_terms(self):
        """Gets the effective schedule ``Id`` query terms.

        :return: the effecive schedule ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    schedule_id_terms = property(fget=get_schedule_id_terms)

    def get_schedule_terms(self):
        """Gets the effective schedule query terms.

        :return: the query terms
        :rtype: ``osid.calendaring.ScheduleQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.ScheduleQueryInspector

    schedule_terms = property(fget=get_schedule_terms)

    def get_event_id_terms(self):
        """Gets the effective event ``Id`` query terms.

        :return: the effecive recurring event ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    event_id_terms = property(fget=get_event_id_terms)

    def get_event_terms(self):
        """Gets the effective event query terms.

        :return: the query terms
        :rtype: ``osid.calendaring.EventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.EventQueryInspector

    event_terms = property(fget=get_event_terms)

    def get_cyclic_event_id_terms(self):
        """Gets the cyclic event ``Id`` query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    cyclic_event_id_terms = property(fget=get_cyclic_event_id_terms)

    def get_cyclic_event_terms(self):
        """Gets the cyclic event query terms.

        :return: the query terms
        :rtype: ``osid.calendaring.cycle.CyclicEventQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.calendaring.cycle.CyclicEventQueryInspector

    cyclic_event_terms = property(fget=get_cyclic_event_terms)

    def get_demographic_id_terms(self):
        """Gets the demographic resource ``Id`` query terms.

        :return: the resource ``Id`` terms
        :rtype: ``osid.search.terms.IdTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.IdTerm

    demographic_id_terms = property(fget=get_demographic_id_terms)

    def get_demographic_terms(self):
        """Gets the demographic resource query terms.

        :return: the resource query terms
        :rtype: ``osid.resource.ResourceQueryInspector``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.resource.ResourceQueryInspector

    demographic_terms = property(fget=get_demographic_terms)


class OsidConstrainerQueryInspector(OsidRuleQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




class OsidProcessorQueryInspector(OsidRuleQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




class OsidGovernatorQueryInspector(OsidObjectQueryInspector, OsidOperableQueryInspector, OsidSourceableQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




class OsidCompendiumQueryInspector(OsidObjectQueryInspector, OsidSubjugateableQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """

    def get_start_date_terms(self):
        """Gets the start date query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.DateTimeRangeTerm

    start_date_terms = property(fget=get_start_date_terms)

    def get_end_date_terms(self):
        """Gets the end date query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.DateTimeRangeTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.DateTimeRangeTerm

    end_date_terms = property(fget=get_end_date_terms)

    def get_interpolated_terms(self):
        """Gets the interpolated query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    interpolated_terms = property(fget=get_interpolated_terms)

    def get_extrapolated_terms(self):
        """Gets the extrapolated query terms.

        :return: the query terms
        :rtype: ``osid.search.terms.BooleanTerm``


        *compliance: mandatory -- This method must be implemented.*

        """
        return # osid.search.terms.BooleanTerm

    extrapolated_terms = property(fget=get_extrapolated_terms)


class OsidCapsuleQueryInspector(OsidQueryInspector):
    """The query inspectors provide a means of accessing the match terms of a query.

    These interfaces are used to examine the actual query terms used in
    a search or that may be used to create a smart catalog. Query
    inspectors may be converted to an ``OsidQuery`` for reuse or
    modification in the search sessions.

    """




