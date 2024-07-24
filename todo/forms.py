from django import forms

from todo.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["content", "deadline", "is_done", "tags"]
        widgets = {
            "deadline": forms.DateTimeInput(
                attrs={"type": "datetime-local",
                       "class": "form-control"}),
        }
