Tutorial: DLKit Learning Service Basics
=======================================

This tutorial is under development. It focuses on aspects of the ``Learning`` service. At the
time of this writing, MIT's Office of Digital Learning has launched its Python-based OSID 
development in support of the MIT Core Concept Catalog (MC3_) project starting with the OSID
``Learning`` package definition.  As a result, this tutorial uses examples primarily from this 
particular service, which deals with managing learning objectives, learning paths and 
relationships between learning objectives and educational assets, assessments, etc.

.. _MC3: http://mc3.mit.edu/

All of the other DLKit Interface Specifications build on most of the 
same patterns outlined in this tutorial, beginning with loading a service manager.

Loading the Learning Manager
----------------------------

All consumer applications wishing to use the DLKit Learning service should start by instantiating 
the ``LearningManager``::
 
    import dlkit
    from dlkit.services.learning import LearningManager
    lm = LearningManager()
    
Everything you need to do within the learning service can now be
accessed through this manager. An OSID ``Manager`` is used like a factory, providing all
the other objects necessary for using the service. You should never try to instantiate any 
other OSID object directly, even if you know where its class definition resides.

The simplest thing you can do with a manager is to inspect its ``display_name`` and ``description`` 
methods. Note that DLKit always returns user-readable strings  as ``DisplayText``
objects. The actual text is available via the ``get_text()`` method. 
Other ``DisplayText`` methods return the ``LanguageType``, ``ScriptType`` and
``FormatType`` of the text to be displayed::
    
    print "Learning Manager successfully instantiated:"
    print "  " + lm.get_display_name().get_text()
    print "  " + lm.get_description().get_text()
    print ("  (this description was written using the " + 
        lm.get_description().get_language_type().get_display_label().get_text() + 
        " language)\n")

Results in something that looks like this::

    Learning Manager successfully instantiated:
      MC3 Learning Service
      OSID learning service implementation of the MIT Core Concept Catalog (MC3)
      (this description was written using the English language)

      # Note that the implementation name and description may be different for you. 
      # It will depend on which underlying service implementation your dlkit library is
      # configured to point to.  More on this later

Alternatively, the Python OSID service interfaces also specify 
property attributes for all basic "getter" methods, so the above 
could also be written more Pythonically as::

    print "Learning Manager successfully instantiated:"
    print "  " + lm.display_name.text
    print "  " + lm.description.text
    print ("  (this description was written using the " + 
        lm.description.language_type.display_label.text + " language)\n")

For the remainder of this tutorial we will use the property attributes
wherever available.

Looking up Objective Banks
--------------------------

Managers encapsulate service profile information, allowing a consumer 
application to ask questions about which functions are supported in the underlying 
service implementations that it manages::
    
    if lm.supports_objective_bank_lookup():
        print "This Learning Manager can be used to lookup ObjectiveBanks"
    else:
        print "What a lame Learning Manager. It can't even lookup ObjectiveBanks"

The ``LearningManager`` also provides methods for getting ``ObjectiveBanks``.
One of the most useful is get_objective_banks(), which will return an iterator 
containing all the banks known to the underlying implementations.  This is 
also available as a property, so treating ``objective_banks`` as an 
attribute works here too::

    if lm.supports_objective_bank_lookup():
        banks = lm.objective_banks
        for bank in banks:
            print bank.display_name.text
    else:
        print "Objective bank lookup is not supported."

This will print a list of the names of all the banks, which can be thought of as catalogs
that contain learning objectives and other related information.  At the time of this writing
the following resulted::

    Crosslinks
    Chemistry Bridge
    i2.002
    Python Test Sandbox
    x.xxx
    
Note that the OSIDs specify to first ask whether a functional area is supported 
before trying to use it.  However, if you wish to adhere to the Pythonic EAFP (easier 
to ask forgiveness than permission) programming style, managers will throw an 
``Unimplemented`` exception if support is not available::

    try:
        banks = lm.objective_banks
    except Unimplemented:
        print "Objective bank lookup is not supported."
    else:
        for bank in banks:
            print bank.display_name.text

