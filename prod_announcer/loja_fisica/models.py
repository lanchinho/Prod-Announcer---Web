# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class Loja(models.Model):
    """
    Model responsável por representar uma Loja Física
    """
    "Pesquisar como faremos para tratar a imagem da loja, link para a img ou subir a imagem para o banco ?"
    "estudar uma maneira de como por tamanho minimo"
    
    #user = models.ForeignKey(User)
    nome_loja = models.CharField("Nome da Loja", max_length=250)
    email_loja = models.EmailField("Email da Loja", max_length=250)
    site_loja = models.URLField("Site", max_length=250, blank=True)
    cnpj_loja = models.CharField("CNPJ",max_length=20, validators=[RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}\/\d{4}\-\d{2}$', message='CNPJ Inválido'),])
    representante_loja = models.CharField("Representante da Loja", max_length=250)
    representante_telefone = models.CharField("Telefone do Representante", max_length=15, validators=[RegexValidator(regex=r'^\((10)|([1-9][1-9])\)[2-9][0-9]{3}-[0-9]{4}|[2-9][0-9]{4}-[0-9]{4}$', message='Número de Telefone Inválido'),])
    estado_loja = models.CharField("Estado", max_length=250)
    cidade_loja = models.CharField("Cidade", max_length=250)
    bairro_loja = models.CharField("Bairro", max_length=250)
    cep_loja = models.CharField("Cep", max_length=10, validators=[RegexValidator(regex=r'^[0-9]{5}-[0-9]{3}$', message='CEP Inválido'),])

    class Meta:
        verbose_name_plural = "Lojas"
        verbose_name = "Loja"

    def __unicode__(self):
        return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.nome_loja, self.email_loja, self.site_loja, self.cnpj_loja, self.senha, self.representante_loja, self.representante_telefone, self.estado_loja, self.cidade_loja, self.bairro_loja, self.cep_loja)
