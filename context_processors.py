__author__ = 'aleksey.aledinov'


from django.conf import settings


def add_conf_proc(request):
    return {'settings': settings}
