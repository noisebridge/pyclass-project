======
README
======

This is the repository for the Noisebridge Python class project.


Installation using buildout
===========================

::

  # Get pyclass-project from github
  git clone git@github.com:noisebridge/pyclass-project.git

  # Generate the project buildout environment
  cd pyclass-project
  python bootstrap.py
  ./bin/buildout


Running the project
===================

::

  # Create mysite database
  #note that bin/django acts similarly to a typical django cmd "python manage.py"
  cd mysite
  bin/django syncdb

  # Launch mysite django application
  bin/django runserver


Issues found
============



