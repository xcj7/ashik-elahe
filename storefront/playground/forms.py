from django import forms
from .models import MyModel,Login


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['name', 'password']

class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['name', 'age']
