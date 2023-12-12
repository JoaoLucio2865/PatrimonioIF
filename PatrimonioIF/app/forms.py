from django import forms
from .models import Predio

class PredioForm(forms.ModelForm):
    class Meta:
        model = Predio
        fields = '__all__'