from django.urls import path

from .views import uppercase_text

urlpatterns = [
    path('uppercase_text', uppercase_text, name='uppercase_text'),
]
