from ..osid import objects as osid_objects


class IdList(osid_objects.OsidList):
    """Like all ``OsidLists,``  ``IdList`` provides a means for accessing ``Id`` elements sequentially either one at a time or many at a time.

    Examples: while (il.hasNext()) { Id id = il.getNextId(); }

    or
      while (il.hasNext()) {
           Id[] ids = il.getNextIds(il.available());
      }
    


    """
    def get_next_id(self):
        """Gets the next ``Id`` in this list.

        :return: the next ``Id`` in this list. The ``has_next()`` method should be used to test that a next ``Id`` is available before calling this method.
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.Id

    next_id = property(fget=get_next_id)

    def get_next_ids(self, n):
        """Gets the next set of ``Ids`` in this list.

        The specified amount must be less than or equal to the return
        from ``available()``.

        :param n: the number of ``Id`` elements requested which must be less than or equal to ``available()``
        :type n: ``cardinal``
        :return: an array of ``Id`` elements.The length of the array is less than or equal to the number specified.
        :rtype: ``osid.id.Id``
        :raise: ``IllegalState`` -- no more elements available in this list
        :raise: ``OperationFailed`` -- unable to complete request

        """
        return # osid.id.Id


