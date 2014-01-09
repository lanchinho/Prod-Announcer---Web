from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',

	url(r'^redefinir_senha/$', TemplateView.as_view(template_name="redefinir_senha.html"), name='redefinir_senha')
	)
