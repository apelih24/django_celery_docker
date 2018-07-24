#!/bin/sh
bash -c "python manage.py migrate django_celery_results && celery -A django_cel_doc worker -l info"