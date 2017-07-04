# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.

class Department(models.Model):
    """
    部门
    """
    name = models.CharField(max_length=20,verbose_name=u'部门名称')

    class Meta:
        verbose_name = u"部门名称"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name

class Position(models.Model):
    """
    职位
    """
    name = models.CharField(max_length=20, verbose_name=u'职位名称')
    department = models.ForeignKey(Department,name=u'所属部门',null=True,on_delete=models.SET_NULL)


class Staff(models.Model):
    """
    职员信息
    """
    pass