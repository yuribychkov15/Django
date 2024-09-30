## restaraunt/urls.py
## description: URL patterns for the restaurant app

from django.urls import path
from django.conf import settings
from . import views

# all of the URLs that are part of this app
urlpatterns = [
    path(r'', views.main, name="main"),
    path(r'confirmation', views.confirmation, name="confirmation"),
    path(r'order', views.order, name="order"),
]