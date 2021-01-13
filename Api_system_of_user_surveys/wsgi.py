import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Api_system_of_user_surveys.settings')

application = get_wsgi_application()
