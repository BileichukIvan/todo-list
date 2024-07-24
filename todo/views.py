from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from todo.models import Task, Tag
from todo.forms import TagForm, TaskForm


class HomePageView(generic.View):
    template_name = "todo/home.html"

    def get(self, request):
        tasks = Task.objects.all().order_by("is_done", "-created_at")
        return render(request, self.template_name, {"tasks": tasks})


def toggle_task_status(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo:home")


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todo:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("todo:home")


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
