from django import forms
from .models import *

class SignupForm(forms.ModelForm):
    class Meta:
        model=UserSignup
        fields='__all__'
        
class UpdateForm(forms.ModelForm):
    class Meta:
        model=UserSignup
        fields=['firstname','lastname','username','password','city','state','mobile']
        
class NotesForm(forms.ModelForm):
    class Meta:
        model=NotesData
        fields=['tech','title','desc','notesfile']

class ContactForm(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'