This is the repository for the Noisebridge Python class project.


Installation Instructions
-------------------------

Checkout a copy from git, then run::

  > git clone git@github.com:noisebridge/pyclass-project.git
  > cd pyclass-project
  > python bootstrap.py
  > ./bin/buildout

To get Pinax running:

  > cd bin
  > ./pinax-admin setup_project -b ../<project name>
  > If the previous does not work, remove "../" and manually move the created folder to the main project directory
  > Follow the instructions here to create a virtual environment with Pinax: http://pinax.readthedocs.org/en/latest/gettingstarted.html#creating-a-project
  > You may end up unable to run manage.py due to not having certain packages.  This link should give a full list of what to install in the case you don't have them