The object returned from the call to ``get_objective_banks()`` is an
``OsidList`` object, which as you can see from the example is just a Python iterator. 
Like all iterators it is "wasting", meaning that, unlike a Python ``list`` it 
will be completely used up and empty after all the elements have been retrieved. 

Like any iterator an ``OsidList`` object can be cast as a more persistent Python 
list, like so::

    banks = list(obls.objective_banks)

Which is useful if the consuming application needs to keep it around for a while.
However, when we start dealing with ``OsidLists`` from service implementations which
may return very large result sets, or where the underlying data changes often, casting
as a ``list`` may not be wise.  Developers are encouraged to treat these as
iterators to the extent possible, and refresh from the session as necessary.

You can also inspect the number of available elements in the expected way::

    len(obls.objective_banks)   
        # or
    banks = obls.objective_banks
    len(banks)

And walk through the list one-at-a-time, in ``for`` statements, or by calling ``next()``::

    banks = lm.objective_banks
    crosslinks_bank = banks.next() # At the time of this writing, Crosslinks was first
    chem_bridge_bank = banks.next() # and Chemistry Bridge was second

OSID Ids
--------

To begin working with OSID *objects*, like ``ObjectiveBanks`` it is important to understand 
how the OSIDs deal with identity.  When an OSID object is asked for its id
an OSID ``Id`` object is returned.  This is *not a ``string``*.  It is the unique identifier object
for the OSID object.  Any requests for getting a specific object by its unique identifier will be
accomplished through passing this ``Id`` object back through the service.

``Ids`` are obtained by calling an OSID object's ``get_id()`` method,
which also provides an ``ident`` attribute property associated with it for convenience
(``id`` is a reserved word in Python so it is not used)

.. currentmodule:: dlkit.osid.objects
.. autosummary::

    OsidObject.ident

So we can try this out::

    crosslinks_bank_id = crosslinks_bank.ident
    chem_bridge_bank_id = chem_bridge_bank.ident
    
``Ids`` can be compared for equality::

    crosslinks_bank_id == chem_bridge_bank_id
        # should return False
        
    crosslinks_bank_id in [crosslinks_bank_id, chem_bridge_bank_id]
        # should return True

If a consumer wishes to persist the identifier then it should serialize the
returned ``Id`` object, using pickle or something similar, so as to
be able to get the object back at a later date.

Once an application has its hands on an ``Id`` object it can go ahead and
retrieve the corresponding Osid Object through a Lookup Session::

    crosslinks_bank_redux = obls.get_objective_bank(crosslinks_bank_id)

We now have two *different* objects representing the *same* Crosslinks bank,
which can be determined by comparing ``Ids``::

    crosslinks_bank_redux == crosslinks_bank
        # should be False
        
    crosslinks_bank_redux.ident == crosslinks_bank_id
        # should be True

Looking up Objectives
---------------------

ObjectiveBanks provide methods for looking up and retrieving learning 
``Objectives``, in bulk, by ``Id``, or by ``Type``.  Some of the more useful
methods include:

.. currentmodule:: dlkit.services.learning
.. autosummary::

    ObjectiveBank.can_lookup_objectives
    ObjectiveBank.objectives
    ObjectiveBank.get_objective
    ObjectiveBank.get_objectives_by_genus_type

So let's try to find an ``Objective`` in the Crosslinks bank with a display name of
"Definite integral".  (Note, that there are also methods for
querying ``Objectives`` by various attributes. More on that later.)::

    for objective in crosslinks_bank:
        if objective.display_name.text == 'Definite integral':
            def_int_obj = objective

Now we have our hands on an honest-to-goodness learning objective as defined by an 
honest-to-goodness professor at MIT!

Authorization Hints
-------------------

Many service implementations will require *authentication* and *authorization* for
security purposes *(authn/authz)*.  Authorization checks will be done when the consuming application
actually tries to invoke a method for which authz is required, and if
its found that the currently logged-in user is not authorized, then the implementation
will raise a ``PermissionDenied`` error.

