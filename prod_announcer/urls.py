from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from prod_announcer.loja_fisica import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'), 

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('prod_announcer.produto.urls')),
    url(r'^', include('prod_announcer.loja_fisica.urls')),
)
