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
    path("blog/", include("blog.urls")), # delegate work to the restaurant url
    path("mini_fb/", include("mini_fb.urls")), # delegate work to the mini_fb url
    path("voter_analytics/", include('voter_analytics.urls')), # delegate work to the voter_analytics url
    path("project/", include('project.urls')), # delegate work to the project url
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
