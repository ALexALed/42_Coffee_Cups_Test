from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^my-bio/', include('Coffee_Cups_Test.bio.urls')),
    url(r'^$',       include('Coffee_Cups_Test.bio.urls')),
    #accounts
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

)
