.. currentmodule:: dlkit.services.transport
.. automodule:: dlkit.services.transport

Services
========


Transport Manager
-----------------

.. autoclass:: TransportManager
   :show-inheritance:





Transport Profile Methods
_________________

   .. automethod:: TransportManager.supports_visible_federation

   .. automethod:: TransportManager.supports_outbound_stream

   .. automethod:: TransportManager.supports_inbound_stream

   .. automethod:: TransportManager.supports_outbound_message

   .. automethod:: TransportManager.supports_inbound_message

   .. automethod:: TransportManager.supports_endpoint_lookup

   .. autoattribute:: TransportManager.endpoint_record_types

   .. automethod:: TransportManager.supports_endpoint_record_type

   .. autoattribute:: TransportManager.request_record_types

   .. automethod:: TransportManager.supports_request_record_type

   .. autoattribute:: TransportManager.response_record_types

   .. automethod:: TransportManager.supports_response_record_type



Endpoint Lookup
_______________

   .. automethod:: TransportManager.can_lookup_endpoints

   .. automethod:: TransportManager.use_comparative_endpoint_view

   .. automethod:: TransportManager.use_plenary_endpoint_view

   .. automethod:: TransportManager.get_endpoint

   .. automethod:: TransportManager.get_endpoints_by_ids

   .. automethod:: TransportManager.get_endpoints_by_genus_type

   .. automethod:: TransportManager.get_endpoints_by_parent_genus_type

   .. automethod:: TransportManager.get_endpoints_by_record_type

   .. automethod:: TransportManager.get_endpoints_by_provider

   .. autoattribute:: TransportManager.endpoints



Transport Proxy Manager
-----------------------

.. autoclass:: TransportProxyManager
   :show-inheritance:





Transport Profile Methods
_________________

   .. automethod:: TransportProxyManager.supports_visible_federation

   .. automethod:: TransportProxyManager.supports_outbound_stream

   .. automethod:: TransportProxyManager.supports_inbound_stream

   .. automethod:: TransportProxyManager.supports_outbound_message

   .. automethod:: TransportProxyManager.supports_inbound_message

   .. automethod:: TransportProxyManager.supports_endpoint_lookup

   .. autoattribute:: TransportProxyManager.endpoint_record_types

   .. automethod:: TransportProxyManager.supports_endpoint_record_type

   .. autoattribute:: TransportProxyManager.request_record_types

   .. automethod:: TransportProxyManager.supports_request_record_type

   .. autoattribute:: TransportProxyManager.response_record_types

   .. automethod:: TransportProxyManager.supports_response_record_type



Endpoint Lookup
_______________

   .. automethod:: TransportProxyManager.can_lookup_endpoints

   .. automethod:: TransportProxyManager.use_comparative_endpoint_view

   .. automethod:: TransportProxyManager.use_plenary_endpoint_view

   .. automethod:: TransportProxyManager.get_endpoint

   .. automethod:: TransportProxyManager.get_endpoints_by_ids

   .. automethod:: TransportProxyManager.get_endpoints_by_genus_type

   .. automethod:: TransportProxyManager.get_endpoints_by_parent_genus_type

   .. automethod:: TransportProxyManager.get_endpoints_by_record_type

   .. automethod:: TransportProxyManager.get_endpoints_by_provider

   .. autoattribute:: TransportProxyManager.endpoints



