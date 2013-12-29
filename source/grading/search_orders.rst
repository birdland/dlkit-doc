.. currentmodule:: dlkit.grading.search_orders
.. automodule:: dlkit.grading.search_orders

Search_Orders
=============


Grade Search Order
------------------

.. autoclass:: GradeSearchOrder
   :show-inheritance:

.. automethod:: GradeSearchOrder.order_by_grade_system

.. automethod:: GradeSearchOrder.supports_grade_system_search_order

.. autoattribute:: GradeSearchOrder.grade_system_search_order

.. automethod:: GradeSearchOrder.order_by_input_score_start_range

.. automethod:: GradeSearchOrder.order_by_input_score_end_range

.. automethod:: GradeSearchOrder.order_by_output_score

.. automethod:: GradeSearchOrder.get_grade_search_order_record



Grade System Search Order
-------------------------

.. autoclass:: GradeSystemSearchOrder
   :show-inheritance:

.. automethod:: GradeSystemSearchOrder.order_by_based_on_grades

.. automethod:: GradeSystemSearchOrder.order_by_lowest_numeric_score

.. automethod:: GradeSystemSearchOrder.order_by_numeric_score_increment

.. automethod:: GradeSystemSearchOrder.order_by_highest_numeric_score

.. automethod:: GradeSystemSearchOrder.get_grade_system_search_order_record



Grade Entry Search Order
------------------------

.. autoclass:: GradeEntrySearchOrder
   :show-inheritance:

.. automethod:: GradeEntrySearchOrder.order_by_gradebook_column

.. automethod:: GradeEntrySearchOrder.supports_gradebook_column_search_order

.. autoattribute:: GradeEntrySearchOrder.gradebook_column_search_order

.. automethod:: GradeEntrySearchOrder.order_by_key_resource

.. automethod:: GradeEntrySearchOrder.supports_key_resource_search_order

.. autoattribute:: GradeEntrySearchOrder.key_resource_search_order

.. automethod:: GradeEntrySearchOrder.order_by_deribed

.. automethod:: GradeEntrySearchOrder.order_by_ignored_for_calculations

.. automethod:: GradeEntrySearchOrder.order_by_grade

.. automethod:: GradeEntrySearchOrder.supports_grade_search_order

.. autoattribute:: GradeEntrySearchOrder.grade_search_order

.. automethod:: GradeEntrySearchOrder.order_by_time_gaded

.. automethod:: GradeEntrySearchOrder.order_by_grader

.. automethod:: GradeEntrySearchOrder.supports_grader_search_order

.. autoattribute:: GradeEntrySearchOrder.grader_search_order

.. automethod:: GradeEntrySearchOrder.order_by_grading_agent

.. automethod:: GradeEntrySearchOrder.supports_grading_agent_search_order

.. autoattribute:: GradeEntrySearchOrder.grading_agent_search_order

.. automethod:: GradeEntrySearchOrder.get_grade_entry_search_order_record



Gradebook Column Search Order
-----------------------------

.. autoclass:: GradebookColumnSearchOrder
   :show-inheritance:

.. automethod:: GradebookColumnSearchOrder.order_by_grade_system

.. automethod:: GradebookColumnSearchOrder.supports_grade_system_search_order

.. autoattribute:: GradebookColumnSearchOrder.gradebook_column_summary_search_order

.. automethod:: GradebookColumnSearchOrder.supports_gradebook_column_summary_search_order

.. autoattribute:: GradebookColumnSearchOrder.grade_system_search_order

.. automethod:: GradebookColumnSearchOrder.get_gradebook_column_search_order_record



Gradebook Column Summary Search Order
-------------------------------------

.. autoclass:: GradebookColumnSummarySearchOrder
   :show-inheritance:

.. automethod:: GradebookColumnSummarySearchOrder.order_by_mean

.. automethod:: GradebookColumnSummarySearchOrder.order_by_median

.. automethod:: GradebookColumnSummarySearchOrder.order_by_mode

.. automethod:: GradebookColumnSummarySearchOrder.order_by_rms

.. automethod:: GradebookColumnSummarySearchOrder.order_by_standard_deviation

.. automethod:: GradebookColumnSummarySearchOrder.order_by_sum

.. automethod:: GradebookColumnSummarySearchOrder.get_gradebook_column_summary_search_order_record



Gradebook Search Order
----------------------

.. autoclass:: GradebookSearchOrder
   :show-inheritance:

.. automethod:: GradebookSearchOrder.get_gradebook_search_order_record



