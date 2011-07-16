from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin, auth
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^my-bio/', include('Coffee_Cups_Test.bio.urls')),
    url(r'^$',       include('Coffee_Cups_Test.bio.urls')),
    #accounts
    url(r'^accounts/login/$', auth.views.login),
    url(r'^accounts/logout/$', auth.views.logout()),

)
