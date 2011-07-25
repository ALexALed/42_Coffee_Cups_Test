__author__ = 'alexaled'

from django import forms

from models import MyBio, HttpRequestSave


class BioForm(forms.ModelForm):
    birth_date = forms.DateField(('%Y-%m-%d',),
                                    label='Birth Date', required=False,
        widget=forms.DateTimeInput(format='%Y-%m-%d', attrs={
            'class': 'input',
            'readonly': 'readonly',
            'size': '15'}))

    class Meta:
        model = MyBio


class HttpEditForm(forms.ModelForm):

    class Meta:
        model = HttpRequestSave
