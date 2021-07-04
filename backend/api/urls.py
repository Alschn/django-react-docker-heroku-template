from django.urls import path

from .views import SimpleAPIView

urlpatterns = [
    path('test', SimpleAPIView.as_view(), name='test_api_view'),
]