However, sometimes its nice to be able to check in advance whether or not the user
is likely to be denied access.  This way a consuming application can decide, for
instance, to hide or "gray out" UI widgets for doing un-permitted functions. This
is what the methods like ``can_lookup_objectives`` are for.  They simply return a
``boolean``.

The Objective Object
--------------------

``Objectives`` inherit from ``OsidObjects`` (``ObjectiveBanks`` do too, by the way),
which means there are a few methods they share with all other ``OsidObjects`` defined by
the specification

.. currentmodule:: dlkit.osid.objects
.. autosummary::

    OsidObject.display_name
    OsidObject.description
    OsidObject.genus_type

The ``display_name`` and ``description`` attributes work exactly like they did for 
``ObjectiveBanks`` and both return a ``Displaytext`` object that can be interrogated
for its text or the format, language, script of the text to be displayed. We'll get 
to ``genus_type`` in a little bit

Additionally ``Objectives`` objects can hold some information particular to the kind
of data that they manage:

.. currentmodule:: dlkit.learning.objects
.. autosummary::

    Objective.has_assessment
    Objective.assessment
    Objective.assessment_id
    Objective.has_cognitive_process
    Objective.cognitive_process
    Objective.cognitive_process_id
    Objective.has_knowledge_category
    Objective.knowledge_category
    Objective.knowledge_category_id

OSID Types
----------

The OSID specification defines ``Types`` as a way to indicate additional agreements
between service consumers and service providers. A Type is similar to an Id but 
includes other data for display and organization:

.. currentmodule:: dlkit.type.primitives
.. autosummary::

    Type.display_name
    Type.display_label
    Type.description
    Type.domain

``Types`` also include identification elements so as to uniquely identify one ``Type``
from another:

.. autosummary::

    Type.authority
    Type.namespace
    Type.identifier

Consuming applications will often need to persist ``Types`` for future use. 
Persisting a type reference requires persisting all three of these identification 
elements.

For instance the MC3 service implementation supports two different types of 
``Objectives``, which help differentiate between *topic* type objectives and  
*learning outcome* type objectives.  One way to store, say, the topic type for
future programmatic reference might be to put it in a dict::

    OBJECTIVE_TOPIC_TYPE = {
        'authority': 'MIT-OEIT',
        'namespace': 'mc3-objective',
        'identifier': 'mc3.learning.topic'
        }

The OSIDs also specify functions for looking up types that are defined
and/or supported, and as one might imagine, there is ``TypeLookupSession`` specifically
designed for this purpose.  This session, however, is not defined in the *learning*
service package, it is found in the *type* learning package, which therefore requires
a ``TypeManager`` be instantiated.  Again, like we did with the ``LearningManger``,
its a good idea to store a reference to the module that contains the ``TypeManger``
class in a settings file or some-such::

    TYPE_MANAGER_MODULE = 'managers'
    ...
    ...
    import importlib
    manager_module = importlib.import_module(TYPE_MANAGER_MODULE)
    tm = manager_module.TypeManager()
    ...
    if tm.supports_type_lookup():
        tls = tm.get_type_lookup_session()

(Note that for the service implementations used in this tutorial, both the
``LearningManger`` and ``TypeManager`` classes happen to be in the same module,
but this will not always be the case)

The ``TypeLookupSession`` provides a number of ways to get types, two of which are
sufficient to get started:

.. currentmodule:: dlkit.type.sessions
.. autosummary::

    TypeLookupSession.types
    TypeLookupSession.get_type

For kicks, let's print a list of all the ``Types`` supported by the implementation::

    for typ in tls.types:
        print typ.display_label.text
    
    # For the MC3 implementation this should result in a very long list

Also, we can pass the ``dict`` we created earlier to the session to get the actual
``Type`` object representing the three identification elements we persisted::

    topic_type = tls.get_type(**OBJECTIVE_TOPIC_TYPE)
    print topic_type.display_label.text + ': ' + topic_type.description.text
    
    # This should print the string 'Topic: Objective that represents a learning topic'

MORE TO COME...