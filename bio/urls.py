__author__ = 'alexaled'

from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns('',
                       url(r'^get-bio/$',                views.my_bio_view,
                                                            name='get-bio'),
                       url(r'^edit-bio/(\d+)/$',         views.edit_data,
                                                        name='edit_bio'),
                       url(r'^edit-bio-reverse/(\d+)/$', views.edit_data,
                               {'reverse': True}, name='edit_bio_reverse'),
                       url(r'^$',                        views.my_bio_view),
                       url(r'^context-proc/$',           views.add_conf,
                                                         name='context-proc'),
                       url(r'^req-list/$',               views.http_view,
                                                         name='req-list'),
                       )
