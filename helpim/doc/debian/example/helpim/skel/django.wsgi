import os
import sys

sys.path[0:0] = ['/etc/helpim/sites/CHATX/']

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

