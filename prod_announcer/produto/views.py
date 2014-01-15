# -*- coding: utf-8 -*
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404

from annoying.decorators import render_to

from prod_announcer.produto.models import Produto

from prod_announcer.produto.forms import ProdutoForm

@render_to("cadastro_produto.html")
def cadastrar_produto(request):
    
    if request.method == 'POST':
    	form = ProdutoForm(request.POST)
    	if form.is_valid():
    		form.save()
    		return redirect('sucesso')

    else:
        form = ProdutoForm()

    return {
        'form': form,
    }    		

def _get_dados_listar_produtos(tipo_produto):

    produtos = []
    titulo_produtos = ""
    if tipo_produto == 'produto':
        produtos = Produto.objects.all()
        titulo_produtos = "Produtos"

    else:
        raise Http404

    return {'produtos' : produtos, 'titulo_produtos' : titulo_produtos, 'tipo_produto': tipo_produto}

@render_to("listagem_produto.html")
def listar_produtos(request, tipo_produto):

    dados_produtos = _get_dados_listar_produtos("produto")
    return dados_produtos

