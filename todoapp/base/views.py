from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Task

# Create your views here.

## for testing purpose
def new(request):
    return HttpResponse('this is new route')


## list view
class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'

## detail view
class TaskDetail(DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

