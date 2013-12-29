# -*- coding: utf-8 -*-
"""Ontology Open Service Interface Definitions
ontology version 3.0.0

The Ontology OSID is an auxiliary service used to define subject matter
that can be related to ``OsidObjects``. Ontologies are an alternative to
tagging where structure, restricted vocabulary, or localization of topic
names are desired.

Subjects

``Subjects`` are used to represent a topic and can be organized in a
hierarchy to form an ontology.

Relevancies

``Subjects`` are related to OSID ``Ids`` with a ``Relevancy``. A
``Relevancy`` is an ``OsidRelationship``.

Ontology Cataloging

``Subjects`` and ``Relevancies`` are organized into ``Ontology``
catalogs.

An external ``Id`` may be mapped to an ``Ontology``. This mapping allows
``OsidCatalogs`` to relate to a specific and sharable ``Ontology`` to
constrain a set of ``Subjects`` that may be relevant to a collection of
external ``OsidObjects``.

Sub Packages

The Ontology OSID includes a rules subpackage for managing rules to
enable subject relevancies and an Ontology Batch OSID for managing
``Subjects,``  ``Relevancies,`` and ``Ontologies`` in bulk.

"""