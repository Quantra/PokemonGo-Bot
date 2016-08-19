import time

# User can configure a choice of db backends if they want
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'sqlite.db',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Required do not change
INSTALLED_APPS = (
    'db',
)

# Use local time but no DST to ensure date/time integrity of DB
TIME_ZONE = time.tzname[0]

# Not used but required to run Django
SECRET_KEY = 'ponieswithmagicalpowers'
