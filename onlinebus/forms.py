from socket import socket

from django import forms
from onlinebus.models import bus,consumer

class busform(forms.ModelForm):
    class Meta:
        model = bus
        fields= '__all__'

class consumerform(forms.ModelForm):
    class Meta:
        model= consumer
        fields='__all__'


class contactform(forms.Form):
    name=forms.CharField(max_length=225)
    age=forms.IntegerField()
    email=forms.EmailField(required=True)
    address=forms.CharField(widget=forms.Textarea)
    contact_no=forms.IntegerField()
    start= forms.CharField()
    end=forms.CharField()
    date=forms.DateField()
    time=forms.TimeField()
    content=forms.CharField(widget=forms.Textarea)