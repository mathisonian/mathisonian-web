mathisonian
=====

An annotation tool for annotating.

Dependencies
----

* Scss / sass - Install sass, bro ```gem install sass```
* pip
* virtualenv - ```pip install virtualenv```
* mysql - only used on production, but you need it to install the ```python-mysql``` dependency. To install on osx do a ```brew install mysql```
* sqlite - the database used locally. probably is already installed


Running Locally
----

1. Create a virtualenv in your git directory (don't worry, it will be ignored on checkins) -- ```virtualenv env```
2. Install all the requirements (ensure ```env``` is active by running "env/bin/activate") -- ```pip install -r var/etc/requirements.txt```
3. Run the celery tasks: ```DJANGO_LOCAL=True ./manage.py celeryd -v 2 -B -E -l INFO```
4. Run the server in local mode -- ```var/bin/run_local.sh``` or ```DJANGO_LOCAL=True python manage.py runserver```
5. Visit <http://localhost:8000/>

Test Users
----

We automatically create some test data including three test users (testuser1, testuser2, and testuser3).

The three users have the same password: "testuser".
