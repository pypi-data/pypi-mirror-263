DOCKER=True
ELASTICSEARCH_CONNECTION_OPTIONS = {
    "timeout": 30,
    "basic_auth": ("elastic", "84VC9b*QFVv1m6W2wiQ8"),
}  
DATABASES = {
    "default": {
        "ENGINE": "django.contrib.gis.db.backends.postgis",  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        "NAME": "arches",  # Or path to database file if using sqlite3.
        "USER": "postgres",  # Not used with sqlite3.
        "PASSWORD": "postgis",  # Not used with sqlite3.
        "HOST": "localhost",  # Set to empty string for localhost. Not used with sqlite3.
        "PORT": "5434",  # Set to empty string for default. Not used with sqlite3.
        "POSTGIS_TEMPLATE": "template_postgis",
    }
}
ELASTICSEARCH_HOSTS = [{"scheme": "http", "host": "localhost", "port": 9202}]
ARCHES_APPLICATIONS=()
