# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u2700976/data/www/ddshop.pro/myshop')
sys.path.insert(1, '/var/www/u2700976/data/www/ddshop.pro/venv/lib/python3.10/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'myshop.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
