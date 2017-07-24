# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
import datetime
from department import Department


class Position(models.Model):
    """
    职位
    """
    name = models.CharField(max_length=20, verbose_name=u'职位')
    department = models.ForeignKey(Department, verbose_name=u'所属部门', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = u"职位名称"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
