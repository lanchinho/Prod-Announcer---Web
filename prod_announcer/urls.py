from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'), 
    #isto vai passar para app de loja !!! Provavelmente
    url(r'^trocar_senha/$', TemplateView.as_view(template_name="relogin.html"), name='trocar_senha'), 
    # provavelmente passara a fazer parte da app de loja ! O html vai ser movido pra la no futuro.
    url(r'^admin/', include(admin.site.urls)),

    url(r'^', include('prod_announcer.produto.urls')),
)
