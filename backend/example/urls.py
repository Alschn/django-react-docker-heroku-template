from django.urls import path

from .views import UppercaseTextAPIView

urlpatterns = [
    path('uppercase/', UppercaseTextAPIView.as_view(), name='uppercase_text'),
]
