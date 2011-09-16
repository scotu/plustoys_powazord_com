import os, sys

# activate virtualenv
activate_this = os.path.expanduser("/home/scotu/.virtualenvs/plustoys.powazord.com/bin/activate_this.py")
execfile(activate_this, dict(__file__=activate_this))

# tell django where our settings module is
sys.path.insert(0, os.path.expanduser("/home/scotu/.virtualenvs/plustoys.powazord.com/sources/plustoys_powazord_com/plustoys"))
os.environ['DJANGO_SETTINGS_MODULE'] = 'plustoys.settings'

# run django
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
