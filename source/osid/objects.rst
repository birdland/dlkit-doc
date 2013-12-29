.. currentmodule:: dlkit.osid.objects
.. automodule:: dlkit.osid.objects

Objects
=======


Osid Object
-----------

.. autoclass:: OsidObject
   :show-inheritance:

.. autoattribute:: OsidObject.display_name

.. autoattribute:: OsidObject.description

.. autoattribute:: OsidObject.genus_type

.. automethod:: OsidObject.is_of_genus_type



Osid Relationship
-----------------

.. autoclass:: OsidRelationship
   :show-inheritance:

.. automethod:: OsidRelationship.has_end_reason

.. autoattribute:: OsidRelationship.end_reason_id

.. autoattribute:: OsidRelationship.end_reason



Osid Catalog
------------

.. autoclass:: OsidCatalog
   :show-inheritance:





Osid Rule
---------

.. autoclass:: OsidRule
   :show-inheritance:

.. automethod:: OsidRule.has_rule

.. autoattribute:: OsidRule.rule_id

.. autoattribute:: OsidRule.rule



Osid Enabler
------------

.. autoclass:: OsidEnabler
   :show-inheritance:

.. automethod:: OsidEnabler.is_effective_by_schedule

.. autoattribute:: OsidEnabler.schedule_id

.. autoattribute:: OsidEnabler.schedule

.. automethod:: OsidEnabler.is_effective_by_event

.. autoattribute:: OsidEnabler.event_id

.. autoattribute:: OsidEnabler.event

.. automethod:: OsidEnabler.is_effective_by_cyclic_event

.. autoattribute:: OsidEnabler.cyclic_event_id

.. autoattribute:: OsidEnabler.cyclic_event

.. automethod:: OsidEnabler.is_effective_for_demographic

.. autoattribute:: OsidEnabler.demographic_id

.. autoattribute:: OsidEnabler.demographic



Osid Constrainer
----------------

.. autoclass:: OsidConstrainer
   :show-inheritance:





Osid Processor
--------------

.. autoclass:: OsidProcessor
   :show-inheritance:





Osid Governator
---------------

.. autoclass:: OsidGovernator
   :show-inheritance:





Osid Capsule
------------

.. autoclass:: OsidCapsule
   :show-inheritance:





Osid Form
---------

.. autoclass:: OsidForm
   :show-inheritance:

.. automethod:: OsidForm.is_for_update

.. autoattribute:: OsidForm.default_locale

.. autoattribute:: OsidForm.locales

.. automethod:: OsidForm.set_locale

.. autoattribute:: OsidForm.comment_metadata

.. autoattribute:: OsidForm.comment

.. automethod:: OsidForm.is_valid

.. autoattribute:: OsidForm.validation_messages

.. autoattribute:: OsidForm.invalid_metadata



Osid Identifiable Form
----------------------

.. autoclass:: OsidIdentifiableForm
   :show-inheritance:





Osid Extensible Form
--------------------

.. autoclass:: OsidExtensibleForm
   :show-inheritance:

.. autoattribute:: OsidExtensibleForm.required_record_types



Osid Browsable Form
-------------------

.. autoclass:: OsidBrowsableForm
   :show-inheritance:





Osid Temporal Form
------------------

.. autoclass:: OsidTemporalForm
   :show-inheritance:

.. autoattribute:: OsidTemporalForm.start_date_metadata

.. autoattribute:: OsidTemporalForm.start_date

.. autoattribute:: OsidTemporalForm.end_date_metadata

.. autoattribute:: OsidTemporalForm.end_date



Osid Subjugateable Form
-----------------------

.. autoclass:: OsidSubjugateableForm
   :show-inheritance:





Osid Aggregateable Form
-----------------------

.. autoclass:: OsidAggregateableForm
   :show-inheritance:





Osid Containable Form
---------------------

.. autoclass:: OsidContainableForm
   :show-inheritance:

.. autoattribute:: OsidContainableForm.sequestered_metadata

.. autoattribute:: OsidContainableForm.sequestered_date

.. autoattribute:: OsidContainableForm.sequestered



Osid Sourceable Form
--------------------

.. autoclass:: OsidSourceableForm
   :show-inheritance:

.. autoattribute:: OsidSourceableForm.provider_metadata

.. autoattribute:: OsidSourceableForm.provider

.. autoattribute:: OsidSourceableForm.branding_metadata

.. autoattribute:: OsidSourceableForm.branding

.. autoattribute:: OsidSourceableForm.license_metadata

.. autoattribute:: OsidSourceableForm.license



Osid Federateable Form
----------------------

.. autoclass:: OsidFederateableForm
   :show-inheritance:





Osid Operable Form
------------------

.. autoclass:: OsidOperableForm
   :show-inheritance:

.. autoattribute:: OsidOperableForm.enabled_metadata

.. autoattribute:: OsidOperableForm.enabled

.. autoattribute:: OsidOperableForm.disabled_metadata

.. autoattribute:: OsidOperableForm.disabled



Osid Object Form
----------------

.. autoclass:: OsidObjectForm
   :show-inheritance:

.. autoattribute:: OsidObjectForm.display_name_metadata

.. autoattribute:: OsidObjectForm.display_name

.. autoattribute:: OsidObjectForm.description_metadata

.. autoattribute:: OsidObjectForm.description

.. autoattribute:: OsidObjectForm.genus_type_metadata

.. autoattribute:: OsidObjectForm.genus_type



Osid Relationship Form
----------------------

.. autoclass:: OsidRelationshipForm
   :show-inheritance:





Osid Catalog Form
-----------------

.. autoclass:: OsidCatalogForm
   :show-inheritance:





Osid Rule Form
--------------

.. autoclass:: OsidRuleForm
   :show-inheritance:

.. autoattribute:: OsidRuleForm.rule_metadata

.. autoattribute:: OsidRuleForm.rule



Osid Enabler Form
-----------------

.. autoclass:: OsidEnablerForm
   :show-inheritance:

.. autoattribute:: OsidEnablerForm.schedule_metadata

.. autoattribute:: OsidEnablerForm.schedule

.. autoattribute:: OsidEnablerForm.event_metadata

.. autoattribute:: OsidEnablerForm.event

.. autoattribute:: OsidEnablerForm.cyclic_event_metadata

.. autoattribute:: OsidEnablerForm.cyclic_event

.. autoattribute:: OsidEnablerForm.demographic_metadata

.. autoattribute:: OsidEnablerForm.demographic



Osid Constrainer Form
---------------------

.. autoclass:: OsidConstrainerForm
   :show-inheritance:





Osid Processor Form
-------------------

.. autoclass:: OsidProcessorForm
   :show-inheritance:





Osid Governator Form
--------------------

.. autoclass:: OsidGovernatorForm
   :show-inheritance:





Osid Capsule Form
-----------------

.. autoclass:: OsidCapsuleForm
   :show-inheritance:





Osid List
---------

.. autoclass:: OsidList
   :show-inheritance:

.. automethod:: OsidList.has_next

.. automethod:: OsidList.available

.. automethod:: OsidList.skip



Osid Node
---------

.. autoclass:: OsidNode
   :show-inheritance:

.. automethod:: OsidNode.is_root

.. automethod:: OsidNode.has_parents

.. autoattribute:: OsidNode.parent_ids

.. automethod:: OsidNode.is_leaf

.. automethod:: OsidNode.has_children

.. autoattribute:: OsidNode.child_ids



