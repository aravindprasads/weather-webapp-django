# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class City(models.Model):
    
    name = models.CharField(max_length=25)


    def __str__(self):
        return self.name

