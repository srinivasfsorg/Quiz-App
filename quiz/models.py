from django.db import models
from django import forms
from django.utils.html import format_html

# Create your models here.
from django import forms
"""
class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)"""



class QuesModel(models.Model):
    question = models.TextField()
    op1 = models.CharField(max_length=200,)
    op2 = models.CharField(max_length=200,)
    op3 = models.CharField(max_length=200,)
    op4 = models.CharField(max_length=200,)
    #add drop down button below
    ans = models.CharField(max_length=200,) 
    
    def __str__(self):
        return self.question