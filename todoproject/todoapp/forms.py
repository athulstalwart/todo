from django.forms import models

from todoapp.models import Task


class TodoForm(models.ModelForm):
    class Meta:
        model=Task
        fields=['name','priority','date']
