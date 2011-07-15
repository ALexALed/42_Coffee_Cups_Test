__author__ = 'aleksey.aledinov'

from django.conf import settings

def add_conf(request):
    return {'settings': settings}