from django import forms
from django.forms import ModelForm
from emailapp.models import Emails


class EmailsForm(ModelForm):

    class Meta:
        model = Emails

        fields=['email']        

