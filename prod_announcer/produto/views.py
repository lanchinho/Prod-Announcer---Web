# -*- coding: utf-8 -*
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

from annoying.decorators import render_to

from prod_announcer.produto.models import Produto
from prod_announcer.produto.forms import ProdutoForm

@render_to("cadastro_produto.html")
def cadastrar_produto(request):
    
    if request.method == 'POST':
    	form = ProdutoForm(request.Post)

    	if form.is_valid():
    		form.save()

    		return redirect('sucesso')

    else:
        form = ProdutoForm()

    return {
        'form': form,
    }    		
