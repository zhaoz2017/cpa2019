from django import forms
from .import models

class RegInfo(forms.ModelForm):
    class Meta:
        model = models.Ctcs
        fields = ['Registration_year', 'Registration_semester', 'major']
