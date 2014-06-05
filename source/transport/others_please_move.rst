.. currentmodule:: dlkit.transport.others_please_move
.. automodule:: dlkit.transport.others_please_move

Others_Please_Move
==================


Request
-------

.. autoclass:: Request
   :show-inheritance:

   .. autoattribute:: Request.id

   .. automethod:: Request.get_request_record



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



