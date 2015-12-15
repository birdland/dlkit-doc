

Objects
=======


Type Form
---------

.. py:class:: TypeForm(abc_type_objects.TypeForm, osid_objects.OsidForm)
    This form provides a means of updating various fields in the ``Type``.


    Note that the domain, authority and identifier are part of the
    ``Type`` identification, and as such not modifiable.





    .. py:method:: get_display_name_metadata():
        :noindex:


    .. py:attribute:: display_name_metadata
        :noindex:


    .. py:method:: set_display_name(display_name):
        :noindex:


    .. py:method:: clear_display_name():
        :noindex:


    .. py:attribute:: display_name
        :noindex:


    .. py:method:: get_display_label_metadata():
        :noindex:


    .. py:attribute:: display_label_metadata
        :noindex:


    .. py:method:: set_display_label(display_label):
        :noindex:


    .. py:method:: clear_display_label():
        :noindex:


    .. py:attribute:: display_label
        :noindex:


    .. py:method:: get_description_metadata():
        :noindex:


    .. py:attribute:: description_metadata
        :noindex:


    .. py:method:: set_description(description):
        :noindex:


    .. py:method:: clear_description():
        :noindex:


    .. py:attribute:: description
        :noindex:


    .. py:method:: get_domain_metadata():
        :noindex:


    .. py:attribute:: domain_metadata
        :noindex:


    .. py:method:: set_domain(domain):
        :noindex:


    .. py:method:: clear_domain():
        :noindex:


    .. py:attribute:: domain
        :noindex:


Type List
---------

.. py:class:: TypeList(abc_type_objects.TypeList, osid_objects.OsidList)
    Like all ``OsidLists,`` ``TypeList`` provides a means for accessing ``Type`` elements
        sequentially
    either one at a time or many at a time.


    Examples: while (tl.hasNext()) { Type type = tl.getNextType(); }




    or
      while (tl.hasNext()) {
           Type[] types = tl.getNextTypes(tl.available());
      }









    .. py:method:: get_next_type():
        :noindex:


    .. py:attribute:: next_type
        :noindex:


    .. py:method:: get_next_types(n):
        :noindex:


