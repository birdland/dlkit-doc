

Queries
=======


Objective Query
---------------

.. py:class:: ObjectiveQuery(abc_learning_queries.ObjectiveQuery, osid_queries.OsidObjectQuery, osid_queries.OsidFederateableQuery)
    This is the query for searching objectives.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_assessment_id(assessment_id, match):
        :noindex:


    .. py:method:: clear_assessment_id_terms():
        :noindex:


    .. py:attribute:: assessment_id_terms
        :noindex:


    .. py:method:: supports_assessment_query():
        :noindex:


    .. py:method:: get_assessment_query():
        :noindex:


    .. py:attribute:: assessment_query
        :noindex:


    .. py:method:: match_any_assessment(match):
        :noindex:


    .. py:method:: clear_assessment_terms():
        :noindex:


    .. py:attribute:: assessment_terms
        :noindex:


    .. py:method:: match_knowledge_category_id(grade_id, match):
        :noindex:


    .. py:method:: clear_knowledge_category_id_terms():
        :noindex:


    .. py:attribute:: knowledge_category_id_terms
        :noindex:


    .. py:method:: supports_knowledge_category_query():
        :noindex:


    .. py:method:: get_knowledge_category_query():
        :noindex:


    .. py:attribute:: knowledge_category_query
        :noindex:


    .. py:method:: match_any_knowledge_category(match):
        :noindex:


    .. py:method:: clear_knowledge_category_terms():
        :noindex:


    .. py:attribute:: knowledge_category_terms
        :noindex:


    .. py:method:: match_cognitive_process_id(grade_id, match):
        :noindex:


    .. py:method:: clear_cognitive_process_id_terms():
        :noindex:


    .. py:attribute:: cognitive_process_id_terms
        :noindex:


    .. py:method:: supports_cognitive_process_query():
        :noindex:


    .. py:method:: get_cognitive_process_query():
        :noindex:


    .. py:attribute:: cognitive_process_query
        :noindex:


    .. py:method:: match_any_cognitive_process(match):
        :noindex:


    .. py:method:: clear_cognitive_process_terms():
        :noindex:


    .. py:attribute:: cognitive_process_terms
        :noindex:


    .. py:method:: match_activity_id(activity_id, match):
        :noindex:


    .. py:method:: clear_activity_id_terms():
        :noindex:


    .. py:attribute:: activity_id_terms
        :noindex:


    .. py:method:: supports_activity_query():
        :noindex:


    .. py:method:: get_activity_query():
        :noindex:


    .. py:attribute:: activity_query
        :noindex:


    .. py:method:: match_any_activity(match):
        :noindex:


    .. py:method:: clear_activity_terms():
        :noindex:


    .. py:attribute:: activity_terms
        :noindex:


    .. py:method:: match_requisite_objective_id(requisite_objective_id, match):
        :noindex:


    .. py:method:: clear_requisite_objective_id_terms():
        :noindex:


    .. py:attribute:: requisite_objective_id_terms
        :noindex:


    .. py:method:: supports_requisite_objective_query():
        :noindex:


    .. py:method:: get_requisite_objective_query():
        :noindex:


    .. py:attribute:: requisite_objective_query
        :noindex:


    .. py:method:: match_any_requisite_objective(match):
        :noindex:


    .. py:method:: clear_requisite_objective_terms():
        :noindex:


    .. py:attribute:: requisite_objective_terms
        :noindex:


    .. py:method:: match_dependent_objective_id(dependent_objective_id, match):
        :noindex:


    .. py:method:: clear_dependent_objective_id_terms():
        :noindex:


    .. py:attribute:: dependent_objective_id_terms
        :noindex:


    .. py:method:: supports_depndent_objective_query():
        :noindex:


    .. py:method:: get_dependent_objective_query():
        :noindex:


    .. py:attribute:: dependent_objective_query
        :noindex:


    .. py:method:: match_any_dependent_objective(match):
        :noindex:


    .. py:method:: clear_dependent_objective_terms():
        :noindex:


    .. py:attribute:: dependent_objective_terms
        :noindex:


    .. py:method:: match_equivalent_objective_id(equivalent_objective_id, match):
        :noindex:


    .. py:method:: clear_equivalent_objective_id_terms():
        :noindex:


    .. py:attribute:: equivalent_objective_id_terms
        :noindex:


    .. py:method:: supports_equivalent_objective_query():
        :noindex:


    .. py:method:: get_equivalent_objective_query():
        :noindex:


    .. py:attribute:: equivalent_objective_query
        :noindex:


    .. py:method:: match_any_equivalent_objective(match):
        :noindex:


    .. py:method:: clear_equivalent_objective_terms():
        :noindex:


    .. py:attribute:: equivalent_objective_terms
        :noindex:


    .. py:method:: match_ancestor_objective_id(objective_id, match):
        :noindex:


    .. py:method:: clear_ancestor_objective_id_terms():
        :noindex:


    .. py:attribute:: ancestor_objective_id_terms
        :noindex:


    .. py:method:: supports_ancestor_objective_query():
        :noindex:


    .. py:method:: get_ancestor_objective_query():
        :noindex:


    .. py:attribute:: ancestor_objective_query
        :noindex:


    .. py:method:: match_any_ancestor_objective(match):
        :noindex:


    .. py:method:: clear_ancestor_objective_terms():
        :noindex:


    .. py:attribute:: ancestor_objective_terms
        :noindex:


    .. py:method:: match_descendant_objective_id(objective_id, match):
        :noindex:


    .. py:method:: clear_descendant_objective_id_terms():
        :noindex:


    .. py:attribute:: descendant_objective_id_terms
        :noindex:


    .. py:method:: supports_descendant_objective_query():
        :noindex:


    .. py:method:: get_descendant_objective_query():
        :noindex:


    .. py:attribute:: descendant_objective_query
        :noindex:


    .. py:method:: match_any_descendant_objective(match):
        :noindex:


    .. py:method:: clear_descendant_objective_terms():
        :noindex:


    .. py:attribute:: descendant_objective_terms
        :noindex:


    .. py:method:: match_objective_bank_id(objective_bank_id, match):
        :noindex:


    .. py:method:: clear_objective_bank_id_terms():
        :noindex:


    .. py:attribute:: objective_bank_id_terms
        :noindex:


    .. py:method:: supports_objective_bank_query():
        :noindex:


    .. py:method:: get_objective_bank_query():
        :noindex:


    .. py:attribute:: objective_bank_query
        :noindex:


    .. py:method:: clear_objective_bank_terms():
        :noindex:


    .. py:attribute:: objective_bank_terms
        :noindex:


    .. py:method:: get_objective_query_record(objective_record_type):
        :noindex:


Activity Query
--------------

.. py:class:: ActivityQuery(abc_learning_queries.ActivityQuery, osid_queries.OsidObjectQuery, osid_queries.OsidSubjugateableQuery)
    This is the query for searching activities.


    Each method match request produces an ``AND`` term while multiple
    invocations of a method produces a nested ``OR``.





    .. py:method:: match_objective_id(objective_id, match):
        :noindex:


    .. py:method:: clear_objective_id_terms():
        :noindex:


    .. py:attribute:: objective_id_terms
        :noindex:


    .. py:method:: supports_objective_query():
        :noindex:


    .. py:method:: get_objective_query():
        :noindex:


    .. py:attribute:: objective_query
        :noindex:


    .. py:method:: clear_objective_terms():
        :noindex:


    .. py:attribute:: objective_terms
        :noindex:


    .. py:method:: match_asset_id(asset_id, match):
        :noindex:


    .. py:method:: clear_asset_id_terms():
        :noindex:


    .. py:attribute:: asset_id_terms
        :noindex:


    .. py:method:: supports_asset_query():
        :noindex:


    .. py:method:: get_asset_query():
        :noindex:


    .. py:attribute:: asset_query
        :noindex:


    .. py:method:: match_any_asset(match):
        :noindex:


    .. py:method:: clear_asset_terms():
        :noindex:


    .. py:attribute:: asset_terms
        :noindex:


    .. py:method:: match_course_id(course_id, match):
        :noindex:


    .. py:method:: clear_course_id_terms():
        :noindex:


    .. py:attribute:: course_id_terms
        :noindex:


    .. py:method:: supports_course_query():
        :noindex:


    .. py:method:: get_course_query():
        :noindex:


    .. py:attribute:: course_query
        :noindex:


    .. py:method:: match_any_course(match):
        :noindex:


    .. py:method:: clear_course_terms():
        :noindex:


    .. py:attribute:: course_terms
        :noindex:


    .. py:method:: match_assessment_id(assessment_id, match):
        :noindex:


    .. py:method:: clear_assessment_id_terms():
        :noindex:


    .. py:attribute:: assessment_id_terms
        :noindex:


    .. py:method:: supports_assessment_query():
        :noindex:


    .. py:method:: get_assessment_query():
        :noindex:


    .. py:attribute:: assessment_query
        :noindex:


    .. py:method:: match_any_assessment(match):
        :noindex:


    .. py:method:: clear_assessment_terms():
        :noindex:


    .. py:attribute:: assessment_terms
        :noindex:


    .. py:method:: match_objective_bank_id(objective_bank_id, match):
        :noindex:


    .. py:method:: clear_objective_bank_id_terms():
        :noindex:


    .. py:attribute:: objective_bank_id_terms
        :noindex:


    .. py:method:: supports_objective_bank_query():
        :noindex:


    .. py:method:: get_objective_bank_query():
        :noindex:


    .. py:attribute:: objective_bank_query
        :noindex:


    .. py:method:: clear_objective_bank_terms():
        :noindex:


    .. py:attribute:: objective_bank_terms
        :noindex:


    .. py:method:: get_activity_query_record(activity_record_type):
        :noindex:


