.. _basic-usage:

Basic DLKit Usage
=================

Runtimes and basic DLKit usage are also covered in the sample :ref:`learning-tutorial`.
The information is discussed here in a more general sense. The examples below
explicitly use the Django runtime, but you can modify them to suit your custom
runtime.

Configuring Runtimes
--------------------

To access ``managers`` using a runtime, you first need to create
a user proxy, which wraps the user object and allows DLKit to calculate
authorizations. You then pass the proxy into the runtime and request managers.::

    from dlkit_django import RUNTIME, PROXY_SESSION

    condition = PROXY_SESSION.get_proxy_condition()
    condition.set_http_request(request)
    proxy = PROXY_SESSION.get_proxy(condition)

    lm = RUNTIME.get_service_manager('LEARNING', proxy)

Service Managers and Catalogs
-----------------------------

In the ``services`` convenience layer, you typically deal with two objects for each service,
the ``manager`` and a ``catalog``, which subclass a subset of OSID classes. This means that you
do not have to worry about managing OSID sessions -- this is managed for you and simplifies
your interactions with DLKit.

Service Managers
^^^^^^^^^^^^^^^^
Service managers typically give you access to all methods that do not require a specific
catalog. For example, the ``LearningManager`` lets you create, update, query, and delete
``ObjectiveBanks`` in the ``learning`` service.::

    bank = lm.get_objective_bank(bank_id)

Service Catalogs
^^^^^^^^^^^^^^^^
The catalogs you get back from a ``service manager`` typically give you access too
all objects within that catalog. So an ``ObjectiveBank`` lets you create, update, query,
and delete learning objectives and activities.::

    objectives = bank.get_objectives()

Creating and Updating objects
-----------------------------

To create or update an object, DLKit uses forms.::

    form = lm.get_objective_bank_form_for_create([])
    form.display_name = "My new test bank"
    new_bank = lm.create_objective_bank(form)

The optional parameter (on creation) allows you to specify which record extensions, if any,
you want applied to the object. For example, an Open edX-type objective bank might have
additional methods that allow you to export content in OLX format.

Once you have an object's ``id``, you can also update it with a form.::

    form = lm.get_objective_bank_form_for_update(bank_id)
    form.description = "For testing with"
    updated_bank = lm.update_objective_bank(form)

To update objects within a catalog, you would do the same thing, but via a ``catalog`` object.::

    form = bank.get_objective_form_for_create([])
    form = bank.get_objective_form_for_update(objective_id)

