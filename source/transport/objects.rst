.. currentmodule:: dlkit.transport.objects
.. automodule:: dlkit.transport.objects

Objects
=======


Endpoint List
-------------

.. autoclass:: EndpointList
   :show-inheritance:

   .. autoattribute:: EndpointList.next_endpoint

   .. automethod:: EndpointList.get_next_endpoints



Request
-------

.. autoclass:: Request
   :show-inheritance:

   .. autoattribute:: Request.id

   .. automethod:: Request.get_request_record



Response
--------

.. autoclass:: Response
   :show-inheritance:

   .. automethod:: Response.ok

   .. autoattribute:: Response.status_message

   .. automethod:: Response.get_response_record



Data Input Stream
-----------------

.. autoclass:: DataInputStream
   :show-inheritance:

   .. automethod:: DataInputStream.at_end_of_stream

   .. automethod:: DataInputStream.available

   .. automethod:: DataInputStream.skip

   .. automethod:: DataInputStream.read

   .. automethod:: DataInputStream.close



Data Output Stream
------------------

.. autoclass:: DataOutputStream
   :show-inheritance:

   .. automethod:: DataOutputStream.write

   .. automethod:: DataOutputStream.write_stream

   .. automethod:: DataOutputStream.close



