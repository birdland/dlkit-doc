.. dlkit documentation master file, created by
   sphinx-quickstart on Wed Oct  9 19:40:31 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to the DLKit documentation!
===================================

This documentation for the Digital Learning Toolkit (DLKit), like the toolkit itself,
is still under development. It currently covers only a small handful of the 180 service packages 
and over 10,000 educational service APIs that have been defined by MIT's Office of Digital Learning and
its collaborators to date.

The DLKit codebase is generated from the Open Service Interface Definitions (OSIDs), 
an extensive and growing suite of interface contract specifications that describe the 
integration points among the core services and components that make up modern educational systems.

Note that this documentation is intended for API consumers. However, at the heart of DLKit is an
integration stack that is even more closely aligned with the OSID specifications.  This has been
designed to allow third parties to extend the library with alternative or additional implementations 
of any of the defined services for the purposes of service integration, technology migration, 
service adaptation, etc. Documentation written for service implementers and system integrators,
including implementation notes and compliance information, will be provided elsewhere.

The complete OSID specification can be found at http://osid.org/specifications.

Currently, DLKit works with Python 2.6 and 2.7.

If you are interested in learning more about the DLKit Python libraries documented here,
please contact dlkit-info@mit.edu

Get DLKit
---------
The latest release of DLKit and related dependencies are available here: https://bitbucket.org/cjshaw/

Testing
-------
Unit tests and limited functional tests for DLKit are available here: https://github.mit.edu/sei/dlkit_tests

Contents:
---------

.. toctree::
   :maxdepth: 2

   introduction
   basic
   advanced
   configuration
   tutorial
   assessment/toc
   commenting/toc
   grading/toc
   hierarchy/toc
   learning/toc
   osid/toc
   proxy/toc
   relationship/toc
   repository/toc
   resource/toc
   type/toc


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

