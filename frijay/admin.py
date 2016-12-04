'''Models are registered here'''
from django.contrib import admin
from frijay.models import Event, User


# Register your models here.
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(Event)
