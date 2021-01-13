import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Api_system_of_user_surveys.settings')

application = get_asgi_application()
