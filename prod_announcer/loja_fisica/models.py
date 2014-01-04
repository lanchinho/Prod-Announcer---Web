# -*- coding: utf-8 -*-
from django.db import models

class Loja(models.Model):
	"""
	Model responsável por representar uma Loja Física
    """

    nome_loja = models.CharField("Nome da Loja", max_length=250)
    email_loja = models.EmailField("Email da Loja", max_length=250)
    site_loja = models.UrlField("Site", max_length=250, blank=True)
    #Pesquisar como faremos para tratar a imagem da loja, link para a img ou subir a imagem para o banco ?
    login_loja = models.CharField("Nome de Usuário", max_length=250)
    senha = models.CharField("Senha", max_length=14) #estudar uma maneira de como por tamanho minimo
    confirmar_senha = models.CharField("Confirme Sua Senha", max_length=14)
    representante_loja = models.CharField("Representante da Loja", max_length=250)
    representante_telefone = models.CharField("Telefone do Representante", max_length=40)
    estado_loja = models.CharField("Estado", max_length=250)
    cidade_loja = models.CharField("Cidade", max_length=250)
    bairro_loja = models.CharField("Bairro", max_length=250)
    cep_loja = models.CharField("Cep", max_length=250)

    class Meta:
    	verbose_name_plural = "Lojas"
    	verbose_name = "Loja"

    def __unicode__(self):
    	return "%s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s - %s" % (self.nome_loja, self.email_loja, self.site_loja, self.login_loja, self.senha, self.confirmar_senha, self.representante_loja, self.representante_telefone, self.estado_loja, self.cidade_loja, self.bairro_loja, self.cep_loja)
