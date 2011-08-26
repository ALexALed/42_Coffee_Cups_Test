__author__ = 'alexaled'

from django import forms

from models import MyBio, HttpRequestSave


class CalendarWidget(forms.TextInput):

    class Media:
        js = ('/media/js/jquery-1.5.1.min.js',
              '/media/js/jquery.datapick.js')
        css = {'all' : '/media/css/css/jquery-ui-1.8.14.custom.css'}


class BioForm(forms.ModelForm):
    birth_date = forms.DateField(widget=CalendarWidget)

    class Meta:
        model = MyBio


class HttpEditForm(forms.ModelForm):

    class Meta:
        model = HttpRequestSave
