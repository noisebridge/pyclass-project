======
README
======

This is the repository for the Noisebridge Python class project.

Converting an existing installation to South
============================================
1. Sync the database to add the South table
::
    bin/django syncdb

2. Fake apply the intial migration
::
    bin/django migrate profiles 0001 --fake

This was the state of the database upon moving to South. It will pretend to apply the migration
and set this as the first migration point. Everything after this should work normally through the
standard process of applying migrations.

Using South to migrate
======================
Full documentation is available at http://south.readthedocs.org/en/latest/index.html


1. Make some changes to the model in the app *appname*

2. Create a migration

If you're changing an existing model use
::
    bin/django schemamigration appname --auto

however, if you're creating an entirely new model you'll want
::
    bin/django schemamigration appname --initial

3. Migrate your changes
::
    bin/django migrate appname

Multiple migrations will be made sequentially with this command if necessary.

Keep in mind that each app needs to have migrations created and applied individually. For example, if
git pulls migrations for two apps you'll need to run
::
    bin/django migrate app1
    bin/django migrate app2




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

4. Apply the intial migrations
::
    bin/django migrate profiles

5. Start the app
::
    bin/django runserver

6. Copy the http:// address into your web browser
::
i.e. Development server is running at http://127.0.0.1:8000/
