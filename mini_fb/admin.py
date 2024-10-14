# Register your models here.
# mini_fb/admin.py
# tell the admin we want to administer these models

from django.contrib import admin

from .models import *
# Register your models here.

# so we can see it in the admin 
admin.site.register(Profile)
admin.site.register(StatusMessage)
