from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3

class ContactForm(forms.Form):
    email = forms.EmailField()
    feedback=forms.CharField(widget=forms.Textarea)
    capthca = ReCaptchaField(widget=ReCaptchaV3)