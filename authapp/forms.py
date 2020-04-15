from django.forms import ModelForm
from .models import inVoice

class createForm(ModelForm):
    class Meta:
        model =inVoice 
        fields ='__all__'
    