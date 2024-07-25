from django.contrib import admin
from core.models import Resource, Newsletter

class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'cat')

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('date_added', 'name', 'email')

admin.site.register(Resource, ResourceAdmin)
admin.site.register(Newsletter, NewsletterAdmin)


