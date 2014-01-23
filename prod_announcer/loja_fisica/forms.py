# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

from prod_announcer.loja_fisica.models import Loja

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password')

class LojaForm(forms.ModelForm):
    """
    Form para o modelo de Loja Fisica
    """
    class Meta:
        model = Loja
        fields = ('nome_loja', 'email_loja', 'site_loja', 'cnpj_loja', 'representante_loja', 'representante_telefone', 'estado_loja', 'cidade_loja', 'bairro_loja', 'cep_loja')