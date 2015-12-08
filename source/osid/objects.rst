
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



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Relationship
-----------------

.. autoclass:: OsidRelationship
   :show-inheritance:

   .. automethod:: OsidRelationship.has_end_reason

   .. autoattribute:: OsidRelationship.end_reason_id

   .. autoattribute:: OsidRelationship.end_reason



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Catalog
------------

.. autoclass:: OsidCatalog
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Rule
---------

.. autoclass:: OsidRule
   :show-inheritance:

   .. automethod:: OsidRule.has_rule

   .. autoattribute:: OsidRule.rule_id

   .. autoattribute:: OsidRule.rule



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



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



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Constrainer
----------------

.. autoclass:: OsidConstrainer
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Processor
--------------

.. autoclass:: OsidProcessor
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Governator
---------------

.. autoclass:: OsidGovernator
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Compendium
---------------

.. autoclass:: OsidCompendium
   :show-inheritance:

   .. autoattribute:: OsidCompendium.start_date

   .. autoattribute:: OsidCompendium.end_date

   .. automethod:: OsidCompendium.is_interpolated

   .. automethod:: OsidCompendium.is_extrapolated



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Capsule
------------

.. autoclass:: OsidCapsule
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Form
---------

.. autoclass:: OsidForm
   :show-inheritance:

   .. automethod:: OsidForm.is_for_update

   .. autoattribute:: OsidForm.default_locale

   .. autoattribute:: OsidForm.locales

   .. automethod:: OsidForm.set_locale

   .. autoattribute:: OsidForm.journal_comment_metadata

   .. autoattribute:: OsidForm.journal_comment

   .. automethod:: OsidForm.is_valid

   .. autoattribute:: OsidForm.validation_messages

   .. autoattribute:: OsidForm.invalid_metadata



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Identifiable Form
----------------------

.. autoclass:: OsidIdentifiableForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Extensible Form
--------------------

.. autoclass:: OsidExtensibleForm
   :show-inheritance:

   .. autoattribute:: OsidExtensibleForm.required_record_types



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Browsable Form
-------------------

.. autoclass:: OsidBrowsableForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Temporal Form
------------------

.. autoclass:: OsidTemporalForm
   :show-inheritance:

   .. autoattribute:: OsidTemporalForm.start_date_metadata

   .. autoattribute:: OsidTemporalForm.start_date

   .. autoattribute:: OsidTemporalForm.end_date_metadata

   .. autoattribute:: OsidTemporalForm.end_date



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Subjugateable Form
-----------------------

.. autoclass:: OsidSubjugateableForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Aggregateable Form
-----------------------

.. autoclass:: OsidAggregateableForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Containable Form
---------------------

.. autoclass:: OsidContainableForm
   :show-inheritance:

   .. autoattribute:: OsidContainableForm.sequestered_metadata

   .. autoattribute:: OsidContainableForm.sequestered



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



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



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Federateable Form
----------------------

.. autoclass:: OsidFederateableForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Operable Form
------------------

.. autoclass:: OsidOperableForm
   :show-inheritance:

   .. autoattribute:: OsidOperableForm.enabled_metadata

   .. autoattribute:: OsidOperableForm.enabled

   .. autoattribute:: OsidOperableForm.disabled_metadata

   .. autoattribute:: OsidOperableForm.disabled



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



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



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Relationship Form
----------------------

.. autoclass:: OsidRelationshipForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Catalog Form
-----------------

.. autoclass:: OsidCatalogForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Rule Form
--------------

.. autoclass:: OsidRuleForm
   :show-inheritance:

   .. autoattribute:: OsidRuleForm.rule_metadata

   .. autoattribute:: OsidRuleForm.rule



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



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



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Constrainer Form
---------------------

.. autoclass:: OsidConstrainerForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Processor Form
-------------------

.. autoclass:: OsidProcessorForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Governator Form
--------------------

.. autoclass:: OsidGovernatorForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Compendium Form
--------------------

.. autoclass:: OsidCompendiumForm
   :show-inheritance:

   .. autoattribute:: OsidCompendiumForm.start_date_metadata

   .. autoattribute:: OsidCompendiumForm.start_date

   .. autoattribute:: OsidCompendiumForm.end_date_metadata

   .. autoattribute:: OsidCompendiumForm.end_date

   .. autoattribute:: OsidCompendiumForm.interpolated_metadata

   .. autoattribute:: OsidCompendiumForm.interpolated

   .. autoattribute:: OsidCompendiumForm.extrapolated_metadata

   .. autoattribute:: OsidCompendiumForm.extrapolated



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid Capsule Form
-----------------

.. autoclass:: OsidCapsuleForm
   :show-inheritance:





Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



Osid List
---------

.. autoclass:: OsidList
   :show-inheritance:

   .. automethod:: OsidList.has_next

   .. automethod:: OsidList.available

   .. automethod:: OsidList.skip



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



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



Osid Methods
------------

   .. autoattribute:: OsidSession.locale

   .. automethod:: OsidSession.is_authenticated

   .. autoattribute:: OsidSession.authenticated_agent_id

   .. autoattribute:: OsidSession.authenticated_agent

   .. autoattribute:: OsidSession.effective_agent_id

   .. autoattribute:: OsidSession.effective_agent

   .. autoattribute:: OsidSession.date

   .. autoattribute:: OsidSession.clock_rate

   .. autoattribute:: OsidSession.format_type

   .. automethod:: OsidSession.supports_transactions

   .. automethod:: OsidSession.start_transaction



