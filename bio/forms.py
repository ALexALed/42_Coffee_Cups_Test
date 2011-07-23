__author__ = 'alexaled'

from django import forms
from models import MyBio, HttpRequestSave
from django.contrib.admin.widgets import AdminDateWidget


class BioForm(forms.ModelForm):
    birth_date = forms.DateField(widget=AdminDateWidget)

    class Meta:
        model = MyBio


class HttpEditForm(forms.ModelForm):

    class Meta:
            model = HttpRequestSave
