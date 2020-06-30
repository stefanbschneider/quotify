# Django Backend

Django Backend for the Quotify app.

Connect to MongoDB doesn't work. `djongo` is not recognized as backend. 
Also other custom backends for free cloud DBs are not available/working...
I'll stay with SQLite.

## Todo

* Allow sorting the index list: https://mdbootstrap.com/docs/jquery/tables/sort/
* Deploy on heroku
* Polish readme
* publish (public repo, link from website)

## Setup

```
pip install -r requirements.txt
```

## Usage

```
python manage.py runserver
```

Then go to http://127.0.0.1:8000/quotes

## Development

* `quotify` is the Django project
* `quotes` is the app

### Django

Relevant Django CLI commands.

#### General dev

* `python manage.py runserver`: Start dev server (run from within `quotify`)
* `python manage.py check`: Check for problems in the project
* `python manage.py shell`: Interactive Python shell with some extra configs for Django
    * For checking/testing the model API
    * Restart shell after making changes to model

#### Setup new project or app

* `django-admin startproject mysite`: Create a new project (here: `quotify`)
* `python manage.py startapp polls`: Create a new app `polls`
* Adding the app in `quotify/settings.py/INSTALLED_APPS`

#### DB Setup or changes

* Change models in `models.py` (per app, eg, `polls`)
* `python manage.py makemigrations polls`: Create migrations for given/changed models, here, in `polls/models.py` 
* `python manage.py migrate`: Setup & sync DB by applying migrations. Can safely be run again - won't repeat actions twice.
* (`python manage.py sqlmigrate polls 0001`: Translate Django migrations to SQL commands (printed out; not yet applied to DB))

#### Django admin

* `python manage.py createsuperuser`: Create new admin user
* Register models that should be managed by the admin under `app/admin.py`. Eg: `admin.site.register(Question)`
