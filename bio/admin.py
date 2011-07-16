__author__ = 'alexaled'

  
import models
from django.contrib import admin


class ModelAdminHttpMidleware(admin.ModelAdmin):
    fields = ( 'http_request', 'remote_addr',)
    list_display = ( 'http_request', 'remote_addr',)


    

#register modfels in admin interface
admin.site.register(models.MyBio)
admin.site.register(models.HttpRequestSave, ModelAdminHttpMidleware)








