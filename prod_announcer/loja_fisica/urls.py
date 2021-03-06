from django.conf.urls import patterns, url
from django.contrib.auth.forms import AdminPasswordChangeForm
from django.views.generic import TemplateView

from prod_announcer.loja_fisica import views

urlpatterns = patterns('',

        url(r'^cadastro_loja/$', views.cadastrar_loja, name= 'cadastro_loja'),
	url(r'^redefinir_senha/$', views.mudar_senha, name='mudar_senha'),
        url(r'^sucesso/$', TemplateView.as_view(template_name="sucesso.html"), name='sucesso'),
        url(r'^senha_alterada/$', TemplateView.as_view(template_name="senha_alterada_sucesso.html"), name='senha_alterada'),
      
    
	)
