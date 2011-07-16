__author__ = 'alexaled'

from django import forms
from models import MyBio
from django.contrib.admin.widgets import AdminDateWidget

class BioForm(forms.ModelForm):
    birth_date = forms.DateField(widget=AdminDateWidget)
    class Meta:
        model = MyBio