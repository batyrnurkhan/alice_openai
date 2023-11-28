from django.urls import path
from .views import alice_webhook

urlpatterns = [
    path('alice/', alice_webhook),
]