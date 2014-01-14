from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from prod_announcer.produto import views

urlpatterns = patterns('',

	url(r'^cadastro_produto/$', views.cadastrar_produto, name= 'cadastro_produto'),
	url(r'^listagem_produtos/$', views.listar_produtos, name= 'listagem_produtos'),
	url(r'^sucesso/$', TemplateView.as_view(template_name="sucesso.html"), name='sucesso'),
    )
