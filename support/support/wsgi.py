import os
import sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support.settings')

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../esupport'))

application = get_wsgi_application()
