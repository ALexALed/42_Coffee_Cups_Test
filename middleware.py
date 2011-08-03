__author__ = 'alexaled'

from bio.models import HttpRequestSave
import datetime


class HttpRequestMiddleware(object):
    def process_request(self, request):
        new_http_req = HttpRequestSave()
        new_http_req.http_request = request.path_info
        new_http_req.remote_addr = request.META['REMOTE_ADDR']
        new_http_req.priority = 0
        new_http_req.datatime = datetime.datetime.now()
        new_http_req.save()
