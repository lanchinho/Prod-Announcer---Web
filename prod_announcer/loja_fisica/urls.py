from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from prod_announcer.loja_fisica import views

urlpatterns = patterns('',

        url(r'^cadastro_loja/$', views.cadastrar_loja, name= 'cadastro_loja'),
	url(r'^redefinir_senha/$', TemplateView.as_view(template_name="redefinir_senha.html"), name='redefinir_senha'),
        url(r'^sucesso/$', TemplateView.as_view(template_name="sucesso.html"), name='sucesso'),
	)
