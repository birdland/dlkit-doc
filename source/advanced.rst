.. _advanced-usage:

Advanced DLKit Usage
====================

Sometimes you may need to use DLKit in a stricter OSID fashion, bypassing the
`services` convenience methods discussed in :ref:`basic-usage`. To use DLKit
in a more OSID-y way, you would manually manage the various admin / lookup / etc.
sessions, from either a service manager or a service catalog.

Currently, the main use case when you would need to manage sessions yourself
is if you want to look up objects without knowing their catalog IDs. For example,
you have an `objective_id` but not the `objective_bank_id` and need to grab the
objective. In the future, we plan to build that capability into the `services`
convenience layer, to reduce the need for manual session management.::

    ols = lm.get_objective_lookup_session()
    objective = ols.get_objective(objective_id)



