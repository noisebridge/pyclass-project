======
README
======

This is the repository for the Noisebridge Python class project.


Installation using buildout
===========================
To install run the following commands

1. Clone Repo from github
::

    git clone git@github.com:noisebridge/pyclass-project.git
    cd pyclass-project

2. Run the bootstrap to setup the environment.
::
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



