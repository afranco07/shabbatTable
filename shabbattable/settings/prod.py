from shabbattable.settings.base import *
DEBUG = True
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
print(DATABASES['default'])
