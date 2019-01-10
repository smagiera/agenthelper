#!/bin/bash
sleep 2
python manage.py makemigrations
python manage.py migrate
gunicorn -b 0.0.0.0:80 agenthelper.wsgi
