# -*- coding: utf-8 -*-
from django.db import models
from django.core.validators import RegexValidator

class CentroComercial(models.Model):
    """
    Model responsável por representar uma Loja Física
    """    
    #criar uma app para shopping e vincular  uma loja a um shopping.
    nome_cc = models.CharField("Nome do Centro Comercial", max_length=250)
    idcc = models.IntegerField("id")
        
    class Meta:
        verbose_name_plural = "CComerciais"
        verbose_name = "CComercial"

    def __unicode__(self):
        return "%s - %s" % (self.user.idcc, self.nome_cc)
