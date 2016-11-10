'''Models are registered here'''
from django.contrib import admin
from frijay.models import User
from frijay.models import Event


# Register your models here.
admin.site.register(User)
admin.site.register(Event)
