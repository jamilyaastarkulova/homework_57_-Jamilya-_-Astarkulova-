from django import forms
from django.forms import widgets
from importlib.metadata import requires
from  webapp.models import Todo, Status, Type



class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['summary', 'description', 'status', 'type']

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

class TypeForm(forms.ModelForm):
    class Meta:
        model = Type
        fields = ['name']
