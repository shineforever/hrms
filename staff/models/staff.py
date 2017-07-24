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
        (2, u'护照')
    )

    GENDER_CHOICE = (
        (1, u'男'),
        (2, u'女')
    )

    MARRIAGE_STATE = (
        (1, u'未婚'),
        (2, u'已婚'),
        (3, u'已婚已育')
    )

    BIRTH_TYPE = (
        (1, u'公历'),
        (2, u'农历'),
    )

    # 工号，根据id计算
    e_number = ''
    # 一级部门，根据职位计算
    dep1 = 1
    # 二级部门，根据职位计算
    dep2 = 2
    # 工龄，根据入职时间计算
    e_age = 3.9

    # 基本信息
    name = models.CharField(max_length=10, verbose_name=u'姓名')
    identity_type = models.SmallIntegerField(choices=IDENTITY_TYPE_CHOICE, verbose_name=u'证件类型', default=1)
    identity_card = models.CharField(max_length=18, verbose_name=u'证件号', null=True, blank=True, unique=True)
    mobile = models.CharField(max_length=11, verbose_name=u'手机号码', null=True)
    marriage = models.SmallIntegerField(choices=MARRIAGE_STATE, verbose_name=u'婚姻状况', default=1)
    birth_type = models.SmallIntegerField(choices=BIRTH_TYPE, verbose_name=u'生日类型', default=1)
    birthday = models.DateField(verbose_name=u'出生日期', null=True)
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1, verbose_name=u'性别')
    people = models.CharField(max_length=11, verbose_name=u'民族', default=u'汉族')
    birthplace = models.CharField(max_length=10, verbose_name=u'籍贯', null=True)

    # 教育状况
    education = models.SmallIntegerField(choices=EDUCATION_CHOICE, verbose_name=u'最高学历', default=1)
    political_status = models.SmallIntegerField(choices=POLITICAL_CHOICE, verbose_name=u'政治面貌', default=1)

    # 在职信息
    staff_status = models.SmallIntegerField(choices=STAFF_CHOICE, verbose_name=u'员工状态', default=1)
    staff_type = models.SmallIntegerField(choices=STAFF_TYPE_CHOICE, verbose_name=u'员工类型', default=1)
    position = models.ForeignKey(Position, verbose_name=u'职位', blank=True, null=True, on_delete=models.SET_NULL)
    is_master = models.BooleanField(verbose_name=u'是否是部门管理者', default=False)
    e_email = models.EmailField(verbose_name=u'工作邮箱', null=True, blank=True, max_length=100)

    # 联系方式
    qq = models.CharField(verbose_name=u'QQ', max_length=15, null=True, blank=True)
    wxid = models.CharField(verbose_name=u'微信', max_length=15, null=True, blank=True)
    email = models.EmailField(verbose_name=u'个人邮箱', null=True, blank=True, max_length=100)
    contact_man = models.CharField(verbose_name=u'紧急联系人', max_length=10, null=True)
    contact_mobile = models.CharField(verbose_name=u'紧急联系人电话', max_length=11, null=True)

    class Meta:
        verbose_name = u"职员"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name
