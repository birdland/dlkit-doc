.. currentmodule:: dlkit.services.transport


Endpoint
========


Endpoint
--------

.. autoclass:: Endpoint
   :show-inheritance:

   .. automethod:: Endpoint.get_endpoint_record



Outbound Stream Methods
-----------------------

   .. autoattribute:: Endpoint.endpoint_id

   .. autoattribute:: Endpoint.endpoint

   .. automethod:: Endpoint.send_data

   .. automethod:: Endpoint.has_data_available

   .. automethod:: Endpoint.receive_data



Inbound Stream Methods
----------------------

   .. autoattribute:: Endpoint.endpoint_id

   .. autoattribute:: Endpoint.endpoint

   .. automethod:: Endpoint.register_callback



Outbound Message Methods
------------------------

   .. autoattribute:: Endpoint.endpoint_id

   .. autoattribute:: Endpoint.endpoint

   .. autoattribute:: Endpoint.request

   .. automethod:: Endpoint.make_request

   .. automethod:: Endpoint.send_request



Inbound Message Methods
-----------------------

   .. autoattribute:: Endpoint.endpoint_id

   .. autoattribute:: Endpoint.endpoint

   .. automethod:: Endpoint.register_callback



