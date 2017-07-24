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
        (1, '本科'),
        (2, '研究生'),
        (3, '博士')
    )

    POLITICAL_CHOICE = (
        (1, '群众'),
        (2, '团员'),
        (3, '预备党员'),
        (4, '党员')
    )

    STAFF_CHOICE = (
        (1, '在职'),
        (2, '离职'),
        (3, '实习')
    )

    STAFF_TYPE_CHOICE = (
        (1, '全职'),
        (2, '兼职')
    )

    IDENTITY_TYPE_CHOICE = (
        (1, u'身份证'),
        (2, u'居民证')
    )

    GENDER_CHOICE = (
        (1, u'男'),
        (2, u'女')
    )

    # 工号，根据id计算

    name = models.CharField(max_length=10, verbose_name=u'姓名')
    identity_type = models.SmallIntegerField(choices=IDENTITY_TYPE_CHOICE, verbose_name=u'证件类型', default=1)
    identity_card = models.CharField(max_length=18, verbose_name=u'证件号', null=True, blank=True, unique=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1, verbose_name=u'性别')
    position = models.ForeignKey(Position, verbose_name=u'所属职位', blank=True, null=True, on_delete=models.SET_NULL)
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码', null=True)
    education = models.SmallIntegerField(choices=EDUCATION_CHOICE, verbose_name=u'学历', default=1)
    political_status = models.SmallIntegerField(choices=POLITICAL_CHOICE, verbose_name=u'政治面貌', default=1)
    staff_status = models.SmallIntegerField(choices=STAFF_CHOICE, verbose_name=u'职员状态', default=1)
    staff_type = models.SmallIntegerField(choices=STAFF_TYPE_CHOICE, verbose_name=u'职员类型', default=1)
    qq = models.CharField(verbose_name=u'QQ号', max_length=15, null=True, blank=True)
    email = models.EmailField(verbose_name=u'电子邮箱', null=True, blank=True, max_length=100)

    class Meta:
        verbose_name = u"职员"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
