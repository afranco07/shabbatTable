from __future__ import unicode_literals
from django.db import models

# Create your models here.
#Super User :  frijay
#Pass :        frijay_pass

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=60)

    def __str__(self):
        return self.first_name