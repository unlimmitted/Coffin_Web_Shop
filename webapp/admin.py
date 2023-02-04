from django.contrib import admin
from webapp.models import *


class CoffinListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'photo')


admin.site.register(CoffinList, CoffinListAdmin)


class ReviewListAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')


admin.site.register(ReviewList, ReviewListAdmin)
