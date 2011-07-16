from django.db import models

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



class HttpRequestSave(models.Model):
    '''
    HTTP request
    '''
    http_request = models.CharField(max_length=300)
    remote_addr  = models.IPAddressField(blank=True)






