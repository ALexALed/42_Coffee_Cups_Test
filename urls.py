from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/',  include(admin.site.urls)),
    url(r'^my-bio/', include('bio.urls')),
    url(r'^$',       include('bio.urls')),

    #accounts
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),

    #data widget
    url(r'^jsi18n',  'django.views.i18n.javascript_catalog'),
)
