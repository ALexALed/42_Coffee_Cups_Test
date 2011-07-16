from django.db import models

from django.contrib import admin

class MyBio(models.Model):
    '''
    Main model for my bio
        first_name - my first name
        last_name - my last name
        birth_date = my birth date
        biography - my biography text area
        contacts - my contacts area
    '''
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    birth_date = models.DateField()
    biography  = models.TextField(blank=True)
    contacts   = models.TextField()


#register modfels in admin interface
#admin.site.register(MyBio)


