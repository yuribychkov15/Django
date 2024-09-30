"""
Our urls for the cs412 project
"""
from django.contrib import admin
from django.urls import path, include # include import needed to acess other apps
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("quotes/", include("quotes.urls")), ## we create the URL quotes/, ## and associate it with URLs in another file
    path("formdata/", include("formdata.urls")), # delegate work to the formdata url
    path("restaurant/", include("restaurant.urls")), # delegate work to the restaurant url
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)
