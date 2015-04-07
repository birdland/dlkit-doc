# -*- coding: utf-8 -*-
"""Dictionary Open Service Interface Definitions
dictionary version 3.0.0

The Dictionary OSID manages key/value pairs. A key and a value may be of
an arbitrary type. Dictionaries may be used to support a Locale or
Configuration OSID, or may be used to provide any dynamic translation or
conversion. The Dictionary OSID is a powerful tool for abstracting and
simplifying applications and other OSID implementations.

Entries

An ``Entry`` is indexed by a key and may contain multiple values of
different types. The key, key type, and value type must be unique. The
interpretation of the value and key are specified through the value type
and key type.

Dictionary

``Entries`` may be organized into federatable ``OsidCatalogs`` called
``Dictionaries``.

Basic Example:
  EntryLookupSession lookupSession = mgr.getEntryLookupSession();
  string definition = (string) lookupSession.getEntry("gambrel", strType, strType);



Federated Example:
  DictionaryLookupSession dictLookupSession = mgr.getDictionaryLookupSession();
  Dictionary dict = dictLookupSession.getDictionary(dict_id);
  EntryLookupSession lookupSession = mgr.getEntryLookupSessionForDictionary(dict);
  JpegImage jpg = lookupSession.getEntry(tiffImage, tiffType, jpegType);



"""