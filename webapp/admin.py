from django.contrib import admin
from webapp.models import *

class сoffinList_admin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'photo')

admin.site.register(coffinList, сoffinList_admin)
