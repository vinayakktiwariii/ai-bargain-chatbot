import os
import sys

# Add the project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bargain_project.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# For Vercel
app = application
