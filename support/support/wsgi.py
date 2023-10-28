"""
WSGI config for support project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


current_directory = os.path.dirname(os.path.abspath(__file__))

esupport_directory = os.path.join(current_directory, 'esupport')

print("Ruta de esupport:", esupport_directory)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'support.support.settings')

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../esupport'))

application = get_wsgi_application()
