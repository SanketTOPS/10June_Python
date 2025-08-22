from django import forms
from .models import *

class StudinfoForm(forms.ModelForm):
    class Meta:
        model=Studinfo
        fields='__all__'