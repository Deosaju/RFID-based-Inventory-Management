from django import forms
from .models import MyData

class MyForm(forms.ModelForm):
    class Meta:
        model = MyData
        fields = ['pid', 'description']
