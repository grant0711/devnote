"""Gunicorn *development* config file"""

wsgi_app = "devnote.wsgi:application"
loglevel = "debug"
workers = 1
bind = "0.0.0.0:8080"
reload = True