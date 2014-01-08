# -*- coding: utf-8 -*-
from django import forms

from prod_announcer.produto.models import Produto

class ProdutoForm(forms.ModelForm):
	"Form do modelo de Produto"

	class Meta:
		model = Produto
