======
README
======

This is the repository for the Noisebridge Python class project.


Installation using buildout
===========================

  # Get pyclass-project from github
  git clone git@github.com:noisebridge/pyclass-project.git

  # Generate the project buildout environment
  cd pyclass-project
  python bootstrap.py
  ./bin/buildout

  # Add the environment to the shell PATH
  export PATH=`pwd`/bin:$PATH

  # Create the pinax project mysite
  pinax-admin setup_project --allow-no-virtualenv -b basic mysite

  # Patch settings.py for mysite to work in the environment
  sed -ri 's/^import posixpath/import posixpath\nimport sys/' mysite/settings.py
  sed -ri 's#DEBUG = True#sys.executable = PROJECT_ROOT + "/../bin/python"\n\nDEBUG = True#' mysite/settings.py


Running the project
===================

  # Create mysite database
  cd mysite
  python manage.py syncdb

  # Launch mysite django application
  python manage.py runserver


Pinax documentation using pip
=============================

Alternatively, you can follow their instructions to create a virtual
environment with Pinax:
http://pinax.readthedocs.org/en/latest/gettingstarted.html


Issues found
============

Pinax is designed to use pip/virtualenv. Here are some issues that appeared
when using buildout instead of pip/virtualenv.


buildout
--------

* dependency versions where not matched when trying to build the pinax project
  itself
- Fixed changing [buildout]/find-links and [versions]

* Cleanup project dependencies
- Removed most dependencies not needed to launch a basic pinax project

* pip script dependency missing. pip is a pinax-admin dependency.
- Added pip in [interpreter]/scripts


bash
----

* buildout creates an (almost) fully contained environment. As pinax (and
  Django) depends on the shell environment, it is needed to update its PATH
- Added   export PATH=`pwd`/bin:$PATH   while in the pinax project directory


pinax
-----

* Prevent pinax-admin dependency on virtualenv
- Added --allow-no-virtualenv  on pinax-admin call

* Django complains Pinax is not installed, even though it is correctly deployed
- Configured django (modifying settings.py) to use buildout patched python
  interpreter
