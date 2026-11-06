from django import forms
from  webapp.models import Todo, Status, Type



class TodoForm(forms.ModelForm):
    status = forms.ModelChoiceField(
        queryset=Status.objects.all(),
        required=True,
        label='Статус'
    )
    type = forms.ModelMultipleChoiceField(
        queryset=Type.objects.all(),
        required=True,
        label='Тип'
    )

    class Meta:
        model = Todo
        fields = ['summary', 'description', 'status', 'type']