from django import forms
from crud.models import Person


class PersonForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    age = forms.IntegerField()
    department = forms.CharField(max_length=50)


class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age', 'email', 'department',]