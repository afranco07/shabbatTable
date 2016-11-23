from shabbattable.settings.base import *
DEBUG = True
#The following setting is for Heroku setup for Postgres.
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