Objective Bank Query
--------------------

.. py:class:: ObjectiveBankQuery(abc_learning_queries.ObjectiveBankQuery, osid_queries.OsidCatalogQuery)
    This is the query for searching objective banks.


    Each method specifies an ``AND`` term while multiple invocations of
    the same method produce a nested ``OR``.





    .. py:method:: match_objective_id(objective_id, match):
        :noindex:


    .. py:method:: clear_objective_id_terms():
        :noindex:


    .. py:attribute:: objective_id_terms
        :noindex:


    .. py:method:: supports_objective_query():
        :noindex:


    .. py:method:: get_objective_query():
        :noindex:


    .. py:attribute:: objective_query
        :noindex:


    .. py:method:: match_any_objective(match):
        :noindex:


    .. py:method:: clear_objective_terms():
        :noindex:


    .. py:attribute:: objective_terms
        :noindex:


    .. py:method:: match_activity_id(activity_id, match):
        :noindex:


    .. py:method:: clear_activity_id_terms():
        :noindex:


    .. py:attribute:: activity_id_terms
        :noindex:


    .. py:method:: supports_activity_query():
        :noindex:


    .. py:method:: get_activity_query():
        :noindex:


    .. py:attribute:: activity_query
        :noindex:


    .. py:method:: match_any_activity(match):
        :noindex:


    .. py:method:: clear_activity_terms():
        :noindex:


    .. py:attribute:: activity_terms
        :noindex:


    .. py:method:: match_ancestor_objective_bank_id(objective_bank_id, match):
        :noindex:


    .. py:method:: clear_ancestor_objective_bank_id_terms():
        :noindex:


    .. py:attribute:: ancestor_objective_bank_id_terms
        :noindex:


    .. py:method:: supports_ancestor_objective_bank_query():
        :noindex:


    .. py:method:: get_ancestor_objective_bank_query():
        :noindex:


    .. py:attribute:: ancestor_objective_bank_query
        :noindex:


    .. py:method:: match_any_ancestor_objective_bank(match):
        :noindex:


    .. py:method:: clear_ancestor_objective_bank_terms():
        :noindex:


    .. py:attribute:: ancestor_objective_bank_terms
        :noindex:


    .. py:method:: match_descendant_objective_bank_id(objective_bank_id, match):
        :noindex:


    .. py:method:: clear_descendant_objective_bank_id_terms():
        :noindex:


    .. py:attribute:: descendant_objective_bank_id_terms
        :noindex:


    .. py:method:: supports_descendant_objective_bank_query():
        :noindex:


    .. py:method:: get_descendant_objective_bank_query():
        :noindex:


    .. py:attribute:: descendant_objective_bank_query
        :noindex:


    .. py:method:: match_any_descendant_objective_bank(match):
        :noindex:


    .. py:method:: clear_descendant_objective_bank_terms():
        :noindex:


    .. py:attribute:: descendant_objective_bank_terms
        :noindex:


    .. py:method:: get_objective_bank_query_record(objective_bank_record_type):
        :noindex:


