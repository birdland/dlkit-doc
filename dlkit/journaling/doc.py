# -*- coding: utf-8 -*-
"""Journaling Open Service Interface Definitions
journaling version 3.0.0

The Journaling OSID defines an auxiliary service to manage journals and
journal entries for versioining.

Journal Entries

A journal entry represents a change to an object that can be another
OSID. The journal entry contains a time, a source ``Id`` and a version
``Id``. The source ``Id`` is the principal identifier for the journaled
object while the version ``Id`` can be used to retrieve a previous
version of the object by using its respective lookup session.

Journal Cataloging

Journal entries can be categorized into ``Journals,`` which may also be
organized into hierarchies for the purpose of federating journal
entries.

Agents & Resources

An ``Agent`` creates a ``JournalEntry``. The ``JournalEntry`` directly
exposes the related ``Resource`` to manage the orchestration with a
Resourtce OSID. Multiple ``Agents`` may be acting on behalf of a
``Resource``.

Orchestration

An orchestrated journaling service is one that creates a journaling
entry for each create and update of an ``OsidObject``. The orchestration
can be tricky since there is no means for connecting a ``JournalEntry``
to a specific ``OsidObject``. other than to arrange the ``Journals``
such that each ``Journal`` contains entries for a designated
``OsidObject`` interface where multiple ``OsidObjects`` are journaled.

The Journaling OSID is designed to provide a history of the data
contained within an OSID object, such as the evolution of an ``Asset``
or a ``Resource``. OSIDs tend to offer a complex array of relationships.
To capture a history of all relationships, states, and cataloging of an
``OsidObject,`` an OSID Provider can offer a rollback of an entire OSID
to a designated point in time.

Sub Packages

The Journaling OSID contains a Journaling Batch OSID for managing
``JournalEntries,``  ``Branches,`` and ``Journals`` in bulk.

"""