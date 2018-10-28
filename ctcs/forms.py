from django import forms
from .import models

class RegTime(forms.ModelForm):
    class Meta:
        model = models.Ctcs
        fields = ['Registration_year', 'Registration_semeter']
class Major(forms.ModelForm):
    class Meta:
        model = models.Ctcs
        fields = ['major']
