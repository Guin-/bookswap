from __future__ import unicode_literals

from django.db import models

from bookswap.users.models import User

class Book(models.Model):
    owner = models.ForeignKey(User)
    ISBN = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    requested = models.BooleanField()
    active = models.BooleanField()

    def __unicode__(self):
        return self.title

class Request(models.Model):
    pass
