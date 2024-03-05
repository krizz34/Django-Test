from django import forms
from .models import medic

class medicForm(forms.ModelForm):
    class Meta:
        model = medic
        fields = ['Mname','Mdesc','Mstock','Mprice']