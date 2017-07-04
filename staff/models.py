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
    department = models.ForeignKey(Department,name=u'所属部门',blank=True,null=True,on_delete=models.SET_NULL)

    class Meta:
        verbose_name = u"职位名称"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class Staff(models.Model):
    """
    职员信息
    """
    name = models.CharField(max_length=10,verbose_name=u'姓名')
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name=u'性别',
                              max_length=6)
    position = models.ForeignKey(Position,verbose_name=u'所属职位',blank=True,null=True,on_delete=models.SET_NULL)
    identity_card = models.CharField(max_length=18, verbose_name=u'身份证', null=True,blank=True,unique=True)
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码', null=True)

    class Meta:
        verbose_name = u"职员信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
