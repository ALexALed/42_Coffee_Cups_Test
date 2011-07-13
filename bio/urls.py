__author__ = 'aleksey.aledinov'

from django.conf.urls.defaults import patterns, include, url
import views

urlpatterns = patterns('',
                       url(r'^get-bio/$',                views.my_bio_view, name='get_bio'),
                       url(r'^$',                        views.my_bio_view),
                       )