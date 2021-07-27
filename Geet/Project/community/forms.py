from django.contrib.auth.models import User
from .models import comment
from django import forms                                   # we need form to submit anything in our page

class EmailForm(forms.Form):
    name=forms.CharField(max_length=30)
    email=forms.EmailField()
    to=forms.EmailField()
    comments=forms.CharField(required=False,widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['email','body',]   