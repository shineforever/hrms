# -*- coding: utf-8 -*-
__author__ = 'shine_forever'
__date__ = '2017/7/9 21:05'

import xadmin
from xadmin import views

from .models import Department,Position,Staff


class DepartmentAdmin(object):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['name']


class PositionAdmin(object):
    list_display = ['name','department']
    search_fields = ['name','department__name']
    list_filter = ['name']


class StaffAdmin(object):
    list_display = ['name', 'gender','position','identity_card','mobile','education','political_status','staff_status','staff_type','qq','email']
    search_fields = ['name','identity_card','mobile']
    list_filter = ['name','identity_card','mobile']

xadmin.site.register(Department,DepartmentAdmin)
xadmin.site.register(Position,PositionAdmin)
xadmin.site.register(Staff,StaffAdmin)