from django import forms
from .models import Search, Todo


class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ['search']
        widgets = {
            'search': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Search tasks'})
        }


class TaskForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['task']

        widgets = {
            'task': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Add a new task"
            })
        }
