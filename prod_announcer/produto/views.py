# -*- coding: utf-8 -*
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from annoying.decorators import render_to

from prod_announcer.produto.models import Produto
from prod_announcer.loja_fisica.models import Loja

from prod_announcer.produto.forms import ProdutoForm

@login_required
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

def _get_dados_listar_produtos(request,tipo_produto):

    produtos = []
    titulo_produtos = ""
    if tipo_produto == 'produto':
        produtos = request.user.loja.produto_set.all()
        titulo_produtos = "Produtos"

    else:
        raise Http404

    return {'produtos' : produtos, 'titulo_produtos' : titulo_produtos, 'tipo_produto': tipo_produto}

@login_required
@render_to("listagem_produto.html")
def listar_produtos(request, tipo_produto):

    dados_produtos = _get_dados_listar_produtos(request,"produto")
    return dados_produtos


def _get_dados_detalhar_produto(tipo_produto, id_produto):
    titulo_produto = ""
    produto = None
    if tipo_produto == 'produto':
        produto = get_object_or_404(Produto,pk=id_produto)
        titulo_produto = "Produtos"

    else:
        raise Http404

    return {'produto' : produto, 'titulo_produto' : titulo_produto, 'titulo_produto':tipo_produto}

@login_required
@render_to("detalhar_produto.html")
def detalhar_produto(request, tipo_produto, id_produto):

    dados_produto = _get_dados_detalhar_produto(tipo_produto, id_produto)

    return dados_produto

@login_required
def produto_update(request, id_produto, template_name='templates/produto_form.html'):
    produto = get_object_or_404(Produto, pk=id_produto)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('listagem_produto')

    return render(request, template_name, {'form':form})

@login_required
def produto_delete(request, id_produto, template_name='templates/produto_confirm_delete.html'):
    produto = get_object_or_404(Produto, pk=id_produto)    
    if request.method=='POST':
        produto.delete()
        return redirect('listagem_produto')

    return render(request, template_name, {'produto':produto})