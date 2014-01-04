#-*- coding: utf-8 -*-
from django.contrib import admin
from prod_announcer.loja_fisica.models import Loja

admin.site.register(Loja, admin.ModelAdmin)

