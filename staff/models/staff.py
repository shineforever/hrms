# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from position import Position


class Staff(models.Model):
    """
    职员信息
    """
    EDUCATION_CHOICE = (
        ('1', '本科'),
        ('2', '研究生'),
        ('3', '博士')
    )

    POLITICAL_CHOICE = (
        ('1', '群众'),
        ('2', '团员'),
        ('3', '预备党员'),
        ('4', '党员')
    )

    STAFF_CHOICE = (
        ('1', '在职'),
        ('2', '离职'),
        ('3', '实习')
    )

    STAFF_TYPE_CHOICE = (
        ('1', '全职'),
        ('2', '兼职')
    )

    name = models.CharField(max_length=10, verbose_name=u'姓名')
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), default='male', verbose_name=u'性别',
                              max_length=6)
    position = models.ForeignKey(Position, verbose_name=u'所属职位', blank=True, null=True, on_delete=models.SET_NULL)
    identity_card = models.CharField(max_length=18, verbose_name=u'身份证', null=True, blank=True, unique=True)
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码', null=True)
    education = models.CharField(choices=EDUCATION_CHOICE, verbose_name=u'学历', default=u'本科', max_length=10)
    political_status = models.CharField(choices=POLITICAL_CHOICE, verbose_name=u'政治面貌', default=u'团员', max_length=10)
    staff_status = models.CharField(choices=STAFF_CHOICE, verbose_name=u'职员状态', default=u'在职', max_length=10)
    staff_type = models.CharField(choices=STAFF_TYPE_CHOICE, verbose_name=u'职员类型', default=u'全职', max_length=5)
    qq = models.IntegerField(verbose_name=u'QQ号', null=True, blank=True)
    email = models.EmailField(verbose_name=u'电子邮箱', null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = u"职员"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
