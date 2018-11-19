from django import forms
from .import models
# CTN = Course taken
class CTN(forms.ModelForm):
    class Meta:
        model = models.Ctcs2
        fields = ['Course_number']
