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

3. sync the django database
::
    bin/django syncdb

4. Start the app
::
    bin/django runserver



