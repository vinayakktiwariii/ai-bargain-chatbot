"""
ASGI config for bargain_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""
"""
ASGI config for real-time WebSocket support
"""

"""
ASGI config for real-time WebSocket support
"""

import os
import django

# CRITICAL: Set settings and initialize Django FIRST
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bargain_project.settings')
django.setup()

# NOW import everything else (after django.setup())
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# Import routing AFTER django.setup()
import chat.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
