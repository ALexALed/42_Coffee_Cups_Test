__author__ = 'alexaled'

from django import forms

from models import MyBio, HttpRequestSave


class BioForm(forms.ModelForm):
    birth_date = forms.DateField(('%d/%m/%Y',),
                                    label='Birth Date', required=False,
        widget=forms.DateTimeInput(format='%d/%m/%Y', attrs={
            'class': 'input',
            'readonly': 'readonly',
            'size': '15'}))

    class Meta:
        model = MyBio


class HttpEditForm(forms.ModelForm):

    class Meta:
        model = HttpRequestSave
