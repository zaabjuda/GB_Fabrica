[![Build Status](https://travis-ci.org/zaabjuda/GB_Fabrica.svg)](https://travis-ci.org/zaabjuda/GB_Fabrica)
# GB_Fabrica
Guest Book Fabrica service. This is test job from RDS


HOW-TO RUN
===========

1. Use virtual env (pyvenv)
2. pip install -r requirements.txt
3. copy gbf/local_settings_template.py to gbf/local_settings.py and edit it
3. python manage.py test
5. python manage.py migrate
6. python manage.py collectstatic
7. python manage.py runserver 0.0.0.0:8000. Please use this host:port because facebook application configured for this.

