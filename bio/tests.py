<<<<<<< HEAD
__author__ = 'alexaled'


=======
>>>>>>> Ticket_1
from django.test import TestCase
from django.test.client import Client
from django.http import HttpRequest
from middleware import HttpRequestMiddleware
from models import HttpRequestSave


from models import MyBio

class TestMyBioModel(TestCase):
    """
    testing model in app bio
    """
    def setUp(self):
        self.my_bio = MyBio.objects.create(
            first_name= "Alex",
            last_name = "Aledinov",
            birth_date= "1986-03-11",
            biography = "My bio",
            contacts = "My contacts",
        )
<<<<<<< HEAD

class HttpRequestTest(TestCase):
    """
    testing http request http middleware   
    """
    def setUp(self):
        self.client = Client()
        self.middleware = HttpRequestMiddleware()
        self.req        = HttpRequest()
        self.req.META['REMOTE_ADDR'] = 'test_ip'
        self.mid_req = self.middleware.process_request(self.req)

    def test_middlew(self):
        req = HttpRequestSave.objects.order_by('-id')[0]
        self.assertEquals(req.remote_addr, self.req.META['REMOTE_ADDR'])
=======
        
>>>>>>> Ticket_1
