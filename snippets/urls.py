from django.urls import path

from .views import create_snippet


urlpatterns = [
    path('', create_snippet)
]