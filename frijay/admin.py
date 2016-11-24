'''Models are registered here'''
from django.contrib import admin
from frijay.models import Event
from frijay.models import User
from frijay.models import UserProfile


# Register your models here.
admin.site.unregister(User)
admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(Event)
