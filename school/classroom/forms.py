from django import forms 

class ContactForm(forms.Form):
    name = forms.CharField()
    massage = forms.CharField(widget=forms.Textarea())