from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from django.contrib.auth.views import LoginView
from .models import Task

# Create your views here.

## login view 

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')

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

## create task view
class TaskCreate(CreateView):
     model = Task
     fields = '__all__'
     success_url= reverse_lazy('tasks')


## update task view
class TaskUpdate(UpdateView):
     model = Task
     fields = '__all__'
     success_url= reverse_lazy('tasks')

## delete task view
class TaskDelete(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url= reverse_lazy('tasks')


