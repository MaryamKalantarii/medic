from .models import NewsLetter,ContactUs
from django import forms


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = ['email']



class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email','subject', 'message']