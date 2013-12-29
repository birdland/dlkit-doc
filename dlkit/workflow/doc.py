# -*- coding: utf-8 -*-
"""Workflow Open Service Interface Definitions
workflow version 3.0.0

The Workflow OSID provides a means for managing the flow of work. The
Workflow OSID is part of a service cluster that includes the Resourcing
OSID, Tracking OSID and Process OSID. The Workflow OSID provides an
overall view of the flow of work through a process.

Work

``Work`` is an abstract concept that indicates something to be worked on
by ``Resources`` (workers) in a workflow ``Process`` .

Steps

A ``Step`` is the primary component of a workflow process in which work
is performed. A ``Step`` may have required input conditions (or states)
that permit ``Work`` to enter a ``Step``. When the ``Work`` is completed
at a ``Step,`` the ``Step`` defines the ``State`` transition of the
``Work``. The valid next ``Steps`` in a ``Process`` is determined by the
accepted input ``States`` of the other ``Steps``.

A ``Step`` may have assigned ``Resources`` to perform the work. These
``Resources`` may be managed manually in the Workflow OSID or through
orchestration of the Resourcing OSID where the ``Process`` maps to a
``Job`` and the ``Work`` is the ``Work`` .

Processes

A ``Process`` is a set of ``Steps`` in a workflow. ``Work`` entering a
``Process`` is assigned an initial ``Step`` and an initial ``State`` as
defined by the ``Process``.

Both ``Processes`` and ``Steps`` are ``OsidGovernators`` that may be
operated through a set of rules to dynamically manage the workflow.

WorkflowEvents

``Work`` moving through a ``Process`` can be examined using
``WorkflowEvents``. Monitoring at a finer grained level can be performed
by orchestrating a Tracking OSID where a ``Step`` is a ``Queue`` and the
``Work`` is an ``Issue``.

Office Cataloging

``Work,``  ``Steps,`` and ``Processes`` may be organized into
federateable ``OsidCatalogs`` .

Sub Packages

The Workflow OSID includes a Workflow Rules OSID to manage the operation
of ``Processes`` and ``Steps`` and impose additional input constraints
on ``Steps``.

"""