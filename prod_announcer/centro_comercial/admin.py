#-*- coding: utf-8 -*-
from django.contrib import admin
from prod_announcer.centro_comercial.models import CentroComercial

admin.site.register(CentroComercial, admin.ModelAdmin)

