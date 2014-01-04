#-*- coding: utf-8 -*-
from django.contrib import admin
from produto.models import Produto

admin.site.register(Produto, admin.ModelAdmin)
