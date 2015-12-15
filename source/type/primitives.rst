

Primitives
==========


Type
----

.. py:class:: Type(abc_type_primitives.Type, osid_markers.OsidPrimitive)
    The Type is a form of identifier that is primarily used to identify interface specifications.


    The ``Type`` differs from ``Id`` in that it offers display
    information and ``Types`` may be arranged in hierarchies to indicate
    an extended interface. Semantically, an ``Id`` identifies any OSID
    object while the ``Type`` identifies a specification.




    The components of the Type that make up its identification are:




      * identifier: a unique key or guid
      * namespace: the namespace of the identifier
      * authority: the isuer of the identifier








    Persisting a type reference means to persist the above
    identification elements. In addition to these identifier components,
    A ``Type`` mai also provide some additional metadata such as a name,
    description and domain.





    .. py:method:: get_display_name():
        :noindex:


    .. py:attribute:: display_name
        :noindex:


    .. py:method:: get_display_label():
        :noindex:


    .. py:attribute:: display_label
        :noindex:


    .. py:method:: get_description():
        :noindex:


    .. py:attribute:: description
        :noindex:


    .. py:method:: get_domain():
        :noindex:


    .. py:attribute:: domain
        :noindex:


    .. py:method:: get_authority():
        :noindex:


    .. py:attribute:: authority
        :noindex:


    .. py:method:: get_identifier_namespace():
        :noindex:


    .. py:attribute:: identifier_namespace
        :noindex:


    .. py:attribute:: namespace
        :noindex:


    .. py:method:: get_identifier():
        :noindex:


    .. py:attribute:: identifier
        :noindex:


