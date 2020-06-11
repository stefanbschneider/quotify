# Django Backend

Mostly based on the [Django tutorial](https://docs.djangoproject.com/en/3.0/intro/tutorial01/).

Currently includes:

* The quotify project
* The polls app from the tutorial

## Development

### Django

Relevant Django CLI commands.

* `python manage.py runserver`: Start dev server (run from within `quotify`)
* `python manage.py check`: Check for problems in the project

#### Setup new project or app

* `django-admin startproject mysite`: Create a new project (here: `quotify`)
* `python manage.py startapp polls`: Create a new app `polls`
* Adding the app in `quotify/settings.py/INSTALLED_APPS`

#### DB Setup or changes

* Change models in `models.py` (per app, eg, `polls`)
* `python manage.py makemigrations polls`: Create migrations for given/changed models, here, in `polls/models.py` 
* `python manage.py migrate`: Setup & sync DB by applying migrations. Can safely be run again - won't repeat actions twice.
* (`python manage.py sqlmigrate polls 0001`: Translate Django migrations to SQL commands (printed out; not yet applied to DB))
