# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/7/4 10:45'

from hrms.settings.base import *


ALLOWED_HOSTS=['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hrms',    ## 数据库名称
        'USER': 'root',
        'PASSWORD': '!@#QWE',    ## 安装 mysql 数据库时，输入的 root 用户的密码
        'HOST': '127.0.0.1',
    }
}