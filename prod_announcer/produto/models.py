# -*- coding: utf-8 -*-
from django.db import models

class NomeDoProduto(object):

	def get_nome_produto(self):
		return self.nome_produto

class Produto(models.Model, NomeDoProduto):
	"""
	Classe responsável por representar um Produto.
	"""

	nome_produto = models.CharField("Nome do Produto", max_length=250)
	fabricante_produto = models.CharField("Fabricante", max_length=250)
	loja = models.ForeignKey('loja_fisica.Loja', verbose_name="Vendido pela Loja")
	preco_produto = models.DecimalField(max_digits=7 ,decimal_places=2, default=0, verbose_name="Preço")
	estoque_produto = models.IntegerField("Quantidade em Estoque")
	foto_produto = models.URLField("Foto do Produto",max_length=250, blank=False)
	info_produto = models.TextField("Informações do Produto", max_length=250)
	em_oferta_produto = models.BooleanField("Produto em Oferta ?", default=False, blank=True)


	class Meta:
		verbose_name = "Produto"
		verbose_name_plural = "Produtos"

	def __unicode__(self):
		return "%s - %s - %s - %s -%s - %s - %s" % (self.nome_produto, self.fabricante_produto, self.preco_produto, self.estoque_produto, self.foto_produto, self.info_produto, self.em_oferta_produto)



