#-*- coding: utf-8 -*-
from django.contrib import admin
from prod_announcer.produto.models import Produto

admin.site.register(Produto, admin.ModelAdmin)
