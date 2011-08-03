from django.db import models
from django.db.models.signals import post_init, post_save, post_delete
import datetime


def signals_init(sender, **kwargs):
    save_signal(sender, 'init')


def signals_save(sender, **kwargs):
    save_signal(sender, 'save')


def signals_delete(sender, **kwargs):
    save_signal(sender, 'delete')


def save_signal(sender, signal):
    if sender.__name__ != 'DbSignals':
        obj = DbSignals()
        obj.model = sender.__name__
        obj.signal = signal
        obj.date = datetime.datetime.now()
        obj.save()

post_init.connect(signals_init, dispatch_uid='Coffee_Cups_test.bio')
post_save.connect(signals_save, dispatch_uid='Coffee_Cups_test.bio')
post_delete.connect(signals_delete, dispatch_uid='Coffee_Cups_test.bio')


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
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    biography = models.TextField(blank=True)
    contacts = models.TextField()


class HttpRequestSave(models.Model):
    '''
    HTTP request
    '''
    http_request = models.CharField(max_length=300)
    remote_addr = models.IPAddressField(blank=True)
    priority = models.IntegerField()
    datatime = models.DateTimeField()


class DbSignals(models.Model):
    """
    table for signals saver
    """
    signal = models.CharField(max_length=50, blank=True)
    model = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(blank=True)
