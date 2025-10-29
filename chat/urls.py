from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('negotiate/<int:product_id>/', views.negotiate, name='negotiate'),
]
