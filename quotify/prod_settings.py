""" Production Settings """

import os
import dj_database_url
from .settings import *


############
# SECURITY #
############

DEBUG = False

SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', SECRET_KEY)

ALLOWED_HOSTS = ['django-quotify.herokuapp.com']
