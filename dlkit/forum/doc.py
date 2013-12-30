# -*- coding: utf-8 -*-
"""Reply Open Service Interface Definitions
forum version 3.0.0

The Forum OSID defines threaded diiscussion groups managing a set of
posts and replies.

Posts

A ``Post`` is an ``OsidObject`` that defines some text, a timestamp, and
a poster.

Replies

A ``Reply`` is similar to a ``Post`` but is in response to either a
``Post`` or another ``Reply``. A ``Reply`` is a ``Containable`` making
directly accessible any nested ``Replies`` outside of the session.

Posters

An ``Agent`` posts to a ``Forum`` or an ``Agent`` replies to a ``Post``.
The relationship between the ``Agent`` and its associated ``Resource``
is orchestrated within the Froum OSID. ``Posts`` and ``Replies`` reveal
both the posting ``Agent`` and the associated poster ``Resource``.

Forum Catalogs

Forums represent collections of ``Posts``. Forums may be created through
federation or by selecting ``Posts`` based on their attributes to create
a virtual catalog of Posts. ``Replies`` are always associated with their
``Posts`` and may not be cataloged independently.

Sub Packages

The Forum OSID contains a Forum Batch OSID for managing ``Posts`` and
``Replies`` in bulk.

"""