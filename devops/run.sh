#!/usr/bin/env bash

python manage.py migrate --noinput --settings=$DJANGO_SETTINGS_MODULE

python manage.py collectstatic --noinput

# debugging with default server uncomment this and comment the gunicorn one
#python manage.py runserver 0.0.0.0:3000, 0.0.0.0:80 --settings=$DJANGO_SETTINGS_MODULE
python manage.py runserver 0.0.0.0:3000 --settings=$DJANGO_SETTINGS_MODULE

#uncomment this line if you want to test with gunicorn
#exec  gunicorn -b 0.0.0.0:80 -b 0.0.0.0:3000 -b 0.0.0.0:3030 \
#      mobile_loans.wsgi \
#         --workers=5\
#         --log-level=info \
#         --log-file=-\
#         --access-logfile=-\
#         --error-logfile=-\
#         --timeout 30\
#         --reload