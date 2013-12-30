.. currentmodule:: dlkit.forum.receivers
.. automodule:: dlkit.forum.receivers

Receivers
=========


Post Receiver
-------------

.. autoclass:: PostReceiver
   :show-inheritance:

.. automethod:: PostReceiver.new_post

.. automethod:: PostReceiver.new_ancestor_post

.. automethod:: PostReceiver.new_descendant_post

.. automethod:: PostReceiver.changed_post

.. automethod:: PostReceiver.deleted_post

.. automethod:: PostReceiver.deleted_ancestor_post

.. automethod:: PostReceiver.deleted_descendant_post



Reply Receiver
--------------

.. autoclass:: ReplyReceiver
   :show-inheritance:

.. automethod:: ReplyReceiver.new_reply

.. automethod:: ReplyReceiver.changed_reply

.. automethod:: ReplyReceiver.deleted_reply



Forum Receiver
--------------

.. autoclass:: ForumReceiver
   :show-inheritance:

.. automethod:: ForumReceiver.new_forum

.. automethod:: ForumReceiver.new_ancestor_forum

.. automethod:: ForumReceiver.new_descendant_forum

.. automethod:: ForumReceiver.changed_forum

.. automethod:: ForumReceiver.deleted_forum

.. automethod:: ForumReceiver.deleted_ancestor_forum

.. automethod:: ForumReceiver.deleted_descendant_forum



