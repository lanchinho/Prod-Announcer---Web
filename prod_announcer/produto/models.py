from django.db import models

# campos que emulam tipos básicos de SQL

# CharField, TextField, BooleanField, NullBooleanField
# DateField, DateTimeField, TimeField
# IntegerField, SmallIntegerField, AutoField
# DecimalField, FloatField
# campos que acrescentam validações sobre tipos básicos

# EmailField, URLField, IPAddressField, SlugField, XMLField
# PositiveIntegerField, PositiveSmallIntegerField, CommaSeparatedIntegerField
# campos para armazenar arquivos

# FileField, FilePathField, ImageField
# nos três casos, os dados são armazenados no sistema de arquivos, e o campo no banco de dados registra apenas o nome do arquivo ou o caminho


class Produto(models.Model):

	nome_produto = models.CharField("Nome do Produto", max_length=250)
	fabricante_produto = models.CharField("Fabricante", max_length=250)
	preco_produto = models.Model.FloatField("Preço", max_digits=7, decimal_places=2)
	estoque_produto = models.Model.IntegerField("Preço", max_digits=7)
	foto_produto = models.URLField(max_length=250, verify_exists=True, blank=False)
	info_produto = models.TextField("Informações do Produto", max_length=250)
	emOferta_produto = models.BooleanField("Produto em Oferta ?", default=False, blank=True)
	#forma_pag_produto

	def __unicode__(self):
	return "%s - %s - %s - %s -%s - %s - %s" % (self.nome_produto, self.fabricante_produto, self.preco_produto, self.estoque_produto, self.foto_produto, self.info_produto, self.emOferta_produto)

