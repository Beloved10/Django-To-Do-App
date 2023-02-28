from django.contrib.auth.forms import UserCreationForm  
from django.forms import ModelForm
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'date', 'created_by']


    