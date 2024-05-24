from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
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
    


class RegisterPage(FormView):
    template_name = 'base/register.html'
    success_url= reverse_lazy('tasks')
    form_class = UserCreationForm
    redirect_authenticated_user = True


    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form) 

    ## function login is not clear, by the this function is used to restrict user from change page by route  

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect  
        return super(RegisterPage, self).get(*args, **kwargs)

    





## list view
class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'

    ## logic for specific user task
    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        context ['tasks'] = context ['tasks'].filter(user = self.request.user)
        context ['counts'] = context ['tasks'].filter(complete=False).count()


        ## logic for searching bar
       
        search_input = self.request.GET.get("search-area", "").strip()
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        
        context['search_input'] = search_input

         # Debugging output
        # print(f"User: {self.request.user}")
        # print(f"Tasks: {list(context['tasks'])}")
        # print(f"Search input: {search_input}")

        return context
    

## detail view
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'

## create task view
class TaskCreate(LoginRequiredMixin,CreateView):
     model = Task
     fields = ['title','description','complete']
     success_url= reverse_lazy('tasks')

     ## login validate data should login user
     def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate,self).form_valid(form)


## update task view
# class TaskUpdate(LoginRequiredMixin,UpdateView):
#      model = Task
#      fields = ['title','description','complete']
#      success_url= reverse_lazy('tasks')


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        # Set the user for the task
        form.instance.user = self.request.user

        # Call the parent class's form_valid() method
        return super().form_valid(form)

## delete task view
class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url= reverse_lazy('tasks')


## for testing purpose
def new(request):
    return HttpResponse('this is new route')