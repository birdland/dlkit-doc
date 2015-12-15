

Searches
========


Grade System Search
-------------------

.. py:class:: GradeSystemSearch(abc_grading_searches.GradeSystemSearch, osid_searches.OsidSearch)
    The interface for governing grade system searches.

    .. py:method:: search_among_grade_systems(grade_system_ids):
        :noindex:


    .. py:method:: order_grade_system_results(grade_system_search_order):
        :noindex:


    .. py:method:: get_grade_system_search_record(grade_system_search_record_type):
        :noindex:


Grade System Search Results
---------------------------

.. py:class:: GradeSystemSearchResults(abc_grading_searches.GradeSystemSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_grade_systems():
        :noindex:


    .. py:attribute:: grade_systems
        :noindex:


    .. py:method:: get_grade_system_query_inspector():
        :noindex:


    .. py:attribute:: grade_system_query_inspector
        :noindex:


    .. py:method:: get_grade_system_search_results_record(grade_system_search_record_type):
        :noindex:


Grade Entry Search
------------------

.. py:class:: GradeEntrySearch(abc_grading_searches.GradeEntrySearch, osid_searches.OsidSearch)
    ``GradeEntrySearch`` defines the interface for specifying package search options.

    .. py:method:: search_among_grade_entries(grade_entry_ids):
        :noindex:


    .. py:method:: order_grade_entry_results(grade_entry_search_order):
        :noindex:


    .. py:method:: get_grade_entry_search_record(grade_entry_search_record_type):
        :noindex:


Grade Entry Search Results
--------------------------

.. py:class:: GradeEntrySearchResults(abc_grading_searches.GradeEntrySearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_grade_entries():
        :noindex:


    .. py:attribute:: grade_entries
        :noindex:


    .. py:method:: get_grade_entry_query_inspector():
        :noindex:


    .. py:attribute:: grade_entry_query_inspector
        :noindex:


    .. py:method:: get_grade_entry_search_results_record(grade_entry_search_record_type):
        :noindex:


Gradebook Column Search
-----------------------

.. py:class:: GradebookColumnSearch(abc_grading_searches.GradebookColumnSearch, osid_searches.OsidSearch)
    ``GradebookColumnSearch`` defines the interface for specifying grading search options.

    .. py:method:: search_among_gradebook_columns(gradebook_column_ids):
        :noindex:


    .. py:method:: order_gradebook_column_results(gradebook_column_search_order):
        :noindex:


    .. py:method:: get_gradebook_column_search_record(gradebook_column_search_record_type):
        :noindex:


Gradebook Column Search Results
-------------------------------

.. py:class:: GradebookColumnSearchResults(abc_grading_searches.GradebookColumnSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_gradebook_columns():
        :noindex:


    .. py:attribute:: gradebook_columns
        :noindex:


    .. py:method:: get_gradebook_column_query_inspector():
        :noindex:


    .. py:attribute:: gradebook_column_query_inspector
        :noindex:


    .. py:method:: get_gradebook_column_search_results_record(gradebook_column_search_record_type):
        :noindex:


Gradebook Search
----------------

.. py:class:: GradebookSearch(abc_grading_searches.GradebookSearch, osid_searches.OsidSearch)
    The interface for governing gradebook searches.

    .. py:method:: search_among_gradebooks(gradebook_ids):
        :noindex:


    .. py:method:: order_gradebook_results(gradebook_search_order):
        :noindex:


    .. py:method:: get_gradebook_search_record(gradebook_search_record_type):
        :noindex:


Gradebook Search Results
------------------------

.. py:class:: GradebookSearchResults(abc_grading_searches.GradebookSearchResults, osid_searches.OsidSearchResults)
    This interface provides a means to capture results of a search.

    .. py:method:: get_gradebooks():
        :noindex:


    .. py:attribute:: gradebooks
        :noindex:


    .. py:method:: get_gradebook_query_inspector():
        :noindex:


    .. py:attribute:: gradebook_query_inspector
        :noindex:


    .. py:method:: get_gradebook_search_results_record(gradebook_search_record_type):
        :noindex:


