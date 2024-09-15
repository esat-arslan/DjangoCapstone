from django import forms
from .models import InputForm

class InputModelForm(forms.ModelForm):
    class Meta:
        model = InputForm
        fields = '__all__'