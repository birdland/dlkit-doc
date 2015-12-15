

Searches
========


Osid Search
-----------

.. py:class:: OsidSearch(abc_osid_searches.OsidSearch, osid_rules.OsidCondition)
    ``OsidSearch`` specifies search options used to perform OSID searches.


    An ``OsidSearch`` is available from an ``OsidSession`` and defines
    methods to govern the overall search of terms supplied in one or
    more ``OsidQuery`` interfaces.




    This interface is available from a search session.Example using the
    search interface to retrieve the first 25 results:
      OsidSearch os = session.getObjectSearch();
      os.limitResultSet(1, 25);




      OsidQuery query;
      query = session.getObjectQuery();
      query.addDescriptionMatch("*food*", wildcardStringMatchType, true);




      ObjectSearchResults results = session.getObjectsBySearch(query, os);
      ObjectList list = results.getObjectList();









    .. py:method:: limit_result_set(start, end):
        :noindex:


Osid Search Results
-------------------

.. py:class:: OsidSearchResults(abc_osid_searches.OsidSearchResults, osid_rules.OsidResult)
    This interface provides a means to capture results of a search.


    An example of searching withina result set: OsidSearch os =
    session.getObjectSearch(); OsidQuery query; query =
    session.getObjectQuery(); query.matchDescription("*food*",
    wildcardStringMatchType, true); ObjectSearchResults results =
    session.getObjectBySearch(query, os); // get information about
    search ObjectList objects = results.getObjects(); int size =
    results.getResultSize(); SearchPerformanceRecord record =
    (SearchPerformanceRecord)
    results.getObjectSearchResultsRecord(performanceRecodType); Duration
    duration = record.getTimeForSearch();





    .. py:method:: get_result_size():
        :noindex:


    .. py:attribute:: result_size
        :noindex:


