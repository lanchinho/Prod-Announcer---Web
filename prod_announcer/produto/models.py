# -*- coding: utf-8 -*-
from django.db import models

class Produto(models.Model):
	"""
	Classe responsável por representar um Produto.
	"""

	nome_produto = models.CharField("Nome do Produto", max_length=250)
	fabricante_produto = models.CharField("Fabricante", max_length=250)
	preco_produto = models.DecimalField(max_digits=7 ,decimal_places=2, default=0)
	estoque_produto = models.IntegerField("Quantidade em Estoque")
	foto_produto = models.URLField("Foto do Produto",max_length=250, blank=False)
	info_produto = models.TextField("Informações do Produto", max_length=250)
	em_oferta_produto = models.BooleanField("Produto em Oferta ?", default=False, blank=True)
	#forma_pag_produto

	class Meta:
		verbose_name = "Produto"
		verbose_name_plural = "Produtos"

	def __unicode__(self):
		return "%s - %s - %s - %s -%s - %s - %s" % (self.nome_produto, self.fabricante_produto, self.preco_produto, self.estoque_produto, self.foto_produto, self.info_produto, self.em_oferta_produto)

