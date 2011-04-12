HelpIM 3.1
==========

Installation (Development)
++++++++++++++++++++++++++

These are preliminary instructions for how to setup a development
environment. This code is not meant to be used in production yet.

1) Download the app with git::

    $ git clone git://github.com/e-hulp/HelpIM.git

2) Download dependencies like this::

    $ cd HelpIM
    $ python bootstrap.py --distribute
    $ ./bin/buildout

  HelpIM runs on django 1.3 by default, if you want another version (say
  1.2.1), run::

    $ ./bin/buildout versions:django=1.2.1

4) Create a mysql database (and a user with full access rights)

5) Copy the development settings template::

    $ cp helpim/development.py{.example,}

6) Edit the development settings at ``helpim/development.py`` and make
   ``DATABASES`` match your DB settings

7) Initialize the DB::

    $ ./bin/django syncdb

  At that point you will be asked to create a first admin user. Remember
  those credentials they are essential.

8) Load the standard permissions and other standard data into the DB::

    $ ./bin/django loaddata setup_data

9) Run the dev server::

    $ ./bin/django runserver

10) Point your browser to http://localhost:8000/admin and login with the
    credentials from above.

Updating the setup data (Development)
++++++++++++++++++++++++++++++++++++++

With the command::

    dump_setup_data.sh > helpim/fixtures/setup_data.json

you can update the setup_data to the changes you have made in the
settings stored in the database. These changes can now be imported
by other developers.

.. note:: When adding models, it might be necessary to update dump_setup_data.sh
.. note:: There is deliberately chosen to not use 'initial_data.json', to avoid
          overwriting data when running syncdb.