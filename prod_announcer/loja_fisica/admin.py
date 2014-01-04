#-*- coding: utf-8 -*-
from django.contrib import admin
from loja_fisica.models import Loja

admin.site.register(Loja, admin.ModelAdmin)

