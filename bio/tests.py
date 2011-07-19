__author__ = 'alexaled'


from django.test import TestCase
from django.test.client import Client

from django.http import HttpRequest
from middleware import HttpRequestMiddleware
from models import HttpRequestSave, MyBio
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.core.management import call_command

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

class ContextProcTest(TestCase):
    """
    testing context proc, which add settings into context
    """
    def setUp(self):
        self.client = Client()
        settings.TEST = 'Test_set'

    def test_resp(self):
        resp = self.client.get("/my-bio/context-proc/")
        self.assertEqual(resp.status_code, 200)

class EditDataViewTest(TestCase):
    """
    Test for edit my data view and login/logout users
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.my_data = MyBio.objects.get(id=settings.TESTS_ID)
        self.my_inform = {
            'first_name' : "Alex",
            'last_name'  : "Aledinov",
            'birth_date' : "1986-03-11",
            'biography'  : "My bio",
            'contacts'   : "My contacts",
        }

    def test_resp(self):
        resp = self.client.get('/my-bio/edit-bio/1/')
        self.assertEqual(resp.status_code, 302)
        self.client.login(username='test', password='test')
        resp = self.client.get('/my-bio/edit-bio/1/')
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, self.my_data.first_name)
        resp = self.client.post('/my-bio/edit-bio/1/', self.my_inform)
        self.assertNotContains(resp, 'This field is required', status_code=302)
        self.my_inform['last_name'] = ''
        self.client.login(username='test', password='test')
        resp = self.client.post('/my-bio/edit-bio/1/', self.my_inform)
        self.assertContains(resp, 'This field is required', status_code=200)
        resp = self.client.get('/my-bio/edit-bio/1/')
        for key, value in self.my_inform.items():
            self.assertContains(resp, value)


class TestMyBioView(TestCase):
    """
    testing view for my bio data
    """
    def setUp(self):
        self.client = Client()
        self.my_info = MyBio.objects.get(id=settings.TESTS_ID)

    def test_resp(self):
        response = self.client.get('/my-bio/get-bio/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.my_info.first_name)
        

class TemplateTagEditAdminTest(TestCase):
    """
    test for admin edit template tag
    """
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('test', 'test@test.com', 'test')
        self.my_data = MyBio.objects.get(id=settings.TESTS_ID)

    def test_resp(self):
        resp = self.client.get('/my-bio/edit-bio/' + str(settings.TESTS_ID) + '/')
        self.assertEqual(resp.status_code, 302)
        self.client.login(username='test', password='test')
        resp = self.client.get('/my-bio/edit-bio/' + str(settings.TESTS_ID) + '/')
        self.assertEqual(resp.status_code, 200)
        self.admintagurl = reverse('admin:%s_%s_change' % (self.my_data._meta.app_label, self.my_data._meta.module_name),
            args=(self.my_data.id,))
        self.assertContains(resp, self.admintagurl)

class CommandsTest(TestCase):
    """
    testing manage commands
    """
    def setUp(self):
        pass

    def test_commands(self):
        self.assertEqual(show_models.Command().handle().count('MyBio34343'), 1)