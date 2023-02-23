from django import forms
from .models import Gadgets
class GadgetsForm(forms.ModelForm):
    class Meta:
        model=Gadgets
        fields=['title','desc','price','image']