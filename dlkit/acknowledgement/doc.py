# -*- coding: utf-8 -*-
"""Acknowledgement Open Service Interface Definitions
acknowledgement version 3.0.0

The Acknowledgement OSID defines and relates credits such as authors or
creators to ``OsidObjects``.

Credits

``Credits`` are relationships between what is being credited and to what
the credit applies. The enttity being credited is represented by a
``Resource``. This service does not define the entity to which the
credit applies and instead references an OSID ``Id`` external to this
service. The ``Id`` is a reference to an entity managed outside this
service.

The external ``Id`` reference positions the Acknowledgement OSID as an
auxiliary service that can be orchestrated with other OSIDs to provide
acknowledgements with any ``OsidObject``. Resource is an abstract
interface used for a variety of purposes including people. The
Acknowledgement OSID this has a very abstract feel whose primary focus
is to manage the relationships.

As with many ``OsidRelationships,`` the genus Type can be used to
describe the nature of the relationship, such as a writer or
photographer. The ``CreditRecord`` may be used to capture data related
to the relatonship itself.

``OsidRelationships`` are temporal by including effective dates.

Billing Cataloging

``Credits`` are mapped to ``Billings`` for organization. ``Billings``
can be managed hierarchically to federate multiple collections of
``Credits`` .

"""