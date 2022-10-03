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