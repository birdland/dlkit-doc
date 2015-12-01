Configuring DLKit
=================

DLKit requires the use of a runtime environment, from which you
configure the user proxy object, get managers, and define which
implementations are used for each service (among other things).
For example, you might use the built-in MongoDB ``learning``
service, or you may decide to use the MC3_ RESTful service,
Handcar.

.. _MC3: http://mc3.mit.edu

Two examples are available, one for Open edX and another for Django. You
can also build your own, using these as templates:

Open edX runtime: https://github.mit.edu/sei/dlkit_edx
Django runtime: https://github.mit.edu/sei/dlkit_django

Both runtimes require the addition of ``configs.py`` and
``registry.py`` files. These allow different instances of
DLKit to behave differently, depending on the project's needs.

**NOTE:** With the Django runtime, you can establish the configuration
values in your project's ``settings.py`` file, which is then referenced
in the runtime files below. This is for your convenience. You can
also configure the settings directly in the files below, as shown
in the Open edX runtime.

configs.py
----------

This file allows you to define various parameters used in the production
runtime as well as a testing runtime. The only required values are for
``BOOTSTRAP`` and ``SERVICE`` (and for running the DLKit tests,
``TEST_SERVICE``).

``SERVICE`` should point to the implementation you want to use for each
service (i.e. Handcar for the ``learning`` service, MongoDB for the

An example skeleton is included in the repository.


registry.py
-----------

Similar to ``setup.py``, this file includes the various entry points
for each service and implementation. For example, if you expect to use the ``grading``
service from the MongoDB implementation, you need to make sure it has
an entry in this file. An example skeleton is included in the repository.

An example::

    MANAGER_PATHS = {
        'service': {
            'ASSESSMENT': ('dlkit.services.assessment.AssessmentManager',
                           'dlkit.services.assessment.AssessmentManager'),
            'REPOSITORY': ('dlkit.services.repository.RepositoryManager',
                           'dlkit.services.repository.RepositoryManager'),
            'LEARNING': ('dlkit.services.learning.LearningManager',
                         'dlkit.services.learning.LearningManager'),
            'COMMENTING': ('dlkit.services.commenting.CommentingManager',
                           'dlkit.services.commenting.CommentingManager'),
            'RESOURCE': ('dlkit.services.resource.ResourceManager',
                         'dlkit.services.resource.ResourceManager'),
            'GRADING': ('dlkit.services.grading.GradingManager',
                        'dlkit.services.grading.GradingManager')
        },
        'mongo': {
            'ASSESSMENT': ('dlkit.mongo.assessment.managers.AssessmentManager',
                           'dlkit.mongo.assessment.managers.AssessmentProxyManager'),
            'REPOSITORY': ('dlkit.mongo.repository.managers.RepositoryManager',
                           'dlkit.mongo.repository.managers.RepositoryProxyManager'),
            'LEARNING': ('dlkit.mongo.learning.managers.LearningManager',
                         'dlkit.mongo.learning.managers.LearningProxyManager'),
            'COMMENTING': ('dlkit.mongo.commenting.managers.CommentingManager',
                           'dlkit.mongo.commenting.managers.CommentingProxyManager'),
            'RESOURCE': ('dlkit.mongo.resource.managers.ResourceManager',
                         'dlkit.mongo.resource.managers.ResourceProxyManager'),
            'GRADING': ('dlkit.mongo.grading.managers.GradingManager',
                         'dlkit.mongo.grading.managers.GradingProxyManager')
        },
        'authz_adapter': {
            'ASSESSMENT': ('dlkit.authz_adapter.assessment.managers.AssessmentManager',
                           'dlkit.authz_adapter.assessment.managers.AssessmentProxyManager'),
            'REPOSITORY': ('dlkit.authz_adapter.repository.managers.RepositoryManager',
                           'dlkit.authz_adapter.repository.managers.RepositoryProxyManager'),
            'LEARNING': ('dlkit.authz_adapter.learning.managers.LearningManager',
                         'dlkit.authz_adapter.learning.managers.LearningProxyManager'),
            'COMMENTING': ('dlkit.authz_adapter.commenting.managers.CommentingManager',
                           'dlkit.authz_adapter.commenting.managers.CommentingProxyManager'),
            'RESOURCE': ('dlkit.authz_adapter.resource.managers.ResourceManager',
                         'dlkit.authz_adapter.resource.managers.ResourceProxyManager'),
            'GRADING': ('dlkit.authz_adapter.grading.managers.GradingManager',
                        'dlkit.authz_adapter.grading.managers.GradingProxyManager')
        },
        },
        'handcar': {
            'LEARNING': ('dlkit.handcar.learning.managers.LearningManager',
                         'dlkit.handcar.learning.managers.LearningProxyManager')
        },
        'aws_adapter': {
            'REPOSITORY': ('dlkit.aws_adapter.repository.managers.RepositoryManager',
                           'dlkit.aws_adapter.repository.managers.RepositoryProxyManager')
        },
        'qbank_authz': {
            'AUTHORIZATION': ('qbank_authz.authorization.managers.AuthorizationManager',
                              'qbank_authz.authorization.managers.AuthorizationProxyManager')
        },
    }


handcar_configs.py
------------------

If you are using the `MC3 Handcar` learning service, then you will also
need to add in proxy agent keys for the appropriate service / server combination
in this file.

.. _MC3 Handcar: http://mc3.mit.edu