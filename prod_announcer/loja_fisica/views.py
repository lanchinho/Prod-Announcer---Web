# -*- coding: utf-8 -*
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, get_object_or_404

from annoying.decorators import render_to

from prod_announcer.loja_fisica.forms import UserForm, LojaForm

@render_to("cadastro_loja.html")
def cadastrar_loja(request):

	registered = False

	if request.method == 'POST':
		user_form = UserForm(request.POST)
		loja_form = LojaForm(request.POST)

		if user_form.is_valid() and loja_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()
			loja = loja_form.save(commit=False)
			loja.user = user
			loja.save()

			registered = True

			return redirect('sucesso')

	else:
		user_form = UserForm()
		loja_form = LojaForm()

	return{
	    'user_form': user_form, 'loja_form': loja_form, 'registered': registered
	}	

@render_to("login.html")
def user_login(request):

	if request.method == 'POST':
	   username = request.POST['username']
	   password = request.POST['password']

	   user = authenticate(username=username, password=password)

	   if user is not None:
	   	  if user.is_active:
	   	  	  login(request, user)
	   	  	  return redirect('cadastro_produto')
	   	  else:
	   	  	  return HttpResponse("Sua conta Prod-Announcer encontra - se desativada")
	   else:
	       print "Informações de Login inválidas: {0}, {1}".format(username, password)
	       return HttpResponse("As informações de login fornecidas são inválidas!")
	else:
		return{
		}    

@login_required		 	  
def user_logout(request):
	logout(request)

	return redirect('index')

@login_required
@render_to("redefinir_senha.html")
def mudar_senha(request):

	if request.method == 'POST': 
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']
		user = request.user

		if password == confirm_password and user is not None:
			user.set_password(confirm_password)
			user.save()
			return redirect('sucesso')

		else:
			return HttpResponse("Erro ! As senhas digitadas não são iguais")
	else:
		return locals()









