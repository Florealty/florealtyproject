from django import forms 
from .models import Feed

    
class Feedform(forms.ModelForm):
    class Meta:
        model = Feed
        fields = ['title', 'content']

