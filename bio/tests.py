from django.test import TestCase


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
        