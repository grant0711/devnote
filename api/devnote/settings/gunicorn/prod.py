"""Gunicorn *production* config file"""

wsgi_app = "devnote.wsgi:application"
loglevel = "info"
workers = 1
reload = False