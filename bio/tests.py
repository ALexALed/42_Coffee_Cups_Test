from django.test import TestCase
from django.test.client import Client
from django.conf import settings
from django.core.urlresolvers import reverse

from models import MyBio
from views import my_bio_view

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
        

        