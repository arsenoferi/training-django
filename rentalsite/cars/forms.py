from django import forms
from . import models
from django.forms import ModelForm 

# class ReviewFrom(forms.Form):
#     first_name = forms.CharField(label='First Name', max_length=100)
#     last_name = forms.CharField(label='Last Name',max_length=100)
#     email = forms.EmailField(label='Email')
#     review = forms.CharField(label='Please Write Your Review',
#                              widget=forms.Textarea(attrs={'class':'myform', 'rows':5, 'columns':3}))

class ReviewFrom(ModelForm):
    class Meta :
        model = models.Review
        #fields = ['first_name','last_name','stars']
        fields = '__all__'

        labels = {
            'first_name' : "Your First Name",
            'last_name' : "Your Last Name",
        }

        error_messages = {
            'stars':{
                'max_value': 'tolong di isi maksimal 5',
                'min_value': 'rating tidak bisa kurang dari 1'
            }
        }