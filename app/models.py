# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class FilesModel(models.Model):
    file = models.FileField(upload_to='demo_files/%Y/%m/%d/')
    date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30, blank=True, null=True)

class ContentModel(models.Model):
    filed_ids = models.CharField(max_length=20)
    desc = models.CharField(max_length=200)


