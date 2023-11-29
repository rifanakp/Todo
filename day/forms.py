from django import forms
from . models import Todo
class Todoform(forms.ModelForm):
    class Meta:
        model=Todo
        fields='__all__'
        labels={
            'title':'Enter your Todo'
            }
