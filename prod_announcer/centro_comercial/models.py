# -*- coding: utf-8 -*-
from django.db import models

class CentroComercial(models.Model):
    """
    Model responsável por representar um Centro Comercial
    """ 
 
    centro_comercial = models.CharField("Nome do Centro Comercial:", max_length=250)

    class Meta:
        verbose_name_plural = "Centros Comerciais"
        verbose_name = "Centro Comercial"

    def __unicode__(self):
        return self.centro_comercial
