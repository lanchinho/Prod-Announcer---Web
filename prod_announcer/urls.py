from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="login.html"), name='login'), 

    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^', include('prod_announcer.produto.urls')),
    url(r'^', include('prod_announcer.loja_fisica.urls')),
)
