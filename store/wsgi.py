import os

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jewelryshop.settings')
# vercel_app/settings.py
WSGI_APPLICATION = 'store.wsgi.app'
application = get_wsgi_application()

app = application