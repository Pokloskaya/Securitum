from django.db import models
from django import forms

class admin(models.Model):
   name = models.CharField(max_length=15)
   password = models.CharField(max_length=15)

class formAdmin(forms.ModelForm):
   class Meta:
      model = admin
      
      fields = ['name','password']